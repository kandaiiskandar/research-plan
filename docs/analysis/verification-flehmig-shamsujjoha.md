# VERIFICATION FINDINGS: FLEHMIG ET AL. & SHAMSUJJOHA ET AL.

**Date:** 2026-07-06
**Reviewer:** Independent Verification
**Purpose:** Verify the characterization of two key sources in the structured literature review "FROM BINARY TO GRADUATED AI GOVERNANCE: A STRUCTURED LITERATURE REVIEW OF THE ADVISORY SCOPE GAP IN SAFETY-CRITICAL DECISION SUPPORT"

---

## 1. EXECUTIVE SUMMARY

| **Source** | **Original Claim** | **Verification Status** | **Key Finding** |
|:---|:---|:---|:---|
| Flehmig et al. [7] | 3-level traffic-light; intermediate changes supervisory behavior, not AI output | ✅ **Confirmed (with nuance)** | At red, control is transferred to backup—functionally similar to blocking, but technically different |
| Shamsujjoha et al. [6] | 13 guardrail actions across 32 studies; context is static, not dynamic | ✅ **Confirmed and strengthened** | The concept of environmental-risk-based advisory scope restriction is absent from the entire taxonomy |

---

## 2. FLEHMIG ET AL. (2024) – FULL VERIFICATION

### 2.1 Source Details

| **Element** | **Value** |
|:---|:---|
| Authors | Niclas Flehmig, Mary Ann Lundteigen, Shen Yin |
| Affiliation | NTNU, Norwegian University of Science and Technology |
| Publication | IEEE IECON 2024: 50th Annual Conference of the IEEE Industrial Electronics Society |
| DOI | 10.1109/IECON55916.2024.10906021 |
| Focus | Quality assurance of AI during operation in safety-critical systems |

### 2.2 Key Findings from the Paper

#### 2.2.1 The Traffic-Light Index (Page 6, Fig. 2)

The paper proposes a three-level degradation index:

| **Level** | **Color** | **AI Status** | **Supervisory Response** |
|:---|:---|:---|:---|
| Level 1 | Green | AI functioning adequately; "recommended to have it in control" | Routine checks recommended |
| Level 2 | Orange | First signs of degradation; "still recommended to rely on the AI component" | Mandated thorough checks; investigate root causes; consider re-training |
| Level 3 | Red | Performance exceeds safe range; "control should be transferred to the conventional non-AI safety controller" | Analyze root cause; initiate countermeasures |

#### 2.2.2 Critical Quote (Page 6)

> *"To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner."*

#### 2.2.3 Scope of the Paper

The paper focuses on:
- Monitoring AI performance degradation
- Detecting concept drift and outliers
- Updating AI models (re-training, lifelong learning)
- Communicating AI status to human operators

The paper does **NOT** address:
- Restricting what the AI is permitted to recommend
- Conditioning advisory scope on environmental safety state
- Graduated recommendation spaces

### 2.3 Verification Against Original Claim

| **Original Claim** | **Actual Paper Content** | **Verdict** |
|:---|:---|:---|
| "Three-level traffic-light degradation index" | ✅ Yes – Fig. 2 shows green/orange/red | **Correct** |
| "Intermediate level changes human supervisory behaviour" | ✅ Yes – Orange: "supervisory component is mandated to conduct thorough checks" | **Correct** |
| "AI advisory scope is identical at green and orange" | ✅ Yes – "it is still recommended to rely on the AI component as the safety function" | **Correct** |
| "At red, the AI is blocked" | ⚠️ **Nuance** – Control is transferred to backup; the AI may still be running but its output is ignored | **Precision needed** |

### 2.4 Recommended Revision

**Original Text:**
> "At red, the AI is blocked; at orange, supervisory checks intensify. The AI's advisory scope, however, is identical at green and orange."

**Revised Text:**
> "At red, control is transferred to a conventional non-AI backup system, functionally removing the AI from the decision loop; at orange, supervisory checks intensify. The AI's advisory scope, however, is identical at green and orange—the intermediate level governs human supervisory behaviour, not AI recommendation content."

