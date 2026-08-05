# Literature Review Improvement Plan
**PhD Research:** Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments

---

# 1. Purpose of This Plan
This document outlines the improvement plan for the literature review chapter. The literature review should not be a collection of paper summaries. Instead, it should build a logical argument that leads to the research gap and motivates the proposed architecture.

The literature review must guide the reader step-by-step toward the need for a graduated safety-state-gated architecture.

---

# 2. Objective of the Literature Review
By the end of the literature review, the reader should understand the following:

1. AI is increasingly used for decision support in safety-critical systems.
2. Deterministic safety constraints are used to prevent unsafe actions.
3. Human–AI decision authority is an important issue.
4. Some systems change autonomy level based on risk or context.
5. AI governance and guardrails are emerging research areas.
6. Low-resource environments introduce additional constraints.
7. Existing systems do not jointly govern AI participation and AI advisory scope using safety states.
8. Therefore, a graduated safety-state-gated architecture is needed.

This logical flow should guide Chapter 2.

---

# 3. Proposed Literature Review Structure (Chapter 2)

## 2.1 AI Decision Support in Safety-Critical Systems
**Purpose:**  
Introduce AI decision support systems and associated risks.

**Topics to include:**
- AI decision support systems
- Safety-critical decision systems
- Maritime, aviation, medical, industrial safety
- Decision support vs autonomous decision making

**Key conclusion:**  
AI decision support improves decision quality but incorrect AI recommendations in safety-critical environments can lead to serious consequences.

---

## 2.2 Deterministic Safety Constraints and Rule-Based Safety Systems
**Purpose:**  
Show how safety rules and constraints are used to prevent unsafe actions.

**Topics to include:**
- Rule-based safety systems
- Constraint-based control
- Safety envelopes
- Runtime verification
- AI safety filters / shields
- Rule engines
- Safety constraint enforcement

**Key limitation to highlight:**  
Most systems block unsafe actions but do not restrict AI advisory reasoning scope.

---

## 2.3 Human–AI Decision Authority and Decision Support Systems
**Purpose:**  
Discuss decision authority between human and AI.

**Topics to include:**
- Decision support systems
- Human-in-the-loop
- Human-on-the-loop
- Supervisory control
- Automation levels
- Decision authority allocation
- Explainable AI advisory systems

**Key limitation to highlight:**  
These systems usually do not define when AI should participate based on safety conditions.

---

## 2.4 Risk-Adaptive and Graduated Autonomy Systems
**Purpose:**  
Review systems that change autonomy level based on risk or context.

**Topics to include:**
- Adaptive autonomy
- Adjustable autonomy
- Risk-aware autonomy
- Operational modes
- Safe / caution / emergency modes
- Degraded modes
- Authority switching
- Context-aware autonomy

**Key limitation to highlight:**
- Autonomy level changes
- Advisory scope is not formally restricted
- No containment relationship between advisory capabilities
- Governance functions are not formally defined

This section is expected to contain the closest literature to the proposed architecture.

---

## 2.5 AI Governance, Guardrails, and Safety Architectures
**Purpose:**  
Introduce AI governance and guardrail concepts.

**Topics to include:**
- AI governance frameworks
- AI guardrails
- Trustworthy AI
- AI safety architectures
- Risk management frameworks
- Safety assurance
- Responsible AI

**Key limitation:**  
Most governance frameworks operate at policy or system level, not runtime decision architecture level.

---

## 2.6 Hybrid AI and Neuro-Symbolic Systems
**Purpose:**  
Review hybrid AI approaches combining deterministic rules and machine learning.

**Topics to include:**
- Hybrid AI
- Neuro-symbolic AI
- Rule + ML systems
- Explainable AI
- Knowledge-based AI
- Constraint-guided AI

**Key positioning statement:**  
Most hybrid AI research focuses on improving prediction accuracy and explainability, not on governing whether AI is allowed to participate in decision-making and what AI is allowed to recommend.

---

