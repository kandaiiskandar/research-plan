# Finding: SDR-001 Approval Readiness Audit

**Date:** 2026-09-08
**Type:** Read-only. **Nothing modified. Model B not adopted. SDR-001 remains DRAFT — NOT APPROVED — NOT APPLIED.**
**Scope:** Approval conditions only. Semantic compatibility is treated as resolved per `finding-unsafe-semantics-audit.md` and `cleanup-report-unsafe-semantics-2026-09-08.md`.
**Predecessors:** `finding-gt-provenance-audit.md` · `finding-gt-operational-semantics.md` · `finding-gt-sensitivity-analysis.md` · `finding-gt-evidence-closure.md` (SDR-001 draft)

---

> ### ✅ Status update, 2026-09-08 — **SDR-001 APPROVED on this verdict**
>
> **C-0 is CLOSED** (`cleanup-report-c0-solar-provenance-2026-09-08.md`) and **SDR-001 was approved on 2026-09-08** as a **design decision**: Model B is the selected replacement design for `g_t`. See `approval-report-sdr-001-2026-09-08.md`.
>
> **Approval did not migrate anything.** **C-1 through C-8 remain OPEN and binding**, the incumbent fixed-clock `g_t` remains canonical, and **7.72% / 5.98% remain the authoritative figures**. This audit is retained unchanged as the record of how the verdict was reached.

# VERDICT: **READY WITH EXECUTION CONDITIONS**

**The design decision is justified. The execution artefacts are not yet in place, and one defect sits in the approval document itself.**

The rationale for Model B survives scrutiny: it is the only regulation-derived option, it fixes a checkable error in the incumbent, and it moves the headline downward. Nothing found here undermines that. But **nine execution conditions must be discharged**, and **one of them must be discharged before approval rather than before migration** — SDR-001 as drafted names an algorithm that has never been validated (§4.1). Approving the text as written would authorise something the evidence does not cover.

**Not READY**, because the approval conditions (b) and (c) are demonstrably unmet today.
**Not NOT READY**, because every gap found is an artefact or documentation gap resolvable within a controlled migration — none impeaches the decision.

---

## 1. Step-cost findings — Condition 1

All figures re-read from `finding-gt-sensitivity-analysis.md` §3. **Not recomputed; nothing re-run.**

### 1.1 Verified transition counts — PRIMARY (43,848 h, 5.00 yr, ERA5-Ocean)

| Measure | **A** incumbent | **B** solar | Δ |
|---|---|---|---|
| **SAFE→CAUTION by `g_t`** | **1,545** | **0** | **−1,545 (eliminated by construction)** |
| **SAFE→UNSAFE (any cause)** | **2** | **1,536** | **+1,534** |
| — of which by `g_t` | 0 | 1,534 | — |
| CAUTION→UNSAFE by `g_t` | 1,724 | 186 | −1,538 |
| **CAUTION prevalence (global)** | **5,375 h (12.26%)** | **2,091 h (4.77%)** | **−61%** |
| SAFE hours | 16,990 (38.75%) | 18,424 (42.02%) | +1,434 |
| UNSAFE hours | 21,483 (48.99%) | 23,333 (53.21%) | +1,850 |
| `g_t` transitions/day | 2.73 | 1.88 | −0.85 |
| Total transitions | 5,201 | 3,661 | −1,540 |
| Level 2 binding (05–09) | 7.72% | 5.81% | −1.91 pp |

**RESOLUTION (28,501 h, 3.25 yr, MFWAM):** SAFE→CAUTION by `g_t` 1,041 → **0**; SAFE→UNSAFE 2 → **1,045**; CAUTION prevalence 11.56% → **3.89%**; Level 2 binding 5.98% → 4.48%. **Same structure, same direction.**

### 1.2 Is CAUTION still materially reachable from non-time components?

**Yes — decisively.**

| | Model B |
|---|---|
| CAUTION hours remaining | **2,091 (4.77% of all hours)**, PRIMARY |
| Source of every one of them | `g_o` or `g_r` — **not** `g_t` |
| `g_o` share of daylight CAUTION (incumbent baseline) | 98.66% / 97.41% |
| `g_r` share of daylight CAUTION | 1.55% / 2.99% |

**CAUTION is not a marginal state under Model B.** 2,091 hours over five years, from the two components that were already producing essentially all of it. `g_t`'s contribution to CAUTION was never the interesting part — `g_o` dominates daylight CAUTION at 98.66% under the *incumbent*.

**A cleaner reading emerges.** Under Model B **every CAUTION hour in the model is a weather CAUTION**. That strengthens the interpretation of the Level 2 result rather than weakening it: the headline stops being partly an artefact of a clock band nothing supports.

### 1.3 Verdict on Condition 1

> ## **Step cost: ACCEPTABLE WITH DISCLOSURE**

Acceptable because system-level graduation survives intact (§2) and the removed band had no evidential basis (§2.3). **With disclosure** because the 2 → 1,536 figure is genuinely in tension with how the contribution is narrated, and must appear in Threats to Validity — stated, not absorbed. The draft SDR already flags this; the audit confirms the flag is warranted and sufficient.

**Not disqualifying.** A cost that must be disclosed is not a cost that forbids the decision.

---

## 2. Does global graduation remain valid? — Condition 1A

> ## **YES. System-level graduation is untouched.**

### 2.1 The two claims are different objects

| | Definition | Under Model B |
|---|---|---|
| **Component-level graduation** | Each `gᵢ` realises all three states — every classifier is surjective onto {SAFE, CAUTION, UNSAFE} | **Lost for `g_t`.** `g_t` becomes two-state |
| **System-level graduation** | `f` realises all three states, and `A_AI` contracts in stages: `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` | **Fully preserved.** 2,091 CAUTION hours; containment untouched |

