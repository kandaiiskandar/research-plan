# A18.1 Step 3 — Governance Contract Reconstruction Report

**21 November 2026 · supervisor-ready · Step 3 only**
Accepted AAI2026 paper, presentation 23 December 2026. **No original file modified; originals confirmed byte-identical.**

Evidence tiers: `VERIFIED_FROM_CODE` read from source with line citation · `COMPUTED_FROM_FILE` recomputed here · `MANUSCRIPT_REPORTED` stated in the paper or its registers · `INFERRED` · `UNKNOWN`.

---

## 1. Headline

The contract reconstructed cleanly and **parity is exact**: 62 of 62 boundary fixtures pass, and 164 of 164 real canonical records classify identically between the reconstruction and `condition_comparison.py`. Every threshold and every comparison operator traces to a specific line. Three scripts define the thresholds independently and **all three agree**.

Two structural results are the substance of this step, and both are properties of the *contract* rather than findings about the world:

**Δ_L2 is identically P(S = CAUTION).** C1 and C2 agree at SAFE and at UNSAFE and differ only at CAUTION, so set-inequality divergence counts CAUTION hours and nothing else. It is invariant to the content of `RESTRICTED`.

**C1 and C3 are the same mapping.** Identical dict literals. So the pre-registered prediction P21 — "C1 vs C3 divergence exactly 0.0" — is a mathematical consequence, not a measurement.

A third property limits what the headline can mean: **`RESTRICTED` retains both `Go` and `Delay`**, the only two departure-decision types. Graduated restriction therefore never changes the departure recommendation; it withholds timing and duration detail only.

**Gate: GO for Step 4**, with conditions that are all reporting constraints rather than code work.

---

## 2. Table A — Manuscript versus code: thresholds, operators, precedence

| Component | Code (verified) | Operator | Manuscript statement | Agreement |
|---|---|---|---|---|
| `g_w` CAUTION | 21.6 kn | **strict `>`** | `> 21.6 kn` (review v8:188) | **MATCH** |
| `g_w` UNSAFE | 27.0 kn | **strict `>`** | `> 27.0 kn` | **MATCH** |
| `g_r` CAUTION | 10.0 mm/hr | **strict `>`** | `> 10.0 mm h⁻¹` | **MATCH** |
| `g_r` UNSAFE | 20.0 mm/hr **or** WMO ∈ {95,96,99} | **strict `>`**, set membership | `> 20.0 mm h⁻¹ or WMO code 95, 96, 99` | **MATCH** |
| `g_o` CAUTION, small | 1.0 m | **inclusive `≥`** | `≥ 1.0 m` | **MATCH** |
| `g_o` UNSAFE, small | 1.25 m | **strict `>`** | `> 1.25 m` | **MATCH** |
| `g_t` SAFE | sunrise ≤ hour < sunset | `≥` and `<`, half-open | `sunrise ≤ t < sunset` | **MATCH** |
| `g_t` image | {SAFE, UNSAFE}, no CAUTION | — | "daylight — / outside" | **MATCH** |
| `g_m` | held at SAFE | — | "excluded, held at SAFE" | **MATCH** |
| Aggregation | `max` over the five terms | `max` | `f(E) = max_>{g_w, g_r, g_m, g_o, g_t}` | **MATCH** |
| Vessel scope of published figures | small only (`condition_comparison.py:76` has no vessel parameter) | — | small (< 10 GRT) | **MATCH** |
| `g_t` time granularity | **integer hour vs float solar hour** | — | **not stated** | **UNKNOWN / undocumented** (A-10) |
| Operator inclusivity rationale | asymmetric by source phrasing | — | **not stated in the manuscript** | **documented only in review v8:168** (A-01) |

No threshold or operator disagreement exists between code and manuscript. The two unresolved cells are both *omissions from the manuscript*, not conflicts.

