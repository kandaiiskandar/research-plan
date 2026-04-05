# Literature Review Extraction
## Paper: Implementing Artificial Intelligence in Safety-Critical Systems during Operation: Challenges and Extended Framework for a Quality Assurance Process

---

## 1. Paper Identity

- **Full title:** Implementing Artificial Intelligence in Safety-Critical Systems during Operation: Challenges and Extended Framework for a Quality Assurance Process
- **Authors:** Niclas Flehmig, Mary Ann Lundteigen, Shen Yin (all NTNU, Norway)
- **Year:** 2024 (IECON 2024 — 50th Annual Conference of the IEEE Industrial Electronics Society)
- **Venue:** IEEE IECON 2024. DOI: 10.1109/IECON55916.2024.10906021
- **Type of paper:** Framework/conceptual paper with literature review (extends ISO/IEC TR 5469)

---

## 2. Core Contribution

- **Main problem:** AI deployed in safety-critical systems may experience performance degradation during operation (due to concept drift, data drift, outliers, temporal model degradation) even when training-time performance was acceptable. ISO/IEC TR 5469 provides a framework for AI in safety-critical systems but does not cover quality assurance during operation.
- **Proposed solution:** An extended framework that adds two components to ISO/IEC TR 5469: (1) **AI monitoring** (non-AI, using statistical methods to detect outliers, concept drift, and measure performance), and (2) **AI updating** (offline re-training with dynamic data selection). Additionally, a **traffic-light degradation indexing framework** with three levels (green/orange/red) that classifies AI degradation severity and provides actionable recommendations to the human supervisor.
- **Main contributions:**
  - Literature review of operational challenges for AI in safety-critical systems (concept drift, temporal degradation, catastrophic forgetting, label scarcity)
  - Extended framework (Figure 1) adding monitoring and updating components to ISO/IEC TR 5469's safety-related system architecture
  - **Traffic-light degradation index** (Figure 2): three-level classification (Level 1/green, Level 2/orange, Level 3/red) governing system behaviour — AI stays in control at Levels 1-2, switches to backup at Level 3
  - Adjusted simplex architecture enabling seamless switching between AI and backup safety system
  - Principle that AI monitoring should use non-AI technologies
- **What is novel:** The traffic-light degradation indexing framework for AI in safety-critical systems. The authors state: "To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner."

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Yes** | The architecture explicitly combines AI component (probabilistic) with non-AI supervisory component, non-AI monitoring, limiting logic (enforcing output restrictions), and non-AI backup safety system (deterministic logic). |
| Safety-critical AI decision-making | **Yes** | Central focus. Safety-critical systems where failure causes potential harm to people or environment. |
| AI governance / control mechanisms | **Yes** | Traffic-light index governs system behaviour: AI stays in control (green/orange) or switches to backup (red). Supervisory component evaluates monitoring, decides on re-training. Limiting logic enforces output restrictions. |
| Low-resource environments | No | Targets industrial safety-critical systems (E/E/PE systems). No discussion of resource constraints. |
| Decision architecture formalisation | **Partial** | Framework with defined components, flows, and the three-level traffic-light index. But not mathematically formalised — no state variables, functions, or formal proofs. |
| Human role in decision-making | **Yes** | Human operator is the supervisor who evaluates monitoring output, decides on switching to backup, triggers re-training, and makes informed decisions using the traffic-light index. AI positioned as "assistant rather than autonomous tool." |
| Socio-technical evaluation | No | No empirical or socio-technical evaluation. |
| Coastal fisheries / maritime domain | No | General industrial safety-critical systems. |

