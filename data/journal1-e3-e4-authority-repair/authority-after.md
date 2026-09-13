# E3 / E4 Authority — AFTER the micro-repair

## E3 — scope bounded

**`evaluation-specification.md` §13** now reads, in substance:

> Cross-configuration resolution sensitivity is reported under PRIMARY and RESOLUTION for empirical quantities whose evaluation design supports a like-for-like comparison.
>
> **Mandatory dual-configuration scope: E3 covers {E1, E2, E6}.**
>
> **E4 is outside the mandatory scope: `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN`.**

with the `NOT_REQUIRED` semantics stated explicitly (not ZERO / NOT_FOUND / FAILED / REFUTED), and with the three prohibited inferences named: E4 is *not* claimed resolution-insensitive, *not* claimed to reproduce under MFWAM, and *not* treated as a missing result from an experiment that should have been run.

**Line 168 (M-Empirical-E3)** now carries the `{E1, E2, E6}` mandatory scope and the E4 exclusion pointer.

**M-Empirical-E4** now states "PRIMARY chronology only" and points to §13.

**§18** no longer designates the frozen `evaluation-specification.csv` as the single source of truth — see `scope-rationale.md` §6.

**`claim-status-matrix.csv` row E3** — `definition`, `required_evidence`, `existing_evidence`, `next_action` and `manuscript_claim_prohibited` rewritten to the bounded scope. `status` remains **CLOSED**.

## E4 — unchanged

`claim-status-matrix.csv` row E4 verified **content-identical** before and after. Values preserved exactly:

| Quantity | Value |
|---|---|
| transitions | 3,661 |
| scheduled transitions | 3,439 |
| non-scheduled transitions | 222 |
| oscillations | 26 |
| hysteresis reduction | 10.36% |

`status` remains **CLOSED**. Nothing recomputed; `hysteresis_analysis.py` not run and not modified.

## Resulting contract

```
E3 = CLOSED
E4 = CLOSED
E3_SCOPE = {E1, E2, E6}
E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
```

E1/E2/E6 dual-configuration evidence verified present and unchanged:

| | PRIMARY | RESOLUTION |
|---|---|---|
| C0↔C1 | 42.88% | 41.08% |
| C0↔C2 | 48.69% | 45.56% |
| C1↔C2 | 5.81% | 4.48% |
| C1↔C3 | 0.00% | 0.00% |
