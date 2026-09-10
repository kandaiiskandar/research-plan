# Report — Journal 1 Algorithm Specification, Batch 2

**Task:** Journal 1 Algorithm Specification — Batch 2: Algorithms 1 & 2
**Task file:** [`docs/tasks/Journal 1 Algorithm Specification batch 2.md`](../../docs/tasks/Journal%201%20Algorithm%20Specification%20batch%202.md)
**Branch:** `design/journal1-algorithm-specification`
**Reported on:** 2026-09-10
**Maintained authority:** [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) (Batch 1 §§1–10 unchanged; Batch 2 adds §§11–16)
**Evidence directory:** [`data/journal1-algorithm-specification/`](.)

---

## Algorithm 1 — Operational Safety Classification

Publication-quality pseudocode implementing `S = F_{D,τ}(obs, v) = f(ρ_{D,τ}(obs), v)`. Full text at [`algorithm-specification.md §11`](../../publications/active/journal-1/algorithm-specification.md).

**Signature.**

```text
Input  : obs = (obs_i){i∈C};  v ∈ V ∪ {⊥_cfg};  D ⊆ {w,r,m,o};  τ_now ∈ 𝕋;
         age = (age_i){i∈C∖D};  date ∈ Date;  solar : Date → (sunrise, sunset)
Output : S ∈ {SAFE, CAUTION, UNSAFE}   — or startup refusal (no S)
```

**Procedure summary (38-line pseudocode, 10-step ordering).**

1. **Startup — `v`** (lines 1–3). `v ∉ V` → refuse startup, return `STARTUP_CONFIGURATION_ERROR`.
2. **Well-formedness — `D`** (lines 4–8). `t ∈ D` or `D ⊄ {w,r,m,o}` or `D = {w,r,m,o}` → refuse startup.
3. **Exclusion pin** (lines 9–11). For `i ∈ D`, `s_i ← SAFE` before any fault handling.
4. **Validation + freshness for `w, m, o`** (lines 12–14). `y_i ← fresh_i(val_i(obs_i), τ_now, age_i)`.
5. **Rainfall two-input classifier** (lines 15–24). `(rate_obs, c_obs) ← obs_r`; `y_rate ← fresh_r(val_r(rate_obs), τ_now, age_r)`; `κ ← χ(c_obs)` (total, `χ(absent) = 0`); `y_r ← ⊥` if `y_rate = ⊥`, else `y_r ← (y_rate, κ)`.
6. **Time / date / canonical solar dependency** (lines 25–31). Read `solar(date)` from the frozen artefact; no astronomy is computed inside Algorithm 1. Failed clock/date/solar → `y_t ← ⊥`.
7. **Five component classifiers** (lines 32–36). `g_w, g_r, g_m, g_o(·, v), g_t(·, date)` — exactly five contributions; `v` conditions `g_o` only; **there is no `g_v`**.
8. **Max-severity aggregation** (line 37). `S ← max-severity(s_w, s_r, s_m, s_o, s_t)` under `UNSAFE ≻ CAUTION ≻ SAFE`.
9. **Return `S`** (line 38).

**Contract** — full detail at [`algorithm-contracts-batch2.csv`](algorithm-contracts-batch2.csv):

- **Preconditions.** P1: `obs` total over `C`. P2: `date` valid, `solar(date)` available. P3: `age_i` specified (symbolic; OPEN-B1-1). P4: `D` well-formed.
- **Postconditions.** Q1: exactly one `S` for valid startup (Theorem C.1b). Q2: `v ∉ V` refuses startup — not a runtime fault (C.2.0.6). Q3: fault-driven UNSAFE via `g_i(⊥) = UNSAFE` (Corollary C.1b.1); rainfall UNSAFE whenever `y_rate = ⊥` irrespective of `c_obs`. Q4: max-severity aggregation. Q5: excluded pin at SAFE; figures under `D ≠ ∅` are lower bounds.
- **Failure behaviour.** Startup / configuration failure returns no `S`; runtime observation fault returns a valid `S` which is UNSAFE. The two modes are disjoint.

---

## Algorithm 2 — Governance Configuration