**Mid-Extraction Relevance Gate:** 4 Yes + 1 Partial → **FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Decision-making structure:** The extended framework (Figure 1) has a layered architecture: data stream → AI component (performs safety function) → limiting logic → switch → output action. In parallel: AI monitoring (non-AI) evaluates AI component and data stream → supervisory component (non-AI) evaluates monitoring → decides on switching to backup or triggering re-training. The backup safety system (non-AI, deterministic logic or human task) provides fallback.
- **Layered architecture / governance structure:** Yes — three-layer governance: (1) **AI component** performs the safety function, (2) **Monitoring + supervisory component** evaluates AI performance and data quality, (3) **Backup safety system** provides deterministic fallback. The traffic-light index mediates between layers 1 and 2.
- **Rule-based constraints or safety checks:** Yes — the "limiting logic" enforces restrictions on AI outputs to prevent unsafe behaviour. The monitoring component uses non-AI statistical methods. The backup safety system uses deterministic logic.
- **Boundary between deterministic control and AI reasoning:** Explicitly defined. The AI component performs the safety function (probabilistic). The supervisory component, monitoring, and backup system are all non-AI (deterministic/statistical). The switch component enables transition between AI and backup.
- **Failure modes / fallback behaviour:** Explicitly addressed. The adjusted simplex architecture enables seamless switching from AI to non-AI backup. The traffic-light index triggers switching at Level 3 (red). The backup system focuses on "transition to a safe (degraded) state only."

**Key parallel to my architecture:** The three-level traffic-light design maps directly to my tripartite safety state model. The architecture's structure (AI constrained by non-AI monitoring and supervisory control, with deterministic backup) is conceptually aligned with my hybrid deterministic-gate + probabilistic-AI approach.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None in the mathematical sense. The framework is presented as an architectural diagram (Figure 1) and a traffic-light classification (Figure 2) with verbal descriptions. No equations, state variables, or formal proofs.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**

| My Architecture | Flehmig et al. |
|---|---|
| E (environmental state vector) | Data stream from controlled system and environment |
| S = f(E) (safety state classification) | Traffic-light index: weighted score from performance metrics, outlier detection, concept drift detection → Level 1/2/3 |
| G(S) = 0 when UNSAFE | Level 3 (red): switch to backup safety system (AI blocked) |
| G(S) = 1 when SAFE/CAUTION | Level 1-2 (green/orange): AI stays in control |
| A_AI(S) varying by state | **Not present** — AI recommendation scope does not vary between Level 1 and Level 2; both keep AI as safety function |
| Safety Dominance Property | Not formally defined |

- **State-dependent recommendation restriction:** **Partially present but not at Level 2 governance.** The traffic-light index creates three distinct states, and the system behaves differently at Level 3 (switch to backup) vs. Levels 1-2 (AI stays in control). However, **there is no differentiation between Level 1 and Level 2 in terms of what the AI may recommend.** At both levels, the AI operates as the safety function without restriction. The difference is only in the supervisory response: Level 1 = routine checks; Level 2 = thorough checks, investigate root cause, possibly re-train. This means the traffic-light system governs **supervisory behaviour**, not **AI recommendation scope**.
- **Safety Dominance Property:** Not formally defined.

**Critical gap relative to my research:** The traffic-light index classifies degradation severity into three levels but does not use the intermediate level (orange/Level 2) to restrict what the AI may recommend. Level 2 triggers supervisory investigation, not AI scope restriction. My CAUTION mode does both: it triggers heightened human awareness AND restricts the AI's admissible recommendation space (A_AI(CAUTION) ⊂ A_AI(SAFE)). Flehmig et al.'s Level 2 operates only on the supervisory/human side, not the AI governance side.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** **Yes — three levels (traffic-light):**
  - **Level 1 (Green):** AI shows no significant degradation. AI stays as safety function. Routine checks recommended.
  - **Level 2 (Orange):** AI shows signs of performance degradation and/or change in underlying data. AI stays as safety function. Supervisory component must conduct thorough checks, investigate root cause, re-train if necessary.
  - **Level 3 (Red):** AI degradation surpassed safety threshold and/or significant change in underlying data. Switch to conventional non-AI safety controller. Analyse root cause, re-training recommended.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:**

