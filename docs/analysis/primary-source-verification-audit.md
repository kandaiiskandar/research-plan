# Primary-Source Verification and Gap Alignment Audit

**Date:** 2026-09-21
**Scope:** Verification of the claims carrying the research gap in `experiment-report-delta-l2.md` §2, §3.1, §3.2, and of the claimed CS contribution.
**Method:** Adversarial. Primary sources consulted directly; extraction notes treated as claims to be tested, not as evidence.
**Report status:** **UNCHANGED.** This document records findings and recommendations only.

---

## Sources consulted at primary level

| Source | Access | Consulted |
|---|---|---|
| FAA AC 20-151C (TCAS II) | faa.gov official PDF | §§2.1.1, 2.2.2.1, 2.2.10, 2.3.4, 2.3.5, 2.3.5.1, 2.3.6.1–2.3.6.7, Tables 1–2 |
| Baxi (2026), CGAE | `papers/sources/` PDF | Defs 1–14, Alg. 1, Props 1–3, §§3.1–3.2.3 |
| Shamsujjoha et al. (2025) | `papers/sources/` PDF | Guardrail rule-type taxonomy, pipeline-stage section |
| Flehmig et al. (2024) | `papers/sources/` PDF | Abstract, §§I–III degradation vocabulary |
| Könighofer et al. (2025) | `papers/sources/` PDF | Full-text term sweep |
| Dalrymple et al. (2024) | `papers/sources/` PDF | Full-text term sweep |

**Not verified at primary level (notes only):** Cleaveland et al. (2023); Parasuraman et al. (2000); Bernabei & Costantino (2024); Kwon & Kim (2026); Indykov et al. (2025). Their coding remains at notes-level authority — see §I.

---

## A. Primary-Source Verification Matrix

| Source | Governed object | Conditioning variable | State representation | Lever | Governance point | Final authority | Observation-quality semantics | Status |
|---|---|---|---|---|---|---|---|---|
| **FAA AC 20-151C** | Advisory **types** issuable to flight crew; nested, contracting to TA-only then empty | **External + platform.** Radio altitude AGL; pressure altitude; flap/slat/landing-gear discretes (§2.3.6.3); weight–altitude–temperature (§2.3.4, Tbl 1 n.1); airspeed margin from stall; bank angle >15°; one-engine-inoperative | **MULTI-COMPONENT, discrete/banded, runtime.** NOT single-component | Advisory scope (automatic); participation is **pilot-selected** mode (TA/RA, TA-only, standby, §2.2.2.1) | **UNCLEAR.** Tbl 2 says "inhibited below X ft" = prevented issuance; §2.3.4 "change strategy and issue an alternative RA" implies selection-level. Pre- vs post-generation **not specified** | **Human, explicitly preserved.** §2.1.1: "TCAS II does not alter or diminish the pilot's basic authority and responsibility to ensure safe flight" | **PARTIAL.** Validity flags required for pressure altitude (§2.3.6.1) and radio altitude (§2.3.6.2.6); sensor-failure alerting (§2.3.6.7). **NO** conservative degradation on invalid input — §2.3.5 concedes the system continues without inhibits and "may command maneuvers that may significantly reduce stall margins". **NO** staleness/latency requirement. **NO** unknown-vs-unavailable distinction | **OVERSTATED / UNDERSTATED** (see B1, B2) |
| **Baxi (2026)** | Permitted **economic action set** E ⊆ Σ of an autonomous agent, across K nested tiers | **AI-internal.** Robustness vector R ∈ [0,1]⁴ = (CC, ER, AS, IH); gate uses three: f(R)=T_k, k = min(g₁(CC), g₂(ER), g₃(AS)) | **MULTI-COMPONENT (3 gating + 1 diagnostic), discrete tiers with thresholds θᵢ⁰<…<θᵢᴷ, monotone (Prop. 1)** | **Both, but UNIFIED in one function.** A single tier index determines participation (T₀) and permitted action set | **Pre-action authorisation.** Alg. 1 runs when an agent requests a higher tier; grants/denies access to T_k actions | **Autonomous agent.** Non-formalisable tasks "excluded from autonomous agent execution" (Assum. 1); human co-signer only for unverifiable aspects | **NO.** No observation-quality machinery. Temporal decay δ(Δt) applies to *certification staleness*, not to observation staleness | **VERIFIED** |
| **Shamsujjoha et al. (2025)** | Agent artifacts and outputs across pipeline stages; 13 guardrail actions | Per-artifact, per-quality-attribute; rule types include **context-dependent** | Not a classified state | **Content filtering**; participation partial (block/isolate) | Input, **intermediate results**, and final outputs — explicitly includes post-generation | Human intervention is one of 13 actions, **not a structural invariant** | **NO** explicit observation-quality semantics | **PROJECT CODING INCORRECT** (see B3) |
| **Flehmig et al. (2024)** | Supervisory response intensity; a "limiting logic" constrains AI outputs but is **not** state-graduated | **AI-internal.** Concept drift, data drift, outliers, adversarial input — verified in abstract and §§I–III | Three-level index | Participation + supervisory intensity; scope unchanged across levels | Runtime supervisory switching; backup at red | **Human operator** — explicit decision-support positioning | **NO.** "Degradation" is model degradation, not observation quality. Distinction in the report **holds** | **VERIFIED** |
| **Könighofer et al. (2025)** | Executable action set of an autonomous agent | Formal model + safety specification | Per-state, per-action | Action admissibility; participation at winning-region boundary | Pre-execution (pre-shielding) or post-hoc filtering | **None** — no human in the loop | **NO.** "Partial observability" appears only in reference titles, not as governed semantics | **VERIFIED** |
| **Dalrymple et al. (2024)** | Whether a verified policy's output reaches the world | Verification against specification relative to world model | Not a classified runtime state | Participation; scope only globally via specification | Policy-level verification; runtime monitoring may disable | Not a governance property | **NO.** "invalid" appears once, not as governed semantics | **VERIFIED** |
| **Proposed architecture** *(reference)* | AI participation + admissible **recommendation categories presented to a human** | **External environmental**, S = f(E) over {w, r, m, o, t} | Multi-component, classified, runtime | **Both, as two separate functions** G(S), A_AI(S) | **Pre-inference** — RS(S) supplied before generation | **Human, unconditionally** | ⊥ semantics separating invalid / absent / stale / unmeasured; declared exclusion set D; fail-safe gᵢ(⊥)=UNSAFE | — |

