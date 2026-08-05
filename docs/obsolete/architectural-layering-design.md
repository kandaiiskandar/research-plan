# Architectural Layering Design and Graphic Representation

**Research title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*

**Purpose:** This document describes the four-layer architecture as a design artefact — the structure of each layer, the rationale for separation, the inter-layer interfaces, and the properties each layer contributes to the Safety Dominance Property.

**Canonical sources:**
- Formal definitions → `docs/appendix-c-formalisation.md`
- Full architecture walkthrough → `docs/architecture-illustration.md`
- Layer 3 model type and proof → `docs/justification-layer3-enforcement.md`

---

## 1. The Formal Pipeline

```
E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision
```

Each arrow is an inter-layer interface. Each box is a functionally distinct layer with its own computational character, assurance basis, and failure mode.

---

## 2. Layer Stack Diagram

```
╔═════════════════════════════════════════════════════════════════════╗
║  LAYER 4 — HUMAN DECISION                                           ║
║  Role: Final decision authority — human cognitive reasoning only    ║
║  No computational component; no algorithmic override possible       ║
║                                                                     ║
║  Receives (two independent paths):                                  ║
║    · Safety state S         — from Layer 2 directly                 ║
║    · AI(E) recommendations  — from Layer 3 (if G(S) = 1)           ║
║                                                                     ║
║  Output: departure decision (go / delay / no-go) — human action,   ║
║          not a system command                                       ║
║  Authority: retained in all three safety states                     ║
╚═════════════════════════════════════════════════════════════════════╝
          ▲
          │  Recommendations + safety state indicator
          │
╔═════════════════════════════════════════════════════════════════════╗
║  LAYER 3 — AI ADVISORY REASONING                                    ║
║  Role: Generate recommendations within governed space               ║
║  Model: Production rule system                                      ║
║  Receives: E (environment) + RS(S) (rule set) from Layer 2          ║
║  Generates: AI(E)  where  AI(E) ⊆ A_AI(S)                          ║
║  Enforcement: Safety Dominance Property holds by construction        ║
╚═════════════════════════════════════════════════════════════════════╝
          ▲
          │  G(S), RS(S), A_AI(S)   [governance configuration]
          │
╔═════════════════════════════════════════════════════════════════════╗
║  LAYER 2 — DETERMINISTIC GOVERNANCE                                 ║
║  Role: Classify safety state; configure Layer 3 governance          ║
║  Computes: S = f(E) via worst-case aggregation                      ║
║  Outputs: governance pair (G(S), A_AI(S))                           ║
║                                                                     ║
║  ┌──────────────┬──────────────┬──────────────┐                    ║
║  │  S = SAFE    │ S = CAUTION  │  S = UNSAFE  │                    ║
║  ├──────────────┼──────────────┼──────────────┤                    ║
║  │  G(S) = 1    │   G(S) = 1   │   G(S) = 0   │                    ║
║  ├──────────────┼──────────────┼──────────────┤                    ║
║  │ A_AI =       │ A_AI =       │ A_AI = ∅     │                    ║
║  │ {Go, Delay,  │ {Go, Delay}  │              │                    ║
║  │  DepTime,    │              │              │                    ║
║  │  Duration}   │              │              │                    ║
║  └──────────────┴──────────────┴──────────────┘                    ║
║                                                                     ║
║  Character: deterministic, O(1), threshold comparisons, no AI       ║
╚═════════════════════════════════════════════════════════════════════╝
          ▲
          │  Raw environmental measurements:  E = {w, r, m, o, v, t}
          │
╔═════════════════════════════════════════════════════════════════════╗
║  LAYER 1 — ENVIRONMENT INPUT                                        ║
║  Role: Observe and supply environmental state vector                ║
║  Produces: E = {w, r, m, o, v, t}                                   ║
║                                                                     ║
║    w — Wind speed           Continuous  ℝ≥0                         ║
║    r — Rainfall intensity   Ordinal categorical                     ║
║    m — Marine warning level Ordinal categorical                     ║
║    o — Ocean state          Bivariate   ℝ≥0 × ℝ≥0                  ║
║    v — Vessel category      Ordinal categorical                     ║
║    t — Time of day          Continuous  [0, 24)                     ║
║                                                                     ║
║  All sources independent of the AI system                           ║
╚═════════════════════════════════════════════════════════════════════╝
```

**Containment property across the governance table:**
A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

---

