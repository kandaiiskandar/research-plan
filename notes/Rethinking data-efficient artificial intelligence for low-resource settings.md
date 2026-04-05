## Literature Review Extraction: Katende (2026)

---

### 1. Paper Identity

- **Title:** Rethinking data-efficient artificial intelligence for low-resource settings
- **Authors:** Ronald Katende
- **Year:** 2025 (published online November 2025; journal volume dated 2026)
- **Venue:** Machine Learning with Applications, Vol. 23, 100796 (Elsevier, open access)
- **DOI:** 10.1016/j.mlwa.2025.100796
- **Type:** Structured mixed-methods review (PRISMA-inspired protocol, 300+ studies screened, 102 included in qualitative synthesis, 47 with quantitative data)

---

### 2. Core Contribution

- **Problem:** Mainstream AI/ML assumes data abundance and computational scale — assumptions that rarely hold in low-resource environments (LMICs). Structural constraints in data, compute, connectivity, and institutional capacity create a fundamentally different design space. Imported high-resource AI paradigms frequently underperform or fail in these settings.
- **Solution:** A comprehensive taxonomy and decision matrix mapping structural constraints (limited data, low compute, unreliable connectivity, domain heterogeneity, privacy concerns) to suitable data-efficient AI methods (PINNs, few-shot learning, self-supervised learning, TinyML, federated learning, LoRA/PEFT, active learning, knowledge distillation, etc.). Evaluated across seven operational axes: data requirement, compute footprint, inference latency, robustness to domain shift, interpretability, ease of maintenance, and deployment cost.
- **Main contributions:**
  - Structured taxonomy linking low-resource constraints to data-efficient algorithmic paradigms (Table 14)
  - Decision matrix for practitioners (Table 1) mapping constraints to method selection
  - Cross-domain empirical synthesis (health, agriculture, climate, education) with structural metrics (Tables 2–10)
  - Evidence-based argument that data-efficient AI is not a stopgap but a foundational paradigm for equitable AI
- **Novelty:** Integrates technical taxonomy with structural infrastructure metrics (electricity access, R&D intensity, farm size, observation density, school connectivity) to show that method selection must start from measured constraints, not assumed availability. Positions lean AI as first-best strategy rather than second-best adaptation.

---

### 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | Partial | Discusses physics-informed neural networks (PINNs) as hybrid physics–ML approaches that embed physical laws into learning architectures. However, "hybrid" here means physics priors + data-driven learning, not deterministic governance layer + probabilistic AI reasoning |
| Safety-critical AI decision-making | No | Not focused on safety-critical decision systems. Domains covered (health, agriculture, climate, education) involve consequential decisions but are not framed through safety-critical architecture or governance |
| AI governance / control mechanisms | No | "Governance" in this paper refers to data governance, institutional capacity, and policy frameworks — not runtime AI operational governance (G(S), A_AI(S)). No mechanism controlling AI participation or advisory scope |
| Low-resource environments | Yes | Core focus. Comprehensive characterisation of low-resource constraints: data scarcity, limited compute, unreliable connectivity, sparse observation networks, low R&D investment, limited institutional capacity. Quantified with structural metrics across Sub-Saharan Africa, South Asia, Latin America |
| Decision architecture formalisation | No | No formal decision architecture. The decision matrix (Table 1) maps constraints to methods but is a practitioner guide, not a formalised pipeline with state variables, gate functions, or safety properties |
| Human role in decision-making | Partial | Active learning and human-in-the-loop methods are included in the taxonomy. Contextual co-design with local users is advocated. However, no formal specification of human override, escalation, or decision authority |
| Socio-technical evaluation | Partial | Strongly advocates for field-relevant evaluation (deployment metrics over benchmark metrics), local validation, and contextual fit. Discusses failures of imported models (diabetic retinopathy in rural India, weather prediction in East Africa). However, does not present a socio-technical evaluation framework per se |
| Coastal fisheries / maritime domain | No | Not addressed. Agricultural examples focus on smallholder farming, not fisheries. Climate examples focus on weather forecasting and hydrology |

**Mid-Extraction Relevance Gate:** 1 Yes, 3 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17)

---

### 4. Decision Architecture Analysis

- **Architecture:** No decision architecture is defined. The paper is a review of AI *methods*, not AI *decision systems*. It provides a taxonomy of techniques and a constraint-to-method mapping, but does not design or specify how any of these methods would be integrated into a governed decision pipeline.
- **Layered structure:** The taxonomy organises methods by constraint axis (data, compute, connectivity, governance), and the evaluation framework uses seven operational axes. This is a method-selection architecture, not a decision-governance architecture.
- **Rule-based constraints before AI:** PINNs embed physical laws (PDEs, conservation laws) into the training loss — this constrains *what the model learns*, not *when/whether it operates*. No pre-AI safety gate or deterministic governance layer is discussed.
- **Boundary between deterministic control and AI reasoning:** Not defined in governance terms. The physics–ML hybrid (PINNs) blends physics constraints with data-driven learning at the model level, but there is no architectural separation between a deterministic governance layer and an AI reasoning layer.
- **Failure modes / fallback:** Contextual misalignment and domain shift are extensively discussed as deployment failure modes. The paper advocates for local validation and offline-first design. However, no runtime fallback mechanism, graceful degradation, or safety-state-triggered AI disengagement is specified.

