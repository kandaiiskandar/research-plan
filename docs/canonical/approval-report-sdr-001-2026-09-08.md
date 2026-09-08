# Approval Report: SDR-001 — `g_t` Solar-Event Two-State Classifier

**Date:** 2026-09-08
**Action:** Formal approval of SDR-001 as a **design decision**
**Scope:** Status change and decision record only. **This is NOT the canonical migration of Model B.** C-1…C-8 not executed. Canonical classifier unmodified.

---

## 1. Precondition verification — all six satisfied

Verified before any change was made.

| # | Precondition | Result | Evidence |
|---|---|---|---|
| 1 | **`UNSAFE` semantic cleanup complete** | ✅ | `cleanup-report-unsafe-semantics-2026-09-08.md` exists; Definition C.1 now defines UNSAFE as *"the governance state in which AI advisory participation is not admissible"*. L1–L4 all closed |
| 2 | **Model B formally compatible with the architecture** | ✅ | `finding-unsafe-semantics-audit.md` line 377 — **Outcome B**, compatible with clarification; clarification since delivered. No theorem, type or proof requires component surjectivity |
| 3 | **Readiness verdict = READY WITH EXECUTION CONDITIONS** | ✅ | `finding-sdr-001-readiness-audit.md` lines 10 and 512 |
| 4 | **C-0 CLOSED** | ✅ | `cleanup-report-c0-solar-provenance-2026-09-08.md` line 178; readiness audit lines 142 and 478 |
| 5 | **SDR no longer claims the validated implementation is Meeus** | ✅ | Decision clause: `grep "Meeus algorithm"` → **0**. Now names *"NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`"* |
| 6 | **C-1 … C-8 remain OPEN** | ✅ | All eight marked OPEN in the C-0 cleanup report; all eight now carried into the approved SDR as binding execution conditions |

**No discrepancy found. Approval proceeded.**

---

## 2. Exact status change

| | Before | After |
|---|---|---|
| **Part 6 heading** | "DRAFT Specification Decision Record — **NOT APPLIED**" | "Specification Decision Record — **APPROVED, NOT YET APPLIED**" |
| **SDR title** | "SDR-001 **(DRAFT)**" | "SDR-001" |
| **Status line** | "**Status: DRAFT. Not applied. Requires approval.**" | "# **Status: APPROVED — NOT YET APPLIED**" |
| **Document header** | "Evidence closure + **DRAFT** decision record. Nothing applied." | "Evidence closure + SDR-001 — **APPROVED, NOT YET APPLIED**" |

**Decision metadata recorded:**

| Field | Value |
|---|---|
| Status | **APPROVED — NOT YET APPLIED** |
| Approved | 2026-09-08 |
| Prior status | DRAFT — NOT APPROVED — NOT APPLIED (superseded 2026-09-08) |
| Decision type | **Design decision** — selects the replacement design for `g_t` |
| Canonical status | ❌ **NOT canonical.** Incumbent fixed-clock `g_t` remains the canonical and runtime specification |
| Approval basis | Readiness verdict **READY WITH EXECUTION CONDITIONS**; **C-0 CLOSED** |
| Blocking conditions | **C-1 … C-8 — all OPEN** |

**What the approval establishes:** Model B is the **selected replacement design** for `g_t`. The open design question — *should `g_t` be graduated at all?* — is answered **no**. No further design deliberation is needed; what remains is execution.

**What it does not establish:** any change to the runtime or canonical specification, any published figure, any prediction outcome, or Appendix C. **Approval sets direction, not state.**

---

## 3. Approved design decision

```
g_t : [0, 24) ∪ {⊥} → {SAFE, UNSAFE}

             ⎧ SAFE     sunrise(date, φ, λ) ≤ t < sunset(date, φ, λ)
    g_t(t) = ⎨ UNSAFE   otherwise
             ⎩ UNSAFE   t = ⊥
```

**Recorded as approved; NOT inserted into Appendix C or any canonical script.** Verified: `grep -ci "sunrise|sunset|USNO|Meeus"` on `appendix-c-formalisation.md` → **0**.

**`g_t` is deliberately binary.** It produces no CAUTION output. This is an approved design position, not an omission: three independent reviews located no source supporting a time-based intermediate state.

**The architecture remains three-state.** `𝒮 = {SAFE, CAUTION, UNSAFE}` is unchanged, and other component classifiers continue to produce CAUTION. Component classifiers are not required to be surjective — type declarations state a codomain, not an image; Theorem C.1 requires each `gᵢ` to be *total*, not onto; C.2, C.3, `G(S)` and `A_AI(S)` never reference component structure.

