# Session Log — 2026-09-08

**Subject:** The `g_t` provenance problem, from discovery to a partially-executed migration.
**Outcome:** SDR-001 **APPROVED — NOT YET APPLIED**. Six of eight execution conditions closed. **Canonical `g_t` unchanged throughout.**

> ### Read this first
>
> **Nothing was migrated.** The canonical classifier is still the incumbent fixed clock — SAFE 06:00–17:00 · CAUTION 17:00–19:00 · UNSAFE otherwise. **7.72% / 5.98% remain the authoritative published figures.** The prediction register is **byte-for-byte unchanged**, `sha256 538808b6d82249fa…`, across every task in this session.
>
> **Two conditions remain open: C-6 and C-8.** Resume there.

---

## 1. Where this started

`g_t` carries **87.63% of all non-SAFE classifications** — more than every other component combined — and its boundaries (06:00, 17:00, 19:00) had **no located source**. The most load-bearing component in the classifier had the thinnest provenance in the specification.

That is the whole session in one sentence. Everything below follows from pulling on it.

---

## 2. What was done, in order

| # | Task | Outcome |
|---|---|---|
| 1 | **`UNSAFE` semantics audit** (read-only) | **Outcome B** — Model B formally compatible, clarification required |
| 2 | **Pre-adoption semantic cleanup** | 4 contradictions closed; `UNSAFE` redefined by governance consequence |
| 3 | **SDR-001 readiness audit** (read-only) | **READY WITH EXECUTION CONDITIONS**; C-0 found inside the approval document |
| 4 | **C-0 — solar provenance correction** | SDR named an algorithm that was never validated. Fixed |
| 5 | **SDR-001 approval** | DRAFT → **APPROVED — NOT YET APPLIED** |
| 6 | **C-1 / C-2 / C-3 — solar reproducibility** | C-1, C-3 closed; C-2 blocked, then closed separately |
| 7 | **C-2 — USNO validation artefact** | Reconstructed 28-row artefact adopted, historical record retained |
| 8 | **C-4 — design consequences** | Non-surjectivity formalised; step cost disclosed |
| 9 | **C-5 — three-stage hysteretic isolation** | Gate passed; P12 computed; data and `g_t` effects separated |
| 10 | **C-7 — baseline reconciliation** | One cause found for every stale value |

---

## 3. The findings that changed the specification

### 3.1 `UNSAFE` was defined by a conjunction, and half of it was false

Definition C.1 said UNSAFE means *"departure lies outside the demonstrated operating envelope **and** no AI advisory output is permissible"* — a world claim conjoined with a governance claim.

**A failed sensor feed produces UNSAFE while the sea is flat.** Route 2 of the fail-safe makes the envelope half vacuous. The definition now reads by governance consequence alone, with three enumerated routes to the state:

1. observation outside a supported operating envelope
2. **fail-safe on a required observation** (`yᵢ = ⊥`)
3. an explicitly defined conservative governance condition

**All formal consequences unchanged:** `G(UNSAFE) = 0`, `A_AI(UNSAFE) = ∅`, Theorem C.3, human override unconditional.

### 3.2 Operator-facing messages asserted danger the state does not establish

*"Dangerous conditions — return to shore"* and *"dangerous conditions — do not depart"* were **false at 19:00 on a calm night under the incumbent classifier**, before Model B entered the picture. Both instructed the operator, contradicting unconditional human authority asserted in five documents.

Replaced with state-reporting wording. The sweep found **two more instances not in the audit's list**, including the **RQ5 study stimulus** — where a message asserting danger would have confounded the exact measurement RQ5 exists to make.

### 3.3 The SDR named an algorithm nobody had validated — **C-0**

SDR-001's Decision clause said sunrise/sunset were computed *"by the **Meeus** algorithm, validated against USNO"*. `solar.py` implements a **truncated Fourier series in the day angle** — no Julian century, no geometric mean longitude, no equation of centre. Searched all 39 lines for every Meeus construct: **zero matches**.

**The 0.9-minute validation certified a different algorithm.** Approving the clause as drafted would have authorised something the project has never validated.

**Resolved by preserving the implementation and correcting the wording** — evidence follows implementation, not the reverse. Meeus was *not* implemented to rescue the prior text.

### 3.4 The site coordinate had no provenance — **C-1**

