# Report — Journal 1 Algorithm Specification, Batch 4

**Task:** Journal 1 Algorithm Specification — Batch 4: Complexity Analysis & Manuscript Integration
**Task file:** [`docs/tasks/Journal 1 Algorithm Specification batch 4.md`](../../docs/tasks/Journal%201%20Algorithm%20Specification%20batch%204.md)
**Branch:** `design/journal1-algorithm-specification`
**Reported on:** 2026-09-10
**Maintained authority:** [`publications/active/journal-1/algorithm-specification.md`](../../publications/active/journal-1/algorithm-specification.md) (Batches 1–3 §§1–24 unchanged; Batch 4 adds §§25–33)
**Manuscript integrated:** [`publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`](../../publications/active/journal-1/submissions/v1-initial-submission/manuscript.md) (§§7, 8, 9)
**Evidence directory:** [`data/journal1-algorithm-specification/`](.)

---

## Complexity summary

**Table.** Per-algorithm bounds and end-to-end. Full record at [`complexity-analysis-batch4.csv`](complexity-analysis-batch4.csv) and [`complexity-traceability-batch4.csv`](complexity-traceability-batch4.csv).

| Algorithm | Fixed time | Generalized time | Auxiliary space | Primary dependency | Status |
|---|---|---|---|---|---|
| **A1** — Operational Safety Classification | `O(1) + T_solar_lookup` | `O(n) + T_solar_lookup` | `O(1)` fixed / `O(n)` generalized | Solar-lookup representation (OPEN-B4-1) | PARAMETERISED |
| **A2** — Governance Configuration | `O(1)` | `O(1)` lookup; static storage `O(\|S\| · \|R\|)` | `O(1)` | Independent of dynamic input | DERIVED |
| **A3** — Rule-Set Supply | `O(1)` (prevalidated ref) *or* `T_select(S) + O(k_S)` | `T_select(S) + O(k_S)` | `O(1)` ref / `O(k_S)` materialised | Rule-repository representation | PARAMETERISED |
| **A4** — Governed Advisory Generation | `O(1) + T_engine(k_S, q, c)` | `O(1) + T_engine(k_S, q, c)` | `O(1) + M_engine` | Rule-engine strategy (OPEN-B3-2) | PARAMETERISED |
| **PIPELINE** — end-to-end per episode | `O(1) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)` | `O(n) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)` | sum of per-algorithm auxiliary + `M_engine` | Engine term retained explicitly | PARAMETERISED |

---

## Algorithm 1

**Fixed-model time.** `T_A1_fixed = O(1) + T_solar_lookup`. The seven stages of Algorithm 1 — startup validation, `D` well-formedness, exclusion pin, validation + freshness on `{w, m, o}`, rainfall two-input (with `κ = χ(c)`), solar/clock/date resolution, five component classifiers, max-severity aggregation — each contribute constant cost at `n = 5`, except the solar lookup.

**Generalized time.** `T_A1 = O(n) + T_solar_lookup`. Exclusion pin, validation/freshness, component classification and max-severity aggregation each become `O(n)`.

**`T_solar_lookup` left symbolic.** The specification requires runtime to consume the frozen artefact `data/solar/solar-events-daily.csv` via `scripts/canonical_gt.py` but does not fix the data structure. Dict-by-date is `O(1)` average; binary search is `O(log d)`; linear scan is `O(d)`. Recorded as **OPEN-B4-1**.

**Space.** `O(1)` fixed / `O(n)` generalized working memory. Raw external datasets and the 43,848-record replay are explicitly excluded from A1's per-decision memory.

---

## Algorithm 2

**Fixed-model time.** `T_A2_fixed = O(1)`. A switch on `S ∈ {SAFE, CAUTION, UNSAFE}` returns the pair `(G(S), A_AI(S))` in constant time.

**Lookup vs static mapping storage — separated.** Lookup itself is `O(1)` for hash / direct addressing on `S`; `O(|S|)` for linear scan. Static mapping storage (if `A_AI` is materialised as a `S → 2^R` table) is `O(|S| · |R|) = 12` bits under the current architecture — a **configuration property, not a per-decision cost**. The switch does not scan `|R|` on every decision.

