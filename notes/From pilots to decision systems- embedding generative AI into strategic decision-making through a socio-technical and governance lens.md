# Literature Review Extraction
## Paper: From Pilots to Decision Systems: Embedding Generative AI into Strategic Decision-Making through a Socio-Technical and Governance Lens

---

## 1. Paper Identity

- **Full title:** From Pilots to Decision Systems: Embedding Generative AI into Strategic Decision-Making through a Socio-Technical and Governance Lens
- **Authors:** Thorn-Ole Saup, Jawad Asghar, Dominik K. Kanbach, Sascha Kraus
- **Year:** 2026 (published online 08 Jan 2026)
- **Venue:** *Journal of Decision Systems*, 35(1), 2597835. DOI: 10.1080/12460125.2025.2597835
- **Type of paper:** Empirical study (qualitative single-case study with 27 semi-structured interviews); theory-building / framework development

---

## 2. Core Contribution

- **Main problem:** Organisations struggle to move generative AI (GAI) beyond pilot projects into routinised inputs for strategic decision-making (SDM). The "pilot-to-decision gap" persists because GAI's analytical affordances outpace organisational governance structures, creating unresolved tensions around provenance, explainability, accountability, and trust.
- **Proposed solution:** A socio-technical, governance-anchored framework that specifies: (1) enablers and barriers of GAI integration, (2) human-AI interaction dynamics (trust, oversight, collaboration), and (3) a four-stage integration pathway from exploration to institutionalisation, governed by four admission gates — quality, provenance, explainability, and accountability — that determine whether AI outputs are admitted into formal strategic deliberation.
- **Main contributions:**
  - Identifies a socio-technical alignment problem between GAI's analytical capabilities and distributed SDM governance
  - Proposes four "admission gates" (quality, provenance, explainability, accountability) as threshold conditions for AI output admissibility in decision forums
  - Articulates a four-stage operationalisation process: Awareness & Exploration → Experimentation & Pilots → Formal Adoption & Integration → Institutionalisation & Transformation
  - Specifies HITL boundary conditions and role reconfigurations across decision phases
  - Synthesises STS, HITL, and XAI as complementary layers within a decision-systems architecture
- **What is novel:** The admission gate logic — treating quality, provenance, explainability, and accountability as measurable design variables (not just metaphors) that sequentially condition whether AI outputs progress from pilots to formally acknowledged decision inputs. The paper also identifies four recurrent failure modes when scaling (gate superficiality, role drift in HITL, metric myopia, pilot habituation).

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | Discusses "hybrid human-AI decision model" where AI augments human judgement, but the hybridity is human-AI collaboration, not rule-based + probabilistic AI architecture |
| Safety-critical AI decision-making | No | Operates in strategic business decision-making (luxury brand management), not safety-critical operational contexts |
| AI governance / control mechanisms | **Yes** | Central focus: admission gates governing what AI outputs enter decision forums; HITL accountability; governance templates; four-stage integration with governance checkpoints |
| Low-resource environments | No | Study context is a well-resourced global luxury conglomerate |
| Decision architecture formalisation | **Partial** | Process model with stages and gates, but no mathematical formalisation — no state variables, no formal gate functions, no action spaces |
| Human role in decision-making | **Yes** | Core theme: human oversight, final decision authority, HITL configurations, role reconfiguration (from analyst to AI interpreter), collaborative augmentation |
| Socio-technical evaluation | **Yes** | Entire paper framed through STS lens; qualitative evaluation of socio-technical conditions for GAI integration; trust, culture, governance as evaluation dimensions |
| Coastal fisheries / maritime domain | No | Luxury brand / multi-brand corporate context |

**Mid-Extraction Relevance Gate:** 3 Yes + 2 Partial → **FULL EXTRACTION** (all 17 sections)

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The paper describes SDM as a multi-layered, governance-bound process spanning problem framing, alternative generation, evaluation, and commitment. It is iterative rather than strictly sequential, integrating structured analytics with scenario planning and strategic-fit checks.
- **Layered architecture / governance structure:** Yes — the framework synthesises three interrelated layers: (1) enablers/barriers, (2) human-AI interaction dynamics, and (3) a four-stage integration process. The admission gates (quality, provenance, explainability, accountability) act as checkpoints governing whether AI outputs progress from one stage to the next and ultimately enter formal strategic deliberation.
- **Rule-based constraints or safety checks before AI decisions:** The admission gates function as pre-deliberation filters. AI-generated outputs are not admitted into strategic forums unless they satisfy gate conditions. However, these gates are organisational/procedural (governance checkpoints, human sign-off, compliance review) rather than deterministic computational rules.
- **Boundary between deterministic control and AI reasoning:** Not formally defined. The paper treats this boundary socially — humans retain final decision authority and apply contextual judgement, while AI provides analytical support. There is no formal computational separation between deterministic and probabilistic processing.
- **Failure modes / fallback behaviour:** Four recurrent failure modes are identified: (1) gate superficiality (explanations exist but are not invoked in deliberation), (2) role drift in HITL (sign-offs diffuse, escalation slows), (3) metric myopia (usage increases without outcome improvement), (4) pilot habituation (pilots persist without entering decision forums). Mitigation involves treating gates as design parameters, assigning single-point accountability per decision episode, and tracking gate-aligned outcomes.

