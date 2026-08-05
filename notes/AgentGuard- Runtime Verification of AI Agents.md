# Literature Review Extraction (Reduced)
## Paper: AgentGuard: Runtime Verification of AI Agents

---

## 1. Paper Identity

- **Full title:** AgentGuard: Runtime Verification of AI Agents
- **Author:** Roham Koohestani
- **Affiliation:** JetBrains Research, The Netherlands
- **Year:** 2025
- **Venue:** 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW), pp. 75– . doi: 10.1109/ASEW67777.2025.00023
- **Type:** Workshop paper — proof-of-concept framework, single author, demonstrated on one system (RepairAgent)
- **Extraction category:** Reduced extraction — governance-adjacent (runtime verification family, alongside AgentSpec, GAVEL, shields)

---

## 2. Core Contribution

- **Problem:** Agentic AI systems built on stochastic LLMs are nondeterministic with emergent behaviour; static/offline verification provides only a pre-deployment snapshot that real-world interaction can invalidate. The verification question becomes probabilistic: not *whether* the system fails but *with what probability under given constraints*.
- **Proposal — Dynamic Probabilistic Assurance:** AgentGuard operates as an inspection layer that (i) observes the agent's raw I/O and abstracts it into formal events corresponding to transitions in a state model, (ii) uses online learning to dynamically build and update a Markov Decision Process (an "Agentic MDP") modelling the agent's emergent behaviour from execution traces, and (iii) applies probabilistic model checking (PCTL properties) to verify quantitative properties in real time. A dashboard presents the quantitative guarantees and **triggers alerts or automated responses if a safety threshold is crossed**.
- **Demonstration:** Integrated into RepairAgent (an LLM-based program repair agent) as proof-of-concept; roadmap for future work.

**Key quote (Abstract):** *"AgentGuard operates as an inspection layer that observes an agent's raw I/O and abstracts it into formal events corresponding to transitions in a state model... using probabilistic model checking, the framework then verifies quantitative properties in real-time."*

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Safety-critical AI decision-making | **Partial** | Quantitative runtime assurance for agentic AI; demonstrated on software repair, not safety-critical operations |
| AI governance / control mechanisms | **Partial** | Runtime verification with threshold-triggered alerts/automated responses — the monitoring half of governance; the intervention itself is not graduated |
| Pre-generation advisory scope restriction | No | Verifies observed execution behaviour; no concept of restricting recommendation scope |
| Environmental state classification | No | State model abstracts the *agent's* behaviour (Agentic MDP states are snapshots of the agent's workflow), not the operator's environment |
| Decision architecture formalisation | **Partial** | Formal MDP + PCTL machinery, but applied to behaviour modelling, not governance structure |
| Human role in decision-making | No | Dashboard for observability; no human decision-support framing |
| Low-resource environments / fisheries | No | Datacentre agentic systems |

**Extraction decision:** Reduced extraction. Belongs to the runtime verification / agent guardrail family already in the corpus (AgentSpec, GAVEL, shields) as its most recent, probabilistic-quantitative member.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- The most recent evidence that state-of-the-art runtime verification governs **execution behaviour, not advisory scope**: AgentGuard's entire object of verification is what the agent *does* (I/O events, workflow state transitions), and its governance action is threshold-triggered alerts or automated responses. Nothing conditions, or contracts, what an AI may *recommend to a human*.
- A useful pre-emptive distinction for reviewers: AgentGuard's assurance is **continuous and quantitative** (failure probabilities updated online), which superficially resembles graduation — but the continuity lies in the *measurement*, not the *governance response*. When a threshold is crossed, the response is an alert or automated intervention, not a formally enumerated intermediate advisory mode. Graduated measurement ≠ graduated governance.
- Reinforces the §4.6 misalignment finding: like Baxi, Flehmig, Kang, Sahoo, and Ghaleb, AgentGuard conditions its governance signal on properties **internal to the AI system** (the learned model of the agent's own behaviour), not on an independently classified environmental state.

**What this paper CANNOT be cited for (overreach guard):**

- It is a **single-author workshop proof-of-concept** demonstrated on one software-engineering agent — cite as an indicator of where the runtime verification frontier is heading, not as an established framework; do not weight it equally with Könighofer's shields or the large surveys.
- It does not claim to address decision support or advisory settings at all, so its omission of advisory scope is corroborating (one more member of the pattern), not independently probative — the gap argument continues to rest on the four-layer structure.
- Despite the user-facing dashboard, it is not a human-in-the-loop governance framework; do not place it in the authority-allocation paradigm.

---

## 5. Positioning for This Research

**Positioning paragraph:** Koohestani (2025) represents the current frontier of the runtime verification line: AgentGuard replaces static pre-deployment verification with Dynamic Probabilistic Assurance, observing an agent's I/O, abstracting it into formal events, learning a Markov Decision Process of the agent's emergent behaviour online, and verifying quantitative PCTL properties in real time, with alerts or automated responses triggered when safety thresholds are crossed. Two features of this most recent design confirm the pattern documented across the runtime assurance literature. First, the object of governance remains execution behaviour — what the agent does — with no concept of restricting what an AI may recommend to a human decision-maker. Second, although its assurance signal is continuous and quantitative, the governance response remains threshold-triggered intervention: the continuity lies in measurement, not in a graduated advisory response, and the signal is derived from a model of the agent's own behaviour rather than from an independently classified environmental state. Even at its probabilistic, dynamically learned frontier, runtime verification thus leaves the advisory scope dimension unaddressed.

---

## 6. Overall Relevance Score

### ⭐⭐ Low–Medium (governance-adjacent, reduced)

**Justification:** A current (2025) datapoint extending the runtime verification family the corpus already covers, valuable for two specific argumentative moves: freshest confirmation that verification targets execution rather than advisory scope, and the measurement-vs-response distinction that pre-empts a "quantitative assurance is already graduated" objection. Workshop-level maturity limits its weight. Best cited in the deterministic safety constraints / runtime assurance discussion (conference paper §4.2 or synthesis §4.6) in a single sentence; also usable in the thesis Chapter 2 runtime verification subsection alongside AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) and GAVEL [[notes]](../notes/GAVEL-%20Rule-Based%20Activation-Level%20Safety%20for%20AI%20Systems.md).
