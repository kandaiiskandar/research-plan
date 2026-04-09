# Literature Review Extraction: Bach et al. (2024)

## 1. Paper Identity

- **Title:** Unpacking Human-AI Interaction in Safety-Critical Industries: A Systematic Literature Review
- **Authors:** Tita A. Bach, Jenny K. Kristiansen, Aleksandar Babic, Alon Jacovi
- **Year:** 2024 (received May 2024, published August 2024)
- **Venue:** IEEE Access, Vol. 12, pp. 106385–106414
- **DOI:** 10.1109/ACCESS.2024.3437190
- **Type:** Systematic literature review (SLR)
- **Affiliation:** DNV Group Research and Development (Norway); Bar Ilan University (Israel)

---

## 2. Core Contribution

- **Problem addressed:** Human-AI interaction (HAII) in safety-critical industries is essential but poorly understood — the literature is limited, fragmented, and inconsistent. No prior review systematically examines what HAII is, what factors influence it, and how it is measured across safety-critical domains.
- **Proposed solution:** A systematic literature review of 24 empirical articles (from an initial 640) examining four research questions: (RQ1) terminology used for HAII, (RQ2) primary roles of AI-enabled systems, (RQ3) factors influencing HAII, and (RQ4) how HAII is measured.
- **Main contributions:**
  - Identification of seven factors influencing HAII: user characteristics, user perceptions and attitudes, user expectations and experience, AI interface and features, AI output, explainability and interpretability, and usage of AI
  - A taxonomy of four primary AI roles by decision-making authority: collaborative AI, AI-assisted decision-making, human-controlled AI, and emotional AI
  - Finding that AI-assisted decision-making is the dominant role (16/24 articles) and that healthcare dominates (70.83% of articles)
  - Evidence that HAII terminology is inconsistent — seven of 24 articles used no term at all to describe the interaction
  - A proposed sequential model (Figure 4) for addressing the seven influencing factors to optimise HAII quality
- **Novelty:** First SLR to simultaneously examine what HAII is, what influences it, and how it is measured, specifically motivated by safety-critical industry contexts. Uniquely applies Technology Readiness Level (TRL) assessment to characterise AI system maturity and its implications for HAII.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | The review does not examine hybrid AI architectures or the integration of deterministic rule-based and probabilistic reasoning. |
| Safety-critical AI decision-making | Yes | Central focus — all 24 included articles involve AI in safety-critical industries (healthcare, automotive, construction, space, nuclear energy). |
| AI governance / control mechanisms | Partial | Addresses decision-making authority (who decides) through the four-role taxonomy, and discusses human override and control authority transfer. However, does not address runtime state-conditioned governance of AI output scope. |
| Low-resource environments | No | Not examined. Most systems are healthcare prototypes in controlled settings; low-resource constraints are not considered. |
| Decision architecture formalisation | No | No formal models, state variables, or mathematical representations of decision architectures are presented. |
| Human role in decision-making | Yes | Core theme — the taxonomy explicitly positions human agency relative to AI agency on a spectrum, and multiple findings address trust, reliance, bias, and override. |
| Socio-technical evaluation | Yes | Extensively discusses user evaluation methods (subjective and objective), measurement tools, and the importance of involving target end-users throughout the AI lifecycle. |
| Coastal fisheries / maritime domain | No | Not addressed. The closest safety-critical domains are healthcare, automotive, and construction. |

**Mid-Extraction Relevance Gate:** 3 Yes → **FULL EXTRACTION**

---

## 4. Decision Architecture Analysis

- **Architecture structure:** The review does not analyse decision architectures of the surveyed systems in technical or structural terms. Instead, it classifies systems by their *primary role* (degree of decision-making authority), which implicitly describes a governance structure but at a conceptual rather than architectural level.
- **Layered architecture or governance structure:** The four-role taxonomy (collaborative AI, AI-assisted decision-making, human-controlled AI, emotional AI) describes a spectrum of decision authority allocation. Collaborative AI shares authority equally; AI-assisted decision-making retains human authority while AI influences; human-controlled AI treats AI as a tool; emotional AI responds to affect. This is a *conceptual* governance structure, not a formal architectural one.
- **Rule-based constraints or safety checks before AI:** Not examined at the architectural level. The review notes that users rely on AI more in low-risk than high-risk conditions (ref [97]), implying informal risk-awareness modulation, but no formal pre-AI safety gating mechanism is identified across the surveyed literature.
- **Boundary between deterministic control and AI reasoning:** Not defined. The review does not distinguish between deterministic and probabilistic components within the AI-enabled systems.
- **Failure modes, fallback, or override:** Discussed qualitatively. Human override is noted for collaborative AI (control authority transfer in robotics and driving, refs [89], [91]). The concept of "warranted trust" is raised to calibrate user reliance. However, no formal fallback architecture is described.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None. The review is entirely empirical and qualitative in its synthesis — no formal models, state variables, gate functions, or mathematical representations are presented.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** No comparable pipeline exists in this paper. The four-role taxonomy is purely descriptive and does not formalise the relationship between environmental state, safety classification, and AI behaviour.
- **State-dependent recommendation restriction:** Not modelled. While the review notes that users rely on AI differently across risk conditions, no system in the review formally restricts AI output scope based on classified safety state.
- **Safety Dominance Property:** Not defined or discussed.
- **Formalisation purpose:** N/A — no formalisation present.

