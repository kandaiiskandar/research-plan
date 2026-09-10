# Journal 1 — Algorithm Specification

**Status:** Batch 1 CLOSED — this document is the single maintained authority for the operational contract that Algorithms 1–4 must preserve. Batches 2 and 3 will populate the pseudocode and complexity analysis in a later revision of this file.
**Batch 1 closed on:** 2026-09-10
**Branch:** `design/journal1-algorithm-specification`
**Task:** [`docs/tasks/Journal 1 Algorithm Specification batch 1.md`](../../../docs/tasks/Journal%201%20Algorithm%20Specification%20batch%201.md)
**Evidence directory:** [`data/journal1-algorithm-specification/`](../../../data/journal1-algorithm-specification/)

---

## 1. Purpose and scope

Batch 1 does one thing: it records the **operational contract** the four algorithms in Journal 1 §7–§8 must preserve. It answers *"what exactly must the algorithms preserve?"* — not *"how should the four algorithms be written?"*, which is Batch 2 and Batch 3.

The contract is not new science. Every construct here is defined in [`docs/canonical/appendix-c-formalisation.md`](../../../docs/canonical/appendix-c-formalisation.md) and restated in [`docs/canonical/architecture-illustration.md`](../../../docs/canonical/architecture-illustration.md), [`docs/canonical/justification-layer3-enforcement.md`](../../../docs/canonical/justification-layer3-enforcement.md), [`research-design.md`](research-design.md) and [`evaluation-specification.md`](evaluation-specification.md). This document is the *interface* through which Batches 2 and 3 read those sources; it does not modify them.

**What is out of scope for Batch 1:** Algorithms 1–4 themselves; Layer 3 implementation; complexity analysis; runtime benchmarking; runtime trace capture; canonical scripts; the submitted conference manuscripts. The 16 protected canonical files pinned in [`data/journal1-algorithm-specification/integrity-before.json`](../../../data/journal1-algorithm-specification/integrity-before.json) are byte-identical after Batch 1's edits — verified by [`build.py`](../../../data/journal1-algorithm-specification/build.py) (result: `integrity-after.json` → 16 unchanged, 0 changed).

---

## 2. Authority

The contract in this document reads from six authorities, in this order of precedence:

| Rank | Authority | Role |
|---|---|---|
| 1 | [`docs/canonical/appendix-c-formalisation.md`](../../../docs/canonical/appendix-c-formalisation.md) | Single source of truth for all formal definitions, theorems and semantic contracts. §C.8 is the canonical statement of the pipeline. |
| 2 | [`docs/canonical/architecture-illustration.md`](../../../docs/canonical/architecture-illustration.md) | Reader-facing restatement of the C.8 pipeline; governance table (§3), scope containment (§4), pipeline layers (§2), scenario walkthrough (§7). |
| 3 | [`docs/canonical/justification-layer3-enforcement.md`](../../../docs/canonical/justification-layer3-enforcement.md) | Layer 3 is a production rule system; Safety Dominance holds by construction from RS(S). |
| 4 | [`evaluation-specification.md`](evaluation-specification.md) | Canonical labels C0/C1/C2 (primary experiment) and C3 (structural comparator); Proposition J1-P1 for the C1 ≡ C3 admissible-set equivalence. |
| 5 | [`research-design.md`](research-design.md) | Closed claim structure (P1–P4 / F1–F3 / E1–E4, E6 / E5) that Journal 1 evaluates against — must not drift from during algorithm design. |
| 6 | [`docs/canonical/empirical-findings-2026-09-06.md`](../../../docs/canonical/empirical-findings-2026-09-06.md) §0a | Current canonical figures (5.81% / 4.48% Level 2 binding; 0.00% C1 ↔ C3 divergence; etc.) — read-only. |

Canonical scripts (`scripts/canonical_gt.py`, `scripts/canonical_figures.py`, `scripts/condition_comparison.py`, `scripts/historical_replay.py`, `scripts/hysteresis_analysis.py`, `scripts/diagnostic_binding.py`) may be inspected for semantic confirmation and are not modified.

