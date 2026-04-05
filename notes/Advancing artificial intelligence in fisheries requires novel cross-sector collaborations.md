# Literature Review Extraction: Wing & Woodward (2024)

## 1. Paper Identity

- **Title:** Advancing artificial intelligence in fisheries requires novel cross-sector collaborations
- **Authors:** Kate Wing, Benjamin Woodward
- **Year:** 2024
- **Venue:** ICES Journal of Marine Science, Vol. 81, Issue 10, pp. 1912–1919
- **DOI:** https://doi.org/10.1093/icesjms/fsae118
- **Type:** Perspective / Opinion piece ("Food for Thought")

---

## 2. Core Contribution

- **Problem addressed:** Fisheries AI innovation and adoption — particularly for electronic monitoring (EM) — faces substantial barriers from fragmented data access, complex regulatory environments, unequal AI capacity across fishing nations, and lack of shared vocabulary between technical and fisheries communities.
- **Proposed solution:** Four cross-sector recommendations: (1) regular cross-sector dialogues for shared AI/fisheries terminology; (2) model contract and data-use agreement libraries for fisheries AI procurement; (3) shared data platforms and development environments to pool training data safely; (4) integration of general AI/data policy lessons (e.g. EU AI Act, GDPR) into fisheries governance.
- **Main contributions:** Identifies the systemic (non-technical) barriers to fisheries AI scaling; maps the stakeholder landscape (fishers, EM vendors, AI developers, governments); articulates how policy shapes the AI marketplace in fisheries; proposes concrete collaboration structures.
- **Novelty:** The paper is not technically novel — it introduces no new model or system. Its value lies in synthesising policy, market, and data-access barriers into a coherent call for cross-sector action, grounded in direct experience with fisheries EM deployment.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Not discussed. No architectural or hybrid design content. |
| Safety-critical AI decision-making | No | EM is framed as a monitoring/compliance tool, not a safety-critical decision support system. No discussion of safety-state classification or risk-gated decisions. |
| AI governance / control mechanisms | Partial | Discusses regulatory governance of AI systems (EU AI Act high-risk classification, human-in-the-loop requirements, algorithmic transparency standards) — but this is *policy-level* governance, not *architectural* governance of AI participation or output scope. |
| Low-resource environments | Partial | Highlights data-poor fisheries (80% of world's fisheries unassessed), unequal AI readiness across fishing nations, and resource constraints (bandwidth, annotation capacity, compute access) — relevant as domain-level evidence of the low-resource challenge. |
| Decision architecture formalisation | No | No formal model, no mathematical representation, no architecture specification. |
| Human role in decision-making | Partial | Notes that human-in-the-loop EM review may receive different regulatory treatment than fully automated systems; discusses human reviewers checking AI-flagged footage. However, this is about monitoring review, not decision support for operational safety. |
| Socio-technical evaluation | Partial | Discusses stakeholder trust, fisher privacy concerns, adoption barriers, and the socio-political dynamics of data ownership — relevant socio-technical framing, though not in the context of evaluating a decision support system. |
| Coastal fisheries / maritime domain | Yes | Core domain. Covers global fisheries EM landscape, small-scale fisheries, data challenges specific to fishing vessels, and the regulatory environment governing fisheries AI deployment. |

**Mid-Extraction Relevance Gate:** 1 Yes + 3 Partial → **REDUCED EXTRACTION** (Sections 4–7 and 12–13 only; Sections 8–11 and 14–15 skipped).

---

## 4. Decision Architecture Analysis

- **Architecture:** The paper does not describe or propose any decision architecture. It discusses AI-supported EM as a data processing pipeline (video capture → transmission → AI flagging → human review) but does not formalise this as an architecture.
- **Layered architecture / governance structure:** None at the system design level. The paper discusses *regulatory* governance layers (EU AI Act risk classification, human-in-the-loop requirements) but not architectural layers controlling AI participation or output.
- **Rule-based constraints before AI:** Not discussed. The paper mentions that government specifications can constrain hardware and software configurations, but this is procurement-level, not runtime safety constraint.
- **Boundary between deterministic control and AI reasoning:** Not defined or addressed.
- **Failure modes / fallback behaviour:** Not discussed. The paper notes that AI models may not perform well on data outside their training distribution, but does not describe any fallback or degradation mechanism.

**Summary:** No decision architecture is present. The paper operates at the ecosystem/policy level, not the system design level.

---

## 5. Formal Model and Mathematical Representation

- **Formal model:** None. The paper contains no formal definitions, mathematical notation, state variables, or decision functions.
- **Comparison to E → S = f(E) → (G(S), A_AI(S)) → AI(E):** Not applicable — no comparable formal structure exists in this paper.
- **State-dependent recommendation restriction:** Not modelled or discussed.
- **Safety Dominance Property:** Not defined or referenced.
- **Formalisation purpose:** N/A.

---

## 6. Safety State Classification

- **Discrete risk/safety levels:** None. The paper does not classify operational or environmental conditions into safety states.
- **Comparison to S = f(E) → {SAFE, CAUTION, UNSAFE}:** Not applicable. The paper discusses AI system risk classification under the EU AI Act (high-risk vs. other), but this is a *regulatory* risk category applied to the AI system itself, not a runtime safety state classification of the operating environment.
- **AI recommendation scope differentiation across safety levels:** Not present. The paper notes that human-in-the-loop systems may be treated differently from fully automated systems under regulation, but this is a static design choice, not a dynamic state-conditioned governance mechanism.

---

## 7. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | Not addressed architecturally. The paper discusses whether AI *should be deployed* in fisheries (a policy/adoption question), not whether AI is dynamically permitted or blocked based on environmental state. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | Not addressed. No discussion of restricting AI output types based on conditions. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not applicable. |

- **Governance type:** The paper discusses *regulatory* governance (EU AI Act, GDPR, algorithmic transparency) and *organisational* governance (data ownership, procurement rules, cross-sector coordination) — neither of which correspond to the runtime architectural governance modelled by (G(S), A_AI(S)).
- **Binary switch vs. graduated model:** Neither — governance here is about market/regulatory conditions for AI deployment, not runtime AI control.
- **Support or contradiction of two-level governance pair:** Neither supports nor contradicts. The paper operates at a different level of abstraction (policy ecosystem vs. system architecture).

---

## 12. Key Concepts and Definitions

| Term / Concept | Definition / Relevance |
|---|---|
| **Electronic monitoring (EM)** | On-vessel video camera and sensor systems recording catch; the primary fisheries monitoring technology context for AI deployment. |
| **Human-in-the-loop EM** | EM system where human reviewers check AI-flagged footage before compliance decisions are made; noted as potentially receiving different regulatory treatment under the EU AI Act. |
| **AI auditability** | The capability of an AI system to be examined and assessed by external or internal teams — distinguished from general "transparency." |
| **Data-poor fisheries** | Fisheries targeting populations that are unassessed or data-limited; estimated at ~80% of world fisheries. Relevant as evidence of the low-resource context. |
| **AI readiness gap** | Unequal distribution of AI development capacity and training data across fishing nations — major producers like Indonesia and Peru score much lower on AI readiness indices than the USA or China. |
| **Regulatory lock-in** | When pilot program specifications from a single EM vendor become codified into program requirements, disadvantaging other providers. |
| **Data intermediaries** | Shared platforms (modelled on biomedical examples like Terra.bio) that allow controlled, permissioned access to pooled training data without direct data ownership transfer. |

---

## 13. Limitations and Unsolved Problems

- **Stated limitations:** The paper is a perspective piece, not a technical study — it identifies problems and proposes directions but does not implement, test, or evaluate any solution. The recommendations are high-level and depend on multi-stakeholder coordination with no clear enforcement mechanism.
- **Unsolved problems acknowledged:**
  - No scalable mechanism yet exists for pooling fisheries training data across governments, fisheries, and vessel types.
  - Regulatory frameworks (EU AI Act, GDPR) have not yet been interpreted or applied specifically to fisheries EM; intersection with fisheries data-as-MCS policy is unclear.
  - AI performance on out-of-distribution fisheries data (different species, gears, conditions) remains a barrier.
  - Small-scale fisheries in low-resource nations lack AI readiness and infrastructure.
- **Gaps aligning with my research:**
  - The paper identifies the low-resource fisheries AI deployment challenge but proposes no architectural solution for operating under resource constraints — my architecture directly addresses this.
  - The paper discusses human-in-the-loop as a binary design choice (fully automated vs. human review) but does not consider *graduated* AI participation based on environmental conditions — the exact gap my CAUTION mode fills.
  - No formal model of AI governance is presented — governance is discussed only at the policy/regulatory level, not at the system architecture level where my (G(S), A_AI(S)) pair operates.

---

## 16. Relation to My Research and Positioning

- **Governance level implemented:** Neither Level 1 nor Level 2 in the architectural sense. The paper discusses policy-level governance (regulation, procurement, data access) rather than runtime governance of AI participation or output scope.
- **State-conditioned governance:** Not applicable.
- **Proximity to (G(S), A_AI(S)):** Distant. The paper operates at an entirely different level of abstraction — the fisheries AI ecosystem rather than the AI decision system architecture.
- **Safety Dominance Property:** Not defined or comparable.
- **Gap my research addresses:** The paper documents the fisheries domain context — data scarcity, regulatory complexity, stakeholder dynamics, low-resource deployment challenges — but offers no architectural response. My research fills this by providing a formal, safety-gated architecture designed specifically for this kind of constrained operating environment.

**Positioning paragraph:** Wing & Woodward (2024) provides **domain background and deployment context** for my research. It documents the real-world fisheries AI landscape — the stakeholder ecosystem, data access barriers, regulatory constraints, and the unequal distribution of AI capacity across fishing nations — that motivates my architecture's focus on low-resource environments. The paper's discussion of human-in-the-loop EM as a binary design choice (fully automated vs. human review) indirectly reinforces the gap my CAUTION mode addresses: no existing fisheries AI framework considers graduated AI participation conditioned on environmental safety state. The paper does not engage with system architecture, formalisation, or safety-state classification, so it occupies the outermost ring of my literature review — useful for setting the scene in the fisheries domain chapter but not for the architectural or governance contribution analysis.

---

## 17. Overall Relevance Score

### ⭐⭐ Low

**Justification:** The paper is a policy/ecosystem perspective piece with no architectural, formal, or governance-mechanism content relevant to the core contribution of my research. Its value is limited to domain background: documenting the fisheries AI deployment landscape, data constraints, and regulatory context that motivate the low-resource focus of my architecture. It does not address safety-critical decision-making, safety-state classification, hybrid AI design, or any form of runtime AI governance — the central themes of my dissertation. Useful for a brief citation in the domain motivation section; not citable in the architecture, formalisation, or governance chapters.
