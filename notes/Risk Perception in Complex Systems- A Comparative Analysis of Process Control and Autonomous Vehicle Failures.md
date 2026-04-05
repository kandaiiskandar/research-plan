## Literature Review Extraction

---

### 1. Paper Identity

- **Title:** Risk Perception in Complex Systems: A Comparative Analysis of Process Control and Autonomous Vehicle Failures
- **Authors:** He Wen, Zaman Sajid, Rajeevan Arunthavanathan
- **Year:** 2025
- **Venue:** *AI*, 6(8), 164 (MDPI open access journal)
- **DOI:** 10.3390/ai6080164
- **Type:** Empirical comparative study (cross-domain analysis of 60 real-world accident reports)

---

### 2. Core Contribution

- **Problem:** As intelligent systems increasingly operate in high-risk environments, understanding how they perceive and respond to hazards is critical — but no systematic study has compared risk perception and human–AI interaction failures across process control systems (PCSs) and autonomous vehicles (AVs).
- **Solution/Finding:** Comparative analysis of 60 real-world accident reports (30 PCS from CSB, 30 AV from NTSB) using a GPT-assisted structured extraction template. Key findings: PCS risks are predominantly internal and managed via deterministic rule-based mechanisms; AV risks are externally driven and managed via probabilistic multi-modal sensor fusion. Despite these architectural differences, both domains exhibit recurring human–AI/automation interaction failures: over-reliance on automation, mode confusion, passive monitoring, and delayed intervention. Human intervention was ineffective in 83.3% of PCS cases and 66.7% of AV cases.
- **Main contributions:**
  1. First systematic cross-domain comparison of risk perception paradigms between PCS and AV domains
  2. Empirical characterisation of human–automation/AI interaction failure patterns across both domains
  3. Evidence that failures stem not from purely technical faults but from complex human–automation interaction breakdowns
  4. Recommendation for hybrid risk perception frameworks integrating deterministic safety logic with adaptive AI intelligence
- **Novelty:** Cross-domain comparative methodology using GPT-assisted structured extraction; bridging PCS (traditional automation) and AV (AI-enabled) domains to project future human–AI interaction challenges in industrial systems.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Contrasts deterministic/rule-based PCS paradigm with probabilistic/ML-based AV paradigm; recommends hybrid frameworks combining both — but does not design or formalise such an architecture |
| Safety-critical AI decision-making | Yes | Core focus: analyses real-world failures in safety-critical process control and autonomous vehicle systems; examines how risk is perceived, interpreted, and acted upon under hazardous conditions |
| AI governance / control mechanisms | Partial | Discusses alarm systems, safety interlocks, emergency shutdowns (PCS) and sensor fusion/automated braking (AV) as control mechanisms — but does not formalise governance structures or gate functions |
| Low-resource environments | No | Not addressed; both PCS and AV domains are well-instrumented, high-resource contexts |
| Decision architecture formalisation | No | No formal model of decision architecture; analysis is empirical/comparative, not mathematical |
| Human role in decision-making | Yes | Core theme: detailed empirical analysis of human roles (operational, supervisory, maintenance, emergency override), intervention effectiveness, and human–automation interaction failure types across both domains |
| Socio-technical evaluation | Partial | Empirical analysis of how human–system interaction contributes to failures; identifies socio-technical failure modes (mode confusion, over-reliance, passive monitoring) — but not framed as socio-technical evaluation methodology |
| Coastal fisheries / maritime domain | No | Not addressed |

**Mid-Extraction Relevance Gate:** 2 Yes + 3 Partial = **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only)

---

### 4. Decision Architecture Analysis

- **PCS architecture:** Structured, deterministic decision-making. Rule-based detection using fixed thresholds and hardwired safety interlocks. Detection → alarm → human interpretation → manual/automated response (e.g., emergency shutdown). Decision logic is transparent and explainable. 100% of PCS cases used rule-based detection methods.
- **AV architecture:** Probabilistic, ML-based decision-making. Multi-modal sensor fusion (LiDAR, radar, camera) → real-time environmental modelling → behaviour prediction → automated response (e.g., emergency braking). Decision logic is often opaque ("black-box"). All AV cases referenced AI-based or probabilistic detection methods.
- **Layered architecture:** Neither domain is described as having a formally layered governance architecture. PCS has sequential alarm hierarchies and safety interlocks as pre-conditions for operation. AV has sensor fusion pipelines feeding into decision modules. Neither implements a state-conditioned governance pair.
- **Failure modes and fallback:** Both domains exhibit failure modes in the human–system interaction boundary. PCS: alarm flooding, misinterpretation, delayed response. AV: sensor misperception, mode confusion, disengaged supervision. The paper identifies that PCS has clearer fallback (structured emergency shutdowns) while AV response is often "variable" and "ambiguous."
- **Boundary between deterministic control and AI reasoning:** The paper draws this boundary clearly at the domain level — PCS = deterministic, AV = probabilistic — but does not examine systems that integrate both paradigms within a single architecture. The recommendation for a "hybrid risk perception framework" combining deterministic and adaptive approaches is stated but not designed or formalised.

