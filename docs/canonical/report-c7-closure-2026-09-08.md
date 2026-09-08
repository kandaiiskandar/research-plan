# Report: SDR-001 Execution Condition C-7 — Prediction Baseline Reconciliation

**Date:** 2026-09-08
**SDR-001:** **APPROVED — NOT YET APPLIED** · **Model B: SELECTED — NOT YET CANONICAL** · canonical `g_t` unchanged
**Scope:** C-7 only. **No prediction re-resolved. No CONFIRMED/REFUTED determined. Prediction register byte-for-byte unchanged. No canonical migration.**

---

# RESULT

# **C-7 CLOSED — PREDICTION BASELINES RECONCILED**

All fifteen closure criteria satisfied.

> ### The headline finding is simpler than expected, and better.
>
> The readiness audit described **"four wrong baselines"**. They are not four errors. They are **one coherent snapshot of a superseded threshold specification**, and **every one of them reproduces exactly** under it.
>
> **Pre-amendment vintage** — v1 data, `r_CAUTION = 7.5 mm/hr`, small-vessel `o_UNSAFE = 1.9 m` — reproduces **P07 88.23 · P09 5,416 · P10 227 · P11 70 · P12 6.17**, all five, exactly.
>
> **Current-threshold vintage** — v1 data, `r_CAUTION = 10.0`, `o_UNSAFE = 1.25` — reproduces **P07 87.58 · P09 5,220 · P10 230 · P11 37 · P12 7.83**, all five, exactly.
>
> The register holds the **current-threshold** values — **except P09**, which holds the pre-amendment one. That single exception is the entire inconsistency, and it is documented in P09's own `notes` field as a deliberate manual restoration.

---

## 1. P07 reconciliation

**Metric:** share of non-SAFE hours where `g_t` is at the maximum. **Scope:** all hours, small vessel.

Recomputed read-only across all candidate configurations. `diagnostic_binding.py` was **not executed** — like `hysteresis_analysis.py`, its `main()` writes the register unconditionally (line 197).

| Dataset | `r_CAUTION` | `o_UNSAFE` | at-max % | exclusive % | |
|---|---|---|---|---|---|
| v1 | **10.0** | **1.25** | **87.58** | 81.95 | ✅ **← register 87.58** |
| v1 | 10.0 | 1.9 | 88.35 | 86.12 | |
| v1 | 7.5 | 1.25 | 87.45 | 81.80 | |
| v1 | **7.5** | **1.9** | **88.23** | 85.97 | ✅ **← findings 88.23** |
| v2 | **10.0** | **1.25** | **87.63** | 81.99 | ✅ **← canonical §0a 87.63** |

**All three circulating values have exact, identified provenance:**

| Value | Configuration | Status |
|---|---|---|
| **87.58** | v1 + current thresholds | ✅ **Register — reproduces exactly. AUTHORITATIVE baseline** |
| **88.23** | v1 + **both pre-amendment** thresholds | Superseded vintage — stale where quoted as the register value |
| **87.63** | v2 + current thresholds | Canonical §0a current reportable figure — correct in its own scope |

**Cause of the discrepancy: threshold vintage.** Not dataset vintage alone, not cell change, not tie-count semantics, not an implementation difference. The at-max/exclusive distinction was checked and is **not** the cause — both metrics were computed and the exclusive share (81.95%) matches neither circulating value.

**87.58 reproduces under the current canonical specification and is preserved as authoritative.**

---

## 2. P09 historical provenance

| | |
|---|---|
| **Registered actual** | **5,416** |
| **Register vintage** | v1 data + **`r_CAUTION = 7.5 mm/hr`** + **`o_UNSAFE = 1.9 m`** + incumbent `g_t` |
| **Current-threshold v1 baseline** | **5,220** (v1 + `r` 10.0/20.0 + `o` 1.0/1.25 + incumbent `g_t`) |
| **Status** | **Historical actual produced under a superseded threshold specification** |

**5,416 is not called wrong.** It is the value that was correctly recorded when P09 was resolved on 2026-09-06, under the specification then in force. The problem is **provenance and scope**, not fabrication or arithmetic error.

Both threshold changes were legitimate research versioning, and the language reflects that:

- **7.5 → 10.0 mm/hr** — the project determined 7.5 was **unsupported by any published source** and replaced it with the JPS/DID *Light* upper limit. This one was found erroneous.
- **1.9 → 1.25 m** — **superseded**, not erroneous: the evidence-backed Yaakob operational ceiling replaced the NORDFORSK failure point. A better reading of the same source.

---

## 3. P09 four-stage decomposition