Publication-quality pseudocode implementing the finite mapping `S → (G(S), A_AI(S))`. Full text at [`algorithm-specification.md §13`](../../publications/active/journal-1/algorithm-specification.md).

**Signature.**

```text
Input  : S ∈ {SAFE, CAUTION, UNSAFE}                   (valid output of Algorithm 1)
Output : (G(S), A_AI(S))
         G(S)    ∈ {0, 1}
         A_AI(S) ⊆ R = {Go, Delay, DepartureTime, Duration}
```

**Procedure.** A single switch over `S`:

| Case | `G` | `A_AI` |
|---|---|---|
| `SAFE` | 1 | `{Go, Delay, DepartureTime, Duration}` |
| `CAUTION` | 1 | `{Go, Delay}` |
| `UNSAFE` | 0 | `∅` |

Return `(G, A_AI)`. **No rule firing, no advisory generation, no RS(S) selection** — the tuple `(G(S), A_AI(S))` is the input Algorithm 3 (Batch 3) will require. OPEN-B1-8 remains OPEN.

**Contract** — full detail at [`algorithm-contracts-batch2.csv`](algorithm-contracts-batch2.csv):

- **Preconditions.** P1: `S ∈ {SAFE, CAUTION, UNSAFE}` by Theorem C.1b.
- **Postconditions.** Q1: exactly one `(G, A_AI)` for every valid `S`. Q2: `G(S)` matches C.3 exactly. Q3: `A_AI(S)` matches C.4 exactly. Q4: participation constraint `G(S) = 0 ⇒ A_AI(S) = ∅` (case UNSAFE). Q5: advisory restriction `A_AI(CAUTION) ⊊ A_AI(SAFE)`. Q6: containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`.

**Bounded correctness language.** Algorithm 2 *implements* the finite mapping on which Theorem C.2 (Monotonicity) is established. It **does not** experimentally validate Theorem C.2 — Theorem C.2 is proved in appendix-c C.6.

---

## Boundary verification

Twenty-four specification-level checks in [`boundary-cases-batch2.csv`](boundary-cases-batch2.csv), each resolved by inspection against the maintained mappings and thresholds. **All PASS.**

**Algorithm 1 — component boundary (B1–B12): 12/12 PASS**

| Case | Input | Expected | Result |
|---|---|---|---|
| B1 | `w = 21.6` | `g_w = SAFE` | PASS |
| B2 | `w = 27.0` | `g_w = CAUTION` | PASS |
| B3 | `w = 27.1` | `g_w = UNSAFE` | PASS |
| B4 | `r = 10.0`, `κ = 0` | `g_r = SAFE` | PASS |
| B5 | `r = 20.0`, `κ = 0` | `g_r = CAUTION` | PASS |
| B6 | any `r`, `κ = 1` | `g_r = UNSAFE` (storm route) | PASS |
| B7 | small, `o = 1.0` | `g_o = CAUTION` | PASS |
| B8 | small, `o = 1.25` | `g_o = CAUTION` | PASS |
| B9 | medium, `o = 1.4` | `g_o = CAUTION` | PASS |
| B10 | medium, `o = 2.8` | `g_o = CAUTION` | PASS |
| B11 | big, `o = 1.5` | `g_o = CAUTION` | PASS |
| B12 | big, `o = 3.5` | `g_o = CAUTION` | PASS |

**Algorithm 1 — semantic checks (B13–B20): 8/8 PASS**

| Case | Input | Expected | Result |
|---|---|---|---|
| B13 | `t = sunrise(date)` | `g_t = SAFE` (half-open) | PASS |
| B14 | `t = sunset(date)` | `g_t = UNSAFE` (half-open) | PASS |
| B15 | `t < sunrise` or `t ≥ sunset` | `g_t = UNSAFE` | PASS |
| B16 | missing rainfall rate | rainfall component UNSAFE | PASS |
| B17 | missing raw code + valid rate | `κ = 0`; classify from rate alone | PASS |
| B18 | `m ∈ D` | `s_m = SAFE` (pin) | PASS |
| B19 | `m ∉ D`, `obs_m` missing/invalid | `s_m = UNSAFE` via `g_m(⊥)` | PASS |
| B20 | `v` missing/invalid | startup refusal — no `S` returned | PASS |

**Algorithm 2 — exhaustive verification (B21–B24): 4/4 PASS**

| Case | Input | Expected | Result |
|---|---|---|---|
| B21 | `S = SAFE` | `(1, {Go, Delay, DepartureTime, Duration})` | PASS |
| B22 | `S = CAUTION` | `(1, {Go, Delay})` | PASS |
| B23 | `S = UNSAFE` | `(0, ∅)` | PASS |
| B24 | containment across `S` | `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` | PASS |

**Overall: 24/24 PASS.** No statistical test is required or appropriate — these are deterministic set/arithmetic checks against the specification.

---

## Correctness mapping

Full table at [`algorithm-traceability-batch2.csv`](algorithm-traceability-batch2.csv). Every construct carried by Algorithms 1 and 2 sits in exactly one of four categories.

**Algorithm 1 → operational totality and fail-safe semantics:**

- `F_{D,τ}` totality on `Y × V` — **theorem-derived** (Theorem C.1b); Algorithm 1 realises the composition. Future fidelity: F1 replay conformance.
- `g_i(⊥) = UNSAFE` fail-safe — **theorem-derived** (Corollary C.1b.1); Algorithm 1 lines 19–23 and 29–30 produce `⊥`, lines 32–36 apply the per-component convention. Future fidelity: F1.
- Startup precondition (`v`, `D`) — **definition-derived** (axiomatic; C.2.0.5–6); Algorithm 1 lines 1–8 refuse startup. Future check: startup-refusal test, outside F1.
- Exclusion-before-fault — **definition-derived** and covered by Lemma C.1c (monotone degradation); Algorithm 1 lines 9–11.

**Algorithm 2 → participation, advisory restriction and monotonicity:**

- `G(S)` and `A_AI(S)` mappings — **definition-derived** (C.3, C.4); Algorithm 2 realises them line-for-line.
- Participation constraint (`G(S) = 0 ⇒ A_AI(S) = ∅`) — **theorem-derived** (Theorem C.3 case 1); Algorithm 2 case UNSAFE.
- Advisory restriction (`A_AI(CAUTION) ⊊ A_AI(SAFE)`) — **theorem-derived** (Corollary C.2); Algorithm 2 cases SAFE and CAUTION.
- Monotonicity — **theorem-derived** (Theorem C.2); Algorithm 2 realises the finite mapping on which the theorem is proved. **Not experimentally validated.**

**Deferred to future implementation-fidelity tests:** F1 (replay conformance), F2 (recommendations outside `A_AI(S)` count = 0), F3 (RS(S) switching correctness at transitions — Batch 3). All three remain OPEN — see OPEN-B1-4 and OPEN-B1-8.

**Bounded language observed.** No sentence in the specification or evidence writes "Algorithm 1 proves safety" or "Algorithm 2 validates monotonicity experimentally." Correctness statements everywhere use *implements* / *realises the mapping on which the theorem is proved* / *invariant relied on*, never *proves* or *validates*.

---

## OPEN items

**Items relevant to Algorithms 1 & 2** — none newly introduced by Batch 2. The following pre-existing Batch 1 OPEN items are the ones that touch either algorithm:

- **OPEN-B1-1** — freshness parameters `age_i`. Batch 2 carries them symbolically in Algorithm 1's input list and in P3. Matched by semantic check `tau_not_invented`.
- **OPEN-B1-3** — medium-vessel `g_o` 2.8 m boundary. Batch 2 does not touch the value; Algorithm 1 line 35 delegates to canonical `g_o` unchanged.
- **OPEN-B1-4** — Layer 3 prototype build (concrete `RS(SAFE)` and `RS(CAUTION)` rule lists). Deferred; Algorithm 2 references `RS(S)` only as handoff to Algorithm 3.
- **OPEN-B1-5** — live `g_m` configuration. Batch 2 does not hard-code `D`; Algorithm 1 is general over any well-formed deployment `D`. The replay's `D = {m}` remains a deployment-specific choice.
- **OPEN-B1-8** — state/rule-set consistency enforcement mechanism. `RS(S)` selection is deferred to Algorithm 3 (Batch 3); no concurrency primitive is chosen.

**Items not touched by Batch 2** (preserved unchanged, per task §23):

- OPEN-B1-2 — runtime provenance capture.
- OPEN-B1-6 — latency threshold `H3 = X ms`.
- OPEN-B1-7 — decision-support utility construct.

**No Batch 1 OPEN item was silently closed.**

---

## Files changed

Full record with scientific effect per file at [`change-map-batch2.csv`](change-map-batch2.csv).

**Maintained authority (edited):**

- [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) — six new sections §§11–16 added (Algorithm 1 pseudocode; Algorithm 1 pre-/postconditions; Algorithm 2 pseudocode; Algorithm 2 pre-/postconditions; Batch 2 boundary verification; Batch 2 correctness traceability). Scientific effect: **none** — new algorithm specification sections that implement the CLOSED Batch 1 operational contract. No Algorithm 3 or 4, no complexity analysis, no canonical file modified.

**Evidence directory (created):**

| File | Rows | Scientific effect |
|---|---|---|
| [`algorithm-contracts-batch2.csv`](algorithm-contracts-batch2.csv) | 22 | None — evidence artefact |
| [`boundary-cases-batch2.csv`](boundary-cases-batch2.csv) | 24 | None — evidence artefact |
| [`algorithm-traceability-batch2.csv`](algorithm-traceability-batch2.csv) | 21 | None — evidence artefact |
| [`semantic-verification-batch2.json`](semantic-verification-batch2.json) | 23 checks | None — evidence artefact (22 PASS / 0 FAIL / 1 OPEN) |
| [`parser-test-batch2.json`](parser-test-batch2.json) | 4 CSVs | None — evidence artefact (all PASS; auto-generated by `build.py`) |
| [`change-map-batch2.csv`](change-map-batch2.csv) | 8 | None — evidence artefact |
| [`closure-batch2.json`](closure-batch2.json) | closure record | None — evidence artefact |
| [`report-batch2.md`](report-batch2.md) | this report | None — reporting artefact |

**Evidence directory (edited):**

- [`build.py`](build.py) — partitions CSVs by suffix (`-batch2.csv` → Batch 2 bucket, otherwise Batch 1); emits both `parser-test-batch1.json` and `parser-test-batch2.json`. Idempotent, read-only against project state.

**Canonical files touched:** none.

---

## Protected integrity

Same 16 protected canonical files as Batch 1.

- **Unchanged:** 16
- **Changed:** 0
- **Verdict:** `PASS — 16 unchanged, 0 changed`

Full record at [`integrity-after.json`](integrity-after.json), regenerated by `python3 build.py`.

Stop conditions from task §24 — none raised:

| Stop condition | Status |
|---|---|
| `ALGORITHM_1_SEMANTIC_CONFLICT` | NOT RAISED |
| `ALGORITHM_2_GOVERNANCE_CONFLICT` | NOT RAISED |
| `NEW_SCIENTIFIC_DECISION_REQUIRED` | NOT RAISED |
| `PROTECTED_CANONICAL_STATE_DRIFT` | NOT RAISED |

---

## Verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 CLOSED —
ALGORITHMS 1 AND 2 VERIFIED AGAINST OPERATIONAL CONTRACT
```

