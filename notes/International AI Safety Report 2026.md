## Literature Review Extraction
### International AI Safety Report 2026

---

## Early Relevance Check: PASSED

1. Does this paper address at least one of the 8 core research themes? **Yes** — addresses safety-critical AI decision-making, AI governance/control mechanisms, hybrid AI concepts, and human role in decision-making extensively.
2. Does this paper contribute to safety-critical AI architecture, AI governance mechanisms, hybrid AI design, formal decision models, low-resource AI deployment, or fisheries/maritime AI? **Yes** — comprehensive treatment of AI governance mechanisms, safety-critical AI systems, risk management frameworks, and technical safeguards.
3. Could this paper plausibly be cited in a literature review about graduated AI governance for safety-critical decision support? **Yes** — directly relevant as a major institutional reference on AI safety governance paradigms, defence-in-depth, risk tiering, and the state of the art in AI control mechanisms.

**Proceed with full extraction.**

---

### 1. Paper Identity

- **Full title:** International AI Safety Report 2026
- **Authors:** Yoshua Bengio (Chair), Stephen Clare, Carina Prunkl (Lead Writers), Malcolm Murray, Maksym Andriushchenko, Ben Bucknall (Chapter Leads), + ~100 contributors from the Writing Group, Expert Advisory Panel (30+ countries), and Senior Advisers
- **Year:** February 2026
- **Publication venue:** Published by the UK Department for Science, Innovation and Technology (DSIT 2026/001), under Crown copyright. Presented at the India AI Impact Summit.
- **Type of paper:** International scientific assessment / policy-informing review. Synthesises existing research on general-purpose AI capabilities, risks, and risk management. Does not make specific policy recommendations.

---

### 2. Core Contribution

- **Main problem addressed:** The "evidence dilemma" facing policymakers — general-purpose AI capabilities are evolving rapidly, but evidence on risks is slow to emerge and difficult to assess. Acting too early risks ineffective interventions; waiting too long leaves society vulnerable.

- **Proposed solution / key finding:** Provides a structured, evidence-based assessment organised around three questions: (1) What can general-purpose AI do and how might capabilities change? (2) What emerging risks does it pose? (3) What risk management approaches exist and how effective are they? Advocates "defence-in-depth" — layering multiple imperfect safeguards across development, deployment, and societal resilience.

- **Main contributions:**
  - Updated capability assessment (reasoning systems, AI agents, inference-time scaling)
  - Risk taxonomy: malicious use (content generation, manipulation, cyberattacks, CBRN), malfunctions (reliability, loss of control), systemic risks (labour markets, human autonomy)
  - Comprehensive review of risk management practices including Frontier AI Safety Frameworks, if-then commitments, technical safeguards, open-weight model challenges
  - OECD-developed capability scenarios through 2030 (stall, slow, continue, accelerate)
  - Identification of the "evaluation gap" — pre-deployment evaluations do not reliably predict real-world behaviour

- **What is novel or unique:** Second edition of the only internationally mandated scientific assessment of AI safety, with nominees from 30+ countries. Introduces structured capability forecasts (OECD scenarios), narrows scope to "emerging risks" at the frontier, and provides the most comprehensive publicly available mapping of Frontier AI Safety Framework architectures across 11 companies.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Discusses defence-in-depth combining multiple safeguard layers (training interventions, deployment filters, monitoring, societal resilience) but does not formalise a hybrid deterministic-probabilistic architecture. References adversarial training, content filters, chain-of-thought monitoring as layered controls. |
| Safety-critical AI decision-making | Yes | Core focus. Covers reliability challenges in high-stakes settings (medicine, finance, critical infrastructure), agent autonomy risks, and the insufficiency of current safeguards for safety-critical deployment. |
| AI governance / control mechanisms | Yes | Extensive treatment. Reviews 11 Frontier AI Safety Frameworks with risk tiers and if-then commitments. Covers Level 1-type participation governance (capability thresholds triggering deployment restrictions) extensively. Identifies binary control as the dominant paradigm. |
| Low-resource environments | Partial | Notes uneven AI adoption (under 10% in much of Africa, Asia, Latin America), performance degradation in low-resource languages, and challenges for lesser-resourced actors. Does not address low-resource operational environments (connectivity, compute constraints) as architectural design considerations. |
| Decision architecture formalisation | Partial | References formal verification, safety cases, and probabilistic risk assessment as emerging methods. Does not define formal decision architectures comparable to E → S = f(E) → (G(S), A_AI(S)) → AI(E). Discusses risk tiers/thresholds but these are organisational rather than formally modelled. |
| Human role in decision-making | Yes | Discusses human-in-the-loop, automation bias, cognitive offloading, over-reliance on AI, and the tension between AI autonomy and human oversight. Notes human oversight is "often impractical" and limited by automation bias. |
| Socio-technical evaluation | Yes | Advocates for "evaluation science" beyond benchmarks, including field-testing, sociotechnical safety evaluation, real-world deployment monitoring, and incident reporting. Identifies the evaluation gap as a central challenge. |
| Coastal fisheries / maritime domain | No | Not addressed. |

