---
layout: document
---

# Architecture Illustration: Graduated Safety-State-Gated Hybrid AI Decision Architecture

This document illustrates the proposed two-level governance architecture through diagrams, tables, and a worked scenario. All formal definitions are canonical in [`appendix-c-formalisation.md`](appendix-c-formalisation.md).

---

## 1. Governance Pipeline

The architecture works in four steps. Each step asks one question, and the answer flows upward to the next step.

```
+=====================================================================+
|  STEP 4: FISHER DECIDES                                             |
|                                                                     |
|  "I can see the conditions, I can see what the system says.         |
|   I decide whether to go."                                          |
|                                                                     |
|  The fisher always has the final word.                               |
+=====================================================================+
        ^
        | Safety state display + AI advice (if any)
        |
+=====================================================================+
|  STEP 3: WHAT CAN THE AI SAY?                                       |
|                                                                     |
|  The safety state controls what types of advice AI is allowed       |
|  to give:                                                           |
|                                                                     |
|  SAFE     --> Full advice: Go/No-go, Delay, Departure time,        |
|               Trip duration                                         |
|  CAUTION  --> Limited advice: Go/No-go and Delay only               |
|               (no timing, no duration — too unreliable)             |
|  UNSAFE   --> AI is silent: no advice at all                        |
|                                                                     |
|  AI cannot override these limits. It can only work within           |
|  the space the safety state allows.                                 |
+=====================================================================+
        ^
        | Safety state: SAFE, CAUTION, or UNSAFE
        |
+=====================================================================+
|  STEP 2: IS IT SAFE?                                                 |
|                                                                     |
|  Each reading is compared against safety thresholds.                |
|  The system asks: what is the single worst reading?                 |
|                                                                     |
|  - If ANY reading is UNSAFE   --> overall state = UNSAFE            |
|  - If ANY reading is CAUTION  --> overall state = CAUTION           |
|  - Only if ALL readings are SAFE --> overall state = SAFE           |
|                                                                     |
|  One dangerous condition is enough. Good conditions on other        |
|  parameters cannot compensate.                                      |
+=====================================================================+
        ^
        | Six environmental readings
        |
+=====================================================================+
|  STEP 1: READ THE ENVIRONMENT                                        |
|                                                                     |
|  The system reads six measurements:                                 |
|                                                                     |
|    Wind speed    Rainfall     Marine warnings                       |
|    Wave height   Vessel category   Time of day                      |
|                                                                     |
|  All readings come from physical sensors or known facts —           |
|  none come from the AI itself.                                      |
+=====================================================================+
```

**Formal notation:** E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision

---

## 2. Architectural Layers

The pipeline separates into four functionally distinct layers. Each layer has a different computational character, a different assurance basis, and a different failure mode.

```
+=====================================================================+
|  Layer 4: HUMAN DECISION                                            |
|  Fisher receives recommendations + safety state display             |
|  Makes final go/no-go decision with full authority                  |
+=====================================================================+
        ^
        | Filtered recommendations + safety state indicator
        |
+=====================================================================+
|  Layer 3: AI ADVISORY REASONING                                     |
|  Probabilistic / learned component                                  |
|  Generates recommendations R ∈ AI(E)                                |
|  Constraint: AI(E) ⊆ A_AI(S)                                       |
+=====================================================================+
        ^
        | Governance configuration: G(S) and A_AI(S)
        |
+=====================================================================+
|  Layer 2: DETERMINISTIC GOVERNANCE                                  |
|  Rule-based, formally verifiable, non-AI                            |
|  Computes: S = f(E)                                                 |
|  Outputs:  G(S) — participation gate (0 or 1)                       |
|            A_AI(S) — admissible recommendation space                |
|  Properties: O(1) time, no GPU, threshold comparisons only          |
+=====================================================================+
        ^
        | Raw environmental measurements
        |
+=====================================================================+
|  Layer 1: ENVIRONMENT / SENSOR                                      |
|  Physical sensors, weather APIs, maritime authority broadcasts       |
|  Produces: E = {w, r, m, o, v, t}                                   |
|  All sources independent of the AI system                           |
+=====================================================================+
```

