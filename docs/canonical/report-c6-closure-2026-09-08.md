# Report: SDR-001 Execution Condition C-6 — Prediction Re-Resolution

**Date:** 2026-09-08
**SDR-001:** **APPROVED — NOT YET APPLIED** · **Model B: SELECTED — NOT YET CANONICAL** · canonical `g_t` unchanged
**Scope:** C-6 only. **C-8 not executed.** No propagation to Appendix C, canonical scripts, figures or manuscripts.

---

# RESULT

# **C-6 CLOSED — AFFECTED PREDICTIONS RE-RESOLVED**

All fourteen closure criteria satisfied.

> ### The headline is an attribution result, not a count.
>
> **7 candidate status flips — but only 3 are attributable to SDR-001.**
>
> **P20, P23, P24** flip because of the `g_t` design change. **P04, P09, P18, P19** were **already REFUTED under the incumbent classifier at the current canonical configuration** — their bands were exited by the threshold and data changes that predate this decision. Reporting all seven as SDR-001's doing would misattribute four of them.

---

## 1. Complete affected prediction list

**All 24 register entries assessed.**

| Class | Count | Predictions |
|---|---|---|
| **Affected — re-resolved** | **20** | P03–P14, P17–P24 |
| **Unaffected** | **4** | P01, P02, P15, P16 |

Of the 20 affected: **18 required computation**, **1 is scope-only** (P03), **1 is structurally invariant** (P21).

*The readiness audit's estimate of "16 computable" was low. Verified from the operative register: **18** predictions required a computed candidate actual — the estimate omitted P03 and P14.*

**Unaffected, with reason:** P01 and P16 (`g_w` activations), P02 (superseded vessel-blind `g_o`), P15 (max sustained wind). None reads `g_t`.

---

## 2. Source of each candidate actual

| Source | Predictions | Authority |
|---|---|---|
| **Frozen C-5 artefact** — not recomputed | P09, P10, P11, P12, P13 | `data/c5/c5-three-stage-metrics.csv` sha256 `3566cd6b…` |
| **Structural argument** — no rerun needed | P21 | `condition_comparison.py` — C1 and C3 are the identical map |
| **Computed read-only under the candidate** | P03–P08, P14, P17–P20, P22–P24 | `data/c6/c6-candidate-actuals.json`, consuming frozen C-3 solar `057c46a1…` |
| **Not re-resolved** | P01, P02, P15, P16 | Metric does not read `g_t` |

**Self-check that validates the whole computation:** the harness was run twice, once with the incumbent `g_t` and once with Model B. **The incumbent column reproduces §0a exactly** — Level 2 PRIMARY **7.7176 ≈ 7.72%**, RESOLUTION **5.9815 ≈ 5.98%**, `g_t` share **87.6275 ≈ 87.63%**, `g_o` daylight CAUTION **98.6577 ≈ 98.66%**, daylight UNSAFE **409**, C1↔C3 **0.00%**. Since the incumbent column reproduces canonical figures, the Model B column differs from it **only** by `g_t`.

**No register-writing script was executed.** `canonical_figures.py`, `condition_comparison.py`, `diagnostic_binding.py` and `hysteresis_analysis.py` all call `reg.to_csv()` unconditionally; their component logic was reproduced from the canonical constants instead.

**Configuration rule:** each prediction was evaluated in the configuration its own registered scope names — MFWAM for P17–P24, PRIMARY otherwise. Changing a prediction's configuration would rewrite the prediction.

---

## 3. P09 provenance chain

> ### **5,416 —(threshold −196)→ 5,220 —(data −19)→ 5,201 —(g_t −1,540)→ 3,661**

| Stage | Value | Cause |
|---|---|---|
| Registered actual | **5,416** | v1 + **pre-amendment** `r` 7.5 / `o` 1.9 |
| Comparable current-threshold v1 baseline *(field 5, mandatory)* | **5,220** | Threshold amendments −196 |
| v2/incumbent | **5,201** | Data/configuration −19 |
| v2/Model B candidate | **3,661** | `g_t` design change −1,540 |

**Check:** −196 − 19 − 1,540 = **−1,755** = 3,661 − 5,416 ✅

> **5,416 → 3,661 is NOT reported as the `g_t` effect.** Doing so would attribute −1,755 to SDR-001 when the true effect is −1,540 — a **14×** overstatement relative to the data effect it would absorb.

---

## 4. P09 outcome

