# Chapter 2: Literature Review – Full Writing Guide

## Research Title
Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments

---

# 1. Purpose of Chapter 2

The literature review builds a structured argument that:

- AI is widely used in decision support systems  
- Safety is a critical concern in such systems  
- Existing approaches manage safety in different ways  
- However, these approaches are fragmented  
- There is no unified governance of AI behaviour  
- Therefore, a new architecture is required  

---

# 2. Writing Strategy

Each section must follow:

1. What exists  
2. How it works  
3. Limitation  
4. Link to research gap  

Avoid:
- Paper-by-paper summaries  
- Descriptive listing  

Focus on:
- Mechanisms  
- Patterns  
- Structural differences  

---

# 3. Section-by-Section Writing Guide

---

## 2.1 AI Decision Support in Safety-Critical Systems

**Paragraph 1 – Context**
- AI used in maritime, aviation, healthcare, industry  
- Supports human decision-making  
- Provides predictions, recommendations, risk assessments  

**Paragraph 2 – Benefits**
- Improves decision quality  
- Reduces cognitive load  
- Handles complex and large data  
- Enhances situational awareness  

**Paragraph 3 – Problem**
- AI may produce incorrect recommendations  
- Model limitations and uncertainty  
- Risk of over-reliance  
- Unsafe outcomes possible  

**Paragraph 4 – Gap Transition**
- Research focuses on improving accuracy  
- Limited focus on governing AI behaviour  
- Missing:
  - control of AI participation  
  - control of advisory scope  

---

## 2.2 Deterministic Safety Constraints and Safety Gating

**Paragraph 1 – What Exists**
- Rule-based safety systems  
- Runtime verification  
- Safety filters and safety shields  

**Paragraph 2 – Mechanism**
- Binary gating (allow / block)  
- Prevent unsafe actions  
- Switch to fallback  

**Paragraph 3 – Limitation**
- Too rigid  
- No intermediate state  
- Cannot represent partial risk  

**Paragraph 4 – Gap Transition**
- Focus on action restriction  
- No control over recommendation scope  
- Need more flexible governance  

---

## 2.3 Human–AI Decision Authority

**Paragraph 1 – Concept**
- Human-in-the-loop  
- Human-on-the-loop  
- Levels of automation  

**Paragraph 2 – Mechanism**
- Decision authority shifts  
- AI suggests, human decides  
- Varies by context  

**Paragraph 3 – Limitation**
- Focus on who decides  
- Does not control what AI recommends  

**Paragraph 4 – Gap Transition**
- AI outputs remain unchanged across risk levels  
- No structured advisory control  

---

## 2.4 Adaptive Autonomy and Risk-Based Systems

**Paragraph 1 – What Exists**
- Adaptive autonomy  
- Risk-aware systems  
- Degraded modes  

**Paragraph 2 – Mechanism**
- Behaviour changes based on risk  
- Switch between modes  

**Paragraph 3 – Limitation**
- Changes control authority only  
- AI still produces same recommendations  

**Paragraph 4 – Gap Transition**
- Need to restrict advisory capability  
- Not just autonomy  

---

## 2.5 AI Governance and Guardrails

**Paragraph 1 – What Exists**
- Guardrails  
- Policy constraints  
- Output filtering  

**Paragraph 2 – Mechanism**
- Post-hoc filtering  
- Modify/remove unsafe outputs  

**Paragraph 3 – Limitation**
- Does not prevent unsafe reasoning  
- Not integrated with safety state  

**Paragraph 4 – Gap Transition**
- Need pre-hoc governance  
- Need integration with safety conditions  

---

## 2.6 Hybrid AI Systems

**Paragraph 1 – What Exists**
- Rule-based + machine learning  
- Neuro-symbolic systems  

**Paragraph 2 – Purpose**
- Improve accuracy  
- Improve explainability  
- Improve robustness  

**Paragraph 3 – Limitation**
- Focus on performance  
- Does not govern AI participation  
- Does not restrict advisory scope  

---

## 2.7 AI in Low-Resource Environments

**Paragraph 1 – Context**
- Limited connectivity  
- Limited computation  
- Mobile-based usage  

**Paragraph 2 – Challenges**
- Sparse/noisy data  
- Limited infrastructure  
- Human-dependent decisions  

**Paragraph 3 – Gap**
- No safety-aware governance  
- No structured AI control  

---

## 2.8 Fisheries Decision Context

**Paragraph 1 – Context**
- Small-scale fisheries  
- High uncertainty  
- Human-driven decisions  

**Paragraph 2 – Risk Factors**
- Weather  
- Sea state  
- Visibility  
- Time of day (important for E)  

**Paragraph 3 – Gap**
- Lack of structured decision support governance  
- No control over AI advisory behaviour  

---

## 2.9 Comparative Analysis

**Paragraph 1 – Purpose**
- Compare systems at architecture level  
- Focus on decision governance  

**Paragraph 2 – Comparison Dimensions**
- Participation Control → whether AI can act  
- Advisory Restriction → what AI can recommend  
- Unified Governance → integration of both  

**Paragraph 3 – Table**

| System Type            | Participation Control | Advisory Restriction | Unified Governance |
|-----------------------|----------------------|---------------------|-------------------|
| Safety Gating         | ✔ Yes                | ✖ No                | ✖ No              |
| Adaptive Autonomy     | ✔ Yes                | ✖ No                | ✖ No              |
| Guardrails            | ✖ No (indirect)      | ✔ Yes (post-hoc)    | ✖ No              |
| Hybrid AI             | ✖ No                 | ✖ No                | ✖ No              |
| This Research         | ✔ Yes                | ✔ Yes               | ✔ Yes             |

**Paragraph 4 – Interpretation**
- Safety gating → participation only  
- Adaptive autonomy → authority only  
- Guardrails → output filtering only  
- Hybrid AI → no governance  

**Paragraph 5 – Key Insight**
- Existing systems implement one mechanism only  
- No unified governance structure  

**Paragraph 6 – Link to Research**
- Proposed architecture integrates:
  - G(S)  
  - A_AI(S)  
- Controlled by safety state  

**Paragraph 7 – Transition**
- Leads to identified research gap  

---

## 2.10 Literature Summary

**Paragraph 1 – Synthesis**
- Safety gating → controls participation  
- Adaptive autonomy → controls authority  
- Guardrails → control outputs  
- Hybrid AI → improves reasoning  

**Paragraph 2 – Limitation**
- Fragmented approaches  
- Lack of integration  

---

## 2.11 Research Gap

**Paragraph 1 – Core Gap**
- No system jointly governs:
  - AI participation  
  - advisory scope  
- No state-conditioned governance  

**Paragraph 2 – Limitation of Existing Work**
- Binary safety models  
- No intermediate state (CAUTION)  
- No advisory containment  

**Paragraph 3 – Contribution Link**
- Need graduated safety-state-gated architecture  
- Need unified governance (G, A_AI)  

---

# 4. Transition to Chapter 3

End Chapter 2 with:

> Therefore, this research proposes a graduated safety-state-gated architecture for AI decision support that defines how safety conditions govern both AI participation and advisory scope.

---

# 5. Final Checklist

Before finalising:

- Clear logical flow  
- No repetition  
- No paper-by-paper writing  
- Strong gap statement  
- Smooth transition to architecture  

---

# 6. Key Writing Principle

The entire chapter answers:

> How do existing systems control AI behaviour under risk?

Final answer:

> They do not do it completely.