The question looked like "116.07 or 116.01". It was **four longitudes**:

| | |
|---|---|
| **116.01** | Requested in all three collection scripts and `data-provenance.md` |
| 116.025 / 116.0 / 116.04167 | Delivered grid cells — Open-Meteo snaps per variable |
| **116.07** | `solar.py` default — **matches nothing** |

**Resolved to 5.98° N, 116.01° E** on a stated rule: solar events belong to the *location*, not to a data grid cell, and since the three cells disagree none can represent the site.

### 3.5 A validation that could not be reproduced — **C-2**

**The 28 per-event USNO values were never stored.** Only summary statistics survived. Nothing was fabricated; a controlled re-query produced a complete artefact, explicitly labelled `RECONSTRUCTED-2026-09-08`.

It **does not reproduce the record** — max 0.92 against 0.90 — and the cause was demonstrated, not assumed: USNO reports whole minutes, so a 14-second coordinate difference flips reference values at rounding boundaries.

**Closed non-destructively.** `V_historical` retained as *"historically reported, underlying comparison artefact unavailable"*; `V_reconstructed` adopted for reproducibility.

**New information the row-level data made available:** mean *signed* difference **+0.0064 min** — no systematic bias — and for the **sunrise/sunset events Model B actually reads**, max **0.75 min**, not 0.92. The 0.92 maximum is a civil-dusk event the classifier never evaluates.

### 3.6 Every "stale baseline" had one cause — **C-7**

The readiness audit reported **"four wrong baselines"**. They are not four errors. **One superseded threshold vintage** (v1 data, `r_CAUTION = 7.5 mm/hr`, small-vessel `o_UNSAFE = 1.9 m`) reproduces **all five** exactly:

| | Pre-amendment vintage | Current thresholds |
|---|---|---|
| P07 | **88.23** ✅ | **87.58** ✅ ← register |
| P09 | **5,416** ✅ ← register | **5,220** ✅ |
| P10 | **227** ✅ | **230** ✅ ← register |
| P11 | **70** ✅ | **37** ✅ ← register |
| P12 | **6.17** ✅ | **7.83** ✅ ← register |

**The anomaly is narrower than reported and sits in the register:** P09 alone carries a pre-amendment value, hand-restored, while its four neighbours carry post-amendment ones.

**Consequence — a corrected attribution:**

> **5,416 —(threshold −196)→ 5,220 —(data −19)→ 5,201 —(g_t −1,540)→ 3,661**

**Δ_data was reported as −215. It is −19.** An elevenfold error in an attributed effect, caught before C-6 could carry it into a re-resolution record.

---

## 4. SDR-001 — the approved design

**Approved 2026-09-08 as a design decision. Not canonical.**

```
g_t : [0, 24) ∪ {⊥} → {SAFE, UNSAFE}
      SAFE     sunrise(date, φ, λ) ≤ t < sunset(date, φ, λ)
      UNSAFE   otherwise
      UNSAFE   t = ⊥
```

**Evidence and policy, kept apart** — this is the part most likely to be pressed at viva:

| Established by evidence | Decided by policy |
|---|---|
| Night navigation carries **elevated** risk (4.08 vs 3.43; 12.80 vs 8.53) | **night ⇒ `g_t` = UNSAFE ⇒ AI abstention** |
| COLREGs Rule 20(b) defines sunset-to-sunrise **for navigation lights** | |
| The incumbent 06:00/17:00/19:00 have **no source** | |
| **No source supports a twilight CAUTION band** | |

**No source establishes the implication.** COLREGs regulates lights; Atacan & Düzbastılar measured accident perception. Neither speaks to advisory systems. The withdrawal is a conservative governance choice, approved *as policy* — and the incumbent is equally policy-defined, on worse provenance.

**Accepted cost, disclosed not softened:**

| | Incumbent | Model B |
|---|---|---|
| Direct SAFE→UNSAFE transitions | **2** | **1,536** |
| `g_t`-driven SAFE→CAUTION | **1,545** | **0** |

**System-level graduation survives:** 2,091 CAUTION hours (4.77%), all weather-driven. Component classifiers are **not required to be surjective** — now stated formally in Appendix C C.2, with a per-theorem verification table.

---

## 5. Execution condition status