**Precedence.** There is none beyond `max`: the five components are independent and any UNSAFE term forces UNSAFE. CAUTION arises only when no term is UNSAFE and at least one is CAUTION. Because `g_t` never emits CAUTION and `g_m` is pinned to SAFE, **CAUTION can only come from `g_w`, `g_r` or `g_o`**. The one cross-component override is the WMO storm code, which forces UNSAFE at any rainfall value including 0.0.

---

## 3. Table B — Configurations C0–C3 by state

| Configuration | Role | SAFE | CAUTION | UNSAFE |
|---|---|---|---|---|
| **C0** ungated | policy baseline | FULL (4) | FULL (4) | FULL (4) |
| **C1** binary-gated | output mask | FULL (4) | FULL (4) | ∅ (0) |
| **C3** Flehmig-style | output mask | FULL (4) | FULL (4) | ∅ (0) |
| **C2** proposed | output mask | FULL (4) | **RESTRICTED (2)** | ∅ (0) |

FULL = {Go, Delay, DepartureTime, Duration} · RESTRICTED = {Go, Delay} · ∅ = {}

All four are **permissible-output masks** over a fixed candidate space, applied as a function of state. None is an advisor proposal: the replay has no proposal-generating step, so there is no `AI(E)` to mask. This is why the script's own "safety dominance" check is vacuous (A-07).

**Verified set relations** (fixtures I-5 … I-10):

- `A_AI(C2)[s] ⊆ A_AI(C1)[s]` at every state — restriction never adds.
- No configuration admits a type outside FULL — admission cannot introduce a category.
- `A_AI(C1) == A_AI(C3)` exactly.
- C1 and C2 differ at CAUTION **and nowhere else**.
- `{Go, Delay} ⊆ RESTRICTED` — both departure types survive.

### The Δ_L2 identity, stated exactly

Divergence is counted as set inequality over paired hours (`condition_comparison.py:198`). Given `A_AI[C1][s] = A_AI[C2][s]` for `s ∈ {SAFE, UNSAFE}` and `A_AI[C1][CAUTION] ≠ A_AI[C2][CAUTION]`:

> **Δ_L2 = (1/n) · |{h : S(h) = CAUTION}| = P(S = CAUTION)**

exactly, for any `n`. **When CAUTION truly binds:** at every CAUTION hour, under C2 and only under C2, the admissible set contracts from 4 types to 2. There is no hour at which C2 binds and the state is not CAUTION, and none at which the state is CAUTION and C2 does not bind.

Two consequences the report must carry: Δ_L2 is **invariant to the content** of `RESTRICTED`, so it says nothing about *which* types were withheld; and because `Go` and `Delay` both survive, it says nothing about the departure decision. It is a state-occupancy frequency. It is **not** evidence of utility, decision quality or maritime safety.

---

## 4. Table C — Test matrix

| Category | Fixtures | Pass | What was tested |
|---|---:|---:|---|
| `g_w` equality and adjacency | 6 | 6 | `nextafter` either side of 21.6 and 27.0, plus exact equality |
| `g_r` equality and adjacency | 6 | 6 | either side of 10.0 and 20.0, plus exact equality |
| `g_r` WMO override | 5 | 5 | codes 95/96/99 force UNSAFE at precip 0.0; 94 and 97 do not |
| `g_o` equality and adjacency, small | 6 | 6 | either side of 1.0 and 1.25 — **confirms inclusive onset, strict ceiling** |
| `g_o` non-canonical profiles | 6 | 6 | medium and big bands, flagged as unused by the published run |
| `g_t` solar boundary | 6 | 6 | hour at/after sunrise, hour containing sunset, midnight, hour 23 |
| `g_t` fail-safe | 2 | 2 | date absent from artefact; non-finite hour — both UNSAFE |
| `g_t` image | 1 | 1 | no CAUTION across 120 dates × 24 hours |
| `g_m` | 1 | 1 | held at SAFE |
| Departure window | 4 | 4 | **04:00 / 05:00 / 09:00 / 10:00** — inclusive both ends |
| Joint hazards and precedence | 8 | 8 | each component dominating alone; three simultaneous CAUTIONs; CAUTION + UNSAFE; all-at-onset; storm override alone |
| Determinism | 1 | 1 | 1,000 repetitions, one distinct result |
| Permutation invariance | 1 | 1 | all 120 orderings of the five terms |
| Unused inputs | 2 | 2 | `wave_period` and tide are not parameters of `f` |
| Policy set relations | 6 | 6 | subset, no-introduction, C1≡C3, CAUTION-only, binding, departure-preserved |
| **Total** | **62** | **62** | |

