# Journal 1 — Algorithm Specification

**Status:** Batches 1–4 completed (workstream closure per the Batch 4 Final Complexity and Authority Residue Repair, 2026-09-10) — Algorithms 1–4 specified, bounded complexity analysis integrated. This document is the single maintained authority for the operational contract that Algorithms 1–4 preserve, their four-algorithm pseudocode, and the accompanying complexity bounds. The historical Batch 1 body (§§1–10) is retained as originally written and describes the pre-reasoning contract that Batches 2–4 later populated with pseudocode (Algorithms 1–2 in §§11–16, Algorithms 3–4 in §§17–24) and complexity (§§25–33).
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

Batch 1 closes carrying eight **bounded** OPEN items, each scoped so it does not create a contradiction elsewhere. Full audit at [`open-decisions.csv`](../../../data/journal1-algorithm-specification/open-decisions.csv). *(Count corrected 2026-09-10 by the Batch 4 Final Complexity and Authority Residue Repair. OPEN-B1-8 was added by the Batch 1 Transition Consistency Repair; this leading sentence had not been updated to match.)*

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

## 11. Algorithm 1 — Operational Safety Classification

Algorithm 1 realises `S = F_{D,τ}(obs, v) = f(ρ_{D,τ}(obs), v)`. It is the operational classifier — not the ideal shorthand `S = f(E)`. The 10-step ordering below is fixed and load-bearing (appendix-c C.2.0.7).

```text
Algorithm 1 — Operational Safety Classification  (F_{D,τ})
──────────────────────────────────────────────────────────
Input:
  obs      = (obs_i)_{i∈C}          ; observation tuple, obs_i ∈ Obs_i = (X_i × 𝕋) ∪ {⊥}
  v        ∈ V ∪ {⊥_cfg}            ; vessel configuration; ⊥_cfg denotes unconfigured
  D        ⊆ C                      ; declared exclusion set, expressed against C = {w, r, m, o, t}
                                    ; well-formedness at lines 5–8: (D1) t ∉ D, (D2) D ⊊ C
                                    ; the maximal well-formed D is {w, r, m, o} (appendix-c C.2.0.5)
  τ_now    ∈ 𝕋                      ; current instant, for freshness
  age      = (age_i)_{i∈C∖D}        ; per-component permitted staleness  (symbolic; OPEN-B1-1)
  date     ∈ Date                   ; valid date accompanying obs_t
  solar    : Date → (sunrise,       ; canonical frozen solar-event lookup
                    sunset)          ; data/solar/solar-events-daily.csv (scripts/canonical_gt.py)

Output:
  S ∈ {SAFE, CAUTION, UNSAFE}       ; or a startup refusal (no S returned)

Procedure:
  ▸ Startup precondition — v  (C.2.0.6)
  1: if v ∉ V then
  2:     refuse startup
  3:     return  "STARTUP_CONFIGURATION_ERROR: v unconfigured or invalid"
  4: end if

  ▸ Well-formedness of D  (C.2.0.5, D1–D2)
      D is declared against the full condition set C = {w, r, m, o, t}, not
      against a narrower universe. Combined with (D1), the constraint (D2)
      D ⊊ C follows automatically from t ∈ C ∖ D — no additional check is
      required. The maximal well-formed exclusion set is D = {w, r, m, o},
      under which g_t alone drives S (appendix-c C.2.0.5, "Why this lemma
      matters more than it looks").
  5: if t ∈ D  or  D ⊄ C then                    ; (D1) t ∉ D
  6:     refuse startup                            ; (D2) D ⊊ C follows since t ∈ C ∖ D
  7:     return  "STARTUP_CONFIGURATION_ERROR: D ill-formed"
  8: end if

  ▸ Declared exclusions — pinned SAFE before fault evaluation  (C.2.0.5, C.2.0.7 step 1)
  9: for each i ∈ D do
 10:     s_i ← SAFE
 11: end for

  ▸ Required non-excluded observation resolution — validation and freshness  (C.2.0.3–4)
      (r and t receive per-component treatment below.)
 12: for each i ∈ (C ∖ D) ∩ {w, m, o} do
 13:     y_i ← fresh_i( val_i(obs_i), τ_now, age_i )     ; ⊥ if invalid, absent, or stale
 14: end for

  ▸ Rainfall — two-input classifier  (C.2.0.4a, C.2.0.2)
 15: if r ∉ D then
 16:     (rate_obs, c_obs) ← obs_r                       ; rate = required coordinate; c = derived
 17:     y_rate ← fresh_r( val_r(rate_obs), τ_now, age_r )
 18:     κ      ← χ(c_obs)                               ; χ total into K = {0, 1}; χ(absent) = 0
 19:     if y_rate = ⊥ then
 20:         y_r ← ⊥                                     ; fail-safe on the required coordinate
 21:     else
 22:         y_r ← (y_rate, κ)
 23:     end if
 24: end if

  ▸ Time — clock, date and canonical solar dependency  (C.2.0.7 step 2b, t ∉ D by D1)
 25: if valid_clock(obs_t) ∧ valid_date(date) ∧ available(solar(date)) then
 26:     y_t                 ← time_of(obs_t)
 27:     (sunrise_d, sunset_d) ← solar(date)              ; consumed from frozen artefact,
 28:                                                      ; not recomputed inside this algorithm
 29: else
 30:     y_t ← ⊥                                          ; clock/date/solar fault
 31: end if

  ▸ Component classifiers — exactly five contributions  (C.2 Aggregation)
 32: if w ∉ D then  s_w ← g_w(y_w)                    end if
 33: if r ∉ D then  s_r ← g_r(y_r)                    end if    ; g_r reads (y_rate, κ) when y_r ≠ ⊥
 34: if m ∉ D then  s_m ← g_m(y_m)                    end if
 35: if o ∉ D then  s_o ← g_o(y_o, v)                 end if    ; v conditions g_o only; there is no g_v
 36:                s_t ← g_t(y_t, date)                          ; always evaluated (t ∉ D)

  ▸ Aggregation under total strict order  UNSAFE ≻ CAUTION ≻ SAFE  (Def C.1, C.2)
 37: S ← max-severity( s_w, s_r, s_m, s_o, s_t )

 38: return S
```

**No emergency shortcut.** The fail-safe `gᵢ(⊥) = UNSAFE → S = UNSAFE` is delivered by lines 32–36 composed with line 37; it is Corollary C.1b.1, not a separate pre-check.

**No astronomy in Algorithm 1.** Lines 27–28 read the frozen solar artefact; no algorithm in this specification computes sunrise or sunset.

**No `g_v`.** Line 35 is the only occurrence of `v`; there is no independent vessel classifier.

---

## 12. Algorithm 1 — Preconditions and Postconditions

**Preconditions.**