> # **5,416 —(threshold)→ 5,220 —(data)→ 5,201 —(g_t)→ 3,661**

| Transition | Effect | Cause |
|---|---|---|
| 5,416 → 5,220 | **Δ_threshold = −196** | Threshold amendments (7.5→10.0 mm/hr, 1.9→1.25 m) |
| 5,220 → 5,201 | **Δ_data = −19** | v1 land cell → v2 sea cell |
| 5,201 → 3,661 | **Δ_g_t = −1,540** | SDR-001 incumbent → Model B |

**Arithmetic check:**

−196 + (−19) + (−1,540) = **−1,755**   and   3,661 − 5,416 = **−1,755** ✅

---

## 4. Corrected effects

| | Previously reported | **Corrected** |
|---|---|---|
| **Δ_data** | −215 | **−19** |
| **Δ_threshold** | *(not separated)* | **−196** |
| **Δ_g_t** | −1,540 | **−1,540** — unchanged, was correct |

**This supersedes the −215 data-effect interpretation, not the historical 5,416 value.** The earlier analysis was right that P09's shortfall predates any `g_t` change; it was wrong about the size and the cause. The data effect was overstated **elevenfold** because it absorbed the threshold amendments.

**Recorded as an annotation on the readiness audit** — its text is retained, and the note states that its conclusion still holds and is now sharper: there are three causes, not two.

---

## 5. P10 reconciliation

| | |
|---|---|
| **Register** | **230** |
| **C-5 Stage 1 (v1 + current thresholds)** | **230** ✅ **Reproduces exactly** |
| Stale value in findings | 227 — reproduces exactly under the **pre-amendment vintage** |

**The register value is reproducible under the current specification. 230 is the authoritative baseline.**

C-5 candidate stages preserved as **evidence only**: **230 → 207 → 222**, Δ_data = **−23**, Δ_g_t = **+15**. **P10 not re-resolved.**

---

## 6. P11 reconciliation

| | |
|---|---|
| **Register** | **37** |
| **C-5 Stage 1** | **37** ✅ **Reproduces exactly** |
| Stale value | **70** |

**70 has recoverable provenance.** It is **not** an unexplained figure: it reproduces **exactly** under v1 + `r` 7.5 + `o` 1.9 — the same pre-amendment vintage as P07's 88.23, P09's 5,416, P10's 227 and P12's 6.17.

**Therefore 70 is NOT classified as "stale documented value inconsistent with any reproducible baseline".** It is a **correctly computed value from a superseded specification**, and the record says so.

C-5 stages: **37 → 27 → 26**. **P11 not re-resolved.**

---

## 7. P12 reconciliation

| | |
|---|---|
| **Register** | **7.83** |
| **C-5 Stage 1** | **7.83** ✅ **Reproduces exactly** — this was the C-5 provenance gate |
| Stale value | **6.17** |

**6.17 has recoverable provenance**, established here by direct computation: under v1 + `r` 7.5 + `o` 1.9, non-scheduled transitions fall 227 → 213, giving **6.17%** exactly. Same vintage as every other stale value.

**7.83 is the authoritative historical/current-threshold v1 baseline.**

C-5 stages: **7.83 → 8.70 → 10.36**, Δ_data **+0.87**, Δ_g_t **+1.66**. **P12 not re-resolved.**

---

## 8. All stale-value locations found

| # | Location | Value(s) | Class | Action |
|---|---|---|---|---|
| 1 | **`CLAUDE.md`** F-6 mode-chattering block | 5,416 · 70 (14/yr) · 6.2% | **Active guidance** | ✅ **CORRECTED** to 5,220 · 37 (7.4/yr) · 7.83%, with a dated note explaining the vintage and flagging the P09 exception |
| 2 | **`finding-gt-evidence-closure.md`** Part 7 re-resolution table | 88.23 · 227 · 70 · 6.17 | **Operative — C-6 will consume this** | ✅ **CORRECTED** — each row now shows the register value with the vintage figure in parentheses, plus a header warning block |
| 3 | `finding-gt-sensitivity-analysis.md` §5 "Registered actual" column | 88.23 · 227 · 70 · 6.17 | Historical finding | ✅ **ANNOTATED**, text unchanged — the column is mislabelled, not miscalculated |
| 4 | `finding-sdr-001-readiness-audit.md` §6 P09 decomposition | Δ_data = −215 | Historical audit | ✅ **ANNOTATED**, text retained — four-stage decomposition added |
| 5 | `finding-sdr-001-readiness-audit.md` §5.2 baseline table | 88.23 · 227 · 70 · 6.17 | Historical audit | ⬜ Left — correctly identifies these as discrepancies; §6 annotation covers the diagnosis |
| 6 | `docs/canonical/session-log-2026-09-06.md` F-6 row | 70 · 6.2% | Historical record of that day | ⬜ **Deliberately untouched** — a dated log of what was found then |
| 7 | `docs/canonical/decision-record-empirical-first.md` line 118 | 70 · 6.2% | Historical record | ⬜ **Deliberately untouched** |
| 8 | `publications/active/journal-1/.../manuscript.md` lines 573, 628 | 5,416 · 70 · 6.2% | **Active manuscript** | ⬜ **Routed to C-8** — manuscript propagation is explicitly C-8's scope (instruction 17) |
| 9 | `report-c4-closure-2026-09-08.md`, `report-c5-closure-2026-09-08.md` | quote the pairs as open C-7 items | Sequential reports | ⬜ Untouched — accurate as of their dates |