### 2.5 Summary for Table 1

| **Framework** | **Levels** | **Intermediate Level Exists?** | **AI Advisory Scope at Intermediate Level** | **AI Status at Red** |
|:---|:---|:---|:---|:---|
| Flehmig et al. traffic-light [7] | 3 (green/orange/red) | Yes (orange) | Unchanged—full scope (AI still "recommended" as safety function) | Control transferred to non-AI backup |

---

## 3. SHAMSUJJOHA ET AL. (2025) – FULL VERIFICATION

### 3.1 Source Details

| **Element** | **Value** |
|:---|:---|
| Authors | Md Shamsujjoha, Qinghua Lu, Dehai Zhao, Liming Zhu |
| Affiliation | Data61, CSIRO, Australia |
| Publication | IEEE 22nd International Conference on Software Architecture (ICSA) 2025 |
| Focus | Taxonomy and reference architecture for multi-layered guardrails of Foundation Model-based agents |

### 3.2 Key Findings from the Paper

#### 3.2.1 Study Scope

| **Element** | **Value** |
|:---|:---|
| Research approach | Systematic Literature Review (SLR) |
| Number of selected studies | 32 high-quality studies |
| Research Questions | 3 (quality attributes, design options, reference architecture) |
| Methodology | Kitchenham's guidelines; PICOC framework; Quality Assessment Criteria |

#### 3.2.2 Guardrail Actions Identified (Table II, Page 7)

The paper identifies **13 guardrail actions**:

| **Action** | **Description** |
|:---|:---|
| Block | Prevent specific inputs/outputs from being processed |
| Filter | Scan and remove undesired or irrelevant content |
| Flag | Mark specific items for human review |
| Modify | Adjust inputs/outputs to meet specific requirements |
| Validate | Check against predefined criteria |
| Parallel calls | Send multiple requests simultaneously |
| Retry | Attempt a request again after initial failure |
| Fall back | Redirect to previous step when execution fails |
| Human intervention | Require human review and approval |
| Defer | Postpone processing until conditions are met |
| Isolate | Segregate a specific entity or component |
| Redundancy | Implement backup processes for reliability |
| Evaluate | Assess intermediate or final results |

#### 3.2.3 Quality Attributes Identified (Pages 4-5)

The paper identifies **14 quality attributes**:

| **Quality Attribute** | **Description** |
|:---|:---|
| Accuracy | Mitigating hallucinations, misinformation, disinformation |
| Efficiency | Managing resources, preventing endless loops |
| Privacy | Protecting sensitive data, preventing leakage |
| Security | Protecting against malicious activities |
| Safety | Preventing harmful or misleading outputs |
| Fairness | Preventing bias and discrimination |
| Compliance | Adhering to legal and regulatory standards |
| Generalizability | Functioning across diverse scenarios |
| Customizability | Tailoring protection to specific needs |
| Adaptability | Adjusting to varying conditions |
| Traceability | Tracking origins, processes, decision paths |
| Portability | Applying across different agents |
| Interoperability | Working across differing technologies |
| Interpretability | Understanding how decisions are made |

#### 3.2.4 Context-Dependent Rules (Page 7)

> *"Context-dependent strategies adjust the implementation of guardrails based on the system's specific operational context. This allows for dynamic adjustments to guardrails in response to changing conditions, user needs, and operational environments [50]."*

**Critical Analysis:**

| **What Shamsujjoha Means by "Context"** | **What Your Paper Means by "Context"** |
|:---|:---|
| User location (e.g., GDPR jurisdiction) | Wave height |
| Regulatory jurisdiction | Wind speed |
| Organizational policies | Visibility |
| Operational environment (static configuration) | Visibility distance |
| User needs and preferences | Current environmental safety state S = f(E) |

**Conclusion:** "Context" in Shamsujjoha refers to **static deployment conditions**, not **dynamic environmental risk state**.

#### 3.2.5 Targets of Guardrails (Table II, Page 7)

