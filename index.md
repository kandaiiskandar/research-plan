---
layout: document
title: Research Plan
---

# A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries

**PhD Research Repository**

**Author:** Mohd Iskandar Samsuddin  
**Institution:** Universiti Malaysia Sabah (UMS)  
**Email:** iskandarsamsuddin@gmail.com  
**Field:** Computer Science / Artificial Intelligence

---

## One sentence summary

I am building and evaluating a two-level governance architecture for AI decision support where classified environmental safety state controls both *whether* AI participates and *what* it is permitted to recommend, applied to small-scale coastal fisheries in Malaysia.

## The one idea that makes this research novel

Every existing safety-critical AI system either fully enables or fully blocks AI. My architecture adds a third mode — CAUTION — where AI continues operating within a formally restricted advisory scope because environmental conditions are elevated but not yet prohibitive. The same classified environmental state governs both the participation gate G(S) and the admissible recommendation space A_AI(S), with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

---

## Abstract

Existing safety-critical AI decision-support architectures govern AI behaviour through a binary mechanism: AI is either fully enabled or completely blocked, leaving no formally defined intermediate mode for conditions of elevated but non-prohibitive risk. Across eight bodies of literature, no architecture unifies participation governance (whether AI may act) and advisory scope governance (what AI may recommend) under the same classified environmental state, and consequently the CAUTION mode, where AI operates within a restricted recommendation space because environmental conditions are dangerous but not yet prohibitive, does not exist.

This research proposes, formalises, and evaluates a **Graduated Safety-State-Gated Architecture** that introduces a three-mode governance structure conditioned on an environmental safety state S = f(E), where E is a vector of observable risk parameters. The architecture defines a participation gate G(S) and an admissible recommendation space A_AI(S) with the formal containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

The study follows Design Science Research, including formal specification, prototype implementation for coastal fisheries in Malaysia, comparative evaluation against binary baselines, and a user study with fishers and fisheries officers.

---

## Proposed Architecture

![Graduated Safety-State-Gated Architecture](docs/images/architecture/proposed_diagram.png)

The architecture operates as a four-layer pipeline:

1. **Environmental Input Layer** — Observes six real-time parameters: wind speed (w), rainfall intensity (r), sea state (m), official marine warning level (o), vessel category (v), and time of day (t), forming E = {w, r, m, o, v, t}.

2. **Deterministic Safety Classification Layer** — Classifies each parameter against predefined thresholds and applies worst-case aggregation to produce S ∈ {SAFE, CAUTION, UNSAFE}. Purely rule-based, no AI.

3. **AI Advisory Layer** — A rule-based engine configured by the governance layer before reasoning begins. The governance layer supplies a rule set RS(S) to the engine: RS(SAFE) contains rules producing {Go, Delay, DepartureTime, Duration}; RS(CAUTION) contains rules producing only {Go, Delay}; RS(UNSAFE) is empty (never passed — G(UNSAFE) = 0). The engine fires only rules in its active RS(S), so recommendations outside A_AI(S) cannot be generated. The Safety Dominance Property AI(E) ⊆ A_AI(S) holds by construction, not by runtime filtering.

4. **Human Decision Layer** — The fisher receives the recommendation (or safety alert under UNSAFE) and makes the final departure decision. Human authority is retained in all three states.

**Three key safety properties:**

- **Non-compensatory aggregation** — A single UNSAFE parameter makes the entire state UNSAFE.
- **Graduated containment** — Under CAUTION, AI provides directional guidance only (Go/Delay). Precision recommendations (DepartureTime/Duration) are removed.
- **Deterministic override** — The Safety Dominance Property AI(E) ⊆ A_AI(S) holds for all E, proved by construction via RS(S). See [`docs/justification-layer3-enforcement.md`](docs/justification-layer3-enforcement.md) for the full proof.

For the full illustrated explanation, see [architecture-illustration.md](docs/architecture-illustration.md).

---

## Problem Statements

The following five problems (PS1–PS5) are identified from the literature. For each, the corresponding **research gap** and the **research objective** that addresses it are stated.

---

### PS1. Absence of an intermediate participation mode

**Problem:**  
Existing safety-critical AI architectures implement binary governance — AI is either fully enabled or fully blocked. No architecture formally defines an intermediate participation mode where AI operates under a restricted recommendation space calibrated to classified environmental risk level.