Every fixture is synthetic, generated in this folder, and carries `synthetic = YES`. **No fixture was written into any original dataset**, and none carries a reference action or safety label.

Each rule operator has at least one equality fixture and one fixture on each side. The requested `04:59`/`09:01` cases are represented as hour 4 and hour 10, because the implementation buckets by integer hour — `04:59` and `04:00` are the same bucket, so the hour-level fixture is the meaningful boundary. This is the same granularity issue raised in A-10.

---

## 5. Table D — Original versus reconstruction parity

| Sample | Records | Match | Mismatch |
|---|---:|---:|---:|
| A — systematic, every 1,000th joined record | 44 | 44 | 0 |
| B — stratified, first 40 reaching each state | 120 | 120 | 0 |
| **Total** | **164** | **164** | **0** |

State coverage: **SAFE 63 · CAUTION 43 · UNSAFE 58**.

Sample A alone yielded only 3 CAUTION rows, which is too thin for the state the paper turns on, so Sample B was added: a chronological scan taking the first 40 records to reach each state. Both are deterministic with no RNG, and strata are capped at 40 so this remains a small sample and computes **no percentage table**.

Comparison was against `scripts/condition_comparison.py:153-166 classify()` executed on the real canonical join, plus `historical_replay.g_w/g_r/g_o` and `canonical_gt.g_t` on every scalar fixture. **Parity is executable, not asserted.** No rule was adjusted to obtain agreement — there was nothing to adjust, since no mismatch arose.

---

## 6. Table E — Step 2 limitations carried forward, interpretation unchanged

| Step 2 ID | Limitation | Status in Step 3 |
|---|---|---|
| D-08 | `decision_time_availability` UNKNOWN for 100% of records; retrospective reanalysis only | **unchanged** — hindsight replay (A-11) |
| D-12 | PRIMARY vs RESOLUTION confounds wave product with wind–wave co-location, 7.20 km vs 2.73 km | **unchanged** (A-12) |
| D-05 | No marine-warning column exists; SAFE handling is a model assumption | **confirmed in code** — `g_m` pinned to SAFE at two sites (R-08, R-09) |
| D-02 | `wave_period` has 35 nulls and is unused | **confirmed** — absent from the contract, fixture I-3 |
| D-06 | Tide file unused | **confirmed** — absent from the contract, fixture I-4 |
| D-03 | Local-time claim is documented-only | **unchanged** |
| D-07 | No provider manifest; local hashes are not provider checksums | **unchanged** |
| D-11 | Stated coordinates are provider-snapped cells | **unchanged**; note `canonical_gt.py:62` records the same 5.98/116.01 request point for the solar artefact |
| D-01 | Land-cell files one careless path away | **satisfied** — selection is by `--v1-historical` flag at `historical_replay.py:121`, not by filename (R-24) |

No Step 2 interpretation was altered, softened or re-opened.

---

## 7. New findings from Step 3

Thirteen entries in `05_rule_assumptions_and_discrepancies.csv`. The ones that matter:

**A-05 and A-04 — the two identities.** Δ_L2 ≡ P(CAUTION), and C1 ≡ C3 making P21 definitional. Both are structural and must be stated, not discovered by a reader.

**A-06 — `RESTRICTED` keeps both departure types.** The restriction withholds `DepartureTime` and `Duration` only.