Closure criteria in task §25 met: all 22 items met; boundary cases 24/24 PASS; semantic checks 22 PASS / 0 FAIL / 1 OPEN (matches specification's own parameterisation); protected canonical state unchanged; no workstream-closing commit yet (deferred to end of Batch 3).

Batch 3 (Algorithms 3 & 4: RS(S) supply and advisory generation within `RS(S)`) can proceed against this contract on request.

---

## Post-repair — Exclusion-Set Domain Repair (2026-09-10)

**Task:** *Journal 1 Algorithm Specification Batch 2 — Exclusion-Set Domain Repair.*

**Canonical position — no contradiction.** Appendix-c C.2.0.5 states `(D1) t ∉ D` and `(D2) D ⊊ C`, and explicitly names `D = {w, r, m, o}` as *"the maximal well-formed exclusion set"*. The prior Batch 2 wording had rejected `D = {w, r, m, o}`, which was strictly stronger than canonical.

**What changed.**

- **Algorithm 1 input signature** (§11 header). `D ⊆ {w, r, m, o}` replaced with `D ⊆ C`, with an inline note that (D1) and (D2) are enforced at the well-formedness check and that `{w, r, m, o}` is the maximal well-formed exclusion set.
- **Algorithm 1 well-formedness check** (§11 lines 5–8). `if t ∈ D or D ⊄ {w, r, m, o} or D = {w, r, m, o}` replaced with `if t ∈ D or D ⊄ C`. (D2) `D ⊊ C` now follows automatically from (D1) since `t ∈ C ∖ D`. **No new requirement is added** that any of `{w, r, m, o}` must remain observed.
- **Algorithm 1 P4** (§12). Rewritten against `C = {w, r, m, o, t}` with an explicit statement that `D = {w, r, m, o}` is well-formed and reduces `S` to `g_t(y_t, date)`.
- **Boundary verification** (§15). Case B25 added: `D = {w, r, m, o}` → well-formed startup; `s_w = s_r = s_m = s_o = SAFE` by pin; `t` classified normally by `g_t`; `S = g_t(y_t, date)`. Section header count 24 → **25**.

Exclusion-before-fault is preserved unchanged — the exclusion pin loop (§11 lines 9–11) runs before any fault handling for every `i ∈ D`, including the new B25 case where all four non-time components are excluded. Algorithm 1 remains general over any deployment-specific `D`; the replay's `D = {m}` is not hard-coded anywhere.

**Scope guard — nothing else moved.**

- Canonical files: none touched (appendix-c C.2.0.5 was already correct; Batch 2 misread it).
- Batch 1 sections §§1–10 of `algorithm-specification.md`: unchanged.
- Algorithm 2 (§13, §14): unchanged.
- Thresholds, classifier semantics, governance mappings, rainfall semantics, solar semantics: unchanged.
- Batch 1 OPEN items OPEN-B1-1..8: all preserved.

**Evidence updates.**

| File | Change |
|---|---|
| [`algorithm-contracts-batch2.csv`](algorithm-contracts-batch2.csv) | A1 input row and A1 P4 row rewritten against C |
| [`boundary-cases-batch2.csv`](boundary-cases-batch2.csv) | Appended B25 (PASS) |
| [`algorithm-traceability-batch2.csv`](algorithm-traceability-batch2.csv) | "D well-formedness" row rewritten; (D2) follows from (D1) |
| [`semantic-verification-batch2.json`](semantic-verification-batch2.json) | `D_wellformedness_preserved` evidence rewritten; added `exclusion_maximal_wellformed_D_admitted` (PASS); PASS 22 → **23**; post-repair note |
| [`closure-batch2.json`](closure-batch2.json) | `post_repair_closure_line` and `post_repair_note` added; §25 checklist entry refreshed; boundary-case count 24 → **25**; semantic PASS count 22 → **23** |
| [`change-map-batch2.csv`](change-map-batch2.csv) | Seven repair rows appended |
| [`report-batch2.md`](report-batch2.md) | This post-repair section |

**Re-verification.**

```
python3 data/journal1-algorithm-specification/build.py
integrity:      PASS — 16 unchanged, 0 changed
parser batch1:  PASS — 4 CSVs checked
parser batch2:  PASS — 4 CSVs checked
```

**Canonical contradiction check.** No canonical authority contradicts the repair. Appendix-c C.2.0.5 explicitly names `D = {w, r, m, o}` as the maximal well-formed exclusion set. The repair aligns Algorithm 1 with that definition.

### Post-repair verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 2 CLOSED —
EXCLUSION-SET DOMAIN CONTRACT REPAIRED
```

Closure condition met: Algorithm 1 reproduces the canonical exclusion domain exactly.

---

*Author: iskandar · Batch 2 report · 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
