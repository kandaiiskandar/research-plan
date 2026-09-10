# Report — Journal 1 Algorithm Specification, Batch 1

**Task:** Journal 1 Algorithm Specification — Batch 1: Authority & Operational Contract
**Task file:** [`docs/tasks/Journal 1 Algorithm Specification batch 1.md`](../../docs/tasks/Journal%201%20Algorithm%20Specification%20batch%201.md)
**Branch:** `design/journal1-algorithm-specification`
**Reported on:** 2026-09-10
**Maintained authority:** [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md)
**Evidence directory:** [`data/journal1-algorithm-specification/`](.)

---

## Authority findings

Per-construct authority is mapped in [`authority-map.csv`](authority-map.csv) (27 entries). Anchor points:

- **Operational classifier** `F_{D,τ} = f ∘ ρ_{D,τ}` — appendix-c **C.2.0.1** and **C.8.1**.
- **Observation space** `Obsᵢ = (Xᵢ × 𝕋) ∪ {⊥}` — **C.2.0.2**; the four conditions (invalid / absent / stale / unmeasured) at **C.2.0**.
- **`v` as startup configuration** — **C.2.0.6**; well-formedness **(D1) `t ∉ D`** — **C.2.0.5**.
- **Rainfall two-input contract** — **C.2 g_r row (retyped 2026-09-09)** and **C.2.0.4a** (χ map, {95, 96, 99}, `κ` never ⊥, missing rate → ⊥).
- **Solar-event `g_t` (SDR-001)** — **C.2 g_t row** and **Theorem C.1(i) g_t case**; consumes the frozen artefact via `scripts/canonical_gt.py`.
- **Wind 21.6 / 27.0 kn** — **C.2 g_w row**; vessel-conditional wave rows — **C.2 g_o row**; **"Note: there is no g_v"**.
- **Max-severity** — **C.2 Aggregation** and **Definition C.1**; **UNSAFE is a governance state, not a physical-world claim** — **C.2 How UNSAFE is reached**.
- **`G(S)`** — **C.3**; **`A_AI(S)`** — **C.4**; **governance constraints** — **C.6**; **RS(S) pre-reasoning** — **C.7.1** and **Theorem C.3 A1–A4**; **human authority** — **C.8.2 step 6**.
- **Layer 3 rule engine** — **justification-layer3-enforcement.md §2, §2a, §3, §4**.
- **Canonical labels C0/C1/C2 and J1-P1** — **evaluation-specification.md §3, §4, §6**.

---

## Confirmed operational contract

The maintained authority is [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md), sections 1–10. Algorithms 1–4 must preserve:

1. **Three-line type system.** `ρ_{D,τ} : ∏Obsᵢ → Y`; `f : Y × V → S`; `F_{D,τ} = f ∘ ρ_{D,τ}`. Algorithm 1 is never reduced to `S = f(E)`.
2. **Evaluation order (C.2.0.7).** Refuse-startup checks → exclusion pin → validation + freshness → κ derivation → clock/date/solar resolution → max-severity aggregation. Exclusion-before-fault is mandatory.
3. **Five component classifiers.** `g_w` (21.6 / 27.0 kn), `g_r(r, κ)` (10.0 / 20.0 mm/hr + storm route), `g_m` (ordinal), `g_o(o, v)` (vessel-conditional; wave-height coordinate only), `g_t(t, d)` (half-open `[sunrise, sunset)`, no CAUTION, frozen solar artefact). `gᵢ(⊥) = UNSAFE` uniformly.
4. **Rainfall specificity.** χ is total into K; missing raw code → `κ = 0` (fail-*open* on the storm disjunct, **not** fail-safe); missing rate → `⊥`.
5. **Aggregation.** Five terms; `v` conditions `g_o` only; severity order `UNSAFE ≻ CAUTION ≻ SAFE`.
6. **Governance.** `G(SAFE) = G(CAUTION) = 1`; `G(UNSAFE) = 0`; `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`; `R = {Go, Delay, DepartureTime, Duration}` fixed.
7. **RS(S) supplied before reasoning** by Layer 2 under A1–A4; no output filter, no runtime check for Safety Dominance.
8. **Human decision unconditional in all three states.**

Full type table with invariants at [`operational-contract.csv`](operational-contract.csv).

---

## Open implementation decisions

Seven bounded OPEN items in [`open-decisions.csv`](open-decisions.csv), none of which invents a value:

| ID | Item | Reason it is open |
|---|---|---|
| OPEN-B1-1 | `ageᵢ` freshness parameters | Specification-parameterised (C.2.0.4); no value proposed. |
| OPEN-B1-2 | Runtime provenance trace capture | Specification-only per C.2.0.8. |
| OPEN-B1-3 | Medium-vessel `g_o` 2.8 m boundary | Interpolated; direct medium-vessel operability data absent. |
| OPEN-B1-4 | Layer 3 prototype build (RS(S) concrete rule lists) | Batches 2 / 3 scope. |
| OPEN-B1-5 | `g_m` operational configuration in a live deployment | Deployment-time decision (C.2.0.5). |
| OPEN-B1-6 | Latency acceptance threshold `H3 = X ms` | Inherited from evaluation-specification.md OPEN-1. |
| OPEN-B1-7 | Decision-support utility construct | Inherited from evaluation-specification.md OPEN-2. |