---

## 9. Baseline-provenance matrix

Machine-readable: **`data/c7/baseline-provenance.csv`**, sha256 `d5db567c50a2927ab8b94f52753210b2b0aea702a16bfc359a19290396780b30`

| Prediction | Registered actual | Reproduced current baseline | Historical / config vintage | Stale conflicting value | Provenance status |
|---|---|---|---|---|---|
| **P07** | **87.58** | **87.58** ✅ v1 + current thresholds | Register = current-threshold vintage | **88.23** = v1 + `r` 7.5 + `o` 1.9 | **Register reproduces.** Stale prose value is the pre-amendment vintage |
| **P09** | **5,416** | **5,220** ❌ *(register does not reproduce)* | **Register = v1 + `r` 7.5 + `o` 1.9 — PRE-AMENDMENT** | 5,416 *is* the register value | **Historical actual from a superseded threshold specification — retained.** Comparable current baseline **5,220** |
| **P10** | **230** | **230** ✅ v1 + current thresholds | Register = current-threshold vintage | **227** = v1 + `r` 7.5 + `o` 1.9 | **Register reproduces.** Stale prose value is the pre-amendment vintage |
| **P11** | **37** | **37** ✅ v1 + current thresholds | Register = current-threshold vintage | **70** = v1 + `r` 7.5 + `o` 1.9 | **Register reproduces.** Stale prose value is the pre-amendment vintage |
| **P12** | **7.83** | **7.83** ✅ v1 + current thresholds | Register = current-threshold vintage | **6.17** = v1 + `r` 7.5 + `o` 1.9 | **Register reproduces.** Stale prose value is the pre-amendment vintage |

**Threshold vintage is stated explicitly for P09, and exact Stage-1 reproduction is confirmed for P07, P10, P11 and P12.**

---

## 10. Classification of each change

### A. Historical value retained

| | |
|---|---|
| **P09 = 5,416** | Valid under the specification in force at resolution. **Retained in the register unchanged.** Status: *historical actual produced under a superseded threshold specification.* |

### B. Active stale prose corrected

| | |
|---|---|
| **`CLAUDE.md`** F-6 block | 5,416 / 70 / 6.2% → **5,220 / 37 / 7.83%**, with vintage explanation |
| **`finding-gt-evidence-closure.md`** Part 7 | Register values now shown, vintage figures parenthesised, warning block added |

### C. Analytical decomposition corrected

| | |
|---|---|
| **P09 Δ_data** | **−215 → −19**, with **−196** separately attributed to threshold amendments. Historical 5,416 retained; only the *interpretation of the delta* changes |

**The three categories are not collapsed.** P09 appears in A and C but not B: its value stands, its interpretation was corrected.

---

## 11. Prediction-register mutation decision

> ## **DECISION: the register was NOT mutated.**

The instruction permits mutation only if necessary, and prefers reconciliation "entirely through notes/adjacent artefact". **An adjacent artefact is fully sufficient**, so the stronger guarantee was taken:

- `data/c7/baseline-provenance.csv` carries every field C-6 needs — registered actual, register vintage, current-threshold baseline, all three candidate vintages, the stale value and its vintage, reproduction status, and the **`c6_comparable_baseline`** column.
- The register therefore keeps its byte-for-byte integrity anchor intact across the entire C-1…C-7 sequence.

**All twelve mutation conditions are trivially satisfied because nothing was written:** prediction text unchanged · expected band unchanged · historical actual not erased · historical status not rewritten · previous values retained · reason documented · guard never invoked · hashes identical.

**No CONFIRMED/REFUTED status was changed.** That is C-6.

---

## 12. Register before / after hash

