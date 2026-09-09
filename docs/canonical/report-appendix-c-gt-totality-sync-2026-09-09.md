# Appendix C `g_t` Totality Synchronisation Report

**Date:** 2026-09-09
**Role:** formal-specification maintainer and canonical-state auditor
**Type:** formal synchronisation — **not** a new scientific decision
**Appendix C:** `1ce268154807bd70` → **`e5c3bb8f2effc5d4`**
**Manuscript:** `27b33b846ae327cb` — **unchanged**

---

## 1. Scope

Bring every *active* canonical `g_t` definition, proof, signature and cross-reference in Appendix C into agreement with SDR-001 Model B. Bounded to `appendix-c-formalisation.md` plus evidence artefacts. Zero empirical change.

## 2. Trigger

The Appendix C Rainfall Signature Synchronisation recorded, as unrelated drift found in passing, that Theorem C.1 still proved totality with the superseded fixed-clock intervals. This is that repair — and the occurrence audit found the defect was **not** confined to Theorem C.1.

## 3. Before-state hashes

23 protected artefacts hashed into `integrity-before.json`.

## 4. Canonical Model B source

SDR-001, applied 2026-09-08 at C-8. Appendix C already declared it canonical at C.1 and in the C.2 `g_t` threshold table with the correct type `g_t : (X_t × Date) ∪ {⊥} → {SAFE, UNSAFE}` and the half-open statement. **The declarations were right; the proof and several supporting lines were not.**

## 5. Canonical executable `g_t`

`scripts/canonical_gt.py` — every row defaults to UNSAFE and is overwritten only when the clock is finite **and** the date is present in the frozen artefact:

```python
out = np.full(len(t), UNSAFE, dtype=int)     # fail-safe default
if not np.isfinite(hi):        continue      # ⊥ → UNSAFE
a, b = sr.get(dates[i]), ss.get(dates[i])
if a is None or b is None:     continue      # ⊥ → UNSAFE
out[i] = SAFE if (a <= hi < b) else UNSAFE   # half-open
```

Half-open `a <= hi < b`; never returns CAUTION; the superseded fixed clock survives only in `g_t_incumbent_superseded`. **GT-1 and GT-2 not triggered.**

## 6. Frozen solar dependency

`data/solar/solar-events-daily.csv`, 1,827 rows, `solar-spec-v1` / `solar-v1`, 5.98° N / 116.01° E, UTC+8. Sunrise spans 5.997043–6.552977 h, sunset 17.937669–18.582765 h. **`0 ≤ sunrise < sunset < 24` holds on all 1,827 dates** — the proof's domain assumption is verified, not assumed. No canonical script computes astronomy. **GT-3 not triggered.**

## 7. Appendix C occurrence audit

18 loci classified in `gt-occurrence-audit.csv`: **7 ACTIVE-CANONICAL repaired**, 8 active and already correct, 3 historical/superseded retained, 1 irrelevant.

## 8. Active fixed-clock defects found

The brief anticipated one defect. **Seven were found**, four of them beyond the stale proof:

1. **Theorem C.1(i) `g_t` case** — the known defect.
2. **The C.2 `g_t` *Domain* line** — `[6,17), [17,19), [19,24) ∪ [0,6)` asserted as the exhaustive partition, sitting **outside** the superseded blockquote and entirely unmarked, 22 lines after the correct two-interval statement. This carried an **active time-CAUTION band** and was the more dangerous of the two, being indistinguishable from current semantics.
3. **The open-provenance blockquote** — described **SDR-001 as "DRAFT — not approved, not applied"**, false since C-8, and quoted 87.63% (a superseded-classifier figure) as though current.
4. **The column-revision note** — "thresholds unchanged", true of the wording cleanup but misleading after SDR-001 replaced the thresholds the same day. This is the §27 contradictory chronology.
5. **The Per-Component preamble** — a *second* type declaration carrying `X_r = ℝ≥0` and "four single-argument functions", contradicting the C.2.0.1 type table. **Residue the rainfall synchronisation did not reach**; repaired here for internal consistency and recorded as such rather than presented as in-scope.
6. **`f(E)` form and Theorem C.1 conclusion** — `g_t(t)` without the date.
7. **C.2.0.7 evaluation order** — no explicit time-dependency resolution step, leaving room for the "missing solar ⇒ night" reading §22 prohibits.

## 9. Historical fixed-clock occurrences retained

The SUPERSEDED blockquote (06:00/17:00/19:00 and the withdrawn 17:00–19:00 CAUTION band), the C.9 migration comparison column, the C.1 superseded note, and the evidence/policy blockquote. All explicitly marked; a reader cannot mistake them for current semantics. **Not deleted** — they are legitimate provenance.

## 10. `g_t` signature assessment

