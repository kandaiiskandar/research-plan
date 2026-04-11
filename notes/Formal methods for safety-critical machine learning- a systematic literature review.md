## Literature Review Extraction: Newcomb & Ochoa (2026)

---

### 1. Paper Identity

- **Title:** Formal methods for safety-critical machine learning: a systematic literature review
- **Authors:** Alexandra Newcomb, Omar Ochoa
- **Year:** 2026 (published 18 February 2026)
- **Venue:** *Frontiers in Artificial Intelligence*, Vol. 9, 1749956
- **DOI:** 10.3389/frai.2026.1749956
- **Type:** Systematic Literature Review (SLR) — 46 peer-reviewed studies from 2020 to mid-2025

---

### 2. Core Contribution

- **Problem addressed:** Traditional testing-based verification is insufficient for providing comprehensive safety guarantees for ML systems deployed in safety-critical domains, due to their non-deterministic, data-driven, black-box nature. The field of formal methods applied to ML safety is fragmented and underexplored.
- **Proposed solution:** A comprehensive SLR synthesising 46 studies into eight categories of formal methods for ML safety: (1) Reachability & Over-Approximation, (2) SMT-based Verification & Abstraction/Refinement, (3) MILP/ILP, (4) Model Checking, (5) Runtime Verification, (6) Shielding Techniques, (7) Control Barrier Function Methods, (8) Risk Verification Methods.
- **Main contributions:**
  - Taxonomy of eight formal method categories applied to ML safety
  - Bibliometric analysis (geographic distribution, publication venues, citation trends)
  - Identification of application domains (NN/DNN controllers, RL policies, perception NNs being the top three)
  - Synthesis of persistent gaps: scalability to large models, limited real-world validation, nearly all approaches applied post-training rather than integrated into training loops
  - Future research roadmap including integrated training-verification loops, hybrid formal methods, and techniques for emerging paradigms (LLMs)
- **Novelty:** First SLR on this topic covering literature produced after 2022; prior reviews are dated (most recent covered up to 2022) and were mostly unsystematic surveys on tangential topics.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **Partial** | Shielding techniques and runtime verification architectures combine formal/rule-based safety enforcement with ML-based agents — structurally hybrid |
| Safety-critical AI decision-making | **Yes** | Core focus: formal methods to guarantee ML safety in safety-critical domains (transportation, healthcare, industrial automation, avionics) |
| AI governance / control mechanisms | **Yes** | Shielding, runtime monitors, CBFs, and limiting logic all implement forms of AI governance — constraining what AI may do at runtime |
| Low-resource environments | **No** | Not addressed; focus is on computational/formal verification challenges, not deployment resource constraints |
| Decision architecture formalisation | **Yes** | Central concern: formal specification of safety properties, mathematical guarantees of system correctness, and verified bounds on ML outputs |
| Human role in decision-making | **No** | Human role is not discussed; the focus is on automated formal verification, not human-AI interaction |
| Socio-technical evaluation | **No** | Not addressed |
| Coastal fisheries / maritime domain | **No** | Not addressed; domains are avionics, autonomous vehicles, robotics, healthcare, 6G networks |

**Mid-Extraction Relevance Gate:** 3 Yes + 1 Partial → **FULL EXTRACTION**.

---

### 4. Decision Architecture Analysis

- **Architecture structure:** The SLR does not propose a single architecture but surveys architectures across 46 studies. The most architecturally relevant patterns are:
  - **Shielding (Section 4.6):** A reactive system alongside the ML agent that intercepts unsafe actions and replaces them with safe alternatives. The shield checks each proposed action against formal safety specifications and corrects if unsafe. This is structurally a Level 1 governance mechanism — binary permit/block per action.
  - **Runtime verification (Section 4.5):** Monitors operating alongside or after ML systems that check property adherence against system traces. Safety properties specified in formal languages (e.g., STL, LTL), monitors generated from specifications, instrumented to extract information from the system.
  - **Control Barrier Functions (Section 4.7):** Assign a scalar safety score to each state; the safe set is the super-level set above a threshold. Controllers use CBF conditions as safety filters to keep trajectories inside the safe set.
  - **Runtime assurance with backup (S8, S10, S16):** Architectures where runtime monitors evaluate ML outputs and can switch to safe backup controllers — structurally analogous to Flehmig et al.'s framework.

- **Rule-based constraints before/alongside AI:** Shields operate *alongside* ML agents, intercepting unsafe actions before execution. Runtime monitors operate *after* ML produces output. CBFs operate as *filters* on proposed actions. Nearly all formal safety enforcement is reactive (post-output or per-action), not proactive (pre-engagement based on environmental state).