Per-construct authority mapping — 27 entries linking each construct to its authoritative file and section — is at [`authority-map.csv`](../../../data/journal1-algorithm-specification/authority-map.csv).

---

## 3. Notation and interfaces

**Condition components.** `C = {w, r, m, o, t}` — the time-varying quantities the classifier reads (appendix-c C.2.0.1). Vessel category `v ∈ V = {small, medium, big}` is *not* a condition component; V is the **configuration domain** (appendix-c C.1 Vessel Category Classification Note; C.2.0.2 "v is not in this space").

**Value domains** (appendix-c C.2.0.1):

| Component | `Xᵢ` |
|---|---|
| `w` | ℝ≥0 (knots, sustained wind) |
| `r` | ℝ≥0 × K, `K = {0, 1}` (mm/hr rate paired with the thunderstorm indicator κ) |
| `m` | {none, advisory, warning, alert} |
| `o` | ℝ≥0 × ℝ≥0 (wave height m, swell period s) |
| `t` | [0, 24) (hour, 24-hour clock) |

**Observation space** (appendix-c C.2.0.2):

```
Obsᵢ = (Xᵢ × 𝕋) ∪ {⊥}
```

An observation pairs a value with the instant it was taken, or ⊥ for a runtime fault. ⊥ attaches to the quantity the classifier *reads*, not to the declared variable — g_o reads only the wave-height coordinate of o, so an absent swell period does not fault o. For r the rate is the required coordinate; the κ coordinate is derived through a total map χ that never returns ⊥.

**Resolved input** (appendix-c C.2.0.1):

```
Y = ∏_{i∈C} (Xᵢ ∪ {⊥})
```

**Interfaces the algorithms must implement.** The three-line type system every algorithm-level artefact preserves:

```
ρ_{D,τ} : ∏_{i∈C} Obsᵢ         → Y
f       : Y × V               → S                    where S = {SAFE, CAUTION, UNSAFE}
F_{D,τ} = f ∘ ρ_{D,τ} : ∏_{i∈C} Obsᵢ × V → S
```

`F_{D,τ}` is the **operational classifier — what a deployment executes**. `f(E)` is retained as ideal-form shorthand for the special case in which D = ∅ and every component holds a valid value; it is not interchangeable with `F_{D,τ}`. **Algorithm 1 must never be reduced to `S = f(E)`.** Full type table at [`operational-contract.csv`](../../../data/journal1-algorithm-specification/operational-contract.csv).

---

## 4. Operational observation-resolution contract

Every algorithm that consumes observations must resolve them through `ρ_{D,τ}` before invoking `f`.

**Four conditions, four responses** (appendix-c C.2.0):

| # | Condition | Decidable from the value alone? | Response | Resolved in |
|---|---|---|---|---|
| A | **Invalid** — outside the physically possible range | Yes | ⊥ → UNSAFE | Validation (C.2.0.3) |
| B | **Absent** — no reading available now | Yes | ⊥ → UNSAFE | Validation (C.2.0.3) |
| C | **Stale** — older than the permitted age `ageᵢ` | No — requires an observation timestamp | ⊥ → UNSAFE | Freshness (C.2.0.4) |
| D | **Unmeasured** — no data source exists in this deployment | No — a property of the deployment | **Declared exclusion**, pinned at SAFE | Configuration (C.2.0.5) |

**Exclusion set well-formedness** (appendix-c C.2.0.5):

- **(D1)** `t ∉ D`. Time of day is read from the device clock; no deployment can satisfy "no time source exists". A clock/date/solar-lookup failure is a *fault* (t = ⊥ → UNSAFE via Corollary C.1b.1), never an exclusion.
- **(D2)** `D ⊊ C`. At least one component must be observed.
- **(D3)** `D` is declared, and every severity figure produced under `D ≠ ∅` is reported as a lower bound.

**The retrospective replay declares `D = {m}`** — no marine warning archive exists for the study site. All severity figures in Journal 1 are therefore lower bounds. **Do not treat replay exclusion as live-deployment policy** — a deployment with a live MET broadcast has `D = ∅`, and `m` unavailable *at a moment* is then a condition B fault, not an exclusion. Live deployment configuration is bounded OPEN — see §10, OPEN-B1-5.