**The contribution is stated at the system level, everywhere it is stated.** The CS claim (CLAUDE.md, Chapter 2 §129, manuscript-v3, Journal 1) is that *no architecture conditions AI advisory scope on classified environmental state via an intermediate mode*. That claim is about `(G(S), A_AI(S))` and `S`. It says nothing about the internal range of any `gᵢ`.

### 2.2 Nothing requires component-level surjectivity — verified

| Artefact | Requirement | Model B |
|---|---|---|
| `gᵢ : Xᵢ ∪ {⊥} → {SAFE, CAUTION, UNSAFE}` (C.2) | A **codomain** declaration, not an image declaration | ✅ Satisfied |
| **Theorem C.1** (totality) | Each `gᵢ` **total**; the `g_t` case argues only that its intervals partition `[0,24)` exhaustively | ✅ Two intervals partition identically |
| **Theorem C.1b** (operational totality) | `gᵢ(⊥) = UNSAFE` + max-severity totality | ✅ Unaffected |
| **Corollary C.1b.1** (fail-safe) | `g_t(⊥) = UNSAFE` | ✅ Retained in the SDR's own signature |
| **Theorem C.2** (monotonicity) | Quantifies over `S₁, S₂ ∈ 𝒮`; never references `gᵢ` | ✅ Unaffected |
| **Theorem C.3** (Safety Dominance) | *"depends only on the value of S, never on how S was reached"* (C.7.2) | ✅ Unaffected |
| **Definition C.1** (severity order) | A total strict order on a three-element **set** — its cardinality, not any component's image | ✅ Unaffected |
| **Containment** `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅` | A property of `A_AI`, defined on `S` | ✅ Unaffected |

**One surjectivity claim exists in the project**, and it concerns **`f`**, not `g_t`: `docs/justification/formal-model.md` line 287 — *"The classification function f: D_E → {SAFE, CAUTION, UNSAFE} is surjective and many-to-one."*

**It survives Model B at the deployed configuration** (`D = {m}`, 2,091 CAUTION hours). It would fail only at `D = {w, r, m, o}` — the degenerate configuration Lemma C.1c already identifies as "total and near-useless". **Non-canonical prose; on the propagation list (§11), not a blocker.**

### 2.3 The honest form of the claim

Component-level graduation was never established for `g_t` in the first place. Three independent reviews found **no source for a twilight CAUTION band**: Atacan & Düzbastılar tested no twilight condition, COLREGs has no intermediate state, and no corpus paper reports a graded dusk risk profile. **Model B does not remove an evidenced middle state; it removes an unevidenced one.**

**Stated against interest:** the architecture is nonetheless *presented* as graduated, and a reviewer meeting a two-state `g_t` beside three-state `g_o` and `g_r` will ask why. The answer — that graduation is a system property and components need not be surjective — is correct and must be *written down*, which is why Part 4.1 of the evidence closure and §11 below both call for an explicit non-surjectivity statement. Leaving it implicit invites the misreading.

---

## 3. The predictable sunset transition — Conditions 1B and 1C

### 3.1 Four-way classification of the 2 → 1,536 step

| Frame | Verdict | Reasoning |
|---|---|---|
| **Formally acceptable** | ✅ **Yes, unreservedly** | No theorem constrains transition *paths*. C.2 bounds `A_AI` at each state and guarantees it never expands as severity rises; a two-level jump is monotone. Nothing in C.1–C.8 mentions transitions at all |
| **Architecturally acceptable** | ✅ **Yes, with the asymmetry stated** | The architecture's thesis is that *governance* is graduated, and it remains so — CAUTION persists at 4.77%, reached by weather. `g_t` is simply not a graduated variable, and there is no evidence it should be |
| **Empirically problematic** | ❌ **No** | The transition is the most *predictable* event in the system: computable years ahead from (date, lat, lon). It is the opposite of the instability hysteresis addresses. F-6 already establishes chattering is not a demonstrated problem (27 oscillations under A, 26 under B — **B is marginally better**) |
| **Mainly a usability/HCI concern** | ✅ **Yes — this is where it actually lives** | The real cost is that an operator loses advisory support at sunset with no in-band warning. That is an interface problem, not a governance-correctness problem |

**The step cost is a usability concern wearing a formal costume.** Recognising that is what makes §3.2 the right answer.

### 3.2 Should a pre-sunset warning be a CAUTION state? — Condition 1C

> ## **Neither a CAUTION state nor "neither" — a notification/anticipatory advisory, kept outside the governance state.**

**Not a CAUTION safety state. Three reasons:**

1. **No evidence supports it.** This is exactly the band three reviews failed to source. Reinstating it to soften a transition would be adopting a band *because it yields a middle state* — the SDR's own stated reason for rejecting Model C, and the reasoning the project has repeatedly refused (7.5 mm/hr, `g_v`, the 1.9 m threshold).
2. **It would corrupt the headline.** A pre-sunset CAUTION band inflates Level 2 binding with hours that are not marginal. Model C demonstrates the failure mode concretely: its 19.59% is civil dawn (05:37–06:11) landing inside the 05:00–09:00 departure window — *"the CAUTION band was moved into the window being measured"*.
3. **It would misdescribe the state.** CAUTION means *AI advisory participation is admissible but restricted* (Definition C.1, as revised). At 17:30 with calm seas, participation is not restricted — it is full, and about to end.

**A notification is the correct instrument**, and the architecture already has a place for it. C.8.2 separates the governance stage from the advisory stage, and `architecture-illustration.md` establishes that the governance layer may emit deterministic messages that are not AI recommendations and do not disturb `A_AI(UNSAFE) = ∅`. An anticipatory notice — *"AI advisory will become unavailable at 18:12 (sunset)"* — is a **deterministic Layer-2 message about a computable future event**. It carries no AI reasoning, changes no admissible set, and violates nothing.

**This is the separation the project should prefer:** governance state describes what is admissible *now*; the interface may describe what is coming. Collapsing anticipation into the state machine is what forces the invention of unevidenced bands.

