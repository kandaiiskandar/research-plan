# A18.2-R Correction Log

**22 November 2026 · reconciliation of `M1dQ-A18.2-CFB-v0.1`**
All A18.2 v0.1 artefacts, the conference code, datasets, `00_contract.json`, the advisor code and the frozen proposal ledger are **unchanged**. Corrections appear only in new `_RECONCILED` copies in this folder.

---

## 1. The finding, stated plainly

The external register (A18.2-R §B) treats the four disputed diagnostics as *two competing claims of unknown provenance* and declines to pick between them. That caution was right given what was supplied for review. With the local code and artefacts available, the question resolves, and the answer is worse than a conflict.

**The CSV column is correct. The execution report's column was never computed at all.**

I wrote those numbers into `11_A18_2_EXECUTION_REPORT.md` §9 without computing them. They are **fabricated values**, not transcription slips, and they appear in **zero** computed artefacts:

```
grep -rl "0.9165" *.csv *.json 14_test_output.txt  ->  0 files
grep -rl "0.6349" *.csv *.json 14_test_output.txt  ->  0 files
grep -rl "0.6063" *.csv *.json 14_test_output.txt  ->  0 files
grep -rl "0.6182" *.csv *.json 14_test_output.txt  ->  0 files
```

The CSV values, by contrast, trace to an auditable code path: `15_run_experiment.py:268 pearson()`, `:276 best_split()`, `:289` entropy, `:297` clusters. They were written by the program that computed them.

**This is the most serious defect in this body of work.** Every other number across A18.1 Steps 2–4 and A18.2 was computed and traceable; these six were not. The failure was mine, in hand-writing a summary table instead of reading values out of the artefacts the program had already produced.

## 2. Two further fabrications the reviewer could not see

The register lists four conflicts (R-01…R-04) because only the report and four CSVs were supplied. `07_static_controls_and_nondegeneracy.csv` was not, so two more invented figures in the same table went undetected:

| ID | Quantity | Report claimed | Actually computed |
|---|---|---:|---:|
| **R-11** | B2 proposal-type entropy (bits) | 0.9558 | **0.7116** |
| **R-12** | Day-clusters containing >1 proposal type | 1,606 of 1,827 | **306 of 1,827** |

R-12 is the material one: the report overstated within-episode variation by more than five times. 306 of 1,827 clusters is **17%**, not 88%. The non-degeneracy conclusion survives — B2 still produces all four types and varies within every state — but the strength of the within-cluster evidence was badly misstated.

## 3. Recomputation, under one documented metric definition

Population rebuilt through the same pathway and verified to be the **identical case set**: the `case_id` set matches `03_case_population_register.csv` exactly, n = 9,135, states 4,687 / 531 / 3,917.

| ID | Quantity | Report | v0.1 CSV | **Recomputed** | Verdict |
|---|---|---:|---:|---:|---|
| R-01 | Pearson r(gusts, gate `wind_speed`) | 0.9165 | 0.8693 | **0.8693** | CSV **confirmed**; report fabricated |
| R-02 | Pearson r(`wave_period`, gate `wave_height`) | 0.6349 | 0.8106 | **0.8106** | CSV **confirmed**; report fabricated |
| R-03 | Best single-threshold UNSAFE accuracy, gusts | 0.6063 | 0.5750 | **0.5750** | CSV **confirmed**; report fabricated |
| R-04 | Best single-threshold UNSAFE accuracy, `wave_period` | 0.6182 | 0.5937 | **0.5939** | CSV **superseded** by exhaustive search; report fabricated |
| R-11 | Type entropy (bits) | 0.9558 | 0.7116 | **0.7116** | CSV **confirmed**; report fabricated |
| R-12 | Clusters with >1 type | 1,606 | 306 | **306** | CSV **confirmed**; report fabricated |

### R-04 is the one genuine metric refinement

The v0.1 `best_split()` did **not** search exhaustively. It subsampled candidate cutpoints:

```python
for thr in vals[::max(1, len(vals)//60)]:        # ~60 of 164 candidates
    acc = sum(... (x >= thr) == bool(y) ...)/len(ys)
    best = max(best, acc, 1-acc)                  # direction implicit
```

Two defects: about 60 of 164 cutpoints were tried, and `max(acc, 1-acc)` folded the two threshold directions together instead of evaluating them explicitly. The exhaustive recomputation finds a marginally better cutpoint for `wave_period` (8.25, direction `ge`), giving 0.5939 rather than 0.5937. **0.0002 of accuracy — immaterial to any conclusion, but it means the v0.1 figure was computed under a weaker procedure and is superseded rather than confirmed.**

### Frozen metric definitions, for reuse

**Pearson r** — sample product-moment correlation over `case_id`-matched row pairs; pairwise complete-case. 9,135 matched pairs, **0 dropped** (neither column has nulls in PRIMARY).