**Evaluation order — load-bearing** (appendix-c C.2.0.7):

```
0.  v configured?  and  D well-formed (t ∉ D)?   no → refuse to start
1.  for i ∈ D:        gᵢ ≜ SAFE                     ← exclusion first
2.  for i ∉ D:        yᵢ ← freshᵢ(valᵢ(obsᵢ), τ_now)   ← validation, then freshness
2a. for r:            κ ← χ(c), total into K; never ⊥
2b. for t:            resolve clock, date and canonical solar lookup;
                      any required one failing → y_t ← ⊥
3.  F ← f(y, v) = max-severity(g_w(y_w), g_r(y_r, κ), g_m(y_m), g_o(y_o, v), g_t(y_t, d))
```

**Exclusion-before-fault is mandatory.** An excluded component contributes SAFE, never ⊥. Confusing the two collapses the classifier — asserted literally to the replay, treating `m ∉ archive` as ⊥ would classify all 43,848 hours UNSAFE.

**Freshness parameter `τ`.** Left symbolic. Per appendix-c C.2.0.4, `ageᵢ` is a specified parameter per component with no proposed value: "wave height at hourly model resolution and a marine warning broadcast have different natural staleness budgets." Inventing an `ageᵢ` would repeat the 7.5 mm/hr rainfall defect corrected on 2026-09-08. Recorded as OPEN-B1-1.

Full operational interface list, invariants and preconditions at [`operational-contract.csv`](../../../data/journal1-algorithm-specification/operational-contract.csv).

---

## 5. Component-classifier contract

Every component classifier `gᵢ : Xᵢ ∪ {⊥} → S` with `gᵢ(⊥) = UNSAFE`. Component classifiers are not required to be surjective (appendix-c "Component classifiers are not required to be surjective"): the *codomain* is S; the *image* may be a proper subset.

**`g_w` — wind (knots, sustained)** — anchored to MET Malaysia:

| | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| `w` | `w ≤ 21.6` | `21.6 < w ≤ 27.0` | `w > 27.0` |

Boundaries preserved at source value: 40 km/h ÷ 1.852 = 21.598 kn (Cat 1 onset); 50 km/h ÷ 1.852 = 26.998 kn (Cat 2 onset). Do not reintroduce 22 kn — it was an undocumented rounding that suppressed two activations over five years.

**`g_r` — rainfall (mm/hr rate, κ storm indicator)** — two-input by canonical signature (appendix-c C.2 g_r row, retyped 2026-09-09; C.2.0.4a):

```
                ⎧ UNSAFE   if  κ = 1                          (storm route)
                ⎪ SAFE     if  κ = 0  ∧  0 ≤ r ≤ 10.0
    g_r(r, κ) = ⎨ CAUTION  if  κ = 0  ∧  10.0 < r ≤ 20.0
                ⎩ UNSAFE   if  κ = 0  ∧  r > 20.0
```

with κ derived from the raw provider weather code c through the **total map** χ:

```
χ(c) = 1   if c ∈ {95, 96, 99}
     = 0   otherwise, including c absent or unrecognised
```

Consequences that Algorithm 1 must preserve:

- **Missing rate → ⊥.** The rate is required. `y_r = ⊥` triggers `g_r(⊥) = UNSAFE` through Corollary C.1b.1 exactly like any scalar component.
- **Missing raw code → κ = 0.** χ is total into K and never returns ⊥. An absent or unrecognised code is *not* a fault; classification proceeds on the rate alone.
- **κ default is fail-*open* on the storm disjunct, not fail-safe.** Recorded explicitly in appendix-c C.2.0.4a. Because κ is escalation-only (Observation C.1c.1), defaulting to 0 is non-escalating, and every `g_r` figure travels as a lower bound where the code feed is absent or incomplete.
- **{95, 96, 99} is the complete set.** No further code is added. Do not redesign the mapping.