- **Failure modes and fallback:** Several architectures include backup controllers (S8 — safe backup flight planner; S10 — shadow versions with active version replacement; S16 — VSRL replacing unsafe actions with uniformly sampled safe ones).

---

### 5. Formal Model and Mathematical Representation

- **Formal models surveyed:** The SLR covers extensive formal machinery — SMT constraints, temporal logic specifications (LTL, STL), reachability sets, barrier certificates, MDP abstractions, hybrid programs in differential dynamic logic (dL), MILP encodings, star-set propagation. These are among the most rigorous formal frameworks available for ML safety.

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):**
  - The formal methods surveyed operate at a *different level of abstraction*. They verify properties of individual ML models (robustness, correctness, safety adherence) rather than governing the architectural interaction between environmental state classification, AI participation, and AI advisory scope.
  - **Shielding** is the closest structural analogue to G(S): a binary gate that permits or blocks individual actions. But shields operate per-action, not per-environmental-state.
  - **No surveyed paper** implements state-dependent recommendation restriction where the admissible action space changes across classified safety states (A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅).
  - **CBFs** define a binary safe/unsafe boundary — states above threshold are safe, below are unsafe. No intermediate "caution" region with restricted but non-empty action space.

- **Safety properties comparable to Safety Dominance Property:**
  - Shielding guarantees that executed actions satisfy safety specifications — structurally similar to AI(E) ⊆ A_AI(S), but A_AI is not state-conditioned across graduated levels.
  - CBFs guarantee trajectories remain in the safe set — a binary containment property, not graduated.
  - Reachability analysis proves that all possible NN outputs fall within specified bounds — the strongest formal analogue to the Safety Dominance Property, but applied to NN verification, not to architectural governance.
  - **No surveyed paper** defines a Safety Dominance Property for graduated (non-binary) governance.

- **Formalisation purpose:** Predominantly for *proof and verification* — providing mathematical guarantees of safety property adherence. This is more rigorous than my descriptive formalisation but operates at a different architectural level.

---

### 6. Safety State Classification

- **Classification schemes:** The surveyed formal methods predominantly operate with **binary safety boundaries** — safe/unsafe, within-bounds/out-of-bounds, property-satisfied/property-violated.
  - Shielding: safe action / unsafe action (binary per action)
  - CBFs: safe set / unsafe set (binary, threshold-based)
  - Reachability: output within bounds / output outside bounds (binary)
  - Runtime verification: property satisfied / property violated (binary per trace)

- **Tripartite classification:** Not present in any surveyed study. No paper classifies states into three levels with differentiated AI behaviour across levels.

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** The formal methods literature universally operates with binary safety classification. This is strong evidence for the binary governance gap claim: even the most formally rigorous approaches to ML safety use binary (safe/unsafe) boundaries, not graduated classifications with intermediate restricted modes.

---

### 7. Governance Level Analysis

| Level | Question | Implemented across surveyed studies? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | **Yes** | Shielding blocks individual unsafe actions; runtime assurance switches to backup controllers; CBFs filter unsafe actions. All implement binary per-action participation control. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | No surveyed paper restricts the *type* or *scope* of AI outputs based on classified environmental state. Governance is per-action (permit/block), not per-output-type (restrict scope). |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Not implemented in any surveyed study. |

- **Binary or graduated?** Universally **binary** across all 46 surveyed studies. Every formal method for ML safety in the literature operates at a single governance level: permit/block individual actions or verify/violate individual properties. No graduated governance with intermediate restricted modes.

- **Support for two-level governance pair?** The SLR strongly **supports the gap claim**: across 46 studies spanning five years of formal methods research for safety-critical ML, no paper implements state-conditioned advisory scope restriction. The entire formal safety verification literature operates with binary safety boundaries.

---

### 8. Human Role in Decision-Making

- **Not addressed.** The SLR focuses entirely on automated formal verification. Human oversight, decision support, and human-AI interaction are not discussed. The reviewed studies verify ML systems as autonomous components, not as decision support tools for human operators.

---

### 9. System Constraints and Environment

- **Scalability is the primary concern.** The SLR identifies scalability as the most persistent challenge: formal methods struggle with large, complex models. Most studies evaluate on small/medium networks and domain-specific benchmarks.
- **Real-world validation gap:** Many evaluations are confined to simulation; limited real-world deployment.
- **Resource-constrained deployment:** One study (S41) specifically addresses quantized DNNs for resource-constrained devices — safety assurance when deploying compressed models.
- **No low-resource environment focus** in the deployment sense (limited connectivity, limited data, low-literacy users).