---

### 5. Formal Model and Mathematical Representation

- **Formal model:** None at the system level. The paper references standard ML formulations (PINN loss functions, RL, few-shot learning) but does not define any formal system-level model with state variables, gate functions, or action spaces.
- **Comparison to DSR pipeline:** No parallel. The paper does not model E → S = f(E) → (G(S), A_AI(S)) → AI(E) or any equivalent pipeline. The decision matrix (Table 1) is a practitioner lookup table, not a formal decision function.
- **State-dependent recommendation restriction:** Not present. Methods are selected based on *structural constraints* (fixed deployment context), not on *runtime safety states* (dynamic environmental conditions).
- **Safety Dominance Property:** Not defined.
- **Formalisation purpose:** N/A — no system-level formalisation is attempted.

---

### 6. Safety State Classification

- **Discrete risk/safety levels:** Not defined. The paper classifies *environments* by structural constraints (data scarcity, compute limits, connectivity gaps) rather than operational *safety states*.
- **Comparison to S = f(E):** Constraint classification is static and structural (characterising a deployment context), whereas S = f(E) is dynamic and operational (classifying real-time environmental conditions for runtime governance). Different functions entirely.
- **AI recommendation scope differentiation across safety levels:** Not addressed. Method selection is constraint-matched (which technique for which setting), not state-conditioned (which AI outputs for which safety state).

---

### 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? (G(S)) | No | No mechanism for enabling/disabling AI based on operational state |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | No | No mechanism restricting AI output types by safety state |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | No | Not addressed |

- **Governance type:** The paper's "governance" is institutional/policy governance (data governance, AI strategies, regulatory frameworks), not operational AI governance. No runtime governance mechanism is defined.
- **Relation to two-level governance pair:** The paper's core contribution — matching AI methods to deployment constraints — is a design-time decision, not a runtime governance mechanism. My architecture's two-level governance pair (G(S), A_AI(S)) operates at runtime, dynamically conditioning AI behaviour on classified environmental state. These are complementary but distinct concerns: Katende addresses *which AI to deploy* (design-time); my architecture addresses *how deployed AI is governed* (runtime).

---

### 12. Key Concepts and Definitions

- **Data-efficient AI:** AI methods designed to achieve reliable performance under data scarcity, limited compute, unreliable connectivity, and constrained institutional capacity. Positioned not as a stopgap but as a foundational paradigm.
- **Structural constraints taxonomy:** Four primary constraint axes — data, compute, connectivity, governance — each mapped to suitable data-efficient methods (Table 1 decision matrix).
- **Physics-Informed Neural Networks (PINNs):** Encode PDEs and conservation laws into training loss, reducing need for dense labelled data by enforcing known physical structure. Relevant to low-resource settings where observational data is sparse but physical models are available.
- **TinyML/Edge ML:** Model–system co-design enabling ML inference on microcontrollers and ultra-low-power devices, minimising cloud dependence. Critical for deployment where connectivity and power are unreliable.
- **Federated learning (low-bandwidth variants):** Training across distributed devices without centralising data, with strategies for intermittent connectivity. Addresses both privacy and connectivity constraints.
- **Contextual misalignment / domain shift:** Failure mode where technically sound models underperform when deployed outside their training context (e.g., diabetic retinopathy screening in rural India, weather prediction in East Africa with sparse observations).
- **Offline-first design:** Architectural principle prioritising local inference and asynchronous synchronisation over continuous cloud connectivity. Identified as a structural requirement, not an optimisation.
- **Lean AI / constraint-aware AI:** Reframing of AI design priorities from scale-driven to constraint-driven — evaluating by field utility (energy, latency, offline capability, robustness, maintenance) rather than benchmark performance.

---

### 13. Limitations and Unsolved Problems

- **Stated limitations:**
  - Language and coverage bias — may under-represent non-English and regionally published work
  - Heterogeneity of sources prevents direct quantitative synthesis or meta-analysis
  - Dependence on secondary reporting where raw data/code was unavailable
  - Rapidly evolving landscape — foundation model fine-tuning and federated deployments may alter the balance
  - Taxonomy and decision matrix are a structured snapshot, not a final state of knowledge
- **Unsolved problems:**
  - How to integrate data-efficient methods into governed decision architectures for safety-critical applications (not addressed)
  - How to ensure AI reliability and safety under low-resource constraints (discussed as a need but no formal mechanism proposed)
  - How to move from design-time method selection to runtime governance of deployed AI in constrained environments