**Space.** `O(1)` working memory — a `(G, A_AI)` pair.

---

## Algorithm 3

**`k_S` dependency explicit.** The parameterised expression is `T_A3 = T_select(S) + O(k_S)`, with `k_S` = number of rules in the active `RS(S)`.

**Selection vs materialisation — separated.** Two conceptually distinct costs, neither forced by the specification:

- `T_select(S)` — cost of `candidate(repository, S)`. `O(1)` if the deployment holds prevalidated state-indexed rule sets; `O(k)` if the selector scans the repository.
- Compliance check — `O(k_S)` scan of `RS_candidate` to test `ConclusionTypes ⊆ A_AI(S)`. Avoidable **only** if compliance is prevalidated at configuration time.
- Materialisation — `O(1)` reference vs `O(k_S)` materialised copy.

**Relevant OPEN items preserved.** OPEN-B3-1 (invalid rule-repository runtime handling) and OPEN-B1-8 (state/rule-set consistency enforcement mechanism) remain OPEN. The complexity table records the implementation choice as a dependency, not as a design decision.

---

## Algorithm 4

**Wrapper vs engine — separated.**

- **Governance wrapper:** `T_A4_wrapper = O(1)`. The `if G(S) = 0 then return ∅ else invoke engine` branch adds constant overhead.
- **Rule-engine reasoning:** `T_engine(k_S, q, c)` — parameterised, unspecified. **OPEN-B3-2** blocks selection of forward chaining, backward chaining, RETE, agenda priority, first-match, all-match, conflict resolution or rule salience.

**Total:** `T_A4 = O(1) + T_engine(k_S, q, c)`.

**Illustrative only.** A naïve linear scan of `RS(S)` under forward chaining would give `O(k_S · c)` — but this is **example only, not the architecture's official complexity**. Labelled `ILLUSTRATIVE ONLY` in [`complexity-traceability-batch4.csv`](complexity-traceability-batch4.csv).

**Space.** `M_A4 = O(1) + M_engine`. Agenda size, RETE network size and caching behaviour are not invented.

---

## End-to-end

Summed across A1 → A2 → A3 → A4 for one decision episode:

```
T_episode = O(n) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)
```

Under the fixed architecture (`n = 5`, `|S| = 3`, `|R| = 4`):

```
T_episode_fixed = O(1) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)
```

**The rule-engine term is retained.** `T_episode` is **not** `O(1)` merely because `n = 5`, `|S| = 3`, `|R| = 4` — Layer 3 reasoning cost dominates any classification / governance constant, and its concrete form is OPEN-B3-2.

---

## Replay complexity distinction

Per-decision complexity is independent of replay length. A retrospective replay of `N` records requires `N` decision evaluations:

- **Full pipeline:** `T_replay(N) = O(N · T_episode)`.
- **Classification-and-governance-only** (no engine invocation, applicable when Layer 3 is not yet built): `T_replay_no_engine(N) = O(N · (n + T_solar_lookup))`.

**The historical replay over 43,848 records is not `O(1)`.** It scales linearly in `N`, excluding external data-loading cost, and does not enter Algorithm 1's single-decision complexity. `N` is defined **only** for this replay-vs-per-decision distinction (§25, §30).

---

## Low-resource boundary

**Complexity analysis is not E5 evidence.** The results above support these bounded statements:

- Classifier and governance mappings operate over small fixed state spaces.
- Per-decision architecture avoids model-size growth in the number of replay records `N`.
- Rule-engine cost is retained as a parameter, not collapsed to a fixed complexity.

They do **not** support any of the following without independent E5 evidence:

- The architecture is lightweight.
- The architecture is efficient on low-end phones.
- The architecture is deployable in low-resource settings.
- The latency is negligible.
- Memory use is minimal.
- Energy use is low.