- **P1.** `obs` is total over `C` — one observation per component, each element of `Obsᵢ = (Xᵢ × 𝕋) ∪ {⊥}`.
- **P2.** `date` is valid and `solar(date)` is available from the canonical frozen artefact.
- **P3.** For every `i ∈ C ∖ D`, `ageᵢ` is specified (values symbolic in this specification; OPEN-B1-1).
- **P4.** `D` is well-formed against the full condition set `C = {w, r, m, o, t}`: **(D1)** `t ∉ D` and **(D2)** `D ⊊ C` (appendix-c C.2.0.5). Given (D1) and `D ⊆ C`, (D2) follows automatically from `t ∈ C ∖ D`; the enforcement at lines 5–8 tests `t ∈ D` and `D ⊄ C` and refuses startup on either. Ill-formed `D` refuses startup — it is not classified UNSAFE. **`D = {w, r, m, o}` is well-formed** (the maximal exclusion set named in appendix-c C.2.0.5); under it, `w, r, m, o` contribute SAFE by pin and `S = g_t(y_t, date)`.

**Postconditions.**

- **Q1.** If `v ∈ V` and `D` is well-formed, exactly one `S ∈ {SAFE, CAUTION, UNSAFE}` is returned (operational totality — Theorem C.1b).
- **Q2.** If `v ∉ V`, startup is refused and no `S` is returned. This is not a runtime observation fault (C.2.0.6).
- **Q3.** If any required non-excluded observation fails validation or freshness, its component classification is UNSAFE via `gᵢ(⊥) = UNSAFE` and Corollary C.1b.1. Rainfall is UNSAFE whenever `y_rate = ⊥`, irrespective of `c_obs`.
- **Q4.** `S = max-severity(s_w, s_r, s_m, s_o, s_t)` under `UNSAFE ≻ CAUTION ≻ SAFE`. Any UNSAFE component gives global UNSAFE; otherwise any CAUTION gives global CAUTION; otherwise SAFE.
- **Q5.** Excluded components (`i ∈ D`) contribute `sᵢ = SAFE`, never `⊥`. `S` computed under `D ≠ ∅` is reported as a lower bound (obligation D3).

**Failure behaviour — two disjoint modes:**

- **Startup / configuration failure** (Q2, and D ill-formed at lines 5–8) — refuses to start; **no `S` is returned**. Handled outside the classification pipeline.
- **Runtime observation fault** on a required non-excluded component (Q3) — the algorithm returns a valid `S`, and that `S` is UNSAFE by Corollary C.1b.1.

Distinguishing these two is required by C.2.0.5–6 and preserved by the ordering at lines 1–8.

---

## 13. Algorithm 2 — Governance Configuration

Algorithm 2 realises the finite mapping `S → (G(S), A_AI(S))`. It performs no reasoning, no rule selection and no advisory generation. RS(S) supply is Algorithm 3 (Batch 3).

```text
Algorithm 2 — Governance Configuration
──────────────────────────────────────
Input:
  S ∈ {SAFE, CAUTION, UNSAFE}       ; must be a valid output of Algorithm 1 / F_{D,τ}

Output:
  (G(S), A_AI(S))  with
    G(S)    ∈ {0, 1}                ; participation gate value
    A_AI(S) ⊆ R = {Go, Delay, DepartureTime, Duration}

Procedure:
  1: switch S
  2:     case SAFE:
  3:         G     ← 1
  4:         A_AI  ← {Go, Delay, DepartureTime, Duration}
  5:     case CAUTION:
  6:         G     ← 1
  7:         A_AI  ← {Go, Delay}
  8:     case UNSAFE:
  9:         G     ← 0
 10:         A_AI  ← ∅
 11: end switch
 12: return (G, A_AI)
```

**Handoff, not implementation.** The tuple `(G(S), A_AI(S))` is the input Algorithm 3 (Batch 3) requires to supply `RS(S)` before Layer 3 reasoning begins (algorithm-specification.md §8; appendix-c C.7.1; Theorem C.3 A2). Algorithm 2 does not select rules and does not generate recommendations. The concurrency/atomicity primitive that enforces state/rule-set consistency (§8) is not chosen here — **OPEN-B1-8 remains OPEN**.

---

## 14. Algorithm 2 — Preconditions and Postconditions

**Preconditions.**

- **P1.** `S` is a valid output of Algorithm 1 — `S ∈ {SAFE, CAUTION, UNSAFE}` by Theorem C.1b operational totality.

**Postconditions.**

- **Q1.** Exactly one pair `(G, A_AI)` is returned for every valid `S`.
- **Q2.** `G(S)` matches the mapping in appendix-c C.3 exactly: `G(SAFE) = G(CAUTION) = 1`, `G(UNSAFE) = 0`.
- **Q3.** `A_AI(S)` matches the mapping in appendix-c C.4 exactly: `A_AI(SAFE) = FULL`, `A_AI(CAUTION) = {Go, Delay}`, `A_AI(UNSAFE) = ∅`.
- **Q4. Participation constraint.** `G(S) = 0 ⇒ A_AI(S) = ∅` (case UNSAFE; appendix-c C.6).
- **Q5. Advisory restriction.** `A_AI(CAUTION) ⊊ A_AI(SAFE)` (cases CAUTION and SAFE; appendix-c C.6).
- **Q6. Containment.** `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`.

**Bounded correctness language.** Algorithm 2 *implements* the finite mapping on which Theorem C.2 (Monotonicity) is established. It does **not** experimentally validate Theorem C.2 — Theorem C.2 is proved (appendix-c C.6); Algorithm 2 realises the mapping the proof quantifies over. Similarly, Algorithm 2 does not "prove" the participation and advisory-restriction constraints; those are proved by Theorem C.3 (Safety Dominance) and by direct inspection of the mapping in C.4. See §16.

---

## 15. Batch 2 Boundary Verification

Twenty-five specification-level checks — twenty on Algorithm 1's component and semantic contract (B1–B20), one on the maximal exclusion set (B25, added by the Exclusion-Set Domain Repair), and four on Algorithm 2's exhaustive input space (B21–B24). **These are specification checks, not empirical experiments**; each is a direct arithmetic or set-inclusion comparison against the maintained mappings.

Full per-case table with expected verdicts, authority sections and PASS/FAIL results at [`boundary-cases-batch2.csv`](../../../data/journal1-algorithm-specification/boundary-cases-batch2.csv).

**Algorithm 1 — component boundary checks (12):**

| # | Case | Component | Expected |
|---|---|---|---|
| B1 | `w = 21.6` | `g_w` | SAFE (`≤ 21.6`) |
| B2 | `w = 27.0` | `g_w` | CAUTION (`≤ 27.0`) |
| B3 | `w > 27.0` (e.g. 27.1) | `g_w` | UNSAFE |
| B4 | `r = 10`, `κ = 0` | `g_r` | SAFE (`≤ 10.0`) |
| B5 | `r = 20`, `κ = 0` | `g_r` | CAUTION (`≤ 20.0`) |
| B6 | `κ = 1` (any `r`) | `g_r` | UNSAFE (storm route) |
| B7 | small, `o = 1.0` | `g_o` | CAUTION (`1.0 ≤ o`) |
| B8 | small, `o = 1.25` | `g_o` | CAUTION (`o ≤ 1.25`) |
| B9 | medium, `o = 1.4` | `g_o` | CAUTION |
| B10 | medium, `o = 2.8` | `g_o` | CAUTION |
| B11 | big, `o = 1.5` | `g_o` | CAUTION |
| B12 | big, `o = 3.5` | `g_o` | CAUTION |

