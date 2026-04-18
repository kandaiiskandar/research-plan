# Keyword & Novelty Verification Report

**Against:** *Architectures of Global AI Governance: From Technological Change to Human Choice* — Matthijs M. Maas (2025), Oxford University Press
**ISBN:** 978-0-19-887783-7 | 646 pages
**Prepared:** 14 April 2026

---

## 1. Executive Summary

A full-text search of all 646 pages of Maas (2025) was conducted against 50+ keywords derived from the proposed dissertation, *"A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments."*

**Key finding:** Every term that defines the core novelty claim — graduated governance, safety state classification, advisory scope restriction, state-conditioned governance, environmental state classification, the (G(S), A_AI(S)) governance pair — returns **zero hits** in the book.

**Critical disambiguation:** Despite having "Architectures" and "Governance" in its title, this book operates at a completely different level of abstraction. Maas uses "governance architecture" (125 hits) to mean the *global institutional landscape* — the web of international treaties, organisations, norms, and regulatory frameworks that collectively govern AI. The dissertation uses "governance architecture" to mean a *system-level computational mechanism* — a runtime function that restricts an AI's output space based on classified environmental state. These are entirely non-overlapping meanings. The book is about how *nations and institutions* govern AI; the dissertation is about how an *AI system governs itself* under environmental conditions.

---

## 2. Full Keyword Search Results

### 2.1 Core Novelty Terms — ALL ZERO HITS

| Keyword | Hits | Notes |
|---|---|---|
| graduated governance | 0 | Not found anywhere in the book |
| safety state / safety-state | 0 | Not found anywhere in the book |
| advisory scope / scope restriction | 0 | Not found anywhere in the book |
| recommendation scope / types | 0 | Not found anywhere in the book |
| state-conditioned | 0 | Not found anywhere in the book |
| environmental state classification | 0 | Not found anywhere in the book |
| environmental state | 0 | Not found (even as a general phrase) |
| governance pair / governance layer | 0 | Not found anywhere in the book |
| containment hierarchy | 0 | Not found anywhere in the book |
| output space | 0 | Not found anywhere in the book |
| admissible action | 0 | Not found anywhere in the book |
| A_AI(S) / G(S) | 0 | Not found anywhere in the book |

### 2.2 Architecture Concepts

| Keyword | Hits | Notes |
|---|---|---|
| governance architecture | 125 | **Means global institutional landscape** (treaties, orgs, norms) — not system-level computational architecture |
| decision support system / DSS | 5 | pp.153, 437, 638 — military DSS mentioned in passing; no architectural treatment |
| adaptive autonomy | 0 | Not found |
| guardrail(s) | 6 | pp.173, 176, 299 — LLM behavioural controls (jailbreaking), US–China diplomatic guardrails; no architectural taxonomy |
| safety filter | 2 | p.117 — adversarial prompt bypass of safety filters; no formal treatment |
| layered architecture | 0 | Not found (in system design sense) |
| two-level governance | 0 | Not found |

### 2.3 Safety Engineering — Barely Present

| Keyword | Hits | Notes |
|---|---|---|
| defense/defence in depth | 0 | Not found |
| Swiss cheese model | 0 | Not found |
| fail-safe | 0 | Not found |
| safety engineering | 4 | pp.371, 383, 532 — mentioned as a bullet point in a governance-rationale table; no substantive treatment |
| formal verification | 2 | pp.371, 383 — listed as one item in a taxonomy table alongside other approaches; no elaboration |
| formal methods | 0 | Not found |
| safety-critical | 0 | Not found |

### 2.4 Domain Concepts — Absent

| Keyword | Hits | Notes |
|---|---|---|
| fisheries / fisher | 3 | pp.10, 475 — author acknowledgement name (Richard Fisher); fisheries monitoring mentioned once as an example of environmental law AI application |
| maritime | 32 | 17 pages — IMO references; Maritime Autonomous Vehicles (MAV) abbreviation; international maritime transport emissions. No fisheries DSS or coastal safety. |
| vessel | 5 | pp.420, 473, 475 — Chinese military vessel incident; vessel monitoring systems for IUU fishing (one sentence). No small-vessel safety architecture. |
| low-resource | 0 | Not found |
| small-scale | 0 | Not found |
| coastal | 0 | Not found |

### 2.5 Broader AI Governance Concepts

| Keyword | Hits | Notes |
|---|---|---|
| AI governance | 799 | Throughout — this is the book's subject, but at international/institutional level |
| AI safety | 166 | 73 pages — AI Safety Institutes, safety research policy; not system-level safety mechanisms |
| automation bias | 10 | pp.371, 380, 383, 463, 532 — substantively discussed as a factor in normal accidents and overtrust; useful supporting reference |
| human-in-the-loop | 2 | pp.154, 635 — nuclear weapons context; brief mention |
| tiered | 5 | pp.79, 139, 157, 224, 327 — risk-based tiered approach to *regulating* AI (EU AI Act); not tiered system-level governance |
| reinforcement learning | 26 | 17 pages — RL as ML technique; safety challenges of RL agents |
| autonomous weapons | 133 | 62 pages — major topic (LAWS, CCW negotiations); military governance, not civilian safety architecture |
| regime complexity | 507 | Major analytical framework of the book |
| sociotechnical | 399 | Core lens of the book |