Consistency note: any such notice must follow the wording standard just established in `cleanup-report-unsafe-semantics-2026-09-08.md` — report state and reason, assert no danger, issue no instruction, and preserve operator authority.

**Out of scope for SDR-001.** This is a UI/notification design item; it should be recorded as follow-on work, not folded into the classifier decision.

---

## 4. Solar implementation reproducibility — Condition 2

### 4.1 ⚠️ The provenance chain does not close — the central finding of this audit

> ✅ **RESOLVED 2026-09-08 — C-0 CLOSED.** The defect diagnosed in this subsection has been corrected in `finding-gt-evidence-closure.md` (Decision clause, Part 2, §1.3, sources table, and a guard on the candidate-source table). **The wording below is retained as the record of the diagnosis; the SDR text it quotes no longer stands.** Resolution: the validated implementation was preserved and the wording corrected — Meeus was not implemented. See `cleanup-report-c0-solar-provenance-2026-09-08.md`. **C-1 through C-8 remain OPEN.**

**Intended chain, verified as intended:**

| Link | Status |
|---|---|
| COLREGs Rule 20(b) → sunset/sunrise as a **maritime operating boundary** | ✅ **Sound.** Rule 20(b) requires navigation lights "from sunset to sunrise". *It regulates lights; it does not state that night operation is unsafe, and this audit does not claim it does* |
| USNO → **authoritative astronomical reference** | ✅ **Sound.** API v4.0.1, a documented government service supporting historical dates |
| Local implementation → **reproducible replay computation** | ❌ **BROKEN — see below** |

**The defect.** SDR-001's Decision clause states:

> "Sunrise and sunset computed per (date, latitude, longitude) by the **Meeus algorithm**, validated against USNO API v4.0.1 (max deviation 0.9 min, §2)."

**The validated code is not Meeus.** `scripts/sensitivity/solar.py` implements the **NOAA GML / Spencer (1971) low-precision Fourier series**:

```python
g  = 2*np.pi/365.0 * (doy - 1)
eq = 229.18*(0.000075 + 0.001868*np.cos(g) - 0.032077*np.sin(g)
             - 0.014615*np.cos(2*g) - 0.040849*np.sin(2*g))
dec = (0.006918 - 0.399912*np.cos(g) + ... )
```

Its own docstring says so: *"NOAA Global Monitoring Laboratory solar calculator equations (Astronomical Almanac low-precision formulae)"*. Meeus, *Astronomical Algorithms* (2nd ed., 1998) is a **materially different method** — Julian-century time argument, geometric mean longitude, mean anomaly, equation of centre, apparent obliquity. It is more accurate and produces different values at the sub-minute scale that §4.3 shows can matter.

**Consequences, stated precisely:**

1. **The 0.9-minute validation certifies Spencer/NOAA. It does not transfer to Meeus.** Approving SDR-001 as drafted would approve an algorithm for which no validation exists in this project.
2. `finding-gt-evidence-closure.md` §2 compounds it by writing *"(scripts/sensitivity/solar.py, NOAA/Meeus formulae)"* — treating two distinct algorithms as one.
3. `finding-gt-sensitivity-analysis.md` §7 is the only document that gets it right: *"NOAA Global Monitoring Laboratory solar-position equations (Astronomical Almanac low-precision formulae)"*.

**This is a documentation defect, not an evidential collapse** — Spencer/NOAA validating to 0.9 min against USNO is a perfectly good result, and either algorithm would serve. But the approval artefact must name the algorithm that was actually validated, or the validation must be re-run against Meeus. **This must be fixed before approval, not before migration.**

*Structurally this is the same failure mode as the 7.5 mm/hr error: a value in the code and a different justification in the document, with nobody comparing them.* The evidence-closure finding itself warned against "repeating the 7.5 mm/hr error in a new variable."

### 4.2 Pinning checklist — Condition 2A

What must be frozen for reproducibility, and what exists today:

| # | Item | Present? | Value / gap |
|---|---|---|---|
| 1 | **Algorithm name** | ❌ **Contradictory** | Code = NOAA/Spencer 1971; SDR = Meeus 1998. **Must be resolved** |
| 2 | **Published reference** | ⚠️ Partial | Meeus 2nd ed. 1998 cited for a method not implemented; NOAA GML has no stable citable version |
| 3 | **Code version / commit** | ❌ **Absent** | No commit hash, no version string, no repo pin. Project is not a git repository |
| 4 | **Latitude** | ✅ | `5.98` N (default arg) — matches `empirical-findings` site |
| 5 | **Longitude** | ⚠️ **Inconsistent** | `solar.py` default `116.07`; the dataset site is `116.01` (empirical-findings §5). **0.06° ≈ 14 s of solar time.** Small, but it is exactly the scale §4.3 shows can flip an hour |
| 6 | **Date source** | ⚠️ Weak | `d.timetuple().tm_yday` — day-of-year only. The Spencer series assumes a 365-day year; **leap-year handling is undocumented** |
| 7 | **Timezone** | ⚠️ Implicit | `tz=8` integer default. Malaysia has no DST so this is correct, but the *reason* is unrecorded |
| 8 | **UTC↔local conversion** | ⚠️ Implicit | `rise_utc_min/60.0 + tz`. Correct; undocumented |
| 9 | **Sunrise/sunset definition** | ✅ | Zenith **90.833°** (refraction 34′ + semi-diameter 16′). Explicit constant |
| 10 | **⊥ / invalid clock or location** | ❌ **Absent from code** | SDR signature has `g_t(⊥) = UNSAFE` ✅, but `solar.py` has **no handling for invalid lat/lon/date**. `np.clip(c, -1, 1)` silently returns a value for polar cases instead of signalling no-event |
| 11 | **Rounding** | ❌ **Absent** | Returns raw float hours. No documented rounding or precision rule |
| 12 | **Boundary comparison rule** | ✅ **Specified** | SDR uses half-open `sunrise ≤ t < sunset` — matches the incumbent's convention and Theorem C.1's partition argument |