Guardrails are applied to:

| **Target Type** | **Specific Targets** |
|:---|:---|
| Pipeline | Prompts, Intermediate results, Final results |
| Artifacts | Goals, Context, Memory, Reasoning, Plans, Workflows, Tools, Knowledge bases, Other agents, FMs |

**Critical Observation:** All targets are **internal artifacts** of the agent system. **None** is "Environmental Safety State" or "External Risk Level."

#### 3.2.6 Applicability Scope (Page 7)

| **Scope Level** | **Description** |
|:---|:---|
| Industry | Regulatory frameworks and standards |
| Organization | Internal policies and procedures |
| Team | Technical and operational constraints |
| User | Individual preferences and requirements |

**Critical Observation:** All scope levels are **static governance domains**. **None** is "Current Environmental Conditions."

### 3.3 Verification Against Original Claim

| **Original Claim** | **Actual Paper Content** | **Verdict** |
|:---|:---|:---|
| "13 guardrail actions across 32 studies" | ✅ Yes – Table II lists 13 actions | **Correct** |
| "Context-dependent rules exist" | ✅ Yes – "Context-dependent strategies adjust the implementation of guardrails" | **Correct** |
| "Context refers to static deployment conditions" | ✅ Yes – Examples: user location, regulatory jurisdiction, organizational policy | **Correct** |
| "No runtime state-conditioned advisory scope" | ✅ Confirmed – No category for environmental-risk-based scope restriction | **Correct** |
| "The concept is absent from the entire taxonomy" | ✅ Confirmed – None of 14 quality attributes, 13 actions, or targets address this | **Correct** |

### 3.4 Recommended Revision

**Original Text:**
> "Shamsujjoha et al.'s Swiss Cheese Model — the most comprehensive taxonomy of runtime AI governance, with 13 guardrail actions — acknowledges context-dependent rules, but context there refers to static deployment conditions such as user location or regulatory jurisdiction, not classified environmental safety state."

**Revised Text (Strengthened):**
> "Shamsujjoha et al.'s Swiss Cheese Model — the most comprehensive taxonomy of runtime AI governance, synthesising 32 studies and identifying 13 guardrail actions and 14 quality attributes — does not include any concept of restricting advisory scope based on environmental risk. While the taxonomy acknowledges 'context-dependent rules,' context is operationalised as static deployment conditions (user location, regulatory jurisdiction, organisational policy), not dynamic environmental safety state. The concept of an admissible recommendation space A_AI(S) that contracts as S worsens is absent from the entire taxonomy."

### 3.5 Summary for Table 1

**Option A: Add a separate row**

| **Framework** | **Levels** | **Intermediate Level Exists?** | **AI Advisory Scope at Intermediate Level** |
|:---|:---|:---|:---|
| Shamsujjoha et al. Swiss Cheese Model [6] | N/A (multi-layered guardrails) | No | Not applicable—guardrails are content filters, not scope governors |

**Option B: Add a note below the table**

> "Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts (prompts, plans, tools, FMs) and pipeline stages. All actions are content-focused (block, filter, flag, modify, validate)—none condition AI advisory scope on environmental safety state."

**Recommendation:** Option B is cleaner for the paper's flow.

---

## 4. UPDATED TABLE 1 (COMPLETE)

| **Framework** | **Levels** | **Intermediate Level Exists?** | **AI Advisory Scope at Intermediate Level** | **AI Status at Red / Maximum Risk** |
|:---|:---|:---|:---|:---|
| Shields [8], GS AI [9], safety filter [10] | 2 (on/off) | No | — | Blocked |
| Flehmig et al. traffic-light [7] | 3 (green/orange/red) | Yes (orange) | Unchanged—full scope | Control transferred to backup |
| Baxi K-tier [15] | K tiers | Yes | Varies by AI robustness, not environmental state | — |
| Tumato 2.0 [16] | 2 (permit/block per action) | No | — | — |
| Shamsujjoha et al. Swiss Cheese Model [6] | N/A (multi-layered guardrails) | No | Not applicable—content filters only | — |

