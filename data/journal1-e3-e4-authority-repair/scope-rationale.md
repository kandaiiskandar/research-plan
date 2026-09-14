# Scope rationale — why E3 was narrowed rather than E4 extended

## 1. The original contradiction

E3's authority placed E4 inside a mandatory dual-configuration reporting scope and asserted that dual-configuration values existed for every empirical claim. E4's authority supplies PRIMARY-only values. E3 additionally prohibited "writing any empirical value as a single figure without the dual-configuration pair" — which is precisely what E4's own `manuscript_claim_allowed` requires.

The two CLOSED contracts were therefore mutually unsatisfiable for E4: reporting it violated E3, omitting it violated E4. This surfaced as a blocker during Journal 1 Manuscript Batch 8A before any manuscript edit was made.

## 2. Why E4 has PRIMARY-only evidence

`scripts/hysteresis_analysis.py` reads the PRIMARY configuration (sea-cell weather joined to `raw_marine_era5_sea.csv`) and contains no MFWAM path — the string does not appear in the file. The only alternative branch is `--v1-historical`, which reproduces the superseded v1 land-cell configuration and is not RESOLUTION. `scripts/canonical_figures.py`, cited by E3 as its existing evidence, emits no transition, oscillation or hysteresis figures at all. A repository-wide search returns no dual-configuration transition figure; every apparent hit is a co-mention of the PRIMARY five-tuple.

There is therefore no RESOLUTION E4 evidence anywhere in the repository, and none was ever produced.

## 3. Why E3 is narrowed rather than E4 extended

Producing RESOLUTION E4 values would require executing `hysteresis_analysis.py` under MFWAM — a new experiment, prohibited by this task and by Batch 8 §54.

More importantly, it would not be scientifically sound as a like-for-like sensitivity comparison even if run. E4 characterises **temporal dynamics** over a predefined chronology: PRIMARY spans 5.00 years (43,848 hourly records), RESOLUTION spans 3.25 years. Transition counts, oscillation counts and hysteresis reduction are **event counts over a window**. Two counts drawn from windows of different length and different temporal coverage are not comparable merely because both configurations carry the names PRIMARY and RESOLUTION. A difference between them would confound resolution effects with window-length effects, and would be uninterpretable as a sensitivity result.

The governing scientific principle adopted is therefore:

> Resolution sensitivity applies only to empirical quantities for which the evaluation design supports a like-for-like PRIMARY/RESOLUTION comparison.

E1, E2 and E6 satisfy this: they are **share-of-hours divergence rates**, normalised by their own denominators, and both configurations are computed by the same harness over their respective records. E4's raw counts do not.

## 4. Why this is not an E4 result change

No E4 value was read, recomputed, modified or reinterpreted. `hysteresis_analysis.py` was not run and not modified. The E4 row of `claim-status-matrix.csv` was verified **content-identical** before and after the repair, field by field, alongside every other non-E3 row. E4 remains CLOSED with exactly the values it held: 3,661 / 3,439 / 222 / 26 / 10.36%.

What changed is the *scope of a reporting contract that referred to E4*, not E4 itself.

## 5. Why no sensitivity claim about E4 is being made

`NOT_REQUIRED_BY_CURRENT_E3_DESIGN` is a statement about the comparison contract, not about the world. The repair explicitly does **not** assert:

- that E4 is insensitive to resolution — untested;
- that E4 would reproduce under MFWAM — unknown;
- that a RESOLUTION E4 result equals the PRIMARY one — no such result exists;
- that a required experiment was omitted — none was required by the design.

Any future E4 sensitivity evaluation must be separately authorised and would need to control for common temporal coverage, comparable input availability, and normalised transition and oscillation rates under equivalent hysteresis parameters. That design is not proposed here.

## 6. Provenance finding — `evaluation-specification.csv` is historical (Interpretation B)

The additional provenance check resolved decisively against filename or directory intuition:

**Evidence for B (historical closed evidence), accepted:**

1. Its `current_status` column is **stale by two batches** — F1, F2 and F3 read `OPEN — requires Layer 3 build`, whereas Batch 5 closed all three PASS with zero violations.
2. `data/journal1-evaluation-specification/build.py` contains **zero references** to the CSV. It does not generate it; it only computes `integrity-after.json` and `parser-test.json`. The CSV is hand-authored, not derived.
3. It is listed in that batch's `closure.json` artefact inventory alongside `integrity-before/after.json` — the signature of frozen batch evidence.
4. Batch 6 treated it as *corroboration* and explicitly recorded that its F1–F3 statuses were superseded, rather than updating it.

**Evidence for A (current companion authority), rejected:**

`evaluation-specification.md` §18 called it "the single-source-of-truth master table". That designation is itself stale drift: it points at an artefact that is demonstrably not maintained.

**Action taken.** The CSV was **not modified**. Its old E3 wording is recorded as historical and superseded in `historical-supersession-record.csv`. §18's designation was corrected in the live Markdown, because leaving it would have re-imported the pre-repair E3 wording through the back door — a reader following §18 to the "master table" would have found the superseded contract presented as authoritative.

## 7. Historical Batch 6 artefacts deliberately left unchanged

`report.md`, `replay-requirement-assessment.md` and `evaluation-dependency-graph.md` under `data/journal1-post-fidelity-plan/` retain the original "E1, E2, E4, E6" assertion. These are records of what Batch 6 concluded at that time, and erasing them would destroy the provenance of the contradiction itself. Each locus is enumerated in `historical-supersession-record.csv` with `current_status = SUPERSEDED`.