| My Model | Flehmig et al. |
|---|---|
| SAFE: G(S) = 1, A_AI = full | Level 1 (Green): AI operates, full scope |
| CAUTION: G(S) = 1, A_AI = restricted | Level 2 (Orange): AI operates, **full scope** (only supervisory response changes) |
| UNSAFE: G(S) = 0, A_AI = ∅ | Level 3 (Red): AI blocked, backup takes over |

- **AI recommendation scope differentiation:** **Not present across levels.** The AI's recommendation scope is identical at Level 1 and Level 2. The traffic-light index governs the *supervisory response intensity*, not the *AI's operational scope*. This is the same binary AI governance (on/off) seen across all surveyed literature, with the tripartite classification applied only to the human supervisory layer.

**This paper is the closest structural precedent to my tripartite safety state but confirms the CAUTION mode gap.** It implements a three-level classification, but the intermediate level changes only human supervisory behaviour, not AI recommendation scope.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Yes** | The traffic-light index at Level 3 (red) triggers switching to non-AI backup → AI participation blocked. At Levels 1-2, AI participates. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **No** | AI recommendation scope does not vary across levels. The AI generates the same outputs regardless of whether the system is at Level 1 or Level 2. Only the supervisory response varies. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified state? | **Partial** | Level 1 governance is state-conditioned (traffic-light triggers backup switch). Level 2 governance is absent. The tripartite classification conditions supervisory behaviour but not AI advisory scope. |

- **Governance type:** **Binary AI governance with tripartite supervisory governance.** The AI itself has two modes: on (Levels 1-2) or off (Level 3). The supervisory component has three modes of response intensity (routine, thorough, switch-and-investigate). This confirms the literature-wide pattern: even when three-level classification exists, it governs human behaviour, not AI scope.
- **Supports or contradicts two-level governance pair:** **Strongly supports the need** — the paper demonstrates that tripartite classification is natural and useful for safety-critical systems, but leaves the Level 2 governance gap open. My research fills this by making the intermediate level (CAUTION) govern the AI's recommendation scope, not just the supervisory response.

---

## 8. Human Role in Decision-Making

- **Human involvement:** The human operator is the supervisor of the safety-related system. They evaluate monitoring output (via traffic-light index), decide on switching to backup, trigger re-training, and determine the updating strategy.
- **Decision support vs. automation:** Explicitly positioned as decision support: "We want to develop an AI assistant that collaborates with the human operator to enhance the safety of the system and augment the operator's capabilities." And: "The AI acts rather as an assistant than an autonomous tool."
- **Human-AI interaction:** The traffic-light index is the primary interface — it communicates AI degradation severity and provides actionable recommendations. The authors state this "aims to assist the human operator in managing the system and making informed decisions."
- **Override / escalation:** Yes — the adjusted simplex architecture enables the operator to "seamlessly switch to the backup safety system, ensuring continuous oversight and intervention in case of an AI misbehavior or degradation." The operator can also "transition back to the AI control" when performance is restored.

---

## 9. System Constraints and Environment

- **Real-world constraints:** The paper discusses operational challenges: concept drift in non-stationary environments, label scarcity, computational expense of monitoring high-dimensional data streams, latency in measuring performance degradation.
- **Deployment context:** Targets industrial safety-critical E/E/PE systems (electrical, electronic, programmable electronic). No real-world deployment reported — framework is conceptual.
- **Resource-aware design:** The paper notes re-training with small batches to save memory, and dynamic evaluation to select adequate re-training datasets without storing all historical data. These are relevant to resource-aware design but not in the low-connectivity/low-compute sense of my research.

---

## 10. Hybrid AI Taxonomy

