# Literature Review Extraction: Punzi et al. (2024)
## AI, Meet Human: Learning Paradigms for Hybrid Decision-Making Systems

---

## 1. Paper Identity

- **Full title:** AI, Meet Human: Learning Paradigms for Hybrid Decision-Making Systems
- **Authors:** Clara Punzi, Roberto Pellungrini, Mattia Setzu, Fosca Giannotti, Dino Pedreschi
- **Year:** 2024 (arXiv v3: March 2025)
- **Venue:** Journal of the ACM (J. ACM), Vol. 1, No. 1; arXiv:2402.06287v3
- **Type:** Survey / Taxonomy paper

---

## 2. Core Contribution

- **Main problem:** The literature on human-AI collaborative decision-making systems is fragmented, with diverse techniques classified sparsely and goals varied across computer science subfields. There is no unified conceptual or technical framework for understanding how humans and machines interact in decision-making.

- **Proposed solution:** A taxonomy of **Hybrid Decision-Making Systems** organised into three learning paradigm families, ordered by increasing integration between human and machine agents:
  1. **Human Overseers** — human accepts or rejects machine predictions (no integration)
  2. **Learning to Abstain** — machine learns when to predict and when to defer to a human (subdivided into Learning to Reject and Learning to Defer)
  3. **Learning Together** — bidirectional interaction where human and machine communicate, correct, and learn from each other

- **Main contributions:**
  - A formal general model of hybrid systems defining machine agent M, human agent H, their prediction functions, loss functions, and deferral/rejection policies
  - A comprehensive survey of Learning to Reject (L2R), Learning to Defer (L2D), and Learning Together paradigms with technical depth on surrogate losses, architectural variants, and theoretical guarantees
  - Identification of open problems across machine-related, human-related, and interaction-related dimensions

- **Novelty:** Provides the first unified taxonomy that spans from simple oversight to deep bidirectional human-AI collaboration, with a consistent formal notation throughout. Bridges previously disconnected literatures (selective classification, learning to defer, interactive ML, neuro-symbolic systems) under a single framework.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | Central topic. Surveys neuro-symbolic approaches, rule-based + neural hybrids in Learning Together paradigm. Discusses logic-based communication languages, knowledge graphs, and explanation-based feedback loops. |
| Safety-critical AI decision-making | **Partial** | Mentions high-stakes domains (medicine, law, finance) as motivation throughout, but does not address safety-critical architecture design, safety constraints, or safety state classification. Focus is on prediction accuracy and human-AI complementarity, not on safety governance. |
| AI governance / control mechanisms | **Partial** | Addresses *who decides* (human vs. machine) through deferral and rejection policies, and *how humans oversee* machine outputs. However, governance is framed as task allocation (who predicts) rather than as safety-state-conditioned control over AI participation scope. No concept of state-dependent restriction of AI advisory scope. |
| Low-resource environments | No | Not addressed. Systems assume standard data availability; L2D even requires human labels for all training instances. |
| Decision architecture formalisation | **Partial** | Provides formal notation for hybrid systems: machine predictor f, human predictor h, rejection/deferral policy ρ_M, and system loss functions. Formalisation is oriented toward optimising prediction accuracy across agents, not toward safety state classification or governance functions. |
| Human role in decision-making | **Yes** | Core focus. Entire taxonomy is organised around the human's role: overseer (Paradigm 1), fallback predictor (Paradigm 2), or interactive collaborator (Paradigm 3). Discusses algorithmic aversion, overreliance, trust calibration, and cognitive biases. |
| Socio-technical evaluation | **Partial** | Discusses human factors (trust, bias, monitoring pitfalls, fairness concerns) but does not conduct socio-technical evaluation. Notes lack of tailored validation measures for hybrid systems as an open problem. |
| Coastal fisheries / maritime domain | No | Not addressed. |

**Mid-Extraction Relevance Gate:** 2 Yes + 3 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The taxonomy defines three architectural patterns of increasing integration:
  - **Human Overseers:** Sequential pipeline — machine predicts, human accepts or rejects. No feedback loop. Machine and human are independent agents.
  - **Learning to Abstain:** Orchestrated allocation — a deferral/rejection policy routes each instance to either the machine or human agent based on estimated performance. Architectures are either *staged* (classifier trained first, then deferral policy) or *joint* (both learned simultaneously via augmented loss).
  - **Learning Together:** Iterative feedback loop — machine generates predictions and explanations/artifacts, human inspects and corrects, machine re-trains or updates. Communication occurs through hard logic, soft reasoning (natural language), or explanation languages.