**Algorithm 1 — solar and semantic checks (8):**

| # | Case | Expected |
|---|---|---|
| B13 | `t = sunrise(date)` exactly | `g_t = SAFE` (half-open) |
| B14 | `t = sunset(date)` exactly | `g_t = UNSAFE` (half-open) |
| B15 | nighttime (`t < sunrise` or `t ≥ sunset`) | `g_t = UNSAFE` |
| B16 | missing rainfall rate (`y_rate = ⊥`) | rainfall component UNSAFE (`y_r = ⊥ → g_r(⊥) = UNSAFE`) |
| B17 | missing raw weather code + valid rate | `κ = 0`, classify from rate alone (not `⊥`) |
| B18 | `m ∈ D` (excluded) | `s_m = SAFE` (pin) |
| B19 | `m ∉ D`, `obs_m` missing/invalid | `s_m = UNSAFE` via `g_m(⊥)` |
| B20 | `v` missing/invalid | startup refusal (no `S` returned) |

**Algorithm 2 — exhaustive verification (4):**

| # | Case | Expected |
|---|---|---|
| B21 | `S = SAFE` | `(G, A_AI) = (1, {Go, Delay, DepartureTime, Duration})` |
| B22 | `S = CAUTION` | `(G, A_AI) = (1, {Go, Delay})` |
| B23 | `S = UNSAFE` | `(G, A_AI) = (0, ∅)` |
| B24 | Containment | `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` (set inclusion) |

**Algorithm 1 — maximal exclusion set (1, added by Exclusion-Set Domain Repair):**

| # | Case | Expected |
|---|---|---|
| B25 | `D = {w, r, m, o}` (t ∉ D; D ⊊ C) | well-formed startup; `s_w = s_r = s_m = s_o = SAFE` by pin; `t` remains required and is classified normally; `S = g_t(y_t, date)` |

**All 25 boundary cases resolve PASS by inspection against the maintained thresholds and mappings.** No statistical test is required or appropriate — these are deterministic set/arithmetic checks against the specification.

---

## 16. Batch 2 Correctness Traceability

Every claim carried by Algorithms 1 and 2 is placed in exactly one of four categories.

- **Definition** — a canonical definition in appendix-c; the algorithm cannot itself prove it.
- **Algorithm implementation of a definition** — the algorithm realises a definition faithfully; correctness is *implementation of a mapping*, not proof.
- **Formal theorem or property** — proved elsewhere (appendix-c C.1b, C.2, C.3, C.6); Batch 2 does not re-prove it.
- **Future implementation-fidelity test** — deferred to Layer 3 build (F1–F3 in evaluation-specification.md §7).

Full per-construct table at [`algorithm-traceability-batch2.csv`](../../../data/journal1-algorithm-specification/algorithm-traceability-batch2.csv). Summary:

| Construct | Definition | Algorithm impl. | Formal property | Future fidelity |
|---|---|---|---|---|
| Operational classifier `F_{D,τ}` | C.2.0.1, C.8.1 | A1 lines 1–38 | Theorem C.1b (Operational Totality) | F1 (replay conformance) |
| Fail-safe `gᵢ(⊥) = UNSAFE` | C.2 (per-component) | A1 lines 19–23, 29–30 delivered to lines 32–36 | Corollary C.1b.1 | F1 |
| Startup precondition (v) | C.2.0.6 | A1 lines 1–3 | not a theorem — an axiomatic precondition | startup-refusal check outside F1 |
| Exclusion-before-fault | C.2.0.5, C.2.0.7 | A1 lines 9–11 | Lemma C.1c (Monotone Degradation) | F1 under `D ≠ ∅` |
| Rainfall two-input | C.2.0.4a, C.2 g_r row | A1 lines 15–24 | Theorem C.1(i) g_r case | F1 |
| Solar half-open boundary | C.2 g_t row | A1 line 36 (via canonical `g_t`) | Theorem C.1(i) g_t case | F1 |
| Frozen solar dependency | C.2 g_t canonical implementation | A1 lines 27–28 | implementation invariant; not a theorem | deployment fidelity |
| Max-severity aggregation (5 terms) | C.2 Aggregation, Def C.1 | A1 line 37 | Theorem C.1(ii) | F1 |
| `G(S)` mapping | C.3 | A2 lines 3, 6, 9 | Participation constraint (C.6) | F1 |
| `A_AI(S)` mapping | C.4 | A2 lines 4, 7, 10 | Advisory restriction (C.6); Theorem C.2 (Monotonicity); Corollary C.2 | F1, F2 |
| RS(S) handoff | C.7.1, Theorem C.3 A2 | A2 §13 note (handoff only) | Theorem C.3 (Safety Dominance) | Batch 3; F3 |
| Human authority | C.8.2 step 6 | neither A1 nor A2 modifies it | unconditional | not applicable to Batch 2 |

**Bounded language reminders (§19 of the task).**

- Do not write "Algorithm 1 proves safety." Algorithm 1 *implements* `F_{D,τ}` whose totality is established by Theorem C.1b and whose fail-safe behaviour is Corollary C.1b.1. The proof is in appendix-c, not in Algorithm 1.
- Do not write "Algorithm 2 validates monotonicity experimentally." Algorithm 2 *implements* the finite mapping on which Theorem C.2 is established. Monotonicity is proved in C.6; Algorithm 2 realises the mapping the proof quantifies over.

---

## 17. Algorithm 3 — Rule-Set Supply

Algorithm 3 supplies the rule set `RS(S)` that Layer 3 is permitted to use for the current decision episode. It runs **before any Layer 3 rule firing begins** and it generates no advisory itself. Concrete Layer 3 rules remain OPEN-B1-4; this section defines the *shape and admissibility contract* only.

```text
Algorithm 3 — Rule-Set Supply
─────────────────────────────
Input:
  S            ∈ {SAFE, CAUTION, UNSAFE}                  ; from Algorithm 1 (F_{D,τ})
  G(S)         ∈ {0, 1}                                   ; from Algorithm 2
  A_AI(S)      ⊆ R = {Go, Delay, DepartureTime, Duration} ; from Algorithm 2
  repository   ; the configured rule repository — a set of production rules
               ; each rule ρ has a conclusion type  type(ρ) ∈ R
  candidate    ; the deployment-defined selector  candidate : repository × 𝒮 → 2^repository
               ; returning the rules the deployment designates as active under state S

Output:
  RS(S) — the rule set supplied to Layer 3 for the current episode, satisfying
           ConclusionTypes(RS(S)) ⊆ A_AI(S) and RS(UNSAFE) = ∅
  OR a bounded CONFIGURATION_FIDELITY_FAILURE — in which case no reasoning begins

Procedure:
  ▸ Gate-off short-circuit (participation)  (appendix-c C.3, C.6)
  1: if G(S) = 0 then
  2:     RS ← ∅                                            ; G(S)=0 ⇒ A_AI(S)=∅ ⇒ RS(S)=∅
  3:     return RS
  4: end if

  ▸ Compliance check on the candidate rule set (no silent filtering)
  5: RS_candidate ← candidate(repository, S)
  6: if ∃ ρ ∈ RS_candidate : type(ρ) ∉ A_AI(S) then
  7:     refuse supply
  8:     return "CONFIGURATION_FIDELITY_FAILURE:
                ConclusionTypes(candidate(repository, S)) ⊄ A_AI(S)"
              ; do not silently filter disallowed rules; do not modify S;
              ; do not invent a new safety state; runtime handling: OPEN-B3-1
  9: end if

  ▸ Supply RS(S) BEFORE Layer 3 begins reasoning for this episode
 10: RS ← RS_candidate
 11: return RS                                             ; ConclusionTypes(RS) ⊆ A_AI(S) by lines 5–9
                                                          ; consistent with the S governing this episode
```

