## Literature Review Extraction: Madsen & Kim (2024)

---

### 1. Paper Identity

- **Full title:** A state-of-the-art review of AI decision transparency for autonomous shipping
- **Authors:** A. N. Madsen, T. E. Kim
- **Year:** 2024
- **Venue:** Journal of International Maritime Safety, Environmental Affairs, and Shipping, 8(1–2), 2336751
- **Type:** Systematic literature review (22 papers analysed via thematic analysis following PRISMA guidelines)

---

### 2. Core Contribution

- **Problem:** The introduction of maritime autonomous surface ships (MASSs) shifts navigators from direct control to supervising AI collision avoidance systems or managing operations from remote operation centres (ROCs). If AI integration reduces human control or leaves humans out of the loop, safety may be jeopardised. AI systems' decisions need to be transparent, interpretable, and accountable to human operators.
- **Solution:** A systematic review of state-of-the-art research on traffic alerts and collision avoidance systems with respect to AI decision transparency for autonomous shipping.
- **Main contributions:**
  1. Identification of three main groups of decision transparency in the literature: **strategies** (human factors, risk assessment, design principles), **visualization** (colour coding, bounding boxes, route displays), and **technology** (system situational awareness, route exchange, identification signalling).
  2. A thematic synthesis of 22 papers revealing how researchers have treated human–machine collaboration for MASS.
  3. Identification of gaps: a lack of focus on onboard (vs. ROC) decision transparency, and no studies evaluating how proposed transparency approaches affect operators' or AI systems' situational awareness.
- **Novelty:** First systematic review specifically focused on AI decision transparency for autonomous shipping, bridging XAI literature with maritime collision avoidance practice.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Several reviewed papers combine rule-based COLREGs compliance with AI-driven collision avoidance (e.g., Huang et al. 2020, NAVDEC systems). The review discusses systems that integrate deterministic maritime rules with AI reasoning, though this is not the review's analytical focus. |
| Safety-critical AI decision-making | Yes | The entire review concerns safety-critical collision avoidance for autonomous ships. It identifies risk management strategies (STPA, STPA-Cog), operating envelope monitoring, and proactive/reactive safety mechanisms. |
| AI governance / control mechanisms | Partial | The review addresses *how* human operators understand and override AI decisions (trust, transparency, human override), and discusses systems that display optimal vs. dangerous solutions. However, it does not formalise governance as a gate function or admissible action space. The concept of an "operating envelope" with safety constraints (Utne et al. 2020) touches on participation governance. |
| Low-resource environments | No | The focus is on autonomous shipping with advanced sensor systems, not low-resource deployments. |
| Decision architecture formalisation | Partial | Hansen et al. (2020) — reviewed within this paper — proposed a formal SA framework using discrete event system (DES) theory with deterministic automata. Van de Merwe et al. (2023) proposed a layered transparency approach. However, no formal model comparable to E → S → G(S) → A_AI(S) is presented or synthesised. |
| Human role in decision-making | Yes | A core theme. The review extensively addresses human–AI collaboration, trust, situational awareness, human override, operator compatibility, the shift from navigator to supervisor, and the need for transparency to support human decision authority. |
| Socio-technical evaluation | Yes | Several reviewed papers conducted empirical studies with operators (simulator studies, interviews, cognitive task analysis). The review highlights the gap between designers' constructions of human–AI collaboration and navigators' actual experiences. |
| Coastal fisheries / maritime domain | Partial | Maritime domain (autonomous shipping, collision avoidance), but not fisheries. The domain context (vessels, COLREGs, maritime risk) is adjacent to coastal fisheries but operates at a different scale and technology level. |