---

## Files changed

**Created only — no canonical or tracked file modified.**

Maintained authority:

- [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) — sections 1–10; no pseudocode.

Evidence directory ([`data/journal1-algorithm-specification/`](.)):

- [`integrity-before.json`](integrity-before.json) · [`integrity-after.json`](integrity-after.json)
- [`authority-map.csv`](authority-map.csv) · [`operational-contract.csv`](operational-contract.csv) · [`open-decisions.csv`](open-decisions.csv) · [`change-map-batch1.csv`](change-map-batch1.csv)
- [`semantic-verification-batch1.json`](semantic-verification-batch1.json) — 18 PASS / 0 FAIL / 1 OPEN
- [`parser-test-batch1.json`](parser-test-batch1.json) — PASS across 4 CSVs
- [`build.py`](build.py) — integrity + parser check
- [`closure-batch1.json`](closure-batch1.json) — closure record
- [`report-batch1.md`](report-batch1.md) — this report

All 4 CSVs parse cleanly under `csv.reader` (strict field-count), `csv.DictReader` and `pandas.read_csv`.

Scientific effect of each change is recorded in [`change-map-batch1.csv`](change-map-batch1.csv) — all rows report *"None — new maintained authority / new evidence artefact. No canonical scientific state is altered."*

---

## Protected state

16 canonical files rehashed and matched byte-for-byte against the prior evaluation-specification pin.

- Verifier: [`build.py`](build.py) — `git hash-object` over each file.
- Before-state: [`integrity-before.json`](integrity-before.json).
- After-state: [`integrity-after.json`](integrity-after.json).
- **Verdict:** `PASS — 16 unchanged, 0 changed.`

Stop conditions from task §16 — none raised:

| Stop condition | Status |
|---|---|
| `PROTECTED_STATE_MISMATCH` | NOT RAISED — all 16 files byte-identical to prior pin |
| `FORMAL_AUTHORITY_CONFLICT` | NOT RAISED — none observed |
| `RAINFALL_SEMANTIC_CONFLICT` | NOT RAISED — appendix-c and canonical scripts agree |
| `SOLAR_SEMANTIC_CONFLICT` | NOT RAISED — appendix-c and `canonical_gt.py` agree |

---

## Verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 CLOSED —
OPERATIONAL CONTRACT VERIFIED
```

Per task §Branch, no closure commit is required yet — that is deferred to the end of Batch 3. Batches 2 and 3 (Algorithms 1–4 pseudocode and complexity analysis) can proceed against this contract on request.

---

## Post-repair — Transition Consistency Repair (2026-09-10)

**Task:** [`docs/tasks/JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 repair.md`](../../docs/tasks/JOURNAL%201%20ALGORITHM%20SPECIFICATION%20BATCH%201%20repair.md)

**What changed.** One bounded implementation over-specification in [`algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) §8. The atomic-swap sentence was replaced with a **state/rule-set consistency requirement per reasoning episode** — the rule set used for the next reasoning episode must be `RS(S_new)`, and no episode may execute with a rule set inconsistent with the state governing it — while leaving the enforcement mechanism (atomic swap, immutable snapshot, locking, transactional update, serialized execution, or an equivalent) unspecified. The **consistency requirement is mandatory**; the **mechanism is bounded OPEN** as OPEN-B1-8.

**F3 scope preserved.** Fidelity criterion F3 in [`evaluation-specification.md`](../../publications/active/journal-1/evaluation-specification.md) §7 continues to test that no stale or inconsistent rule set is used across a state transition.

**No canonical file modified.** The 16 protected files remain byte-identical to the prior pin ([`integrity-after.json`](integrity-after.json)).

**Evidence updates.**

- [`algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) §8 (wording repair) and §10 (OPEN-B1-8 row appended).
- [`open-decisions.csv`](open-decisions.csv) — OPEN-B1-8 appended.
- [`semantic-verification-batch1.json`](semantic-verification-batch1.json) — new check `transition_consistency_requirement_bounded` (PASS); summary refreshed (PASS 18 → 19; OPEN count unchanged at 1).
- [`closure-batch1.json`](closure-batch1.json) — post-repair closure line and note added; §17 checklist wording refreshed.
- [`change-map-batch1.csv`](change-map-batch1.csv) — five rows appended, one per file touched by the repair.

**Re-verification.** `python3 build.py` — integrity PASS (16 unchanged, 0 changed), parser PASS (4 CSVs).

### Post-repair verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION BATCH 1 CLOSED —
TRANSITION CONSISTENCY CONTRACT REPAIRED
```

Closure condition met: implementation mechanism remains OPEN while the state/rule-set consistency requirement remains mandatory.

---

*Author: iskandar · Batch 1 report · 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