**State/rule-set consistency across episodes.** When `S` changes between episodes (`S_old → S_new`), Algorithm 3 is re-invoked on the new state and the `RS(S_new)` it returns is what the next reasoning episode uses. The reasoning engine must not reuse `RS(S_old)` when it is inconsistent with `S_new` (§8 of this specification, and appendix-c C.7.1). **The mechanism enforcing this consistency at runtime is not prescribed here** — atomic swap, immutable snapshot, locking, transactional update, serialized execution and equivalents are all admissible; the choice is bounded OPEN-B1-8 (unchanged from Batch 1). Algorithm 3 specifies the invariant, not the concurrency primitive.

**No advisory generation in Algorithm 3.** Line 2 and line 11 return only a rule set (or `∅`); no rule firing occurs and no `AI(E)` element is produced.

---

## 18. Algorithm 3 — Preconditions and Postconditions

**Preconditions.**

- **P1.** `S ∈ {SAFE, CAUTION, UNSAFE}` — a valid output of Algorithm 1 (Theorem C.1b operational totality).
- **P2.** `(G(S), A_AI(S))` is the corresponding Algorithm 2 output (Q2 and Q3 of §14).
- **P3.** The rule repository is configured — the deployment supplies a rule set with a well-defined `candidate` selector and, for each rule `ρ`, a conclusion type `type(ρ) ∈ R`.
- **P4.** Reasoning has not yet begun for this decision episode. Algorithm 3 runs strictly before Layer 3 rule firing.

**Postconditions.**

- **Q1.** `ConclusionTypes(RS(S)) ⊆ A_AI(S)` — the conclusion-type inclusion required by appendix-c C.7.1 and Theorem C.3 A2. Enforced by lines 5–9 (no silent filtering) and delivered by line 10.
- **Q2.** `G(S) = 0 ⇒ RS(S) = ∅`. Enforced by lines 1–3.
- **Q3.** `RS(UNSAFE) = ∅`. Follows from Q2 since `G(UNSAFE) = 0`.
- **Q4.** No `AI(E)` element is produced — Algorithm 3 emits only a rule set (or a bounded configuration/fidelity failure).
- **Q5.** If the candidate rule set violates the conclusion-type constraint, Algorithm 3 refuses supply. The failure is treated as configuration/fidelity: **`S` is not modified**, **no new safety state is invented**, and the failure is not remapped to environmental UNSAFE. Runtime handling beyond refusal of supply is bounded OPEN — see OPEN-B3-1 in §24.

**No post-hoc filter substituted for governance.** Q1 is preserved by *choosing* the rules Layer 3 is permitted to fire, not by discarding non-compliant outputs after generation. See §16 of the Batch 3 task and appendix-c C.7 (enforcement mechanism).

---

## 19. Algorithm 4 — Governed Advisory Generation

Algorithm 4 consumes the governance configuration produced by Algorithms 1–3 and invokes Layer 3 only when participation is permitted. The recommendation-space guarantee `AI(E) ⊆ A_AI(S)` holds **by construction**, from Algorithm 3's postcondition combined with the rule-engine fidelity assumption — not by a runtime filter on outputs.

```text
Algorithm 4 — Governed Advisory Generation
──────────────────────────────────────────
Input:
  E            ; resolved decision context (appendix-c C.1 / C.8.2). This is the same E
               ; that fed Algorithm 1; do not silently redefine it.
  S            ∈ {SAFE, CAUTION, UNSAFE}                  ; from Algorithm 1
  G(S)         ∈ {0, 1}                                   ; from Algorithm 2
  A_AI(S)      ⊆ R                                        ; from Algorithm 2
  RS(S)        ; from Algorithm 3 — the rule set for this episode
               ; ConclusionTypes(RS(S)) ⊆ A_AI(S) by A3 Q1
  engine       ; production rule symbolic reasoner satisfying the fidelity assumption
               ; (Theorem C.3 A4): fires only rules present in the active RS(S);
               ; no active rule produces a conclusion type outside RS(S)

Output:
  AI(E) ⊆ A_AI(S)                                          ; holds by construction

Procedure:
  ▸ Gate-off path: participation withdrawn (S = UNSAFE ⇒ G(S) = 0)
  1: if G(S) = 0 then
  2:     AI ← ∅                                            ; no rule firing; no advisory
  3:     return AI                                         ; state-reporting UI, if any, is outside AI(E)
  4: end if

  ▸ Participating path (G(S) = 1): reason using only RS(S)
  5: AI ← engine.reason(E, RS)                            ; engine has RS(S) in scope and no other rule sets
  6: return AI                                             ; AI ⊆ A_AI(S) by A3 Q1 + engine fidelity (Theorem C.3 A4)
```

**No post-hoc filter substitution.** The required chain is:

```text
A_AI(S)  →  ConclusionTypes(RS(S)) ⊆ A_AI(S)  →  engine fires only rules in RS(S)  →  AI(E) ⊆ A_AI(S)
```

Line 6 does **not** re-filter `AI` against `A_AI(S)` at runtime. Correctness is delivered by rule-set restriction (Algorithm 3), not by output inspection. A defensive assertion could exist in a future implementation, but it is not authoritative and does not appear here.

**Rule-engine evaluation strategy is unspecified.** Forward chaining, backward chaining, RETE, agenda priority, first-match, all-match, conflict resolution, rule salience — none of these are fixed by Algorithm 4. The governance contract is engine-agnostic; the strategy is bounded OPEN — see OPEN-B3-2 in §24.

**No `Do Not Go` / `Cancel Trip` / `Return Home` under UNSAFE.** Those would themselves be AI outputs and are not members of `A_AI(UNSAFE) = ∅`. State-reporting UI ("UNSAFE — AI advisory unavailable. Triggered by: …") is not an `AI(E)` element and belongs outside this algorithm.

---

## 20. Algorithm 4 — Preconditions and Postconditions

**Preconditions.**

