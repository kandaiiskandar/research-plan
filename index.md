---
layout: document
title: Research Plan
---

# A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments

**PhD Research Repository**

**Author:** Mohd Iskandar Samsuddin
**Institution:** Universiti Malaysia Sabah (UMS)
**Field:** Computer Science / Artificial Intelligence

I am building and evaluating a two-level governance architecture for AI decision support where classified environmental safety state controls both *whether* AI participates and *what* it is permitted to recommend, applied to small-scale coastal fisheries in Malaysia.

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

3. **AI Advisory Layer** — Generates recommendations within the scope permitted by the safety state. The governance pair (G(S), A_AI(S)) controls both participation and advisory scope, with containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

4. **Human Decision Layer** — The fisher receives the recommendation (or safety alert under UNSAFE) and makes the final departure decision. Human authority is retained in all three states.

**Three key safety properties:**

- **Non-compensatory aggregation** — A single UNSAFE parameter makes the entire state UNSAFE.
- **Graduated containment** — Under CAUTION, AI provides directional guidance only (Go/Delay). Precision recommendations (DepartureTime/Duration) are removed.
- **Deterministic override** — The Safety Dominance Property guarantees AI(E) ⊆ A_AI(S) for all E.

For the full illustrated explanation, see [architecture-illustration.md](docs/architecture-illustration.md).

---

## Problem Statements

### PS1. Absence of an intermediate participation mode

No architecture formally defines an intermediate mode where AI operates under a restricted recommendation space calibrated to classified environmental risk.

**Objective (O1):** Design a three-mode architecture where AI participation is graduated (enabled / restricted / disabled) based on classified environmental safety state.

### PS2. Governance triggered by AI performance, not environmental state

Where graduated governance has been attempted, the trigger is AI model performance degradation, not environmental safety state.

**Objective (O2):** Formally define E, S = f(E), G(S), and A_AI(S) with the containment property, including domain-specific thresholds for coastal fisheries.

### PS3. No design for low-resource environments

Safety-critical AI governance architectures have not been designed for environments with incomplete data, intermittent connectivity, and limited digital literacy.

**Objective (O3):** Implement a functional prototype for the constraints of small-scale coastal fisheries (offline capability, limited data, mobile deployment).

### PS4. No comparative evaluation of graduated vs. binary governance

No evaluation isolates the contribution of Level 2 (advisory scope) beyond Level 1 (participation gate).

**Objective (O4):** Evaluate safety compliance, decision consistency, and comparative performance against binary-gated and ungated baselines.

### PS5. No socio-technical evaluation of graduated governance

No study examines user response to the CAUTION mode as a distinct operational state.

**Objective (O5):** Evaluate user understanding, trust calibration, and decision behaviour across all three safety modes.

For full traceability, see [Research Alignment Table](docs/research-alignment-table.md).

---

## Novelty

The proposed architecture is the first unified two-level governance architecture for safety-critical AI that:

1. **Unifies Level 1 and Level 2 governance** under the same classified environmental state
2. **Formalises the CAUTION mode** as a distinct operational state with restricted advisory scope
3. **Conditions on environmental state, not AI performance** — unlike Flehmig et al. (2024) or Baxi (2026)
4. **Proves the Safety Dominance Property** — AI(E) ⊆ A_AI(S) for all environmental states
5. **Designs for low-resource deployment** — S = f(E) executes in constant time with negligible memory, satisfying TinyML constraints

The gap is confirmed independently across 91 collaborative intelligence papers (Ramos et al., 2024), 46 formal methods studies (Newcomb & Ochoa, 2026), 11 international AI safety frameworks (Bengio et al., 2026), and the cross-domain safety-critical AI survey (Perez-Cerrolaza et al., 2024).

For the full novelty argument, see [justification-novelty-gap.md](docs/justification-novelty-gap.md).

---

## References

The corpus contains 63 papers. For the full citation-to-notes mapping, see [citation-notes-map.md](docs/citation-notes-map.md).
