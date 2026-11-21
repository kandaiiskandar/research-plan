# A18.1 Step 5 Handoff

**From Step 4, 21 November 2026.** Validated, reusable components and what remains scientifically open.
**No claim of independently verified policy safety is made anywhere below.**

---

## 1. Validated and reusable

| Component | Status | Path |
|---|---|---|
| Canonical population, PRIMARY | 43,848 usable / 9,135 window — **verified twice** | `03_population_reconciliation.csv` |
| Canonical population, RESOLUTION | 28,501 usable / 5,935 window — **verified twice** | same |
| State classification | **exact parity**, 34/34 quantities, two independent paths | `09_original_vs_independent_parity.csv` |
| Dependency-free classifier | stdlib, no pandas, line-cited to source | `../A18_1_step3_20261121/08_reconstruction_reference.py` |
| Independent aggregator | stdlib; populations, occupancy, decomposition, divergence, all variants | `independent_reproduce.py` |
| All 34 manuscript figures | reproduced at integer level | `07_manuscript_numerical_reconciliation.csv` |
| Input hashes | 9 artefacts, byte-identical before/after | `13_SHA256SUMS.txt` |

Step 5 can treat the population, the state assignment and every reported percentage as settled, and need not re-derive them.

## 2. The identity set Step 5 must carry

Verified at integer-numerator level in both configurations:

```
D(C1,C2) = #CAUTION / n          D(C0,C1) = #UNSAFE / n
D(C0,C2) = (#CAUTION + #UNSAFE) / n          D(C1,C3) = 0 / n
```

So **Δ_L2 is P(S = CAUTION)**, invariant to the content of `RESTRICTED`. Any Step 5 statement framing it as a comparative policy effect is unsupported by this evidence.

## 3. Case counts available for Step 5 selection

Departure window, canonical small-vessel profile. **Counts only — no case list, no selection, no labels were produced.**

| | PRIMARY | RESOLUTION |
|---|---:|---:|
| CAUTION hours (where C2 binds and C1 does not) | **531** | **266** |
| of which wave-bound | 518 | 253 |
| of which rain-bound | 13 | 13 |
| wind-bound | 0 | 0 |
| multi-component ties | 0 | 0 |
| UNSAFE hours | 3,917 | 2,438 |
| SAFE hours | 4,687 | 3,231 |

If Step 5 stratifies, the natural strata are wave-bound CAUTION (518) and rain-bound CAUTION (13). **The rain stratum is 13 cases and cannot support any quantitative comparison.**

## 4. What remains scientifically open

**Not closable from local artefacts:**

1. **Decision-time availability.** Every input is retrospective reanalysis. Closing this needs archived *issue-time* forecast products for Kota Kinabalu 2020–2024. Without them the replay is permanently hindsight (D-08).
2. **Any independent safety or utility outcome.** No harm, incident, decision-quality or user-benefit variable exists anywhere in the repository. No safety–utility trade-off can be stated.
3. **An AI proposal generator.** The replay masks a fixed candidate space; nothing was ever proposed, so nothing was ever withheld. Commission and omission risk are undefined here (B-05).
4. **Separating wave product from co-location.** Needs a wind field co-located with each wave cell — a new experiment, not a documentation fix (D-12, B-07).
5. **Certified vessel thresholds.** The 1.0/1.25 m band is a researcher transfer from vessel length to tonnage (A-03).
6. **A marine-warning archive.** None exists; `g_m` is pinned SAFE and every state is a lower bound (D-05).

**Closable cheaply:**

7. **The timezone claim** (D-03) — one provider request with `timezone=UTC`, compared on a single sample hour.
8. **Provenance authenticity** (D-07) — store request URL, parameters, response headers and retrieval timestamp on any future pull.

## 5. Statements Step 5 must not make

No maritime safety improvement. No effect on actual departure decisions. No injury prevention. No user benefit. No algorithmic novelty. No causal wave-resolution effect. No population safety guarantee. No IID confidence interval or significance test over state occupancy — the hours are strongly autocorrelated and these are exact frequencies over an archived period, not estimates with sampling error (B-08).

## 6. Reporting conditions

1. State each headline with the identity that produces it (B-04).
2. Note that `RESTRICTED` keeps `Go` and `Delay`, so the departure recommendation never changes.
3. Label the sourced envelope **small-vessel** (B-02).
4. State the `g_t` integer-hour granularity wherever the daylight-only figure appears (A-10).
5. Report the PRIMARY/RESOLUTION gap as **two opposing effects**, +1.97 pp and −0.64 pp, not one (B-07).
6. Keep `g_m` and the length-to-tonnage transfer explicit as assumptions.
7. Report the component concentration honestly: only **three of five** components can contribute CAUTION at all, since `g_t` emits none by design and `g_m` is pinned (B-06).

## 7. Re-running Step 4

```bash
cd /Users/iskandar/Documents/my_stuff/research-test-2
sha256sum -c research_audits/A18_1_step4_20261121/13_SHA256SUMS.txt   # inputs section
python3 scripts/condition_comparison.py                               # no --write-register
python3 scripts/sensitivity/threshold_sensitivity.py
python3 -I research_audits/A18_1_step4_20261121/independent_reproduce.py
git diff HEAD --diff-filter=MD --name-only                            # must be empty
```

Deterministic: no RNG anywhere, so repeated runs are bit-identical.
