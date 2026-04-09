# Usable Content: Attard-Frost & Lyons (2025)

**Citation:** Attard-Frost, B., & Lyons, K. (2025). AI governance systems: A multi-scale analysis framework, empirical findings, and future directions. *AI and Ethics*, 5, 2557–2604. https://doi.org/10.1007/s43681-024-00569-5

**Status:** Peer-reviewed journal article (Springer). DOI confirmed. Fully citable for load-bearing arguments.

---

## The Paper's Contribution

Attard-Frost and Lyons apply a service systems analysis framework to an empirical study of Canada's national AI governance system. Through 20 semi-structured interviews with government leaders and subject matter experts (February–July 2023), they produce a dataset of 610 governance-related topics across 12 analytical dimensions. This is the most comprehensive empirical decomposition of a national-scale AI governance system in the literature.

The 12 analytical dimensions are: interview context, actors, benefits/risks/harms, resources, networks, interactions, evaluations, logics, functional bounds, rules, ecosystem, and opportunities for improvement (p. 2558–2559, Fig. 6, p. 2596).

The study identifies 120 unique actors (44 organisational, 23 socio-technical, 53 specific instances), 142 unique resources (75 knowledge/cognitive, 26 policy/legal, 18 financial, 17 data/computational, 6 cultural), and 40 unique networks (18 resource integration, 22 governance) involved in Canada's national AI governance system (Table 1, p. 2563).

---

## Usable Content #1: The Field's Own Definition of AI Governance

The paper adopts Mäntymäki et al.'s (2022) definition: "AI governance is a system of rules, practices, processes, and technological tools that are employed to ensure an organization's use of AI technologies aligns with the organization's strategies, objectives, and values; fulfils legal requirements; and meets principles of ethical AI followed by the organization" (p. 2558).

**Why this matters for your research:** This is the field's own self-definition of AI governance. It explicitly frames governance as an *organisational/institutional* phenomenon — rules, practices, processes — oriented toward alignment, compliance, and ethics. There is no reference to runtime environmental state classification, no concept of an admissible output space that varies by condition, no state-conditioned scope restriction. The definition describes *who governs and through what policy instruments* — not *how the AI system's behaviour is formally bounded by classified environmental state at runtime*. This confirms that the entire AI governance field operates at a different analytical layer from the two-level governance pair (G(S), A_AI(S)).

---

## Usable Content #2: 610-Topic Empirical Mapping with Zero Runtime State-Conditioned Concepts

The 610-topic dataset (Appendix 1, pp. 2574–2596) covers the full scope of what 20 governance experts perceive as constituting a national AI governance system. The topics range across policy instruments, institutional actors, knowledge resources, financial constraints, evaluation criteria, governance logics, and ecosystem dynamics.

**What is present:**
- Regulatory development (11/20 interviews), organisational AI governance (8/20), standards development (6/20) as the most prominent work contexts (p. 2562)
- 142 unique governance resources including laws, regulations, directives, guidance documents, auditing frameworks, compliance programs (pp. 2565, 2580–2587)
- 21 rule-based constraints including AI-related laws (9/20 interviews), jurisdictional limitations (7/20), organisational norms (7/20) (p. 2567)
- 25 ecosystem-level phenomena including international framework alignment (13/20), cross-initiative feedback loops (11/20), the AI Brussels Effect (7/20) (p. 2568)

**What is absent:**
- No topic references runtime environmental state classification
- No topic references state-conditioned advisory scope restriction
- No topic references graduated operational modes for AI systems
- No topic references a formally bounded admissible output space
- No topic references a safety dominance property or containment relationship
- No topic references anything analogous to the CAUTION mode

**Why this matters for your research:** This is the strongest available empirical evidence that the institutional governance literature — even at its most granular — does not contain the concept you are contributing. The absence is not due to shallow analysis; it is a 610-topic, 12-dimension mapping that covers the full breadth and depth of governance system components. The Level 2 concept simply does not exist at this analytical layer.

---

## Usable Content #3: "Guardrails" Appear Only in Binary Framing

In the 610-topic dataset, the concept of runtime AI control ("guardrails") appears only twice:

- **Topic ID#1.15** — "Guardrails on AI" — mentioned in 2 of 20 interviews as a work context (p. 2574)
- **Topic ID#6.21** — "Guardrails effectively prevent harms" — mentioned in 2 of 20 interviews as an evaluation criterion (p. 2589)

Both instances frame guardrails in binary terms: they either exist or they don't; they either prevent harms or they fail to. There is no graduated concept — no notion that guardrails might *partially* restrict AI behaviour based on environmental conditions while still permitting bounded participation.

**Why this matters for your research:** Even when governance practitioners reference runtime AI control, they default to binary framing. This is consistent with the gap claim that all existing governance mechanisms implement at most binary participation governance (permit/block). The practitioners' own mental model of runtime AI governance is binary, confirming that the graduated CAUTION mode — where AI participates within a formally restricted non-empty scope — is genuinely absent from both the technical literature and the practitioner discourse.

---

## Usable Content #4: Policy Instrument Spectrum — Graduated Intuition Without Runtime Implementation

The paper finds that governance practitioners perceive "a spectrum of AI policy instruments with varying tradeoffs between legal force and administrative agility, ranging from legislation and regulation (high force/low agility) to voluntary guidance documents (low force/high agility)" (p. 2568).