**Mid-Extraction Relevance Gate:** 3 Yes (safety-critical AI, human role, socio-technical evaluation) → **FULL EXTRACTION.**

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The reviewed literature presents various architectures, but the review itself does not propose a unified decision architecture. The systems discussed generally follow a **perception → risk assessment → decision → action** pipeline for collision avoidance. The review organises the transparency dimension into three layers: strategies (how to approach transparency), visualization (how to display it), and technology (what technical mechanisms enable it).
- **Layered architecture:** Van de Merwe et al. (2023) proposed a **layered approach to transparency** enabling remote operators to observe different facets of a system's input parameters, reasoning, decisions, and actions. This is a *transparency layer* model, not a *safety governance layer* model. Hansen et al. (2020) proposed separating a system's understanding of a situation from its anticipation of the near future using deterministic automata — a form of layered SA architecture.
- **Rule-based constraints before AI decisions:** Multiple reviewed papers discuss COLREGs compliance as a deterministic constraint on AI collision avoidance (Martelli et al. 2023, NAVDEC systems). Utne et al. (2020) proposed early warnings on possible violations of an autonomous ship's operating envelope based on safety constraints — a proactive rule-based check.
- **Boundary between deterministic control and AI reasoning:** Not explicitly formalised in the review. The reviewed systems generally apply COLREGs as deterministic rules that constrain AI-generated collision avoidance manoeuvres, but the boundary is described qualitatively rather than formally.
- **Failure modes and fallback:** The review emphasises human override capability as the primary fallback mechanism. Utne et al. (2020) proposed reactive risk management giving operators additional time for crisis intervention. Dugan et al. (2023) categorised verification requirements into failure handling and integration testing.

**Key distinction from my architecture:** The transparency layers discussed here concern *what information the human sees about AI decisions*, not *what the AI is permitted to recommend under varying safety states*. The governance question in this review is "Can the human understand and override the AI?" — not "What is the AI formally permitted to output under classified environmental conditions?"

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** The review itself does not present a formal model. Among the reviewed papers:
  - Hansen et al. (2020) used **discrete event system (DES) theory** with deterministic automata to model system SA, integrating Endsley's three-level SA model (perception, comprehension, projection).
  - Wu et al. (2021) applied **prospect theory** (Kahneman & Tversky 1979) to model individual navigators' risk appetite and maneuvering behaviour.
  - Utne et al. (2020) proposed an online risk model with proactive and reactive components based on safety constraints — conceptually formal but not presented as a mathematical pipeline in this review.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - **Environmental inputs (E):** Reviewed systems process maritime traffic data, sensor data, CPA/TCPA calculations, and environmental conditions. These are functionally analogous to the environmental state vector but not formalised as a unified vector.
  - **Safety state classification S = f(E):** Colour coding schemes (Ożoga & Montewka 2018) use five colours from "no hazard" to "extreme danger" based on TCPA/CPA — a form of risk classification that maps environmental inputs to discrete risk levels. This is conceptually close to S = f(E) but is used for *display purposes* (telling the human what risk level exists), not for *AI governance* (restricting what the AI may recommend).
  - **Gate function G(S):** The concept of an "operating envelope" with safety constraints (Utne et al. 2020) implies a boundary beyond which AI should not operate autonomously. However, this is not formalised as G(S) = 0/1.
  - **Admissible action space A_AI(S):** No equivalent. No reviewed paper restricts the *type* of AI recommendation based on classified safety state. The systems either recommend collision avoidance manoeuvres (full scope) or rely on the human to override.

- **State-dependent recommendation restriction:** Not present. Colour coding varies the *visual display* by risk level, but does not vary the *AI's permitted output types*. The AI generates the same types of recommendations regardless of risk classification.
- **Safety Dominance Property:** Not defined or approximated. No formal guarantee that AI outputs fall within state-determined bounds.
- **Formalisation purpose:** Where formalisation exists (Hansen et al. DES model), it is used for system design and analysis, not for proving safety properties.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** Yes — but for *visualisation*, not for *AI governance*:
  - Ożoga & Montewka (2018): Five-colour scheme from no hazard to extreme danger, based on TCPA/CPA.
  - Pietrzykowski et al. (2017): Colour-coded rosette indicating safe and dangerous zones.
  - Zhao et al. (2023): Colour-coded target ships by collision risk level.
  - Van de Merwe et al. (2023): Traffic-light colour coding based on risk evaluation for maneuverability indicators.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The risk classification schemes are structurally analogous — they map environmental/traffic conditions to discrete risk levels. Some even use traffic-light coding (green/amber/red) that maps approximately to SAFE/CAUTION/UNSAFE. However, these classifications serve *display* and *human awareness* functions, not *AI behavioural governance* functions.