**Why layering matters:**
- Layer 2 is deterministic and independent of Layer 3 — governance functions even if AI is degraded or unavailable
- Layer 2 can be verified using conventional software engineering methods (static analysis, exhaustive testing of a finite classification function)
- Layer 3 requires probabilistic and empirical assurance methods
- The causal flow is unidirectional (Environment -> Governance -> AI) with no feedback from AI to governance — AI cannot influence its own governance

---

## 3. Three Safety States: Governance Configuration

Each safety state defines a distinct governance configuration — a specific combination of participation gate value and admissible recommendation space.

| | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| **Safety state** | S = SAFE | S = CAUTION | S = UNSAFE |
| **Participation gate G(S)** | 1 (AI enabled) | 1 (AI enabled) | 0 (AI disabled) |
| **Admissible recommendations A_AI(S)** | {Go, Delay, DepartureTime, Duration} | {Go, Delay} | {} |
| **Advisory scope** | Full | Restricted | None |
| **What AI provides** | Go/no-go, delay guidance, departure window, trip duration | Go/no-go with caution qualifier, delay guidance | Nothing — AI is silent |
| **What AI cannot provide** | (No restriction) | Departure timing, trip duration | Any recommendation |
| **Human role** | Reviews full advisory set; decides | Reviews restricted advisory set; decides | Decides alone using own judgement |
| **Governance level active** | Level 1 + Level 2 | Level 1 + Level 2 | Level 1 only |

**The CAUTION mode is the architectural contribution.** At Level 1 (participation gate), CAUTION and SAFE are identical — G(S) = 1 in both. The distinction exists entirely at Level 2 (advisory scope): A_AI(CAUTION) is a proper subset of A_AI(SAFE). This is why binary governance architectures cannot express CAUTION — they have no Level 2.

**Why the fisher always decides.** The human operator retains final decision authority in all three states — including SAFE, where full AI advice is available. The AI is advisory in every state; it never acts autonomously. This is a deliberate design choice grounded in the deployment context: Gao (2024) documents that fishers make departure decisions based on personal experience (importance 4.71/5 — the highest-rated factor), integrating environmental conditions with tacit knowledge about local waters, vessel capabilities, and economic needs that the AI cannot fully capture. The architecture supports this existing decision structure rather than replacing it. Wen et al. (2025), analysing 60 real-world accident reports, find that human intervention was ineffective in 83.3% of process control incidents — but this was in contexts where AI acted autonomously and the human was asked to override. In the proposed architecture, the relationship is reversed: the AI advises, the human acts. The governance layer constrains the AI, not the human.

**What happens under UNSAFE.** When G(S) = 0 and A_AI(S) = {}, the AI is silent — it generates no recommendations. However, the governance layer (Layer 2) may still display a deterministic safety alert (e.g., "Dangerous conditions — return to shore"). This alert is not an AI recommendation — it is a pre-defined system message triggered directly by the safety state classification, with no AI reasoning involved. It is functionally equivalent to a weather warning broadcast: a deterministic, rule-based message that does not depend on the AI advisory layer. The formal model's guarantee A_AI(UNSAFE) = {} is preserved because the alert originates from the governance layer, not from AI(E).

---

## 4. Advisory Scope Containment

The admissible recommendation spaces form a strict containment hierarchy. As environmental risk increases, the set of recommendation types the AI may generate shrinks monotonically until it reaches the empty set.

As conditions get worse, the AI is allowed to say fewer things:

```
                        Go/     Delay    Departure   Trip
                        No-go   guidance   time      duration
                        ─────   ────────  ─────────  ────────
  SAFE (all clear)       Yes      Yes       Yes        Yes
                                                            
  CAUTION (elevated)     Yes      Yes        No         No
                                                            
  UNSAFE (dangerous)      No       No        No         No
```

**Reading this table:** Each row is a safety state. Each column is a type of advice the AI could give. "Yes" means the AI is allowed to give that type of advice. "No" means the AI is architecturally prevented from giving it — not filtered after the fact, but never generated at all.

