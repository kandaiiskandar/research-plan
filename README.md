# A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries

**PhD Research Repository**

**Author:** Mohd Iskandar Samsuddin  
**Institution:** Universiti Malaysia Sabah (UMS)  
**Field:** Computer Science / Artificial Intelligence

---

## One sentence summary

I am building and evaluating a two-level governance architecture for AI decision support where classified environmental safety state controls both *whether* AI participates and *what* it is permitted to recommend, applied to small-scale coastal fisheries in Malaysia.

## The one idea that makes this research novel

Every existing safety-critical AI system either fully enables or fully blocks AI. My architecture adds a third mode — CAUTION — where AI continues operating within a formally restricted advisory scope because environmental conditions are elevated but not yet prohibitive. The same classified environmental state governs both the participation gate G(S) and the admissible recommendation space A_AI(S), with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

---

## Abstract

Existing safety-critical AI decision-support architectures govern AI behaviour through a binary mechanism—AI is either fully enabled or completely blocked—leaving no formally defined intermediate mode for conditions of elevated but non-prohibitive risk. Across eight bodies of literature (AI decision support, safety gating, human-AI authority, adaptive autonomy, guardrails, hybrid AI, low-resource systems, and fisheries decision context), no architecture unifies participation governance (whether AI may act) and advisory scope governance (what AI may recommend) under the same classified environmental state, and consequently the CAUTION mode—where AI operates within a restricted recommendation space because environmental conditions are dangerous but not yet prohibitive—does not exist. This research proposes, formalises, and evaluates a **Graduated Safety-State-Gated Architecture** that introduces a three-mode governance structure conditioned on an environmental safety state S = f(E), where E is a vector of observable risk parameters. The architecture defines a participation gate G(S) and an admissible recommendation space A_AI(S) with the formal containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The study follows Design Science Research, including formal specification, prototype implementation for coastal fisheries in Malaysia, comparative evaluation against binary baselines, and a user study with fishers and fisheries officers. The primary contribution is the first unified two-level governance architecture for safety-critical AI that formalises the CAUTION mode as a distinct operational state, with technical, empirical, and socio-technical evidence on whether graduated governance produces safer and more usable outcomes than binary governance in low-resource environments.

---

## Proposed Architecture

![Graduated Safety-State-Gated Architecture](docs/images/architecture/proposed_diagram.png)

The architecture operates as a four-layer pipeline that processes environmental conditions into safety-governed AI recommendations:

1. **Environmental Input Layer** — Observes six real-time parameters: wind speed (w), rainfall intensity (r), sea state (m), official marine warning level (o), vessel category (v), and time of day (t), forming the environmental state vector E = {w, r, m, o, v, t}.

2. **Deterministic Safety Classification Layer** — Classifies each parameter against predefined thresholds and applies worst-case (max-severity) aggregation to produce a single safety state S ∈ {SAFE, CAUTION, UNSAFE}. This layer is purely rule-based — no AI, no learning, no probability.

3. **AI Advisory Layer** — Generates recommendations within the scope permitted by the safety state. The two-level governance pair (G(S), A_AI(S)) controls both *whether* AI participates and *what* it is allowed to recommend, with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

4. **Human Decision Layer** — The fisher receives the AI recommendation (or safety alert under UNSAFE) and makes the final departure decision. The human always retains ultimate decision authority in all three safety states.

**Three key safety properties:**

- **Non-compensatory aggregation** — Favourable conditions on one parameter cannot offset danger on another. A single UNSAFE parameter makes the entire state UNSAFE.
- **Graduated containment** — Under CAUTION, AI continues operating but can only provide directional guidance (Go/Delay). Precision recommendations (DepartureTime/Duration) are removed because their reliability degrades under adverse conditions.
- **Deterministic override** — The Safety Dominance Property guarantees that AI can never generate recommendations outside the scope permitted by the deterministic safety classification: AI(E) ⊆ A_AI(S) for all E.

For the full illustrated explanation, see [`docs/architecture-illustration.md`](docs/architecture-illustration.md).

---

## Problem Statement

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

### PS3. No design for low‑resource environments

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

- **(a)** a binary-gated baseline that implements Level 1 only (participation gate \( G(S) \) with full advisory scope, analogous to shield-based systems in Section 2.2, e.g., Könighofer et al., 2025)
- **(b)** an ungated AI advisory baseline (no governance)

using scenario-based testing.

---

### PS5. No empirical or socio‑technical evaluation of graduated governance

**Problem:**  
Socio-technical evaluation of AI governance architectures in safety-critical low-resource environments remains limited. No study has examined how users understand, trust, and respond to a graduated AI participation model — where the system communicates that AI is not merely on or off, but operating under restriction.

**Gap:**  
No socio-technical evaluation exists of graduated AI governance architectures, particularly user response to the CAUTION mode (G(S) = 1 but A_AI restricted) as distinct from SAFE (G(S) = 1, full A_AI) and UNSAFE (G(S) = 0, A_AI = ∅).