---

## 3. Novelty Claim Verification

The dissertation's core novelty claim is: *environmental-state-conditioned, formally guaranteed restriction of AI advisory recommendation types through a unified governance pair (G(S), A_AI(S)), implementing a graduated three-state containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.*

### 3.1 "Governance Architecture" — Different Meaning Entirely

This is the most important finding. Maas uses "governance architecture" 125 times across 101 pages, but it consistently means the *global institutional architecture* — the web of treaties, organisations, norms, standards bodies, and regulatory frameworks that collectively form the governance landscape for AI. Examples: "how to instead organize the global governance architecture for AI" (p.38); "the trends, trajectories, and changes in the global governance architecture" (p.58); "AI as Persistent Threat to Governance Architectures" (p.484, meaning threats to international legal regimes). The dissertation's "governance architecture" means a computational mechanism within a single AI system. There is no overlap in meaning.

### 3.2 Safety Risks Section (§4.6.2.3, pp. 378–384)

The book's most relevant section discusses AI safety as a *governance rationale* — why safety risks justify regulatory intervention. It covers opacity, normal accidents, value misalignment, alignment challenges, and principal–agent problems. But the treatment is about *why* governance is needed, not *how* to implement it at the system level. There is no discussion of safety state classification, advisory scope restriction, or any runtime governance mechanism. The closest concept is "fail-safes instil further automation bias, as operators may trust safety systems overmuch" (p.380) — which actually *supports* the dissertation's argument for scope restriction over binary shutdown.

### 3.3 "Tiered" Approach — Different Level

"Tiered" appears 5 times, always referring to **risk-based tiered regulation** at the policy level — specifically the EU AI Act's approach to categorising AI applications by risk tier (unacceptable, high, limited, minimal) to determine regulatory burden. This is tiered *regulation of AI products*, not tiered *governance within an AI system*. The former determines which AI products require what regulatory compliance; the latter determines what an individual AI system may output under varying environmental conditions.

### 3.4 Automation Bias (pp. 371, 380, 383, 463, 532)

This is the book's most substantively relevant content to the dissertation. Maas discusses automation bias in the context of "normal accidents" — operators over-trusting AI systems, which undermines the effectiveness of human-in-the-loop safeguards. On p.380: "fail-safes instil further automation bias, as operators may trust safety systems overmuch, resulting in risk homeostasis and creating new avenues for error." This directly supports the dissertation's argument that binary governance (AI ON or AI OFF) is insufficient, and that scope restriction (reducing what the AI recommends rather than removing it entirely) is a more appropriate response to degraded conditions.

### 3.5 Domain Coverage

The book mentions maritime contexts 32 times but exclusively in the context of international organisations (IMO), autonomous vessels in military contexts, or transport emissions. Vessel monitoring systems for illegal fishing are mentioned once (p.475) as an example of AI-enhanced environmental monitoring. There is no discussion of fisheries decision support, coastal safety, low-resource deployment, or small-vessel operations.

---

## 4. Verdict

**The novelty claim is confirmed as absent from Maas (2025).**

Specifically, the book does not contain:

- Any concept of system-level governance architecture (all "governance architecture" references mean the global institutional landscape)
- Any state-conditioned or graduated runtime governance mechanism
- Any concept of restricting AI advisory scope based on environmental classification
- Any formal model, mathematical formalisation, or formal governance pair
- Any treatment of safety engineering principles as system design mechanisms (safety engineering is mentioned only as a governance-rationale bullet point)
- Any discussion of fisheries DSS, coastal safety, low-resource deployment, or small-vessel safety as application domains

The book is an excellent, comprehensive treatment of global AI governance at the international law and policy level. It analyses how nations, institutions, and regulatory frameworks should govern AI development and deployment. But it operates at a fundamentally different level of abstraction from the dissertation. The dissertation's contribution — a formalised, runtime, system-level computational mechanism that restricts AI output scope based on environmental state — is not within the book's scope, and no mechanism described in the book approaches this contribution.

---

## 5. Usability for the Dissertation

Although the book does not threaten the novelty claim, it is a potentially valuable reference for:

- **Sociotechnical framing** (Ch. 4): The sociotechnical change lens supports the argument that AI safety governance must consider the interaction between technical systems and social contexts — including fisher decision-making practices
- **Automation bias** (pp. 380, 383, 463): Substantive discussion of how human overtrust of AI creates "normal accident" dynamics — directly supports the argument for scope restriction over binary shutdown
- **Safety risks taxonomy** (§4.6.2.3): The classification of AI failure modes (opacity, environmental interactions, normal accidents, value misalignment) provides vocabulary for situating the dissertation's safety state classification
- **Governance rationales** (Table 4.2, pp. 371, 383): The mapping of safety challenges to governance logics could support the argument that different safety states warrant different governance responses
- **Tiered regulatory precedent** (pp. 79, 139, 224): The EU AI Act's risk-based tiered approach, while operating at the policy level, provides a normative precedent for the principle of graduated (rather than binary) governance — applicable by analogy to system-level architecture
- **Regime complexity** (Ch. 6–7): The argument that effective governance requires multiple complementary mechanisms operating at different levels supports the dissertation's layered architecture design