## 3. Per-Layer Specification

| Property | Layer 1 | Layer 2 | Layer 3 | Layer 4 |
|---|---|---|---|---|
| **Name** | Environment Input | Deterministic Governance | AI Advisory Reasoning | Human Decision |
| **Role** | Observe and supply E | Classify safety state; configure governance | Generate recommendations within A_AI(S) | Final decision authority |
| **Input** | Six independently observable parameters: E = {w, r, m, o, v, t} | E from Layer 1 | E + RS(S) from Layer 2 | Safety state S from Layer 2 (direct) + AI(E) from Layer 3 (if G(S) = 1) |
| **Output** | E = {w, r, m, o, v, t} | S = f(E); governance pair (G(S), A_AI(S)); RS(S) | AI(E) ⊆ A_AI(S) | Departure decision |
| **Computational character** | Sensor / data acquisition | Deterministic threshold comparisons | Production rule system; finite rule evaluation | Human cognitive reasoning |
| **AI involved?** | No | No | Yes — rule-based | No |
| **Assurance basis** | Sensor calibration; source independence from AI | Static analysis; exhaustive threshold testing | Proof by construction via RS(S) | Human authority; no algorithmic override |
| **Formal property it contributes** | Independence of E from AI | S = f(E) correctness; Safety Dominance enablement | AI(E) ⊆ A_AI(S) — Safety Dominance Property | Final decision not delegated to AI |
| **Runtime complexity** | Sensor acquisition | O(1) | O(n), n = rule set size | — |
| **GPU required?** | No | No | No | No |
| **Low-resource viable?** | Yes | Yes | Yes | Yes |
| **Failure mode** | Sensor fault → stale E | Threshold miscalibration → wrong S | Rule set error → wrong AI(E) | Automation bias — fisher ignores own judgement |

---

## 4. Inter-Layer Interfaces

### Interface 1 → 2: Environmental state vector

**From:** Layer 1 (Environment Input)
**To:** Layer 2 (Deterministic Governance)
**Content:** E = {w, r, m, o, v, t}
**Parameter types:** w — Continuous ℝ≥0; r — Ordinal categorical; m — Ordinal categorical; o — Bivariate ℝ≥0 × ℝ≥0; v — Ordinal categorical; t — Continuous [0, 24)
**Critical property:** E must be independent of the AI system. The governance layer must not use the system it governs as a data source. Violation would allow the AI to influence its own safety classification.

### Interface 2 → 3: Governance configuration

**From:** Layer 2 (Deterministic Governance)
**To:** Layer 3 (AI Advisory Reasoning)
**Content:** G(S) — participation gate; RS(S) — active rule set; A_AI(S) — admissible recommendation space
**Timing:** Configuration is delivered to Layer 3 **before** any reasoning begins
**Critical property:** If G(S) = 0, Layer 3 receives no input and generates nothing. The rule set RS(S) determines AI(E) by construction — Layer 3 cannot produce recommendation types not represented in RS(S).

### Interface 3 → 4: Recommendations and state display

**From:** Layer 3 (AI Advisory Reasoning) and Layer 2 (safety state indicator)
**To:** Layer 4 (Human Decision)
**Content:** AI(E) — generated recommendations; safety state S — current classification
**Critical property:** The human receives the safety state independently of the AI recommendations. Under UNSAFE, the state alert comes from Layer 2 directly — it is not an AI recommendation and does not violate A_AI(UNSAFE) = ∅.

---

## 5. Why This Specific Layer Separation

### Why Layer 2 is separate from Layer 3

The governance function (Layer 2) must be independent of the AI advisory function (Layer 3) for three reasons:

1. **Verifiability.** Layer 2 is a finite deterministic function over a fixed threshold table. It can be verified by exhaustive testing and static analysis. If governance were embedded inside the AI, formal verification would require reasoning about probabilistic model behaviour — a fundamentally harder problem.

2. **Failure independence.** If Layer 3 fails (rule engine crash, corrupt rule set), Layer 2 continues operating. The safety state is still classified and the governance configuration is still computed. The system can issue a safety state alert even with no AI output.

3. **Causal direction.** The advisory engine cannot influence its own governance. Causal flow is strictly unidirectional: E → S → (G(S), A_AI(S)) → AI(E). No feedback path runs from Layer 3 back to Layer 2. The AI cannot reclassify its own safety state.

### Why Layer 1 is separate from Layer 2