- **P1.** `S ∈ {SAFE, CAUTION, UNSAFE}` (Theorem C.1b).
- **P2.** `(G(S), A_AI(S))` produced by Algorithm 2.
- **P3.** `RS(S)` produced by Algorithm 3, satisfying `ConclusionTypes(RS(S)) ⊆ A_AI(S)` and `RS(UNSAFE) = ∅` (A3 Q1–Q3).
- **P4. Engine fidelity (Theorem C.3 A4).** The rule engine fires only rules present in the active `RS(S)`, and no active rule produces a conclusion type outside its own conclusion. **This is an implementation assumption**, not a fact Algorithm 4 re-proves.
- **P5. Consistency with `S`.** The `RS(S)` supplied to the engine is `RS(S_current)`, not a stale `RS(S_prior)` from a preceding episode (state/rule-set consistency invariant; OPEN-B1-8).

**Postconditions.**

- **Q1.** `AI(E) ⊆ A_AI(S)` — Safety Dominance (Theorem C.3). Holds by construction from P3 + P4; Algorithm 4 does not re-prove it.
- **Q2.** `G(S) = 0 ⇒ AI(E) = ∅` — participation withdrawn. Delivered by lines 1–3; corresponds to Case 1 of Theorem C.3.
- **Q3.** No advisory type outside `A_AI(S)` appears in `AI(E)` — by P3 and P4, not by a post-hoc filter.
- **Q4. Human authority unconditional.** `AI(E) = ∅` does **not** forbid human action; `Go ∈ AI(E)` does **not** automatically approve departure. Algorithm 4 introduces no automated approval, prohibition, override or enforcement semantics (appendix-c C.8.2 step 6).

**Bounded correctness language.** Algorithm 4 *implements* the enforcement contract on which Theorem C.3 depends (assumptions A1–A4 in appendix-c C.7.2). It **does not** independently prove Safety Dominance — the theorem exists and covers the deployed classifier `F_{D,τ}` and the ideal `f(E)`.

---

## 21. Batch 3 State and Transition Verification

Seven state-space specification checks (three for Algorithm 3, three for Algorithm 4, one for an invalid rule repository) and six transition specification checks. Full detail at [`state-cases-batch3.csv`](../../../data/journal1-algorithm-specification/state-cases-batch3.csv) and [`transition-cases-batch3.csv`](../../../data/journal1-algorithm-specification/transition-cases-batch3.csv). **All resolve PASS by inspection against the maintained mappings and the pseudocode above.** These are specification checks, not F3 fidelity results.

**Algorithm 3 by state (SC1–SC3):**

| # | State | Expected `RS(S)` |
|---|---|---|
| SC1 | `S = SAFE` | rules with conclusion types in `{Go, Delay, DepartureTime, Duration}` |
| SC2 | `S = CAUTION` | rules with conclusion types in `{Go, Delay}` |
| SC3 | `S = UNSAFE` | `RS = ∅` (short-circuit at A3 lines 1–3) |

**Algorithm 4 by state (SC4–SC6):**

| # | State | Expected `AI(E)` |
|---|---|---|
| SC4 | `S = SAFE`, compliant `RS(SAFE)` | `AI ⊆ {Go, Delay, DepartureTime, Duration}` — engine reasons using only `RS(SAFE)` |
| SC5 | `S = CAUTION`, compliant `RS(CAUTION)` | `AI ⊆ {Go, Delay}` — engine reasons using only `RS(CAUTION)` |
| SC6 | `S = UNSAFE` | `AI = ∅` — gate-off at A4 lines 1–3; **no rule firing** |

**Invalid rule repository (SC7):**

| # | Case | Expected |
|---|---|---|
| SC7 | some `ρ ∈ candidate(repository, S)` has `type(ρ) ∉ A_AI(S)` | Algorithm 3 refuses supply (`CONFIGURATION_FIDELITY_FAILURE`); `RS(S)` is not passed to Layer 3; `S` is not modified; no new safety state introduced; runtime handling beyond refusal is bounded OPEN-B3-1 |

**Transition checks (TC1–TC6).** For each transition `S_old → S_new`, the next decision episode must use the governance configuration and `RS(S_new)` corresponding to the new state; the algorithm chain (A1 → A2 → A3 → A4) is re-invoked on the new state.

| # | `S_old → S_new` | Expected on the next episode |
|---|---|---|
| TC1 | SAFE → CAUTION | `A_AI` shrinks to `{Go, Delay}`; `RS(CAUTION)` supplied; `DepartureTime` and `Duration` conclusion types no longer available |
| TC2 | CAUTION → SAFE | `A_AI` expands to `{Go, Delay, DepartureTime, Duration}`; `RS(SAFE)` supplied; timing and duration types available again |
| TC3 | CAUTION → UNSAFE | `G = 0`; `A_AI = ∅`; `RS = ∅`; `AI(E) = ∅`; Layer 3 not invoked |
| TC4 | UNSAFE → CAUTION | `G = 1`; `A_AI = {Go, Delay}`; `RS(CAUTION)` supplied; Layer 3 re-enabled with restricted scope |
| TC5 | SAFE → UNSAFE | `G = 0`; `A_AI = ∅`; `RS = ∅`; `AI(E) = ∅`; Layer 3 not invoked |
| TC6 | UNSAFE → SAFE | `G = 1`; `A_AI = {Go, Delay, DepartureTime, Duration}`; `RS(SAFE)` supplied; full scope |

Each transition case verifies **the specification invariant that state/rule-set consistency is preserved by re-invocation of A3 on `S_new`**. **Do not read this as F3 PASS** — F3 is a future implementation-fidelity test on a built Layer 3 (evaluation-specification.md §7). Batch 3 supplies no runtime fidelity evidence.

---

## 22. Safety-Dominance Dependency Trace

The runtime guarantee `AI(E) ⊆ A_AI(S)` (Theorem C.3, Safety Dominance) is delivered by a four-link chain. Each link has a distinct status, and the chain must not be collapsed into "Algorithm 4 proves safety". Full table at [`safety-dominance-trace-batch3.csv`](../../../data/journal1-algorithm-specification/safety-dominance-trace-batch3.csv).

```
┌────────────────────────────────────────────────────────────┐
│  A_AI(S)                                                   │  Link L1 — definition
│    │                                                        │
│    ▼                                                        │
│  ConclusionTypes(RS(S)) ⊆ A_AI(S)                          │  Link L2 — algorithmic contract (A3 Q1)
│    │                                                        │
│    ▼                                                        │
│  engine fires only rules present in active RS(S)            │  Link L3 — engine-fidelity assumption
│  and produces no output beyond fired-rule conclusion types  │             (Theorem C.3 A4; A4 P4)
│    │                                                        │
│    ▼                                                        │
│  AI(E) ⊆ A_AI(S)                                            │  Link L4 — formal theorem (Theorem C.3)
└────────────────────────────────────────────────────────────┘
```

**Classification of each link:**

| Link | Statement | Category |
|---|---|---|
| L1 | `A_AI : S → 2^R` — the admissible recommendation space per state | **Definition** (appendix-c C.4) |
| L2 | `ConclusionTypes(RS(S)) ⊆ A_AI(S)` | **Algorithmic enforcement contract** — Algorithm 3 postcondition Q1, enforced by A3 lines 5–9 (no silent filtering) |
| L3 | Engine fires only rules in active `RS(S)`; no rule produces a type outside its own conclusion | **Implementation assumption** — Theorem C.3 assumption A4; Algorithm 4 precondition P4. A **future implementation-fidelity obligation** (F1, F2) validates it, but Batch 3 does not test it |
| L4 | `AI(E) ⊆ A_AI(S)` | **Formal theorem** — Theorem C.3 (Safety Dominance), proved in appendix-c C.7.2 |