---

## 5. REVISED SECTION 3.5 (FOUR-SOURCE SYNTHESIS)

**Original Section 3.5:**

> "First, the three large-scale surveys [5], [6], [7] collectively find no mechanism conditioning AI advisory scope on classified environmental safety state..."

**Revised Section 3.5 (Complete):**

> Four independent sources confirm the same absence. First, the three large-scale surveys [5], [6], [7] collectively find no mechanism conditioning AI advisory scope on classified environmental safety state. Notably, Indykov et al.'s trade-off matrix records AT11 (rule-based models) → Safety = 0 — despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. Shamsujjoha et al.'s Swiss Cheese Model, the most comprehensive guardrails taxonomy synthesising 32 studies, identifies 13 guardrail actions and 14 quality attributes — none of which address environmental-risk-based scope restriction; their "context-dependent" rules refer to static deployment conditions such as user location or regulatory jurisdiction [6]. Flehmig et al.'s traffic-light index, the closest structural precedent, classifies AI degradation into three levels but uses the intermediate level to intensify supervisory checks while leaving AI output unchanged; at red, control transfers to a non-AI backup, functionally but not technically blocking the AI [7]. Fourth, Attard-Frost and Lyons' empirical mapping of a national AI governance system, spanning 610 topics from expert interviews, contains no runtime state-conditioned advisory scope concepts; guardrails appear only in binary framing [22].

---

## 6. REVISED SECTION 4 (CONCLUSION)

**Original Conclusion:**

> "This review establishes, from multiple independent bodies of literature, that AI governance in safety-critical decision support is binary by design..."

**Revised Conclusion (Strengthened):**

> This review establishes, from multiple independent bodies of literature, that AI governance in safety-critical decision support is binary by design: participation gating exists, advisory scope gating does not. The most comprehensive guardrails taxonomy in the field—Shamsujjoha et al.'s Swiss Cheese Model, synthesising 32 studies and identifying 13 guardrail actions—contains no concept of restricting advisory scope as a function of environmental risk. The closest structural precedent, Flehmig et al.'s traffic-light index, changes human supervisory behaviour at its intermediate level but leaves AI output unchanged. Across all bodies of literature reviewed, no system formally specifies an admissible recommendation space that contracts as classified operational risk increases.

---

## 7. SUMMARY OF RECOMMENDED CHANGES

| **Change #** | **Section** | **Change Description** | **Priority** |
|:---|:---|:---|:---|
| 1 | Section 3.3 | Flehmig: red = backup transfer, not block | High |
| 2 | Section 3.3 | Flehmig: AI scope unchanged at orange | High |
| 3 | Section 3.5 | Shamsujjoha: gap absent from entire taxonomy | High |
| 4 | Section 3.5 | Shamsujjoha: context = static, not dynamic | High |
| 5 | Table 1 | Flehmig entry: add red-level detail | High |
| 6 | Table 1 | Add Shamsujjoha note | Medium |
| 7 | Section 4 | Use Shamsujjoha confirmation in conclusion | Medium |

---

## 8. FINAL VERIFICATION STATUS

| **Source** | **Original Claim** | **Verification Status** |
|:---|:---|:---|
| Indykov et al. [5] | 206 papers, 16 tactics—no safety-state conditioned scope | ✅ Confirmed |
| Shamsujjoha et al. [6] | 32 studies, 13 actions, 14 quality attributes—no environmental-risk-based scope restriction | ✅ Confirmed and strengthened |
| Flehmig et al. [7] | 3-level traffic-light—intermediate changes supervisory behavior, not AI output | ✅ Confirmed (with nuance) |
| Attard-Frost & Lyons [22] | 610-topic governance mapping—no runtime state-conditioned advisory scope | ✅ Confirmed |

**Overall Assessment:** The gap identified in the paper is **confirmed and strengthened** by reading both primary sources. The recommended revisions improve precision without weakening the core argument.