**The pattern:** Every "Yes" in CAUTION is also a "Yes" in SAFE. Every "Yes" in UNSAFE (there are none) is also a "Yes" in CAUTION. As conditions worsen, advice types are only ever *removed*, never *added*. This is the containment property — what the AI can say under worse conditions is always a subset of what it can say under better conditions.

**What each recommendation type means:**

| Type | Description | Available in |
|---|---|---|
| **Go** | Go / no-go recommendation (proceed or stay ashore) | SAFE, CAUTION |
| **Delay** | Recommendation to delay departure until conditions improve | SAFE, CAUTION |
| **DepartureTime** | Recommended departure window (e.g., "depart between 06:00–07:30") | SAFE only |
| **Duration** | Recommended safe trip duration (e.g., "return within 4 hours") | SAFE only |

Under CAUTION, the AI retains directional guidance (should you go? should you wait?) but loses precision guidance (when exactly should you leave? how long can you stay?). This restriction removes recommendation types whose reliability degrades under elevated environmental risk, while preserving types that remain reliable.

### Why these four recommendation types?

The four types in R = {Go, Delay, DepartureTime, Duration} are not arbitrary — they correspond to the decision types that fishers actually make before and during each trip. Gao (2024), through 25 semi-structured interviews with Penang fishers, maps the daily operational decision structure: under favourable conditions, fishers decide *whether to go*, *when to depart*, *how long to stay*, and *where to fish* — full-scope decisions covering timing, location, species, and duration. Under marginal conditions, the decision collapses to *whether to go at all* and *whether to delay*. Under adverse conditions, operations halt entirely.

The architecture formalises this observed pattern. The four recommendation types map directly to the decision types Gao documents: Go (whether to go), Delay (whether to wait), DepartureTime (when to depart), Duration (how long to stay). Fishing area and species selection are excluded from the current formalisation because they are economic optimisation decisions rather than safety-critical decisions — they do not directly affect whether the fisher returns safely.

### Why Go and Delay survive into CAUTION but DepartureTime and Duration do not

This split reflects an empirically grounded distinction between directional and precision guidance.

**Directional guidance (Go, Delay)** answers binary questions: *should I go or stay?* *should I wait?* These questions remain answerable under elevated conditions because they require only a coarse assessment of overall risk. Gao (2024) documents that even under marginal conditions, fishers still make go/no-go decisions — the question does not disappear, it becomes more consequential. Rahim et al. (2024) confirm this in coastal Indonesia: under extreme weather, fishers decide whether to go at all (participation) and whether to shift to near-shore operations (scope restriction), but they do not attempt to optimise departure timing or trip duration.

**Precision guidance (DepartureTime, Duration)** answers continuous questions: *what is the best departure window?* *how many hours can I safely stay?* These require accurate forecasting of how conditions will evolve over the coming hours. Under elevated conditions, this forecasting reliability degrades for two reasons. First, Ryu & Han (2025) demonstrate that all maritime sensing modalities degrade simultaneously under adverse environmental conditions — the data that timing and duration estimates depend on becomes less reliable precisely when precision matters most. Second, Schrills et al. (2025) demonstrate that users anchor their behaviour on communicated precision: a specific departure time (e.g., "depart at 06:15") implicitly communicates high reliability, regardless of whether that reliability is warranted. Removing precision recommendations under CAUTION eliminates this false precision at source rather than relying on the fisher to discount it.

### Why Go carries a caution qualifier in CAUTION mode

When S = CAUTION, the Go recommendation type remains available but is presented with a caution qualifier (e.g., "Proceed with caution"). The recommendation *type* is unchanged — it is still a Go/no-go assessment. The qualifier communicates that conditions are elevated and the fisher should exercise additional vigilance. This design preserves set containment (Go ∈ A_AI(CAUTION) and Go ∈ A_AI(SAFE) — same type in both) while ensuring the fisher understands that CAUTION-mode advice carries a different risk profile than SAFE-mode advice. Without the qualifier, a Go recommendation under CAUTION would be indistinguishable from one under SAFE, undermining the fisher's ability to calibrate trust to the current safety state.

---

## 5. Environmental State Classification

### 5.1 The Environmental State Vector

The safety classification function operates on six independently observable parameters:

```
E = { w, r, m, o, v, t }
      |  |  |  |  |  |
      |  |  |  |  |  +-- t: Time of day (hour, 24-hour clock)
      |  |  |  |  +----- v: Vessel category (small, medium, big)
      |  |  |  +-------- o: Ocean state (wave height, swell period)
      |  |  +----------- m: Marine warning level (categorical)
      |  +-------------- r: Rainfall intensity (categorical)
      +----------------- w: Wind speed (knots, sustained)
```

All six parameters are measurable by non-AI sensors. This independence from the AI system is a formal requirement: the governance layer must not depend on the system it governs.

### 5.2 Per-Parameter Classification

Each parameter is independently classified into a safety zone using threshold comparisons:

| Parameter | SAFE | CAUTION | UNSAFE |
|---|---|---|---|
| **w** — Wind speed | < 15 knots | 15-25 knots | > 25 knots |
| **r** — Rainfall | None / light | Moderate | Heavy / storm |
| **m** — Marine warning | None | Advisory | Warning / alert |
| **o** — Ocean state (wave height) | < 1.0 m | 1.0-2.0 m | > 2.0 m |
| **v** — Vessel category | Big | Medium | Small |
| **t** — Time of day | 06:00-17:00 | 17:00-19:00 | 19:00-06:00 |

*Thresholds are illustrative. Final values require domain expert calibration and validation against Malaysian maritime safety data. The architecture's formal properties hold for any valid threshold assignment.*

### 5.3 Worst-Case Aggregation

The overall safety state is determined by the most severe per-parameter classification:

**S = max-severity(S_w, S_r, S_m, S_o, S_v, S_t)**

If *any single parameter* classifies as UNSAFE, the overall state is UNSAFE.  
If *any parameter* classifies as CAUTION and *none* as UNSAFE, the overall state is CAUTION.  
Only if *all parameters* classify as SAFE is the overall state SAFE.

**Example: How worst-case aggregation works in practice**

Suppose a fisher checks conditions at 07:00 on a day with a marine advisory:

```
  Parameter          Reading          Status
  ─────────────────────────────────────────────
  Wind speed         10 knots         SAFE
  Rainfall           none             SAFE
  Marine warning     advisory         CAUTION  <── worst reading
  Wave height        0.8m             SAFE
  Vessel category    big              SAFE
  Time of day        07:00            SAFE
  ─────────────────────────────────────────────

  Five out of six readings are SAFE.
  But one reading (marine warning) is CAUTION.

  Result:  Overall state = CAUTION

  Why? Because the system follows the worst reading,
  not the average. One concerning condition is enough.
  Five safe readings cannot cancel out one warning.
```

The same logic applies if any single reading reaches UNSAFE:

```
  Same day, but wind increases to 30 knots:

  Wind speed         30 knots         UNSAFE  <── worst reading
  Rainfall           none             SAFE
  Marine warning     advisory         CAUTION
  Wave height        0.8m             SAFE
  Vessel category    big              SAFE
  Time of day        07:00            SAFE
  ─────────────────────────────────────────────

  Result:  Overall state = UNSAFE

  Even though most readings are fine, the wind alone
  makes conditions dangerous. AI is switched off entirely.
```

This worst-case rule ensures that a single dangerous condition cannot be hidden or diluted by other favourable conditions.

---

## 6. Two-Level Governance vs. Existing Approaches

The proposed architecture is structurally distinct from four established classes of AI systems. The distinction is not one of degree but of kind: each class solves a different problem.

Consider what happens when conditions become dangerous. Each existing approach responds differently — and none responds the way the proposed architecture does.

**Scenario: Wind rises to 20 knots (CAUTION level). What does each system do?**

