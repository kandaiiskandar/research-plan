# Artificial Intelligence Risk Management Framework (AI RMF 1.0)

**Citation:** National Institute of Standards and Technology (NIST). (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

**Short reference:** NIST AI RMF 1.0 (2023)

**PDF:** https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

**Corpus status:** Added August 2026 — primary AI governance framework for Section 3 and for positioning the proposed architecture against established governance standards

---

## 1. What the document is

A voluntary framework published by the U.S. National Institute of Standards and Technology (NIST) in January 2023, intended to help organisations design, develop, deploy, and use AI systems in ways that manage risk to individuals, organisations, and society. It is sector-agnostic and does not mandate specific technical implementations.

The document is structured in two parts:
- **Part 1 (Framing Risk):** Conceptual foundations — what AI risk is, who AI actors are, and what characteristics trustworthy AI should have
- **Part 2 (Core and Profiles):** The four Core Functions — GOVERN, MAP, MEASURE, MANAGE — and how organisations can apply them

AI RMF 1.0 is a living document; NIST committed to reviewing it by 2028. A voluntary companion document, the AI RMF Playbook, provides actionable sub-practices.

---

## 2. Trustworthy AI Characteristics (Part 1)

NIST identifies seven characteristics of trustworthy AI. These are the normative targets for governance:

| Characteristic | Summary |
|----------------|---------|
| Accountable & Transparent | Actors take responsibility; AI decisions are explainable to affected parties |
| Explainable & Interpretable | AI outputs are understandable to intended audiences |
| Fair (Bias Managed) | AI does not produce unjustified discriminatory outcomes |
| Privacy-Enhanced | Data governance respects individual privacy rights |
| Reliable | AI behaves consistently and accurately across its intended use conditions |
| Resilient | AI maintains performance under adversarial or unexpected inputs |
| **Safe** | AI does not cause undue harm to people, property, or environment |
| Secure | AI and its infrastructure are protected against adversarial compromise |
| Valid | AI performs as intended and meets specifications |

**Safe** is defined as freedom from conditions that can cause harm to people, other living beings, or the environment — including harms arising from intended use, misuse, or unintended behaviour.

---

## 3. The Four Core Functions (Part 2)

### GOVERN
Establishes the organisational culture, policies, accountability structures, and processes needed for AI risk management. GOVERN is foundational — the other three functions depend on it.

Key sub-categories:
- **GOVERN-1:** Policies, processes, and practices are established and disseminated
- **GOVERN-2:** Accountability is assigned and human oversight is maintained
- **GOVERN-4:** Organisational risk tolerance is established and communicated
- **GOVERN-6:** Policies and procedures exist for AI risks in acquisition, deployment, and operation

### MAP
Identifies and categorises AI risks in context. Outputs include risk identification, risk characterisation, and impact assessment.

Key sub-categories:
- **MAP-1:** Establish context — intended use, stakeholders, affected populations
- **MAP-2:** Scientific and organisational understanding of AI limitations
- **MAP-5:** Likelihood and magnitude of risk impacts are mapped

### MEASURE
Analyses and assesses AI risks using qualitative and quantitative methods. Covers metrics, testing, benchmarking, and monitoring.

### MANAGE
Prioritises and addresses identified AI risks. Includes treatment plans, residual risk acceptance, and incident response.

---

## 4. Relevance to this research

### 4.1 The proposed architecture as a technical instantiation of GOVERN

AI RMF defines *what* governance should accomplish but does not specify *how* to technically enforce it at runtime. The proposed graduated safety-state-gated architecture is a concrete technical mechanism that operationalises AI RMF principles at the implementation level:

| AI RMF principle | Proposed architecture implementation |
|-----------------|--------------------------------------|
| GOVERN-1: Policies govern AI participation | G(S) = 0 when f(E) = UNSAFE — participation gate enforces the policy |
| GOVERN-6: Policies govern advisory scope | A_AI(S) restricts recommendation types to those warranted by the current safety state |
| GOVERN-4: Risk tolerance operationalised | The three-state structure (SAFE, CAUTION, UNSAFE) implements a formal risk tolerance ladder |
| Safe (trustworthy AI) | Safety Dominance Property: AI(E) ⊆ A_AI(f(E)) — formally proved by construction |
| Reliable | Totality (Theorem 5.1): f(E) is defined for all E — no undefined governance states |

### 4.2 The CAUTION gap in AI RMF

AI RMF does not define a technical analogue to the CAUTION mode. Its governance language is organisational and qualitative: it identifies that AI systems should be governed under varying risk levels, but does not formalise a mechanism for graduated advisory scope restriction. This supports the research gap argument: AI RMF identifies the *need* for graduated governance but does not provide the *formal technical mechanism* to implement it. The proposed architecture fills this gap at the implementation layer.

Specifically:
- AI RMF has no concept of a formally defined intermediate governance state with a constrained-but-non-zero advisory scope
- AI RMF does not define A_AI(S) or any analogue of per-state recommendation space restriction
- AI RMF's safety properties are normative targets, not formally proved properties
- The proposed architecture achieves what AI RMF describes as the goal of GOVERN in a domain-specific, formally verifiable implementation

### 4.3 Positioning in the paper

**Section 3 (AI Governance Foundations):** AI RMF is the primary governance framework reference. Use it to establish the vocabulary of AI governance (GOVERN, risk tolerance, safe AI characteristics) and to show that existing frameworks identify what good governance should do without specifying runtime technical mechanisms.

**Section 5 (Formal Architecture):** Brief forward reference — the governance pair (G(S), A_AI(S)) can be positioned as a formal, domain-specific implementation of AI RMF's GOVERN function.

**Section 6 / Gap argument:** The absence of a CAUTION analogue in AI RMF supports the four-layer gap argument — the gap exists not only in the academic literature but in the primary voluntary AI governance framework in active use.

### 4.4 What AI RMF does NOT support

- No formal specification language or mathematical notation
- No proof obligations or verification requirements
- No technical architecture for runtime enforcement
- No domain-specific threshold design (thresholds are an implementation concern outside AI RMF's scope)
- Not a standard with compliance requirements — voluntary adoption only
- No concept of graduated advisory scope restriction

---

## 5. Accurate citation text for Section 3

> The NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0) (NIST, 2023) is the primary voluntary AI governance framework in current use. It organises AI risk management around four Core Functions — GOVERN, MAP, MEASURE, and MANAGE — and defines seven characteristics of trustworthy AI, of which **Safe** (freedom from conditions that cause undue harm) and **Reliable** (consistent performance across intended use conditions) are directly relevant to deployment in safety-critical environments. The GOVERN function establishes that AI systems should be subject to policies governing both participation and advisory scope, and that organisations should operationalise a formal risk tolerance position. However, AI RMF is a process framework: it identifies *what* governance should achieve — including graduated, risk-proportionate controls — but does not specify *how* to technically enforce such controls at runtime. No AI RMF sub-category defines a formal intermediate governance state equivalent to the proposed CAUTION mode, in which an AI system remains active but operates within a formally restricted recommendation space. The proposed architecture is a domain-specific technical implementation of AI RMF's GOVERN objectives, extended with formal verifiability that AI RMF does not itself require.

---

## 6. Bibliographic details

- **Title:** Artificial Intelligence Risk Management Framework (AI RMF 1.0)
- **Short title:** AI RMF 1.0
- **Publisher:** National Institute of Standards and Technology (NIST), U.S. Department of Commerce
- **Document number:** NIST AI 100-1
- **Year:** January 2023
- **DOI:** https://doi.org/10.6028/NIST.AI.100-1
- **URL:** https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **Access:** Open access (free of charge)
- **Scope:** Voluntary; sector-agnostic; U.S. federal but internationally influential
- **Status:** Living document; next major review expected by 2028
- **Companion document:** NIST AI RMF Playbook (sub-practices for each Core Function)