---

### 10. Hybrid AI Taxonomy

- **Shielding:** Supervisory control — rule-based shield monitors and corrects ML agent's proposed actions. Safety enforcement sits *alongside* AI reasoning (concurrent filtering).
- **Runtime verification:** Post-hoc monitoring — monitors check ML outputs after generation. Safety enforcement sits *after* AI reasoning.
- **CBFs:** Safety filter — scalar safety score constrains action selection. Safety enforcement sits *before action execution* but *after action proposal*.
- **None of these** support two-level governance where both AI participation and advisory scope are governed by environmental state. All are single-level binary control mechanisms applied per-action or per-output.

---

### 11. Baseline Comparison and Evaluation

- **Formal methods vs. traditional testing:** The SLR extensively documents why testing is insufficient (Section 4.9): testing cannot prove absence of violations, cannot exhaustively cover infinite input spaces, and provides only statistical guarantees.
- **No comparison of graduated vs. binary governance.** No surveyed study compares restricted intermediate modes against binary on/off governance.
- **Evaluation gaps:** Limited real-world validation, scalability to production-size models, nearly all verification applied post-training (not integrated into training loops), and limited work on emerging paradigms (LLMs).

---

### 12. Key Concepts and Definitions

- **Shielding:** A reactive system alongside an ML agent that enforces safety properties by intercepting and correcting unsafe actions before execution.
- **Control Barrier Function (CBF):** A scalar function assigning safety scores to states; the safe set is the super-level set above a threshold. Used as a safety filter for action selection.
- **Runtime Verification:** Lightweight formal method applied at runtime; monitors generated from formal specifications check property adherence against system traces.
- **Reachability Analysis:** Computes the set of all possible outputs an NN can produce within specified input bounds; provides mathematical proof that outputs remain within safe bounds.
- **Safety Property:** A formal specification (in temporal logic, constraints, or similar formalism) that a system must satisfy to be considered safe.
- **Sound over-approximation:** A computed set that provably contains every true output of the NN — a conservative guarantee that no safe output is excluded.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations of the SLR:** Limited to four digital library sources; excludes non-peer-reviewed work (ArXiv, ResearchGate); inclusion of "testing" and "traditional verification" in search terms may have excluded relevant articles.

- **Gaps across the surveyed literature:**
  - Scalability to large and complex models remains the dominant challenge
  - Nearly all formal methods applied post-training, with minimal integration into training loops
  - Limited real-world validation beyond simulation benchmarks
  - Steep technical expertise required, hindering practitioner adoption
  - Little integration with mainstream ML frameworks (TensorFlow, PyTorch)
  - No formal verification techniques for LLMs or emerging ML paradigms

- **Gaps aligned with my research:**
  - **Binary safety boundaries universal:** Every formal method surveyed operates with binary (safe/unsafe) classification. No graduated safety state classification with differentiated AI behaviour across levels. This is the strongest evidence from the formal methods literature for the binary governance gap.
  - **No state-conditioned advisory scope restriction:** Shields, CBFs, and runtime monitors all implement per-action binary governance. No mechanism restricts the *type* of output AI may generate based on classified environmental state.
  - **No Safety Dominance Property for graduated governance:** Reachability analysis and CBFs provide formal containment guarantees, but only for binary safe sets — not for graduated admissible action spaces.
  - **Verification as post-hoc, not proactive:** The surveyed methods verify ML models or filter individual outputs — they do not proactively restrict AI engagement scope based on environmental state classification.

---

### 14. Methodology Notes

- **Method:** Systematic Literature Review following Carrera-Rivera et al. (2022), Zhou et al. (2015), and Kitchenham & Charters (2007). PICOC framework for search string design; inclusion/exclusion criteria; quality assessment checklist.
- **DSR alignment:** Minimal. This is a synthesis/survey paper, not a design-build-evaluate paper.
- **Methodological value:** The SLR's taxonomy of eight formal method categories provides a structured way to position my deterministic safety classification within the broader formal methods landscape. The finding that all surveyed methods use binary safety boundaries is directly citable as gap evidence.

---

### 15. Quotable / Citable Points

1. **Binary safety universality:** The entire SLR surveys 46 studies across eight formal method categories, and every method operates with binary safety boundaries (safe/unsafe, property-satisfied/violated). No study implements graduated safety states — strong gap evidence. (Sections 4.1–4.8, synthesised across all categories)

2. **Shielding as per-action binary control:** "A shield is a reactive system implemented alongside the learning agent that enforces safety properties specified in a formal language. The learning agent observes the environment and selects an appropriate action, which is then checked by the shield and corrected if the chosen action is deemed unsafe." (Section 4.6) — Confirms shielding operates at Level 1 only, per-action.