```
+---------------------------------------------------------------------+
|  CONVENTIONAL DSS (e.g., weather-informed fishing app)               |
|                                                                     |
|  The system still gives ALL advice types:                           |
|    "Depart at 06:15"   "Trip duration: 6 hours"   "Try area B"     |
|                                                                     |
|  Problem: The departure time and duration estimates are             |
|  unreliable under these conditions, but the system gives            |
|  them anyway. The fisher must guess which advice to trust.          |
+---------------------------------------------------------------------+

+---------------------------------------------------------------------+
|  ADAPTIVE AUTONOMY (e.g., Flehmig et al.)                           |
|                                                                     |
|  The system changes WHO has authority:                               |
|    "Human supervisor must now approve AI recommendations"           |
|                                                                     |
|  The AI still gives ALL advice types — same as before.              |
|  Only the approval process changes. The unreliable departure        |
|  time and duration estimates are still presented.                   |
+---------------------------------------------------------------------+

+---------------------------------------------------------------------+
|  GUARDRAILS / SHIELDS (e.g., Konighofer et al.)                     |
|                                                                     |
|  The system checks each individual output:                          |
|    "Go recommendation" --> pass or block?                           |
|    "Depart at 06:15"   --> pass or block?                           |
|                                                                     |
|  Each output is either fully allowed or fully blocked.              |
|  There is no middle ground. No CAUTION mode exists.                 |
+---------------------------------------------------------------------+

+---------------------------------------------------------------------+
|  PROPOSED ARCHITECTURE                                               |
|                                                                     |
|  The system restricts WHAT TYPES of advice AI can give:             |
|    "Go/No-go: Proceed with caution"          <-- allowed            |
|    "Delay: Consider waiting for conditions"   <-- allowed           |
|    "Depart at 06:15"                          <-- NOT allowed       |
|    "Trip duration: 6 hours"                   <-- NOT allowed       |
|                                                                     |
|  The AI still participates — but only with advice types that        |
|  remain reliable under current conditions. Unreliable types         |
|  are removed at source, not filtered after the fact.                |
+---------------------------------------------------------------------+
```

**The core difference in one sentence:**

- Conventional DSS: gives everything, always
- Adaptive Autonomy: changes *who approves*, not *what AI says*
- Guardrails/Shields: blocks individual outputs — all or nothing
- **Proposed**: changes *what types of advice AI is allowed to give*, based on current conditions

**Comparison table:**

| Question | DSS | Adaptive Autonomy | Guardrails | **Proposed** |
|---|---|---|---|---|
| Does AI advice change when conditions change? | No | No | Per-output only | **Yes — by type** |
| Is there a mode between "full AI" and "no AI"? | No | No | No | **Yes — CAUTION** |
| Who decides what AI can say? | Designer (fixed) | Designer (fixed) | Static rules | **Environmental state** |
| Can a fisher get basic guidance under moderate risk? | Gets everything (including unreliable) | Gets everything (needs supervisor) | Gets nothing (blocked) | **Gets go/no-go and delay only** |

---

## 7. Scenario Walkthrough: A Fisher's Day

This walkthrough traces a single day of operations to illustrate how the governance architecture responds to changing environmental conditions.

### 05:30 — Pre-Dawn Assessment

```
Environmental State:
  w = 8 knots     → S_w = SAFE
  r = none        → S_r = SAFE
  m = none        → S_m = SAFE
  o = 0.5m waves  → S_o = SAFE
  v = big         → S_v = SAFE
  t = 05:30       → S_t = UNSAFE  ← night hours

S = max-severity(SAFE, SAFE, SAFE, SAFE, SAFE, UNSAFE) = UNSAFE
G(S) = 0    |    A_AI(S) = {}
```

**System display:** "UNSAFE — AI advisory unavailable. Darkness: insufficient visibility for safe small-vessel operation. Environmental conditions are otherwise favourable. Advisory will activate after 06:00."

The fisher sees conditions are good apart from darkness. The system is transparent about *why* AI is unavailable and *when* it will become available.

### 06:15 — Morning Departure Window

```
Environmental State:
  w = 8 knots     → S_w = SAFE
  r = none        → S_r = SAFE
  m = none        → S_m = SAFE
  o = 0.5m waves  → S_o = SAFE
  v = big         → S_v = SAFE
  t = 06:15       → S_t = SAFE  ← daylight

S = max-severity(SAFE, SAFE, SAFE, SAFE, SAFE, SAFE) = SAFE
G(S) = 1    |    A_AI(S) = {Go, Delay, DepartureTime, Duration}
```

**System display:** "SAFE — Full advisory available."