| | Condition | Status |
|---|---|---|
| **C-0** | Correct the algorithm provenance in the SDR | ✅ **CLOSED** |
| **C-1** | Pin the solar implementation | ✅ **CLOSED** — `solar-spec-v1`, `solar-v1`, 12/12 checklist items |
| **C-2** | 28-row USNO validation artefact | ✅ **CLOSED** — reconstructed, historical retained |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — 1,827 rows, both configurations |
| **C-4** | Document design consequences | ✅ **CLOSED** — C.2 non-surjectivity, C.9.5 cost, C.9.6 notification |
| **C-5** | Three-stage hysteretic isolation | ✅ **CLOSED** — gate passed, P12 computed |
| **C-6** | **Re-resolve affected predictions** | 🔴 **OPEN** |
| **C-7** | Baseline reconciliation | ✅ **CLOSED** |
| **C-8** | **Execute the propagation list** | 🔴 **OPEN** |

---

## 6. C-5 result — P12 and the isolated effects

**Provenance gate: Stage 1 reproduced P12 = 7.83 exactly** (|diff| 0.0000). That is what licensed Stages 2 and 3.

| Metric | v1/incumbent | v2/incumbent | v2/Model B | **Δ_data** | **Δ_g_t** |
|---|---|---|---|---|---|
| **P12** hysteresis reduction | **7.83%** | **8.70%** | **10.36%** | **+0.87** | **+1.66** |
| P09 total transitions | 5,220 | 5,201 | 3,661 | −19 | −1,540 |
| P10 non-scheduled | 230 | 207 | 222 | −23 | +15 |
| P11 oscillations | 37 | 27 | 26 | −10 | −1 |

**Hysteresis becomes *more* effective under Model B**, because removing the time-driven CAUTION band leaves a higher proportion of non-scheduled transitions in the wave and rainfall components hysteresis actually governs.

**Settled from the code:** hysteresis applies to `g_o` and `g_r` only, at component level before max-severity. **It never touches `g_t`** — so the Model B sunset transition is neither delayed nor amplified. No sunset hysteresis was invented.

---

## 7. Artefacts created

**Findings and reports — `docs/canonical/`**

`finding-unsafe-semantics-audit.md` · `cleanup-report-unsafe-semantics-2026-09-08.md` · `finding-sdr-001-readiness-audit.md` · `cleanup-report-c0-solar-provenance-2026-09-08.md` · `approval-report-sdr-001-2026-09-08.md` · `report-c1-c2-c3-solar-reproducibility-2026-09-08.md` · `report-c2-closure-2026-09-08.md` · `report-c4-closure-2026-09-08.md` · `report-c5-closure-2026-09-08.md` · `report-c7-closure-2026-09-08.md`

**Frozen data artefacts**

| Path | Rows | Purpose | sha256 |
|---|---|---|---|
| `data/solar/usno-validation-2026-09-08.csv` | 28 | C-2 validation record | `da14a8dc…` |
| `data/solar/solar-events-daily.csv` | 1,827 | C-3 daily solar events | `057c46a1…` |
| `data/solar/solar-boundary-audit.csv` | 2 | C-3 boundary verification | — |
| `data/c5/c5-three-stage-metrics.csv` | 3 | C-5 stage metrics | `3566cd6b…` |
| `data/c5/c5-three-stage-deltas.json` | — | C-5 isolated effects | `23de3c07…` |
| `data/c5/c5-run-manifest.json` | — | C-5 provenance authority | `1f04720c…` |
| `data/c7/baseline-provenance.csv` | 5 | C-7 baseline matrix | `d5db567c…` |

**Scripts — new, isolated, non-canonical**

`scripts/solar/build_solar_artefacts.py` · `scripts/c5/three_stage_hysteresis.py`

---

## 8. Canonical documents amended

| Document | Change |
|---|---|
| `appendix-c-formalisation.md` | Definition C.1 redefined by governance consequence; C.9.4 rescoped; **C.2 non-surjectivity statement**; **new C.9.5** accepted transition cost; **new C.9.6** notification separation; `g_t` basis column and C.1 daylight wording corrected; `cause` OPEN note |
| `architecture-illustration.md` | Three operator-message corrections |
| `rq5-study-design.md` | DT-UNSAFE stimulus wording |
| `finding-gt-evidence-closure.md` | SDR-001 approved; C-0/C-1/C-2/C-3/C-4/C-5/C-7 rows closed; Part 2 two-evidence-object header; Part 7 baselines corrected |
| `justification/formal-model.md` | `f` surjectivity claim scoped into three distinct statements |
| `justification/viva-formalisation-architecture.md` | Maritime-authority claim removed |
| `manuscript-v3.md` | **Threats to Validity — step-cost disclosure** |
| `CLAUDE.md` | `g_t` block rewritten with the do-not-implement guard; F-6 figures corrected to 5,220 / 37 / 7.83% |