- **Differentiated AI recommendation scope across safety levels:** **No.** This is the critical gap. The colour coding tells the *human* the risk level, but the *AI* generates the same types of output (route recommendations, collision avoidance manoeuvres) regardless of the classified risk level. There is no CAUTION mode where AI still participates but with restricted output types. The human is expected to exercise their own judgement about whether to follow AI recommendations under varying risk levels — the architecture does not enforce this structurally.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | Utne et al. (2020) proposed early warnings when an autonomous ship approaches operating envelope boundaries — implying a boundary beyond which AI should not operate autonomously. Human override mechanisms throughout the reviewed literature function as manual Level 1 governance (human can switch AI off). However, no *automated* participation gate conditioned on classified environmental state is described. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | No reviewed paper restricts the types of recommendations AI may generate based on safety state. AI collision avoidance systems generate the same output types (routes, manoeuvres, speed changes) regardless of classified risk level. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Risk classification exists for visualisation but does not govern AI participation or advisory scope. |

- **Binary AI switch or graduated governance?** The reviewed literature implicitly assumes a binary model: AI is either providing recommendations or the human has overridden it. There is no graduated mode where AI continues operating but with a restricted recommendation scope.
- **Level 2 governance:** Not implemented in any reviewed paper.
- **Support or contradiction for (G(S), A_AI(S))?** The review **strongly supports the motivation** for state-conditioned governance without implementing it. The reviewed literature demonstrates that: (a) risk classification is already performed (colour coding by TCPA/CPA), (b) transparency layers depend on situation type and complexity (Van de Merwe et al. 2023), and (c) the information needed to understand a system depends on the degree of human oversight and time available. These findings imply that AI behaviour itself should also vary by classified state — but no reviewed paper takes this step. The gap is precisely the one my architecture fills.

---

### 8. Human Role in Decision-Making

- **Human involvement:** The human is the final decision-maker in all reviewed systems. The systems are positioned as **decision support**, not decision automation. Even in autonomous ship contexts, the review emphasises that humans (either onboard or in ROCs) must be able to understand, validate, and override AI decisions.
- **System positioning:** Decision support with human override. Huang et al. (2020) explicitly designed a system to display optimal decisions and highlight dangerous solutions, enabling operators to confirm or propose alternatives.
- **Human–system interaction:** Through visualisation layers: colour-coded risk displays, bounding boxes showing what the AI detects, route displays showing recommended manoeuvres, and textual/graphical safety assessments. Van de Merwe et al. (2023) proposed a layered transparency approach showing input parameters, reasoning, decisions, and actions.
- **Override mechanisms:** Central to the review's findings. The review emphasises that operators must be able to intervene, with transparency enabling informed intervention. However, the review also notes that in complex situations, operators may not comprehend a system's reasoning and may intervene inappropriately.

---

### 9. System Constraints and Environment

- **Real-world constraints:** The review acknowledges that MASS systems must function in varying operating environments — open waters, coastal areas, port approach areas (Pietrzykowski 2018). Traffic density varies significantly, and systems designed for open sea may not function appropriately in port approach areas.
- **Deployment context:** Mixed. Some reviewed papers are conceptual, some use simulation, and some involve prototype testing with operators. No fully deployed operational MASS collision avoidance system is evaluated in the review.
- **Resource-aware design:** Not a focus. The reviewed systems assume modern sensor suites, computing infrastructure, and trained operators in ROCs. No consideration of limited connectivity, low computing power, or low-literacy users.
- **Edge cases:** The review notes that the adequacy of transparency approaches depends on circumstances — simple scenarios may be self-explanatory, but complex multi-vessel situations may overwhelm operators. This is an important edge-case consideration.

---

### 10. Hybrid AI Taxonomy

- **Hybrid approach:** Several reviewed papers implement what could be classified as **rule-ML pipeline** or **supervisory control** approaches:
  - COLREGs-compliant collision avoidance systems combine deterministic maritime rules with AI-generated manoeuvres (Martelli et al. 2023, NAVDEC systems).
  - Utne et al. (2020) proposed a supervisory risk control model where safety constraints define the operating envelope and AI operates within it.
  - Hansen et al. (2020) combined deterministic automata (DES theory) with Endsley's SA model.
- **Safety enforcement location:** Generally **alongside** AI reasoning — safety constraints (COLREGs, operating envelope) are applied concurrently with AI decision-making, and the human provides post-hoc override.
- **Two-level governance support:** The reviewed literature supports single-level governance at most (Level 1: human can override AI). No paper implements two-level governance where both AI participation and AI advisory scope are governed by safety state.
- **Comparison to my architecture:** The reviewed systems assume the human provides the "graduated governance" through their own judgement — risk colour coding informs the human, who then decides how much to trust the AI recommendation. My architecture formalises this governance structurally within the system itself, removing reliance on human judgement for scope restriction.