**Summary:** The paper describes a socio-technical governance architecture for AI integration into decision-making, with admission gates serving as the core control mechanism. However, the architecture is organisational and procedural — it governs the *social process* of admitting AI outputs into human deliberation, not the *computational process* of constraining AI reasoning or output generation. There is no formal decision pipeline comparable to E → S → (G(S), A_AI(S)) → AI(E).

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None. The paper develops a qualitative, inductively derived framework (Figure 2) rather than a mathematical model. The four admission gates are conceptualised as "measurable design variables" but are not specified mathematically.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No formal pipeline exists. The paper's "gates" are procedural checkpoints applied by human actors within organisational workflows, not computational functions applied to environmental state vectors. There is no environmental state classification, no gate function G(S) that evaluates a safety state, and no formally defined admissible action space A_AI(S).
- **State-dependent recommendation restriction:** Not present in a formal sense. The paper does not define distinct operational states that condition what types of AI output are permitted. The admission gates are applied uniformly across contexts — the same four criteria (quality, provenance, explainability, accountability) apply regardless of operational conditions. There is no analogue to A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.
- **Safety Dominance Property:** Not defined. No formal guarantee that AI outputs fall within state-determined bounds.
- **Formalisation purpose:** N/A — no formalisation exists. The paper's contribution is a qualitative process model, not a formal specification.

**Key distinction from my research:** The paper's admission gates govern whether AI outputs enter *human* deliberation; my gate function G(S) and action space A_AI(S) govern what the *AI system itself* is permitted to compute and output. Their gates are downstream (post-generation, pre-deliberation); my gates are upstream (pre-generation, conditioning the AI's operational scope).

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** Not present. The paper does not classify operational or environmental conditions into safety levels. The four-stage integration pathway (Awareness → Experimentation → Formal Adoption → Institutionalisation) describes organisational maturity stages, not operational safety states.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No comparison possible. The paper has no environmental state vector, no safety classification function, and no tripartite safety model.
- **AI recommendation scope differentiation across safety levels:** Not present. The paper does not differentiate what AI may recommend based on operational risk. The admission gates apply the same criteria regardless of environmental conditions. There is no concept of a restricted-but-non-empty AI participation mode analogous to CAUTION.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Partial** | The four-stage pathway implies that AI participation increases as organisations mature (from exploration to institutionalisation). Governance checkpoints can block AI outputs from entering deliberation. However, this is an organisational adoption decision, not a real-time operational gate conditioned on environmental state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **Partial** | The admission gates filter what AI outputs are "strategically admissible" based on quality, provenance, explainability, and accountability. This is a form of output-scope governance, but it is applied per-artefact by human reviewers, not as a state-conditioned computational restriction on AI's recommendation space. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | The gates are not conditioned on classified environmental or operational safety state. They are applied based on organisational governance maturity, decision-episode characteristics, and human assessment — not on a computed safety state function S = f(E). |

- **Governance type:** The paper implements a form of graduated organisational governance (from pilot to institutionalised use), with admission gates as quality filters. This is fundamentally different from my two-level governance model: their gates govern the *social admissibility* of AI outputs into human deliberation; my governance pair (G(S), A_AI(S)) governs the *computational scope* of AI reasoning conditioned on environmental safety state.
- **Binary or graduated:** Graduated in the sense that AI integration deepens across four maturity stages, and different gate criteria may be more or less stringently applied depending on decision stakes. But there is no formal graduation tied to classified environmental states.
- **Supports or contradicts two-level governance pair:** Supports the *principle* that AI outputs should be governed (not just generated), and that governance should encompass both "whether AI participates" and "what AI outputs are admissible." However, the paper's governance is organisational and procedural, not formal and state-conditioned. It provides complementary socio-technical context for my research but does not address the same architectural layer.