---

## 6. Safety State Classification

- **Discrete safety/risk levels:** Not classified. The review does not examine how the surveyed systems classify operational conditions into safety states.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** No comparable classification. One finding notes that users relied on AI more during no-risk driving conditions than during high-risk and very-high-risk conditions (ref [97]), which implies informal risk differentiation but does not constitute a formal safety state classification.
- **Differentiation of AI recommendation scope across safety levels:** Not addressed. No system in the review restricts AI output types based on risk level. The gap between binary (AI on/off) and graduated scope restriction is not identified.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | The four-role taxonomy implicitly addresses whether AI participates (e.g., human-controlled AI has minimal AI agency), but no formal participation gate conditioned on environmental state is described. Control authority transfer in collaborative AI (refs [89], [91]) is the closest — determining *when* AI vs. human drives — but is negotiated, not state-classified. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | No system restricts the *types* of AI recommendations based on classified safety state. The review does not distinguish between governing AI participation and governing AI output scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not present in any surveyed system. |

- **Binary vs. graduated:** The taxonomy describes a spectrum of human-AI authority sharing, but this is a *design-time* role assignment, not a *runtime* state-conditioned governance mechanism. No graduated governance model comparable to the (G(S), A_AI(S)) pair is identified.
- **Support or contradiction:** The review *indirectly supports* the motivation for state-conditioned governance by showing that: (a) HAII quality varies by context and risk level; (b) users modulate reliance based on perceived risk; (c) one-size-fits-all AI roles are inadequate. However, it does not identify the architectural gap — i.e., that no system formally restricts AI advisory scope based on classified environmental state at runtime.

---

## 8. Human Role in Decision-Making

- **Human involvement:** Central finding. In 16/24 articles, the AI system's primary role was AI-assisted decision-making, where users hold final decision-making authority but AI influences the process.
- **Decision support vs. automation:** Overwhelmingly decision support. Only collaborative AI (4 articles) approaches shared/equal authority; no system is fully autonomous.
- **How the system interacts with users:** Through various modalities — visual displays, heat maps, text explanations, conversational interfaces, social robots. Users preferred simpler visualisations, progressive disclosure, and actionable recommendations with evidence.
- **Human override or escalation:** Discussed for collaborative AI (control authority transfer between AI and human in driving/robotics). For AI-assisted decision-making, override is implicit — the human can simply disregard AI output, though cognitive biases (automation bias, confirmation bias, over-reliance) make this difficult in practice.
- **Key insight for my research:** Even in AI-assisted decision-making (where the human formally decides), it is cognitively difficult to ignore AI output once exposed to it. This supports the design rationale for architecturally restricting what AI *may recommend* in elevated-risk conditions, rather than relying on users to self-regulate.

---

## 9. System Constraints and Environment

- **Real-world constraints:** Not systematically examined. The review notes the heterogeneity of environments (ref [93], [94]) and that AI effectiveness decreased in more complex scenarios (ref [84]).
- **Deployment vs. simulation:** Most systems are prototypes (TRL 3–4). Only 4/24 reached TRL 8 (commercial products). None reached TRL 9 (proven in operational environment).
- **Resource-aware design:** Not addressed. No discussion of limited data, connectivity, compute, or offline capability.
- **Low-resource relevance:** The review's finding that AI must be tailored to specific users and environments supports the argument that low-resource environments require architecturally distinct approaches, but this is not explicitly stated.

---

## 10. Hybrid AI Taxonomy

- **Hybrid approach:** Not examined. The review classifies AI capabilities (computer vision, NLP, forecasting, etc.) but does not analyse the hybrid integration of rule-based and probabilistic components.
- **Safety enforcement location:** Not discussed at the architectural level.
- **Two-level governance support:** Not addressed. The review does not distinguish between governance of AI participation and governance of AI output scope.
- **Comparison to my architecture:** The review operates at a different level of abstraction — it examines HAII factors and roles rather than internal AI architecture. It does not address the structural question of how deterministic safety constraints interact with probabilistic AI reasoning.

---

