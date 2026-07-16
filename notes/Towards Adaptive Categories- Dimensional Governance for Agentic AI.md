# Literature Review Extraction (Reduced)
## Paper: Towards Adaptive Categories: Dimensional Governance for Agentic AI

---

## 1. Paper Identity

- **Full title:** Towards Adaptive Categories: Dimensional Governance for Agentic AI
- **Authors:** Zeynep Engin, David Hand
- **Affiliations:** The Digital Statecraft Academy (UK); University College London; Imperial College London
- **Year:** 2025
- **Venue:** arXiv:2505.11579 (v3) — commentary format; acknowledgements indicate peer review (apparently for *Data & Policy*)
- **Type:** Conceptual/policy framework paper — no empirical data, no formal model, no implementation
- **Extraction category:** External evidence (governance-theory alignment — not a runtime architecture comparator)

---

## 2. Core Contribution

- **Argument:** Static categorical governance frameworks — fixed risk tiers (EU AI Act style), autonomy levels, human-in/out-of-the-loop distinctions — are increasingly insufficient for dynamic, agentic AI. Categories were designed to police boundaries that foundation models and multi-agent systems now blur.
- **Proposal — dimensional governance:** track how **decision authority**, **process autonomy**, and **accountability** ("the 3As") distribute dynamically across human-AI relationships. Categories are retained but repositioned as **context-sensitive designations built on continuous dimensions**: measure systems along dimensions, set evidence-based thresholds that define the categories and their regulatory requirements, adjust thresholds as evidence accumulates while the dimensional framework stays stable.
- **Key mechanism claim:** the approach can *"explicitly monitor system movement toward and across key governance thresholds, enabling pre-emptive adjustments before risks materialise."*
- **Analogies:** BMI thresholds over height/weight; credit-scoring thresholds adjusted to economic conditions; psychiatric diagnostic thresholds — categories atop dimensions, with deliberate threshold adjustment.

**Key quote (Abstract):** *"traditional categorical governance frameworks—based on fixed risk tiers, levels of autonomy, or human oversight models—are increasingly insufficient on their own... we make the case for dimensional governance: a framework that tracks how decision authority, process autonomy, and accountability (the 3As) distribute dynamically across human-AI relationships."*

---

## 3. Relevance to My Research

Governance theme, at the **conceptual/policy layer**. The paper supplies the theoretical vocabulary for exactly the structural move the proposed architecture makes: governance categories defined as thresholds over continuously measured dimensions, with graduated responses as systems move across thresholds. S = f(E) is architecturally this pattern — continuous environmental observation E, thresholded into three actionable categories (SAFE/CAUTION/UNSAFE) that carry differentiated governance requirements (G(S), A_AI(S)) — implemented as an enforced runtime mechanism rather than a regulatory process.

**Extraction decision:** Reduced extraction, external evidence.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- Conceptual validation from the governance-theory literature that **static categorical frameworks are insufficient for dynamic conditions** and that the principled alternative is **categories built on continuously monitored dimensions with explicit thresholds** — precisely the design pattern of S = f(E) and the graduated governance pair. The proposed architecture can be positioned as a concrete, formally enforced, domain-level instantiation of the dimensional-governance idea.
- The threshold-crossing insight: monitoring movement *toward* thresholds enables pre-emptive adjustment — the runtime analogue in the architecture is the treatment of state transitions at classification boundaries (dual-threshold hysteresis).
- A sharpening observation for the gap argument: even this most adaptive strand of governance thinking centres its dimensions on properties of the AI system and the human-AI relationship (authority, autonomy, accountability) — consistent with the review's finding that contemporary frameworks condition governance on AI-internal variables. None of the 3As is the operator's physical environment.

**What this paper CANNOT be cited for (overreach guard):**

- It is a **policy commentary with no formal model, no architecture, and no enforcement mechanism** — do not cite it as an architectural precedent or comparator, and do not claim it "proposes" state-conditioned advisory scope restriction. It has no advisory scope concept.
- Its dimensions (3As) are **not environmental state**: decision authority, process autonomy, and accountability are properties of the human-AI relationship. The mapping from their framework to S = f(E) is *our* structural analogy — cite the alignment of governance philosophy, not equivalence.
- Its thresholds are adjusted through **regulatory/evidence-based processes over time**, not computed at runtime; the architecture's runtime classification is a different operational register.
- arXiv version; verify the *Data & Policy* publication details before citing in a submitted manuscript.

---

## 5. Positioning for This Research

**Positioning paragraph:** Engin and Hand (2025) argue from the governance-theory literature that static categorical frameworks — fixed risk tiers, autonomy levels, oversight models — are increasingly insufficient for dynamic AI systems, and propose dimensional governance: categories repositioned as explicit thresholds over continuously monitored dimensions, adjusted as conditions evolve, with system movement toward thresholds monitored to enable pre-emptive response. The proposed architecture instantiates this design philosophy at the runtime-architecture level: continuous environmental observation E is thresholded by a deterministic classifier S = f(E) into three actionable governance categories, each carrying formally differentiated requirements through the governance pair (G(S), A_AI(S)). Two distinctions preserve the architecture's novelty claim: Engin and Hand's dimensions (decision authority, process autonomy, accountability) are properties of the human-AI relationship rather than of the operator's physical environment — consistent with this review's finding that even adaptive governance thinking conditions on AI-internal variables — and their framework is a regulatory process rather than an enforced runtime mechanism. The architecture supplies what the dimensional-governance proposal explicitly lacks: a formally specified, by-construction enforcement of category-conditioned constraints on AI advisory output.

---

## 6. Overall Relevance Score

### ⭐⭐ Low–Medium (external evidence)

**Justification:** No architecture, formalism, or empirical content, but valuable as governance-theory legitimation: it shows the policy literature independently converging on graduated, threshold-based, dimension-grounded governance — the design philosophy the architecture implements and formally enforces. Cite in the motivation or discussion when positioning graduated governance against static binary/tiered approaches, and optionally in the gap synthesis for the observation that even adaptive governance theory centres on AI-internal dimensions rather than environmental state. Not a comparator for Table 1 (it has no intermediate mode, no enforcement, no advisory scope).