---

## 8. Human Role in Decision-Making

- **Human involvement:** Central. Humans retain ultimate decision authority throughout. The paper explicitly frames GAI as decision *support*, not decision *automation*.
- **Decision support vs. automation:** Firmly positioned as **decision support**. The paper repeatedly emphasises that AI augments rather than replaces human judgement. The authors state: GAI should be embedded "in ways that augment — not automate — human decision roles."
- **Human-AI interaction:** Three dynamics identified: (1) **Trust and confidence** — built gradually through repeated interactions, shaped by transparency, explainability, and outcome feedback; (2) **Oversight and final decision** — humans review AI outputs critically, with clear sign-off points and escalation pathways; (3) **Collaboration and augmentation** — GAI used as a cognitive partner for brainstorming, scenario exploration, and thought clarification, not for direct decision-making.
- **Human override / escalation:** Yes — explicit escalation pathways, peer review of AI recommendations, human sign-off points in workflows, and guardrails limiting GAI to specific tasks. The four-stage model includes governance checkpoints at each transition.

**Relevance to my research:** The human role described here maps well to the decision-support framing in my architecture (Theme 6). In my system, the fisher makes the final go/no-go decision; AI provides recommendations within the admissible action space. The admission gates in this paper provide a socio-technical complement to my computational governance model — they describe the organisational conditions under which humans accept and act on AI recommendations, which is relevant to my socio-technical evaluation (Theme 7).

---

## 9. System Constraints and Environment

- **Real-world constraints:** The paper identifies several organisational constraints: data fragmentation, legacy system integration challenges, IP and privacy concerns, prompt engineering skill gaps, and hallucination risks. These are enterprise IT constraints, not physical-environment constraints (weather, connectivity, computing hardware).
- **Deployment context:** Real-world organisational deployment within a global luxury group — but the "deployment" is of generative AI tools (ChatGPT-like systems) into strategic workflows, not of safety-critical decision systems into operational environments.
- **Resource-aware design:** Not in the low-resource sense relevant to my research. The paper addresses capability readiness (training, skills, data quality) rather than hardware/connectivity constraints.
- **Edge cases / resource-limited conditions:** Not addressed in the physical/operational sense. The paper discusses organisational edge cases (pilot habituation, gate superficiality) rather than environmental edge cases.

---

## 10. Hybrid AI Taxonomy

- **Type of hybrid AI:** The paper describes a **human-AI augmentation model** — GAI provides analytical and generative capabilities while humans provide contextual interpretation, creativity, ethical judgement, and accountability. This is hybrid in the human-AI collaboration sense, not in the neuro-symbolic or rule-ML pipeline sense.
- **Classification:** Does not fit neatly into the standard taxonomy for my research (neuro-symbolic, supervisory control, constitutional/governance-based, stage-gate, rule-ML pipeline). The closest match is a **governance-based augmentation model** where organisational governance structures (admission gates, HITL accountability) constrain how AI outputs are used, but the AI itself is unconstrained — the constraints operate at the social/organisational layer.
- **Safety enforcement location:** After AI reasoning — the admission gates are post-generation filters applied by human reviewers before outputs enter decision forums. There are no pre-generation computational constraints on what AI may produce.
- **Two-level governance support:** The paper supports the principle of multi-level governance (both participation and output scope are governed) but implements it at the organisational layer, not the computational layer. It does not implement state-conditioned two-level governance.
- **Comparison to my architecture:** My research implements governance computationally (deterministic-gate-first, state-conditioned action space restriction). This paper implements governance organisationally (human reviewers apply admission criteria to AI outputs). These are complementary layers — my architecture governs the AI system's computational behaviour; their framework governs the organisational integration of AI outputs into human decision-making.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparison:** No formal baseline. The paper is a qualitative case study, not a comparative evaluation. There is no system without safety constraints tested against one with constraints.
- **Metrics:** Qualitative themes derived through inductive coding (Gioia method). The paper suggests future metrics: share of decisions with attached provenance, explanation coverage, time to understanding, user trust scores, post-hoc error rates, rework frequency, escalation frequency, and time-to-decision. These are proposed, not measured.
- **Evaluation type:** Single-case qualitative analysis with 27 interviews, triangulated with internal documents and industry reports. No simulation, no prototype testing, no scenario-based evaluation.
- **CAUTION zone testing:** N/A — no safety states are defined, so no testing of intermediate modes.
- **Safety Dominance Property verification:** N/A — no formal property to verify.
- **Graduated vs. binary governance comparison:** Not tested. The paper argues conceptually for graduated governance (four-stage pathway with progressively deeper integration) but does not empirically compare graduated vs. binary approaches.
- **Evaluation gaps:** The paper acknowledges: single-case design limits generalisability; cross-sectional snapshot of a rapidly evolving phenomenon; no causal claims; no inter-coder reliability statistics; sample bias toward advocates/early adopters; no direct observation or trace data.