`g_t : (X_t × Date) ∪ {⊥} → {SAFE, UNSAFE}` was already correct and was **not** changed. Only the *usage* sites were brought into line: `g_t(t, d)` in the `f(E)` form, the Theorem C.1 conclusion and evaluation-order step 3.

## 11. Valid-input domain

`X_t = [0, 24)` **deliberately unchanged**. The existing architecture treats the clock as the classifier value and date/solar as required context resolved upstream; that separation is intentional and is now stated explicitly rather than widened into `X_t`. No global type rewrite.

## 12. Revised totality proof

For valid `(t, d)`, with `s_r = sunrise(d)`, `s_s = sunset(d)` and `0 ≤ s_r < s_s < 24`:

- `[s_r, s_s)` and `[0, s_r) ∪ [s_s, 24)` are **disjoint** — a point cannot be both inside and outside a set;
- and **exhaustive** — every `t ∈ [0, 24)` satisfies exactly one of `t < s_r`, `s_r ≤ t < s_s`, `t ≥ s_s`.

`g_t` returns SAFE on the first and UNSAFE on the second, so every valid `(t, d)` receives exactly one classification. **Two intervals, not three.** No twilight interval invented; no CAUTION introduced.

## 13. Boundary semantics

Verified against the canonical implementation on 2024-03-20 (sunrise 6.341591, sunset 18.452345), probing at 1e-6 — below the artefact's six-decimal stored precision, so no epsilon was invented:

| Case | Result |
|---|---|
| just before sunrise | UNSAFE ✓ |
| **exact sunrise** | **SAFE** ✓ |
| just after sunrise | SAFE ✓ |
| midday | SAFE ✓ |
| just before sunset | SAFE ✓ |
| **exact sunset** | **UNSAFE** ✓ |
| just after sunset | UNSAFE ✓ |
| midnight, 23:59 | UNSAFE ✓ |

**CAUTION emissions across all 1,827 dates: 0.**

## 14. Operational totality

Theorem C.1b required **no change**. Its proof already quantifies over `Xᵢ ∪ {⊥}` generically. The ideal/operational distinction is preserved: C.1 covers valid clock, date and solar context; C.1b covers resolution failure.

## 15. Fault vs policy semantics

Evaluation-order steps 2a and 2b were made explicit, with the load-bearing sentence stated plainly: a failed clock, date or solar lookup reaches UNSAFE **as a fault**, and **does not establish that it is night**. The two routes to `g_t = UNSAFE` agree in value and differ in provenance. Verified: failed clock → UNSAFE, failed date → UNSAFE, both via the fail-safe rather than a valid-night inference.

## 16. Cause-taxonomy impact

**None.** `reasons : Q → 𝒫({fault, hazard, policy})` unchanged; valid night → **policy**, failed time dependency → **fault**, both already correct at C.2.0.8. No new reason category. Valid night is not classified as hazard.

## 17. Surjectivity assessment

`Im(g_t) = {SAFE, UNSAFE}` retained. The non-surjectivity subsection is intact, and the repaired proof states explicitly that **totality does not require surjectivity** — the old proof's three time bands mirrored the three global states for no reason other than symmetry, which is precisely the error. No time-based CAUTION reintroduced.

## 18. Scenario/test impact

SC-10 and SC-15 are **not present in Appendix C** — they live elsewhere and were not touched. No table or scenario in Appendix C makes a bare active claim such as "18:00 = CAUTION"; the only such values sit inside marked-superseded blocks.

## 19. Empirical invariance

Canonical generators re-run after the edits: Level 2 **5.81% / 4.48%**; `g_t` all-hours non-SAFE **86.82% / 90.19%**; `g_o` daylight CAUTION **98.71% / 97.66%**; `g_r` daylight CAUTION **1.48% / 2.70%**; daylight UNSAFE 1,262 / 455; transitions **3,661 / 3,439 (93.9%) / 222 → 199 (10.36%) / 26 oscillations**. The canonical 1,536 direct SAFE→UNSAFE and 0 time-driven SAFE→CAUTION Model B metrics were not recomputed under any modified classifier. **GT-4 not triggered.**

## 20. Prediction-register invariance

**24 · 15 CONFIRMED / 9 REFUTED**, P09 actual 3,661, P20 actual 1,529. Untouched. P20's registered 06:00–17:00 scope and the 455 astronomical-daylight RESOLUTION count remain distinct; no wording rewrote historical prediction scope. SDR-001 attribution remains P20/P23/P24 only, and the P09 chain 5,416 → 5,220 → 5,201 → 3,661 is not collapsed. **GT-5 not triggered.**

## 21. Files changed

`docs/canonical/appendix-c-formalisation.md` — eight loci, all in `gt-formal-change-map.csv`, every row `semantic_change = NONE`.