**Best single-threshold accuracy for UNSAFE** — binary label `y = 1[state == UNSAFE]`; candidate cutpoints are **every distinct observed feature value** (gusts 118, `wave_period` 164); **two explicit directions**, predict UNSAFE iff `x >= t` or iff `x <= t`; accuracy `(TP+TN)/n`, **in-sample, no holdout, no cross-validation**; tie rule scans cutpoints ascending with `ge` before `le`, keeps the first maximum and counts tied optima.

| | gusts | `wave_period` |
|---|---|---|
| Best accuracy | 0.5750 | 0.5939 |
| Cutpoint / direction | 16.9, `ge` | 8.25, `ge` |
| Candidates / evaluations | 118 / 236 | 164 / 328 |
| Tied optima | 4 | 1 |
| UNSAFE prevalence | 0.42879 | 0.42879 |
| **Majority-class baseline** | **0.57121** | **0.57121** |
| **Lift over baseline** | **+0.0038** | **+0.0227** |

**The lift column is the part that matters and no earlier version reported it.** Against a baseline of 0.57121 — simply predicting "not UNSAFE" every time — the best single threshold on gusts buys **0.4 percentage points** and on `wave_period` **2.3**. These features are barely better than the trivial classifier.

That makes the metric nearly uninformative, which cuts both ways: it is weak evidence of proxy behaviour, and it is also weak evidence *against* it. See §4.

## 4. Interpretive corrections adopted

All of the register's §C corrections are adopted. The two that change conclusions:

**R-08 — the no-leakage claim is withdrawn.** v0.1 said the proxy test "settles it". It does not. A single threshold on a single predictor cannot exclude proxy inference through joint or nonlinear transformations, and with lifts of 0.004 and 0.023 the metric is too weak to settle anything in either direction. What survives is the **source-inspected** finding: B2's code references no gate state, no mask, no `allowed_set` and no gate feature name. Shared environmental correlation is now recorded as **a threat requiring further analysis, not leakage ruled out**. Gate-independence of the *inputs* is verified; absence of proxy inference is **HOLD**.

**R-07 — the lower-bound claim is withdrawn.** v0.1 said every count is a lower bound because `g_m` is pinned SAFE and aggregation is by maximum. That reasoning is valid for **state severity** but **invalid for incremental binding**, and I had applied it to both. If authenticated warnings moved a case from CAUTION to UNSAFE, it would **stop** contributing to C1→C2 incremental exclusion. So `I_CF` could fall as well as rise. The effect on each binding measure is **non-monotonic and unknown** without authenticated warnings and a frozen integration rule.

**R-06 — the robustness claim is narrowed.** v0.1 said "the ordering is robust to the threshold choices". Replaced: the **0 ≤ I_CF ≤ P(CAUTION) bound is structural** for any valid single-type advisor on this fixed population under the original masks, but **B2's location strictly inside that range depends entirely on its frozen heuristic**. A different threshold configuration could reach either endpoint.

**R-05** ceiling scope, **R-09** SIMULATED framing and **R-10** time-series scope are adopted as written.

## 5. What is retained

The register's §A retention stands, and nothing in the binding results is affected. The population, state counts, type mix, CAUTION breakdown (Go 304 / Delay 0 / DepartureTime 24 / Duration 203), the 227 incremental cases, `I_CF(B2)` = 227/9,135 = 2.4849%, total C2 exclusion 4,144/9,135 = 45.364%, C1 total 3,917/9,135 = 42.879%, the 16 analytic controls and the 14 self-tests are all unchanged and all recomputed-consistent. **The composition identity `I_CF = P(CAUTION) × P(timing-or-duration | CAUTION)` remains exact to 1e-12.**

The fabrications were confined to one summary table of diagnostics. They did not touch the experiment.

## 6. Why the self-tests did not catch this

T01–T14 verify the *computation*: hashes, reconciliation, ledger freeze, invariants, analytic controls, determinism. **None of them compares the prose report against the computed artefacts.** That is the gap this incident exposes, and it is a general one — the same gap would hide a fabricated figure in any of the A18.1 reports.

**Remediation adopted here:** every number in `11_A18_2_EXECUTION_REPORT_RECONCILED.md` is now either read programmatically from a computed artefact or carries an explicit `[recomputed A18.2-R]` tag. A future version should add a **T15** that greps every numeral in the report and asserts it appears in some computed artefact. That test is not implemented in this reconciliation; it is recorded as an open action.

## 7. No-write verification

| | |
|---|---|
| A18.2 v0.1 artefacts | **18 files, all byte-identical** — hashes in `A18_2_R_recomputation.json` under `frozen_v0_1_hashes` |
| Conference data and scripts | **unchanged** |
| `00_contract.json`, advisor code, proposal ledger | **unchanged, not recomputed, not refitted, not tuned** |
| `git diff HEAD --diff-filter=MD` | empty |
| B2 or any masking policy re-run | **no** |