---

## 12. Key Concepts and Definitions

| Concept | Definition / Description | Relevance |
|---|---|---|
| **Admission gates** | Four threshold conditions (quality, provenance, explainability, accountability) that govern whether AI outputs are admitted into formal strategic deliberation | Conceptually parallel to my governance model — but operates at the socio-organisational layer rather than the computational layer |
| **Strategic admissibility** | The condition under which AI-generated outputs become acceptable evidence in strategic decision-making | Useful framing for the socio-technical evaluation of my system — even if AI outputs are computationally valid (within A_AI(S)), they must also be socially admissible to users |
| **Decision systems** | Multi-level, governance-bound processes integrating analytical artefacts with human oversight under explicit governance | Provides theoretical framing for positioning my architecture as a "decision system" |
| **HITL (Human-in-the-loop)** | Collaborative arrangements where explainability, transparency, and trust frame AI output usage while accountability remains with humans | Aligns with my architecture's decision-support positioning (fisher decides) |
| **Pilot-to-decision gap** | The persistent failure of organisations to scale AI from isolated pilots to routinised decision inputs | Could be cited as a general challenge that my architecture must also address |
| **Gate superficiality** | Failure mode where explanations and provenance exist formally but are not actually invoked during deliberation | Relevant to socio-technical evaluation — even well-designed computational gates could suffer from this if users ignore them |
| **STS (Socio-Technical Systems)** | Theory emphasising co-evolution of technology, organisation, culture, and processes | Background theory for my Theme 7 (socio-technical evaluation) |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Single-case design — transferability constrained by one organisation's governance, data, and capability profile
  - Cross-sectional snapshot of rapidly evolving capabilities and policies
  - Semi-structured interviews subject to self-report, recall, and social desirability biases
  - No direct observation or digital trace data
  - No formal inter-coder reliability statistics
  - Sample biased toward advocates and early adopters; dissenting voices underrepresented
  - Process model is explanatory, not causal — does not identify whether gates actually improve decision quality

- **Unsolved problems / future work:**
  - Whether admission gates improve decision quality or speed (requires experimental/quasi-experimental designs)
  - Binding thresholds for gate conditions remain undefined
  - Longitudinal trajectories from exploration to institutionalisation (including reversals and failures) not captured
  - Comparative designs across governance regimes (centralised vs. decentralised) and sectors (varying regulatory intensity) needed
  - Trust, explainability, provenance, and accountability need validated psychometric scales combined with behavioural/log-based measures

- **Alignment with my research gaps:**
  - The paper does **not** identify the lack of a two-level state-conditioned governance model as a gap — its governance operates at the organisational, not computational, layer
  - The paper does **not** identify the need for a CAUTION mode or state-conditioned AI recommendation restriction
  - The paper does **not** address safety-critical operational contexts or the Safety Dominance Property
  - **However**, the paper's admission gates provide a socio-technical complement to my computational governance — my architecture addresses the upstream question (what may AI compute?), while their framework addresses the downstream question (under what conditions do humans accept AI outputs into deliberation?)

---

## 14. Methodology Notes

- **Research method:** Qualitative single-case study (Yin, 2018) with structured inductive coding (Gioia et al., 2013). Data from 27 semi-structured interviews, internal documents, and industry reports.
- **Alignment with DSR pipeline:** Does not align. The paper uses qualitative theory-building methodology, not Design Science Research. There is no design → formalise → prototype → evaluate cycle.
- **Methodological insights for my research:**
  - The Gioia method (first-order concepts → second-order themes → aggregate dimensions) could inform the qualitative component of my socio-technical evaluation (Theme 7)
  - The concept of "admission gates" as measurable design variables suggests a way to operationalise the socio-technical evaluation of my governance model — testing whether fishers actually understand and trust the SAFE/CAUTION/UNSAFE classifications and the resulting AI recommendation scope
  - The failure mode taxonomy (gate superficiality, role drift, metric myopia, pilot habituation) provides useful evaluation lenses for my system's real-world deployment

