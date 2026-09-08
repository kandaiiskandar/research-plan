# Finding: `g_t` Evidence Closure and Specification Decision Record

**Date:** 2026-09-08 · **SDR-001 approved 2026-09-08**
**Status:** **Evidence closure + SDR-001 — APPROVED, NOT YET APPLIED.** *(Was: DRAFT decision record. Approved 2026-09-08 on the readiness verdict READY WITH EXECUTION CONDITIONS, with C-0 closed.)*

> **⚠️ APPROVAL IS A DESIGN DECISION, NOT A MIGRATION.** Model B is the **selected replacement design** for `g_t`. **It is not canonical and not in effect.** The incumbent fixed-clock `g_t` (06:00 / 17:00 / 19:00) remains the canonical and runtime specification, and **7.72% / 5.98% remain the authoritative published figures**. Canonical `g_t`, Appendix C, canonical scripts, `solar.py`, replay outputs, figures and the prediction register (24 predictions, 22 CONFIRMED / 2 REFUTED) are all **unmodified**. No prediction re-resolved. **C-1 through C-8 remain OPEN and are binding on migration** — Part 6.

**Predecessors:** `finding-gt-provenance-audit.md` · `finding-gt-operational-semantics.md` · `finding-gt-sensitivity-analysis.md`
**Approval chain:** `finding-unsafe-semantics-audit.md` → `cleanup-report-unsafe-semantics-2026-09-08.md` → `finding-sdr-001-readiness-audit.md` → `cleanup-report-c0-solar-provenance-2026-09-08.md` → `approval-report-sdr-001-2026-09-08.md`

---

## Part 1 — Authoritative solar provenance

### 1.1 Candidate sources assessed

> **⚠️ Read this table as a survey of *external* candidate sources — not as a description of the local implementation.** *(Guard added 2026-09-08, C-0.)* The columns below characterise USNO, the NOAA GML web calculator, Meeus and the Malaysian agencies **as published artefacts**. In particular, the NOAA column's statement that *"NOAA states it implements the Meeus formulae"* is a report of NOAA's description **of its own web calculator**. It says nothing about `scripts/sensitivity/solar.py`, and it must not be chained into an inference that the local code is Meeus-derived. **No project evidence establishes that equivalence.** The local implementation is described in Part 2 and in the Decision clause of Part 6.

| | **USNO Astronomical Applications** | **NOAA GML Solar Calculator** | **Meeus, *Astronomical Algorithms*** | MET Malaysia / JUPEM / Falak network |
|---|---|---|---|---|
| **Institution** | U.S. Naval Observatory, Astronomical Applications Department | NOAA Global Monitoring Laboratory (U.S. Dept of Commerce) | Willmann-Bell (formally published monograph) | Malaysian government agencies |
| **Algorithm / service** | JSON REST API `rstt/oneday`, **v4.0.1**; also one-day and one-year HTML tables. Backed by USNO's own ephemeris | Web calculator; NOAA states it implements the Meeus formulae | Low-precision solar formulae, Ch. 15 (rising/setting) and Ch. 25 (solar position) | Falak observatories (e.g. Al-Biruni, Tanjung Dumpil, Putatan) support **prayer-time determination** |
| **Required inputs** | date, lat, lon, tz | date, lat, lon, tz | date, lat, lon, tz | — |
| **Historical dates** | ✅ Yes. *USNO notes it does not track historical time-zone changes* — irrelevant here: Malaysia's UTC+8 is unchanged across 2020–2024 | ✅ Yes | ✅ Yes, unbounded | — |
| **Offline reproducible** | ❌ **No** — network service; 1,827 daily requests for the replay period | ⚠️ Partially — the algorithm is republishable, the calculator is not | ✅ **Yes** — a published algorithm, implementable anywhere | — |
| **Precision** | Sub-minute; the reference standard here | ~1 min for \|lat\| < 72° | ~1 min for \|lat\| < 72° | — |
| **Citation suitability** | ✅ **Excellent** — government astronomical authority, versioned API | ✅ Good — government source, but cites Meeus rather than being primary | ✅ **Excellent** — the standard formally published reference | ❌ **Not applicable** |
| **Limitation** | Network dependency; no guarantee of long-term API stability; requires caching for reproducibility | Not itself primary; web calculator not archivable | Not an authority on *values*, only on *method*; needs validation against an authority | **No general sunrise/sunset ephemeris service located.** The falak network serves Islamic prayer times, not maritime operations |

### 1.2 Malaysian source — searched, not found

**No MET Malaysia or JUPEM astronomical service publishing sunrise/sunset for arbitrary dates and coordinates was located.** Malaysia's official astronomical infrastructure is the *falak* observatory network, whose remit is Islamic prayer-time determination.

This is consistent with the pattern already established in `finding-met-lower-boundary-gap.md`: **MET publishes hazard warnings, not operating parameters.** A sunrise table is neither. The absence is structural, not an oversight, and it is recorded as a negative search result rather than proof of non-existence.

### 1.3 Recommended provenance model — **two-source**

> **Method:** a formally published solar-position algorithm, implementable offline, citable, and reproducible without network access.
>
> **Authority:** **USNO Astronomical Applications API v4.0.1** — used to *validate* the implementation at documented reference dates, with the validation result recorded in the specification.