---

### 5. Formal Model and Mathematical Representation

- **No formal model is defined.** The paper is entirely empirical, using structured qualitative/quantitative comparison of accident report data.
- No state variables, safety functions, gate functions, or action spaces are formalised.
- **Comparison to DSR pipeline:** No analogue exists. The paper does not define E → S = f(E) → (G(S), A_AI(S)) → AI(E) or any equivalent pipeline.
- **No state-dependent recommendation restriction.** Neither PCS nor AV systems as described vary their output type based on classified safety state. PCS alarms trigger binary responses (shutdown or continue). AV systems apply probabilistic decision-making without state-conditioned restriction of output scope.
- **No Safety Dominance Property or equivalent.** The paper does not define formal safety properties guaranteeing that AI outputs fall within state-determined bounds.
- The comparison tables (Tables 2–7) provide structured qualitative comparison but no mathematical formalisation.

---

### 6. Safety State Classification

- **PCS:** Operates on binary threshold logic — normal operating parameters vs. alarm conditions. Safety interlocks activate at predefined thresholds. No intermediate "caution" mode is described; the paradigm is binary (normal/alarm) with alarm hierarchies for prioritisation.
- **AV:** Operates on probabilistic confidence scores from sensor fusion. Risk assessment is continuous rather than discretised into safety states. No formal classification into discrete safety levels is described.
- **No tripartite classification.** Neither domain implements a SAFE/CAUTION/UNSAFE classification scheme comparable to S = f(E) → {SAFE, CAUTION, UNSAFE}.
- **No differentiation of AI recommendation scope across safety levels.** PCS alarms trigger fixed responses (shutdown, vent, evacuate) regardless of graduated risk state. AV systems apply the same probabilistic decision pipeline regardless of classified risk level — the paper notes that AV "system prediction" was absent or undefined in most cases.
- **Key gap evidence:** The paper's finding that PCS uses binary threshold logic (rule-based, deterministic) while AV uses undifferentiated probabilistic reasoning (no state-conditioned output restriction) directly supports the claim that neither paradigm implements graduated governance with state-conditioned AI advisory scope restriction.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | Partial | PCS: safety interlocks can shut down operations (effectively G(S) = 0 under alarm). AV: no formal AI participation gate described — the AI perception/decision pipeline operates continuously. Neither implements a classified-state-conditioned participation gate. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | No | Neither domain restricts the *type* of AI/system output based on classified safety state. PCS alarms trigger fixed responses. AV systems do not vary their recommendation scope by risk level. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not implemented in either domain as described. |

- **Governance type:** PCS implements binary safety control (interlocks on/off = Level 1 only). AV implements no formal governance over AI participation or scope — the AI operates continuously with no state-conditioned restriction.
- **Binary vs. graduated:** Both domains operate with binary governance at best (PCS: normal/alarm; AV: no formal governance). Neither implements graduated governance where AI participation and advisory scope vary across multiple classified states.
- **Supports the gap claim:** The paper provides cross-domain empirical evidence that safety-critical systems in both process control and autonomous vehicle domains lack graduated, state-conditioned governance of AI behaviour — reinforcing the universality of the binary governance paradigm.

---

### 12. Key Concepts and Definitions

- **Risk perception (dual definition):** (1) Human risk perception — the cognitive process by which individuals recognise and assess potential hazards; (2) System-based risk perception — a system's ability to detect and respond to risks using sensor data and programmed or learned logic
- **Deterministic vs. probabilistic risk paradigms:** PCS = rule-based, threshold-driven, single-modal, transparent, low adaptability; AV = ML-based, multi-modal sensor fusion, adaptive, opaque ("black-box")
- **Human–AI/automation interaction failure types:** Over-reliance on automation (PCS 20%, AV 30%), passive monitoring (PCS 16.7%, AV 36.7%), mode confusion (PCS 13.3%, AV 10%), human error (PCS 26.7%, AV 20%), maintenance/inspection (PCS 23.3%, AV 3.3%)
- **Role-responsibility mismatch:** PCS operators have high authority but face information overload; AV users have low authority but are expected to react under uncertainty — a "structural paradox" increasing susceptibility to failure in both domains
- **Hybrid risk perception framework:** Recommended (but not designed or formalised) — integrating deterministic safety logic with adaptive AI intelligence to improve situational awareness and responsiveness

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  1. Modest sample size (30 cases per domain) — sufficient for structured comparison but not for statistical generalisation
  2. PCS cases do not involve deployed AI systems; human–automation interaction patterns are extrapolated as indicative of future human–AI interaction challenges
  3. GPT-assisted extraction is sensitive to narrative variability and may inconsistently interpret ambiguous descriptions
  4. Single primary coder for all extraction and preprocessing (mitigated by co-author verification)
  5. AV case availability constrained by limited public reporting and proprietary data