**Score: 3 of 12 fully satisfied; 5 partial; 4 absent.**

### 4.3 USNO validation status — Condition 2B

| Item | Recorded value |
|---|---|
| **Validation dates** | **7** |
| **Events per date** | **4** (sunrise, sunset, civil dawn, civil dusk) |
| **Total comparisons** | **28** |
| **Maximum absolute difference** | **0.9 min** |
| **Mean absolute difference** | **0.37 min** |
| **Sunrise/sunset only** (what Model B uses) | max **0.9 min**, mean **0.35 min** |
| **Annual extremes covered** | ✅ **All four** — latest sunrise (2024-02-02, 06:33), earliest sunrise (2024-05-24, 06:00), latest sunset (2024-07-17, 18:35), earliest sunset (2024-11-11, 17:56) |
| **Seasonal reference dates** | ✅ March equinox, June solstice, December solstice |

**Is 7 dates sufficient for hourly replay resolution? — Yes, with one qualification.**

**Sufficient because** the extremes are the binding cases. Solar event times at 5.98° N vary smoothly and by only ~34 min across the year; a method that tracks USNO to 0.9 min at all four extremes plus three reference points has been tested where it is most likely to fail. Adding dates would sample a smooth curve more densely without probing new regimes. **At hourly resolution, 0.9 min is immaterial for the overwhelming majority of hours.**

**The qualification is §4.4**, and it is not answered by adding dates.

**One gap in the record itself:** the 28 comparisons are reported as summary statistics. **The per-event USNO values are not stored anywhere in the project** — so the validation cannot presently be re-verified without re-querying a live external API, which defeats the purpose of a pinned validation.

### 4.4 Boundary sensitivity — Condition 2C

The measured hazard, from `finding-gt-evidence-closure.md` §2.1, over the 1,827-day replay:

| | Within 1 min of an hour mark | Within 2 min |
|---|---|---|
| **Sunrise** | **160 days** | 335 |
| **Sunset** | **60 days** | 125 |

**Closest approach: 0.02 minutes.**

So on ~220 of 1,827 days a sub-minute implementation difference *can* flip an hour's classification. Expected actual flips are far fewer — the difference must exceed the gap and both values must fall the same side — but the exposure is real and is concentrated at exactly the boundary Model B depends on.

**Therefore pinning alone is insufficient.** Three requirements, in increasing strength:

1. **Pin the implementation** — necessary, not sufficient. A future reimplementation differing by 1 min changes published figures silently. This is precisely the drift the recomputation rule exists to stop.
2. **Store the computed solar timestamp per replay day** — **required.** The replay must emit `date, sunrise_local, sunset_local` alongside its classifications, so any figure can be re-derived without re-running the solar routine.
3. **Make classification reproducible from stored inputs + implementation version** — **required.** With (2), the classification becomes a pure function of stored data, and the solar routine moves off the critical path for reproducing published numbers.

Requirements (2) and (3) also close the §4.3 gap: with per-day timestamps stored, the USNO validation becomes re-checkable against a frozen artefact.

### 4.5 Verdict on Condition 2

> ## **Reproducibility condition: NOT SATISFIED**

Not "satisfied with minor documentation". Three of the four gaps are substantive:

- the **algorithm named in the approval document is not the algorithm validated** (§4.1);
- there is **no version pin of any kind** (§4.2 item 3);
- **solar timestamps are not stored**, so figures are not re-derivable without re-running an unpinned routine (§4.4);
- and a **coordinate inconsistency** (116.07 vs 116.01) sits at the scale that matters (§4.2 item 5).

**All are fixable inside a controlled migration.** None impeaches Model B. But condition (b) of the SDR — *"the solar implementation is pinned with its USNO validation recorded"* — is **demonstrably unmet today**.

---

## 5. Complete prediction-impact matrix — Condition 3

**All 24 register entries assessed. Values below are read from `data/prediction-register.csv`. Nothing re-resolved; nothing written.**