**Objective (O5):**  
To evaluate user understanding of safety states, trust calibration, and decision behaviour across all three modes, with particular attention to how users interpret and respond to the CAUTION state where AI participates within a restricted recommendation space \( A_{\text{AI}}(\text{CAUTION}) \subset A_{\text{AI}}(\text{SAFE}) \).


For full traceability across PS → Gap → RQ → Objective → Methodology, see the [Research Alignment Table](docs/research-alignment-table.md).

---

## Literature Review

The full literature review is available here: [`docs/chapter-2-draft.md`](docs/chapter-2-draft.md).

It is organised into the following sections:

- [**2.1** AI Decision Support in Safety-Critical Systems](docs/chapter-2-draft.md#21-ai-decision-support-in-safety-critical-systems)
- [**2.2** Deterministic Safety Constraints and Safety Gating (Level 1 Governance)](docs/chapter-2-draft.md#22-deterministic-safety-constraints-and-safety-gating)
- [**2.3** Human–AI Decision Authority](docs/chapter-2-draft.md#23-humanai-decision-authority)
- [**2.4** Adaptive Autonomy and Risk-Based Systems](docs/chapter-2-draft.md#24-adaptive-autonomy-and-risk-based-systems)
- [**2.5** AI Governance and Guardrails (Level 2 Governance)](docs/chapter-2-draft.md#25-ai-governance-and-guardrails)
- [**2.6** Hybrid AI Systems](docs/chapter-2-draft.md#26-hybrid-ai-systems)
- [**2.7** AI in Low-Resource Environments](docs/chapter-2-draft.md#27-ai-in-low-resource-environments)
- [**2.8** The Fisheries Decision Context](docs/chapter-2-draft.md#28-fisheries-decision-context)
- [**2.9** Comparative Analysis (Table 2.1: 15 comparator systems)](docs/chapter-2-draft.md#29-comparative-analysis)
- [**2.10** Literature Summary](docs/chapter-2-draft.md#210-literature-summary)
- [**2.11** Research Gap](docs/chapter-2-draft.md#211-research-gap)

**Key findings from the literature review:**

- Binary governance is consistent across **91** collaborative intelligence papers (Ramos et al., 2024), **46** formal methods studies (Newcomb & Ochoa, 2026), **11** frontier AI safety frameworks (Bengio et al., 2026), and the cross-domain safety-critical AI survey (Perez-Cerrolaza et al., 2024).
- No architecture unifies participation governance G(S) and advisory scope governance A_AI(S) under the same classified environmental state. The CAUTION mode — where AI participates within a restricted recommendation space — does not exist.
- The gap is structural — present at the technical, formal methods, and institutional governance layers simultaneously.
- In low-resource environments, binary governance is asymmetrically costly: blocking AI under moderate risk transfers the decision burden to operators who lack institutional alternatives.

---

## Formalisation

The complete mathematical formalisation of the proposed architecture is provided in [`docs/appendix-c-formalisation.md`](docs/appendix-c-formalisation.md).

Key definitions: environmental state vector **E = {w, r, m, o, v, t}**, safety state function **S = f(E)**, participation gate **G(S)**, admissible recommendation space **A_AI(S)**, and the full governance pipeline **E → S = f(E) → (G(S), A_AI(S)) → AI(E)**.

---

## Novelty

The proposed architecture is the first unified two-level governance architecture for safety-critical AI that:

1. **Unifies Level 1 and Level 2 governance** — no prior work implements both participation governance G(S) and advisory scope governance A_AI(S) under the same classified environmental state
2. **Formalises the CAUTION mode** — the intermediate operational state where AI participates within a restricted recommendation space because conditions are elevated but not prohibitive
3. **Conditions on environmental state, not AI performance** — unlike Flehmig et al. (2024) who trigger on AI degradation, or Baxi (2026) who conditions on agent robustness, this architecture triggers on observable environmental conditions
4. **Proves the Safety Dominance Property** — AI(E) ⊆ A_AI(S) for all environmental states, guaranteeing that what AI produces is always within the permitted recommendation space
5. **Designs for low-resource deployment** — the governance layer S = f(E) executes in constant time with negligible memory (threshold comparisons on six parameters), satisfying TinyML constraints for edge deployment on small-vessel hardware / mobile apps

The gap is confirmed independently across 91 collaborative intelligence papers (Ramos et al., 2024), 46 formal methods studies (Newcomb & Ochoa, 2026), 11 international AI safety frameworks (Bengio et al., 2026), and the cross-domain safety-critical AI survey (Perez-Cerrolaza et al., 2024). The structurally closest prior work (Baxi, 2026) implements graduated governance but conditions on agent robustness rather than environmental state — making the two architectures complementary, not competing.

For the full novelty argument, see [`docs/justification-novelty-gap.md`](docs/justification-novelty-gap.md).

---

## References

The corpus contains 63 papers. For the full citation-to-notes mapping, see [`docs/citation-notes-map.md`](docs/citation-notes-map.md).