**Consequence.** Batch 3 does **not** re-prove Safety Dominance. It makes L2 an explicit algorithmic contract (Algorithm 3) and L3 an explicit engine-fidelity assumption (Algorithm 4 P4), so that Theorem C.3's antecedents (A1–A4) are visibly discharged by the algorithm pipeline. If a future Layer 3 implementation violates L3, Theorem C.3 ceases to hold operationally — the fidelity criteria F1–F3 in [`evaluation-specification.md`](evaluation-specification.md) §7 test for exactly that failure mode.

---

## 23. Batch 3 Correctness Traceability

Every construct carried by Algorithms 3 and 4 is placed in exactly one category. Full table at [`algorithm-traceability-batch3.csv`](../../../data/journal1-algorithm-specification/algorithm-traceability-batch3.csv).

| Construct | Definition | Algorithmic implementation | Formal theorem / property | Implementation assumption | Future fidelity test | OPEN implementation decision |
|---|---|---|---|---|---|---|
| `G(S)` mapping | appendix-c C.3 | consumed by A3 lines 1–4 and A4 lines 1–4 | Participation constraint (C.6) | — | F1 | — |
| `A_AI(S)` mapping | appendix-c C.4 | consumed by A3 lines 5–9 | Advisory restriction; Corollary C.2; Theorem C.2 | — | F1 | — |
| `RS(S)` shape and admissibility | appendix-c C.7.1 | A3 lines 5–10 | Theorem C.3 A2 | — | F1 | OPEN-B1-4 (concrete rule contents) |
| `ConclusionTypes(RS(S)) ⊆ A_AI(S)` | — | **A3 Q1** — enforced at lines 5–9 | Theorem C.3 A2 | — | F1 | — |
| Pre-reasoning supply | appendix-c C.7.1 | A3 line 10 runs before A4 line 5 | Theorem C.3 A2 | — | F1, F3 | — |
| State/rule-set consistency across episodes | algorithm-specification.md §8 | A3 re-invoked on `S_new`; A4 P5 | invariant | consistency enforcement | F3 | **OPEN-B1-8** (concurrency primitive) |
| Engine-fidelity assumption (A4) | — | A4 line 5 uses only `RS(S)`; A4 P4 states the assumption | Theorem C.3 A4 | **assumption** — Batch 3 does not test it | F1, F2 | — |
| `AI(E) ⊆ A_AI(S)` | — | delivered by A3 Q1 + engine fidelity | **Theorem C.3** (proved) | — | F1 | — |
| `AI(E) = ∅` under UNSAFE | appendix-c C.6 | A4 lines 1–3 (gate-off) | Theorem C.3 case 1 | — | F1 | — |
| Human authority unconditional | appendix-c C.8.2 step 6 | neither A3 nor A4 alters it; A4 Q4 records it | unconditional | — | not applicable | — |
| Concrete Layer 3 rules | — | — | — | — | — | **OPEN-B1-4** |
| Rule-engine evaluation strategy | — | — | — | — | — | **OPEN-B3-2** |
| Invalid RS runtime handling | — | A3 refuses supply (lines 6–8); runtime handling beyond refusal is not fixed | — | — | — | **OPEN-B3-1** |
| Decision-episode implementation boundary | — | — | — | — | — | **OPEN-B3-3** |

**Bounded language reminder.** No sentence in Batch 3 writes "Algorithm 4 proves safety" or "the transition checks demonstrate F3." Correctness statements everywhere use *contract-derived* / *by construction* / *enforcement assumption* / *future fidelity obligation*.

---

## 24. Batch 3 Open Implementation Decisions

Three new bounded OPEN items originate in Batch 3. Full audit at [`open-decisions-batch3.csv`](../../../data/journal1-algorithm-specification/open-decisions-batch3.csv).

| ID | Item | Reason it is open | Blocks |
|---|---|---|---|
| OPEN-B3-1 | Invalid rule-repository runtime handling | Algorithm 3 refuses supply on `ConclusionTypes(candidate) ⊄ A_AI(S)` (A3 lines 6–8), but no canonical authority prescribes the runtime response beyond refusal — for example, whether the deployment logs and continues without Layer 3, halts, alerts the operator, or requires a config reload. | Fault-response wiring only. Governance contract is unaffected — the invalid `RS(S)` is not supplied to reasoning either way. |
| OPEN-B3-2 | Rule-engine evaluation strategy | Forward chaining, backward chaining, RETE, agenda priority, first-match, all-match, conflict resolution, rule salience — no canonical authority fixes one. Algorithm 4's governance contract is engine-agnostic. | Complexity analysis (deferred to a later batch); does not block Batches 1–3. |
| OPEN-B3-3 | Decision-episode implementation boundary | The specification is clear that *one governing `S` → one governance configuration → one `RS(S)`* per reasoning episode; the exact episode duration, polling interval, refresh frequency, thread model, concurrency model and transaction boundary are not authoritative. | Runtime implementation and OPEN-B1-8 mechanism selection; specification-level checks in §21 hold regardless. |

**Batch 1 OPEN items (OPEN-B1-1..8) preserved unchanged.** In particular OPEN-B1-8 remains OPEN — Algorithm 3's state/rule-set consistency invariant is specification-level; no concurrency primitive is chosen.

**Also preserved:** OPEN-B1-4 (concrete Layer 3 rules) — Algorithm 3 defines the *shape and admissibility contract* for `RS(S)`, not its contents.

---

## 25. Complexity Analysis — Notation and Scope

Batch 4 derives **bounded asymptotic complexity** for Algorithms 1–4. It distinguishes:

- **Fixed current architecture** — the specification with `n = 5`, `|S| = 3`, `|R| = 4` as literal constants.
- **Generalized architecture** — the same algorithms parameterised by `n`, `|S|`, `|R|`, `k_S`, so that adding a component or a state is a specification-level change with a stated cost.
- **Concrete implementation performance** — wall-clock latency, memory footprint, CPU and energy on target hardware.

**Batch 4 addresses only the first two.** Asymptotic complexity is not runtime performance. The pattern *"algorithm is O(1), therefore suitable for low-resource environments"* is **not admissible**; deployment-level performance claims require E5 evidence (OPEN-B1-6). Complexity analysis is not E5 evidence.

**Notation.**