---

### 11. Baseline Comparison and Evaluation

- **Baseline comparison:** Most reviewed papers compare their proposed visualisation or transparency approaches against prior systems or operator performance without transparency features. No paper compares governance models (binary vs. graduated).
- **Evaluation methods:** Simulator studies (Man et al. 2018, Zhao et al. 2023, Madsen et al. 2023), interviews and cognitive task analysis (Van de Merwe et al. 2022, 2023), case studies (Cheng et al. 2023), conceptual frameworks (Utne et al. 2020, Porathe 2022).
- **CAUTION zone testing:** Not applicable — no paper defines or tests a CAUTION mode.
- **Safety Dominance Property verification:** Not applicable — no formal safety property is defined or tested.
- **Graduated vs. binary governance comparison:** Not performed in any reviewed paper.
- **Evaluation gaps:** The review explicitly identifies that *none* of the reviewed studies evaluated how proposed transparency approaches affect operators' or systems' SA. It also notes a lack of focus on onboard (vs. ROC) transparency and a lack of real-world operational testing.

---

### 12. Key Concepts and Definitions

- **AI decision transparency:** The quality of an AI system's "thinking" and decisions being transparent to human operators, with alternative decisions easy to execute. Defined specifically for navigation and collision avoidance contexts.
- **Situational awareness (SA):** Referenced extensively but the review notes that most papers fail to clearly define it. Endsley's three-level model (perception, comprehension, projection) is the implicit framework.
- **Layered transparency:** Van de Merwe et al. (2023) proposed observing different facets of a system's input parameters, reasoning, decisions, and actions — transparency as layers that can be selectively engaged.
- **Operating envelope:** (Utne et al. 2020) The bounded set of environmental and operational conditions within which an autonomous ship is approved to operate, with safety constraints defining the boundaries.
- **STPA-Cog:** (Cheng et al. 2023) Extension of System-Theoretic Process Analysis integrating human cognitive modelling for human–system collaboration safety analysis.
- **Risk Appetite (RA) approach:** (Wu et al. 2021) Tailoring AI collision avoidance to individual navigator risk preferences using prospect theory.
- **Minimal explainability:** (Madsen et al. 2023) The baseline transparency layer of simply displaying system-recommended routes/manoeuvres.

---

### 13. Limitations and Unsolved Problems

**Stated limitations of the review:**
1. Limited to 22 papers — the field is still nascent with few empirical studies.
2. Focus is predominantly on ROC-based transparency; onboard decision transparency for manned MASSs is surprisingly underexplored.
3. Most reviewed papers are conceptual or simulation-based; real-world deployment evidence is lacking.

**Unsolved problems / future work:**
1. No study has evaluated how proposed transparency approaches affect operators' or AI systems' SA.
2. The information needed to understand a system depends on situation type, degree of human oversight, complexity, and time available — but no framework governs this adaptively.
3. Systems must distinguish between open water, coastal, and port approach operations — but no adaptive governance responds to these domain differences.

**Alignment with my research gaps:**
- **No two-level governance model.** The reviewed literature provides risk classification for *visualisation* but not for *AI behavioural governance*. The human is expected to infer governance (how much to trust the AI) from the displayed risk level — this is not formalised or enforced structurally.
- **No CAUTION mode.** All reviewed systems assume full AI advisory scope regardless of classified risk. The colour coding tells the human the situation is dangerous, but the AI still recommends the same types of outputs. My architecture would restrict the AI's recommendation types under elevated risk, removing reliance on human judgement for scope restriction.
- **No Safety Dominance Property.** No formal guarantee that AI outputs are bounded by state-classified constraints.
- **The "operating envelope" concept (Utne et al. 2020) is the closest antecedent** to my gate function but operates as a binary boundary (inside/outside envelope), not as a graduated three-state classifier.

---

### 14. Methodology Notes

- **Method:** Systematic literature review following PRISMA guidelines, with thematic analysis using Braun & Clarke's (2012) six-phase approach. Three databases (Scopus, Web of Science, EBSCO). 1564 items found → 22 included.
- **Alignment with my DSR pipeline:** Limited. This is a review paper, not a design science study. However, its thematic synthesis of transparency strategies and identification of gaps could inform the socio-technical evaluation dimension of my research (Theme 7).
- **Methodological insights:** The thematic analysis approach (strategies / visualization / technology) is a useful categorisation framework. The identification that transparency requirements vary by situation type, complexity, and time available supports the argument for state-conditioned governance — if transparency needs vary by state, AI behaviour should also vary by state.

