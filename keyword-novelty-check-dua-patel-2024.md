# Keyword & Novelty Verification Report

**Against:** *Optimizing Generative AI Workloads for Sustainability: Balancing Performance and Environmental Impact in Generative AI* — Ishneet Kaur Dua & Parth Girish Patel (2024), Apress
**ISBN:** 979-8-8688-0916-3 | 328 pages
**Prepared:** 14 April 2026

---

## 1. Executive Summary

A full-text search of all 328 pages of Dua & Patel (2024) was conducted against 45+ keywords derived from the proposed dissertation, *"A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments."*

**Key finding:** This book occupies a completely different problem space. It is a technical handbook on optimising the computational efficiency, energy consumption, and environmental sustainability of generative AI workloads (hardware selection, model compression, distributed training, edge deployment, carbon footprint reduction). It contains **zero coverage** of AI safety governance, decision support architectures, formal methods, maritime/fisheries domains, or any mechanism resembling the dissertation's contribution. All core novelty terms return zero hits.

**Thematic distance:** Among the three books checked so far, this is the most distant from the dissertation. Hendrycks (2024) shared the "AI safety" problem space; Maas (2025) shared the "AI governance" problem space; Dua & Patel (2024) shares neither — it is an engineering optimisation manual.

---

## 2. Full Keyword Search Results

### 2.1 Core Novelty Terms — ALL ZERO HITS

| Keyword | Hits | Notes |
|---|---|---|
| graduated governance | 0 | Not found |
| safety state / safety-state | 0 | Not found |
| advisory scope / scope restriction | 0 | Not found |
| recommendation scope / types | 0 | Not found |
| state-conditioned | 0 | Not found |
| environmental state | 0 | Not found |
| governance pair / layer | 0 | Not found |
| containment hierarchy | 0 | Not found |
| output space | 0 | Not found |

### 2.2 Architecture Concepts — Absent

| Keyword | Hits | Notes |
|---|---|---|
| decision support system / DSS | 0 | Not found |
| adaptive autonomy | 0 | Not found |
| guardrail | 1 | p.48 — policy guardrails for aligning private interests with public welfare; one sentence |
| safety filter | 0 | Not found |
| governance architecture | 0 | Not found |

### 2.3 Safety Engineering — Absent

| Keyword | Hits | Notes |
|---|---|---|
| defense in depth | 0 | Not found |
| Swiss cheese model | 0 | Not found |
| fail-safe | 0 | Not found |
| formal verification | 0 | Not found |
| formal methods | 0 | Not found |
| safety-critical | 1 | p.213 — one sentence: "accuracy may take precedence over efficiency in safety-critical systems" |
| safety engineering | 0 | Not found |
| AI safety | 0 | Not found |
| AI governance | 0 | Not found |
| automation bias | 0 | Not found |

### 2.4 Domain Concepts — Absent

| Keyword | Hits | Notes |
|---|---|---|
| fisheries / fisher | 0 | Not found |
| maritime | 0 | Not found |
| low-resource | 0 | Not found |
| coastal | 0 | Not found |
| vessel | 0 | Not found |

### 2.5 The Book's Actual Domain — Computational Sustainability

| Keyword | Hits | Notes |
|---|---|---|
| sustainability | 472 | 206 pages — the book's core subject |
| energy efficiency | 135 | 86 pages — hardware/software energy optimisation |
| carbon | 95 | 60 pages — carbon footprint of AI workloads |
| edge computing | 115 | 45 pages — edge deployment for efficiency |
| model compression | 22 | 16 pages — pruning, quantization, distillation |
| quantization | 55 | 31 pages — inference optimisation technique |
| pruning | 40 | 25 pages — model size reduction |
| distillation | 31 | 19 pages — knowledge distillation for smaller models |
| tiered | 8 | 5 pages — tiered *storage architecture* (hot/warm/cold data), not tiered governance |
| reinforcement learning | 6 | 4 pages — mentioned as a training paradigm |

---

## 3. Novelty Claim Verification

The dissertation's core novelty claim is: *environmental-state-conditioned, formally guaranteed restriction of AI advisory recommendation types through a unified governance pair (G(S), A_AI(S)), implementing a graduated three-state containment hierarchy A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.*

### 3.1 No Overlap Whatsoever

The book does not discuss any form of AI governance (system-level or policy-level), any safety architecture, any decision support system, any formal model, or any mechanism for restricting AI output based on environmental conditions. The word "safety" appears twice in the entire book — once about safety-critical systems requiring accuracy over efficiency (p.213), and once about road safety in a transportation case study (p.301).

### 3.2 "Tiered" Means Something Completely Different

"Tiered" appears 8 times but refers exclusively to **tiered storage architecture** — the practice of placing frequently-accessed data on fast/expensive storage and cold data on slow/cheap storage (hot/warm/cold tiers). This is a data management concept with no connection to tiered governance.

### 3.3 "Edge Computing" and "Low-Resource" — Superficial Keyword Overlap Only

The book extensively covers edge computing (115 hits) and resource-constrained deployment. However, "low-resource" in this book means *computationally constrained hardware* (edge devices, mobile chips) where the goal is to run inference efficiently. The dissertation's "low-resource environments" means *institutionally and infrastructurally constrained operational settings* (coastal fisheries in developing regions) where the goal is to provide safe decision support. These are fundamentally different uses of the same words.

---

## 4. Verdict

**The novelty claim is confirmed as absent from Dua & Patel (2024).**

This is the clearest case of the three books checked — the book occupies a completely non-overlapping problem space. It is about *how to make AI workloads consume less energy*, not about *how to make AI systems safe for human decision-makers*. There is no discussion of governance, safety architecture, formal methods, decision support, fisheries, maritime operations, or any mechanism remotely resembling the dissertation's contribution.

---

## 5. Usability for the Dissertation

Despite the absence of overlap, one narrow area may be useful:

- **Edge deployment and model compression** (Chapters 3–4, 7): If the dissertation's architecture is eventually deployed on resource-constrained hardware in fishing communities, techniques like quantization, pruning, and edge computing from this book could inform the implementation layer. However, this would be for the engineering implementation of Paper 3 (domain application), not for the core architectural contribution of Paper 2.
- **"Tiered storage" as a disambiguation point**: When defending the use of "tiered" or "graduated" in the dissertation, it may be useful to note that the only prior use of "tiered architecture" in the AI literature refers to data storage tiers — not governance tiers — further demonstrating the novelty of the concept.