**Historical records annotated, never rewritten:** `session-log-2026-09-06.md`, `decision-record-empirical-first.md`, `finding-gt-provenance-audit.md`, `finding-gt-operational-semantics.md`, `finding-gt-sensitivity-analysis.md`, `finding-sdr-001-readiness-audit.md`.

The sequence stays visible: **provenance audit → semantics audit → readiness audit → C-0 → approval → C-1/C-2/C-3 → C-4 → C-5 → C-7**.

---

## 9. Resume here

### C-6 — re-resolve affected predictions

**Baseline authority rule** (from C-7, mandatory): original prediction text and expected band preserved; new actual computed under the new canonical specification; historical actuals never overwritten. Eight fields per re-resolution record.

**Comparable baselines** — use `data/c7/baseline-provenance.csv`:

| Prediction | Compare from |
|---|---|
| P07 · P10 · P11 · P12 | Register value (reproduces) |
| **P09** | **5,220**, not the registered 5,416 — **field 5 mandatory** |

> ⚠️ **C-6 must not label 5,416 → 3,661 as a `g_t` effect.** That would overstate SDR-001's impact by **14×**. The decomposition is threshold −196, data −19, `g_t` −1,540.

C-5's frozen artefacts are the authority; no re-run needed unless a contradiction appears.

### C-8 — propagation

**8 scripts** (including `threshold_comparison.py`, missing from the SDR's original list of 7) and **~17 documents** (including `evaluation-design-rq4.md` **SC-10** — its only CAUTION trigger is `g_t` at 18:00, which becomes date-dependent — and the **Journal 1 manuscript**, omitted from the original list).

**"Daylight" is redefined, not merely recomputed.** It is currently *defined* as `g_t` = SAFE (06:00–17:00).

**Also queued for C-8:**

- Journal 1 manuscript lines 573, 628 — stale F-6 figures (5,416 / 70 / 6.2%)
- The publication-reference gap for the solar formulation (C-1 recorded it; not yet citable to a specific publication)
- Imprecise attributions in `solar.py`, `gt_counterfactual.py` and sensitivity §7 docstrings

### Separate workstreams, unblocked but unscheduled

- **`cause` taxonomy mismatch** — a `g_t`-driven UNSAFE at 19:00 on a calm night is assigned `hazard`. Provenance-only, no theorem affected, **pre-existing under the incumbent**. OPEN note in Appendix C C.2.0.8.
- **Anticipatory sunset notification** — UI/notification design. C.9.6 records the separation and forbids inventing a warning interval.
- **`ageᵢ`** still unspecified. Layer 3 rule engine (Q8) still unimplemented.

---

## 10. What this session is really a record of

Four defects were found, and **three of them shared a shape**: a value in the code with a different justification in the document, and nothing comparing the two.

- **7.5 mm/hr** — the original instance, found before this session.
- **116.07** — a coordinate in `solar.py` that matched nothing, cited by three findings as the site.
- **"Meeus"** — an algorithm named in an approval document, never implemented, carrying a validation that belonged to different code.
- **P09 = 5,416** — a correct figure from a superseded threshold vintage, read as a data effect.

The fourth is different in kind but the same in consequence: **a validation recorded only as a summary became unreproducible within days**, not because anyone erred, but because the evidence behind it was never stored.

**None of these was caught by the analysis producing the numbers.** Each was caught by a gate that asked *what exactly does this claim, and does the evidence cover it* — the readiness audit, the C-0 provenance check, the C-5 Stage-1 gate. That is the argument for keeping the gates even when they feel procedural.

**The register survived all of it byte-for-byte.** `sha256 538808b6d82249fa…`, identical from the first task to the last.

---

**SDR-001: APPROVED — NOT YET APPLIED · Model B: SELECTED — NOT YET CANONICAL · canonical `g_t`: incumbent, unchanged · C-6 and C-8: OPEN.**