**`g_m` — marine warning level** (ordinal categorical): SAFE `{none}`; CAUTION `{advisory}`; UNSAFE `{warning, alert}`. Under `D = {m}` in the replay, `m` is pinned at SAFE — never ⊥.

**`g_o` — ocean state, vessel-conditional**. `g_o` reads the **wave-height coordinate only** (an absent swell period does not fault `o`). Vessel category `v` parameterises `g_o`; **there is no `g_v`** (appendix-c "Note: there is no g_v").

| `v` (GRT) | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| small (< 10) | `o < 1.0` m | `1.0 ≤ o ≤ 1.25` m | `o > 1.25` m |
| medium (10–25) | `o < 1.4` m | `1.4 ≤ o ≤ 2.8` m | `o > 2.8` m |
| big (> 25) | `o < 1.5` m | `1.5 ≤ o ≤ 3.5` m | `o > 3.5` m |

**`g_t` — time of day, solar-event classifier (SDR-001 applied 2026-09-08)**:

```
g_t : ([0, 24) × Date) ∪ {⊥} → {SAFE, UNSAFE}
      SAFE    sunrise(date) ≤ t < sunset(date)      (half-open: exact sunrise SAFE, exact sunset UNSAFE)
      UNSAFE  otherwise, and for t = ⊥
```

**`g_t` emits no CAUTION.** `Im(g_t) = {SAFE, UNSAFE}` deliberately; the architecture remains three-state via `g_o` and `g_r`. Runtime classification **consumes the frozen solar artefact** `data/solar/solar-events-daily.csv` through `scripts/canonical_gt.py`; **no script computes solar astronomy**. Do not reintroduce the fixed 06:00 / 17:00 / 19:00 window or the withdrawn 17:00–19:00 CAUTION band.

**Aggregation** (appendix-c C.2 Aggregation, Definition C.1):

```
f(y, v) = max-severity( g_w(y_w), g_r(y_r, κ), g_m(y_m), g_o(y_o, v), g_t(y_t, d) )
```

Five terms — `v` enters through `g_o` and is not an argument. Severity order `UNSAFE ≻ CAUTION ≻ SAFE` is a total strict order on {SAFE, CAUTION, UNSAFE}.

Operational implications the four algorithms must preserve:

- Any UNSAFE component → global UNSAFE.
- Otherwise any CAUTION → global CAUTION.
- Otherwise SAFE.

**UNSAFE is a governance state, not a claim about the physical world.** It does not assert legal prohibition or certain physical danger — a fail-safe on a missing observation yields UNSAFE while the sea may be flat. Route-of-arrival is annotation (§C.2.0.8 `reasons(q) ∈ 𝒫({fault, hazard, policy})`) that **never participates in governance**.

---

## 6. Failure and exclusion semantics

**Fault chain** (appendix-c C.2.0.3 – C.2.0.4, C.2.0.7, Corollary C.1b.1):

```
resolution failure (invalid, absent, or stale on a required non-excluded component)
  → yᵢ = ⊥
  → gᵢ(⊥) = UNSAFE
  → global S = UNSAFE via max-severity
```

The fail-safe is **Corollary C.1b.1**, not a separate pre-check: it follows from `gᵢ(⊥) = UNSAFE` together with the maximality of UNSAFE under ≻. Algorithm 1 must not introduce an emergency-shortcut branch outside this chain; a separate short-circuit would not be a bug, but it would need a separate proof that it is formally equivalent to the max-severity chain.

**Exclusion contract** (appendix-c C.2.0.5):

- Excluded components (`i ∈ D`) are pinned at SAFE — the least element of ≻. `gᵢ(·) ≜ SAFE` for all `i ∈ D`.
- The pin cannot raise the classification.
- The three obligations are indivisible: `D` is declared, the pin is at the least severe value, every severity figure produced under a non-empty `D` is a lower bound.

**Structural components differ from scalar components on `⊥` semantics.** ⊥ attaches to what the classifier reads:

- `g_o` reads only wave height → an absent swell period is not a fault.
- `g_r` reads (rate, κ) → an absent rate is a fault; an absent raw code is not.

