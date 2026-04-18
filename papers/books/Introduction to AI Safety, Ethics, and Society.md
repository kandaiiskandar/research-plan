# Keyword & Novelty Verification Report

**Against:** *Introduction to AI Safety, Ethics, and Society* — Dan Hendrycks (2024), CRC Press / Taylor & Francis
**ISBN:** 978-1-040-26116-3 | 562 pages
**Prepared:** 14 April 2026

---

## 1. Executive Summary

A full-text search of all 562 pages of Hendrycks (2024) was conducted against 35+ keywords derived from the proposed dissertation, *"A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments."*

**Key finding:** Every term that defines the core novelty claim — graduated governance, safety state classification, advisory scope restriction, state-conditioned governance, environmental state classification, the (G(S), A_AI(S)) governance pair — returns **zero hits** in the book. The architectural contribution is entirely absent from Hendrycks' treatment.

The book does cover related safety engineering principles (defense in depth, Swiss cheese model, fail-safes) and AI governance at the policy level (Chapter 8), but these operate at a fundamentally different level of abstraction. Hendrycks discusses *societal-scale AI risk governance* (policy, regulation, international agreements), not *system-level architectural governance* (runtime state-conditioned restriction of AI output scope). The gap between what this book covers and what the dissertation proposes is precisely the gap the research fills.

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
| governance pair / governance layer | 0 | Not found anywhere in the book |
| governance architecture | 0 | Not found anywhere in the book |
| A_AI(S) / G(S) | 0 | Not found anywhere in the book |

### 2.2 Architecture Concepts — Mostly Absent

| Keyword | Hits | Notes |
|---|---|---|
| decision support system | 1 | p.360 — brief mention in social welfare context, not as architecture class |
| adaptive autonomy | 0 | Not found |
| guardrail(s) | 4 | pp.166, 303, 493 — used informally (LLM jailbreaking, ethics); no architectural taxonomy |
| safety filter | 1 | p.28 — GPT-4 safety filters bypassed; no formal treatment |
| formal verification / formal methods | 0 | Not found anywhere in the book |
| neuro-symbolic / hybrid AI | 0 | Not found anywhere in the book |
| operational design domain | 0 | Not found anywhere in the book |
| shield(s) (RL safety sense) | 0 | Not found |

### 2.3 Safety Engineering — Present but General

| Keyword | Hits | Notes |
|---|---|---|
| defense in depth | 12 | pp.208–213 — general principle (multiple layers); no state-conditioned variant |
| Swiss cheese model | 15 | pp.213–218 — component-failure accident model; no runtime governance |
| fail-safe(s) | 12 | pp.209–210 — binary shutdown concept; no graduated intermediate mode |
| safety-critical | 4 | pp.33, 51, 93, 320 — general mentions (military, aviation); no domain-specific architecture |

### 2.4 Domain Concepts — Absent

| Keyword | Hits | Notes |
|---|---|---|
| fisheries / fisher | 2 | pp.386, 453 — fishery depletion (game theory); Fisher's theorem (evolution). Not fisheries DSS. |
| maritime | 1 | p.503 — IMO mentioned in international governance context only |
| low-resource | 0 | Not found |
| coastal | 0 | Not found |
| small vessel | 0 | Not found |

### 2.5 Broader AI Governance — Different Abstraction Level

| Keyword | Hits | Notes |
|---|---|---|
| AI governance | 17 | pp.465–513 — Chapter 8: policy-level (corporate, national, international); no system-level architecture |
| automation bias | 1 | p.322 — brief mention in fairness context |
| human-in-the-loop | 3 | pp.79, 141 — general concept; no formal treatment of authority vs scope |
| reinforcement learning | 40 | Extensive coverage as ML technique; no safety-state governance for RL agents |

---

## 3. Novelty Claim Verification

The dissertation's core novelty claim is: *environmental-state-conditioned, formally guaranteed restriction of AI advisory recommendation types through a unified governance pair (G(S), A_AI(S)), implementing a graduated three-state containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.*

This claim was checked against every mechanism described in the book.

### 3.1 Defense in Depth (pp. 208–213)