---

## 4. Evidence / policy distinction — recorded in the SDR

### What the evidence establishes

| Claim | Source |
|---|---|
| Night navigation carries **elevated operational risk** — probability 4.08 vs 3.43, consequence 12.80 vs 8.53 against a daytime baseline | Atacan & Düzbastılar (2023) |
| **COLREGs Rule 20(b) provides an authoritative maritime sunset-to-sunrise boundary** — for **navigation-light requirements** | COLREGs Rule 20(b) |
| The incumbent **06:00 / 17:00 / 19:00 lack direct evidential support** — no source across five priority tiers states any of the three values | `finding-gt-provenance-audit.md` |
| **No evidence supports the incumbent 17:00–19:00 CAUTION band** | Three independent reviews |

### What architecture policy decides

> **night-time ⇒ `g_t` = UNSAFE ⇒ AI advisory abstention**

**Recorded explicitly as an architectural governance policy choice. No source establishes this implication.**

The SDR now states, in terms:

- **COLREGs does not require AI abstention** — it regulates when navigation lights must be exhibited, and is used here *only* as the boundary definition.
- **Atacan & Düzbastılar do not require AI abstention** — they measure accident risk perception in a bridge simulator and say nothing about advisory systems.
- **Neither source establishes that night operation is physically prohibited or universally unsafe**, and the record makes no such claim. Fishers demonstrably operate at night. `S = UNSAFE` sets `G(S) = 0` and `A_AI(S) = ∅` — *the AI does not advise* — and **human decision authority remains unconditional**.

**The policy is approved as policy.** It follows the architecture's stated principle of conservative over-approximation, and the project already carries `UNSAFE` boundaries set on interpretive grounds and labelled as such. Worth recording: **the incumbent `g_t` is equally policy-defined, with strictly worse provenance** — policy on unsourced numbers, versus policy on a regulated boundary.

---

## 5. Accepted design cost — recorded in full, not softened

| Measure (PRIMARY, 43,848 h) | Incumbent | **Model B** |
|---|---|---|
| **Direct SAFE→UNSAFE transitions** | **2** | **1,536** |
| **SAFE→CAUTION caused by `g_t`** | **1,545** | **0** |
| CAUTION→UNSAFE by `g_t` | 1,724 | 186 |
| `g_t` transitions/day | 2.73 | 1.88 |

**Accepted as a design trade-off.** The architecture's own thesis is that graduated governance beats a binary step, and Model B makes the most predictable transition of the day a step. That tension is real and is recorded rather than explained away.

**Assessed in four framings:** formally acceptable (no theorem constrains transition paths; a two-level jump is monotone under Theorem C.2); architecturally acceptable (governance remains graduated; `g_t` is simply not a graduated variable); not empirically problematic (the most predictable event in the system; oscillations fall 27 → 26); **primarily a usability concern**.

> **Binding disclosure obligation:** the 2 → 1,536 figure must appear in **Threats to Validity**, stated plainly, not absorbed into surrounding text. Recorded as **C-4**.

---

## 6. System-level graduation remains intact

**Confirmed.** Under Model B the PRIMARY replay still produces:

> ### **2,091 global CAUTION hours (4.77% of all hours) — all weather-driven**

Every one arises from `g_o` or `g_r`. What is removed is *time-driven* CAUTION, for which no evidence was ever found.

The containment property `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` is untouched, CAUTION remains materially reachable, and the CS contribution — a two-level governance pair with an intermediate advisory mode — is unaffected. **Arguably the interpretation improves:** every remaining CAUTION hour becomes a weather CAUTION.

### Anticipatory notification — kept separate, recorded out of scope

A pre-sunset notification **may be considered later** and is **not** part of this decision. **No UI implementation is required or authorised here.** If pursued it must remain separate from `g_t`:

> **governance state ≠ anticipatory UI notification**

**No artificial CAUTION interval may be created to provide warning.** Reinstating a time-based band to soften the transition would be adopting a band *because it yields a middle state* — the stated reason for rejecting Model C, and the failure mode this project has refused repeatedly (7.5 mm/hr, `g_v`, the 1.9 m threshold).

---

## 7. Solar provenance wording retained

The approved SDR carries the corrected C-0 terminology unchanged:

> **NOAA-style low-precision solar-position formulation implemented in `scripts/sensitivity/solar.py`**
> Validation authority: **USNO Astronomical Applications API v4.0.1** — 28 comparisons, max 0.9 min, mean 0.37 min; sunrise/sunset alone max 0.9 min, mean 0.35 min.
> **USNO is the independent reference, not the algorithm source.**

**None of `Meeus`, `NOAA/Meeus`, `Meeus/NOAA`, `NOAA/Spencer` was reintroduced.** Verified: `grep "Meeus algorithm"` on the Decision clause → **0**.

**`solar.py` unmodified** — `sha256 3b7dc371ebe5931b…`, identical to its pre-approval hash.

---

## 8. C-1 through C-8 — all OPEN, all binding

Carried into the approved SDR as a table headed *"Model B cannot become canonical until C-1 through C-8 are discharged."* Verified: **8 rows marked 🔴 OPEN.**

| | Condition | Status |
|---|---|---|
| **C-0** | Correct algorithm provenance in the Decision clause | ✅ **CLOSED 2026-09-08** |
| **C-1** | Pin the solar implementation; resolve all reproducibility parameters — exact published reference, version/commit, **longitude 116.07 vs 116.01**, leap-year handling, timezone documentation, invalid-input/`⊥` behaviour, rounding, zenith constants, boundary rule | 🔴 **OPEN** |
| **C-2** | Record the complete USNO validation artefact, **all 28 per-event values** | 🔴 **OPEN** |
| **C-3** | Store per-day solar timestamps; make replay reproducible from stored inputs + pinned version | 🔴 **OPEN** |
| **C-4** | Document binary `g_t`, system-level graduation, accepted SAFE→UNSAFE cost | 🔴 **OPEN** |
| **C-5** | Three-stage hysteretic re-run for P12: **v1/incumbent → v2/incumbent → v2/Model B** | 🔴 **OPEN** |
| **C-6** | Re-resolve affected predictions under the established protocol | 🔴 **OPEN** |
| **C-7** | Reconcile baselines — register authoritative: **P07 87.58 · P10 230 · P11 37 · P12 7.83** | 🔴 **OPEN** |
| **C-8** | Execute the propagation list — 8 scripts, ~17 documents | 🔴 **OPEN** |

**None executed. Approval discharged none of them.**

---

## 9. Canonical migration has NOT occurred

The approved SDR carries an explicit gate:

> # **APPROVAL DOES NOT AUTHORISE CANONICAL MIGRATION.**
>
> Canonical migration may begin **only** through a separate controlled task that explicitly executes C-1 through C-8.

**Verified by direct inspection, not assertion:**

| Check | Result |
|---|---|
| Solar terms in `appendix-c-formalisation.md` | **0** |
| `g_t` in `canonical_figures.py` | Unchanged — `sha256 5af9eaf7f4420180…` |
| `g_t` in `condition_comparison.py` | Unchanged — `1f0f4e9cd2868820…` |
| `g_t` in `diagnostic_binding.py`, `historical_replay.py`, `hysteresis_analysis.py` | Unchanged |
| Any script executed | **None** |
| Any figure regenerated | **None** |

---

## 10. Incumbent `g_t` remains canonical

> **`g_t^canonical` = `g_t^incumbent`**
> SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE 19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00

Verified verbatim in `appendix-c-formalisation.md` lines 505–507.

**Authoritative published figures — unchanged and still to be reported:**

| | |
|---|---|
| **PRIMARY Level 2 binding** | **7.72%** — 8 occurrences intact in §0a |
| **RESOLUTION Level 2 binding** | **5.98%** — 5 occurrences intact |

**The Model B sensitivity values (5.81% / 4.48%) were NOT substituted anywhere.** They remain counterfactual, produced by non-canonical analysis code, and are labelled as such.

---

## 11. Prediction-register integrity

> ### **BYTE-FOR-BYTE UNCHANGED — `sha256 538808b6d82249fa…`**

Identical to the hash recorded in the readiness audit *before* the C-0 correction and before this approval.

| Check | Result |
|---|---|
| Entries | **24** |
| Outcomes | **22 CONFIRMED / 2 REFUTED** |
| Prediction text | Unchanged |
| Expected bands | Unchanged |
| Actual values | Unchanged — P07 **87.58** · P09 **5416.0** · P10 **230.0** · P11 **37.0** · P12 **7.83** · P18 **8.32** · P19 **6.1** |
| Status fields | Unchanged |
| Register notes | Unchanged |
| P09, P12, P18, P19 | **Untouched** |