| Symbol | Meaning |
|---|---|
| `n` | number of condition components in `C` (fixed value: 5) |
| `\|S\|` | number of governance states (fixed value: 3) |
| `\|R\|` | number of recommendation types (fixed value: 4) |
| `k_S` | number of rules in the active `RS(S)` |
| `k` | size of the configured rule repository |
| `q` | number of rule evaluations / firings the engine performs in one episode |
| `c` | cost of one rule-condition evaluation |
| `T_solar_lookup` | cost of one solar-event lookup for a given date (unspecified representation — OPEN-B4-1) |
| `T_select(S)` | cost of `candidate(repository, S)` selection (representation-dependent — see §28) |
| `T_engine(k_S, q, c)` | rule-engine cost per episode (strategy unspecified — OPEN-B3-2) |
| `M_engine` | rule-engine working memory (parameterised) |
| `N` | number of records in a retrospective replay (used **only** in the replay-vs-per-decision distinction of §30) |

No new variable is introduced unless a bound cannot be expressed without it.

---

## 26. Algorithm 1 Complexity

**Per-decision time.** The seven stages of Algorithm 1 (§11 lines 1–37) contribute:

| Stage | Fixed-model cost | Generalized cost |
|---|---|---|
| Startup validation (lines 1–3) | `O(1)` | `O(1)` |
| `D` well-formedness (lines 5–8) | `O(1)` | `O(\|D\|) ≤ O(n)` |
| Exclusion pin (lines 9–11) | `O(1)` | `O(\|D\|) ≤ O(n)` |
| Validation + freshness on `{w, m, o}` (lines 12–14) | `O(1)` | `O(n − \|D\|) ≤ O(n)` |
| Rainfall two-input (lines 15–24) | `O(1)` | `O(1)` |
| κ derivation via χ (line 18) | `O(1)` | `O(1)` (membership test in `{95, 96, 99}`) |
| Solar/clock/date resolution (lines 25–31) | `T_solar_lookup` | `T_solar_lookup` |
| Component classifiers (lines 32–36) | `O(1)` (five classifiers, each threshold comparison) | `O(n)` |
| Max-severity aggregation (line 37) | `O(1)` (constant tuple of size 5) | `O(n)` |

**Fixed-model total.** `T_A1_fixed = O(1) + T_solar_lookup`.

**Generalized total.** `T_A1 = O(n) + T_solar_lookup`.

**`T_solar_lookup` is left symbolic.** The specification requires that runtime consumes the frozen artefact `data/solar/solar-events-daily.csv` via `scripts/canonical_gt.py` — it does **not** fix the data structure. A pre-loaded dictionary keyed by date supports `O(1)` average lookup; a sequential CSV scan is `O(d)` in the number of dates; a sorted-array binary search is `O(log d)`. **Do not collapse `T_solar_lookup` to `O(1)` in this specification** — that is a deployment choice recorded as OPEN-B4-1.

**Fail-safe cost.** `gᵢ(⊥) = UNSAFE` (Corollary C.1b.1) does not add a stage — it is the value of `gᵢ` at ⊥ and is delivered inside the per-component classifier evaluation.

---

## 27. Algorithm 2 Complexity

**Per-decision time.** A single switch over `S` (§13 lines 1–11) returns `(G(S), A_AI(S))` in constant time:

- **Fixed-model:** `T_A2_fixed = O(1)`.
- **Generalized (lookup):** `O(1)` for hash / direct addressing on `S`; `O(\|S\|)` for a linear scan over the state list. The specification does not fix the lookup mechanism.

**Static mapping storage — separated from lookup.** If `A_AI` is materialised as a `S → 2^R` table, its storage is `O(\|S\| · \|R\|)`. In the fixed architecture this is `3 × 4 = 12` set-membership bits (or twelve boolean entries), i.e. a constant. **Storage cost is a configuration property, not a per-decision cost** — the switch does not scan `\|R\|` on every decision.

**Space (working memory).** `O(1)` — a pair `(G, A_AI)` where `A_AI ⊆ R`.

---

## 28. Algorithm 3 Complexity

Algorithm 3 (§17) has two conceptually distinct costs, and the specification does not force one implementation over the other. Both are recorded.

**Selection cost `T_select(S)`.**

- If the deployment holds a *prevalidated state-indexed rule set* (RS(S) precomputed at configuration time), `T_select(S) = O(1)` — a reference is looked up.
- If Algorithm 3 selects candidates from a general repository at supply time, `T_select(S)` depends on the selector — for example, `O(k)` in a linear scan over the repository.

**Compliance-check / materialisation cost.** Lines 5–9 test `ConclusionTypes(RS_candidate) ⊆ A_AI(S)`. This scans the candidate set at cost `O(k_S)`.

- If compliance is prevalidated at configuration time, this per-supply cost can be avoided — but only under that implementation choice, which is not required by the specification.

**Complexity of the currently specified Algorithm 3 pseudocode.** Lines 5–9 always run when `G(S) = 1` and perform a candidate-set compliance scan of size `k_S = |RS_candidate|`:

```
T_A3_current = T_select(S) + O(k_S)
```

Under an `O(1)` selector this reduces to `O(1) + O(k_S)` — **not simply `O(1)`**. The fixed architecture constants `n = 5`, `|S| = 3`, `|R| = 4` do **not** make `k_S` constant; `k_S` is variable and set by the deployment's rule repository. *(Corrected 2026-09-10 by the Batch 4 Final Complexity and Authority Residue Repair.)*

Selection cost `T_select(S)` remains parameterised:

- **State-indexed selector** (repository holds precomputed candidate sets keyed by `S`): `T_select(S) = O(1)`.
- **Repository scan**: `T_select(S) = O(k)`.

**Implementation variant / future optimisation — not the current algorithm.** A deployment that **prevalidates** the conclusion-type constraint at configuration time and holds a state-indexed rule set as an immutable reference could remove lines 5–9 from runtime execution, reducing `T_A3` to `T_select(S)` alone. **That is a different implementation realisation** of the algorithm; it is not a bound on the currently specified pseudocode, and it must remain labelled as an *implementation variant* / *future optimisation* in every table and traceability row.

**Space.**

- **Reference-only:** `O(1)` — `RS` is a pointer into repository.
- **Materialised copy:** `O(k_S)` — `RS_candidate` is a new set constructed for this episode.

**Do not silently close OPEN-B3-1 (invalid RS runtime handling) or OPEN-B1-8 (state/rule-set consistency mechanism) by fixing an implementation choice here.** Both remain OPEN; the complexity table records the choice as a dependency, not as a design decision.

---

## 29. Algorithm 4 Complexity

The governance wrapper (§19 lines 1–5) has:

- **Gate-off short-circuit:** `O(1)`.
- **Participating-path dispatch to the engine:** `O(1)` overhead.

Total wrapper cost: `T_A4_wrapper = O(1)`. Total Algorithm 4 cost:

**`T_A4 = O(1) + T_engine(k_S, q, c)`.**

**The rule-engine term `T_engine(k_S, q, c)` is parameterised and remains unspecified.** OPEN-B3-2 (rule-engine evaluation strategy) blocks selection of forward chaining, backward chaining, RETE, agenda priority, first-match, all-match, conflict resolution or rule salience. **Do not collapse `T_engine` to a specific expression in this specification.**

**Illustrative example (not canonical).** A naïve linear scan of the active `RS(S)` in a forward-chaining loop would give `O(k_S · c)`. **This is an example only; it is not the architecture's official complexity.** Traceability rows label such examples as `ILLUSTRATIVE ONLY`, never as `DERIVED`.

