## Literature Review Extraction — REDUCED
### Bengio, Hinton, Yao, Song et al. (2024) — Managing Extreme AI Risks Amid Rapid Progress

---

### 1. Paper Identity

- **Title:** Managing extreme AI risks amid rapid progress
- **Authors:** Yoshua Bengio, Geoffrey Hinton, Andrew Yao, Dawn Song, Pieter Abbeel, Trevor Darrell, Yuval Noah Harari, Ya-Qin Zhang, Lan Xue, Shai Shalev-Shwartz, Gillian Hadfield, Jeff Clune, Tegan Maharaj, Frank Hutter, Atılım Güneş Baydin, Sheila McIlraith, Qiqi Gao, Ashwin Acharya, David Krueger, Anca Dragan, Philip Torr, Stuart Russell, Daniel Kahneman, Jan Brauner, Sören Mindermann
- **Year:** 2024
- **Venue:** *Science* (DOI: 10.1126/science.adn0117)
- **Type:** Perspective / policy paper
- **Note:** This is the supplementary materials PDF containing the full text with 73 extended references. The main paper was published in *Science*, one of the highest-impact journals globally.

---

### 2. Core Contribution

- **Problem:** AI is progressing rapidly toward generalist, autonomous systems. Risks include large-scale social harms, malicious uses, and irreversible loss of human control. Current governance initiatives and safety research are incommensurate with the pace of progress.
- **Proposed solution:** A comprehensive plan combining technical R&D reorientation with proactive, adaptive governance mechanisms. Calls for at least one-third of AI R&D budgets to be allocated to safety.
- **Main contributions:**
  1. Identifies key technical R&D challenges: oversight/honesty, robustness, interpretability, inclusive development, emerging failure modes, dangerous capability evaluation, alignment evaluation, risk assessment, resilience
  2. Proposes governance mechanisms: fast-acting institutions, government insight (mandatory reporting, white-box audits), safety cases (burden of proof on developers), mitigation measures (licensing, autonomy restrictions, development halts)
  3. Advocates for "if-then" commitments: automatic policy triggers tied to capability milestones
- **Novelty:** Authoritative consensus statement from 25 leading AI researchers (including two Turing Award winners) calling for specific governance mechanisms drawn from safety-critical industry parallels.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **No** | No technical architecture discussed. |
| Safety-critical AI decision-making | **Yes** | Central concern — the paper frames AI as a safety-critical technology requiring governance analogous to pharmaceuticals, aviation, nuclear energy, and financial systems. |
| AI governance / control mechanisms | **Yes** | Central focus, but at the **policy/regulatory layer** — institutional governance, safety cases, liability, licensing, auditing. Not at the **architectural runtime layer** (no G(S), A_AI(S), or runtime state-conditioned governance). |
| Low-resource environments | **No** | Focus is on frontier AI systems (billion-dollar training runs), not low-resource deployment. |
| Decision architecture formalisation | **No** | No formal models or mathematical representations. |
| Human role in decision-making | **Partial** | Emphasises human oversight of autonomous systems and the risk of "delegating key societal roles to autonomous AI systems with insufficient human oversight." Does not specify human–AI interaction mechanisms. |
| Socio-technical evaluation | **Partial** | Discusses societal-scale risk assessment and the need for sociotechnical governance, but does not conduct socio-technical evaluation. |
| Coastal fisheries / maritime domain | **No** | No domain-specific application. |

**Mid-Extraction Relevance Gate:** 2 Yes + 2 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only, plus 16–17)

---

### 4. Decision Architecture Analysis

Not applicable. The paper does not describe a technical decision architecture. It operates entirely at the policy/institutional governance level — prescribing *what institutions should do* about AI risk, not *how AI systems should be architecturally governed at runtime*.

---

### 5. Formal Model and Mathematical Representation

None. The paper contains no formal models, mathematical representations, or architectural specifications.

---

### 6. Safety State Classification

The paper does not classify operational states. However, it implicitly advocates for **capability-milestone-triggered governance** — "policies that automatically trigger when AI hits certain capability milestones. If AI advances rapidly, strict requirements automatically take effect, but if progress slows, the requirements relax accordingly." This is a form of graduated governance at the *institutional policy* level (not the architectural runtime level), where governance intensity varies with assessed capability level. This is conceptually parallel to, but categorically distinct from, my environmental-state-conditioned architectural governance.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Partial (policy layer)** | Calls for governments to "halt development and deployment in response to worrying capabilities" and "license development" of exceptionally capable systems. This is institutional-level participation governance — governments deciding whether AI systems may be developed/deployed at all. Not architectural runtime governance. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **Partial (policy layer)** | Calls to "restrict autonomy in key societal roles." This is institutional-level scope restriction — limiting what roles AI may fill in society. Not runtime restriction of AI advisory output scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Governance is triggered by capability milestones (model-level assessment), not by classified environmental state at runtime. |