**H3 = X ms remains OPEN** (OPEN-B1-6). The manuscript's §9 bullet that previously read *"low-resource constraints: offline-first, lightweight"* was repaired — `"lightweight"` was removed and the bullet now reads *"Planned implementation stack targets: offline-first operation; per-decision working memory bounded (see §8). Device-level performance suitability requires E5 evidence and is not claimed here."*

**F1–F3 are separate.** Complexity analysis does not test whether a built Layer 3 prototype honours the engine-fidelity assumption. F1–F3 in `evaluation-specification.md` §7 remain future implementation-fidelity evidence.

---

## Manuscript integration

Full per-section trace at [`manuscript-integration-batch4.csv`](manuscript-integration-batch4.csv). Summary:

| Manuscript section | Change | Scientific effect |
|---|---|---|
| **§7 Algorithms** | Placeholder replaced with §§7.1–7.4 publication-ready pseudocode summaries for A1–A4 plus §7.5 Safety-Dominance Dependency four-link chain | Adds pseudocode; no scientific state change; formal notation preserved (`F_{D,τ}`, `ρ_{D,τ}`, `RS(S)`, `AI(E)`) |
| **§8 Complexity Analysis** | Placeholder replaced with three-level framing, notation table, per-algorithm complexity table §8.1, end-to-end §8.2, per-decision vs replay §8.3, low-resource claim boundary §8.4 | Adds bounded complexity claims; no low-resource deployability inference |
| **§9 Prototype Implementation** | One-line repair — "lightweight" removed | Repairs an unsupported claim without changing §9's status as an unbuilt prototype description |
| §§5, 6, 10, 11 | Audit only — no edit | Consistent with the new §§7–8 |

**Audits (no drift):**

- **Algorithm naming** — confirmed: Algorithm 1 — Operational Safety Classification / 2 — Governance Configuration / 3 — Rule-Set Supply / 4 — Governed Advisory Generation. No alternate formal names ("Safety Algorithm", "Gating Algorithm", "AI Safety Filter", "Decision Algorithm") introduced.
- **Formal notation** — `F_{D,τ}` used as operational classifier (not regressed to `S = f(E)`); no `g_v`; rainfall two-input signature preserved; `g_t` emits only SAFE / UNSAFE; sunrise/sunset half-open [sunrise(date), sunset(date)) preserved; `G(S)` and `A_AI(S)` exact; `RS(S)` supplied pre-reasoning; no post-hoc filter substitution.
- **Safety Dominance wording** — bounded to *"the governed advisory output is constrained to the configured admissible recommendation types for the current safety state, subject to the stated rule-engine fidelity assumptions"* (§7.4 Invariants). Forbidden phrasings ("algorithm guarantees safe decisions", "AI cannot produce unsafe advice") do not appear.
- **Human authority** — unconditional; §7.4 records that `AI(E) = ∅` does not forbid human action and `Go ∈ AI(E)` does not automatically approve departure.
- **F1–F3 boundary** — §8.4 states fidelity criteria remain future evidence; no PASS claim.
- **E5 boundary** — §8 opening states H3 remains OPEN; no latency / CPU / memory / energy measurement in the manuscript.

---

## OPEN items

**All prior OPEN items preserved unchanged.**

| ID | Item | Status |
|---|---|---|
| OPEN-B1-1 | Freshness parameters `age_i` | OPEN |
| OPEN-B1-2 | Runtime provenance capture | OPEN |
| OPEN-B1-3 | Medium-vessel evidence limitation | OPEN |
| OPEN-B1-4 | Layer 3 prototype (concrete rule contents) | OPEN |
| OPEN-B1-5 | Live `g_m` configuration | OPEN |
| OPEN-B1-6 | Latency threshold `H3 = X ms` | OPEN |
| OPEN-B1-7 | Decision-support utility construct | OPEN |
| OPEN-B1-8 | State/rule-set consistency enforcement mechanism | OPEN |
| OPEN-B3-1 | Invalid rule-repository runtime handling | OPEN |
| OPEN-B3-2 | Rule-engine evaluation strategy | OPEN |
| OPEN-B3-3 | Decision-episode implementation boundary | OPEN |