**Space.** `M_A4 = O(1) + M_engine(...)`. Do not invent agenda size, RETE network size or caching behaviour.

---

## 30. End-to-End Decision-Episode Complexity

A single decision episode invokes A1 → A2 → A3 → A4. The end-to-end time is the sum of the per-algorithm bounds:

```
T_episode = T_A1 + T_A2 + T_A3 + T_A4
          = [O(n) + T_solar_lookup]
          + O(1)
          + [T_select(S) + O(k_S)]
          + [O(1) + T_engine(k_S, q, c)]
          = O(n) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)
```

**Fixed architecture (n = 5, |S| = 3, |R| = 4):**

```
T_episode_fixed = O(1) + T_solar_lookup + T_select(S) + O(k_S) + T_engine(k_S, q, c)
```

**The rule-engine term is retained.** `T_episode` is **not** `O(1)` merely because `n = 5`, `|S| = 3`, `|R| = 4`. Layer 3 reasoning cost dominates any classification/governance constant.

**Replay complexity is separate from per-decision complexity.** For a retrospective replay of `N` records:

```
T_replay(N) = O(N · T_episode)
```

For a classification-and-governance-only replay (no engine invocation, applicable when Layer 3 is not yet built):

```
T_replay_no_engine(N) = O(N · (n + T_solar_lookup))
```

**The historical replay over 43,848 records is not `O(1)`.** Do not mix `N` into any per-decision bound. Do not treat the raw dataset load as Algorithm 1's memory complexity.

---

## 31. Space Complexity

Separate **static configuration storage** from **per-decision working memory**.

| Store | Cost | Notes |
|---|---|---|
| Threshold constants (per component) | `O(n)` | Loaded once |
| `G(S)` table | `O(\|S\|)` | Loaded once |
| `A_AI(S)` mapping | `O(\|S\| · \|R\|)` | Loaded once |
| Rule repository | `O(k)` | Loaded once (deployment configuration) |
| Frozen solar artefact | `O(d)` where `d` = configured date range | Loaded once |
| A1 working memory | `O(1)` fixed / `O(n)` generalized | Resolved observation vector + component states |
| A2 working memory | `O(1)` | Returned pair |
| A3 working memory | `O(1)` reference **or** `O(k_S)` materialised | Representation-dependent (§28) |
| A4 working memory | `O(1) + M_engine` | Engine memory parameterised |

**Do not count** raw external datasets, the historical replay dataset or per-episode logging as per-decision working memory.

---

## 32. Complexity Claim Boundaries

The complexity results in §§26–31 support these bounded statements:

- The classifier and governance mappings operate over small fixed state spaces.
- The per-decision architecture avoids model-size growth in the number of replay records `N`; replay over `N` records requires `N` decision evaluations.
- The rule-engine cost is retained as a parameter and is not collapsed to a fixed complexity.

They do **not** support any of the following without independent E5 evidence:

- The architecture is lightweight.
- The architecture is efficient on low-end phones.
- The architecture is deployable in low-resource settings.
- The latency is negligible.
- Memory use is minimal.
- Energy use is low.

**Complexity is not evidence for any of the six forbidden claims above.** OPEN-B1-6 (latency threshold `H3 = X ms`) remains OPEN; E5 remains the empirical performance workstream.

**F1–F3 are separate.** Complexity analysis does not test whether a built Layer 3 prototype honours L3 (engine fidelity). F1–F3 in `evaluation-specification.md` §7 remain future implementation-fidelity evidence.

**New bounded OPEN item introduced by Batch 4:**

| ID | Item | Reason it is open |
|---|---|---|
| **OPEN-B4-1** | Solar-lookup data structure and its cost `T_solar_lookup` | The specification requires runtime to consume the frozen artefact `data/solar/solar-events-daily.csv` via `scripts/canonical_gt.py` but does not fix the data structure. Dict-by-date gives `O(1)` average; binary search gives `O(log d)`; linear scan gives `O(d)`. The choice is a deployment decision recorded as a bounded OPEN. |

All prior OPEN items (OPEN-B1-1..8, OPEN-B3-1..3) are preserved unchanged.

---

## 33. Manuscript Integration Trace

The active Journal 1 manuscript is [`submissions/v1-initial-submission/manuscript.md`](submissions/v1-initial-submission/manuscript.md) (path name is a working-draft label, not evidence of submission). Batch 4 integrates the four algorithms and their bounded complexity into publication-ready form. `algorithm-specification.md` remains the detailed internal authority; the manuscript carries only what is needed for reviewer understanding.

Per-section trace at [`manuscript-integration-batch4.csv`](../../../data/journal1-algorithm-specification/manuscript-integration-batch4.csv). Summary:

| Manuscript section | Change | Scientific effect |
|---|---|---|
| §7 Algorithms | Replaced placeholder with publication-ready pseudocode summaries for Algorithms 1–4 using canonical names and notation | Adds pseudocode; no scientific state change; formal notation preserved (`F_{D,τ}`, `ρ_{D,τ}`, `RS(S)`, `AI(E)`) |
| §8 Complexity Analysis | Replaced placeholder with fixed-model and generalized complexity table plus bounded narrative | Adds bounded complexity claims; no low-resource deployability claim inferred from asymptotics |
| §9 Prototype Implementation | One-line repair of the low-resource bullet: "lightweight" removed and replaced with "per-decision working memory bounded (see §8)" | Repairs an unsupported claim without altering §9's status as an unbuilt prototype description |

**No unrelated manuscript edits.** All algorithm names, formal notation, `g_v` absence, rainfall two-input signature, `g_t` no-CAUTION property, exact `G(S)` / `A_AI(S)`, RS(S) pre-reasoning contract, no post-hoc filter substitution, bounded Safety Dominance wording, unconditional human authority, and F1–F3 / E5 boundaries are audited in [`manuscript-integration-batch4.csv`](../../../data/journal1-algorithm-specification/manuscript-integration-batch4.csv).

---

## Guiding rule

> "*What exactly must the algorithms preserve?*" — Batch 1 answers this and only this.
> "*How should all four algorithms be written?*" — Batch 2 (Algorithms 1 & 2) and Batch 3 (Algorithms 3 & 4).
> "*What are their bounded complexity properties, and how do they enter the manuscript?*" — Batch 4.

> **Batch 3 guiding principle.** Make the governance enforcement contract precise enough that the next implementation agent has no freedom to silently change the scientific architecture. Batch 3 defines *what implementation fidelity must satisfy*; it supplies no fidelity evidence.

> **Batch 4 guiding principle.** *formal definition ≠ algorithm specification ≠ asymptotic complexity ≠ implementation ≠ implementation-fidelity evidence ≠ performance evidence ≠ human/outcome validation.* Batch 4 closes only the first three layers.

---

*Author: iskandar · Batch 1 closed: 2026-09-10 · Batch 2 closed: 2026-09-10 · Batch 3 closed: 2026-09-10 · Batch 4 closed: 2026-09-10 · Branch: `design/journal1-algorithm-specification`*