| | |
|---|---|
| Original band | **5,400–8,000** (unchanged) |
| Previous actual / status | 5,416 · **CONFIRMED** |
| Candidate actual | **3,661** |
| **Candidate status** | **REFUTED** |
| Flip attributable to SDR-001? | ❌ **NO** — **already REFUTED at v2/incumbent (5,201)**, and even the v1 current-threshold baseline (5,220) is below the 5,400 floor |

**P09's band was exited by the threshold amendments alone.** Model B moves it further out; it did not cause the exit.

---

## 5–8. P10, P11, P12, P13 outcomes

| | Band | Previous | Baseline | Candidate | Previous status | **Candidate status** | Deltas |
|---|---|---|---|---|---|---|---|
| **P10** | <500 | 230 | 230 | **222** | CONFIRMED | ✅ **CONFIRMED** | Δ_data −23 · Δ_g_t **+15** |
| **P11** | <100 | 37 | 37 | **26** | CONFIRMED | ✅ **CONFIRMED** | Δ_data −10 · Δ_g_t **−1** |
| **P12** | 5–40% | 7.83 | 7.83 | **10.36** | CONFIRMED | ✅ **CONFIRMED** | Δ_data +0.87 · Δ_g_t **+1.66** · Δ_total +2.53 pp |
| **P13** | NO | non-sched 230, osc 37 | — | **non-sched 222, osc 26** | CONFIRMED | ✅ **CONFIRMED** | — |

**P13 applied verbatim, no new band invented:** its original criteria are non-scheduled ≤ 500 **and** oscillations ≤ 100. **222 ≤ 500 and 26 ≤ 100**, so mode-chattering remains **not demonstrated** → **NO** → CONFIRMED.

**Stale values used as provenance only:** P11's 70 and P12's 6.17 are the pre-amendment vintage (C-7), recorded in the artefact's notes and nowhere used as baselines.

---

## 9. P21 handling — structurally invariant

**Included, not omitted.**

`condition_comparison.py` defines both conditions identically:

```python
"C1": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
"C3": {SAFE: FULL, CAUTION: FULL, UNSAFE: EMPTY},
```

**C1 and C3 are the same admissible-set map, so their divergence is 0 for any classifier whatsoever.** Recomputed anyway as a check: **0.0000% under both the incumbent and the candidate.**

| | |
|---|---|
| Band | 0 · Previous 0.0 · Candidate **0.0000** |
| **Candidate status** | ✅ **CONFIRMED** |
| Attribution | **structurally invariant — no empirical rerun needed** |

**Role preserved.** P21 carries **F-15**, the result answering Review 3's novelty objection: a Flehmig-style traffic-light baseline collapses to a plain binary gate because its intermediate level does not touch advisory scope. **That claim cannot be disturbed by this decision**, which is a material de-risking of the migration.

---

## 10. All remaining affected predictions

| | Band | Previous | Baseline (v2/incumbent) | Candidate | Prev | **Candidate** | Attribution |
|---|---|---|---|---|---|---|---|
| **P03** | 0.0% | 0.0 | 0.0 | **0.0000** | CONF | ✅ **CONFIRMED** | Scope wording only; invariant |
| **P04** | 12.0–12.8% | 12.4 | **7.7176** | **5.8128** | CONF | ❌ **REFUTED** | threshold + data + `g_t`; **already refuted at incumbent** |
| **P05** | >90% | 97.95 | 98.6577 | **98.5252** | CONF | ✅ **CONFIRMED** | data + `g_t` (−0.13 pp) |
| **P06** | <5% | 1.76 | 1.2230 | **0.8263** | CONF | ✅ **CONFIRMED** | data + `g_t` (−0.40 pp) |
| **P07** | >70% | 87.58 | 87.6275 | **86.8236** | CONF | ✅ **CONFIRMED** | data + `g_t` (−0.80 pp) |
| **P08** | ≤4 | 3.0 | 3 | **3** | CONF | ✅ **CONFIRMED** | `g_t` still binds pre-sunrise in 05–09 |
| **P14** | YES | g_o 97.5%, g_t 88.2% | g_o 98.66%, g_t 87.63% | **g_o 98.53%, g_t 86.82%; g_w & g_m never bind** | CONF | ✅ **CONFIRMED** | Holds **more strongly** — `g_t` becomes purely a curfew |
| **P17** | MFWAM LOWER | 8.01 | MFWAM 11.56 vs ERA5 12.53 | **MFWAM 3.89 vs ERA5 5.05** | CONF | ✅ **CONFIRMED** | Both rates fall; ordering preserved |
| **P18** | 8–12% | 8.32 | **5.9815** | **4.4819** | CONF | ❌ **REFUTED** | threshold + data + `g_t`; **already refuted at incumbent** |
| **P19** | 6.0–6.2% | 6.1 | **5.9815** | **4.4819** | CONF | ❌ **REFUTED** | data + `g_t`; **already refuted at incumbent** |
| **P20** | 400–420 h | 409 | 409 | **1,529** | CONF | ❌ **REFUTED** | **`g_t` — attributable to SDR-001** |
| **P22** | 6.0–6.2% | 5.98 | 5.9815 | **4.4819** | **REF** | ❌ **REFUTED** | `g_t`; **status unchanged**, margin widened |
| **P23** | 20–30% | 28.19 | 28.1887 | **45.5602** | CONF | ❌ **REFUTED** | **`g_t` — attributable to SDR-001** |
| **P24** | 14–24% | 22.21 | 22.2072 | **41.0783** | CONF | ❌ **REFUTED** | **`g_t` — attributable to SDR-001** |