- **Safety constraint mechanism:** None. There is no safety layer, no gate function, and no safety state classification. The deferral policy ρ_M is a binary function {0, 1} that routes instances based on predicted *accuracy*, not on environmental or operational safety conditions.

- **Rule-based constraints before AI:** Not present as safety constraints. In Learning Together, logic rules and knowledge graphs serve as *communication artifacts* between human and machine, not as safety gates. In L2R/L2D, the rejection threshold τ is a performance-based parameter, not a safety constraint.

- **Boundary between deterministic control and AI reasoning:** Not explicitly defined in safety terms. The closest concept is the deferral policy ρ_M, which deterministically routes instances to human or machine — but the routing criterion is predictive accuracy/uncertainty, not safety state. In Learning Together with hard reasoning, there is an explicit symbolic-subsymbolic boundary, but it serves reasoning transparency, not safety governance.

- **Failure modes and fallback:** Discusses monitoring pitfalls (algorithmic aversion, overreliance, biased monitoring, failure to oversee) as human failure modes in Paradigm 1. In L2R/L2D, deferral to a human is the fallback when the machine is uncertain. No deterministic fallback behaviour defined for when the entire system is unsafe.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** Yes. The paper defines a general formal framework for hybrid systems:
  - Machine agent M implementing predictor f: X → Y_M
  - Human agent H implementing predictor h: X × Z → Y_H (where Z is human expertise)
  - Rejection/deferral policy ρ_M: X → {0, 1}
  - System loss ℒ_defer combining machine loss and human loss, weighted by the deferral indicator
  - L2R formulation: f^ρ_M(x) = ∅ if ρ_M(x) = 1, else f(x)
  - L2D formulation: f^ρ_M(x) = h(x) if ρ_M(x) = 1, else f(x)
  - Various surrogate loss functions (ℒ_CE, ℒ_OvA, ℒ_ASM, ℒ_RS, ℒ_DCE) with theoretical guarantees (Fisher consistency, classification-calibration, realizable consistency)

- **Comparison to my pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - The paper's formal model operates at a fundamentally different level. It formalises *who predicts* (machine or human) on a per-instance basis, optimised for accuracy. My pipeline formalises *whether AI may participate at all* and *what AI may recommend*, conditioned on classified environmental safety state.
  - Their ρ_M is instance-level and accuracy-driven; my G(S) is state-level and safety-driven.
  - Their system has no concept of environmental state vector E, safety state S, or safety classification function f(E).
  - Their deferral is binary (predict or defer); my architecture is ternary (SAFE / CAUTION / UNSAFE) with graduated advisory scope.

- **State-dependent recommendation restriction (analogous to A_AI(S)):** **No.** The deferral policy ρ_M is a binary switch: the machine either generates its full prediction or defers entirely. There is no intermediate mode where the machine participates but with a restricted output space. When ρ_M(x) = 0 (machine predicts), the machine generates the same type of output regardless of any risk or uncertainty level. There is no concept analogous to A_AI(CAUTION) ⊂ A_AI(SAFE).

- **Safety Dominance Property (AI(E) ⊆ A_AI(S)):** **No.** No formal property constrains AI outputs to a state-determined admissible space. The surrogate loss optimisation guarantees (Fisher consistency, calibration) concern accuracy and calibration, not safety containment. The coverage constraint (Eq. 5) bounds the *quantity* of deferrals, not the *scope* of AI outputs.

- **Formalisation purpose:** The formal model is used for analysis (proving theoretical guarantees of surrogate losses) and for defining optimisation objectives. It is rigorous and functional, not purely descriptive.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** **No.** The paper does not classify operational or environmental conditions into risk or safety levels. The deferral decision is driven by per-instance uncertainty or predicted error probability, not by a classified safety state.

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The paper has no equivalent. The closest analogue is the binary deferral outcome {predict, defer}, which is instance-specific and accuracy-motivated rather than environment-level and safety-motivated.

