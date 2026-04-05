## Literature Review Extraction
### Kalmykov & Kalmykov (2025) — Towards eXplicitly eXplainable Artificial Intelligence

---

### 1. Paper Identity
- **Title:** Towards eXplicitly eXplainable Artificial Intelligence
- **Authors:** Vyacheslav L. Kalmykov, Lev V. Kalmykov
- **Year:** 2025 (Accepted 17 May 2025; available online 18 May 2025)
- **Venue:** Information Fusion, Vol. 123, 103352
- **DOI:** 10.1016/j.inffus.2025.103352
- **Type:** Conceptual framework / position paper with precedent demonstrations

---

### 2. Core Contribution
- **Problem:** Neural network AI (including XAI) remains fundamentally opaque — a black box whose subsymbolic, statistical nature cannot be made fully transparent. Four barriers have historically prevented widespread adoption of symbolic "white box" AI: (1) operational opacity of mathematical methods, (2) semantic opacity of natural language terms, (3) lack of a general abstract ontology, and (4) insurmountable combinatorial explosion.
- **Solution:** XXAI (eXplicitly eXplainable AI) — a fully transparent symbolic AI implemented on deterministic logical cellular automata whose rules are based on first principles (axioms) of the general physical theory of the relevant problem domain. The authors claim this overcomes all four barriers.
- **Key claims:** XXAI can make autonomous, fully transparent decisions; it should serve as the "senior partner" in neuro-symbolic hybrid AI systems, systematically validating neural network solutions for reliability, security, and ethics throughout the AI lifecycle.
- **Novelty:** The specific framing of cellular automata + domain-specific axiomatic theory as a general method for white-box AI, and the claim that this overcomes all four historical barriers to symbolic AI.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Explicitly proposes neuro-symbolic hybrid AI where XXAI (symbolic, deterministic, white-box) serves as the governing partner that validates and controls neural network (subsymbolic, probabilistic, black-box) AI |
| Safety-critical AI decision-making | **Partial** | Discusses safety, reliability, and accountability concerns with opaque AI; argues for transparent AI as prerequisite for safe autonomous decisions; but does not address a specific safety-critical operational domain or decision architecture |
| AI governance / control mechanisms | **Partial** | Argues symbolic AI should take control of learning and decisions of subsymbolic AI — a high-level governance vision. But this is AI-system-level governance (symbolic controls neural network), not operational governance over what AI may recommend in different safety states |
| Low-resource environments | No | Not addressed |
| Decision architecture formalisation | **Partial** | Cellular automata provide a formal, deterministic, multi-level framework; ecological models demonstrate bottom-up integration of local rules into global system behaviour. But no decision architecture for operational AI advisory systems is formalised |
| Human role in decision-making | Partial | Discusses human-AI cooperation in Industry 5.0 context; argues human control over AI is fundamentally limited and symbolic AI should take over that control function |
| Socio-technical evaluation | No | Not addressed |
| Coastal fisheries / maritime domain | No | Not addressed (ecological competition modeling is used as demonstration, but not in fisheries context) |

**Mid-Extraction Relevance Gate:** 1 Yes + 3 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only)

---

### 4. Decision Architecture Analysis
- The paper does not propose a decision architecture for operational AI systems. Rather, it proposes a **computational paradigm** — deterministic logical cellular automata grounded in domain-specific axiomatic theory — as the foundation for transparent AI.
- The cellular automata models are **multi-level**: micro (lattice site / individual agent), meso (cellular automaton neighbourhood / local interactions), macro (entire lattice / system as a whole). Rules operate simultaneously across all levels at each iteration.
- **Safety constraints:** Not explicit. The paper argues that transparency itself ensures safety — if you can trace every causal step, you can verify safety. But no safety gate, safety state classification, or governance mechanism is defined.
- **Deterministic control vs. AI reasoning boundary:** The paper's vision positions XXAI (deterministic, symbolic) as the controller/validator of neural network AI (probabilistic, subsymbolic). The boundary is between the two AI paradigms, not between a safety layer and an advisory layer within a single system.
- **Fallback/override:** Not discussed for operational systems. The paper envisions XXAI preventing unsafe neural network outputs before deployment, not runtime fallback.

---

### 5. Formal Model and Mathematical Representation
- **Cellular automaton formal definition (Sec. 3.1):** Five components — (1) regular homogeneous lattice, (2) finite set of possible site states, (3) initial pattern, (4) neighbourhood definition, (5) transition function (if-then rules applied simultaneously to all sites at each iteration).
- **Model transparency classification (Fig. 1):** Black-box (equations, stochastics, neural networks) → Grey-box (hybrid) → White-box (logical deterministic cellular automata). Transparency is defined as the level of control over local causal interactions of subsystems.
- **Comparison to DSR pipeline:** No correspondence. The paper's formalism models ecological systems (species competition on spatial lattices), not decision support pipelines. There is no equivalent of E → S = f(E) → (G(S), A_AI(S)) → AI(E). The cellular automaton models system dynamics, not a governance architecture over AI advisory scope.
- **State-dependent recommendation restriction:** Not present. The cellular automaton sites change state based on local neighbourhood rules, but this models population dynamics, not restriction of AI output types across safety states.
- **Safety Dominance Property equivalent:** Not defined. The closest concept is the claim that XXAI can "systematically validate neural network solutions" — but this is a design-time validation vision, not a formal runtime property.