Hendrycks presents defense in depth as a general design principle: use multiple independent layers of defense. The treatment is illustrative (virus prevention analogy, Titanic lifeboats) and does not formalise the principle. There is **no concept of state-conditioned governance** — the layers are static, not graduated based on environmental classification. The closest the book comes is the Swiss cheese model (each layer has "holes"), but this is a failure-analysis model, not a runtime governance mechanism.

### 3.2 Fail-Safes (pp. 209–210)

The book describes fail-safes as binary shutdown mechanisms: a kill switch, or a confidence monitor that "stops enacting decisions if this component falls below a critical level." This is exactly the **binary governance** paradigm (ON/OFF) that the dissertation identifies as the gap. There is no intermediate CAUTION mode where the AI continues to participate under restricted scope. The book's fail-safe is: AI works, or AI stops. The dissertation's contribution is the third state: AI works with restricted recommendation types.

### 3.3 Guardrails (pp. 166, 303, 493)

The term "guardrails" appears four times, always informally: LLM jailbreaking bypass (p.166), ethics as insufficient guardrails for AI behaviour (p.303), and defensive cybersecurity measures (p.493). There is **no architectural taxonomy of guardrail mechanisms**, no discussion of per-output vs per-state governance, no distinction between content filtering and scope restriction, and no formal treatment whatsoever. The book uses "guardrails" as a colloquial metaphor, not as a technical architecture class.

### 3.4 AI Governance — Chapter 8 (pp. 465–513)

Chapter 8 covers AI governance extensively but at the **policy level**: corporate governance (legal structure, ownership), national governance (standards, regulations, liability, export controls), international governance (treaties, agreements), and compute governance. This is governance *of AI development and deployment* by human institutions. The dissertation's contribution operates at a completely different level: governance *within an AI system's architecture* — a runtime mechanism that restricts the AI's own output space based on environmental state. These two governance concepts are complementary, not overlapping.

### 3.5 Domain Coverage

The book contains no discussion of fisheries decision support, coastal/maritime safety systems, low-resource deployment environments, or small-vessel operations. The word "fisheries" appears once (p.386) in a game-theory context about common-pool resource depletion, and "maritime" appears once (p.503) referencing the IMO in an international governance list. The domain application space of the dissertation is entirely absent.

---

## 4. Verdict

**The novelty claim is confirmed as absent from Hendrycks (2024).**

Specifically, the book does not contain:

- Any concept of state-conditioned governance (restricting AI behaviour based on classified environmental state)
- Any graduated/three-state governance mechanism (the book's safety mechanisms are uniformly binary: ON/OFF, pass/block, safe/shutdown)
- Any concept of advisory scope restriction (restricting which *types* of recommendations an AI may generate, as distinct from filtering individual outputs)
- Any formal governance pair or layered governance architecture at the system level
- Any treatment of environmental state classification as a governance input (S = f(E))
- Any discussion of fisheries DSS, maritime decision support, low-resource AI deployment, or small-vessel safety
- Any formal methods, formal verification, or mathematical formalisation of safety governance

The book is a broad, high-quality introductory textbook on AI safety, ethics, and societal risk. It covers safety engineering principles, catastrophic AI risks, machine ethics, collective action problems, and policy-level governance. However, its treatment of safety mechanisms remains at the *principle level* (defense in depth, fail-safes, Swiss cheese) and its governance discussion operates at the *institutional/policy level* (corporate, national, international). The dissertation's contribution — a formalised, runtime, system-level governance architecture that dynamically restricts AI advisory scope based on classified environmental state — occupies a space the book does not enter.

---

## 5. Usability for the Dissertation

Although the book does not threaten the novelty claim, it may be a useful supporting reference for:

- Defense in depth as a general safety principle that motivates layered architectures (Chapter 4, §4.3.8)
- Swiss cheese model as a conceptual predecessor to multi-layer safety thinking (Chapter 4, §4.4.1)
- Fail-safe design as the binary paradigm your graduated architecture extends (Chapter 4, §4.3.4)
- Systemic safety and complex systems perspectives (Chapters 4–5) that support the argument for environmental-state-aware governance
- Policy-level AI governance (Chapter 8) as the institutional complement to system-level architectural governance
- Automation bias (p.322) as a brief supporting reference for why scope restriction matters