**AI recommendations (full scope):**
- **Go**: "Conditions are favourable for departure"
- **DepartureTime**: "Optimal departure window: 06:30-07:30"
- **Duration**: "Recommended trip duration: up to 8 hours"

The fisher reviews the full advisory set and decides to depart at 07:00.

### 13:00 — Afternoon Deterioration

```
Environmental State:
  w = 18 knots    → S_w = CAUTION  ← wind increasing
  r = moderate    → S_r = CAUTION  ← rain beginning
  m = advisory    → S_m = CAUTION  ← advisory issued
  o = 1.3m waves  → S_o = CAUTION  ← seas building
  v = big         → S_v = SAFE
  t = 13:00       → S_t = SAFE

S = max-severity(CAUTION, CAUTION, CAUTION, CAUTION, SAFE, SAFE) = CAUTION
G(S) = 1    |    A_AI(S) = {Go, Delay}
```

**System display:** "CAUTION — Restricted advisory. Conditions elevated. Detailed timing and duration guidance unavailable."

**AI recommendations (restricted scope):**
- **Go**: "Proceed with caution — consider returning to shore"
- **Delay**: "Conditions may deteriorate further; if returning, do not delay"

The AI does *not* provide DepartureTime or Duration. It cannot say "you have 3 more hours" because the reliability of duration estimates is degraded under these conditions. The fisher receives directional guidance (should I stay or go back?) without false precision.

### 16:30 — Conditions Worsen

```
Environmental State:
  w = 28 knots    → S_w = UNSAFE  ← exceeds threshold
  r = heavy       → S_r = UNSAFE
  m = warning     → S_m = UNSAFE
  o = 2.5m waves  → S_o = UNSAFE
  v = big         → S_v = SAFE
  t = 16:30       → S_t = SAFE

S = max-severity(UNSAFE, UNSAFE, UNSAFE, UNSAFE, SAFE, SAFE) = UNSAFE
G(S) = 0    |    A_AI(S) = {}
```

**System display:** "UNSAFE — AI advisory withdrawn. Dangerous conditions: high wind (28 kn), heavy rain, 2.5m seas, marine warning active. Return to shore immediately. This is a safety alert, not AI advice."

The AI is completely silent. The safety alert is a deterministic system message from the governance layer, not an AI recommendation. The fisher relies on own judgement and any operational safety systems (radio, GPS, emergency beacon).

### 18:30 — In Port, Conditions Easing

```
Environmental State:
  w = 12 knots    → S_w = SAFE  (below 15 kn threshold)
  r = light       → S_r = SAFE
  m = none        → S_m = SAFE  (advisory lifted)
  o = 0.8m waves  → S_o = SAFE
  v = big         → S_v = SAFE
  t = 18:30       → S_t = CAUTION  ← approaching darkness

S = max-severity(SAFE, SAFE, SAFE, SAFE, SAFE, CAUTION) = CAUTION
G(S) = 1    |    A_AI(S) = {Go, Delay}
```

**System display:** "CAUTION — Restricted advisory. Approaching darkness limits safe operation window."

**AI recommendations (restricted scope):**
- **Go**: "Conditions have improved but darkness approaching — departure not recommended"
- **Delay**: "Delay departure until tomorrow morning"

Even though weather conditions have returned to SAFE ranges, the time-of-day classification keeps the overall state at CAUTION. The AI provides directional guidance but cannot recommend a departure window or trip duration because those recommendation types are not in A_AI(CAUTION).

---

## 8. Formal Safety Properties

The architecture is defined by three formal properties that must hold at all times.

### Property 1: Participation Constraint

> **If G(S) = 0, then A_AI(S) = {}**

When the participation gate is closed, the admissible recommendation space must be empty. Deterministic safety classification overrides AI advisory reasoning unconditionally.

### Property 2: Advisory Restriction Constraint

> **A_AI(CAUTION) is a proper subset of A_AI(SAFE)**

The CAUTION state must restrict AI advisory scope relative to SAFE. CAUTION is not SAFE with a warning label — it is a governance state with a formally smaller recommendation space.

### Property 3: Safety Dominance Property

> **For all E: AI(E) is a subset of A_AI(f(E))**