`κ` cannot produce ⊥ because χ is total into K. Theorem C.1b's Note on the structured components makes this explicit: `y_r = ⊥` denotes failure of the rate coordinate only.

**Provenance reasons are annotation only** (appendix-c C.2.0.8). `reasons : Q → 𝒫({fault, hazard, policy})` is a specification contract; runtime capture is unimplemented (recorded as OPEN-B1-2). Reasons never alter resolution, max-severity, `G(S)`, `A_AI(S)`, `RS(S)`, rule selection or human authority. Theorem C.3 depends only on `S`, and its proof is identical for fault-driven, hazard-driven, policy-driven and mixed reason sets.

---

## 7. Governance mappings

`G : S → {0, 1}`:

```
G(SAFE)    = 1
G(CAUTION) = 1
G(UNSAFE)  = 0
```

`R = {Go, Delay, DepartureTime, Duration}` is fixed at design time. `A_AI : S → 2^R`:

```
A_AI(SAFE)    = {Go, Delay, DepartureTime, Duration}   = FULL
A_AI(CAUTION) = {Go, Delay}
A_AI(UNSAFE)  = ∅
```

Containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` follows from Theorem C.2 (Monotonicity of A_AI) and Corollary C.2 (Strict Monotonicity).

**Do not alter recommendation types or introduce subtypes.** The Go recommendation carries a **caution qualifier** under CAUTION (presentation and explanation are modified by the safety state), but the recommendation *type* is unchanged — `Go ∈ A_AI(CAUTION)` and `Go ∈ A_AI(SAFE)` are the same type in both.

`R` is fixed by [`architecture-illustration.md`](../../../docs/canonical/architecture-illustration.md) §4 and appendix-c C.4; extending it (e.g. fishing area, species) would require an argument from `A_AI(S)` for each state that preserves containment — an architectural extension, not an algorithmic decision.

**Governance constraints** (appendix-c C.6):

- **Participation:** `G(S) = 0 ⇒ A_AI(S) = ∅`.
- **Advisory restriction:** `S = CAUTION ⇒ A_AI(CAUTION) ⊊ A_AI(SAFE)`.

Both are proved (Theorem C.2 and Theorem C.3). Algorithms 2 and 3 must preserve both.

---

## 8. RS(S) pre-reasoning contract

Layer 3 is a **production rule system** (justification-layer3-enforcement.md §2a). The Safety Dominance Property `AI ⊆ A_AI(S)` holds **by construction** from the rule set `RS(S)` supplied *before* any reasoning begins (Theorem C.3 assumptions A1–A4).

**Rule set specification** (appendix-c C.7.1):

```
RS(SAFE)    rules produce recommendations in {Go, Delay, DepartureTime, Duration}
RS(CAUTION) rules produce recommendations in {Go, Delay}
RS(UNSAFE)  = ∅                        (never supplied — G(UNSAFE) = 0)
```

**Pre-reasoning contract for the algorithms:**

- **Preconditions.** (i) `S` has been classified through `F_{D,τ}`; (ii) `G(S)` and `A_AI(S)` have been read from `S`; (iii) if `G(S) = 1`, the active rule set `RS(S)` has been supplied to Layer 3 before any rule firing occurs.
- **Postconditions.** (i) `AI ⊆ A_AI(S)` by construction (no rule producing a disallowed type exists in the active `RS(S)`); (ii) no output filter is applied after generation — correctness is a property of the active rule set, not of a runtime check; (iii) if `G(S) = 0`, Layer 3 has received no input and produces nothing.
- **State/rule-set consistency (Algorithm 3 responsibility).** When `S` changes across decision episodes, the rule set used for the next reasoning episode must be `RS(S_new)`. A reasoning episode must not execute with a rule set inconsistent with the state governing that same episode. The **implementation mechanism** that enforces this consistency — for example atomic swap, immutable snapshot, locking, transactional update, or serialized execution — **is not yet specified** (OPEN-B1-8; §10). Fidelity criterion F3 (evaluation-specification.md §7) tests that no stale or inconsistent rule set is used across a state transition, and its scope is preserved by this bounded wording.
- **Engine fidelity (A4).** The rule engine fires only rules present in the active `RS(S)`; no rule produces a type not present in its conclusion.

**Implementation is not designed in Batch 1.** Concrete rule lists in `RS(SAFE)` and `RS(CAUTION)`, inference-engine wiring, and the Layer 2 → Layer 3 supply mechanism are Batch 2 / Batch 3 territory. Recorded as OPEN-B1-4.

---

## 9. Human-decision boundary

**Human Decision is unconditional in all three states** (appendix-c C.8.2 step 6; architecture-illustration.md §3). The architecture constrains AI advisory scope, not the human decision. The operator may act contrary to any recommendation, including under UNSAFE.

Algorithm-level consequences:

- No algorithm introduces automated approval, prohibition or "override" semantics.
- No system message instructs the operator. State notices under UNSAFE report the state, the fact that AI advisory is unavailable, the triggering reason where available, and the operator's retained authority (architecture-illustration.md §3 "Why the wording is state-reporting rather than an instruction").
- Fault-driven UNSAFE, hazard-driven UNSAFE and policy-driven UNSAFE receive the same governance response (`G(S) = 0`, `A_AI(S) = ∅`), and none of them constrains human authority.

---

## 10. Open implementation decisions

Batch 1 closes carrying seven **bounded** OPEN items, each scoped so it does not create a contradiction elsewhere. Full audit at [`open-decisions.csv`](../../../data/journal1-algorithm-specification/open-decisions.csv).

| ID | Item | Reason it is open | Blocks |
|---|---|---|---|
| OPEN-B1-1 | Per-component freshness parameters `ageᵢ` | `τ` is symbolic in the specification; no per-component value is proposed (appendix-c C.2.0.4). | Freshness-driven ⊥ in a live deployment. Does not block replay evaluation (`m` excluded; other components are hourly and effectively fresh for hourly ticks). |
| OPEN-B1-2 | Runtime provenance trace capture | C.2.0.8 defines the `reasons` annotation contract but records runtime capture as unimplemented. | Reason-set surfacing at Layer 4. Does not affect S or governance. |
| OPEN-B1-3 | Medium-vessel `g_o` CAUTION→UNSAFE boundary (2.8 m) | Medium row is interpolated; no direct medium-vessel operability data. | Medium-vessel bindings inherit the flag; small-vessel figures unaffected. |
| OPEN-B1-4 | Layer 3 prototype build (`RS(SAFE)` and `RS(CAUTION)` concrete rule lists) | Batch 1 records only the pre-reasoning contract. | Fidelity criteria F1–F3 remain deferred until the prototype exists. |
| OPEN-B1-5 | `g_m` operational configuration in a live deployment | Retrospective replay declares `D = {m}`. A live deployment's `D` is a deployment-time decision (C.2.0.5). | Live deployment only; retrospective replay unaffected. |
| OPEN-B1-6 | Latency acceptance threshold `H3 = X ms` | No externally justified acceptance criterion exists (evaluation-specification.md §11). | RQ-J2 pass/fail closure only; descriptive measurement unaffected. |
| OPEN-B1-7 | Decision-support utility construct | No operational definition on replay alone (evaluation-specification.md §9). | Utility metric only; other metrics unaffected. |
| OPEN-B1-8 | State/rule-set consistency enforcement mechanism | The architecture requires state/rule-set consistency (§8) but does not prescribe the concurrency/atomicity mechanism used to achieve it — atomic swap, immutable snapshot, locking, transactional update, and serialized execution are all admissible. | Does not block algorithm specification, provided Algorithms 3–4 express the consistency requirement as a precondition/postcondition rather than prescribing an implementation primitive. |

No numerical threshold, utility formula, `ageᵢ` value or human-outcome value is fabricated to close any of these items.

---

## Guiding rule

> "*What exactly must the algorithms preserve?*" — Batch 1 answers this and only this.
> "*How should all four algorithms be written?*" — Batch 2 and Batch 3.

---

*Author: iskandar · Batch 1 closed: 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