**Critical distinction:** This paper's governance operates at the **policy/regulatory layer** — who may develop AI, under what conditions, with what oversight. My architecture operates at the **architectural runtime layer** — what the AI system may output, conditioned on classified environmental state. These are categorically different governance layers. The paper does not threaten or address the architectural governance gap.

---

### 12. Key Concepts and Definitions

| Concept | Definition / Relevance |
|---|---|
| **Safety cases** | "Structured arguments with falsifiable claims supported by evidence that identify potential hazards, describe mitigations, show that systems will not cross certain red lines, and model possible outcomes to assess risk." Drawn from aviation, medical devices, defence software. Referenced to Kelly (2004) and Clymer et al. (2024). Relevant as a governance mechanism from safety-critical industries. |
| **Capability-triggered governance** | "Policies that automatically trigger when AI hits certain capability milestones." Graduated institutional governance that scales with assessed risk level — conceptually parallel to but distinct from runtime state-conditioned governance. |
| **Burden of proof reversal** | "Developers of frontier AI should carry the burden of proof to demonstrate that their plans keep risks within acceptable limits" — not "safe unless proven unsafe." Follows best practices from aviation, medical devices, defence. |
| **If-then commitments** | "Specific safety measures [companies] will take if specific red-line capabilities are found in their AI systems." Pre-committed governance responses to capability thresholds. |
| **Autonomous AI risks** | Systems that "pursue undesirable goals... gain human trust, acquire resources, and influence key decision-makers... copy their algorithms across global server networks." The paper frames autonomous AI as the highest-risk category requiring the strongest governance. |

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. "We do not know for certain how the future of AI will unfold" — acknowledges uncertainty about timelines
  2. Safety R&D challenges "cannot be addressed by simply using more computing power" and "may require leaps of progress" — acknowledges that technical solutions may not arrive in time
  3. "Present testing methodologies" for frontier AI "cannot reliably rule out" dangerous capabilities — acknowledges fundamental evaluation limitations

- **Gaps aligned with my research:**
  - The paper calls for "commensurate mitigations" that "restrict autonomy" and "halt development" for exceptionally capable systems — but these are binary institutional responses (develop/don't develop, deploy/don't deploy). There is no discussion of **graduated architectural governance** where the AI system itself operates under state-conditioned scope restrictions at runtime.
  - The "capability-triggered governance" mechanism is graduated at the institutional level but does not translate to a runtime architectural mechanism. My architecture fills this gap by implementing graduated governance *within* the AI decision system itself.
  - The paper acknowledges the need for "safety cases" from safety-critical industries but does not discuss how formal safety properties (like the Safety Dominance Property) could be architecturally embedded.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** Institutional-level only (licensing, halting development). No architectural runtime implementation.
- **Level 2 governance:** Institutional-level only (restricting autonomy in societal roles). No runtime advisory scope restriction.
- **State-conditioned:** Capability-milestone-conditioned at the policy level, not environmental-state-conditioned at the runtime architectural level.
- **Two-level governance pair proximity:** Not applicable — operates at a different governance layer entirely.
- **Safety Dominance Property:** Not discussed. No formal safety properties.
- **Gap my research addresses:** The paper motivates the *need* for AI governance broadly but does not specify *how* governance operates within the AI system at runtime. My architecture addresses this by embedding two-level governance directly in the decision architecture, conditioned on classified environmental state.

**Positioning paragraph:** This *Science* perspective paper, authored by 25 leading AI researchers including Bengio and Hinton, provides authoritative context for the urgency of AI governance in safety-critical domains. It calls for graduated institutional governance (capability-triggered policies), safety cases drawn from safety-critical industries, and burden-of-proof reversal for frontier AI developers. However, its governance recommendations operate entirely at the **policy/regulatory layer** — prescribing what institutions, companies, and governments should do. It does not address **architectural runtime governance** — how the AI system itself should be governed at the decision-output level based on classified environmental state. This paper should be cited in Section 1 (motivation/context) as a high-authority reference establishing the urgency of AI safety governance, and in Section 2.1 (background) to distinguish policy-layer governance from the architectural-layer governance that is the focus of the dissertation. The paper's advocacy for capability-triggered graduated governance at the institutional level is conceptually parallel to, but categorically distinct from, the dissertation's environmental-state-conditioned graduated governance at the architectural level. The distinction between these two governance layers should be made explicit when citing this paper.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

High-authority context reference (*Science*, Bengio + Hinton + 23 co-authors) for the urgency of AI governance. Useful for motivation (Section 1) and for distinguishing policy-layer governance from architectural-layer governance (Section 2.1). Does not directly address the two-level governance gap, runtime state-conditioned governance, or any technical architecture. Complements your existing extraction of the International AI Safety Report 2026 (Bengio et al.) — that report provides the institutional baseline confirming binary governance across Frontier AI Safety Frameworks; this earlier paper provides the *Science*-published call to action that preceded it.