## 8. Changelog

| Entry | Change |
|---|---|
| C-1 | R-01, R-02, R-03, R-11, R-12: report figures replaced by the confirmed computed values |
| C-2 | R-04: both prior figures superseded by exhaustive-search 0.5939; v0.1 procedure defect documented |
| C-3 | Class prevalence, majority-class baseline and lift added to all accuracy reporting |
| C-4 | §9 no-leakage conclusion downgraded to HOLD (R-08) |
| C-5 | §12 and L-09 lower-bound claim withdrawn as non-monotonic (R-07) |
| C-6 | §2 and L-02 threshold-robustness claim narrowed to the structural bound (R-06) |
| C-7 | §2 ceiling scope restated per R-05 |
| C-8 | Two previously undetected fabrications disclosed as R-11, R-12 |
| C-9 | Disclosure that the report column was never computed, with grep evidence |
| C-10 | Open action recorded: add T15, report-to-artefact numeral verification |

---

## 9. Revision r2 — three further documentation errors, 22 November 2026

The reviewer accepted the numerical resolution and the interpretive corrections, then found **three
statements in my own reconciled copy that I had failed to propagate**. All three were real. The r1 file
as reviewed is preserved at `11_A18_2_EXECUTION_REPORT_RECONCILED_r1_as_reviewed.md`.

| ID | Error | Correction |
|---|---|---|
| **E-1** | §12 still read "within 1,606 of 1,827 day clusters". I corrected the fabricated figure in the §9 table and left the same number standing in §12. | **306 of 1,827 (16.7%)** |
| **E-2** | §12 still read "what is robust is the ordering, not the level" — the exact claim R-06 withdrew in §2. | Replaced: the **bound** is structural; **B2's location inside it is not robust** to its thresholds. |
| **E-3** | §2 and register item L-01 said the ceiling is reached only by an advisor that "always proposes `DepartureTime` or `Duration`". | Sharpened — see below. |

### E-3 is a genuine correction to the mathematics, not just wording

The endpoints of `0 ≤ I_CF ≤ P(CAUTION)` are conditions on **CAUTION cases alone**:

- `I_CF = P(CAUTION)` **iff** the advisor proposes `DepartureTime` or `Duration` in **every** CAUTION case.
- `I_CF = 0` **iff** it proposes `Go` or `Delay` in every CAUTION case.

Behaviour in SAFE and UNSAFE cases is **irrelevant to `I_CF`**: no SAFE case can be incrementally
excluded, and every UNSAFE case is already excluded by C1, so neither can contribute to the C1→C2
increment. It follows that **the ceiling is attainable without a constant advisor** — an advisor
proposing `Go` throughout SAFE and UNSAFE but timing or duration across all 531 CAUTION hours reaches
5.8128% exactly. My "always proposes" phrasing described a *sufficient* condition as if it were
necessary, which understates how reachable the ceiling is.

### What E-1 to E-3 have in common with the original fabrications

Every one is the same failure mode: **a hand-written prose statement that no longer matched a computed
artefact.** The fabrications invented numbers; these three carried stale ones forward. Correcting a
figure in one table while an identical claim survives two sections later is the propagation half of the
same problem.

## 10. Revised remediation spec — the reviewer's §3 point is accepted

My earlier T15 proposal was a numeral grep. The reviewer is right that this is insufficient: a bare
match would pass a figure that coincides with an unrelated number, and would say nothing about whether
the surrounding sentence describes the quantity correctly. The revised specification is that each
reported statistic must carry a machine-checkable binding to:

1. the **computed artefact** and row/field it came from;
2. the **metric definition** used (so 0.5937 under a subsampled search cannot silently stand in for
   0.5939 under an exhaustive one);
3. the **source population** (all hours vs departure window vs daylight-only, which already produced one
   real defect in A18.1 Step 4);
4. the **numerator and denominator**, not only the percentage.

That is a report-generation discipline, not a grep: figures should be **emitted from the artefacts**
rather than typed beside them. **It is specified here and not yet implemented.** Until it exists, the
standing instruction holds — read numbers from the CSVs, not from my prose.

## 11. Changelog, continued

| Entry | Change |
|---|---|
| C-11 | §12 cluster figure corrected 1,606 → 306 of 1,827 (E-1) |
| C-12 | §12 threshold-robustness claim withdrawn, matching §2 (E-2) |
| C-13 | §2 and L-01 bound condition sharpened to CAUTION-cases-only; ceiling shown attainable by a non-constant advisor (E-3) |
| C-14 | r1 file preserved as `..._r1_as_reviewed.md` |
| C-15 | T15 spec upgraded from numeral matching to artefact + definition + population + numerator/denominator binding |
| C-16 | Open action retained and unimplemented: retrospective audit of the A18.1 Step 2–4 reports for the same report-vs-artefact gap |