| | |
|---|---|
| **BEFORE** | `538808b6d82249faa66caf20fece38e994144fbbe2280b62d3193817a3cdc484` |
| **AFTER** | `538808b6d82249faa66caf20fece38e994144fbbe2280b62d3193817a3cdc484` |
| | ✅ **BYTE-FOR-BYTE IDENTICAL** — matches the integrity anchor |

24 entries · **22 CONFIRMED / 2 REFUTED**. Values intact: P07 `87.58` · P09 `5416.0` · P10 `230.0` · P11 `37.0` · P12 `7.83` · P13 `non-sched=230, osc=37`.

---

## 13. Exact register changes

> ### **NONE.** No field, row, value, status, note or byte was altered.

---

## 14. Baseline authority rule for C-6

> ### **Rule.** For re-resolution caused by a canonical model change, the comparison uses **the prediction's original text and original expected band**, with the **new actual computed under the new canonical specification**. Historical actuals remain for provenance and are never overwritten.

**Every re-resolution record must contain all eight fields:**

1. Original prediction text (verbatim)
2. Original expected band (verbatim)
3. Previous canonical specification
4. Previous recorded actual
5. **Intermediate current-baseline value where the register's actual is of a different vintage**
6. New canonical specification
7. New actual
8. Reason for re-resolution

### 14.1 Comparable baselines C-6 must use

| Prediction | Register actual | **Baseline C-6 compares from** | Note |
|---|---|---|---|
| P07 | 87.58 | **87.58** | Register reproduces |
| **P09** | 5,416 | **5,220** | ⚠️ **Field 5 is mandatory** — register actual is a different vintage |
| P10 | 230 | **230** | Register reproduces |
| P11 | 37 | **37** | Register reproduces |
| P12 | 7.83 | **7.83** | Register reproduces |

### 14.2 Mandatory constraint on P09

> **C-6 must NOT label 5,416 → 3,661 as a `g_t` effect.**
>
> The causal decomposition is:
>
> **5,416 —(threshold −196)→ 5,220 —(data −19)→ 5,201 —(g_t −1,540)→ 3,661**
>
> Recording it as a single −1,755 `g_t` effect would overstate SDR-001's impact by **14×**.

---

## 15. Files modified — 5

| File | Change | Class |
|---|---|---|
| `data/c7/baseline-provenance.csv` | **Created** — machine-readable provenance matrix | New artefact |
| `CLAUDE.md` | F-6 figures corrected + vintage note + P09 exception flagged | **B** — active guidance |
| `docs/canonical/finding-gt-evidence-closure.md` | Part 7 baselines corrected + warning block; C-7 row marked CLOSED | **B** — operative |
| `docs/canonical/finding-gt-sensitivity-analysis.md` | Dated annotation on §5; text unchanged | Annotation |
| `docs/canonical/finding-sdr-001-readiness-audit.md` | Dated annotation on the −215 decomposition; text retained | **C** — annotation |

Plus this report. **No script, dataset, canonical figure or register entry modified.** A stray `__pycache__` from the read-only imports was removed.

---

## 16. Historical artefacts left untouched

| Document | Why |
|---|---|
| `session-log-2026-09-06.md` F-6 row (70, 6.2%) | A dated log of what was found that day. Rewriting it would erase the sequence |
| `decision-record-empirical-first.md` line 118 | Same |
| `finding-gt-provenance-audit.md`, `finding-gt-operational-semantics.md`, `finding-unsafe-semantics-audit.md` | Read-only inputs; no baseline claims requiring correction |
| `cleanup-report-*`, `approval-report-*`, `report-c1-c2-c3-*`, `report-c2-closure-*`, `report-c4-closure-*`, `report-c5-closure-*` | Sequential records, accurate as of their dates |
| `finding-gt-sensitivity-analysis.md` §5 table body | **Annotated, not rewritten** — its numbers are correct for the vintage it computed |
| `finding-sdr-001-readiness-audit.md` §5.2, §6 body | **Annotated, not rewritten** |
| **`data/prediction-register.csv`** | **Not mutated at all** |

**The sequence remains visible:** provenance audit → semantics audit → readiness audit → C-0 → approval → C-1/C-2/C-3 → C-4 → C-5 → **C-7**.

---

## 17–20. Condition status