> **⚠️ Amended 2026-09-08 (C-0).** This subsection originally named **Meeus, *Astronomical Algorithms* (2nd ed., Willmann-Bell, 1998)** as the method. **That was a recommendation, not a description of what was built** — and the gap between the two is what produced the C-0 defect: the SDR's Decision clause then asserted Meeus as though it had been implemented and validated, when the validated code is the NOAA-style formulation in `solar.py` (Part 6).
>
> **The two-source structure stands; only the method slot changes.** Separating *how values are computed* from *what certifies them* remains right, and mirrors the wave thresholds (Yaakob supplies the method's evidence; NORDFORSK certifies the criteria). What is corrected is that the method slot must name **the implementation actually in use and actually validated**, not a preferred alternative.
>
> **Meeus remains a legitimate future option** — it is more accurate and more securely citable, and adopting it would be a reasonable C-1 decision. But it would require **re-running the 28-comparison USNO validation against the new implementation**, because the existing 0.9-min result does not transfer. It was not implemented here, precisely because evidence must follow implementation.

This separates *how values are computed* from *what certifies them*, which is the same structure already used for wave thresholds (Yaakob supplies the method's evidence; NORDFORSK certifies the criteria). It satisfies both requirements: offline reproducibility for a 1,827-day replay, and an authoritative citation.

**Commercial sunrise/sunset websites are excluded as authority.** timeanddate.com appears in the earlier findings only as an informal cross-check; it is superseded here by USNO and should not be cited in the specification.

---

## Part 2 — Validation result

> ### ⚠️ Two distinct evidence objects — read this before using any number below
>
> *(Added 2026-09-08 on closure of C-2. **Nothing in this Part has been overwritten.**)*
>
> | | |
> |---|---|
> | **V_historical** — everything in this Part as originally written | **Retained for provenance.** Status: **historically reported, underlying comparison artefact unavailable.** The 28 per-event reference values were never stored, so the 0.90 / 0.37 summaries **cannot be independently reproduced from current project artefacts**. They are not withdrawn and are not alleged to be wrong — the row-level evidence simply does not exist |
> | **V_reconstructed** — `data/solar/usno-validation-2026-09-08.csv` | **The authoritative reproducible validation record for SDR-001 going forward.** A controlled re-query of USNO API v4.0.1 on 2026-09-08 at the canonical coordinate **5.98° N, 116.01° E**. 28 rows, every statistic recomputable from the table itself |
>
> **V_reconstructed supersedes V_historical for reproducibility only. It does not replace it as a record of what was reported at the time.** See `report-c2-closure-2026-09-08.md`.

Local implementation — the **NOAA-style low-precision solar-position formulation in `scripts/sensitivity/solar.py`** — checked against **USNO API v4.0.1**, 5.98° N, 116.07° E, tz = +8.

*Corrected 2026-09-08 (C-0): previously written "NOAA/Meeus formulae". **That hybrid is not supportable** — NOAA-published solar material and Meeus's* Astronomical Algorithms *are distinct methods, no project source establishes their equivalence, and the code implements neither under that joint name. What follows validates the implementation named above and nothing else.*

> **Longitude — RESOLVED under C-1 on 2026-09-08. The canonical coordinate is 5.98° N, 116.01° E.** The comparisons *in this Part* were run at **116.07° E**, the old `solar.py` default, which is retained above as the historical record. **116.07 has no demonstrated provenance** — it matches neither the requested site coordinate (116.01, declared in all three collection scripts and in `data-provenance.md`) nor any delivered grid cell (116.025 / 116.0 / 116.04167). Environmental providers snap independently to different cells, so no single cell can represent the site; **solar events describe the study location, not any one provider's grid centroid**. The 0.06° difference is 0.24 min (14 s) of solar time, applied uniformly to every event. **V_reconstructed uses 116.01.** See `report-c1-c2-c3-solar-reproducibility-2026-09-08.md` §1–§2.

**7 dates × 4 events = 28 comparisons**, chosen to include all four annual extremes:

| Date | Selected because | Max \|diff\| across 4 events |
|---|---|---|
| 2024-02-02 | **annual latest sunrise** (06:33) | 0.8 min |
| 2024-03-20 | March equinox | 0.9 min |
| 2024-05-24 | **annual earliest sunrise** (06:00) | 0.7 min |
| 2024-06-21 | June solstice | 0.7 min |
| 2024-07-17 | **annual latest sunset** (18:35) | 0.4 min |
| 2024-11-11 | **annual earliest sunset** (17:56) | 0.8 min |
| 2024-12-21 | December solstice | 0.8 min |

> ### **V_historical — as reported at the time: maximum absolute difference 0.9 minutes, mean 0.37 minutes.**
> **Sunrise/sunset only (the events Model B uses): max 0.9 min, mean 0.35 min.**
>
> ⚠️ *Status (2026-09-08, C-2): **historically reported, underlying comparison artefact unavailable.** The 28 per-event values behind these summaries were never stored and cannot be recovered. Retained unchanged as the record of what was reported; **not** to be cited as reproducible evidence.*

> ### **V_reconstructed — the reproducible record, from `data/solar/usno-validation-2026-09-08.csv`**
>
> Recomputed **from the 28 stored rows only**, at the canonical coordinate 5.98° N, **116.01° E**, implementation `solar-v1` (`sha256 3b7dc371…c36c`):
>
> | Subset | n | Max | Mean | Median | Min |
> |---|---|---|---|---|---|
> | **All events** | 28 | **0.92 min** | **0.38 min** *(0.3786)* | 0.39 | 0.01 |
> | **Sunrise/sunset — the events Model B uses** | 14 | **0.75 min** | **0.33 min** *(0.3321)* | 0.33 | 0.01 |
> | Civil dawn/dusk — computed, unused by Model B | 14 | 0.92 min | 0.43 min *(0.4250)* | 0.42 | 0.03 |
>
> **All 28 comparisons agree within one minute.** Mean signed difference **+0.0064 min** — no systematic bias. **The 0.92 max is a civil-dusk event; across the sunrise/sunset events Model B actually depends on, the worst disagreement is 0.75 min.**
>
> *Reported to 2 d.p.; full precision preserved in the artefact. Values are **not** rounded to agree with V_historical.*

### 2.1 A caveat the validation alone does not settle

At **hourly** data resolution a sub-minute difference is almost always immaterial — but not unconditionally. It can flip a classification only when a solar boundary falls within 0.9 min of an hour mark. Over the 1,827-day replay period:

| | Days with boundary within 1 min of an hour mark | Within 2 min |
|---|---|---|
| Sunrise | **160** | 335 |
| Sunset | **60** | 125 |

**Closest approach: 0.02 min.** So implementation choice *can* change the classification of individual hours on roughly 220 of 1,827 days, though the expected number of actual flips is far smaller (the difference must exceed the gap, and both must fall the same side).

**Consequence for the decision:** this does not undermine Model B, but it means **the implementation must be pinned and its validation recorded**, not treated as interchangeable with any other solar routine. A future re-implementation differing by one minute would produce slightly different figures — exactly the class of silent drift the recomputation rule exists to prevent.

*Per instruction, the canonical model is unchanged on the basis of this validation alone.*

---

## Part 3 — Model B semantics: confirmed, with one wording correction

**Proposed:**

```
             ⎧ SAFE     sunrise(date, lat, lon) ≤ t < sunset(date, lat, lon)
    g_t(t) = ⎨
             ⎩ UNSAFE   otherwise
```

| Proposed wording | Assessment |
|---|---|
| SAFE corresponds to operation during the daylight interval defined by sunrise and sunset | ✅ **Supported.** Matches COLREGs Rule 20(b)'s complement and the study's daytime baseline |
| UNSAFE corresponds to the night interval governed by the sunset-to-sunrise distinction | ⚠️ **Supported only under the governance reading** — see below |
| `g_t` has no CAUTION output because no evidence supports a separate twilight-risk state | ✅ **Supported.** No source found in three reviews |

### 3.1 The wording correction

**Darkness does not prove physical unsafety, and the specification must not say it does.** Atacan & Düzbastılar establish *elevated risk*, not impossibility; fishers demonstrably operate at night. A claim that night is physically unsafe would be false on its face.

**The claim is admissible only because UNSAFE in this architecture means governance admissibility, not physical impossibility.** `S = UNSAFE` sets `G(S) = 0` and `A_AI(S) = ∅` — *the AI does not advise* — and says nothing about whether the human may depart. C.7 already establishes human override as unconditional.

**Required wording, if adopted:**

> `g_t` = UNSAFE during the night interval (sunset to sunrise) denotes that **AI advisory participation is not admissible**, on the grounds that the conditions under which the advisory model's environmental inputs and recommendation types were validated do not obtain. It does **not** assert that departure is physically unsafe, and it does not restrict the operator.

This is the same correction already applied to Definition C.1's severity ordering in the claim sweep ("outside the demonstrated operating envelope", not "not survivable"). **Consistency requires it here too.**

---

## Part 4 — Architectural compatibility: **confirmed, no dependency found**

**Claim to verify:** `g_t : X_t → {SAFE, UNSAFE}` can participate in `S = max(g_w, g_r, g_m, g_o, g_t)` with `S ∈ {SAFE, CAUTION, UNSAFE}`.

**Verified. The architecture never requires any `gᵢ` to be surjective.**

| Check | Result |
|---|---|
| **Type declarations** (`gᵢ : Xᵢ ∪ {⊥} → {SAFE, CAUTION, UNSAFE}`, C.2, C.8.1) | ✅ Declare the **codomain**, not the image. A function into a three-element set need not hit all three. `g_t` two-state is a well-typed member of this signature |
| **max-severity** (C.2, Theorem C.1 part ii) | ✅ *"takes a tuple ∈ {SAFE, CAUTION, UNSAFE}⁵ and returns the element greatest under ≻… ≻ is a total strict order on a finite set."* Depends only on the order, never on which values occur |
| **Theorem C.1 (Totality)** | ✅ Requires each `gᵢ` **total on its domain**, not surjective onto the codomain. The `g_t` case argues only that its intervals partition [0, 24) exhaustively — a two-interval partition satisfies this identically |
| **Theorem C.1b (Operational Totality)** | ✅ Case analysis is over `Xᵢ ∪ {⊥}`, unaffected by image size |
| **Theorem C.2 (Monotonicity)** | ✅ Operates on `A_AI(S)` set definitions; does not reference any `gᵢ` |
| **Theorem C.3 (Safety Dominance)** | ✅ Case analysis is on the **value of S**, never on how S arose (restated in the consistency pass) |
| **`G(S)`, `A_AI(S)`** (C.3, C.4) | ✅ Defined on `S`, not on any `gᵢ`. CAUTION remains reachable via `g_o` and `g_r` |
| **Lemma C.1c** (monotone degradation) | ✅ Requires only that pinning uses the least element of ≻ |

**No theorem, type declaration or proof assumes surjectivity. Searched: `surject`, `onto {SAFE`, `all three states`, `every gᵢ`. Zero hits.**

### 4.1 The one thing that would need changing

**Prose, not formalism.** Appendix C's `g_t` presentation is written as a three-row table alongside the other components, and the C.1 note describes "three safety zones". Neither is a formal dependency, but both would read as inconsistent beside a two-state `g_t`. **A short statement that component classifiers need not be surjective, and that `g_t` is deliberately binary, would prevent this being read as an error.**

**Empirical confirmation:** the sensitivity analysis ran Model B end-to-end and produced a valid three-state distribution — SAFE 42.02%, **CAUTION 4.77%**, UNSAFE 53.21%. CAUTION remains reachable; it becomes purely weather-driven.

---

## Part 5 — `cause` semantics: **a genuine mismatch, reported separately**

**Current:** `cause : Y → {fault, hazard}` (C.2.0.8), where `fault` means some `yᵢ = ⊥` and `hazard` means everything else.

**Under Model B, a sunset-driven UNSAFE would be classified `hazard`.** That is **not** correct, and the mismatch is sharper than under the incumbent.

| | Weather UNSAFE (`g_o` > 1.25 m) | Time UNSAFE (Model B, after sunset) |
|---|---|---|
| Arises from | A measured environmental condition | A **deterministic astronomical fact** |
| Predictable | No | **Yes — to the minute, years ahead** |
| Actionable by waiting | Sometimes | **Always, and the wait time is known exactly** |
| Is it a "hazard"? | Yes | **Questionable.** Sunset is not a hazard; it is a scheduled condition under which the advisory model is not validated |

**Why Model B sharpens it.** Under the incumbent, `g_t`'s boundaries were arbitrary clock times that could loosely be read as proxying a hazard. Under Model B the boundary is explicitly astronomical, and calling *sunset* a hazard is plainly wrong.

**Assessment: this exposes a real semantic gap, but it does not block the decision.**

- `cause` is **provenance only** — C.2.0.8 states it has no effect on `G(S)` or `A_AI(S)`. No formal property depends on it.
- The mismatch is **already latent** under the incumbent; Model B makes it visible rather than creating it.
- **A third `cause` value (e.g. `scheduled`) is not introduced here.** Per instruction it is reported, not adopted. It would be a small, self-contained change, and the case for it is that an operator log reading *"UNSAFE — hazard"* every night at sunset is misleading in the same way `⊥`-driven UNSAFE would be.

**Recommendation: treat as a separate decision, sequenced after the `g_t` decision, not bundled into it.**

---

## Part 6 — Specification Decision Record — **APPROVED, NOT YET APPLIED**

> ### SDR-001 — `g_t`: fixed-clock three-state → solar-event two-state
>
> # **Status: APPROVED — NOT YET APPLIED**
>
> | | |
> |---|---|
> | **Status** | **APPROVED — NOT YET APPLIED** |
> | **Approved** | 2026-09-08 |
> | **Prior status** | DRAFT — NOT APPROVED — NOT APPLIED (superseded 2026-09-08) |
> | **Decision type** | Design decision — selects the replacement design for `g_t` |
> | **Canonical status** | ❌ **NOT canonical.** The incumbent fixed-clock `g_t` remains the canonical and runtime specification |
> | **Approval basis** | `finding-sdr-001-readiness-audit.md` — verdict **READY WITH EXECUTION CONDITIONS**; **C-0 CLOSED** (`cleanup-report-c0-solar-provenance-2026-09-08.md`) |
> | **Blocking conditions** | **C-1 … C-8 — all OPEN.** See "Execution conditions" below |
>
> ### 🚧 MIGRATION GATE
>
> > # **APPROVAL DOES NOT AUTHORISE CANONICAL MIGRATION.**
> >
> > Canonical migration may begin **only** through a separate controlled task that explicitly executes **C-1 through C-8**. Until that migration completes:
> >
> > **`g_t^canonical` = `g_t^incumbent`** — SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE otherwise
> >
> > **The currently published figures therefore remain authoritative and must continue to be reported:**
> >
> > | | |
> > |---|---|
> > | **PRIMARY Level 2 binding** | **7.72%** |
> > | **RESOLUTION Level 2 binding** | **5.98%** |
> >
> > **The Model B sensitivity values (5.81% / 4.48%) are counterfactual and must not replace them.** They were produced by non-canonical analysis code and remain hypothetical until migration completes.
>
> ### What this approval does and does not establish
>
> **Establishes:** Model B is the **selected replacement design** for the time component `g_t`. The design question — *should `g_t` be graduated at all?* — is answered **no**, on the evidence and reasoning below. No further design deliberation is required; what remains is execution.
>
> **Does not establish:** any change to the runtime or canonical specification, to any published figure, to any prediction outcome, or to Appendix C. **Approval sets direction, not state.**

### Decision

Replace the fixed-clock three-state `g_t` with a solar-event two-state classifier — **on approval as the target design; not applied to Appendix C or any canonical script by this approval**:

```
g_t : [0, 24) ∪ {⊥} → {SAFE, UNSAFE}

             ⎧ SAFE     sunrise(date, φ, λ) ≤ t < sunset(date, φ, λ)
    g_t(t) = ⎨ UNSAFE   otherwise
             ⎩ UNSAFE   t = ⊥
```

**`g_t` is deliberately binary.** It produces no CAUTION output, and this is an approved design position rather than an omission: no source located in three separate reviews supports a time-based intermediate state (Part 1, `finding-gt-operational-semantics.md` §6).

**The architecture remains three-state.** `𝒮 = {SAFE, CAUTION, UNSAFE}` is unchanged, and CAUTION remains materially reachable — under Model B the PRIMARY replay still yields **2,091 CAUTION hours (4.77% of all hours)**, every one produced by `g_o` or `g_r`. **Component classifiers are not required to be surjective**: type declarations state a codomain, not an image; Theorem C.1 requires each `gᵢ` to be *total*, not onto; and C.2, C.3, `G(S)` and `A_AI(S)` never reference component structure (Part 4; `finding-unsafe-semantics-audit.md` §3). Documenting this explicitly in Appendix C is **C-4**.

Sunrise and sunset computed per (date, latitude, longitude) by the **NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`** (`solar-v1`, sha256 `3b7dc371…c36c`) at the canonical study coordinate **5.98° N, 116.01° E**, UTC+8 — specification `solar-spec-v1`.

**Validation statement** *(revised 2026-09-08 on closure of C-2)*:

> The local solar implementation was **historically reported** as agreeing with **USNO API v4.0.1** within **0.90 min** maximum absolute deviation and **0.37 min** mean absolute deviation over 28 comparisons. **The original row-level validation artefact was not preserved**, so those summaries are not independently reproducible from current project artefacts.
>
> A **reproducible reconstruction on 2026-09-08** at the canonical study coordinate (5.98° N, 116.01° E) produced, over the same 7 dates × 4 events: **maximum absolute deviation 0.92 min, mean 0.38 min** (0.3786), median 0.39 min; and for the **sunrise/sunset events Model B actually uses**, **maximum 0.75 min, mean 0.33 min** (0.3321). All 28 comparisons agree within one minute, with mean signed difference +0.0064 min.
>
> **The frozen 28-row artefact `data/solar/usno-validation-2026-09-08.csv` is the authoritative validation record used for reproducibility going forward.** It is labelled `RECONSTRUCTED-2026-09-08` and is **not** the original run.

**USNO is the independent astronomical reference against which the local implementation was checked. It is not the source of the algorithm, and no claim is made that USNO uses this or any particular formulation.**

> **⚠️ C-0 correction, 2026-09-08 — algorithm provenance.** This clause previously read *"by the **Meeus** algorithm, validated against USNO API v4.0.1"*. **That was wrong: the implementation validated at 0.9 min is not Meeus.** `solar.py` computes solar declination and the equation of time from a truncated Fourier series in the day angle `Γ = 2π(doy−1)/365` — a low-precision formulation of the kind reproduced in NOAA solar-calculation material. Meeus, *Astronomical Algorithms* (2nd ed., 1998) is a structurally different method built on a Julian-century time argument, geometric mean longitude, mean anomaly, equation of centre and apparent obliquity; **none of those constructs appears in the code.** Approving the clause as previously drafted would have authorised an algorithm this project has never validated.
>
> **The implementation was preserved and the wording corrected — evidence follows implementation, not the reverse.** Meeus was not implemented merely to rescue the prior wording. The validation figures are unchanged and were not recomputed; only the question of *what they validate* is corrected.
>
> **Remaining citation gap — C-1, not C-0.** The exact published reference for this formulation is not yet pinned. The code's own docstring attributes it to *"NOAA Global Monitoring Laboratory solar calculator equations (Astronomical Almanac low-precision formulae)"*, which names two distinct sources, and the coefficient set matches neither exactly as documented in this project. The conservative wording above is used deliberately until a specific published rendering is identified and cited. See C-1.

### Approval rationale — evidence and policy separated

**This separation is load-bearing and must be preserved wherever the decision is described.**

#### What the evidence establishes

| Claim | Source |
|---|---|
| **Night navigation carries elevated operational risk** — accident probability 4.08 vs 3.43, consequence 12.80 vs 8.53, relative to a daytime baseline | Atacan & Düzbastılar (2023) |
| **COLREGs Rule 20(b) provides an authoritative maritime sunset-to-sunrise boundary** — for the purpose of **navigation-light requirements** | COLREGs Rule 20(b), binding on these vessels |
| **The incumbent thresholds 06:00 / 17:00 / 19:00 lack direct evidential support** — no source in the corpus or in any standard searched across five priority tiers states any of the three values | `finding-gt-provenance-audit.md` |
| **No evidence supports the incumbent 17:00–19:00 CAUTION band** — the study tested no twilight condition; COLREGs has no intermediate state; no corpus paper reports a graded dusk risk profile | Three independent reviews |

#### What architecture policy decides

> **night-time ⇒ `g_t` = UNSAFE ⇒ AI advisory abstention**

**This implication is an architectural governance policy choice. No source establishes it.**

- **COLREGs Rule 20(b) does not require AI abstention.** It regulates when navigation lights must be exhibited. It is used here **only** as the authoritative definition of the sunset-to-sunrise boundary, not as a warrant for withdrawing decision support.
- **Atacan & Düzbastılar do not require AI abstention.** They establish elevated risk in a bridge-simulator study of accident perception. They say nothing about advisory systems.
- **Neither source establishes that night operation is physically prohibited or universally unsafe**, and this record makes no such claim. Small-scale fishers demonstrably operate at night. `S = UNSAFE` sets `G(S) = 0` and `A_AI(S) = ∅` — *the AI does not advise* — and **human decision authority remains unconditional** (Definition C.1 as revised; C.8.2 step 6).

**The policy is nonetheless defensible, and is approved as policy.** It follows the architecture's stated design principle of conservative over-approximation (C.1, Worst-Case Aggregation Justification Note), and the project already carries `UNSAFE` boundaries set on interpretive or design grounds and labelled as such (C.9.1). What is *not* permitted is presenting it as an evidential finding. **The incumbent `g_t` is equally policy-defined, with strictly worse provenance** — it is policy resting on unsourced numbers, where Model B is policy resting on a regulated boundary.

### Rationale

1. **The incumbent boundaries have no provenance.** No source in the corpus or in any searched standard states 06:00, 17:00 or 19:00.
2. **The cited night-navigation evidence defines no clock boundary.** Atacan & Düzbastılar tested "night navigation" as one of six *simulator scenarios*; the paper contains no clock times and could not, given its design.
3. **Restricted-visibility evidence was incorrectly transferred to the time variable.** The 7.90 score cited in Appendix C is the *restricted visibility (100 m)* scenario, not the *night* scenario (4.08 / 12.80). The study and COLREGs both treat darkness and restricted visibility as separate hazards.
4. **COLREGs Rule 20(b) supplies an authoritative boundary** — navigation lights "from sunset to sunrise". Binding on these vessels, and the only boundary evidence found across five priority tiers.
5. **No evidence supports a twilight CAUTION band.** Three reviews found none; COLREGs has no intermediate state; no corpus paper reports a graded dusk risk profile.
6. **Sensitivity analysis confirms `g_t` is genuinely load-bearing** — tied-at-maximum in 86.5–87.6% of non-SAFE hours and *exclusively* binding in 81–82%, across all three models. Its dominance is a site property, not a threshold artefact. The component matters, so its provenance must be sound.
7. **Retaining a three-state time classifier for architectural symmetry would exceed the evidence.** Part 4 confirms symmetry is not required: no theorem, type or proof assumes surjectivity, and CAUTION remains reachable through `g_o` and `g_r`.
8. **The incumbent is wrong in a checkable way.** SAFE begins at 06:00; sunrise at this site is 06:01–06:34. **SAFE currently begins before sunrise on every day of the year.**

### Rejected alternatives

| Alternative | Why rejected |
|---|---|
| **Incumbent fixed clock (Model A)** | No provenance for any of three values; 06:00 precedes sunrise year-round; 17:00 precedes sunset by 57–95 min while being labelled "approaching darkness" |
| **Civil-twilight three-state (Model C)** | CAUTION band unsupported by any source. Its Level 2 figure (19.59%) is an artefact of civil dawn (05:37–06:11) falling inside the 05:00–09:00 departure window — not comparable to the incumbent's 7.72%. Would be adopting a band because it yields a middle state, which is the wrong reason |
| **Nautical twilight** | A celestial-navigation concept; no source applies it to small coastal vessels. Testing it would mean testing an option nothing supports |
| **Arbitrary policy-defined clock bands** | Permissible *only* if presented as a governance design choice. Appendix C presents the values as empirically derived, so adopting this route requires rewriting the justification — and it would still leave the most load-bearing component resting on undefended numbers when a regulated alternative exists |

### Known consequences

- **Level 2 binding falls: 7.72% → 5.81% (primary), 5.98% → 4.48% (resolution).** The fourth provenance-driven correction to *lower* the headline.
- **Time-driven CAUTION is eliminated by construction** — SAFE→CAUTION transitions caused by `g_t` go from 1,545 to **0**. All remaining CAUTION becomes weather-driven, which strengthens the Level 2 result's interpretation.
- **Direct SAFE→UNSAFE transitions rise from 2 to 1,536.** ⚠️ **The principal cost.** The architecture argues graduated governance beats a binary step, and under B the most predictable transition of the day becomes a step. **This must be stated in the paper, not absorbed.**
- **`g_t` transitions/day fall 2.73 → 1.88.**
- Prose implying every component is three-state must be corrected (Part 4.1).
- `cause` semantics mismatch surfaces (Part 5) — separate decision.

### Accepted design cost — recorded, not softened

**Approval explicitly accepts the following transition consequence as a design trade-off.** It is stated here in full because the architecture's own thesis is that graduated governance beats a binary step, and Model B makes the most predictable transition of the day a step.

| Measure (PRIMARY, 43,848 h) | Incumbent | **Model B** |
|---|---|---|
| **Direct SAFE→UNSAFE transitions** | **2** | **1,536** |
| **SAFE→CAUTION transitions caused by `g_t`** | **1,545** | **0** |
| CAUTION→UNSAFE by `g_t` | 1,724 | 186 |
| `g_t` transitions/day | 2.73 | 1.88 |

**This does not eliminate system-level graduation.** Under Model B the PRIMARY replay still produces **2,091 global CAUTION hours (4.77%)**, **all weather-driven** — every one from `g_o` or `g_r`. What is removed is time-driven CAUTION, for which no evidence was ever found. Arguably this *improves* the interpretation of the Level 2 result: every remaining CAUTION hour becomes a weather CAUTION.

**Four framings, assessed separately:** the step is **formally acceptable** (no theorem constrains transition paths; a two-level jump is monotone under Theorem C.2); **architecturally acceptable** (governance remains graduated; `g_t` is simply not a graduated variable); **not empirically problematic** (the transition is the most predictable event in the system, and oscillations fall slightly, 27 → 26); and **primarily a usability concern** — an operator loses advisory support at sunset with no in-band warning.

> ### ⚠️ Disclosure obligation — binding
>
> **The 2 → 1,536 figure must be disclosed in Threats to Validity**, stated plainly, not absorbed into surrounding text. A reader must be able to see that the architecture's headline argument and this component's behaviour stand in tension, and that the tension was accepted deliberately. **Recorded as C-4.**

### Out of scope — anticipatory notification

A **pre-sunset notification** may be considered later, and is explicitly **not** part of this decision. **No UI implementation is required or authorised here.**

If pursued, it must remain **separate from `g_t`**:

> **governance state ≠ anticipatory UI notification**

**No artificial CAUTION interval may be created to provide warning.** Reinstating a time-based CAUTION band to soften the transition would be adopting a band *because it yields a middle state* — the stated reason for rejecting Model C above, and the failure mode this project has refused repeatedly (7.5 mm/hr, `g_v`, the 1.9 m threshold). The architecture already accommodates the alternative: C.8.2 separates the governance stage from the advisory stage, and the governance layer may emit deterministic messages that are not AI recommendations and do not disturb `A_AI(UNSAFE) = ∅`. Any such notice must follow the wording standard in `cleanup-report-unsafe-semantics-2026-09-08.md` — report state and reason, assert no danger, issue no instruction, preserve operator authority.

### Execution conditions — C-1 through C-8, all binding

> # **Model B cannot become canonical until C-1 through C-8 are discharged.**
>
> **All eight are OPEN. None is executed by this approval.**

| | Condition | Status |
|---|---|---|
| **C-0** | Correct the algorithm provenance in this Decision clause | ✅ **CLOSED 2026-09-08** — `cleanup-report-c0-solar-provenance-2026-09-08.md` |
| **C-1** | **Pin the solar implementation** and resolve all reproducibility parameters | ✅ **CLOSED 2026-09-08** — `solar-spec-v1`; impl `solar-v1` sha256 `3b7dc371…c36c`; **longitude resolved to 116.01**; 12/12 checklist items explicit. Publication-reference gap recorded, not invented. `report-c1-c2-c3-solar-reproducibility-2026-09-08.md` |
| **C-2** | **Record the complete USNO validation artefact**, all 28 per-event values | ✅ **CLOSED 2026-09-08** — `data/solar/usno-validation-2026-09-08.csv`, 28 rows, sha256 `da14a8dc…9c81`. **V_historical retained unchanged; V_reconstructed adopted for reproducibility.** `report-c2-closure-2026-09-08.md` |
| **C-3** | **Store per-day computed solar timestamps** and make replay reproducible from stored inputs plus the pinned version | ✅ **CLOSED 2026-09-08** — `data/solar/solar-events-daily.csv`, 1,827 rows covering both configurations, governance-separated |
| **C-4** | **Document binary `g_t`, system-level graduation, and the accepted SAFE→UNSAFE transition cost** | ✅ **CLOSED 2026-09-08** — non-surjectivity statement added to Appendix C C.2; accepted cost recorded in **C.9.5**; notification separation in **C.9.6**; `f` surjectivity prose qualified in `formal-model.md`; Threats to Validity disclosure added to `manuscript-v3.md`. Canonical `g_t` unchanged. `report-c4-closure-2026-09-08.md` |
| **C-5** | **Three-stage hysteretic re-run** for P12 and related predictions | ✅ **CLOSED 2026-09-08** — gate passed: Stage 1 reproduces **P12 = 7.83 exactly**. **P12: 7.83 → 8.70 → 10.36**, Δ_data **+0.87**, Δ_g_t **+1.66**. Stage 3 consumed the frozen C-3 solar artefact. Artefacts in `data/c5/`; register byte-identical. **P09 baseline found non-reproducible and diagnosed → C-7.** `report-c5-closure-2026-09-08.md` |
| **C-6** | **Re-resolve affected predictions** using the established protocol | ✅ **CLOSED 2026-09-08** — 20 affected, 4 unaffected. **7 candidate status flips, but only 3 attributable to SDR-001** (P20, P23, P24); P04/P09/P18/P19 were already REFUTED under the incumbent at the current configuration. Candidate totals **15 CONFIRMED / 9 REFUTED**; **canonical totals remain 22/2**. Register annotated additively — no `actual` or `status` changed. `data/c6/prediction-reresolution.csv` · `report-c6-closure-2026-09-08.md` |
| **C-7** | **Reconcile baseline discrepancies before any comparison** | ✅ **CLOSED 2026-09-08** — single cause identified: all four "stale" values are the **pre-amendment threshold vintage** (v1, `r` 7.5, `o` 1.9) and reproduce exactly under it; the register holds the current-threshold values and also reproduces exactly. **P09 is the sole register exception** — its 5,416 is the pre-amendment figure, retained as historical; comparable current-threshold baseline **5,220**. Register **not mutated**; provenance in `data/c7/baseline-provenance.csv`. `report-c7-closure-2026-09-08.md` |
| **C-8** | **Execute the complete propagation/update list** — **8 scripts** (incl. `threshold_comparison.py`) and **~17 documents** (incl. `evaluation-design-rq4.md` SC-10, the Journal 1 manuscript, and every "daylight" label). **"Daylight" is redefined, not merely recomputed** | 🔴 **OPEN** |

**Full detail: `finding-sdr-001-readiness-audit.md` §11.**

### Prediction register — unchanged by this approval

**Approval alters no prediction.** Text, expected bands, actual values, CONFIRMED/REFUTED status and notes are all untouched. **The register remains the record of the *current canonical* architecture** — the incumbent `g_t` — until controlled re-resolution occurs under C-5, C-6 and C-7. P09, P12, P18, P19 and all others stand exactly as resolved.

---

## Part 7 — Prediction-register integrity

**No outcome overwritten. The register guard in every script (added 2026-09-08) makes resolved entries immutable; a re-run cannot silently rewrite them.**

**SDR-001 is now APPROVED (2026-09-08), but approval alone re-resolves nothing.** The register continues to record the *current canonical* architecture — the incumbent `g_t` — and every entry below stands as resolved. Re-resolution happens only during the controlled migration, under **C-5, C-6 and C-7**.

At that point each affected prediction must be **explicitly re-resolved** with all five fields recorded, in the manner already used for P16 and P22:

`previous canonical specification · new canonical specification · old result · new result · reason for re-resolution`

| Prediction | Registered statement | Current | Under Model B | Re-resolution needed? |
|---|---|---|---|---|
> ### ⚠️ Baseline column corrected 2026-09-08 (C-7). **Read this before using the "Current" column below.**
>
> The "Current" values in this table were quoted from the **pre-amendment threshold vintage** (v1 data, `r_CAUTION = 7.5 mm/hr`, small-vessel `o_UNSAFE = 1.9 m`) — not from the prediction register. **One cause explains every one of them**, and all five reproduce exactly under that vintage. The register holds the **current-threshold** values.
>
> | | Register (authoritative) | This table quoted | Both reproduce? |
> |---|---|---|---|
> | **P07** | **87.58** | 88.23 | ✅ Yes — different vintages |
> | **P09** | **5,416** | 5,416 | ⚠️ Register value *is* the pre-amendment one; current-threshold baseline is **5,220** |
> | **P10** | **230** | 227 | ✅ Yes |
> | **P11** | **37** | 70 | ✅ Yes |
> | **P12** | **7.83** | 6.17 | ✅ Yes |
>
> **C-6 must use the register values, and for P09 the current-threshold baseline 5,220**, per the authority rule in `report-c7-closure-2026-09-08.md`. Machine-readable: `data/c7/baseline-provenance.csv`.

| **P07** | `g_t` share of non-SAFE > 70% | CONFIRMED — register **87.58%** *(88.23% is the pre-amendment vintage)* | 86.82% | Annotate; **outcome unchanged** |
| **P09** | total transitions 5,400–8,000 | CONFIRMED — register **5,416** *(pre-amendment vintage; current-threshold baseline **5,220**)* | 3,661 | ⚠️ **See isolation note below** |
| **P10** | non-scheduled transitions < 500 | CONFIRMED — register **230** *(227 is the pre-amendment vintage)* | 222 | Annotate; outcome unchanged |
| **P11** | oscillations < 100 | CONFIRMED — register **37** *(70 is the pre-amendment vintage)* | 26 | Annotate; outcome unchanged |
| **P12** | hysteresis reduction 5–40% | CONFIRMED — register **7.83%** *(6.17% is the pre-amendment vintage)* | **C-5: 8.70% (v2/inc) / 10.36% (v2/Model B)** | ✅ Computed under C-5 |
| **P13** | chattering not demonstrated | CONFIRMED | Supported | Annotate; outcome unchanged |
| **P14** | wave gate + night curfew | CONFIRMED | Holds more strongly | Annotate; outcome unchanged |
| **P19, P20** | 6.1% binding; 409 daylight UNSAFE h | CONFIRMED | Both change | Re-resolve — "daylight" is itself redefined |
| **P22, P23, P24** | C1↔C2, C0↔C2, C0↔C1 divergence | P22 REFUTED; P23, P24 CONFIRMED | All change | Re-resolve |
| **P01, P16** | `g_w` activations | REFUTED / CONFIRMED | Unaffected | None — independent of `g_t` |

> ### ⚠️ P09 isolation requirement
>
> **P09's shortfall is a data-configuration effect, not a `g_t` effect, and the two must not be merged.**
>
> P09 was registered against **v1 land-cell** data and confirmed at 5,416. On **sea-cell** data the *incumbent* already yields **5,201** — below the registered 5,400 band, **before any `g_t` change**. Model B's 3,661 compounds a v1→v2 data effect with a `g_t` effect.
>
> **Any re-resolution of P09 must state both causes separately.** Attributing the whole shortfall to `g_t` would misrecord the history; attributing it to the data alone would understate the `g_t` effect. This is precisely the failure the register guard was installed to prevent.

---

## Part 8 — Exact propagation list

**Documents (7):** `appendix-c-formalisation.md` — C.1 time-of-day note, C.2 `g_t` table + signature, C.2.0.1/C.8.1 type tables, Theorem C.1 partition, C.9.1, plus a non-surjectivity statement (Part 4.1); `docs/reference/explainer-per-component-classification-functions.md` (definition + worked examples); `docs/implementation/dataset-label-derivation.md`; `docs/justification/safety-state-design.md`; `docs/justification/formal-model.md` (example vectors using `t`); `CLAUDE.md` (type table, threshold table, `g_t` open block); `notes/Determination of risk perception…md` (strike the unsupported Rahim claim and the peninsular-Malaysia twilight paragraph).

**Scripts (7):** `canonical_figures.py`, `condition_comparison.py`, `diagnostic_binding.py`, `hysteresis_analysis.py`, `historical_replay.py`, `compare_v1_v2.py`, `threshold_decision.py` — **plus** promotion of a validated solar module from `scripts/sensitivity/` into the canonical path, with its USNO validation recorded.

**Figures — every time-windowed value in §0a:** Level 2 binding (both configs); daylight UNSAFE hours and share; weather-driven share of UNSAFE; `g_t`, `g_o`, `g_r` binding shares; small-vs-big departure divergence; **the entire C0/C1/C2/C3 divergence matrix** (all four conditions share `g_t`); F-6 transition and oscillation counts; F-7 binding table; F-15 TABLE VII.

**⚠️ "Daylight" is redefined, not merely recomputed.** It is currently *defined* as `g_t` = SAFE (06:00–17:00). Under Model B it becomes sunrise–sunset — so "daylight UNSAFE hours" changes meaning as well as value, and every use of the term needs checking.

**Manuscript:** `manuscript-v3.md` — Algorithm 1 `g_t` line, TABLE VI, Results 1–6, abstract and conclusion figures, Threats to Validity (the SAFE→UNSAFE step cost belongs there).

**Predictions:** as tabulated in Part 7.

---

## Part 9 — Stop condition verified

Canonical `g_t` unchanged · Appendix C unchanged · canonical scripts unchanged · replay outputs unchanged · figures unchanged (7.72% / 5.98%) · prediction outcomes unchanged · prediction register unchanged (24 predictions, 22 confirmed / 2 refuted).

New material is confined to this finding and the pre-existing `scripts/sensitivity/`.

---

## Part 10 — Sources

| Source | Tier | Role |
|---|---|---|
| [USNO Astronomical Applications Department](https://aa.usno.navy.mil/) · [API `rstt/oneday` v4.0.1](https://aa.usno.navy.mil/api/rstt/oneday) · [Rise/Set one-year tables](https://aa.usno.navy.mil/data/RS_OneYear) | 2 | **Recommended authority.** Supplied all 28 validation reference values |
| Meeus, J. (1998). *Astronomical Algorithms*, 2nd ed. Willmann-Bell | 4 | **Candidate method, not implemented.** Surveyed as an option; **not** the algorithm in `solar.py` and **not** what the 0.9-min validation certifies (C-0 correction, §1.3, Part 6) |
| [NOAA GML Solar Calculator](https://gml.noaa.gov/grad/solcalc/) | 3 | Surveyed external calculator. *Corrected 2026-09-08 (C-0): previously described as "implementation of the same formulae" — **that equivalence is not established by any project evidence** and was one route by which the Meeus/NOAA conflation spread. NOAA's own material describes more than one formulation, and this project has not determined which corresponds to `solar.py`* |
| [COLREGs Rule 20 — Application](https://www.cultofsea.com/colregs/part-c-lights-and-shapes-rules-20-31/rule-20-application/) · [eColRegs](https://ecolregs.com/index.php?option=com_k2&view=item&layout=item&id=60&Itemid=393&lang=en) | 3 | **"From sunset to sunrise"** — the boundary authority for the decision |
| [Islamic falak location spots in Malaysia](https://en.wikipedia.org/wiki/List_of_Islamic_falak_location_spots_in_Malaysia) | 1 | Records that Malaysia's astronomical network serves prayer-time determination; **no general ephemeris service located** |
| Atacan & Düzbastılar (2023) [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | 4 | Night riskier than day; **no clock boundary** |