- **Unsolved problems / future work:**
  1. Developing standardised taxonomies of human–AI failure modes
  2. Designing interpretable models of machine risk perception
  3. Empirical studies on dynamic role allocation in human–AI teams
  4. Cross-domain simulation frameworks to evaluate hybrid risk perception during real-time operations
  5. Simulation-based validation, human-in-the-loop testing, and expert assessment to operationalise insights in high-risk environments

- **Alignment with DSR research gaps:**
  - The paper **recommends** a hybrid risk perception framework combining deterministic and adaptive approaches — but **does not design or formalise one**. This is precisely the gap the DSR architecture fills: a formalised hybrid architecture where deterministic safety governance (rule-based state classification and gating) controls when and how AI reasoning is permitted.
  - The finding that neither PCS nor AV implements state-conditioned governance of AI behaviour supports the claim that the two-level governance pair (G(S), A_AI(S)) is absent across safety-critical domains.
  - The paper's evidence on human intervention ineffectiveness (83.3% PCS, 66.7% AV) supports the motivation for architectures that do not rely solely on human override as a safety mechanism — the DSR architecture's deterministic gating provides safety enforcement independent of human intervention timing.
  - The absence of a CAUTION mode in either domain (PCS: binary alarm; AV: continuous probabilistic) directly supports the novelty claim for graduated governance with a restricted-but-non-empty AI advisory scope.

---

### 16. Relation to My Research and Positioning

- **Governance level:** PCS implements Level 1 governance (binary safety interlocks = participation control) at the operational level. AV implements neither Level 1 nor Level 2 governance formally — the AI perception/decision pipeline operates continuously without state-conditioned restriction. Neither domain implements Level 2 (advisory scope governance) or the unified governance pair.
- **No state-conditioned governance.** Neither PCS nor AV as described varies AI behaviour based on classified environmental safety state.
- **Gap relative to DSR:** The paper's core recommendation — a hybrid framework integrating deterministic and probabilistic risk perception — directly describes the architectural space the DSR research occupies. However, the paper only identifies the need without providing a solution. No formal model, no state classification, no gate function, no admissible action space, no Safety Dominance Property.
- **No Safety Dominance Property equivalent.**

- **Positioning paragraph:** This paper serves as **cross-domain gap evidence** for the DSR literature review. Its empirical comparison of process control (deterministic/rule-based) and autonomous vehicle (probabilistic/ML-based) risk perception paradigms demonstrates that both safety-critical domains operate with at most binary governance (PCS alarm interlocks) or no formal governance of AI behaviour (AV continuous operation). The paper's recommendation for a "hybrid risk perception framework" combining deterministic safety with adaptive intelligence articulates the need the DSR architecture addresses — but provides no architectural solution, no formalisation, and no state-conditioned governance mechanism. The finding that human intervention is ineffective in the majority of cases across both domains (83.3% PCS, 66.7% AV) further supports the motivation for architectures that enforce safety properties deterministically rather than relying on human override. This paper is best cited in the **research gap section** as cross-domain evidence that (1) safety-critical systems universally lack graduated, state-conditioned AI governance, (2) the hybrid architecture need is recognised but unfulfilled, and (3) human oversight alone is insufficient as a safety mechanism. It may also be cited in the **human role discussion** for its empirical data on human intervention effectiveness and failure typology.

---

### 17. Overall Relevance Score

**⭐⭐ Low**

**Justification:** The paper provides useful empirical evidence on risk perception and human–AI interaction failures across two safety-critical domains, supporting the gap claim that binary governance is universal and that hybrid frameworks are needed but absent. However, it does not address AI governance formalisation, decision architecture design, state classification, or any mechanism comparable to the two-level governance pair. It operates entirely at the empirical-comparative level without formal modelling. It does not address low-resource environments, fisheries/maritime domains, or decision architecture formalisation. Its contribution to the DSR literature review is limited to secondary gap evidence and human role background.

**Recommended citation uses:**
- Research gap section: cross-domain evidence that PCS (binary interlocks) and AV (continuous probabilistic) both lack graduated, state-conditioned governance of AI behaviour
- Human role discussion: empirical data on human intervention ineffectiveness (83.3% PCS, 66.7% AV) and failure typology (over-reliance, passive monitoring, mode confusion)
- Hybrid AI motivation: evidence that the need for hybrid deterministic + adaptive frameworks is recognised across domains but not yet formalised — the paper recommends it without providing a solution
- Background evidence that deterministic rule-based and probabilistic ML-based paradigms are treated as separate domain-level approaches rather than integrated within a single governance architecture