**P20 requires a note.** "Daylight" was held at the **registered scope 06:00–17:00**, preserving the original prediction. Under Model B the 06:00 hour is UNSAFE (sunrise 06:01–06:34), so UNSAFE now intrudes into the registered window and the count rises 409 → 1,529. **The term is redefined, not merely recomputed** — the C-8 propagation item.

**P23 and P24 rise** because Model B enlarges UNSAFE, widening the divergence between the ungated condition C0 and the gated ones.

---

## 11. Status-change summary

| Prediction | Previous actual | Candidate actual | Previous status | Candidate status | Change? | Attributable to SDR-001? |
|---|---|---|---|---|---|---|
| **P04** | 12.4 | **5.8128** | CONFIRMED | **REFUTED** | **YES** | ❌ **No** — already refuted at incumbent |
| **P09** | 5,416.0 | **3,661** | CONFIRMED | **REFUTED** | **YES** | ❌ **No** — already refuted at incumbent |
| **P18** | 8.32 | **4.4819** | CONFIRMED | **REFUTED** | **YES** | ❌ **No** — already refuted at incumbent |
| **P19** | 6.1 | **4.4819** | CONFIRMED | **REFUTED** | **YES** | ❌ **No** — already refuted at incumbent |
| **P20** | 409.0 | **1,529** | CONFIRMED | **REFUTED** | **YES** | ✅ **Yes** |
| **P23** | 28.19 | **45.5602** | CONFIRMED | **REFUTED** | **YES** | ✅ **Yes** |
| **P24** | 22.21 | **41.0783** | CONFIRMED | **REFUTED** | **YES** | ✅ **Yes** |

**Unchanged outcomes are not hidden.** 17 predictions retain their status: P01, P02 (unaffected), P03, P05, P06, P07, P08, P10, P11, P12, P13, P14, P15, P16, P17, P21, and **P22 — which was REFUTED and remains REFUTED**, though at a wider margin and for a different reason.

**7 flips, all CONFIRMED → REFUTED. No REFUTED → CONFIRMED.**

---

## 12. Previous vs candidate outcome totals

**The two counts are reported separately and must not be mixed.**

| | CONFIRMED | REFUTED |
|---|---|---|
| **Canonical (current, authoritative)** | **22** | **2** |
| **Migration candidate (conditional on C-8)** | **15** | **9** |

> **The canonical count remains 22 / 2.** Model B is not canonical, so the canonical outcome of every prediction is still the incumbent one. **The 15 / 9 count is hypothetical and applies only if migration completes.**

---

## 13. Machine-readable artefact

| | |
|---|---|
| **Path** | `data/c6/prediction-reresolution.csv` |
| **sha256** | `46474a320e11502c0b62d383d13d8df1db7a14c9132702db8b5fcd294d604a64` |
| **Rows** | **24** — one per prediction, including the 4 unaffected |
| **Columns** | 25 |

**All twelve mandatory fields present**, plus four attribution columns added because the analysis required them:

`original_prediction_text` · `original_scope` · `original_expected_band` · `band_lo` / `band_hi` · `previous_specification` · `previous_actual` · `previous_status` · `comparable_baseline` · `candidate_specification` · `candidate_actual` · `candidate_status` · `status_changed` · **`incumbent_at_current_config`** · **`status_under_incumbent_at_current_config`** · **`already_refuted_before_model_b`** · **`flip_attributable_to_sdr_001`** · `delta_components` · `change_attribution` · `evidence_source` · `reason_for_reresolution` · `reresolution_date` · `condition` · `applies_only_if_migration_completes` · `notes`

Supporting: `data/c6/c6-candidate-actuals.json` (`962748b0…`) — incumbent and candidate values side by side for every metric.