| ID | Metric | Registered | Status | `g_t`-sensitive? | Classification |
|---|---|---|---|---|---|
| **P01** | `g_w` activations | 0 | REFUTED (2) | No | **Unaffected** |
| **P02** | superseded vessel-blind `g_o` UNSAFE | 0 | CONFIRMED (0) | No | **Unaffected** |
| **P03** | SAFE % under superseded `g_v`, **scope "daylight 06-17"** | 0.0% | CONFIRMED (0.0) | ⚠️ **Scope only** | **Affected in scope definition; outcome invariant** (0% holds under any window) |
| **P04** | Level 2 binding, dep. window | 12.4% | CONFIRMED (12.4) | **Yes** | **Affected, computable.** Already superseded (v1 config) |
| **P05** | `g_o` share of daylight CAUTION | >90% | CONFIRMED (97.95) | **Yes — doubly** | **Affected, computable.** Scope redefines *and* value rises toward 100% as time-CAUTION vanishes |
| **P06** | `g_r` share of non-SAFE, daylight | <5% | CONFIRMED (1.76) | **Yes — doubly** | **Affected, computable** |
| **P07** | `g_t` share of non-SAFE | >70% | CONFIRMED (**87.58**) | **Yes** | **Affected, computable.** B = 86.82% → **outcome unchanged** |
| **P08** | distinct functions at max, dep. window | ≤4 | CONFIRMED (3.0) | **Yes** | **Affected, computable.** `g_t` still binds pre-sunrise → **outcome unchanged** |
| **P09** | total transitions | 5400–8000 | CONFIRMED (**5416**) | **Yes** | **Affected — see §6 isolation** |
| **P10** | non-time-driven transitions | <500 | CONFIRMED (**230**) | **Yes** | **Affected, computable.** B = 222 → outcome unchanged |
| **P11** | oscillations <3 h | <100 | CONFIRMED (**37**) | **Yes** | **Affected, computable.** B = 26 → outcome unchanged |
| **P12** | hysteresis reduction | 5–40% | CONFIRMED (**7.83**) | **Yes** | ❌ **NOT RESOLVABLE YET — see §7** |
| **P13** | chattering demonstrated? | NO | CONFIRMED | **Yes** | **Affected, computable.** Holds under B |
| **P14** | wave gate + night curfew? | YES | CONFIRMED | **Yes** | **Affected, computable.** Holds *more strongly* under B |
| **P15** | max sustained wind, sea cell | 20–30 kn | CONFIRMED (21.8) | No | **Unaffected** |
| **P16** | `g_w` activations, sea cell | >0, <500 | CONFIRMED (2) | No | **Unaffected** |
| **P17** | MFWAM vs ERA5 CAUTION rate | MFWAM LOWER | CONFIRMED (8.01) | **Yes** | **Affected, computable.** Comparative — direction likely holds, **must be confirmed not assumed** |
| **P18** | Level 2 binding, MFWAM | 8–12% | CONFIRMED (8.32) | **Yes** | ⚠️ **Affected — outcome may flip.** B RESOLUTION = **4.48%**, below the 8–12% band. Already superseded (1.9 m config) but requires explicit re-resolution |
| **P19** | Level 2 binding after 1.25 m | 6.1% | CONFIRMED (6.1) | **Yes** | **Affected — outcome likely flips.** B = 4.48% |
| **P20** | daylight UNSAFE hours | 409 | CONFIRMED (409) | **Yes — definitionally** | **Affected. "Daylight" is redefined, not just recomputed** |
| **P21** | C3 ≡ C1 divergence | 0 | CONFIRMED (0.0) | **No — structurally invariant** | **Unaffected. See §5.1** |
| **P22** | C2 vs C1 divergence | 6.0–6.2% | REFUTED (5.98) | **Yes** | **Affected, computable** |
| **P23** | C0 vs C2 divergence | 20–30% | CONFIRMED (28.19) | **Yes** | **Affected, computable** |
| **P24** | C0 vs C1 divergence | 14–24% | CONFIRMED (22.21) | **Yes** | **Affected, computable** |

**Totals:** 4 unaffected · 1 unaffected-but-structural (P21) · 1 scope-only (P03) · **16 affected and computable** · **1 not resolvable yet (P12)** · 1 outcome-flip risk requiring care (P18/P19).

### 5.1 P21 is structurally invariant — and this matters more than its row suggests

**P21 carries F-15, the result that answers Review 3's novelty objection.** It is **immune to the `g_t` decision**, and provably so.

From `scripts/condition_comparison.py` lines 86 and 92:

```python
"C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
"C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
```

**C1 and C3 are the identical map.** Their admissible sets coincide for *every* state, hence for every hour, under *any* classifier whatsoever. The 0.00% divergence is a structural consequence of Flehmig's governance topology — its intermediate level does not touch advisory scope — not an empirical coincidence of the incumbent `g_t`.

**Consequence for the decision:** the single most reviewer-facing empirical claim in the project **cannot be disturbed by adopting Model B**. It should still be re-run for the record, but its outcome is not at risk.

*Recorded for completeness: P21 was omitted from the SDR's Part 7 table, while Part 8 asserts "the entire C0/C1/C2/C3 divergence matrix" changes. Both are now resolved — C0/C1/C2 values change, the C1↔C3 result does not.*

### 5.2 ⚠️ Baseline discrepancy — must be reconciled before any re-resolution

**The `g_t` findings quote registered actuals that do not match the register.**

| ID | Register (`prediction-register.csv`) | Quoted in `finding-gt-sensitivity-analysis.md` §5 and `finding-gt-evidence-closure.md` Part 7 |
|---|---|---|
| **P07** | **87.58** | 88.23 |
| **P10** | **230** | 227 |
| **P11** | **37** | 70 |
| **P12** | **7.83** | 6.17 |

**The register is authoritative.** Anyone executing the migration from the SDR's Part 7 table would compare Model B results against **four wrong baselines**. In P11's case the quoted figure (70) is nearly double the registered one (37) — and 70 also appears in `CLAUDE.md` ("70 genuine oscillations, 14/yr"), so the wrong figure is circulating in the project's own orientation document.

**Pre-existing, unrelated to Model B, and squarely a prediction-integrity issue.** Reconciling it is an execution condition (§9, C-7).

### 5.3 Verdict on Condition 3

> ## **Prediction integrity: SATISFIED ONCE NAMED COMPUTATIONS ARE RUN**

The protocol is sound, the register guard is installed and working (it is what caught the P09 and P18 overwrites), and no outcome has been silently altered. **What is missing is computation and reconciliation, not integrity.** Named in §9: C-5 (P12 hysteretic re-run), C-6 (16 computable re-resolutions), C-7 (baseline reconciliation).

---

## 6. P09 isolation — Condition 3A

> ## **Confirmed. The current miss is a data-configuration effect, not a `g_t` effect. Model B additionally affects it, and the two causes must be recorded separately.**

**The arithmetic settles it:**

| Configuration | `g_t` | Data | Total transitions | Against band 5,400–8,000 |
|---|---|---|---|---|
| **As registered** (2026-09-06) | Incumbent | **v1 land-cell** | **5,416** | ✅ **CONFIRMED — in band** |
| Recomputed | **Incumbent** | **v2 sea-cell** | **5,201** | ❌ **Below band — before any `g_t` change** |
| Counterfactual | **Model B** | v2 sea-cell | **3,661** | ❌ Further below |

**Decomposition:**

- **v1 → v2 data effect: −215 transitions** (5,416 → 5,201). This alone breaks the band.