---

## B. Corrections required to §3.2 and §3.1

**B1 — TCAS state representation. Current: "one banded measurement" → Verified: MULTI-COMPONENT.**
§3.1 states "The avionics precedent conditions on one banded measurement in a certified airframe." The primary source contradicts this. AC 20-151C §2.3.6.3 requires "discrete information from flaps, slat, landing gear, and/or other aircraft configuration sensors"; §2.3.4 and Table 1 add weight–altitude–temperature, airspeed margin from stall, bank angle >15°, and one-engine-inoperative conditions. *Reason:* the previous coding read only the radio-altitude inhibit table (§2.3.6.2) and missed the performance-based inhibit logic. **This removes "multi-component" as a differentiator.**

**B2 — TCAS final authority. Current: "procedurally constrained, not unconditional" → Verified: EXPLICITLY PRESERVED.**
§2.1.1: *"We view TCAS II systems as a supplement to the pilot who has the primary responsibility for avoiding midair collisions… TCAS II does not alter or diminish the pilot's basic authority and responsibility to ensure safe flight."* The ICAO RA-compliance expectation is real but sits outside this source. *Reason:* the notes imported an external procedural fact into a cell about what the source states. **This weakens "unconditional human authority" as a differentiator against TCAS.**

**B3 — Shamsujjoha "context-dependent". Current: "static deployment conditions" → Verified: INCORRECT.**
Primary source: *"Context-dependent strategies adjust the implementation of guardrails based on the system's specific operational context. This allows for **dynamic adjustments to guardrails in response to changing conditions, user needs, and operational environments**."* The report's *(interp.)* cell asserts the opposite. *Reason:* the interpretation was recorded in this project's own verification document and never checked against the paper. The taxonomy still specifies no classified state, no admissibility contract and no formal semantics — so the gap does not collapse — but **the stated distinction is false and must be withdrawn.**

**B4 — TCAS governance point. Current: implied post-hoc → Verified: UNCLEAR.**
The AC does not specify pre- vs post-generation suppression. Neither the project nor a reviewer can settle this from this source. **"Pre-inference" cannot be claimed as a differentiator against TCAS without further evidence.**

**B5 — Baxi.** Coding **VERIFIED**. One refinement available: participation and scope are unified in a *single* tier index, not expressed as two functions. The separation of G(S) from A_AI(S) is therefore a genuine structural difference, though a modest one.

---