---

## 15. Quotable / Citable Points

1. **GAI as decision support, not oracle:** The paper reframes GAI "not as an autonomous oracle but as decision support within decision systems, clarifying conditions under which creative or efficient outputs become strategically admissible" (Abstract/Section 5.1). — *Useful for positioning my architecture as decision support*

2. **Admission gates as governance mechanism:** The paper introduces "four admission gates — quality, provenance, explainability, and accountability — as decisive preconditions for admitting AI outputs into formal deliberation" (Section 6). — *Citable as a socio-technical complement to my computational governance*

3. **Gate superficiality failure mode:** The paper identifies that "explanations and provenance exist but are not invoked in deliberation" as a recurrent failure mode (Section 5.3). — *Relevant warning for my socio-technical evaluation*

4. **Pilot-to-decision gap:** The paper addresses how "organisations are urged to rely on GAI to improve strategic choices, while the socio-organisational conditions of SDM systematically impede such usage" (Section 1). — *Background motivation for why governance frameworks matter*

5. **Sequential gate conditioning:** The paper argues "admissibility follows a sequence in which the value of later gates (explainability, accountability) is conditioned by early gates (quality, provenance)" (Section 5.2). — *Interesting parallel to my containment relationship A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅*

---

## 16. Relation to My Research and Positioning

- **Governance levels implemented:** Partial Level 1 (organisational decisions about whether AI participates) and Partial Level 2 (admission gates filtering what AI outputs enter deliberation). Neither level is state-conditioned or computationally formalised.
- **State-conditioned governance:** No. Gates are applied based on organisational governance maturity and decision-episode characteristics, not classified environmental safety state.
- **Proximity to (G(S), A_AI(S)):** Distant at the formal/computational level. The paper's admission gates operate at the organisational/social layer — they govern human acceptance of AI outputs, not the AI system's computational scope. However, the conceptual structure is parallel: both my research and this paper recognise the need for multi-level governance that controls both AI participation and AI output scope.
- **Safety Dominance Property:** Not defined, not addressed.
- **Gap my research fills:** This paper demonstrates that even in well-resourced organisational contexts, AI outputs require governance before entering human deliberation. But the governance described is entirely post-generation and human-applied. My research fills the gap of **pre-generation, computationally enforced** governance that conditions what the AI system itself is permitted to recommend, based on classified environmental safety state. Where this paper asks "should humans accept this AI output?", my research asks "should the AI system have been allowed to generate this output at all?"

**Positioning paragraph:** Saup et al. (2026) provides a **socio-technical evaluation framework and governance background** that complements my research at the organisational layer. Their four admission gates (quality, provenance, explainability, accountability) address the downstream question of whether human decision-makers accept AI outputs into formal deliberation — a question my architecture must also answer in its socio-technical evaluation phase (Theme 7). The paper's STS/HITL/XAI synthesis provides theoretical grounding for evaluating whether fishers in my target context understand, trust, and appropriately act on AI recommendations generated within the state-conditioned admissible action space. Their concept of "strategic admissibility" parallels my concept of "operational admissibility" — in my architecture, AI outputs are computationally admissible only if they fall within A_AI(S), and socially admissible only if users understand and trust the governance structure. The paper's failure mode taxonomy (gate superficiality, role drift, metric myopia, pilot habituation) offers useful evaluation lenses for my system's deployment context. However, the paper operates entirely at the organisational governance layer with no computational formalisation, no environmental state classification, no state-conditioned recommendation restriction, and no Safety Dominance Property — confirming that the gap between socio-technical AI governance theory and formal computational governance architecture remains open. My research bridges this gap by formalising the governance pair (G(S), A_AI(S)) as a computational mechanism that complements the organisational governance structures described by Saup et al.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** The paper is directly relevant to three of my research themes (AI governance, human role, socio-technical evaluation) and partially relevant to two more (hybrid AI, decision architecture). It provides useful conceptual vocabulary (admission gates, strategic admissibility, pilot-to-decision gap), a socio-technical evaluation framework that could inform my Theme 7, and a failure mode taxonomy relevant to deployment evaluation. However, it operates entirely at the organisational/qualitative layer with no computational formalisation, no environmental state classification, no state-conditioned governance, and no Safety Dominance Property. It does not address safety-critical contexts, low-resource environments, or the specific two-level governance gap that defines my contribution. Its primary value is as **socio-technical background and evaluation-framework reference** — not as an architectural antecedent, baseline comparator, or gap-evidence paper for the core computational contribution.