3. **Testing insufficiency for safety-critical ML:** Multiple studies confirm that testing-based verification cannot prove absence of violations and provides only statistical guarantees, insufficient for safety-critical deployment. (Section 4.9) — Supports the need for deterministic safety constraints in safety-critical architectures.

4. **Post-training verification gap:** "Nearly all approaches apply formal methods after model training...with little integration back into the training loop." (Section 5.2.1) — Supports the case for proactive, design-time safety governance rather than post-hoc verification alone.

5. **Limited real-world validation:** "Many evaluations are confined to small, domain-specific benchmarks and have not been validated in real-world scenarios." (Section 5.2.1) — Supports the need for real-world evaluation in safety-critical contexts.

---

### 16. Relation to My Research and Positioning

- **Governance levels:** The surveyed formal methods implement **Level 1 governance only** — binary per-action permit/block via shielding, CBFs, runtime monitors, and reachability verification. **Level 2 governance** (state-conditioned advisory scope restriction) is absent from the entire formal methods literature surveyed.
- **Proximity to (G(S), A_AI(S)):** Shielding implements the closest analogue to G(S) — a binary gate checking each proposed action. But it operates per-action, not per-environmental-state, and does not implement A_AI(S). No surveyed paper combines both levels in a unified governance pair.
- **Formal safety property:** Reachability analysis and CBFs provide formal containment guarantees (outputs within bounds, trajectories within safe sets) that are structurally analogous to the Safety Dominance Property. However, these are binary (single safe set), not graduated (nested containment across safety states).
- **Gap my research addresses:** This SLR demonstrates that the entire formal methods community for safety-critical ML operates with binary safety paradigms. My two-level governance pair with graduated safety states and the Safety Dominance Property for non-binary governance fills a gap that exists not only in the applied AI governance literature but also in the formal verification literature.

**Positioning paragraph:** Newcomb & Ochoa (2026) serves as **authoritative evidence for the binary governance gap** from the formal methods perspective. This comprehensive SLR of 46 studies across five years demonstrates that every formal method for safety-critical ML — shielding, runtime verification, CBFs, reachability analysis, model checking, SMT-based verification — operates with binary safety boundaries (safe/unsafe, permit/block). No surveyed paper implements graduated safety states with differentiated AI behaviour, no paper restricts AI advisory scope based on classified environmental state, and no paper defines a Safety Dominance Property for non-binary governance. This positions the binary governance paradigm not merely as a design convention in applied AI systems (as documented by Perez-Cerrolaza et al., 2024) but as a universal pattern across the most formally rigorous approaches to ML safety. The paper belongs in the **formal methods / formalisation background** section of the literature review, cited to extend the binary governance gap claim from applied architecture (Perez-Cerrolaza; Chen; Flehmig) into formal verification territory.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium — provides useful background and strengthens gap claim from the formal methods perspective**

**Justification:** The paper addresses three core themes (safety-critical AI, AI governance, decision architecture formalisation) and provides the most comprehensive survey of formal methods for ML safety currently available. Its primary citation value is strategic rather than architectural: it demonstrates that the binary governance paradigm is universal even in the most formally rigorous corner of ML safety research. No surveyed paper implements graduated governance, state-conditioned advisory scope, or non-binary Safety Dominance Properties. This strengthens the gap claim from a different angle than the applied architecture papers (Perez-Cerrolaza, Flehmig). However, the paper does not itself propose an architecture, does not address environmental state classification, does not discuss human-AI decision support, and does not engage with low-resource or maritime contexts. It is background/gap evidence, not a direct comparator or baseline.

---

### Recommended Citation Uses

| Use | Section | Specific claim |
|---|---|---|
| Binary governance gap (formal methods) | Research gap | All 46 surveyed formal methods for ML safety operate with binary safety boundaries; no graduated governance exists in the formal verification literature |
| Shielding as Level 1 baseline | Governance gap / architecture comparison | Shielding implements per-action binary permit/block — the formal methods equivalent of Level 1 governance, with no Level 2 |
| Formal safety property landscape | Formalisation background | Reachability analysis and CBFs provide containment guarantees analogous to Safety Dominance Property, but only for binary safe sets |
| Post-hoc vs. proactive governance | Design rationale | Nearly all formal methods are applied post-training; supports case for proactive, design-time environmental state classification |
| Testing insufficiency | Motivation | Multiple studies confirm testing cannot prove absence of violations — supports deterministic safety constraints in safety-critical systems |