---

### 15. Quotable / Citable Points

1. **Layered transparency depends on situation type:** Van de Merwe et al. (2023) found that "the information needed to understand a system depended on the type of situation, the degree of human oversight, the complexity of the situation, and/or the time available to intervene" — supports the argument that AI governance should also be state-dependent. (Design principles section)

2. **Colour coding as risk classification for display:** Multiple reviewed papers implement traffic-light or multi-level colour coding based on TCPA/CPA (Ożoga & Montewka 2018; Van de Merwe et al. 2023; Zhao et al. 2023) — demonstrating that discrete risk classification is already standard practice in maritime AI, but is used only for visualisation, not for governing AI output scope. (Visualization section)

3. **Operating envelope as safety boundary:** Utne et al. (2020) proposed "early warnings on possible violations of an autonomous ship's operating envelope based on safety constraints" — the closest antecedent to the gate function concept, but operating as a binary boundary. (Risk management section)

4. **Gap between designer intent and navigator experience:** Veitch et al. (2022) revealed "a discrepancy between designers' constructions of human–AI collaboration and navigators' own accounts in the field" — supports the need for socio-technical evaluation of AI governance architectures. (Design principles section)

5. **No SA evaluation of transparency approaches:** The review notes that "none of the studies identified in this review evaluated how proposed strategies, visualization, or technology affect systems' or individual operators' SA" — a significant evaluation gap. (Conclusions)

---

### 16. Relation to My Research and Positioning

- **Level 1 governance:** Partially present through human override mechanisms and the operating envelope concept, but not formalised as an automated gate function.
- **Level 2 governance:** Not implemented. AI generates the same output types regardless of classified risk level.
- **State-conditioned?** Risk classification exists (colour coding) but conditions only *display*, not *AI behaviour*.
- **Two-level governance pair (G(S), A_AI(S))?** Falls significantly short. The reviewed literature demonstrates the building blocks (risk classification, transparency layers, operating envelopes) but does not assemble them into a unified state-conditioned governance architecture.
- **Safety Dominance Property?** Not defined or approximated.
- **Gap my research addresses:** The review reveals that maritime AI already classifies environmental risk into discrete levels (for display purposes) and already acknowledges that transparency requirements vary by situation — but no system uses this classification to govern AI behaviour itself. My architecture takes the existing risk classification paradigm and extends it from a *display function* to a *governance function*: the same environmental state that determines what colour the operator sees also determines what the AI is formally permitted to recommend.

**Positioning paragraph:** Madsen & Kim (2024) provides a comprehensive synthesis of the state of the art in AI decision transparency for autonomous shipping, directly relevant to the maritime domain context and human-role themes of my research. The review demonstrates that risk classification into discrete levels (via colour coding) is already common practice in maritime collision avoidance systems, and that transparency requirements vary by situation type and complexity. These findings strongly motivate my architecture: if environmental risk classification is already performed for display, and if transparency needs are acknowledged to be state-dependent, then AI *governance* should also be state-dependent. The review's finding that no studied system restricts AI output scope based on classified risk provides direct gap evidence for the two-level governance model. The operating envelope concept (Utne et al. 2020) is the closest antecedent to Level 1 governance (G(S)), but remains binary (inside/outside envelope) and does not extend to Level 2 (advisory scope restriction). This paper is best positioned as **domain background and gap evidence** — confirming that the maritime sector already performs discrete risk classification but uses it only for human awareness, not for formal AI behavioural governance.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** The paper directly addresses the maritime domain with safety-critical AI decision-making and human-role themes. It provides valuable domain background showing that discrete risk classification (colour coding) is standard practice in maritime AI but is used only for visualisation, not for AI governance — directly evidencing the gap my architecture fills. The operating envelope concept, layered transparency, and situation-dependent information needs all support the motivation for state-conditioned governance. However, the paper does not propose or formalise any governance architecture, does not define formal models comparable to E → S → G(S) → A_AI(S), and does not address low-resource environments or fisheries specifically. Its primary value is as domain gap evidence and background on the human role in maritime AI decision support, not as an architectural antecedent or formal comparator.