## 2.7 AI Systems in Low-Resource Environments
**Purpose:**  
Justify the low-resource environment context in the research title.

**Topics to include:**
- Mobile-based decision systems
- Edge AI
- Intermittent connectivity systems
- ICT4D (Information and Communication Technology for Development)
- Rural decision support systems
- Technology adoption in developing regions
- Socio-technical systems in rural communities
- Low-compute AI systems

**Key idea:**  
AI systems in low-resource environments must operate with limited connectivity, limited compute resources, and users with varying levels of digital literacy.

---

## 2.8 Technology and Decision Support in Small-Scale Fisheries
**Purpose:**  
Justify the case study domain (coastal fisheries).

**Topics to include:**
- Fisheries decision support systems
- Marine weather decision tools
- Navigation safety tools
- Fisheries information systems
- Technology for small-scale fisheries
- Livelihood technology
- Community technology adoption
- Socio-technical fisheries systems

---

## 2.9 Literature Summary and Research Gap
This section summarises the limitations of existing studies.

### Literature Summary Table
| Area | What Exists | Limitation |
|------|-------------|-----------|
| Safety rules | Block unsafe actions | Do not control AI advisory scope |
| Decision support | AI gives advice | Do not control when AI participates |
| Adaptive autonomy | Change authority level | Do not formalise advisory containment |
| AI governance | High-level governance | Not runtime decision architecture |
| Hybrid AI | Combine rules and ML | Focus on accuracy, not governance |
| Low-resource AI | Focus on deployment | Not safety-gated decision architecture |

### Research Gap Statement
Existing studies implement safety constraints, decision support systems, adaptive autonomy, AI governance frameworks, and hybrid AI approaches independently. However, the literature does not present an architectural model in which environmental safety state simultaneously governs both AI participation and AI advisory recommendation scope as a unified governance mechanism. Therefore, there is a lack of a formally defined graduated safety-state-gated architecture for AI decision support in safety-critical and low-resource environments.

---

# 4. Paper Review Extraction Template
For each paper reviewed, extract the following information:

| Item | Description |
|------|-------------|
| Paper Title | Title of paper |
| Domain | Aviation / Maritime / Medical / Industrial / etc |
| Type of System | Decision support / Autonomous / Hybrid |
| Governance Trigger | What triggers safety control |
| AI Participation Controlled | Yes / No |
| Advisory Scope Restricted | Yes / No |
| Graduated States | Yes / No |
| Formal Model | Yes / No |
| Human Role | Human decision / AI decision / Shared |
| Low Resource Consideration | Yes / No |
| Key Contribution | Summary |
| Limitation | What is missing |

This table will later be used to build the architecture comparison table.

---

# 5. Literature Review Writing Strategy
The literature review should be written as a logical argument, not paper summaries.

The logical flow should be:

1. AI is used for decision support.
2. Safety constraints are used to prevent unsafe decisions.
3. Human–AI decision authority is important.
4. Some systems change autonomy level based on risk.
5. AI governance and guardrails are emerging.
6. Low-resource environments require special design.
7. Existing systems do not jointly govern AI participation and advisory scope using safety states.
8. Therefore, this research proposes a graduated safety-state-gated architecture.

---

# 6. Next Action Plan
## Step 1
Group all collected papers into categories:
- AI decision support
- Safety constraints
- Human-AI decision authority
- Adaptive autonomy
- AI governance / guardrails
- Hybrid AI
- Low-resource systems
- Fisheries technology

## Step 2
For each paper, fill in the paper review extraction table.

## Step 3
Build a comparison table of architectures.

## Step 4
Write literature review sections following the proposed structure.

## Step 5
Write literature summary and research gap section.

---

# 7. Final Goal of Chapter 2
By the end of Chapter 2, the reader must clearly understand:

- How existing AI decision systems are governed
- What safety mechanisms exist
- How decision authority is managed
- How autonomy changes with risk
- What is missing in current architectures
- Why a graduated safety-state-gated architecture is needed

If Chapter 2 achieves this, the research positioning will be strong.