> ### ⚠️ Decomposition superseded 2026-09-08 (C-5 measurement, C-7 reconciliation). **Text retained as the record of what was concluded here.**
>
> **The −215 figure conflates two changes.** 5,416 is not the v1/incumbent value under the *current* specification — it requires the **pre-amendment** thresholds (`r_CAUTION = 7.5`, `o_UNSAFE = 1.9`). Measured cleanly, the decomposition is four-stage:
>
> **5,416 —(threshold −196)→ 5,220 —(data −19)→ 5,201 —(g_t −1,540)→ 3,661**
>
> So **Δ_data = −19, not −215**; the remaining −196 is threshold vintage. **Δ_g_t = −1,540 was correct.** The conclusion this section draws — that P09's shortfall exists before any `g_t` change and that both causes must be recorded separately — **still holds, and is now sharper**: there are three causes, not two.
- **Model B `g_t` effect: −1,540 transitions** (5,201 → 3,661), consistent with `g_t` transitions/day falling 2.73 → 1.88.

**The shortfall exists without Model B.** The incumbent classifier on sea-cell data already yields 5,201, which is 199 below the registered floor.

**Why the separation is load-bearing.** Attributing the whole shortfall to `g_t` would misrecord the history and overstate Model B's disruption. Attributing it to the data alone would understate the `g_t` effect by a factor of seven. Either error would corrupt the register's function as a record of what was expected before results were seen — and the register's `notes` field already documents that a re-run once silently rescored P09 to 5,220 and had to be restored by hand.

**Required at re-resolution:** both magnitudes recorded, with the incumbent-on-sea-cell figure (5,201) stated as the intermediate baseline that isolates them.

---

## 7. P12 status — Condition 3B

> ## **NOT RESOLVABLE YET. A full hysteretic re-run is required. This is stated explicitly, as instructed.**

**Why the sensitivity analysis cannot answer it.** P12 measures *"percentage reduction in non-time-driven transitions from dual-threshold hysteresis"*. That requires two runs — with and without hysteresis — and the hysteretic run is **stateful and sequential**: `classify_hysteretic()` in `scripts/hysteresis_analysis.py` (lines 85–125) walks the series hour by hour, applying a 10% return margin (`MARGIN = 0.10`) to `g_o` and `g_r`, where each hour's classification depends on the previous state. **`scripts/sensitivity/gt_counterfactual.py` implements no hysteresis at all.** Its transition counts are non-hysteretic.

**P12's outcome must not be inferred from non-hysteretic sensitivity output.** It has not been, and must not be. The sensitivity finding correctly marked it *"❌ not computed"* under all three models.

**Two confounded changes, and this is the sequencing risk.** `hysteresis_analysis.py` reads the **v1 land-cell files** (`raw_weather.csv`, `raw_marine.csv`, `raw_rainfall.csv`) — the cells F-10 condemned and CLAUDE.md forbids quoting as current. So computing P12 under Model B requires:

1. porting the hysteretic classifier to **v2 sea-cell data**, and
2. substituting the **solar `g_t`**.

**Run together, these confound exactly as P09 did.** The migration must run the hysteretic classifier in **three stages** — v1/incumbent (reproducing 7.83), v2/incumbent, v2/Model B — so the data effect and the `g_t` effect are separable at re-resolution. **Anything less repeats the P09 problem in a new prediction, knowingly.**

**Note:** the same v1-data dependency applies to P09, P10, P11 and P13, all resolved from this script. The three-stage requirement covers them too.

---

## 8. Re-resolution protocol — Condition 3C

The protocol below is the one already used for **P16** (REFUTED → CONFIRMED at the corrected 21.6 kn boundary) and **P22**. It is not new; it is being restated as the binding rule for this migration.

**For every affected prediction, in order:**

1. **Preserve the original prediction text verbatim.** Never edit `metric`, `scope` or `rationale` to match a new result.
2. **Preserve the original expected band** (`pred_lo`, `pred_hi`, `pred_stated`) unchanged.
3. **Document the canonical-model change** — the specification delta that triggered re-resolution, citing SDR-001.
4. **Re-run the affected metric** under the new canonical specification, using the canonical script, not an ad-hoc one.
5. **Record the new observed value** in `actual`, retaining the prior value in `notes`.
6. **Classify CONFIRMED / REFUTED against the *original* prediction** — the question is always "was the original expectation right about the world as now measured?"
7. **Never rewrite the prediction to fit the new result.**

**Five fields to be recorded for each, as with P16:**
`previous canonical specification · new canonical specification · old result · new result · reason for re-resolution`

**Two additional rules specific to this migration:**

- **Isolation rule.** Where a prediction is affected by *both* the v1→v2 data change and the `g_t` change (P09, P10, P11, P12, P13), **both magnitudes must be recorded separately**, with the intermediate v2/incumbent value stated. §6 and §7.
- **Register-guard rule.** The `_register_guard` in every register-writing script must remain active throughout. No script may silently rescore a resolved entry; re-resolution is a deliberate, documented act.

---

## 9. Propagation and update list — Condition 4

**The SDR's Part 8 list is materially incomplete.** Verified counts below.

### 9.1 Scripts — **8, not 7**

| # | Script | Site | In SDR Part 8? |
|---|---|---|---|
| 1 | `canonical_figures.py` | L121–122 `g_t`; **L134 daylight window** | ✅ |
| 2 | `condition_comparison.py` | L155–156 | ✅ |
| 3 | `diagnostic_binding.py` | L72–73 `g_t`; L121 daylight | ✅ |
| 4 | `hysteresis_analysis.py` | L72–73 `g_t_series` | ✅ |
| 5 | `historical_replay.py` | L88–90 `g_t`; L206 daylight label | ✅ |
| 6 | `compare_v1_v2.py` | L36 inline `g_t` | ✅ |
| 7 | `threshold_decision.py` | L57 | ✅ |
| 8 | **`threshold_comparison.py`** | **L45 `day = m[(m.hr >= 6) & (m.hr < 17)]`** | ❌ **MISSING** |