## C. Gap conjunct audit (G1–G9)

| # | Proposition | Verdict | Evidence |
|---|---|---|---|
| **G1** | Classified multi-component state | **ALREADY ESTABLISHED** | TCAS (radio alt + config discretes + W/A/T + airspeed + bank + OEI); Baxi (3-component weakest-link gate over discrete tiers) |
| **G2** | State is external/environmental, not AI-internal | **PARTIALLY ESTABLISHED** | TCAS conditions on external sensor + platform state. Baxi, Flehmig, Kwon & Kim are AI-internal. No verified source conditions on a classified *environmental* state in the weather/sea sense |
| **G3** | Observation-resolution / exclusion semantics | **NOT IDENTIFIED IN VERIFIED SOURCES** | TCAS requires validity *flags* (§§2.3.6.1, 2.3.6.2.6) but mandates **no** conservative degradation — §2.3.5 concedes continued operation without inhibits; no staleness/latency requirement; no unknown-vs-unavailable distinction. Absent from Baxi, Shamsujjoha, Flehmig, Könighofer, Dalrymple. **Now a coded absence, not an absence of coding** |
| **G4** | State-conditioned advisory-type admissibility | **ALREADY ESTABLISHED** | TCAS Table 2 — nested, contracting to empty |
| **G5** | Governance independent of the generator | **ALREADY ESTABLISHED** | Könighofer (shield separate from RL agent); Baxi (gate separate from agent) |
| **G6** | Applied before impermissible categories can be produced | **UNCLEAR** | Not specified in AC 20-151C. Könighofer's pre-shielding is a precedent for supplying a safe set *before* selection, but for machine actions |
| **G7** | Human-facing decision support | **ALREADY ESTABLISHED** | TCAS (flight crew); Flehmig (explicit assistant positioning); Kwon & Kim (clinician) |
| **G8** | Human retains final decision authority | **ALREADY ESTABLISHED** | AC 20-151C §2.1.1 verbatim; Kwon & Kim (deferral without override) |
| **G9** | Participation and scope separately represented | **PARTIALLY ESTABLISHED / NOT IDENTIFIED** | Baxi controls both but unifies them in one tier index. TCAS has pilot-selected mode + automatic scope restriction, but participation is not state-conditioned. **No verified source specifies them as two state-conditioned functions** |

**Conjunction test.** Seven of nine conjuncts are established or partially established individually. **No verified source exhibits the conjunction.** The conjunction survives — but it is carried by G3, G9 and the environmental reading of G2, not by G1, G4, G7 or G8, which the current §3.1 leans on.

---

## D. Strongest prior precedents

1. **FAA AC 20-151C** — the dominant threat. Verified to establish G1, G4, G7 and G8 simultaneously: a multi-component discrete state restricting advisory *types* presented to a human whose authority is explicitly undiminished. This is most of the architecture's shape, certified since the 1990s. The project's own notes already warn that the "it governs an algorithm, not AI" defence must not be relied on, since Layer 3 is a deterministic rule engine.
2. **Baxi (2026)** — establishes the formal machinery: multi-component classified state, monotone gate, nested admissible sets, pre-action application, containment theorem. Conditioning variable and governed object differ; preprint, unreviewed.
3. **Shamsujjoha et al. (2025)** — weaker than B3 previously suggested, since context-dependent strategies do contemplate dynamic operational environments, but supplies no classified state or admissibility contract.

---

## E. Smallest surviving gap

> Within the verified sources, advisory-type admissibility conditioned on a multi-component runtime state, presented to a human retaining final authority, is established practice in certified collision-avoidance avionics; and graduated admissibility over a classified multi-component state with a monotone gate and nested permitted sets is established for AI-internal robustness conditioning. What was not identified in the verified sources is a treatment in which **(i)** the conditioning state is an external *environmental* classification assembled from heterogeneous, independently-faulting observations, **(ii)** observation quality is itself given governed semantics — invalid, absent, stale and structurally unmeasured handled distinctly, with declared exclusions and fail-safe resolution — and **(iii)** participation and advisory scope are specified as two separate state-conditioned functions rather than a single graduated index.

Conceded relative to current §3.1: multi-component state, advisory-type admissibility, human-facing delivery, unconditional human authority, generator-independent governance, nested contracting sets, formal monotonicity.

---

## F. Computer Science contribution after concession

**Already established — do not claim:** state-conditioned advisory admissibility; nested admissible sets contracting to empty; deterministic safety gating; multi-level graduated governance; human-in-the-loop decision support; monotone gate functions; containment theorems; generator-independent governance placement.

