# Literature Review Extraction (Reduced)
## Paper: From Linear Risk to Emergent Harm: Complexity as the Missing Core of AI Governance

---

## 1. Paper Identity

- **Full title:** From Linear Risk to Emergent Harm: Complexity as the Missing Core of AI Governance
- **Author:** Hugo Roger Paz
- **Affiliation:** Faculty of Exact Sciences and Technology, National University of Tucumán (UNT), Argentina
- **Year:** 2025 (14 December 2025)
- **Venue:** White Paper / Policy Brief (Working Paper) — Zenodo, doi: 10.5281/zenodo.17929014; also arXiv:2512.12707 — **not peer-reviewed**
- **Type:** Conceptual/policy argument — no empirical data, no formal model, no architecture
- **Extraction category:** External evidence (policy-layer critique of static risk-based governance — weakest evidentiary tier in the external set)

---

## 2. Core Contribution

- **Argument:** Risk-based AI regulation (the dominant paradigm) fails for structural reasons: it *"implicitly assume[s] linear causality, stable system boundaries, and largely predictable responses to regulation."* In practice AI operates within **complex adaptive socio-technical systems** where harm is *"emergent, delayed, redistributed, and amplified through feedback loops and strategic adaptation by system actors."* Consequently, compliance can rise while harm is displaced or concealed.
- **Diagnosis of static classification:** risk categories are assigned to systems as if they were stable artefacts, but the system is moving — classification decays as behaviour, context, and actors adapt (§3.2 "Risk classification in a moving system").
- **Proposal:** a complexity-based framework with three principles — regulation as *intervention* rather than control, *dynamic system mapping* over static classification, and *learning* (causal reasoning, simulation, adaptive evaluation) over static compliance.

**Key quote (Abstract):** *"such frameworks often fail for structural reasons: they implicitly assume linear causality, stable system boundaries, and largely predictable responses to regulation. In practice, AI operates within complex adaptive socio-technical systems in which harm is frequently emergent, delayed, redistributed, and amplified through feedback loops."*

---

## 3. Relevance to My Research

Governance theme, at the **policy/conceptual layer**. Provides a critique-side argument that static, categorical, design-time governance is structurally mismatched to systems whose risk context changes dynamically — supporting the motivation for governance that responds to *current* conditions at runtime. The over-reliance failure mode the thesis cites (operators accepting full-scope AI output under deteriorating conditions) can be characterised in this vocabulary: the harm is not a direct design defect but an emergent effect of the human-AI feedback loop under a static governance regime.

**Extraction decision:** Reduced extraction, external evidence.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- Policy-layer support for the claim that **static classification and design-time risk tiers are structurally insufficient** when the operative risk context is dynamic — motivating runtime, state-conditioned governance. Pairs naturally with Engin & Hand (2025) [[notes]](../notes/Towards%20Adaptive%20Categories-%20Dimensional%20Governance%20for%20Agentic%20AI.md): Engin & Hand supply the constructive proposal (categories over monitored dimensions), Paz supplies the critique (why static categories fail).
- Framing the over-reliance harm as **emergent in the socio-technical loop** rather than a direct design failure: a binary gate that treats marginal conditions as structurally safe does not itself produce harm — harm emerges from the interaction of full-scope advice, operator trust, and deteriorating conditions. Useful vocabulary for the RQ5 discussion.

**What this paper CANNOT be cited for (overreach guard):**

- It is an **unreviewed single-author white paper** — the weakest source in the external evidence set. Never load-bearing; cite only alongside peer-reviewed support (Engin & Hand, Reuel et al.), or omit if reference count is tight.
- It contains **no architecture, no formal model, no runtime mechanism** — not a comparator, and no advisory scope concept.
- The claim that the intermediate-risk gap "is a perfect example of non-linear failure" is an interpretive stretch. The advisory scope gap is a **granularity problem in governance design**, established by the four-layer gap argument; complexity theory is at most a framing for the *consequences* of the gap (emergent over-reliance harm), not evidence for the gap itself. Do not rest the gap argument on complexity vocabulary.
- **Project positioning caution:** this paper's complex-adaptive-socio-technical framing belongs to the socio-technical strand that project rules confine to RQ5 discussion. Do not import it into Chapter 2, the methodology, or the primary CS framing of the thesis.

---

## 5. Positioning for This Research

**Positioning paragraph:** Paz (2025), in a policy white paper, argues that risk-based AI governance fails structurally because it assumes linear causality and stable system boundaries, whereas AI operates in complex adaptive socio-technical systems where harm is emergent, delayed, and amplified through feedback loops — and that governance should therefore prioritise dynamic system state over static classification. At the runtime-architecture level, the proposed architecture responds to precisely this critique: rather than assigning the AI decision-support system a fixed design-time risk tier, it conditions governance continuously on the classified current environmental state S = f(E), contracting the admissible advisory space A_AI(S) as conditions deteriorate. The over-reliance failure mode of binary gating — operators accepting full-scope recommendations in marginal conditions the data can no longer support — is an instance of the emergent, feedback-mediated harm Paz describes: it arises not from any single design defect but from the interaction of static governance, AI output, and human trust under changing conditions.

---

## 6. Overall Relevance Score

### ⭐ Low (external evidence, unreviewed)

**Justification:** Conceptually aligned but evidentially weak: an unreviewed working paper at the policy layer with no formal or empirical content. Use as colour alongside Engin & Hand (2025) and Reuel et al. (2025) in motivation or RQ5 discussion — the critique of static classification and the emergent-harm vocabulary — never as standalone support, never in the architectural gap argument, and never as a primary socio-technical framework (project positioning rule).