Plus: promotion of a validated solar module from `scripts/sensitivity/` into the canonical path (§4).

### 9.2 Documents — **~13, not 7**

**In the SDR's list:** `appendix-c-formalisation.md` · `explainer-per-component-classification-functions.md` · `dataset-label-derivation.md` (L147–148) · `safety-state-design.md` (L79, **L104** — the "critical safety boundary" claim) · `formal-model.md` (**L29** three-zone text, **L287** surjectivity) · `CLAUDE.md` (L237, L266) · `notes/Determination of risk perception….md`

**Missing from the SDR's list — all verified present:**

| # | Document | Site |
|---|---|---|
| 9 | **`docs/canonical/evaluation-design-rq4.md`** | L105 threshold row; **SC-10** (18:00 → CAUTION; only `g_t`-triggered scenario, becomes date-dependent — KK sunset 17:57–18:35); SC-15 (22:00, safe) |
| 10 | **`docs/canonical/architecture-illustration.md`** | L234 threshold table; scenario walkthrough (05:30, 16:30, 18:30 rows) |
| 11 | **`docs/canonical/empirical-findings-2026-09-06.md`** | §0a **"Daylight UNSAFE hours (06:00–17:00)"** — the *label* embeds the definition; F-6/F-7 tables |
| 12 | **`docs/implementation/data-source-met-malaysia.md`** | L128 threshold row |
| 13 | **`docs/canonical/finding-met-lower-boundary-gap.md`** | L94 `g_t` share row (87.55/87.63/90.96/91.10) |
| 14 | **`docs/canonical/rq5-study-design.md`** | DT-CAUTION / DT-UNSAFE scenario times |
| 15 | **`publications/active/journal-1/.../manuscript.md`** | **L183 `g_t` row** — the SDR names only `manuscript-v3.md` |
| 16 | **`publications/active/journal-1/section-5-plan.md`** | L80 |
| 17 | `docs/canonical/session-log-2026-09-06.md` | Historical record — **annotate, do not rewrite** |

### 9.3 Category-specific items

| Category | Finding |
|---|---|
| **"three zones" language** | `appendix-c` L35 (now "three governance zones" after the cleanup — still needs → two); `formal-model.md` L29 |
| **Dusk / CAUTION references** | `explainer-…md` L28 ("Dusk"), L72 |
| **18:00 scenarios** | `evaluation-design-rq4.md` **SC-10** — *the only scenario whose sole trigger is `g_t` CAUTION*; requires a date or a new trigger |
| **Time-derived CAUTION examples** | `formal-model.md` example vectors; `dataset-label-derivation.md` L148 |
| **Figures assuming 17:00–19:00** | All of §0a's time-windowed values; F-6 transition/oscillation counts; F-7 binding table; F-15 TABLE VII; manuscript-v3 TABLE VI and L455 |
| **87.63% explanations** | `appendix-c` **C.2.0.5 (D1)** — the "t ∉ D is load-bearing" argument cites 87.63%; §0a L29; L465; manuscript-v3 L455; `CLAUDE.md` L266; `finding-met-lower-boundary-gap.md` L94. **Under B: 86.82% / 90.20% — the argument survives, the number moves** |
| **"daylight" = fixed 06:00–17:00** | §0a label; `historical_replay.py` L206 label; `canonical_figures.py` L134; `diagnostic_binding.py` L121; `threshold_comparison.py` L45; P03/P05/P06/P20 register scopes. **Redefinition, not recomputation** |
| **Algorithm 1 / pseudocode** | `manuscript-v3.md` L316; `manuscript-v2.5-submitted.md` L250 (archive — annotate only); `supervisor-feedback-response.md` L69 |
| **Non-surjectivity statement** | **New text required** in `appendix-c` — components need not be surjective; `g_t` is deliberately binary (§2.3) |

**Register scopes are documents too.** P03, P05, P06 and P20 carry `"daylight 06-17"` in their `scope` field. Re-resolution must state that the scope *definition* changed, not merely the value.

---

## 10. Integrity check

**This audit was read-only. No file was created other than this finding.**

| Item | Status | Verification |
|---|---|---|
| Canonical `g_t` | ✅ **UNCHANGED** | `06:00 ≤ t < 17:00` / `17:00 ≤ t < 19:00` / `19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00` |
| Appendix C | ✅ **UNCHANGED** | Read only |
| Scripts | ✅ **UNCHANGED** | `g_t` logic identical in all 8 sites |
| Replay outputs | ✅ **UNCHANGED** | Nothing executed |
| Sensitivity outputs | ✅ **UNCHANGED** | `scripts/sensitivity/` unmodified; nothing re-run |
| Figures | ✅ **UNCHANGED** | 7.72% present 8× in §0a |
| Prediction register | ✅ **UNCHANGED** | 24 entries, 22 CONFIRMED / 2 REFUTED · `sha256 538808b6d82249fa…` |
| All prediction outcomes | ✅ **UNCHANGED** | None re-resolved |
| **SDR-001** | ✅ **DRAFT — NOT APPROVED — NOT APPLIED** | "Status: DRAFT. Not applied. Requires approval." |
| Model B | ✅ **NOT ADOPTED** | |

*The five files modified earlier today belong to the completed semantic cleanup, not to this audit.*

---

## 11. Conditions that must be satisfied before canonical migration

### 11.1 Before **approval** — 1 condition

| | Condition |
|---|---|
| **C-0** | ✅ **CLOSED 2026-09-08.** **Correct SDR-001's Decision clause to name the algorithm that was actually validated.** It said "Meeus"; the 0.9-min USNO validation certifies the local implementation in `scripts/sensitivity/solar.py` (§4.1). **Resolved by preserving the validated implementation and correcting the wording** — the Decision clause, Part 2 and §1.3 of `finding-gt-evidence-closure.md` now name it *"NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`"*, with USNO named as validation authority only. Meeus was **not** implemented to rescue the prior wording. See `cleanup-report-c0-solar-provenance-2026-09-08.md`. |