## 11. Baseline Comparison and Evaluation

- **Baseline comparison:** Individual included articles compare AI-assisted vs. unassisted performance (e.g., efficiency gains in ref [81], additional time in ref [79]), but the review itself does not compare systems with vs. without safety constraints or gating.
- **Metrics:** Predominantly subjective (user perceptions, trust, attitudes, workload). Objective metrics include task completion time, accuracy, efficiency, eye movement, and heart rate variability.
- **CAUTION zone testing:** Not applicable — no system implements a CAUTION mode with restricted AI scope.
- **Graduated vs. binary governance comparison:** Not evaluated. The review does not test whether restricting AI output scope at intermediate risk adds value beyond binary AI on/off.
- **Safety Dominance Property verification:** Not applicable.
- **Evaluation gaps identified:** The review identifies a research gap in direct and objective HAII measurements, the need for longitudinal studies of HAII, and the lack of cross-industry comparisons. These gaps are relevant to PS4 and PS5 evaluation design.

---

## 12. Key Concepts and Definitions

- **Human-AI Interaction (HAII):** "Any situation where a human is directly using, engaging, or interacting with AI to complete a task or achieve a goal."
- **AI-enabled system:** "Any system that contains or relies on one or more AI components" (from DNV-RP-0671).
- **Safety-critical industries:** "Industries in which safety is of paramount importance and where the consequences of failure or malfunction may be loss of life or serious injury, serious environmental damage, or harm to plant or property."
- **Four primary AI roles:** Collaborative AI (equal authority), AI-assisted decision-making (human decides, AI influences), human-controlled AI (AI as tool), emotional AI (responds to affect).
- **Seven HAII influencing factors:** User characteristics, user perceptions and attitudes, user expectations and experience, AI interface and features, AI output, explainability and interpretability, usage of AI.
- **Technology Readiness Level (TRL):** Applied (by the reviewers, not original authors) to assess AI system maturity on a 1–9 scale.
- **Warranted trust:** The appropriate level of trust calibrated to the actual capabilities and limitations of the AI system (ref [117]).
- **Automation bias:** Favouring recommendations from automated systems and ignoring those from non-automated systems.

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Only 24/640 articles (3.75%) met inclusion criteria — small sample, findings should be generalised with caution
  - Dominated by healthcare (70.83%) and USA/China (50%); findings may not generalise to other industries or cultures
  - No grey literature included
  - Does not explore unique properties of individual safety-critical industries
  - The seven HAII factors do not include interaction frequency or duration
- **Unsolved problems:**
  - HAII terminology is not codified — no agreed definitions across the field
  - No TRL 9 AI systems found — real-world operational deployment remains unproven
  - How to balance user trust calibration with the practical difficulty of ignoring AI output
  - Whether and how HAII can develop into longer-term human-AI relationships
  - How cultural aspects influence HAII in safety-critical settings
- **Gaps my architecture could address:**
  - The review does not identify the absence of *state-conditioned AI output scope restriction* — this is the precise gap my Level 2 governance fills
  - The review notes that users modulate reliance by perceived risk, but no system formalises this into architectural governance — my (G(S), A_AI(S)) pair addresses this
  - The review notes that one-size-fits-all AI is inadequate and that context/environment matter — my architecture operationalises this through the S = f(E) classification
  - The review does not examine how AI systems should behave at intermediate risk — the CAUTION mode is unaddressed

---

## 14. Methodology Notes

- **Method:** Systematic literature review (SLR) following PRISMA standards, registered in Open Science Framework (OSF).
- **Databases:** IEEE Xplorer, Scopus, ACM Digital Library, Web of Science (Semantic Scholar excluded due to overlap).
- **Search strategy:** Database search with structured keyword combinations across seven search string groups. No snowballing or hand searching.
- **Selection:** 640 initial → 619 after deduplication → 268 after title screening → 144 after abstract screening → 24 after full-text screening.
- **Analysis:** Independent content analysis by three reviewers; group consensus adjudicated by fourth author.
- **Inclusion criteria:** Published 2011–2023, English, peer-reviewed, empirical, focused on HAII, applied to safety-critical industry, involving target end-users.
- **DSR alignment:** Not a DSR study. However, the SLR methodology and PRISMA flow are relevant to my own search methodology documentation (highest priority outstanding item). The structured search string approach and multi-reviewer screening process offer a methodological reference point.
- **Informative for my research:** The seven-factor HAII framework is directly relevant to PS5 (socio-technical evaluation of the CAUTION mode). The finding that subjective and objective measures sometimes diverge supports using both in PS4/PS5.

---

## 15. Quotable / Citable Points

1. **On terminological fragmentation:** Seven of 24 articles do not use any term to describe the interaction between users and AI-enabled systems, highlighting the lack of consensus (Section VI-A, Table 5).