---

## 14. Register mutation decision

> ## **Additive annotation only. No `actual`, no `status`, no band, no text changed.**

**Reasoning.** The schema carries one active `status` and one active `actual`. Model B is **not canonical**, so writing candidate statuses would either destroy the canonical verdict or publish a 15/9 count for an architecture that does not exist. Instruction 17 forbids mixing the two counts; with a single-status schema, the only way to honour that is to leave the status fields alone.

**A pointer was appended to `notes`** for each of the 20 re-resolved predictions, naming the candidate actual, the candidate status, whether it is a flip, whether the flip is attributable to SDR-001, and the evidence artefact. Every note is prefixed **`[C-6 2026-09-08 — CANDIDATE ONLY, NOT APPLIED]`**.

**A programmatic guard enforced this.** `annotate_register.py` re-reads every row after editing and aborts without writing if any of thirteen protected fields differs: `id`, `registered`, `analysis`, `scope`, `metric`, `pred_type`, `pred_lo`, `pred_hi`, `pred_stated`, `rationale`, **`actual`**, **`status`**, `resolved`. **The guard passed.**

**A pre-mutation backup was taken:** `data/c6/prediction-register.pre-c6.csv`, sha256 `538808b6d82249fa…` — byte-identical to the register as it stood at the end of C-7.

---

## 15. Exact register changes

| Field | Rows touched | Change |
|---|---|---|
| **`notes`** | **20** (P03–P14, P17–P24) | Candidate pointer **appended**; any pre-existing note text preserved ahead of it |
| Every other field | **0** | Unchanged, guard-verified |

**Verified after mutation:** 24 entries · **22 CONFIRMED / 2 REFUTED** · P04 `12.4` · P09 `5416.0` · P12 `7.83` · P20 `409.0` · P22 `5.98` — all original actuals intact.

**P09's existing note was preserved.** Its prior RESTORED provenance text still leads the field, with the C-6 pointer appended after it.

---

## 16. Register before / after hash

| | |
|---|---|
| **BEFORE** | `538808b6d82249faa66caf20fece38e994144fbbe2280b62d3193817a3cdc484` |
| **AFTER** | `d95cf81f19341c3c14f136070473bbf56ffa1928458d164fbd4bbf85bed218ce` |
| **Backup of BEFORE** | `data/c6/prediction-register.pre-c6.csv` — `538808b6…` ✅ |

**The hash changed, deliberately and auditably.** This is the first mutation since the anchor was established, it is confined to `notes`, and the pre-state is preserved byte-identically alongside it.

---

## 17. Files modified

| File | Change |
|---|---|
| `scripts/c6/reresolve_predictions.py` | **Created** — candidate computation, read-only |
| `scripts/c6/build_reresolution_artefact.py` | **Created** — mechanical outcome assignment |
| `scripts/c6/annotate_register.py` | **Created** — guarded additive annotation |
| `data/c6/c6-candidate-actuals.json` | **Created** |
| `data/c6/prediction-reresolution.csv` | **Created** |
| `data/c6/prediction-register.pre-c6.csv` | **Created** — pre-mutation backup |
| `data/prediction-register.csv` | **Modified** — `notes` only, 20 rows |
| `docs/canonical/finding-gt-evidence-closure.md` | C-6 row marked CLOSED |

Plus this report. **No canonical script, dataset, figure or manuscript touched.**

---

## 18. Historical records retained

**Nothing was overwritten anywhere.**

- **Every previous actual and status** survives in the register, untouched, and is duplicated into the artefact's `previous_actual` / `previous_status` columns.
- **P09's pre-amendment provenance note** preserved verbatim.
- **The C-7 stale-vintage values** (88.23, 227, 70, 6.17) are recorded as provenance in the artefact and used as baselines nowhere.
- **Prior audits and findings** untouched — no document was rewritten to make a prediction look as though it had been resolved under Model B.
- **Pre-mutation register** preserved as a byte-identical backup.

---

## 19–22. Condition status

| | Condition | Status |
|---|---|---|
| **C-1** | Pin solar implementation | ✅ **CLOSED** — unaffected |
| **C-2** | 28-row USNO validation artefact | ✅ **CLOSED** — unaffected |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — **consumed** by Model B here, unmodified (`057c46a1…`) |
| **C-4** | Model B design consequences | ✅ **CLOSED** — unaffected |
| **C-5** | Three-stage hysteretic isolation | ✅ **CLOSED** — **frozen values consumed** for P09–P13, no rerun, no contradiction (`3566cd6b…`) |
| **C-7** | Baseline reconciliation | ✅ **CLOSED** — its authority rule applied throughout; artefact unchanged (`d5db567c…`) |
| **C-6** | Re-resolve affected predictions | ✅ **CLOSED** |
| **C-8** | Execute the propagation list | 🔴 **OPEN — not executed** |