Whatever the AI generates must belong to the admissible recommendation space defined by the current safety state. Probabilistic AI reasoning cannot produce recommendations outside deterministic safety constraints.

**Consequence:** If S = UNSAFE, then A_AI(S) = {} (by Property 1), therefore AI(E) must be a subset of {} = {}, therefore AI(E) = {}. The AI generates nothing. This is guaranteed by architecture, not by AI behaviour.

---

## Summary of Formal Components

| Symbol | Meaning | Computational character |
|---|---|---|
| **E** = {w, r, m, o, v, t} | Environmental state vector | 6 observable parameters from non-AI sensors |
| **S** = f(E) | Safety state classification | Deterministic, O(1), threshold comparisons |
| **G(S)** | AI participation gate | Binary: 0 (disabled) or 1 (enabled) |
| **A_AI(S)** | Admissible recommendation space | Set of permitted recommendation types |
| **(G(S), A_AI(S))** | Governance pair | Two-level governance controlled by S |
| **AI(E)** | AI-generated recommendations | Must satisfy AI(E) ⊆ A_AI(S) |

**The governance pipeline:**

E -> S = f(E) -> (G(S), A_AI(S)) -> AI(E) -> Human Decision

The proposed contribution is the governance pair (G(S), A_AI(S)) — a two-level governance architecture that formally constrains how AI participates in decision-making under different safety states. The architecture ensures AI operates within a safety-governed advisory space and cannot generate recommendations outside deterministic safety constraints.

---

## 9. Limitations

The architecture makes deliberate trade-offs in favour of safety. The following limitations are inherent consequences of these design choices.

**Important context:** In practice, the UNSAFE state typically occurs when the fisher is already on shore — either they checked conditions before departure and the system classified UNSAFE (so they never left), or conditions deteriorated gradually through CAUTION first. During CAUTION, the AI already advised "consider returning to shore." The architecture's graduated design means the fisher should rarely be caught at sea during UNSAFE without prior CAUTION-mode warning. Most limitations below therefore affect planning capability on shore (e.g., "when will conditions improve?"), not immediate safety at sea.

### L1. Loss of planning capability under UNSAFE

When the system classifies UNSAFE, the fisher — typically on shore — receives no AI advisory support. The governance layer can issue pre-defined safety alerts (e.g., "dangerous conditions — do not depart"), but these are generic deterministic messages, not contextualised guidance. The AI cannot advise on *when conditions are expected to improve*, *whether tomorrow's forecast is better*, or *how to plan around the adverse period* — those would be AI recommendations, which A_AI(UNSAFE) = {} prohibits.

The practical cost is lost planning capability during the waiting period. The fisher knows conditions are dangerous (the system tells them so), but cannot get AI-assisted guidance on when they might safely resume operations. For fishers who depend on daily catches for income — Rahim et al. (2024) document that income drops from IDR 656,000 to IDR 213,000 per trip during extreme weather and trip frequency halves — this planning gap has direct economic consequences. The fisher's situation under UNSAFE is equivalent to the current status quo (no AI decision support at all), not a degradation from it — but the architecture could, in principle, provide more.

### L2. Binary cliff at the CAUTION-UNSAFE boundary

The CAUTION mode solves the binary governance problem between SAFE and CAUTION: instead of jumping from full AI to no AI, the fisher receives restricted AI. But the same binary problem reappears at the CAUTION-UNSAFE boundary — the transition from {Go, Delay} to {} is a binary cliff. There is no intermediate state between "basic directional guidance" and "nothing."

In practice, this cliff is mitigated by the graduated design itself. Environmental conditions typically deteriorate gradually — wind builds over hours, seas rise in response. The system transitions through CAUTION before reaching UNSAFE, giving the fisher a warning period with restricted AI advice. A sudden jump from SAFE directly to UNSAFE (e.g., an unexpected squall) is meteorologically possible but uncommon for the sustained conditions captured by the E vector. The CAUTION buffer absorbs most real-world transitions.