---

### 6. Safety State Classification
- No classification of operational or environmental conditions into safety levels.
- The cellular automaton sites have discrete states (e.g., alive/dead/recovering in ecological models), but these model ecological entities, not safety conditions.
- No comparison possible to S = f(E) → {SAFE, CAUTION, UNSAFE}.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | Not addressed at operational level |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | Not addressed |
| **Levels 1 + 2 unified, state-conditioned** | Both governed by classified environmental state? | No | Not addressed |

- The paper proposes a **different kind of governance**: symbolic AI governing neural network AI at the system design and validation level. This is paradigm-level governance ("XXAI validates and controls neural network AI"), not operational governance over what AI may recommend under different environmental safety states.
- The paper supports the general principle that deterministic, rule-based systems should govern probabilistic AI — which aligns philosophically with my architecture's principle that deterministic safety gates should constrain probabilistic AI reasoning. But the level of abstraction is entirely different.

---

### 12. Key Concepts and Definitions
- **XXAI (eXplicitly eXplainable AI):** Fully transparent symbolic AI implemented on deterministic logical cellular automata with rules based on first principles of the domain's general physical theory
- **White-box vs. black-box models (Fig. 1):** Transparency spectrum from opaque (equations, stochastics, neural networks) to fully transparent (logical deterministic cellular automata)
- **Four barriers to symbolic AI:** (1) operational opacity of mathematical methods, (2) semantic opacity of natural language, (3) lack of general abstract ontology, (4) insurmountable combinatorial explosion
- **Neuro-symbolic hybrid AI:** Combining subsymbolic (neural network) and symbolic (logical, rule-based) AI, with XXAI proposed as the "senior partner" governing neural network AI
- **Hyperlogic:** Cellular automaton logic executed simultaneously for all sites at each iteration, implementing knowledge-based inference
- **Intellectual debt in AI:** Accumulated opacity and lack of understanding in machine learning systems, analogised to technical debt

---

### 13. Limitations and Unsolved Problems
- **Stated limitations:**
  - The approach has only been demonstrated in one domain (ecological competition modelling); generalisation to other domains requires creating axiomatic theories for each domain
  - The creation of a "general abstract ontology of our world" — acknowledged as an unsolved foundational problem coinciding with Hilbert's sixth problem
  - Attracting implementers is difficult due to 150 years of positivist dominance in science; the approach requires skills in abstract theoretical thinking that are culturally undervalued
  - The paper is explicitly a "program" / vision — the precedent demonstrations are limited to ecological competition models
- **Gaps aligning with my research:**
  - The paper does not address **operational AI governance** — when and what AI should recommend under different conditions. It addresses whether AI is trustworthy at the paradigm level, not how to govern AI advisory scope at runtime.
  - The deterministic cellular automata approach is philosophically aligned with my use of deterministic rules governing probabilistic AI, but at a completely different level of abstraction.
  - No concept of safety state classification, graduated governance, or state-conditioned advisory scope restriction.

---

### 16. Relation to My Research and Positioning
- The paper implements neither Level 1 nor Level 2 governance in the operational sense.
- No formal safety property comparable to the Safety Dominance Property is defined.
- The gap between this paper and my research is one of abstraction level: this paper asks "how to make AI itself transparent" (paradigm-level); my research asks "how to govern what a (potentially opaque) AI may recommend under different safety conditions" (operational-level).

**Positioning paragraph:** This paper provides theoretical background on the white-box vs. black-box AI distinction and the argument for deterministic symbolic AI governing probabilistic neural network AI. The philosophical alignment with my architecture is real but operates at a different abstraction level — Kalmykov & Kalmykov argue that deterministic cellular automata should validate and control neural networks at the system design level; my architecture uses deterministic safety gates to govern what a probabilistic AI advisory system may recommend at the operational runtime level. The paper's classification of model transparency (Fig. 1) and its framing of four barriers to symbolic AI could provide useful theoretical context in a background section on hybrid AI, but the paper does not contribute to the specific problem of state-conditioned AI governance for safety-critical decision support. Published in Information Fusion (high-impact venue), so it carries citation weight, but its relevance to my core contribution is peripheral.

---

### 17. Overall Relevance Score

**⭐⭐ Low — tangentially related theoretical background on white-box AI and neuro-symbolic hybrids**

**Justification:** The paper's core argument — that deterministic symbolic AI should govern probabilistic neural network AI — resonates philosophically with my architecture's principle of deterministic safety gates constraining probabilistic AI reasoning. However, the paper operates at the AI paradigm level (how to make AI itself transparent) rather than at the operational governance level (how to control what AI recommends under classified safety states). It proposes no decision architecture, no safety state classification, no governance mechanism, and no formal safety property. The ecological cellular automata demonstrations model population dynamics, not decision support. For my literature review, stronger sources exist for the hybrid AI theme (Könighofer et al. on shields, Dalrymple et al. on guaranteed safe AI) and for the white-box argument (the entire symbolic AI literature). Citable only as peripheral support for the general principle that deterministic mechanisms should govern probabilistic AI — and even that point is better sourced elsewhere.