- **Differentiated AI recommendation scope across safety levels:** **No.** This is a critical gap relative to my research. When the machine predicts (ρ_M = 0), it produces the same output type at the same scope regardless of any ambient risk. When it defers (ρ_M = 1), it produces nothing. There is no mode analogous to CAUTION where the AI participates with a restricted recommendation space.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (≡ G(S)) | **Partial** | The deferral policy ρ_M determines whether AI predicts or defers, but this is conditioned on per-instance accuracy estimates, not on classified environmental safety state. It is functionally a participation gate, but accuracy-gated, not safety-gated. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (≡ A_AI(S)) | **No** | When the machine predicts, it generates the same output type at full scope. No mechanism restricts what types of recommendations AI may produce. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Neither level is conditioned on environmental safety state. |

- **Binary switch or graduated governance?** Binary. The deferral is strictly {predict, defer} — a Level 1-only mechanism. Even the L2D-ME variant that selects *which* expert to defer to still operates as a binary per-instance gate for the machine.

- **Level 2 governance:** Not present. No mechanism constrains the machine's output scope. When the machine is allowed to predict, it generates its full output.

- **Support for two-level governance pair (G(S), A_AI(S))?** The paper **indirectly supports** the motivation for this construct. Its taxonomy shows that all three paradigms (oversight, abstention, collaboration) operate with binary AI participation (predict or don't predict). No paradigm implements graduated governance where the AI's advisory scope varies by safety state. This constitutes evidence for the two-level governance gap that my architecture addresses.

---

## 12. Key Concepts and Definitions

- **Hybrid Decision-Making System:** A system composed of human agent H and machine agent M that jointly address a predictive task, combining complementary strengths.
- **Human Oversight:** Paradigm where human accepts/rejects machine predictions via policy ρ_H: X × Y_M × Z → {accept, reject}.
- **Learning to Reject (L2R):** Machine learns rejection policy ρ_M based on predicted accuracy; deferred instances handled by human. Fixed rejection cost R.
- **Learning to Defer (L2D):** Machine learns deferral policy ρ_M incorporating human expertise Z; optimises combined human-machine system loss. Subsumes L2R when human cost is constant.
- **Learning Together:** Bidirectional paradigm where human and machine communicate via artifacts (logic rules, explanations, natural language) and iteratively improve.
- **Deferral/Rejection Policy (ρ_M):** Binary function routing each instance to machine or human. Instance-level, accuracy-driven.
- **Surrogate Loss Functions:** ℒ_CE (cross-entropy), ℒ_OvA (One-vs-All), ℒ_ASM (asymmetric softmax), ℒ_RS (realizable consistent), ℒ_DCE (dependent cross-entropy) — various loss formulations with theoretical guarantees for L2D.
- **Communication Language:** The medium through which human and machine interact in Learning Together systems: hard reasoning (logic), soft reasoning (natural language), or explanations (feature relevance, decision rules).
- **Interaction Artifacts:** Atomic units of communication (logic rules, feature importance scores, knowledge graph triples) that are understandable by both agents, malleable by the human, and embeddable into the machine.
- **Intrinsic vs. Extrinsic Artifacts:** Intrinsic artifacts update model parameters internally (human has no direct control over integration); extrinsic artifacts are stored in an artifact bank directly accessible to both agents.
- **Algorithmic Aversion / Overreliance:** Cognitive biases where humans either excessively doubt or blindly trust machine predictions — key monitoring pitfalls.

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
- Human Oversight and L2A systems lack meaningful communication mechanisms — humans receive predictions and possibly uncertainty scores, but not explanations of *why* to accept/reject.
- L2D requires human predictions for all training instances alongside ground truth labels, making it impractical for most real-world scenarios. Limited-label approaches exist but remain early-stage.
- Learning Together systems are "monolingual" — designed for one communication language, one type of human agent, and cannot adapt to heterogeneous users.
- Learning Together systems are largely static: cannot switch communication languages, adapt to different humans, or defend against incorrect/malicious human feedback.
- No tailored validation measures exist for hybrid systems — particularly for assessing how well machines comply with human corrections or providing guarantees on correction effects.
- Fairness concerns arise in all paradigms: from biased monitoring (Paradigm 1), to abstention-induced disparities (Paradigm 2), to unverified feedback (Paradigm 3).
- The data annotation labour force underpinning L2D systems faces lax regulations, low wages, and few legal protections — an ethical concern.

**Alignment with my research problem:**
- **Two-level governance gap:** The paper's entire taxonomy operates with binary participation governance only (ρ_M ∈ {0, 1}). No paradigm implements graduated advisory scope governance. The paper does not identify this as a gap, but the absence is structurally apparent across all three paradigms. My architecture's Level 2 governance (A_AI(S)) addresses exactly this missing dimension.
- **CAUTION mode absence:** None of the three paradigms defines an intermediate mode where AI participates with restricted output scope. The deferral is always all-or-nothing. My CAUTION mode — where G(S) = 1 but A_AI(CAUTION) ⊂ A_AI(SAFE) — fills this gap.
- **Safety state conditioning absence:** All governance in the paper is instance-level and accuracy-driven. No paradigm conditions AI participation or scope on classified environmental safety state. My architecture's state-conditioned governance pair (G(S), A_AI(S)) provides the missing environmental safety dimension.
- **Safety Dominance Property absence:** The paper provides theoretical guarantees for accuracy (Fisher consistency, calibration) but no formal property guaranteeing AI outputs remain within safety-determined bounds. My Safety Dominance Property (AI(E) ⊆ A_AI(S)) addresses this.

---

## 16. Relation to My Research and Positioning

- **Level 1 governance (participation control):** Partial. The deferral policy ρ_M is functionally a participation gate, but it is accuracy-conditioned per-instance, not safety-state-conditioned.
- **Level 2 governance (output-scope control):** Not implemented. When the machine predicts, it generates full-scope output.
- **Two-level governance pair (G(S), A_AI(S)):** Not approached. The paper's governance is single-level (predict/defer) and not conditioned on environmental safety state.
- **Formal safety property (Safety Dominance):** Not defined. Theoretical guarantees concern accuracy and calibration, not safety containment.
- **Gap my research addresses:** The paper demonstrates that the entire field of hybrid decision-making systems — from simple oversight to sophisticated learning-to-defer and bidirectional collaboration — operates exclusively with binary AI participation governance. No paradigm varies the *scope* of AI recommendations based on safety conditions. This confirms the two-level governance gap from a different angle: not just in safety-critical AI and shielding literature, but also in the broader human-AI collaboration literature.

**Positioning paragraph:** Punzi et al. (2024) provides authoritative background on how human-AI hybrid systems structure the interaction between human and machine agents. Its three-paradigm taxonomy (Human Overseers, Learning to Abstain, Learning Together) comprehensively maps the landscape of hybrid decision-making, with rigorous formal treatment of deferral policies and surrogate losses. For my research, this paper serves two roles. First, it provides **background on the human role dimension**: its treatment of oversight, deferral, and collaboration paradigms contextualises where my architecture sits within the broader human-AI interaction landscape — specifically as a *decision support* system where the human retains final authority, with AI participation governed by environmental safety state rather than per-instance accuracy. Second, and more critically, it provides **structural gap evidence**: across all three paradigms and their many variants, AI participation governance is universally binary (predict or defer), and no mechanism varies the AI's *recommendation scope* by safety state. This absence, visible across a comprehensive survey of the field, strengthens the claim that the two-level governance model (G(S), A_AI(S)) with graduated advisory scope is a genuine architectural contribution not addressed by existing hybrid system designs.

---

## 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** The paper provides a comprehensive, well-formalised survey of hybrid human-AI decision-making that is directly useful for contextualising the human role dimension of my research (Theme 6) and for establishing that binary AI participation governance is the universal paradigm even in the broader human-AI collaboration literature (gap evidence for Themes 2–3). However, it does not address safety-critical architecture, safety state classification, environmental governance, low-resource deployment, or formalisation of safety properties — the core architectural concerns of my dissertation. Its primary value is as **background context on hybrid AI paradigms** and as **additional gap evidence** confirming that graduated, state-conditioned AI governance is absent from the literature. Functional role: **background theory / gap evidence from the human-AI collaboration perspective**.