A finer graduation (e.g., a fourth state between CAUTION and UNSAFE) is architecturally possible — the containment property A_AI(S₁) ⊃ A_AI(S₂) ⊃ ... ⊃ A_AI(S_n) = {} generalises to any number of states. However, each additional state increases classification complexity, threshold calibration burden, and the cognitive load on users who must understand and respond to each distinct mode. Three states represent a balance between graduated governance and operational simplicity — aligned with the proceed/caution/stop grammar used across safety-critical domains (Gyllenhammar et al., 2025; Flehmig et al., 2024) and with fisher decision patterns (Gao, 2024: go/cautious-go/don't-go).

### L3. No degraded AI fallback within UNSAFE

The participation gate G(S) is binary: AI is either enabled (G = 1) or disabled (G = 0). The architecture does not define a minimal or degraded AI mode within UNSAFE — for example, a simple rule-based fallback that could provide basic directional guidance without the full probabilistic model. Whether wind is 26 knots (just over the UNSAFE threshold) or 50 knots (extreme storm), the system response is identical: AI off.

This limitation is a consequence of the Safety Dominance Property. If AI(E) ⊆ A_AI(S) and A_AI(UNSAFE) = {}, then AI must produce nothing. Allowing any AI output under UNSAFE would violate the formal safety guarantee. A degraded fallback would need to be classified as a non-AI deterministic system (like the safety alert) rather than as AI advisory output — an extension that the current formalisation does not address.

### L4. Fixed recommendation type set

The recommendation type space R = {Go, Delay, DepartureTime, Duration} is defined at design time. The architecture does not currently accommodate dynamic expansion of recommendation types (e.g., adding route guidance or species-specific advice) without revisiting the formal definitions of A_AI(S) for each state. In practice, adding new recommendation types requires determining which safety states they belong to — a domain calibration task, not an architectural change, but one that must be performed carefully to preserve the containment property.

### L5. Threshold sensitivity

The safety state classification S = f(E) depends on threshold values that partition each parameter's range into SAFE, CAUTION, and UNSAFE zones. The architecture's formal properties (containment, Safety Dominance) hold for any valid threshold assignment — but the practical value of the system depends on thresholds being well-calibrated. Poorly calibrated thresholds could produce excessive over-classification (system stuck in CAUTION or UNSAFE under conditions fishers consider manageable, leading to disuse) or under-classification (system in SAFE when conditions are genuinely dangerous). Threshold calibration requires domain expert validation and empirical testing — essential for deployment but outside the scope of the architectural contribution.

### L6. No trip phase awareness

The governance pair (G(S), A_AI(S)) is conditioned solely on safety state S. It does not distinguish between a fisher on shore planning a departure, a fisher in transit leaving port, and a fisher at sea mid-operation. The same safety state produces the same governance configuration regardless of operational phase.

In practice, the useful advice differs by phase. Pre-departure, the fisher needs "should I go?" and "when should I leave?" At sea, the fisher needs "should I return?" and "how much time do I have left?" The Go recommendation type means different things in each context — "depart or stay home" versus "continue or return to shore" — but the architecture treats them identically.

This limitation is most visible under CAUTION at sea: the AI advises "proceed with caution" using the same pre-departure framing, when what the fisher actually needs is return guidance. A trip phase parameter p ∈ {shore, transit, sea} as a separate input to the governance pair — A_AI(S, p) rather than A_AI(S) — would allow phase-appropriate recommendations without modifying the environmental state vector E or the safety classification function S = f(E). This extension preserves the architecture's formal properties (containment and Safety Dominance would hold along the S dimension for each fixed p) and is a candidate for future work.

### Summary: What these limitations share

All six limitations stem from the same design principle: the architecture prioritises *never giving unreliable advice* over *always giving some advice*. This is the correct trade-off for a safety-critical system where the consequences of bad advice (a fisher following an unreliable departure time into dangerous conditions) are more severe than the consequences of no advice (a fisher relying on their own judgement, as they do today). The graduated design mitigates the sharpest edge of this trade-off: the CAUTION mode ensures that AI withdrawal under UNSAFE is rarely abrupt, because the fisher has already received restricted advisory guidance during the preceding CAUTION period. The limitations define the boundaries of the current contribution and frame directions for future work — particularly the design of deterministic fallback mechanisms that could operate within UNSAFE without violating the Safety Dominance Property.