- **Type:** **Supervisory control with deterministic backup** — AI component performs the safety function, monitored by non-AI supervisory component, with non-AI backup safety system as fallback. The limiting logic constrains AI outputs. This maps to my "supervisory control" category.
- **Safety enforcement location:** Alongside (monitoring evaluates AI in real-time) and after (limiting logic constrains outputs). The backup system provides post-failure fallback.
- **Two-level governance support:** Supports Level 1 (traffic-light triggers AI on/off via backup switch). Does not implement Level 2 (AI scope unchanged across levels).
- **Comparison to my architecture:** The structural parallel is strong: both architectures have a deterministic safety layer constraining a probabilistic AI, with human oversight and deterministic fallback. The key difference is that my architecture varies the AI's recommendation scope by safety state (Level 2 governance), while theirs keeps AI scope constant and varies only the supervisory response.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparison:** None — conceptual framework paper.
- **Evaluation:** None empirical. The paper proposes the framework and indexing system as "initial frameworks to open up further discussions."
- **CAUTION zone testing:** The Level 2 (orange) behaviour is described verbally but not tested.
- **Future work includes:** Deploying AI alongside the quality assurance process in a safety-related system, evaluating the framework, and integrating the degradation index.

---

## 12. Key Concepts and Definitions

| Concept | Definition / Description | Relevance |
|---|---|---|
| **Traffic-light degradation index** | Three-level (green/orange/red) classification of AI degradation severity with actionable recommendations per level | **Closest structural precedent to my tripartite safety state model** — but governs supervisory behaviour, not AI scope |
| **Concept drift** | Unpredictable change in data distribution during operation; virtual (input drift, no effect on decision boundary), actual (affects decision boundary), or mixed | Relevant operational challenge for my architecture's deployment |
| **Temporal degradation of AI** | Performance degradation that cannot be fully explained by concept drift in data, but within the models themselves | Background on AI reliability in operation |
| **Limiting logic** | Component that enforces restrictions on AI outputs to prevent unsafe behaviour | Parallel to my architecture's gate function constraining AI outputs |
| **Adjusted simplex architecture** | Enables seamless switching between AI and backup safety system | Relevant fallback mechanism design |
| **Catastrophic forgetting** | Model "forgets" previously learned tasks when learning new ones, leading to poor generalisation | Background on AI updating challenges |
| **ISO/IEC TR 5469** | Technical report on AI and functional safety — classifies AI usage into levels (A-D) and classes (I-III) based on safety function role and standards compliance | Standards reference for positioning my architecture |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Framework is a first draft requiring further investigation and refinement
  - Traffic-light index not yet empirically validated
  - Limited to quality assurance during operation — excludes data acquisition, training, and system integration
  - Label scarcity in real-world deployment remains a fundamental challenge
  - Monitoring methods may produce high false positive/negative rates

- **Alignment with my research gaps:**
  - The paper implements a **three-level classification** but uses the intermediate level (orange) to govern **supervisory behaviour only**, not **AI recommendation scope** — confirming the CAUTION mode gap
  - The paper's architecture has all the components for two-level governance (AI component, monitoring, supervisory component, limiting logic, backup) but does not formally connect the traffic-light state to AI scope restriction
  - No formal model — the traffic-light index is described verbally with weighted scoring but not mathematically specified

---

## 14. Methodology Notes

- **Research method:** Literature review (Web of Science, Google Scholar) + conceptual framework development extending ISO/IEC TR 5469.
- **Alignment with DSR:** Partially — proposes a design artefact (extended framework + indexing) but does not formally evaluate it. Future work plans deployment and evaluation.
- **Methodological insights:** The traffic-light design principle could inform the interface design for communicating SAFE/CAUTION/UNSAFE states to fishers in my system.

---

## 15. Quotable / Citable Points

1. **AI as assistant, not autonomous:** "We want to develop an AI assistant that collaborates with the human operator to enhance the safety of the system and augment the operator's capabilities" (Introduction). — *Directly supports my decision-support positioning*

2. **Traffic-light novelty claim:** "To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner" (Discussion). — *Establishes the novelty of tripartite classification in this space; my architecture extends this by connecting the tripartite state to AI scope restriction*