**Gap:**  
Existing guardrail systems (Könighofer et al., 2025; Liang et al., 2025; Abella et al., 2025) and governance architectures (Wang et al., 2026; Shamsujjoha et al., 2025) treat AI participation as binary. Only Flehmig et al. (2024) implement graduated governance, but the trigger is AI performance degradation — not environmental safety state — and it governs monitoring intensity, not the AI-admissible recommendation space. No architecture formally models a CAUTION mode with a restricted AI recommendation space.

**Objective (O1):**  
To design a three-mode hybrid AI decision architecture in which AI participation is graduated (enabled / restricted / disabled) based on classified environmental safety state, ensuring that AI recommendation scope narrows as operational risk increases.

---

### PS2. Governance triggered by AI performance, not environmental state

**Problem:**  
Where graduated AI governance has been attempted (Flehmig et al., 2024), it is triggered by AI model performance degradation, not by the safety state of the operational environment. No existing architecture conditions participation or advisory scope on classified environmental conditions.

**Gap:**  
Where graduated governance has been attempted, the trigger is AI model performance degradation — not environmental safety state. No architecture conditions participation or advisory scope on classified environmental conditions. Flehmig et al.'s traffic-light model governs monitoring intensity; Li et al.'s (2026) dynamic threshold operates within a single agent. Neither formally restricts AI recommendation content per environmental safety state.

**Objective (O2):**  
To formally define the environmental state vector **E**, safety state function S = f(E), participation gate function G(S), and AI-admissible recommendation space A_AI(S) with the property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅, resulting in a two-level governance architecture of participation governance and advisory scope governance, including domain-specific operationalisation of safety thresholds for coastal fisheries.

---

### PS3. No design for low-resource environments

**Problem:**  
Safety-critical AI governance architectures have not been designed for or evaluated in low-resource environments where data may be incomplete, connectivity is intermittent, and users have limited digital literacy. Existing fisheries AI platforms provide forecasts and alerts but do not formally govern how AI participation should be constrained under varying environmental risk.

**Gap:**  
Formal safety governance has not been integrated with low-resource deployment constraints. Bhuvaneswari et al. address hybrid AI in resource-constrained emergency medicine but without formal governance architecture. Domain papers confirm the absence of formal safety-state-gated AI in fisheries: Haque and Al Jufaili (2026) review AI across four fisheries application domains and find that no system implements formal participation governance or advisory scope restriction conditioned on environmental safety state.

**Objective (O3):**  
To implement a functional prototype decision-support system based on the proposed three-mode architecture, designed for the constraints of small-scale coastal fisheries (offline capability, limited data, small-vessel hardware/mobile).

---

### PS4. No comparative evaluation of graduated vs. binary governance

**Problem:**  
Existing evaluations of safety-critical AI architectures compare gated systems against ungated baselines but do not assess whether graduated two-level governance (participation gate + advisory scope restriction) produces safer outcomes than simpler binary governance (participation gate only). The added value of the CAUTION mode — where G(S) = 1 but A_AI(S) is restricted — has not been empirically tested.

**Gap:**  
No comparative evaluation exists between graduated two-level governance and binary single-level governance. Current baselines compare gated versus ungated only. No evaluation isolates the contribution of Level 2 (advisory scope governance) beyond Level 1 (participation governance).

**Objective (O4):**  
To evaluate the architecture's safety compliance, decision consistency, and comparative performance against:

- **(a)** a binary-gated baseline (C1) that implements Level 1 only — participation gate G(S) with full advisory scope regardless of safety state, analogous to shield-based systems (e.g., Könighofer et al., 2025)
- **(b)** an ungated baseline (C0) — no governance, AI outputs full recommendation set across all safety states

using scenario-based three-condition comparative analysis (C0 vs C1 vs C2), with Safety Dominance Property compliance as the primary metric. The discriminating condition is CAUTION: C1 and C2 are identical at Level 1 under CAUTION (G(S) = 1 for both), so any difference in recommendation output is attributable entirely to Level 2 governance. See [`docs/evaluation-design-rq4.md`](docs/evaluation-design-rq4.md) for the full evaluation design.

---

### PS5. No contextual validation of graduated governance with real users

**Problem:**  
No study has examined how users perceive, understand, and respond to a graduated AI participation model — where the system communicates that AI is not merely on or off, but operating under a formally restricted advisory scope. The CAUTION mode in particular introduces a new interaction pattern that has no precedent in existing systems.

**Gap:**  
No contextual validation exists of graduated AI governance architectures, particularly whether users correctly perceive the safety state, understand why AI advisory scope is restricted under CAUTION, and make different decisions across the three governance modes.

