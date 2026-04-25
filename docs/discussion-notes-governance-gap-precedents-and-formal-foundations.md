# Discussion Notes — The Governance Gap, Precedents, and Formal Foundations

**Date**: 24 April 2026  
**Purpose**: Personal study notes, supervisor reference, and viva preparation  
**Topics covered**: The problem and gap in existing governance architectures; Indykov et al. (2025) on architectural tactics; Dalrymple et al. (2024) on Guaranteed Safe AI; Flehmig et al. (2024) on traffic-light degradation indexing  
**Cross-references**: For the formal architecture, see `docs/appendix-c-formalisation.md`. For the full architectural comparison, see `docs/justification-architectural-comparison.md`.

---

## 1. The Problem and the Gap

### In plain language

Imagine a fishing vessel AI that helps a fisher decide whether to go to sea. The AI looks at the weather, ocean conditions, and other factors, and then gives advice — for example, "it is safe to depart at 6am" or "delay your trip."

Now imagine the weather is getting dangerous — not fully dangerous, but in a warning zone. Under this condition, the AI should probably not be giving departure time recommendations, because those recommendations depend on data that is now unreliable. The AI's confidence in its departure time prediction is no longer valid.

The problem is: **existing AI architectures do not know how to handle this middle ground**. They have two settings — either the AI is fully on (giving all its advice) or fully off (blocked completely). There is no in-between where the AI still helps but only gives the advice it can reliably give.

This is the binary governance problem. The existing architectures implement:

**G(S) → {participate, block}**

When G(S) = 1 (participate), the AI generates the same full set of recommendations regardless of whether conditions are SAFE or CAUTION. The human decision-maker sees confident-looking advice without knowing the AI is advising beyond its reliable range.

### The formal gap

No existing architecture in the reviewed literature formally specifies **pre-generation advisory scope restriction** — a mechanism that restricts which *categories* of recommendation the AI is permitted to generate, based on classified environmental safety state.

The proposed architecture addresses this by introducing a second level of governance:

- **Level 1 — Participation gate**: G(S) — does the AI operate at all?
- **Level 2 — Advisory scope**: A_AI(S) — what is the AI permitted to recommend?

Together these form the **governance pair (G(S), A_AI(S))**, governed by the classified environmental safety state S = f(E).

The result is a **graduated containment hierarchy**:

```
A_AI(SAFE)    = {Go, Delay, DepartureTime, Duration}   ← full scope
A_AI(CAUTION) = {Go, Delay}                             ← restricted scope
A_AI(UNSAFE)  = ∅                                       ← no scope
```

Which formally means: **A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**

The formal safety property this produces is the **Safety Dominance Property**:

**AI(E) ⊆ A_AI(S) for all E**

This means: whatever the AI recommends is always within the admissible space determined by the current environmental safety state. The unsafe recommendation is never generated at all — not filtered after the fact, but structurally prevented before the AI reasons.

### The traffic light analogy

Existing architectures have only two states: green (AI fully on) and red (AI blocked). This architecture adds yellow — under CAUTION, the AI still participates, but only gives the advice that the current conditions can reliably support.

---

## 2. Indykov et al. (2025) — Architectural Tactics for ML-Enabled Systems

**Full reference**: Indykov, Strüber & Wohlrab (2025) [[notes]](../notes/Architectural%20tactics%20to%20achieve%20quality%20attributes%20of%20machine-learning-enabled%20systems-%20a%20systematic%20literature%20review.md), *The Journal of Systems & Software*, 223, 112373.

### Who they are and what they did

Vladislav Indykov (Chalmers University), Daniel Strüber (Radboud University), and Rebekkha Wohlrab (Carnegie Mellon University) conducted a systematic literature review of 206 papers to answer three questions:

1. What quality attributes do ML-enabled systems need? → They found **11 Common Quality Attributes (CQAs)**
2. What architectural tactics help achieve those attributes? → They found **16 Architectural Tactics (ATs)**
3. What are the trade-offs between tactics and quality attributes? → They documented **85 trade-offs**

### What is a quality attribute?