**One new bounded OPEN item introduced by Batch 4:**

| ID | Item | Reason |
|---|---|---|
| **OPEN-B4-1** | Solar-lookup data structure and its cost `T_solar_lookup` | The specification requires runtime to consume the frozen artefact via `scripts/canonical_gt.py` but does not fix the data structure. Dict / binary-search / linear-scan are all admissible. Deployment decision. |

**No prior OPEN item was silently closed by asymptotic analysis.**

---

## Protected integrity

Same 16 protected canonical files as Batches 1–3.

- **Unchanged:** 16
- **Changed:** 0
- **Verdict:** `PASS — 16 unchanged, 0 changed`

Stop conditions from task §31 — none raised:

| Stop condition | Status |
|---|---|
| `RULE_ENGINE_COMPLEXITY_REQUIRES_IMPLEMENTATION_DECISION` | NOT RAISED |
| `MANUSCRIPT_ALGORITHM_CONTRACT_CONFLICT` | NOT RAISED |
| `LOW_RESOURCE_PERFORMANCE_CLAIM_REQUIRES_E5` | NOT RAISED |
| `NEW_SCIENTIFIC_DECISION_REQUIRED` | NOT RAISED |
| `PROTECTED_CANONICAL_STATE_DRIFT` | NOT RAISED |

---

## Verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS CLOSED —
FOUR-ALGORITHM CONTRACT, COMPLEXITY BOUNDS AND MANUSCRIPT INTEGRATION VERIFIED
```

Closure criteria in task §32 met: all items MET; boundary distinctions preserved; semantic checks 23 PASS / 0 FAIL / 1 OPEN (matching the new bounded OPEN-B4-1); all prior OPEN items preserved; protected canonical state unchanged; no new scientific decision introduced.

**Workstream status.** The full Journal 1 **Algorithm Specification & Complexity Analysis workstream (Batches 1–4, plus two closed repairs) is now CLOSED.** The next workstream — Layer 3 Prototype Implementation → F1–F3 implementation-fidelity testing → E5 performance measurement — remains outside Batch 4 and can be picked up as a separate workstream when you say so.

---

## Post-repair — Final Complexity and Authority Residue Repair (2026-09-10)

**Task:** [`docs/tasks/Journal 1 Algorithm Specification — Batch 4 Repair.md`](../../docs/tasks/Journal%201%20Algorithm%20Specification%20%E2%80%94%20Batch%204%20Repair.md)

Two bounded repairs before Batch 4 is accepted as closed.

### Repair 1 — Algorithm 3 complexity matches the currently specified pseudocode

**Defect.** The Batch 4 report and evidence had listed *"O(1) (prevalidated reference) *or* T_select(S) + O(k_S)"* as the A3 fixed-model bound, treating the prevalidated-state-indexed variant as a form of the current algorithm's complexity. The currently specified Algorithm 3 pseudocode (§17 lines 5–9) **always** runs the compliance scan when `G(S)=1`, so `k_S = |RS_candidate|` is variable and is not made constant by `n=5, |S|=3, |R|=4`.

**Repair.**

- **`algorithm-specification.md` §28** — A3 complexity paragraph rewritten. The current-algorithm bound is `T_A3_current = T_select(S) + O(k_S)`. Under an `O(1)` selector this is `O(1) + O(k_S)`, **not simply `O(1)`**. The prevalidated-at-configuration option is relabelled **IMPLEMENTATION VARIANT / FUTURE OPTIMISATION**, distinct from the current algorithm.
- **[`complexity-analysis-batch4.csv`](complexity-analysis-batch4.csv)** — A3 selection / compliance / TOTAL rows rewritten. PIPELINE fixed cell rewritten. One additional row records the variant explicitly with `claim_status = IMPLEMENTATION VARIANT / FUTURE OPTIMISATION`.
- **[`complexity-traceability-batch4.csv`](complexity-traceability-batch4.csv)** — A3 rule-set selection and compliance rows rewritten. One additional row records the variant.
- **`manuscript.md` §8.1** — A3 row rewritten to `T_select(S) + O(k_S)`. A3 narrative bullet rewritten to distinguish the currently specified pseudocode from the future-optimisation variant.
- **End-to-end** (§30, `manuscript.md` §8.2) — already retains `T_select(S)`, `O(k_S)` and `T_engine(...)` explicitly and states *"T_episode is not O(1) merely because n=5, |S|=3, |R|=4"*. Preserved without change.

### Repair 2 — Authority-header status residue

**Defect (a).** `algorithm-specification.md` header status still read *"Batch 1 CLOSED … Batches 2 and 3 will populate the pseudocode and complexity analysis in a later revision."* — historical and inaccurate once Batches 2, 3 and 4 populated the file.

**Repair.** Concise refresh: *Batches 1–4 completed; Algorithms 1–4 specified; bounded complexity analysis integrated; workstream closure per the Batch 4 Final Complexity and Authority Residue Repair (2026-09-10).* The historical Batch 1 body (§§1–10) is preserved as originally written.

**Defect (b).** §10 leading sentence read *"seven bounded OPEN items"* while the table below listed OPEN-B1-1..8 (eight items — OPEN-B1-8 was added by the Batch 1 Transition Consistency Repair).

**Repair.** Count-only correction: *seven* → *eight*, with an inline note recording the correction and its cause. **No OPEN item's meaning or status changed.**

### Re-verify — 13 post-repair checks

Full detail at [`semantic-verification-batch4.json`](semantic-verification-batch4.json) `post_repair_checks`. Summary:

| Check | Verdict |
|---|---|
| `algorithm3_current_complexity_includes_kS` | **PASS** |
| `prevalidated_A3_variant_not_misreported_as_current_algorithm` | **PASS** |
| `end_to_end_engine_and_kS_terms_retained` | **PASS** |
| `full_pipeline_not_claimed_O1` | **PASS** |
| `authority_header_current` | **PASS** |
| `batch1_open_item_count_correct` | **PASS** |
| `solar_lookup_remains_parameterised` | **OPEN** (OPEN-B4-1, unchanged) |
| `rule_engine_strategy_remains_OPEN_B3_2` | **PASS** (unchanged) |
| `low_resource_claim_not_inferred_from_complexity` | **PASS** |
| `E5_not_run` | **PASS** |
| `F1_F3_not_reported` | **PASS** |
| `all_prior_OPEN_items_preserved` | **PASS** |
| `protected_canonical_state_unchanged` | **PASS** |

**Post-repair: 12 PASS / 0 FAIL / 1 OPEN** (matching the pre-existing OPEN-B4-1; no new OPEN item introduced).

### Scope preservation — nothing else moved

Not touched: `F_{D,τ}`, `ρ_{D,τ}`, `g_w`, `g_r`, `g_m`, `g_o`, `g_t`, `G(S)`, `A_AI(S)`, `RS(S)`, `AI(E)`, thresholds, recommendation types, rule-engine strategy (OPEN-B3-2), state/rule-set concurrency mechanism (OPEN-B1-8), OPEN-B4-1. All 16 protected canonical files remain byte-identical.

### Re-verification

```
python3 data/journal1-algorithm-specification/build.py
integrity:      PASS — 16 unchanged, 0 changed
parser batch1:  PASS — 4 CSVs checked
parser batch2:  PASS — 4 CSVs checked
parser batch3:  PASS — 7 CSVs checked
parser batch4:  PASS — 4 CSVs checked
```

### Post-repair closure condition

Met — the complexity table now distinguishes fixed environmental/governance constants (`n=5, |S|=3, |R|=4`) from variable rule-set size `k_S`, and the maintained authority header no longer carries stale workstream-status language.

### Post-repair verdict

```text
JOURNAL 1 ALGORITHM SPECIFICATION AND COMPLEXITY ANALYSIS CLOSED —
ALGORITHM 3 COMPLEXITY AND AUTHORITY RESIDUE REPAIRED
```

---

*Author: iskandar · Batch 4 report · 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