**Objective (O5):**  
To validate that the architecture functions as intended with the population it was designed for — specifically, whether fishers correctly identify the current safety state (Q1), correctly understand why AI is restricted under CAUTION as a scope limitation rather than a display change (Q2), and make different decisions under CAUTION than under SAFE and UNSAFE (Q3). See [`docs/rq5-study-design.md`](docs/rq5-study-design.md) for the full study design.


For full traceability across PS → Gap → RQ → Objective → Methodology, see the [Research Alignment Table](docs/research-alignment-table.md).

---

## Novelty

The architecture's core contribution is captured by the formal pipeline:

**`E → S = f(E) → (G(S), A_AI(S)) → AI(E)`**

Read step by step:

- **E** — Observe the environment: wind speed, rainfall intensity, sea state, official marine warning level, vessel category, and time of day.
- **S = f(E)** — Classify those observations into a safety state — SAFE, CAUTION, or UNSAFE — using worst-case aggregation across all parameters.
- **(G(S), A_AI(S))** — The safety state sets two governance rules: whether the AI is permitted to operate at all (G(S)), and what types of recommendation it is permitted to give (A_AI(S)).
- **AI(E)** — The AI generates recommendations, but only within the space those governance rules define.

The proposed architecture is the first unified two-level governance architecture for safety-critical AI that:

1. **Unifies Level 1 and Level 2 governance** under the same classified environmental state
2. **Formalises the CAUTION mode** as a distinct operational state with restricted advisory scope
3. **Conditions on environmental state, not AI performance** — unlike Flehmig et al. (2024) or Baxi (2026)
4. **Proves the Safety Dominance Property by construction** — AI(E) ⊆ A_AI(S) for all environmental states, enforced by the rule set RS(S) supplied to Layer 3 before reasoning begins — not by runtime filtering
5. **Designs for low-resource deployment** — S = f(E) executes in constant time with negligible memory, satisfying TinyML constraints

The gap is confirmed independently across 91 collaborative intelligence papers (Ramos et al., 2024), 46 formal methods studies (Newcomb & Ochoa, 2026), 11 international AI safety frameworks (Bengio et al., 2026), and the cross-domain safety-critical AI survey (Perez-Cerrolaza et al., 2024).

For the full novelty argument, see [justification-novelty-gap.md](docs/justification-novelty-gap.md).

---

## Key Design Documents

| Document | Purpose |
|---|---|
| [`docs/justification-layer3-enforcement.md`](docs/justification-layer3-enforcement.md) | Layer 3 rule-based engine decision, RS(S) enforcement mechanism, and proof by construction of Safety Dominance Property |
| [`docs/evaluation-design-rq4.md`](docs/evaluation-design-rq4.md) | RQ4 three-condition comparative evaluation — scenarios, metrics, C0/C1/C2 design |
| [`docs/rq5-study-design.md`](docs/rq5-study-design.md) | RQ5 contextual validation study — three questions, instrument, participants, scope |
| [`docs/appendix-c-formalisation.md`](docs/appendix-c-formalisation.md) | Full formal model — E, S = f(E), G(S), A_AI(S), RS(S), Safety Dominance Property proof |
| [`docs/architecture-illustration.md`](docs/architecture-illustration.md) | Architecture walkthrough — layers, governance table, scenario, limitations |
| [`docs/research-improvement-plan.md`](docs/research-improvement-plan.md) | Six-step improvement plan (25 April 2026) — all steps completed |
| [`docs/justification-environmental-state-governance.md`](docs/justification-environmental-state-governance.md) | Why governance is conditioned on environmental safety state rather than AI confidence, risk score, or performance |
| [`docs/justification-safety-state-design.md`](docs/justification-safety-state-design.md) | Safety state naming, boundary definitions, thresholds, dynamics, misclassification, and domain-specificity |
| [`docs/justification-rainfall-intensity-mapping.md`](docs/justification-rainfall-intensity-mapping.md) | Rainfall intensity mapping from ERA5 mm/hr to ordinal categorical r via JPS/DID thresholds |
| [`docs/data-source-met-malaysia.md`](docs/data-source-met-malaysia.md) | MET Malaysia data acquisition — environmental variables, coverage, and operationalisation for f(E) |
| [`docs/dataset-label-derivation.md`](docs/dataset-label-derivation.md) | Advisory AI training label derivation from empirical fisher studies |

---

## References

The corpus contains 63 papers. For the full citation-to-notes mapping, see [citation-notes-map.md](docs/citation-notes-map.md).