A quality attribute (QA) is a measurable property of a system that tells you how well it does its job — beyond just whether it produces correct outputs. Examples: how safe it is, how reliable, how explainable, how fair. Indykov et al. found that the 11 most commonly cited QAs for ML systems are: Safety, Fairness, Security, Explainability, Privacy, Reliability, Resource Efficiency, System Accuracy, Usability, Maintainability, and Data Quality.

### What is an architectural tactic?

An architectural tactic (AT) is a specific design decision an architect makes to achieve a quality attribute. For example, "use human-in-the-loop" is a tactic for achieving maintainability and explainability. "Use rule-based models" is a tactic for achieving explainability.

### The two tactics most relevant to this research

**AT11 — Rule-based Models**: A type of model that relies on explicit if-then rules designed by humans or domain knowledge. This maps conceptually to the deterministic governance layer S = f(E) in the proposed architecture — the layer that classifies the environmental state using a set of explicit threshold rules.

**AT4 — Human-in-the-Loop (HitL)**: An architectural approach where a human expert is integrated into the ML-enabled system as a separate component for monitoring and improving the system's behaviour. This maps conceptually to Layer 4 (the human decision-maker) in the proposed architecture.

### The critical finding: AT11 scores 0 for Safety

Indykov et al. produced a trade-off matrix (Table 3) showing the impact of each AT on each QA. The scoring is: + (positive impact), − (negative impact), a (ambivalent), 0 (insufficient evidence).

**AT11 → Safety = 0 (insufficient evidence)**. Despite Safety being one of the two most frequently cited QAs (19 papers reference it), no existing architectural tactic has demonstrated a formally positive impact on the Safety attribute. The architectural tactics literature has not established how rule-based mechanisms formally achieve safety properties.

This is independently confirmatory evidence for the research gap. The proposed architecture specifically uses an AT11-type rule-based mechanism (the deterministic governance layer) to formally guarantee the Safety Dominance Property — something none of the 16 identified tactics can currently provide.

### An important distinction: AT11 limitation becomes a feature

Indykov et al. note that AT11's main limitation is "limited adaptability to complex and dynamic data patterns when scenarios lie outside the predefined rules." This is a weakness when you are trying to use rule-based models to *approximate* what a neural network does — because the rules are too rigid to capture everything a neural network can learn.

But in this research, AT11 is not used to approximate ML behaviour. It is used to *govern* ML behaviour. In a governance context, the non-adaptability is a design feature, not a weakness — you *want* the governance boundary to be deterministic, stable, and formally verifiable. You do not want the governance rules to drift or learn from AI outputs.

### Where this paper sits in the literature review

Indykov et al. (2025) provides **confirmatory background** — useful for establishing that the architectural building blocks of the proposed system (rule-based layer, human layer) are recognised concepts in ML system architecture, while simultaneously confirming that no existing tactic formally addresses the Safety attribute. It does not directly compare architectures; it provides the quality framework within which the proposed architecture's formal contribution can be measured.

---

## 3. Dalrymple et al. (2024) — Guaranteed Safe AI

**Full reference**: Dalrymple, Skalse, Bengio, Russell, Tegmark, Seshia, Omohundro, Szegedy et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), arXiv:2405.06624. Affiliated institutions: UK ARIA, Oxford, Mila/Montreal, UC Berkeley, MIT, Stanford, CMU, Columbia, Cornell.

### Who they are

This is a 17-author position paper written by some of the most prominent AI safety researchers in the world, including Yoshua Bengio and Stuart Russell. Because of the authority of its authors and the breadth of institutions represented, it is one of the highest-authority references in the corpus — rated ⭐⭐⭐⭐⭐.

### What is red-teaming, and why is it insufficient?

Red-teaming is a method borrowed from military and cybersecurity practice where a dedicated group deliberately tries to break or fool a system — by crafting adversarial inputs, finding edge cases, or probing for hidden failure modes. If the red team cannot break it, the system is considered safe.

Dalrymple et al.'s argument against red-teaming is precise: it is a **negative result method**. No matter how many attacks fail, you have not proven the system is safe — you have only proven that those specific attacks failed. You cannot test every possible input. A sufficiently clever adversary, an unusual real-world situation, or gradual distributional shift (where real-world conditions slowly drift outside what was tested) can still cause failure after months of successful red-teaming.