Layer 1 separates the **observation of the environment** from the **classification of the environment**. This distinction matters because:

- Layer 1 sources (sensors, maritime authority broadcasts) must be independent of the AI system. Mixing data acquisition with governance logic would obscure this independence.
- Threshold values in Layer 2 require domain calibration and may be updated over time. Keeping them in a distinct governance layer means threshold updates do not affect sensor interfaces.
- Under sensor fault conditions, the failure mode is localised to Layer 1. Layer 2 can detect stale or missing readings and respond deterministically (e.g., default to UNSAFE on missing data).

### Why Layer 4 is separate from Layer 3

The human decision layer is architecturally distinct — not just a consumer of AI output. This separation encodes the design principle that AI in this system is **advisory**, never **executive**. Regardless of what Layer 3 recommends, the fisher makes the departure decision. The architecture enforces this by design: there is no path from AI(E) to an actuator. The only output path from Layer 3 is a display to Layer 4, and Layer 4's output is a human action, not a system command.

---

## 6. Formal Properties and the Layer That Enforces Each

| Property | Formal statement | Layer that enforces it | How |
|---|---|---|---|
| Environmental independence | E is independent of AI(E) | Layer 1 | All E sources are non-AI sensors and authority broadcasts |
| Safety state correctness | S = f(E) produces correct classification | Layer 2 | Deterministic threshold comparison; verified by exhaustive testing |
| Participation constraint | G(S) = 0 ⇒ AI(E) = ∅ | Layer 2 → Layer 3 interface | Layer 2 sends no input to Layer 3 when G(S) = 0 |
| Advisory restriction | A_AI(CAUTION) ⊂ A_AI(SAFE) | Layer 2 | RS(CAUTION) ≠ RS(SAFE); different rule sets supplied |
| Safety Dominance Property | AI(E) ⊆ A_AI(S) for all E | Layer 3 | RS(S) contains only rules producing types in A_AI(S) — proof by construction |
| Containment hierarchy | A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ | Layer 2 (definition of RS(S)) | Rule sets are defined to satisfy containment at design time |
| Human authority | Final decision is human, not AI | Layer 4 separation | No actuator path from Layer 3; AI output is advisory display only |

---

## 7. Low-Resource Compliance

The architecture is designed for deployment on constrained devices with intermittent connectivity (small-scale coastal fisheries, Terengganu and Penang). Each layer's computational requirements:

| Layer | Runtime | Memory | Connectivity | GPU |
|---|---|---|---|---|
| Layer 1 | Sensor read — milliseconds | Negligible | Required for API sources; optional for local sensors | No |
| Layer 2 | O(1) — six threshold comparisons | Constant — threshold table only | Not required | No |
| Layer 3 | O(n) — n = rule set size (small, finite) | Rule set in memory — kilobytes | Not required | No |
| Layer 4 | Human decision time | — | Not required | — |

The architecture can operate fully offline after initial rule set and threshold deployment. Layer 2 and Layer 3 are both deterministic, finite-state functions that execute in bounded time with negligible memory. This satisfies TinyML constraints and the deployment requirements established in the low-resource fisheries context.

---

## 8. The Contribution: The Governance Pair

The architectural contribution is the **governance pair (G(S), A_AI(S))** — the two-level structure at Layer 2 that simultaneously controls:

- **Level 1** — *whether* AI participates (G(S))
- **Level 2** — *what* AI is permitted to recommend (A_AI(S))

Both levels are conditioned on the same environmental safety state S = f(E). This is what prior architectures do not have:

- Binary gate architectures (e.g., Könighofer et al., 2025) implement Level 1 only. Under CAUTION, they give AI the full recommendation set because they have no Level 2.
- Adaptive autonomy architectures (e.g., Flehmig et al., 2024) change supervisory intensity, not AI recommendation scope. The AI still gives the same types of advice; only the approval process changes.
- Ungated systems give full AI output in all conditions.

The CAUTION mode — where G(S) = 1 (AI active) and A_AI(CAUTION) ⊂ A_AI(SAFE) (scope restricted) — is the unique operational state that only a two-level governance pair can produce. It is the architectural novelty that no single-level architecture can express.

---

*For the full formal proof that AI(E) ⊆ A_AI(S) holds by construction, see `docs/justification-layer3-enforcement.md` Section 4.*
*For the worked scenario showing all four layers in operation, see `docs/architecture-illustration.md` Section 7.*