**Adaptation / operationalisation:** transfer of the certified avionics advisory-inhibition pattern from a single-platform certified airframe to an unattended, heterogeneous, low-resource environmental setting.

**Defensible contribution:** an **operational governance contract** — the observation-to-classification layer, not the gate. Specifically: ⊥ semantics distinguishing invalid, absent, stale and structurally unmeasured inputs; the declared exclusion set D with its lower-bound consequence; fail-safe resolution gᵢ(⊥)=UNSAFE with totality proved over the observation space rather than the ideal domain; and the separation of G(S) from A_AI(S) as two functions. Best characterised as **operationalisation plus formalisation of observation-quality semantics**, with an **empirical characterisation** of activation frequency — not as a novel architecture.

**Domain contribution:** threshold instantiation for small-scale Malaysian coastal fisheries, with the MET boundary gap documented, and the five-year characterisation.

---

## G. Evidence–claim alignment

| Surviving claim | Status | Note |
|---|---|---|
| Intermediate state changes the admissible set (structural) | **SUPPORTED** | Entailed by comparator definitions; §3.3 |
| Level 2 becomes operationally active on real traces | **SUPPORTED BY CURRENT EXPERIMENT** | Δ_L2 = 5.81% / 4.48% |
| Participation and scope as two separate functions | **PARTIALLY SUPPORTED** | C1↔C2 isolates the scope term, but no condition varies G(S) and A_AI(S) independently |
| **Observation-quality semantics (⊥, D, staleness, fail-safe resolution)** | **NOT CURRENTLY EVALUATED** | ⚠️ **EVIDENCE–CLAIM ALIGNMENT PROBLEM** |
| Human retains final authority | **NOT CURRENTLY EVALUATED** | No human-subject evidence; RQ5 deferred |

### ⚠️ EVIDENCE–CLAIM ALIGNMENT PROBLEM

The element that best survives primary-source verification — observation-quality semantics (G3) — is **the one the experiment does not test**. The replay runs with `D = {m}` held constant; no hour manipulates staleness, invalidity or resolution, and no condition varies the exclusion set. Δ_L2 measures the *gate*, which is the part now largely conceded to prior work.

Restated: **the experiment evidences the conceded contribution; the surviving contribution is unevidenced.**

Options, none of which the current replay satisfies: (a) add a condition varying D or injecting faults and measure classification divergence; (b) present the observation semantics as formal contribution evidenced by proof rather than replay; (c) narrow the claimed contribution to what Δ_L2 evidences, conceding G3 as specification-only.

---

## H. Recommended changes — NOT IMPLEMENTED

| Location | Change | Priority |
|---|---|---|
| **§3.1** | Remove "one banded measurement" (factually wrong, B1). Adopt E, or a narrowing of it | **HIGH** |
| **§3.2** TCAS row | State representation → multi-component with the full input list; authority → quote §2.1.1; governance point → UNCLEAR | **HIGH** |
| **§3.2** Shamsujjoha row | Withdraw the "static deployment conditions" claim (B3) | **HIGH** |
| **§3.2** interpretation | "Where a mechanism governs a human-facing advisory set by external state, its state is single-component and authority is procedurally constrained" — both halves now false | **HIGH** |
| **§2** GAP box | Currently rests on the multi-component/environmental reading; re-anchor on observation semantics + G-A_AI separation | **MEDIUM** |
| **Contribution statement** | Reframe from architecture-novelty to operationalisation + observation-semantics formalisation (F) | **MEDIUM** |
| **§6 limitations** | Add the evidence–claim alignment problem | **HIGH** |

---

## I. Open questions

1. **Does the experiment need to change, or the claim?** The alignment problem in G is a supervisor decision, not a writing fix.
2. **Five sources remain unverified at primary level** — Cleaveland, Parasuraman, Bernabei & Costantino, Kwon & Kim, Indykov. Kwon & Kim matters most: it currently carries G8.
3. **TCAS governance point (G6)** — needs RTCA DO-185B/MOPS-level evidence, which AC 20-151C references but does not contain.
4. **Is G3 sufficient as a CS contribution?** Observation-quality semantics may read as engineering detail rather than a computer-science result. Supervisor judgement.
5. **Broader search not performed.** Fault-tolerant sensor fusion and fail-operational architectures were not searched and are the literature most likely to contain G3 precedents.