Their concrete example: ChatGPT's safety precautions were circumvented within **one day** of going public despite months of intensive safety evaluation. This is why they argue that empirical testing alone — no matter how thorough — cannot provide genuine safety guarantees for safety-critical AI.

### What is Guaranteed Safe (GS) AI?

GS AI is Dalrymple et al.'s proposed family of approaches for achieving AI safety through **formal mathematical guarantees** rather than empirical testing. The name distinguishes it precisely: the guarantee is not statistical or probabilistic — it is a formal proof certificate that the AI satisfies its safety requirements.

A GS AI system is defined by three core components: a world model, a safety specification, and a verifier.

### The three core components — in plain language

**World model**: The system's mathematical understanding of how the AI's actions affect the real world. If the AI recommends action X, what happens next? The world model is the component that connects AI output to real-world consequences. Without it, you cannot reason formally about whether an action is safe — you only know what the AI said, not what it will cause.

**Safety specification**: A mathematical definition of what counts as acceptable. "Safe" is not self-defining — it is a value judgement that must be made explicit. The safety specification is where that judgement is encoded in a form that can be checked formally. It is also the component that can be audited by humans, regulators, and the public — it makes the system's values transparent rather than buried inside a neural network.

**Verifier**: The enforcement mechanism. It takes the AI's policy, the world model, and the safety specification, and produces a proof certificate that the AI satisfies the specification given how the world works. Only AI output that passes this check is allowed to reach the real world.

### Why all three components are necessary together

The three components are logically interdependent — removing any one collapses the guarantee.

- If you have a world model and a specification but **no verifier**: you have described what safe means, but nothing enforces it. Safety is only on paper.
- If you have a verifier and a specification but **no world model**: the verifier has nothing to reason about. It cannot connect AI outputs to real-world consequences, so it cannot check anything meaningful.
- If you have a world model and a verifier but **no specification**: the verifier has nothing to check against. It does not know what "safe" looks like.

Each component is necessary. All three are sufficient together to produce a formal guarantee.

### How GS AI relates to the proposed architecture

GS AI is the **high-level theoretical umbrella**. The proposed architecture is a **domain-specific, state-conditioned instantiation** of GS principles — but with two important differences that define the contribution.

| | GS AI (Dalrymple et al.) | Proposed Architecture |
|---|---|---|
| What is verified | The entire AI policy globally | Individual AI recommendations per environmental state |
| When it operates | Before or during policy deployment | At runtime, per interaction |
| Governance type | Binary — policy passes or fails | Graduated — SAFE, CAUTION, UNSAFE |
| CAUTION mode | No analogue | AI participates with restricted advisory scope |
| Formal property | Global: Vψ(π, m) ∈ permissible set | Per-state: AI(E) ⊆ A_AI(S) |
| Low-resource suitability | No — targets frontier AI systems | Yes — O(1) deterministic governance |

The key contribution relative to GS AI: the CAUTION mode. The GS framework is binary at the verification level — the policy either passes (AI operates) or fails (AI is disabled). There is no intermediate mode where the AI still participates but with a formally restricted advisory scope. The proposed architecture fills this gap with the governance pair (G(S), A_AI(S)) and the Safety Dominance Property, which operates at per-state granularity rather than per-policy granularity.

In short: **Dalrymple et al. establish why formal guarantees are necessary. The proposed architecture shows how those guarantees can be implemented in a graduated, state-conditioned, low-resource DSS context** — which the GS framework itself does not address.

---

## 4. Flehmig et al. (2024) — The Closest Structural Precedent

**Full reference**: Flehmig, Lundteigen & Yin (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), IEEE IECON 2024. All authors from NTNU, Norway.

### What they did and why it matters

Flehmig et al. identified a gap in ISO/IEC TR 5469 — the international standard for AI in safety-critical systems. The standard covers how to qualify AI before deployment, but says nothing about what happens when AI performance degrades *during operation*, due to concept drift (data distribution shifting over time), temporal model degradation, or outliers in the real world.

Their proposed solution is an extended framework with two additions: an **AI monitoring component** (using non-AI statistical methods to detect degradation) and an **AI updating component** (offline re-training). The centrepiece of their contribution is a **traffic-light degradation index** — a three-level classification of AI operational status with distinct recommended actions at each level.

### The traffic-light index