| | Condition | Status |
|---|---|---|
| **C-1** | Pin solar implementation | ✅ **CLOSED** — unaffected |
| **C-2** | 28-row USNO validation artefact | ✅ **CLOSED** — unaffected |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — unaffected, unchanged (`057c46a1…`) |
| **C-4** | Model B design consequences | ✅ **CLOSED** — unaffected |
| **C-5** | Three-stage hysteretic isolation | ✅ **CLOSED** — its frozen artefacts used as authority, unchanged (`3566cd6b…`, `23de3c07…`, `1f04720c…`); **no re-run required, no contradiction found** |
| **C-7** | Prediction baseline reconciliation | ✅ **CLOSED** |
| **C-6** | Re-resolve affected predictions | 🔴 **OPEN — not executed.** No outcome determined, no register entry changed |
| **C-8** | Execute the propagation list | 🔴 **OPEN — not executed.** Journal 1 manuscript stale figures routed here |

### C-7 closure test — all fifteen criteria

| # | Criterion | Met |
|---|---|---|
| 1 | P09's 5,416 provenance explicitly identified | ✅ v1 + `r` 7.5 + `o` 1.9 |
| 2 | P09 5,220 current-threshold baseline preserved | ✅ §2, matrix, artefact |
| 3 | Threshold effect −196 separated | ✅ §3 |
| 4 | Data effect corrected to −19 | ✅ §4 |
| 5 | `g_t` effect −1,540 separately recorded | ✅ §3–§4 |
| 6 | P10 = 230 baseline verified | ✅ §5 |
| 7 | P11 = 37 verified, stale 70 reconciled | ✅ §6 — 70 has recoverable provenance |
| 8 | P12 = 7.83 verified, stale 6.17 reconciled | ✅ §7 — 6.17 provenance computed |
| 9 | P07 87.58 vs 88.23 reconciled | ✅ §1 |
| 10 | Baseline-provenance matrix created | ✅ §9 + CSV artefact |
| 11 | Historical values not silently overwritten | ✅ §16 |
| 12 | Active stale guidance corrected or annotated | ✅ §8 |
| 13 | Register provenance sufficient for C-6 | ✅ §14 |
| 14 | No prediction outcome re-resolved | ✅ §13 |
| 15 | Canonical `g_t` unchanged | ✅ §21 |

---

## 21. Canonical `g_t` integrity

> **`g_t^canonical` = `g_t^incumbent`** — SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE otherwise

All three rows verbatim in Appendix C. **Unchanged by hash:** `hysteresis_analysis.py` `73015d88…` · `diagnostic_binding.py` `69bc2bd6…` · `canonical_figures.py` `5af9eaf7…` · `solar.py` `3b7dc371…`. Neither register-writing script was executed.

**Also unchanged:** wind 21.6/27.0 · rainfall 10.0/20.0 · wave 1.0/1.25 · `cause` · `G(S)` · `A_AI(S)` · C-3 and C-5 artefacts.

---

## 22. Canonical figures integrity

| | |
|---|---|
| **PRIMARY 7.72%** | ✅ **UNCHANGED** — 8 occurrences in §0a |
| **RESOLUTION 5.98%** | ✅ **UNCHANGED** — 5 occurrences |

`empirical-findings-2026-09-06.md` §0a not touched. **Model B remains approved but not canonical.**

---

## 23. Assessment

**The reconciliation turned out to be one finding, not four.** Every discrepancy — P07's 88.23, P09's 5,416, P10's 227, P11's 70, P12's 6.17 — reproduces exactly under a single superseded configuration. That matters for how the project should describe its own history: the findings were not sloppy, they were **a consistent snapshot taken before two threshold amendments**, and the register is a consistent snapshot taken after. The right word is *vintage*, not *error*.

**The genuine anomaly is narrower than reported and sits in the register**, not the findings: P09 alone carries a pre-amendment value, hand-restored, while its four neighbours carry post-amendment ones. Its `notes` field records the restoration, so the inconsistency was documented rather than hidden — but it was never labelled as a *vintage* mismatch, which is why the readiness audit read it as a −215 data effect.

**Correcting that decomposition is the substantive output.** −215 → −19, with −196 reassigned to threshold vintage. An elevenfold error in an attributed effect, caught before C-6 could carry it into a re-resolution record.

**The register was left alone deliberately.** It could have been annotated, and the notes field is the natural place — but an adjacent artefact serves C-6 equally well while preserving a byte-identical integrity anchor across seven consecutive execution conditions. When the choice is between a convenient write and a provable non-write, the non-write is worth more here.

---

# **C-7 CLOSED — PREDICTION BASELINES RECONCILED**

**C-1 · C-2 · C-3 · C-4 · C-5 · C-7 CLOSED — C-6 and C-8 REMAIN OPEN.**
**SDR-001 remains APPROVED — NOT YET APPLIED. Canonical migration has not begun.**