## 22. Files intentionally unchanged

The manuscript — checked against verified Model B semantics and found in agreement, so **GT-6 not triggered and no edit made**. All canonical scripts, the prediction register, the frozen solar artefacts, C5–C8 evidence, historical reports and submissions, and Journal 1.

**Note on solar provenance:** Appendix C contains **no NOAA or USNO wording at all** — that provenance lives in the manuscript and the Solar Citation Closure report. There was nothing to preserve here and nothing was changed. Reported as an observed absence rather than claimed as a preservation.

## 23. Protected-state verification

23 artefacts re-hashed. **Changed: 1 — Appendix C. Unexpected: none.** `__pycache__` swept. Both CSVs parser-tested with `csv.DictReader` **and** `pandas.read_csv` under a strict field-count check: PASS. Consistency sweep `all_consistent: true`, with **0 active fixed-clock hits** and **0 active time-CAUTION hits**.

**One error of my own, caught and corrected:** the first draft of the repaired proof cited `(C.9.2)` for the solar ordering assumption. C.9.2 is "Parameters not vessel-conditioned" — a plausible-looking but false cross-reference, exactly the failure mode this workstream exists to catch. Both instances now point to the frozen artefact directly, and the ordering is labelled a property of the low-latitude study site rather than a general astronomical claim.

## 24. Deferred repository drift

1. `CLAUDE.md` — 98.66 / 97.41 → 98.71 / 97.66
2. `canonical_figures.py` trailer — "22 kn" → 21.6 kn
3. `docs/justification/formal-model.md`, `docs/reference/explainer-per-component-classification-functions.md`, `docs/canonical/data-provenance.md` — scalar `g_r`
4. Journal 1 manuscript and section plans — scalar/categorical `g_r` and fixed-clock `g_t`

## 25. Stop-condition assessment

| | Condition | Triggered |
|---|---|---|
| GT-1 | Canonical Model B conflict | **NO** |
| GT-2 | Boundary semantics conflict | **NO** — half-open verified at both ends |
| GT-3 | Solar dependency conflict | **NO** |
| GT-4 | Unexpected empirical drift | **NO** |
| GT-5 | Prediction state drift | **NO** |
| GT-6 | Manuscript contradiction | **NO** |
| GT-7 | Active fixed-clock residue | **NO** — 0 hits |
| GT-8 | Active time-CAUTION residue | **NO** — 0 hits |

## 26. Final closure decision

All closure criteria pass. Model B is verified canonical; exact sunrise is SAFE and exact sunset UNSAFE; `Im(g_t) = {SAFE, UNSAFE}` with no active time-based CAUTION anywhere in the document; Theorem C.1 proves totality over the astronomical partition with disjointness and exhaustiveness argued rather than asserted; no fixed-clock totality proof remains; operational failures remain fail-safe and are distinguished from valid night in both the evaluation order and the cause taxonomy; no theorem requires component surjectivity; the evidence/policy boundary is intact; and the empirical and prediction state is bit-identical.

The canonical formal proof now says exactly what the canonical classifier does. Historical fixed-clock semantics remain, clearly marked as provenance.

---

*Artefacts:* `data/appendix-c-gt-sync/` — `integrity-before.json`, `integrity-after.json`, `gt-occurrence-audit.csv`, `gt-formal-change-map.csv`, `gt-boundary-verification.json`, `gt-canonical-consistency.json`, `parser-test.json`, `closure.json`, `build.py`.

---
---

# Independent Closure Residue Repair

**Date:** 2026-09-09 · **Appendix C:** `e5c3bb8f2effc5d4` → **`abee8715e842e0d9`** · **Manuscript:** `27b33b846ae327cb` unchanged

**These were closure-hygiene defects, not a new scientific decision.** No SDR was opened, no threshold moved, no classifier changed, and no empirical value shifted. The core Model B repair above stands; what follows makes its closure claim literally true.

## 1. Independent-review trigger

The preceding section ended `CLOSED`. Independent review found **two active canonical residues** that the closure sweep had missed. Both misses trace to the same methodological fault: **the sweep searched for the superseded classifier's *time strings*, never for its *chronology claims* or its *empirical metric*.** A residue can assert stale canon without containing "06:00".

Specifically:

- **L42 was reported "HISTORICAL-MARKED" because the line contains the word "previously"** — which referred to the *row wording*, not to the thresholds. A line-level keyword heuristic cannot distinguish which clause a marker governs, and it produced a false negative on a bolded, sentence-final active claim.
- **87.63% was never searched for at all.** No pattern in the sweep would have matched it.

## 2. C.1 chronology residue

