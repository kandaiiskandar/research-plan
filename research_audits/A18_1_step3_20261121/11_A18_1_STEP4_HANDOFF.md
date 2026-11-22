# A18.1 Step 4 Handoff — exact commands, NOT executed

**From Step 3, 21 November 2026.** Everything below was prepared and verified read-only. **Nothing here was run.** Step 4 is separately authorized.

---

## 1. Verified entry point

**Use `scripts/condition_comparison.py`.** It is the only canonical script that defines C0–C3, that handles both configurations, and that merges correctly. Do **not** use `historical_replay.py` for Step 4: it has no C0–C3 notion, never reads the MFWAM file, and carries the latent gust-alignment defect A-08.

Read-only by default — the register write at `:333-334` requires `--write-register`, which **must be omitted**.

## 2. Commands

```bash
cd /Users/iskandar/Documents/my_stuff/research-test-2

# Confirm the environment matches the documented pins
python3 -c "import pandas, numpy; print(pandas.__version__, numpy.__version__)"
# expect: 2.3.3 2.2.6

# Confirm inputs are the ones Step 2 and Step 3 audited
sha256sum data/raw_weather_sea.csv data/raw_marine_era5_sea.csv \
          data/raw_marine_mfwam.csv data/solar/solar-events-daily.csv \
          data/prediction-register.csv

# THE RUN. No flags. Register stays read-only.
python3 scripts/condition_comparison.py | tee \
  research_audits/A18_1_step4_YYYYMMDD/step4_console.log

# Confirm nothing was written
sha256sum data/prediction-register.csv
git diff HEAD --diff-filter=MD --name-only   # must be empty
```

**Do not pass** `--write-register`. **Do not pass** `--v1-historical` to any script: that selects the F-10 condemned land cell.

## 3. Expected input hashes

Any difference means the data changed since Step 2 and Step 4 must stop.

```
96850d7547189ffa5ccc02a36cf69987bfae742e54b61597c2ca7d251e84c424  data/raw_weather_sea.csv
6754e2c2ee5586ee864e590f1ccf363bbd8840b364763e01e8c9eb05e5d63888  data/raw_marine_era5_sea.csv
e9f323e086a3e9dddd29129bda6dbbea7590bbdcc9a1500c0460ca18233bf60f  data/raw_marine_mfwam.csv
5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6  data/prediction-register.csv
```

Local hashes only. Not provider checksums (Step 2 D-07).

## 4. Configuration matrix eligible for Step 4

| Configuration | Wave file | Vessel | Expected records | Expected window hours | Eligible |
|---|---|---|---:|---:|---|
| PRIMARY | `raw_marine_era5_sea.csv` | small only | 43,848 | 9,135 | **YES** |
| RESOLUTION | `raw_marine_mfwam.csv` | small only | 28,501 | 5,935 | **YES** |
| v1 land cell | `raw_marine.csv` | — | — | — | **NO** — F-10 condemned |
| medium / big vessel | — | — | — | — | **NO** — not in the published comparison (A-02) |

Both counts were independently reproduced in Step 2 and the rules reproduced in Step 3.

## 5. Expected output schema

`divergence_matrix()` prints, per configuration and per mask (all hours, departure window):

- state distribution: counts and percentages for SAFE, CAUTION, UNSAFE
- a 4×4 pairwise divergence matrix over `ORDER = ["C0", "C1", "C3", "C2"]`, as percentage of hours where the two configurations permit different admissible sets
- the pre-registered checks P21–P24

## 6. Reproduction targets — expectations, not success criteria

From the manuscript. **Do not hard-code these into any computed field** and do not adjust anything to reach them.

| Quantity | Pair | PRIMARY | RESOLUTION |
|---|---|---:|---:|
| Intermediate binding Δ_L2 | C2 vs C1 | 5.81% | 4.48% |
| Participation-only | C0 vs C1 | 42.88% | 41.08% |
| Combined | C0 vs C2 | 48.69% | 45.56% |

### Two predictions Step 3 has already settled analytically

**P21 (C1 vs C3 = exactly 0.0) will reproduce as 0.00 by construction**, because C1 and C3 are identical dict literals (A-04). Confirming it numerically verifies the harness, not the architecture.

**Δ_L2 will equal P(S = CAUTION) exactly**, because C1 and C2 differ only at CAUTION (A-05). So the C2-vs-C1 cell and the CAUTION share of the state distribution must agree to floating-point precision in every configuration and mask. **If they disagree, the harness is wrong** — that is the sharpest single check available in Step 4.

A useful arithmetic cross-check for PRIMARY: 5.81% of 9,135 window hours ≈ 531 hours, which matches the figure recorded at `aai-2026-evidence-resolution-and-configuration-register.md:94`.

## 7. Mandatory reporting constraints

Carried from Step 2 and Step 3, to be stated in the Step 4 report:

1. **Δ_L2 is a state-occupancy frequency**, invariant to the content of `RESTRICTED`, and since `Go` and `Delay` both survive the restriction it says nothing about the departure recommendation (A-05, A-06).
2. **P21 is definitional** (A-04).
3. **Small vessel only** (A-02).
4. **`g_t` buckets by integer hour** against float solar values, which shifts the daylight boundary to the next whole hour and bears directly on the first two departure-window hours (A-10).
5. **Operator inclusivity is asymmetric by source phrasing**; state the three conventions (A-01).
6. **The 1.0/1.25 m band is a researcher length-to-tonnage transfer**, not a certified marine safety threshold (A-03).
7. **`g_m` is pinned to SAFE as a model assumption**; every state is a LOWER BOUND on severity, and this is not an observed absence of warnings (D-05, R-08).
8. **`decision_time_availability` is UNKNOWN for 100% of records** — hindsight replay (D-08).
9. **PRIMARY vs RESOLUTION is a two-factor change**, wave product and wind–wave co-location 7.20 km vs 2.73 km; no difference may be attributed to resolution alone (D-12).
10. **Do not equate** governance binding, state occupancy or threshold crossing with correct or safe fishing actions, and **do not** import A1/A2/A3 fisheries action semantics — the conference types are exactly `{Go, Delay, DepartureTime, Duration}`.

## 8. Independent check available to Step 4

`08_reconstruction_reference.py` in the Step 3 folder is a standing, dependency-free implementation of the contract. Step 4 can classify any record with it and compare against the original without importing pandas. It matched the original on 164 real records across all three states and on 62 boundary fixtures, with zero mismatches.

## 9. Stop conditions

Step 4 is percentage and count reproduction only. No expert adjudication, no historical warning reconstruction, no algorithm design, no safety inference, no change to the accepted paper's data or conclusions.