**A-01 — asymmetric operator inclusivity.** Wave is inclusive at its onset while wind and rain are strict. **This is not new and not a defect**: `aai-2026-independent-review-v8.md:133,168` already documents it and gives each operator its source — Jeong & Im's "1 m or above" is inclusive, the MMD *Ribut Petir* trigger "> 20 mm/hr" is strict, and 1.25 m is the top of the highest *passing* category so exactly 1.25 m still passes. That review's own verdict stands: the defect is that none of it is stated in the manuscript.

**A-03 — length-to-tonnage transfer.** The 1.0/1.25 m band is sourced from vessel *length* (≤ 10 m LOA; a 6.54 m vessel) and applied to a *tonnage* class (< 10 GRT). Researcher assumption. **Not certified marine safety thresholds.**

**A-10 — undocumented time granularity.** `g_t` compares an integer hour to a float solar hour, so a bucket is judged by its start: with sunrise at 6.424, hour 6 is UNSAFE despite 34 of its minutes being after sunrise. Defensible and conservative, but nowhere stated — and it bears directly on the departure window, whose first two hours sit around sunrise.

**A-07 — the vacuous safety-dominance check.** `historical_replay.py:246` reads `all(A_AI[s] <= A_AI[s] ...)`, comparing each set to itself, which is trivially true; the result is assigned and never used. **No safety-dominance property was tested by that code.** It affects no published figure, which comes from `condition_comparison.py`, but the section must not be cited as verification.

**A-13 — resolves a Step 2 warning.** The `prediction-register.csv` write is behind an explicit `--write-register` flag and did not fire; hash confirmed unchanged after import.

---

## 8. Table F — Step 4 readiness

### Gate: **GO**

Independent Step 4 reconstruction is possible **without rewriting any old code**. The contract is fully specified, every rule traces to a line, parity is exact over all tested fixtures and a state-stratified real sample, and the canonical entry point `condition_comparison.py` is read-only by default.

**Non-blocking conditions — all reporting constraints:**

1. Present Δ_L2 as the CAUTION-occupancy identity (A-05), with its invariance to `RESTRICTED` and the survival of `Go`/`Delay` (A-06).
2. Present P21 as definitional, not measured (A-04).
3. Run the **small** vessel profile only; say so (A-02).
4. State the `g_t` integer-hour granularity (A-10).
5. State the three operator conventions and their sources (A-01).
6. Describe the band as a researcher length-to-tonnage transfer, not certified (A-03).
7. Do not cite `historical_replay.py`'s safety-dominance section (A-07).
8. Carry D-08 and D-12 forward verbatim (A-11, A-12).
9. Omit `--write-register`; use `condition_comparison.py`, not `historical_replay.py`, for RESOLUTION (A-08).

**Blocking items: none.**

Two items block *claims* rather than execution, permanently: no operational-availability statement is possible (D-08), and no PRIMARY/RESOLUTION difference may be attributed to resolution alone (D-12).

---

## 9. Acceptance checks

| Check | Result |
|---|---|
| Originals byte-for-byte untouched | **PASS** — 5 artefacts hashed before and after; `git diff HEAD --diff-filter=MD` empty |
| Every rule traceable to exact source lines, or marked unverified | **PASS** — 30 rules in `02_`, each with path, function, line, exact text |
| No manuscript percentage hard-coded as a computed output | **PASS** — no percentage is computed anywhere in this folder |
| Parity executable, not asserted | **PASS** — 62 fixtures + 164 real records, 0 mismatches, exit 0 |
| Synthetic fixtures separate from historical data, no safety labels | **PASS** — all 62 carry `synthetic = YES` |
| ≥ 1 boundary fixture per operator and priority interaction | **PASS** — equality and both adjacencies for every active threshold; 8 joint-hazard cases |
| Clear GO/HOLD on independent Step 4 without rewriting old code | **PASS** — GO |
| All promised artifacts exist | **PASS** — 14 files verified present |
| Stopped after Step 3 | **PASS** — no percentages, no adjudication, no warning reconstruction, no algorithm design, no safety inference |
