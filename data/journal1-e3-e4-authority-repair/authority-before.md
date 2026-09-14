# E3 / E4 Authority — BEFORE the micro-repair

State as of HEAD `fcbbe8d`, before any modification.

## E3 (live authority)

**`publications/active/journal-1/evaluation-specification.md` §13 — global empirical-reporting contract**

> Every empirical figure in Journal 1 must be reported under both configurations. The difference between them is a **resolution-sensitivity result**, not a confidence interval. Do not write "`5.81 ± something`". If a value is available only under one configuration, state that explicitly and identify the missing configuration.

**`evaluation-specification.md` line 168 — M-Empirical-E3 metric row**

> Resolution sensitivity: report every empirical value under PRIMARY and RESOLUTION

**`data/journal1-post-fidelity-plan/claim-status-matrix.csv`, row E3**

- `definition` — "every empirical figure reported under PRIMARY … and RESOLUTION …"
- `required_evidence` — "Both configurations computed and reported for every empirical value in **E1 E2 E4 E6**."
- `next_action` — "None — **dual-configuration values exist for all empirical claims.** Enforce the reporting contract: every empirical figure in Journal 1 must appear under both configurations."
- `manuscript_claim_prohibited` — "Writing **any** empirical value as a single figure without the dual-configuration pair …"

## E4 (live authority)

**`claim-status-matrix.csv`, row E4**

- `required_evidence` — "Canonical values from `scripts/hysteresis_analysis.py`: 3,661 state transitions in 5 yr; 26 genuine oscillations (5.2/yr); hysteresis reduces non-scheduled transitions by 10.36%."
- `manuscript_claim_allowed` — single PRIMARY figures only.
- `status` — CLOSED.

## The contradiction

E3 named E4 inside its mandatory dual-configuration scope and asserted that dual-configuration values existed for all empirical claims. E4's authoritative evidence is PRIMARY-only, and `scripts/hysteresis_analysis.py` contains no MFWAM/RESOLUTION path at all. E3's own prohibition therefore forbade E4's own permitted reporting: writing E4 violated E3, and omitting E4 violated E4.