The Time of Day Classification Note ended: **"The thresholds 06:00 / 17:00 / 19:00 are unchanged."** True of the pre-adoption wording cleanup at the moment it was written; false as an unqualified active statement once SDR-001 replaced those thresholds later the same day.

## 3. D1 87.63% residue

`(D1) t ∉ D` justified itself with: *"`g_t` determines 87.63% of all non-SAFE classifications at the study site (F-7)."* **Wrong twice over.**

First, the figure is superseded — computed under the fixed-clock classifier; the canonical share is 86.82% PRIMARY / 90.19% RESOLUTION. Second, and more seriously, **the reasoning was inverted.** Asked whether an empirical percentage is logically required to justify `t ∉ D`, the answer is **no**. Resting a structural constraint on a site-specific binding share would imply the constraint weakens wherever `g_t` binds less often — when in fact it holds at every site regardless of binding profile. Substituting the correct percentage would have preserved the error.

## 4. Exact repairs made

1. **C.1 chronology** — three-step sequence stated explicitly: the cleanup was wording-only and left the incumbent thresholds; SDR-001 superseded them later the same day; the fixed clock is not canonical. Historical provenance retained in a dated note.
2. **C.1 adjacent sentence** — *"the boundaries themselves have no located source"*, an equivalent Class A residue in the same paragraph, found by the audit rather than named in the brief. Under Model B the boundary comes from COLREGs Rule 20(b); what has no source is the **policy**, not the boundary. Corrected while preserving the policy-not-finding claim intact.
3. **D1** — restated **structurally**, with the empirical dependency removed entirely: declared exclusion is condition D (*no data source exists*), t is read from the device clock so no deployment satisfies that, and clock/date/solar failure is definitionally a fault. The canonical figures appear only in the dated correction note, configuration-labelled, explicitly carrying no part of the argument.

## 5. Occurrence-audit result

`residue-occurrence-audit.csv`, 7 loci. **Class A active: 0. Class B active: 0.** Retained as HISTORICAL-SUPERSEDED: the D1 correction note, the C.2 open-provenance blockquote, the C.2 SUPERSEDED block, the C.9 migration table. No historical provenance was deleted to obtain zero textual hits.

## 6. Model B consistency verification

Re-verified against `canonical_gt.py` on 2024-03-20: **exact sunrise SAFE · exact sunset UNSAFE · just before sunrise UNSAFE · just after sunset UNSAFE**; failed clock UNSAFE, failed date UNSAFE, both via the fault route; **0 CAUTION emissions across all 1,827 dates**. Active fixed-clock classifier definitions **0**; active time-derived CAUTION definitions **0**. Type, `Im(g_t) = {SAFE, UNSAFE}`, the `reasons` contract, COLREG lighting scope, the no-AI-abstention statement and unconditional human authority all intact. Fault/policy separation undisturbed — a missing solar lookup is nowhere described as evidence of night.

## 7. Protected-state verification

Level 2 **5.81% / 4.48%**; `g_t` all-hours non-SAFE **86.82% / 90.19%**; `g_o` daylight CAUTION **98.71% / 97.66%**; `g_r` daylight CAUTION **1.48% / 2.70%**; daylight UNSAFE **1,262 / 455**; register **24 · 15 / 9**; P09 **3,661**; P20 **1,529**. P09 chain and the P20-vs-455 scope distinction untouched; SDR-001 attribution remains P20/P23/P24.

## 8. Before/after Appendix C hash

`e5c3bb8f2effc5d4` → `abee8715e842e0d9`

## 9. Unexpected changed files

**None.** 20 protected artefacts re-hashed; exactly one changed — Appendix C. Manuscript, canonical scripts, frozen solar artefact and prediction register all byte-identical. CSV parser-tested with `csv.DictReader` and `pandas.read_csv`: PASS.

## 10. Deferred repository drift

Unchanged and still out of scope: `CLAUDE.md` 98.66/97.41; `canonical_figures.py` trailer "22 kn"; `docs/justification/formal-model.md`, `docs/reference/explainer-per-component-classification-functions.md`, `docs/canonical/data-provenance.md` scalar `g_r`; Journal 1 scalar/categorical `g_r` and fixed-clock `g_t`.

## 11. Final closure decision

All closure criteria pass. No stop condition (GT-R1…GT-R8) triggered.

**Method note worth carrying forward:** two consecutive sweeps of this document each declared closure while an active residue remained, because each searched for the *form* the previous defect had taken rather than for the *claim* being made. Detecting stale canon requires searching for superseded **assertions** — chronology, metrics, status — not only superseded **literals**.

---

*Closure-repair artefacts:* `data/appendix-c-gt-closure-repair/` — `integrity-before.json`, `integrity-after.json`, `residue-occurrence-audit.csv`, `closure-verification.json`, `parser-test.json`, `build.py`.