This is the most structurally similar system to the proposed architecture found in the entire literature review — rated ⭐⭐⭐⭐ High.

| Level | Colour | AI status | What happens |
|---|---|---|---|
| Level 1 | Green | No significant degradation | AI stays in control. Routine checks. |
| Level 2 | Orange | Signs of degradation | AI stays in control. Supervisor investigates thoroughly, considers re-training. |
| Level 3 | Red | Degradation past safety threshold | Switch to non-AI backup system. AI blocked. |

Map this directly against the proposed architecture:

| Flehmig et al. | Proposed Architecture |
|---|---|
| Level 1 (Green): AI on, full scope | SAFE: G(S) = 1, A_AI = full scope |
| Level 2 (Orange): AI on, **full scope** | **CAUTION: G(S) = 1, A_AI = restricted scope** |
| Level 3 (Red): AI blocked, backup takes over | UNSAFE: G(S) = 0, A_AI = ∅ |

The structural parallel is nearly exact — except for one critical difference at the middle level.

### The gap Flehmig et al. confirm

At Level 2 (Orange), the AI continues to operate with **identical, unrestricted scope** as at Level 1. The intermediate level changes what the *human supervisor does* — investigate more, consider re-training — but it does **not** change what the *AI may recommend*. The AI gives the same full set of outputs at Level 2 as at Level 1.

This is the binary governance problem appearing inside a three-level framework. Even with three states, the AI itself only has two modes: fully on (Levels 1 and 2) or blocked (Level 3). The intermediate level governs **supervisory behaviour**, not **AI advisory scope**.

Their own words confirm this is a novel space: *"To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner."* They know the three-level design is new — but they do not take the next step of using the intermediate level to restrict what the AI may recommend.

### Two reasons this paper strengthens the research argument

**First — structural validation.** Flehmig et al. independently confirm that tripartite safety classification is a natural and useful design for safety-critical AI. This supports the choice of S ∈ {SAFE, CAUTION, UNSAFE} over a binary model. If an examiner challenges "why three states?", Flehmig et al. provide independent motivation from a different domain and research group.

**Second — the most precise gap-evidence paper for the CAUTION mode.** The paper has almost everything needed for the proposed architecture's governance structure: a three-level classification, a non-AI monitoring layer (parallel to the deterministic S = f(E)), a limiting logic constraining AI outputs (parallel to G(S)), and a deterministic backup (parallel to UNSAFE mode). But the intermediate level does not restrict AI scope — it only triggers supervisory investigation. That missing connection — using the CAUTION state to formally restrict A_AI(S) — is exactly the proposed contribution.

### One citable quote

*"We want to develop an AI assistant that collaborates with the human operator to enhance the safety of the system and augment the operator's capabilities."* — directly supports the decision-support positioning of the proposed system.

---

## 5. How All Four Topics Connect

Each topic contributes a different layer of the overall argument:

**The problem and gap** establishes what is missing in plain CS terms — no existing architecture formally restricts AI advisory scope based on environmental safety state. This is the research problem.

**Indykov et al. (2025)** provides independent confirmation from the ML systems quality literature. After surveying 206 papers and 16 architectural tactics, no tactic has demonstrated formal positive impact on the Safety attribute (AT11 → Safety = 0). The gap exists not just in AI architecture papers but across the broader ML systems design literature.

**Dalrymple et al. (2024)** establishes the theoretical framework within which the proposed architecture sits. GS AI is the high-level principle; the proposed architecture is a specific, state-conditioned instantiation that extends GS AI into graduated governance for DSS contexts — addressing a gap that Dalrymple et al. themselves do not fill (their framework is binary at the verification level, with no CAUTION mode).

**Flehmig et al. (2024)** provides the closest structural precedent. Their traffic-light design is almost identical to the proposed tripartite safety state, confirming that three-level classification is independently motivated. But even their design uses the intermediate level only to govern human supervisory behaviour — not AI recommendation scope — making it the most precise available evidence that the CAUTION mode gap is real and remains unfilled.

Together, the four topics form a coherent and multi-layered argument: the problem is real, the gap is confirmed from multiple independent sources across different literatures, the proposed architecture fills it within an established theoretical foundation, and the closest available precedent confirms the gap even as it approaches the solution.