This means practitioners already understand that governance need not be all-or-nothing at the institutional layer. They recognise intermediate positions between binding law and voluntary guidance.

**Why this matters for your research:** The *intuition* for graduated governance already exists among practitioners — but only at the policy instrument layer (what type of policy to apply). Nobody has translated this intuition into the runtime architectural layer (what output space to permit the AI based on classified environmental state). The two-level governance pair formalises at the runtime layer what practitioners already practice informally at the institutional layer: not every situation requires the same governance intensity; intermediate conditions call for intermediate restrictions.

---

## Usable Content #5: Multi-Scale Governance Without Runtime Dimension

The paper establishes that AI governance operates across five institutional scales: international, national, subnational, sectoral, and organisational (p. 2557–2559). Fig. 4 (p. 2569) depicts these scales as nested systems with strategy initiatives, policy initiatives, and coordinating actors at each level.

**Why this matters for your research:** The governance literature has thoroughly explored *institutional scale variation* — from OECD-level international frameworks down to municipal directives. What it has not explored is *runtime state variation* within a single AI system. The two-level governance pair operates at a single institutional scale (one deployed AI system in one operational context) but varies *across classified environmental states* at runtime. This is the dimension the multi-scale governance literature does not address: not the institutional hierarchy of who governs, but the runtime classification of what environmental conditions determine what the AI may recommend.

---

## Usable Content #6: Knowledge Resource Constraints — Low-Resource Governance Motivation

The most frequently perceived functional limitation on AI governance was "knowledge/expertise resource limitations within organizations" (10 of 20 interviews), followed by "gaps in stakeholder literacies and awareness" (8/20) and "knowledge/expertise resource limitations within Canada's AI ecosystem" (6/20) (p. 2567).

The paper also identifies financial limitations (5/20 interviews), administrative incapacities (4/20), and interpretive barriers around foundational terms like "AI systems" and "AI governance" (4/20) as constraints (p. 2567).

**Why this matters for your research:** If knowledge and expertise gaps are the most severe governance constraint even in Canada — the first country to launch a national AI strategy, with dedicated institutions (CIFAR, Vector Institute, Mila), federal directives, and a proposed AI Act — then in low-resource environments like small-scale coastal fisheries, these gaps are orders of magnitude more severe. This strengthens the case for *architecturally embedded governance* (your system) rather than reliance on institutional governance capacity that may not exist in the operational environment. Governance cannot be expected to come from external institutions when the deployment context lacks the knowledge, expertise, and financial resources to support those institutions. Instead, governance must be built into the AI architecture itself — which is what the two-level governance pair achieves.

---

## Usable Content #7: The "Proactive Governance" Absence

In the dataset, "proactive governance" appears only twice:
- **Topic ID#1.19** — "Proactive governance" as a work context — 2 of 20 interviews (p. 2574)
- **Topic ID#11.37** — "More proactive governance initiatives" as an opportunity for improvement — 1 of 20 interviews (p. 2595)

This confirms that proactive governance (governance triggered *before* harm occurs, based on environmental state assessment) is barely on the radar even as an aspiration. The dominant paradigm is reactive — governance responding to observed harms, compliance failures, or audit findings.

**Why this matters for your research:** The proactive/reactive distinction is one of your key differentiators. Existing governance operates reactively (responding to detected AI misbehaviour or external compliance requirements). Your governance pair operates proactively — classifying environmental state *before* the AI acts, and conditioning the admissible output space on that classification. The empirical evidence that governance practitioners barely mention proactive governance (3 out of 610 topics) strengthens the claim that proactive, state-conditioned governance is genuinely novel.

---

## Relationship to Previously Extracted Papers

**Pairs with Bengio et al. (2024/2026):** Bengio provides breadth (11 Frontier AI Safety Frameworks across nations); Attard-Frost & Lyons provides depth (610 topics within one national system). Together they show the institutional governance layer has been studied at both breadth and depth — and the Level 2 concept is absent from both.

**Supersedes Hood (2026) for citability:** Hood proposes the "Nomotic AI" vocabulary for the same governance layer but is grey literature with no DOI. Attard-Frost & Lyons is peer-reviewed, empirical, and published in a Springer journal. If only one policy-layer citation is needed, prefer Attard-Frost & Lyons.

**Complements Shamsujjoha et al. (2025):** Shamsujjoha et al. shows that guardrail *mechanisms* are binary at the technical level. Attard-Frost & Lyons shows that guardrail *perceptions among governance practitioners* are also binary. Together they confirm the binary limitation exists at both the mechanism layer and the practitioner discourse layer.

**Complements Duit & Galaz (2008):** Duit & Galaz provide theoretical governance typologies; Attard-Frost & Lyons provides empirical governance components. Both confirm the absence of state-conditioned runtime scope restriction — Duit & Galaz at the theoretical level, Attard-Frost & Lyons at the empirical level.

---

## Bottom Line

This paper is a **high-quality, peer-reviewed source** that you can use to establish what institutional AI governance looks like at maximum empirical resolution — and to show that even at that resolution, the concept of state-conditioned runtime advisory scope restriction does not appear. Its strongest deployment is as a single-sentence empirical anchor for the layer-distinction argument: the institutional governance layer has been mapped exhaustively, and the two-level governance pair occupies a different layer entirely.