### C-6 closure test — all fourteen criteria

| # | Criterion | Met |
|---|---|---|
| 1 | Complete affected set identified | ✅ 20 affected / 4 unaffected, from the operative register |
| 2 | Original text and bands preserved | ✅ Copied verbatim; guard-verified unchanged |
| 3 | Candidate actuals computed or sourced reproducibly | ✅ Frozen C-5 + C-3 + read-only computation |
| 4 | P09 four-stage provenance preserved | ✅ §3 |
| 5 | No threshold/data change misattributed to `g_t` | ✅ §11 — 4 of 7 flips explicitly **not** attributed |
| 6 | P10–P13 re-resolved | ✅ §5–§8 |
| 7 | P21 structural invariance handled explicitly | ✅ §9 |
| 8 | Outcomes determined mechanically | ✅ In-band → CONFIRMED, else REFUTED. No softening categories |
| 9 | Previous actual/status retained | ✅ §18 |
| 10 | Machine-readable artefact created | ✅ §13 |
| 11 | Register mutation controlled and auditable | ✅ §14 — guarded, backed up |
| 12 | Before/after hashes recorded | ✅ §16 |
| 13 | No manuscript/canonical propagation | ✅ §17 |
| 14 | C-8 remains OPEN | ✅ |

---

## 23. Canonical `g_t` integrity

> **`g_t^canonical` = `g_t^incumbent`** — SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE otherwise

All three rows verbatim in Appendix C. **Canonical scripts unchanged by hash:** `canonical_figures.py` `5af9eaf7…` · `condition_comparison.py` `1f0f4e9c…` · `hysteresis_analysis.py` `73015d88…` · `diagnostic_binding.py` `69bc2bd6…` · `solar.py` `3b7dc371…`.

Also unchanged: wind 21.6/27.0 · rainfall 10.0/20.0 · wave 1.0/1.25 · `cause` · `G(S)` · `A_AI(S)`.

---

## 24. Headline figure integrity

| | |
|---|---|
| **PRIMARY 7.72%** | ✅ **UNCHANGED** — 8 occurrences in §0a |
| **RESOLUTION 5.98%** | ✅ **UNCHANGED** — 5 occurrences |
| **5.81% / 4.48% in canonical findings** | ✅ **ZERO occurrences** — not introduced |

`empirical-findings-2026-09-06.md` untouched. **Model B remains approved but not canonical.**

---

## 25. Assessment

**The count that matters is 3, not 7.**

Seven predictions flip, and a careless report would hand a reviewer "SDR-001 refutes seven of your predictions". Four of those — **P04, P09, P18, P19** — had already left their bands under the *incumbent* classifier at the current canonical configuration. Their bands were exited by the threshold amendments and the land-to-sea cell correction, both of which predate this decision and were adopted for their own reasons.

**Making that separable required computing the incumbent column at all.** It would have been simpler to compute only Model B and difference against the register, and the answer would have been wrong in the same way C-7 found the −215 figure wrong: by attributing to `g_t` what belonged to earlier changes.

**What SDR-001 genuinely costs is three refutations** — P20, P23, P24 — and all three are the same phenomenon: Model B enlarges UNSAFE, so the daylight-UNSAFE count rises and the C0-versus-gated divergences widen. That is the sensitivity analysis's `2 → 1,536` step showing up in the prediction record, which is what C-4 disclosed and accepted.

**What survives is worth noting.** **P12 strengthens** (7.83 → 10.36, still in band): hysteresis becomes more effective when the time-driven CAUTION band is removed. **P14 holds more strongly** — with no time-driven CAUTION, `g_t` is purely a curfew, which is exactly what the prediction claimed. And **P21 cannot move at all**, so the F-15 novelty result answering Review 3 is untouched by the migration.

**The register was annotated, not rewritten.** A single-status schema cannot carry two architectures at once, and the honest resolution is that the canonical count stays 22 / 2 until an architecture exists to justify changing it.

---

# **C-6 CLOSED — AFFECTED PREDICTIONS RE-RESOLVED**

**C-1 · C-2 · C-3 · C-4 · C-5 · C-6 · C-7 CLOSED — C-8 REMAINS OPEN.**
**SDR-001 remains APPROVED — NOT YET APPLIED. Canonical migration has not begun.**