- **Alignment with my research gaps:**
  - The paper comprehensively characterises the low-resource deployment challenge but does not address how AI should be *governed at runtime* in these settings. My architecture fills precisely this gap: given that low-resource environments demand lean, constraint-aware AI, the two-level governance pair (G(S), A_AI(S)) provides the formal mechanism ensuring that deployed AI operates within safety-state-determined bounds
  - The paper's PINNs/physics-informed hybrid concept is structurally adjacent to my hybrid architecture (deterministic rules + probabilistic AI), but operates at the model level (physics in the loss function) rather than at the governance level (deterministic gate constraining AI participation)
  - No Safety Dominance Property or equivalent — the paper assumes AI will produce outputs; the question of whether/what AI should be *permitted* to produce is not raised

---

### 16. Relation to My Research and Positioning

- **Governance implementation:** Neither Level 1 nor Level 2 governance is implemented or proposed.
- **Two-level governance pair:** Not approached. The paper's contribution is orthogonal — it addresses *which AI methods work under low-resource constraints* (design-time), not *how deployed AI is governed under varying safety states* (runtime).
- **Safety Dominance Property:** Not defined.
- **Gap my research addresses:** Katende provides the strongest available characterisation of low-resource deployment constraints and the AI methods suited to them, but stops at method selection. My research extends this into operational governance: once a data-efficient AI method is selected and deployed in a low-resource, safety-critical environment, the two-level governance pair (G(S), A_AI(S)) ensures that the AI's participation and advisory scope are dynamically conditioned on classified environmental safety state. This is the missing runtime governance layer that Katende's design-time taxonomy does not provide.

**Positioning paragraph:** Katende (2026) is a **strong background reference for the low-resource AI deployment theme** in my literature review. It provides the most comprehensive recent characterisation of why mainstream AI paradigms fail in low-resource environments and what data-efficient alternatives are available — a framing that directly motivates my choice of coastal fisheries as a deployment domain. The paper's decision matrix (Table 1), structural metrics (Tables 2–10), and cross-domain failure cases (diabetic retinopathy in rural India, weather prediction in data-sparse Africa) provide citable evidence for the claim that AI systems deployed in low-resource settings must be designed around measured constraints. Critically, the paper demonstrates that even the most sophisticated constraint-aware AI taxonomy stops at design-time method selection and does not address runtime governance — the question of *whether and what* AI should be permitted to do under varying safety conditions. This is precisely the gap my two-level governance architecture fills. Katende should be cited as: (a) primary evidence for the low-resource deployment challenge, (b) support for physics-informed and data-efficient method selection as design-time decisions complementary to runtime governance, and (c) a framing reference for the argument that data-efficient AI is necessary but insufficient — it must be paired with formal safety-state-conditioned governance to be safely deployed in safety-critical, low-resource environments.

---

### 17. Overall Relevance Score

**⭐⭐⭐ Medium**

**Justification:** The paper is the strongest available reference for the low-resource AI deployment theme (Theme 4), providing comprehensive empirical and structural evidence for why AI in constrained environments requires fundamentally different design approaches. It also partially addresses hybrid AI (PINNs), human-in-the-loop methods, and socio-technical deployment concerns. However, it does not address safety-critical governance, decision architecture formalisation, or the core two-level governance gap — the themes central to my dissertation's contribution. Its value is as a strong contextual/motivational reference for the low-resource deployment rationale, not as an architectural or governance precedent. Elevated from ⭐⭐ to ⭐⭐⭐ because of the quality and comprehensiveness of its low-resource characterisation, which directly supports my domain selection justification.

---

### Recommended Citation Uses

| Use | Section in dissertation | Specific point |
|---|---|---|
| Low-resource deployment constraints | Literature review — low-resource environments section | Comprehensive characterisation of data, compute, connectivity, and institutional constraints in LMICs; structural metrics (Tables 2–10) |
| Design-time vs. runtime governance gap | Research gap section | Evidence that even comprehensive constraint-aware AI taxonomies stop at method selection and do not address runtime governance |
| Domain failure cases | Motivation / problem statement | Diabetic retinopathy failure in rural India (Beede et al. 2020 via Katende); weather prediction failure in data-sparse Africa — imported models fail under local constraints |
| Physics-informed methods as design-time complement | Architecture design rationale | PINNs/hybrid physics–ML as model-level constraint embedding, complementary to but distinct from architecture-level governance |
| Offline-first and edge deployment principles | System design / implementation | Offline-first design, TinyML, and federated learning as structural requirements for low-resource deployment — relevant to system design choices in my prototype |
| Decision matrix methodology | Evaluation methodology | Constraint-to-method mapping framework as a precedent for structured method selection in constrained environments |