2. **On dominance of AI-assisted decision-making:** AI-assisted decision-making was the most dominant primary role (16/24 articles), where users hold final authority but AI influences the process (Section VI-B).

3. **On risk-modulated user reliance:** Users relied on AI-enabled systems significantly more during no-risk conditions than during very-high-risk and high-risk conditions (Section VI-C, ref [97]).

4. **On the difficulty of ignoring AI output:** "Even though the user has the freedom to ignore the AI's recommendations, it is very difficult to ignore the influence of AI output in clinical decision making once a user is exposed to the AI output" (Section VI-B, p. 106400).

5. **On the need for tailoring:** "One size does not fit all when it comes to ensuring quality HAII in safety-critical industries... developers still need to tailor their AI-enabled systems to their users" (Section VII, p. 106409).

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Neither Level 1 nor Level 2 governance is formally implemented or identified across the 24 surveyed systems. The four-role taxonomy describes *design-time* authority allocation, not *runtime* state-conditioned governance.
- **State-conditioned Level 2:** Not present. No system restricts AI output scope based on classified environmental state.
- **Proximity to (G(S), A_AI(S)):** Distant. The review operates at the socio-technical and human factors level, not the architectural governance level. It identifies that users informally modulate reliance by risk, but no formal mechanism is described.
- **Safety Dominance Property:** Not defined or comparable.
- **Gap my research addresses:** The review's key finding — that users modulate reliance based on perceived risk but no architectural mechanism supports this — is precisely the gap my Level 2 governance fills. My architecture operationalises the intuition that AI should behave differently at different risk levels into a formal, runtime, state-conditioned mechanism.
- **Positioning paragraph:** Bach et al. (2024) provides a comprehensive socio-technical foundation for understanding how humans interact with AI in safety-critical industries, identifying seven influencing factors and a four-role taxonomy of AI decision-making authority. The review strongly supports the *motivation* for my architecture: it demonstrates that HAII quality varies by context and risk, that users informally modulate reliance by perceived risk, and that one-size-fits-all AI is inadequate for safety-critical deployment. However, the review operates entirely at the human factors level and does not examine the *architectural* question of how AI systems should formally govern their own behaviour across risk states. No surveyed system implements state-conditioned restriction of AI output scope — the precise gap my Level 2 governance (A_AI(S)) addresses. The paper is best positioned as **background/motivation** in my literature review: it establishes the socio-technical case for why AI governance must be context-sensitive, while my architecture provides the formal mechanism to achieve this. The seven-factor HAII framework and measurement approaches are directly relevant to PS5 evaluation design, particularly the finding that subjective and objective measures sometimes diverge.

---

## 17. Overall Relevance Score

### ⭐⭐⭐ Medium

**Justification:** The paper provides strong socio-technical background for safety-critical AI deployment and directly supports the motivation for context-sensitive AI governance. It is relevant to Themes 2 (safety-critical AI), 6 (human role), and 7 (socio-technical evaluation). However, it does not address AI governance mechanisms at the architectural level, does not formalise any decision model, and does not identify the specific gap (absence of state-conditioned AI output scope restriction) that my architecture fills. Its primary value is as a motivational and evaluation-design reference rather than a core architectural or governance reference.

---

## Post-Extraction Commentary

### Strategic citation placement
- **Section 2.1 (background on AI in safety-critical industries):** Cite for the definition of safety-critical industries, the seven HAII influencing factors, and the finding that HAII research is fragmented and immature.
- **Section 2.5 or socio-technical evaluation chapter:** Cite for the measurement methodology discussion — particularly the finding that subjective and objective measures sometimes diverge (relevant to PS4/PS5 design decisions).
- **Architecture motivation chapter:** Cite the finding that users informally modulate reliance by risk level (ref [97] within this paper) as evidence that *architectural* risk-conditioned governance is needed to formalise what users already do informally.

### Inter-paper relationships
- Complements **Aquilino et al. (2025)** on cognitive trust for low-anthropomorphism decision support — Bach et al. provides the broader HAII factor framework within which trust sits.
- Complements **McGrath et al. (2025) S-TIAS** — the measurement methodology discussion supports the case for using validated trust instruments in PS4/PS5.
- Tangentially related to **Flehmig et al. (2024)** — both address graduated AI governance in safety-critical contexts, but Bach et al. from the human factors side and Flehmig from the supervisory intensity side.

### Tracker clustering suggestion
- Cluster: **Socio-technical evaluation & human factors** (alongside Aquilino et al., McGrath et al., Atf & Lewis)
- Secondary cluster: **Safety-critical AI background** (alongside Bloomfield & Rushby, International AI Safety Report)