> **⚠️ Terminology note added 2026-09-08.** This audit uses the hybrid **"NOAA/Spencer"** in §4.1, §4.2 and §11 to describe the code's mathematical form. **That phrasing is superseded.** The Fourier-series form is real and is what distinguishes the code from Meeus — the diagnosis stands — but **no project source establishes a Spencer citation**, so a hybrid name overstates the provenance the project holds. The agreed term is **"NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`"**, with the exact published reference recorded as an open **C-1** item. *This audit's text is annotated rather than rewritten: it is the record of how the defect was found, and the finding it reports is unchanged.*

### 11.2 Before **canonical migration** — 8 conditions

| | Condition | Closes |
|---|---|---|
| **C-1** | **Pin the solar implementation**: version/commit identifier, published reference, lat/lon (**resolve 116.07 vs 116.01**), timezone and UTC conversion, leap-year date handling, zenith constant, rounding rule, `⊥`/invalid-input behaviour, and the half-open boundary rule. 4 of 12 checklist items are absent today | §4.2 |
| **C-2** | **Record the USNO validation in the specification**, including the **28 per-event reference values** — not only the summary statistics — so it is re-verifiable without a live API call | §4.3 |
| **C-3** | **Store the computed solar timestamps per replay day** (`date, sunrise_local, sunset_local`) and make every published figure re-derivable from stored inputs plus the pinned version. Required by the 160/60 near-boundary days | §4.4 |
| **C-4** | **Accept the SAFE→UNSAFE step cost (2 → 1,536) as a design position** and write it into Threats to Validity. Record that `g_t` is deliberately two-state, with an explicit non-surjectivity statement in Appendix C | §1, §2, §3 |
| **C-5** | **Run the hysteretic classifier in three stages** — v1/incumbent (must reproduce **7.83**), v2/incumbent, v2/Model B — before re-resolving **P12**. Also covers P09, P10, P11, P13 | §7 |
| **C-6** | **Re-resolve the 16 computable predictions** under the §8 protocol, applying the isolation rule to P09–P13 and recording both magnitudes | §5, §6, §8 |
| **C-7** | **Reconcile the baseline discrepancy** — the findings quote P07 88.23 / P10 227 / P11 70 / P12 6.17 against register values **87.58 / 230 / 37 / 7.83**. Correct the findings and `CLAUDE.md` to the register before comparing anything to them | §5.2 |
| **C-8** | **Execute the corrected propagation list** — **8 scripts** (add `threshold_comparison.py`) and **~17 documents** (add `evaluation-design-rq4.md` incl. **SC-10**, `architecture-illustration.md`, `empirical-findings` §0a labels, `data-source-met-malaysia.md`, `finding-met-lower-boundary-gap.md`, `rq5-study-design.md`, **Journal 1 manuscript L183**, `section-5-plan.md`). Treat **"daylight" as redefined, not recomputed** | §9 |

### 11.3 Recorded, out of scope for SDR-001

- **Anticipatory sunset notification** — a UI/notification item, deliberately kept outside the governance state (§3.2).
- **`cause` taxonomy mismatch** — provenance-only; separate workstream, per the OPEN note now in Appendix C C.2.0.8.

---

## 12. Closing assessment

**The decision is sound and the audit did not find a reason to refuse it.** Model B is the only regulation-derived option, the incumbent is wrong in a checkable way (SAFE begins at 06:00; sunrise is 06:01–06:34, so SAFE currently begins before sunrise **every day of the year**), and the headline moves downward — the fourth provenance correction in this project to cost the result rather than flatter it.

**What is not ready is the execution scaffolding**, and one gap sits inside the approval document itself. The Meeus/NOAA discrepancy is small in substance and large in principle: it is the same shape as the 7.5 mm/hr error — a value in the code and a different justification in the document, with nothing comparing them. Catching it before approval rather than after publication is the whole point of having this gate.

**Two findings that reduce migration risk, worth stating plainly:** P21 — the F-15 result answering Review 3 — is **structurally immune** to this decision, because C1 and C3 are the identical map (§5.1). And system-level graduation is untouched: **2,091 CAUTION hours remain, every one of them weather-driven** (§1.2). The contribution is not at risk from this change.

**One that increases it:** the baseline discrepancy in §5.2 means the migration would have been executed against four wrong numbers had it proceeded from the SDR's own table.

> ## **READY WITH EXECUTION CONDITIONS**
> **C-0 before approval. C-1 through C-8 before canonical migration.**
> **SDR-001 remains DRAFT — NOT APPROVED — NOT APPLIED.**

---

## 13. Sources

`docs/canonical/finding-gt-sensitivity-analysis.md` (§1–§8) · `docs/canonical/finding-gt-evidence-closure.md` (Parts 1–8, SDR-001 draft) · `docs/canonical/finding-gt-provenance-audit.md` · `docs/canonical/finding-gt-operational-semantics.md` (§5, §6) · `docs/canonical/finding-unsafe-semantics-audit.md` · `docs/canonical/cleanup-report-unsafe-semantics-2026-09-08.md` · `docs/canonical/appendix-c-formalisation.md` (Definition C.1, C.2, C.2.0.5, C.2.0.8, C.7.2, C.8.2, C.9.4) · `docs/canonical/empirical-findings-2026-09-06.md` §0a · `docs/canonical/evaluation-design-rq4.md` · `data/prediction-register.csv` (all 24 entries) · `scripts/sensitivity/solar.py` · `scripts/hysteresis_analysis.py` · `scripts/condition_comparison.py` · `scripts/canonical_figures.py` · `scripts/threshold_comparison.py` · COLREGs Rule 20(b) · USNO Astronomical Applications API v4.0.1 · Meeus, *Astronomical Algorithms* (2nd ed., 1998) · Spencer (1971) / NOAA GML solar calculator · Atacan & Düzbastılar (2023)