3. **Non-AI monitoring principle:** "The goal of the implemented framework is to leave out AI technologies and fully rely on non-AI technologies to monitor the AI component" (Section III-B). — *Supports my deterministic (non-AI) safety state classification function S = f(E)*

4. **Backup as deterministic fallback:** The backup safety system uses "deterministic logic or human task, focus on transition to a safe (degraded) state only" (Figure 1). — *Parallels my UNSAFE state where G(S) = 0 and the system reverts to deterministic warnings*

---

## 16. Relation to My Research and Positioning

- **Governance levels implemented:** Full Level 1 (traffic-light Level 3 blocks AI, switches to backup). No Level 2 (AI scope unchanged across levels).
- **State-conditioned governance:** Partial — the tripartite classification conditions supervisory behaviour and AI participation (on/off), but not AI recommendation scope.
- **Proximity to (G(S), A_AI(S)):** Structurally close but functionally incomplete. The traffic-light index is the closest structural precedent to my safety state S ∈ {SAFE, CAUTION, UNSAFE}. The architecture has all the components needed for two-level governance. But the intermediate level (orange) does not restrict AI scope — it only triggers supervisory investigation.
- **Safety Dominance Property:** Not formally defined.
- **Gap my research fills:** This paper demonstrates that three-level safety classification is natural and useful for safety-critical AI systems, and that the intermediate level is operationally meaningful. But it uses the intermediate level to govern *human supervisory behaviour* only, not *AI recommendation scope*. My architecture extends this by making the intermediate CAUTION state govern both: the human is alerted (as in Flehmig et al.) AND the AI's admissible recommendation space is restricted (A_AI(CAUTION) ⊂ A_AI(SAFE)).

**Positioning paragraph:** Flehmig et al. (2024) provides the **closest structural precedent to my tripartite safety state model** and serves as a key **gap-evidence paper** for the CAUTION mode contribution. Their traffic-light degradation index (green/orange/red) classifies AI operational status into three levels with distinct recommended actions — a structure that directly parallels my S ∈ {SAFE, CAUTION, UNSAFE} classification. Their extended framework architecture (AI component + non-AI monitoring + non-AI supervisory component + deterministic backup + limiting logic) closely mirrors my hybrid deterministic-gate + probabilistic-AI architecture. However, their three-level classification governs only the **supervisory response intensity** (routine checks → thorough investigation → switch to backup), not the **AI's recommendation scope**. At both Level 1 (green) and Level 2 (orange), the AI operates with identical, unrestricted scope — the intermediate level changes what the *human supervisor does*, not what the *AI may recommend*. This is precisely the gap my CAUTION mode addresses: in my architecture, the intermediate safety state restricts the AI's admissible recommendation space (A_AI(CAUTION) ⊂ A_AI(SAFE)), providing computational governance at Level 2 that complements the supervisory governance Flehmig et al. implement. The paper can be cited as evidence that (a) tripartite safety classification is independently motivated in the safety-critical AI literature, and (b) even when tripartite classification is implemented, the intermediate level's governance potential for AI scope restriction remains unrealised.

---

## 17. Overall Relevance Score

### ⭐⭐⭐⭐ High

**Justification:** The paper is directly relevant to four core themes (hybrid AI, safety-critical AI, AI governance, human role) and partially to one more (decision architecture). Its traffic-light degradation index is the closest structural precedent to my tripartite safety state model in the entire review, making it a critical gap-evidence paper for the CAUTION mode contribution. The extended framework architecture closely parallels my hybrid approach. The paper does not reach ⭐⭐⭐⭐⭐ because it lacks mathematical formalisation, does not implement Level 2 governance (AI scope restriction), and does not address the fisheries/maritime domain or low-resource environments. But it is a strong gap-evidence and structural-precedent paper that independently validates the tripartite safety classification while demonstrating that the intermediate level's AI governance potential remains untapped.