**Yes/Partial count:** 5 Yes, 3 Partial → **FULL EXTRACTION**

---

### 4. Decision Architecture Analysis

- **Decision-making structure:** The report does not describe a single decision architecture but rather a **layered defence-in-depth model** for AI risk management. This operates across four sequential stages: (1) training interventions (data curation, RLHF, adversarial training, unlearning), (2) deployment interventions (content filters, chain-of-thought monitors, sandboxing), (3) post-deployment monitoring (user interaction monitors, incident reporting), and (4) societal resilience (education, detection tools, legal frameworks).

- **Layered architecture / governance structure:** Yes — the report describes a "Swiss cheese" defence-in-depth model (Figure 3.5) where multiple imperfect safeguard layers compensate for individual failures. Organisationally, Frontier AI Safety Frameworks implement risk tiering with capability thresholds triggering graduated responses.

- **Rule-based constraints before AI decisions:** Yes — described at multiple levels: input/output content filters, acceptable use policies, capability thresholds that gate deployment decisions, and hardware-based monitoring mechanisms. These are applied *before* or *alongside* AI operation.

- **Boundary between deterministic control and AI reasoning:** Not formally defined. The report describes the boundary implicitly through safeguard layers: deterministic rules (filters, thresholds, sandboxing) constrain probabilistic AI operation, but the boundary is enforced through engineering practice rather than formal specification.

- **Failure modes, fallback behaviour, override mechanisms:** Extensively discussed. Identifies: hallucinations, out-of-distribution failures, tool use failures, multi-agent miscoordination, adversarial attacks (jailbreaks, prompt injection), reward hacking, situational awareness enabling evaluation gaming, and autonomous replication attempts. Fallback mechanisms include human-in-the-loop, sandboxing, and staged deployment. However, the report notes that "no combination of methods ensures the high reliability required in critical domains."

---

### 5. Formal Model and Mathematical Representation

- **Formal model defined?** No. The report does not define a formal mathematical model of any AI safety or governance system. It references formal verification and safety cases as aspirational methods but notes they "cannot currently be scaled to large models" and "rely on assumptions."

- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** The report describes analogous *concepts* but without formalisation:
  - **E (environmental state):** Frontier AI Safety Frameworks reference "capability levels" and "risk thresholds" that function as state inputs, but these are measured via evaluations rather than environmental sensing.
  - **S = f(E) (safety state classification):** Risk tiering in Frontier AI Safety Frameworks (e.g., Anthropic's ASL-1 through ASL-4+, OpenAI's High/Critical, Google's Critical Capability Levels) performs a classification function analogous to S = f(E), but based on *model capability* rather than *environmental conditions*.
  - **G(S) (gate function):** Clearly present — all frameworks implement binary or graduated participation gates (deploy / don't deploy / halt development) triggered by capability thresholds.
  - **A_AI(S) (admissible action space):** **Not present as a formal concept.** Frameworks restrict *deployment context* and *access controls* when thresholds are crossed, but do not formally define a state-conditioned restriction of the *types of recommendations* AI is permitted to generate.

- **State-dependent recommendation restriction (A_AI varies across safety states)?** No. The report documents that existing frameworks gate AI participation (Level 1) but do not formally restrict AI advisory scope conditioned on classified safety state (Level 2). Access controls and deployment restrictions are applied, but these operate at the system/deployment level, not at the recommendation-type level.

- **Safety Dominance Property (AI(E) ⊆ A_AI(S))?** No formal property comparable to this is defined in any framework reviewed. The report notes that "developers cannot yet provide robust, quantifiable assurances that AI systems will avoid specific harmful behaviours." Formal verification methods that could support such a property are described as immature and unscalable.

- **Formalisation purpose:** The limited formalisation present (risk tiers, capability thresholds) is used for *organisational decision-making* (deploy/don't deploy) rather than for formal analysis or proof.

---

### 6. Safety State Classification

- **Discrete risk/safety levels?** Yes — extensively documented across 11 Frontier AI Safety Frameworks. Classification schemes include:
  - **Anthropic:** ASL-1 (no significant risk) → ASL-2 (early dangerous capabilities) → ASL-3 (substantially increased catastrophic misuse risk) → ASL-4+ (undefined)
  - **OpenAI:** High (amplify existing pathways to severe harm) → Critical (unprecedented new pathways)
  - **Google DeepMind:** Critical Capability Levels with early warning evaluations and alert thresholds
  - **Meta:** Moderate → High → Critical
  - **NVIDIA:** MR1–MR5 risk scores
  - **Cohere:** Low → Medium → High → Very High

- **How thresholds are defined:** Via capability evaluations, red-teaming, and benchmark performance on dangerous capability domains (CBRN, cyber, autonomous AI R&D). Thresholds are typically qualitative ("could amplify existing pathways") rather than quantitative. The report notes that "unlike risk management approaches from other sectors, such as aviation or nuclear power, Frontier AI Safety Frameworks typically do not use explicit quantitative risk thresholds."

- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Frontier AI Safety Frameworks classify based on **model capability** (what the AI *can* do), not **environmental state** (what conditions the AI operates in). This is a fundamentally different classification input. The output is typically binary (deploy/don't deploy) or graduated (deploy with mitigations / don't deploy / halt development), but the graduation governs *deployment decisions*, not *recommendation scope*.

- **Does AI recommendation scope vary across safety levels?** **No.** This is a critical finding for my research. When frameworks escalate risk levels, they apply:
  - Enhanced security controls
  - Access restrictions (user vetting, API-only access)
  - Additional monitoring
  - Deployment restrictions or halts
  
  But they do **not** define a restricted-but-non-empty recommendation space where AI still participates under constrained advisory scope. The response is either "deploy with additional safeguards" or "don't deploy" — a binary participation decision, not a graduated advisory scope restriction.

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (equivalent to G(S)) | **Yes** | All 11 Frontier AI Safety Frameworks implement capability thresholds that determine whether a model is deployed. If-then commitments specify conditions under which deployment is restricted or halted. Google's "Critical Capability Levels," Anthropic's ASL system, OpenAI's Preparedness Framework all function as participation gates. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (equivalent to A_AI(S)) | **No** | No framework reviewed defines state-conditioned restrictions on the *types* of recommendations AI may generate. Safeguards (content filters, acceptable use policies) constrain outputs, but these are static (same filtering regardless of safety state) or per-interaction (responding to individual harmful prompts), not conditioned on a classified environmental or system safety state. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Level 1 is well-established but conditioned on model capability assessments, not environmental state. Level 2 does not exist as a formal governance mechanism in any reviewed framework. |

- **Binary switch or graduated governance?** The report documents that existing governance is primarily **binary at the participation level** (deploy / don't deploy), with some graduation in the *intensity of safeguards* applied (e.g., NVIDIA's MR1–MR5 with escalating review requirements, Anthropic's ASL levels with escalating security standards). However, this graduation governs the *rigor of controls around deployment*, not the *scope of AI advisory output*.

- **Level 2 governance: state-conditioned or static?** Where output constraints exist (content filters, acceptable use policies), they are **static** — applied uniformly regardless of operational safety state. The report does not identify any framework where output constraints vary based on classified safety state.

- **Support or contradict the two-level governance pair?** **Strongly supports the gap claim.** The report comprehensively documents that:
  1. Level 1 governance (participation control) is well-established and increasingly sophisticated
  2. Output constraints exist (content filters, guardrails) but are static and per-interaction
  3. No framework unifies participation governance and advisory scope governance under a classified safety state
  4. The dominant paradigm is binary: AI operates fully or is blocked entirely

---

### 8. Human Role in Decision-Making

- **Human involvement:** The report positions AI systems primarily as tools that should operate under human oversight, but documents a trajectory toward increasing autonomy. AI agents are described as "designed to pursue goals... with much less oversight or assistance from humans." The human role varies by deployment context — from direct oversight in safety-critical settings to minimal oversight in consumer chatbots.

- **Decision support vs. decision automation:** The report documents both paradigms coexisting. Consumer AI (chatbots, coding assistants) operates as decision support. AI agents increasingly approach decision automation, especially in software engineering. The report raises concerns that "AI agents pose heightened risks because they act autonomously, making it harder for humans to intervene before failures cause harm."

- **Human-AI interaction:** Information is presented through chat interfaces, API outputs, and increasingly through autonomous agent actions. The report notes automation bias as a significant concern — users "place more trust in the AI system than is warranted."

- **Override/escalation mechanisms:** Human-in-the-loop is described as an important safeguard but is "often impractical" due to speed requirements, cognitive limitations, and automation bias. Sandboxing restricts agent autonomy but limits functionality.

---

### 9. System Constraints and Environment

- **Real-world constraints:** The report addresses several constraints relevant to low-resource environments:
  - **Data limitations:** Performance degrades for low-resource languages; models "correctly answered 79% of questions about everyday US culture but only 12% of questions about Ethiopian culture"
  - **Compute constraints:** Training costs are hundreds of millions of dollars; inference costs matter for deployment
  - **Connectivity:** Not explicitly addressed as a design constraint
  - **User expertise:** Automation bias and AI literacy are identified as challenges
  - **Uneven adoption:** "Across much of Africa, Asia, and Latin America adoption rates likely remain below 10%"

- **Real-world deployment vs. simulation:** The report emphasises the "evaluation gap" — systems perform differently in controlled settings versus real-world deployment. Advocates for field-testing and post-deployment monitoring.

- **Resource-aware design choices:** Discussed in the context of open-weight models enabling "less well-resourced actors" to access AI capabilities. Distillation is noted as enabling capable models at lower cost. However, resource-aware *safety* design (lightweight safety mechanisms, offline capability, graceful degradation) is not discussed.

- **Edge cases / resource-limited conditions:** The report notes that "current agents reliably fail on longer tasks, lose track of their progress, and often cannot adapt to unexpected obstacles." Performance in edge cases is identified as a significant evidence gap.

---

### 10. Hybrid AI Taxonomy

- **Type of hybrid AI approach:** The report describes a **defence-in-depth / supervisory control** paradigm:
  - Deterministic components: content filters, acceptable use policies, capability thresholds, sandboxing
  - Probabilistic components: neural network-based AI models, chain-of-thought reasoning
  - Monitoring components: chain-of-thought monitors, internal state monitors, user interaction monitors
  
  This is closest to **supervisory control** (AI output monitored by rule-based supervisor) combined with **stage-gate** elements (sequential checkpoints regulate deployment).

- **Where safety enforcement sits:** At **multiple stages** — before AI reasoning (input filters, capability gating), alongside it (chain-of-thought monitoring, internal state monitoring), and after it (output filters, human-in-the-loop). This is the defence-in-depth principle.

- **Two-level governance support?** The hybrid approach described supports **Level 1 governance only**. The supervisory/filtering mechanisms constrain AI outputs per-interaction but do not implement state-conditioned advisory scope restriction (Level 2). The report's entire framing is: either the AI operates (with safeguards applied uniformly) or it doesn't.

- **Comparison to my architecture:** The report's defence-in-depth model operates at the *safeguard implementation* level, not the *decision architecture* level. My architecture formalises governance as an integral part of the decision pipeline (E → S → (G(S), A_AI(S)) → AI(E)), whereas the report describes governance as external controls applied *around* the AI system. The key architectural difference is that my model makes governance *structural* (embedded in the architecture) rather than *supervisory* (applied as external constraints).

---

### 11. Baseline Comparison and Evaluation

- **Baseline comparison?** Not in the traditional sense. The report compares current safeguards against adversarial attacks and documents declining but still high attack success rates (Figure 3.9). It also compares AI performance across capability benchmarks over time.

- **Metrics:** Attack success rates for jailbreaks, benchmark scores (GPQA Diamond, SWE-bench, FrontierMath, SimpleQA), task completion times, hallucination rates, and adoption statistics.

- **Evaluation methods:** Benchmarks, red-teaming, bug bounty programmes, field-testing, incident reporting. The report is critical of all methods, noting the evaluation gap and that "the absence of identified risks does not imply that those risks are low."

- **CAUTION zone testing?** **No.** No framework or evaluation tests behaviour in a mode where AI participates under restriction (G(S) = 1 but A_AI restricted). Evaluations test whether AI should operate at all (capability thresholds) or whether specific outputs are harmful (content filtering), not whether AI should operate with restricted advisory scope.

- **Safety Dominance Property verification?** **No.** No evaluation verifies a formal property comparable to AI(E) ⊆ A_AI(S). The report notes that "developers cannot yet provide robust, quantifiable assurances."

- **Graduated vs. binary governance comparison?** **Not tested.** No framework or evaluation compares the effectiveness of graduated governance (Level 1 + Level 2) against binary governance (Level 1 only).

- **Evaluation gaps:** Extensive — including inability to predict real-world performance from benchmarks, lack of standardised agent evaluations, limited evidence on safeguard effectiveness in deployment, and absence of quantitative risk thresholds.

---

### 12. Key Concepts and Definitions

- **Defence-in-depth:** "A strategy that involves implementing multiple layers of independent safeguards, such that if one measure fails, others remain in place to prevent harm" — directly relevant as a design principle, though lacking formal specification.

- **Frontier AI Safety Framework:** "A set of protocols created by an AI developer, typically structured as if-then commitments, that specifies safety or security measures that they will take when their AI systems reach predefined thresholds" — the primary organisational governance mechanism reviewed.

- **If-then commitments:** "Conditional protocols that trigger specific responses when AI models and systems reach predefined capability thresholds" — analogous to my gate function G(S) but triggered by capability assessments rather than environmental state.

- **Evaluation gap:** "How a system performs in pre-deployment evaluations like benchmark testing often seems to overstate its practical utility, because such evaluations do not capture the full complexity of real-world tasks" — validates my emphasis on real-world operational conditions.

- **Evidence dilemma:** "The challenge that policymakers face when making decisions about a new technology before there is strong scientific evidence about its benefits or risks" — contextualises the need for formal governance architectures that can operate under uncertainty.

- **Safety case:** "A structured argument, supported by evidence, that a system is acceptably safe to operate in a particular context" — an emerging practice that could benefit from formal safety properties like the Safety Dominance Property.

- **Sandbagging:** "Behaviour where a model or system performs below its capabilities on evaluations, potentially to avoid further scrutiny or restrictions" — a failure mode that my architecture addresses by making safety classification independent of AI self-reporting (based on environmental state E, not AI performance).

- **Marginal risk:** "The extent to which the deployment or release of a model counterfactually increases risk beyond that already posed by existing models or other technologies."

- **Risk tolerance / risk threshold:** Qualitative or quantitative limits distinguishing acceptable from unacceptable risks — the report notes these are typically qualitative in AI, unlike other safety-critical industries.

---

### 13. Limitations and Unsolved Problems

**Stated limitations:**
- "No combination of safeguards is perfectly reliable" — fundamental limitation acknowledged
- Evaluation gap persists — benchmarks don't predict real-world behaviour
- Limited interpretability — "current techniques for understanding how AI models produce their outputs also remain unreliable"
- Information asymmetries — developers hold proprietary information about development processes
- Competitive pressures — "firms that invest heavily in risk mitigation may face competitive disadvantages"
- Cross-border coordination challenges
- Frontier AI Safety Frameworks "vary substantially in scope, thresholds, and enforceability" and their real-world effectiveness is uncertain

**Unsolved problems:**
- How to provide "robust, quantifiable assurances that AI systems will avoid specific harmful behaviours"
- How to design evaluations that reliably predict real-world risk
- How to balance open-weight model benefits against irreversible release risks
- How to attribute liability for AI agent harms
- How to manage the offence-defence balance in dual-use capabilities

**Gaps aligned with my research problem:**

1. **Lack of a two-level governance model:** The report documents extensively that existing governance operates at Level 1 (participation control) only. Output constraints exist (Level 2 *elements*) but are static and per-interaction, not state-conditioned. No framework implements the unified governance pair (G(S), A_AI(S)) conditioned on classified safety state. This is the central gap my architecture addresses.

2. **Absence of a CAUTION mode:** The report confirms that the dominant paradigm is binary — AI operates fully or is blocked entirely. No framework defines an intermediate mode where AI participates under restricted recommendation scope. The graduated risk tiers in Frontier AI Safety Frameworks govern *deployment decisions and safeguard intensity*, not *AI advisory scope*.

3. **Absence of a formal Safety Dominance Property:** The report notes that formal verification methods "cannot currently be scaled to large models" and that "developers cannot yet provide robust, quantifiable assurances." No framework defines a formal property guaranteeing that AI outputs fall within state-determined bounds.

4. **Environmental state as governance input:** Frontier AI Safety Frameworks classify based on *model capability* (what the AI can do), not *environmental conditions* (what the operational context is). My architecture's use of environmental state vector E = {w, r, m, o, v, t} as the governance input is architecturally distinct from all frameworks reviewed.

---

### 14. Methodology Notes

- **Research method:** International scientific assessment / structured literature synthesis. Over 100 expert contributors, Expert Advisory Panel with nominees from 30+ countries, structured multi-stage review process (external subject-matter experts → Expert Advisory Panel → Senior Advisers → industry and civil society representatives).

- **Alignment with DSR pipeline:** Partial alignment. The report performs *synthesis and assessment* but does not follow a design-formalise-prototype-evaluate cycle. It informs the *contextual grounding* and *gap identification* stages of my DSR pipeline but does not itself employ DSR.

- **Methodological insights for my research:**
  - The report's comprehensive mapping of Frontier AI Safety Framework architectures (Table 3.5) provides a validated baseline comparison structure
  - The OECD capability scenarios (stall/slow/continue/accelerate) could inform scenario-based evaluation of my architecture
  - The emphasis on defence-in-depth and the "Swiss cheese" model provides a framing within which my two-level governance pair can be positioned as an architectural layer
  - The documentation of the evaluation gap validates my approach of using formal properties (Safety Dominance Property) rather than relying solely on empirical evaluation

---

### 15. Quotable / Citable Points

1. **On the binary governance paradigm (§3.3, Table 3.6):** The report documents that all reviewed technical safeguards and Frontier AI Safety Frameworks implement either full AI operation with uniform safeguards or complete blocking — confirming the binary control paradigm as the state of the art.

2. **On the absence of quantitative risk thresholds (§3.2):** "Unlike risk management approaches from other sectors, such as aviation or nuclear power, Frontier AI Safety Frameworks typically do not use explicit quantitative risk thresholds" — supports my argument for formal safety state classification.

3. **On the limits of current assurances (§3.1):** "Developers cannot yet provide robust, quantifiable assurances that AI systems will avoid specific harmful behaviours" — motivates the Safety Dominance Property as a formal guarantee.

4. **On the evaluation gap (§3.1):** "How a system performs in pre-deployment evaluations like benchmark testing often seems to overstate its practical utility, because such evaluations do not capture the full complexity of real-world tasks" — validates the need for architecturally embedded safety rather than reliance on evaluation alone.

5. **On defence-in-depth (§3.2):** The Swiss cheese model (Figure 3.5) where "multiple layers of defences can compensate for flaws in individual layers" — provides the meta-framework within which my two-level governance pair operates as a formal architectural layer.

---

### 16. Relation to My Research and Positioning

- **Level 1 governance implemented?** Yes — extensively documented across all 11 Frontier AI Safety Frameworks. Capability thresholds trigger deployment decisions (deploy / restrict / halt).

- **Level 2 governance implemented?** No — not as a formal, state-conditioned mechanism. Output constraints exist (content filters, acceptable use policies) but are static and per-interaction, not conditioned on classified safety state.

- **State-conditioned?** Level 1 is conditioned on *model capability assessments*, not on *environmental state*. Level 2 does not exist as a state-conditioned mechanism.

- **Proximity to (G(S), A_AI(S))?** The Frontier AI Safety Frameworks come closest to Level 1 governance (G(S)) but differ in their classification input (model capability vs. environmental state). None approaches the unified two-level governance pair. The gap between current practice and my architecture is significant and well-documented by this report.

- **Formal safety property?** No. No framework defines a property comparable to the Safety Dominance Property. The report identifies formal verification as an aspiration but notes fundamental scalability limitations.

- **Gap my research addresses:** The report comprehensively documents that: (1) all existing governance is binary at the participation level, (2) output constraints are static rather than state-conditioned, (3) no framework unifies participation and advisory scope governance, (4) governance is triggered by model capability assessments rather than operational environmental state, and (5) no formal safety properties guarantee bounded AI behaviour under graduated governance. My architecture addresses all five gaps through the formally defined pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) with the Safety Dominance Property.

**Positioning paragraph:**

This report serves as the **definitive institutional baseline** for my literature review's treatment of the AI safety governance landscape. As the most comprehensive, internationally mandated assessment of AI safety practices, it provides authoritative documentation of the current state of the art in AI governance — and its limitations. The report's exhaustive mapping of 11 Frontier AI Safety Frameworks confirms that the dominant governance paradigm is binary participation control (Level 1), with no framework implementing state-conditioned advisory scope restriction (Level 2). Its identification of the evaluation gap, the absence of quantitative risk thresholds, and the inability to provide formal safety assurances collectively motivate my architecture's core contribution: a formally defined two-level governance pair (G(S), A_AI(S)) conditioned on environmental safety state, with a provable Safety Dominance Property. The report's defence-in-depth framework provides the meta-architectural context within which my graduated governance model operates as a formal layer — one that addresses the specific structural gap between "AI fully operates" and "AI is blocked" that the report documents but does not resolve.

---

### 17. Overall Relevance Score

## ⭐⭐⭐⭐ High

**Justification:** This report is the authoritative institutional reference on the current state of AI safety governance. It provides comprehensive documentation of the binary governance paradigm across all major Frontier AI Safety Frameworks, directly confirming the gap that my two-level governance architecture addresses. It does not itself propose formal architectures or address the coastal fisheries domain, preventing a ⭐⭐⭐⭐⭐ rating. However, it is essential for: (1) establishing that binary control is the universal paradigm, (2) documenting that no framework implements state-conditioned advisory scope restriction, (3) confirming the absence of formal safety properties in current practice, and (4) providing the defence-in-depth meta-framework within which my architecture is positioned. It should be treated as a **primary background/gap-evidence source** — the institutional counterpart to the technical gap evidence provided by papers like AgentSpec, Shields for Safe RL, and Towards Guaranteed Safe AI.

**Functional role in literature review:** Background/gap evidence — institutional baseline confirming the binary governance paradigm and the absence of graduated, state-conditioned AI advisory scope governance.