**The register remains the record of the current canonical architecture** — the incumbent `g_t` — until controlled re-resolution under C-5, C-6 and C-7. Part 7 of the SDR now states this explicitly, so approval cannot be misread as licensing re-resolution.

---

## 12. Files changed — 3

| File | Change |
|---|---|
| `docs/canonical/finding-gt-evidence-closure.md` | Status DRAFT → **APPROVED — NOT YET APPLIED**; decision metadata block; migration gate; deliberately-binary + three-state note; evidence/policy rationale section; accepted-cost section; out-of-scope notification section; C-1…C-8 execution-conditions table; prediction-register note; header updated |
| `docs/canonical/finding-sdr-001-readiness-audit.md` | **Status annotation only** — records that SDR-001 was approved on this verdict and that C-1…C-8 remain open. **The audit itself is not rewritten** |
| `CLAUDE.md` | `g_t` open block replaced with the approved-but-not-canonical status, the do-not-implement guard, and the corrected solar terminology |

Plus this report. **No script, dataset, figure or register file modified** — confirmed by mtime and by hash.

### Historical integrity

**No historical finding was rewritten.** The provenance audit, operational-semantics review, sensitivity analysis, `UNSAFE` semantics audit and readiness audit all stand as written — they are the record of the sequence through which the decision was reached. Where a pointer was needed, a short dated status annotation was added instead of an edit.

---

## 13. Final integrity verification

| Item | Status | Evidence |
|---|---|---|
| **Canonical Appendix C `g_t`** | ✅ **UNCHANGED** | Lines 505–507 verbatim |
| **06:00 / 17:00 / 19:00 classifier** | ✅ **UNCHANGED** | Verified in Appendix C and all 8 script sites |
| **`solar.py`** | ✅ **UNCHANGED** | `3b7dc371ebe5931b…` |
| **All canonical scripts** | ✅ **UNCHANGED** | `canonical_figures` `5af9eaf7…` · `condition_comparison` `1f0f4e9c…` · `hysteresis_analysis` `73015d88…` · `diagnostic_binding` `69bc2bd6…` · `historical_replay` `dd6a6c3f…` · `gt_counterfactual` `eb585089…` |
| **Wind thresholds** | ✅ **UNCHANGED** | `21.6, 27.0` |
| **Rainfall thresholds** | ✅ **UNCHANGED** | `10.0, 20.0` |
| **Wave thresholds** | ✅ **UNCHANGED** | `{small:(1.0,1.25), medium:(1.4,2.8), big:(1.5,3.5)}` |
| **`cause`** | ✅ **UNCHANGED** | `cause : Y → {fault, hazard}` |
| **Replay outputs** | ✅ **UNCHANGED** | Nothing executed |
| **Sensitivity outputs** | ✅ **UNCHANGED** | Nothing re-run |
| **Figures** | ✅ **UNCHANGED** | 7.72% ×8, 5.98% ×5 |
| **Prediction register** | ✅ **BYTE-FOR-BYTE UNCHANGED** | `538808b6d82249fa…` |
| **All 24 predictions and outcomes** | ✅ **UNCHANGED** | 22 CONFIRMED / 2 REFUTED |
| **Model B in canonical spec** | ✅ **ABSENT** | 0 solar terms in Appendix C |
| **C-1 … C-8** | ✅ **ALL OPEN** | 8 rows marked OPEN |

---

## 14. Assessment

The decision this approval records is narrow and it is the right narrow thing: **Model B is the design the project will migrate to, and no further design argument is needed.** What made that decidable was the sequence — the semantic cleanup that removed the physical-danger reading of `UNSAFE`, the readiness audit that separated design justification from execution readiness, and C-0, which caught the SDR naming an algorithm nobody had validated.

**Two properties of this approval are worth keeping visible.** It is *reversible in effect* — nothing canonical moved, so an approved design that later proves unworkable costs a status line rather than a recomputation. And it is *honest about its cost*: the 2 → 1,536 step sits in the record with a binding disclosure obligation, not in a footnote.

**What remains is execution, and it is not small.** Eight conditions, including a hysteretic re-run that must be staged in three parts to avoid confounding, and a baseline reconciliation that would otherwise have had the migration comparing against four wrong numbers.

---

# **SDR-001 APPROVED — MODEL B SELECTED — NOT YET CANONICAL**

# **C-1 THROUGH C-8 REMAIN OPEN.**
