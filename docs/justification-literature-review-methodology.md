# Defending the Literature Review: Comprehensiveness, Comparison Methodology, Fairness, and Novelty

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 2 (Literature Review) and viva preparation  
**Questions addressed**: How was comprehensiveness ensured? What if someone already proposed this? Why these comparison dimensions? Are comparisons fair across domains? Is the contribution incremental or novel?

**Cross-references**: For the full gap argument with 22-row comparison table, see `justification-novelty-gap.md`. For differentiation from four system classes, see `justification-architecture-differentiation.md`. For the five-point differentiation method, see `justification-unified-governance.md` §7. For the search methodology itself, see `papers/search-methodology.md`.

---

## 1. How Was the Literature Review Made Comprehensive?

### 1.1 The Comprehensiveness Strategy

The literature search employed a multi-method strategy designed to ensure that no existing implementation of state-conditioned two-level governance was missed:

**Four search strands covering the full problem space.** The search was structured around four strands mapped to the five research questions: (1) AI safety governance and hybrid AI architecture (RQ1, RQ2), (2) formal methods and safety properties (RQ2), (3) low-resource environments and fisheries domain (RQ3), and (4) trust, evaluation, and human factors (RQ4, RQ5). This structure ensures coverage of both the governance mechanisms that might subsume the contribution and the domain/evaluation literature that grounds it.

**Multiple databases and discovery methods.** The primary search was conducted via Scopus (indexing IEEE, ACM, Elsevier, Springer, Taylor & Francis), supplemented by direct arXiv search for formal methods preprints. Additional papers were identified through backward snowball sampling (reference list scanning of key papers) and forward citation chasing (checking citing papers of primary comparators: Flehmig et al., Könighofer et al., Dalrymple et al., Baxi). Six methodological foundation papers were added following examiner recommendation.

**63 papers across 30+ venues.** The final corpus includes 63 papers: 30 full extraction (all 17 sections), 27 reduced extraction (7 sections), and 6 methodological foundation papers. These span IEEE, ACM, Elsevier, Springer, Frontiers, MDPI, Taylor & Francis, Wiley/Oxford, arXiv, and specialist venues — representing the breadth of the safety-critical AI, formal methods, and fisheries literatures.

**Structured extraction with relevance gating.** Each paper was extracted using a structured 17-section template covering paper identity, core contribution, relevance mapping (8 themes), decision architecture analysis, formal model analysis, safety state classification, governance level analysis, and positioning relative to the research. A mid-extraction relevance gate determined extraction depth (full vs. reduced), ensuring efficient allocation of analytical effort.

### 1.2 Systematic Review Confirmation

The comprehensiveness claim rests not only on the primary search but on four independent systematic reviews within the corpus that collectively survey bodies of literature far larger than any single researcher could cover:

| Systematic review | Papers surveyed | Domain | Binary governance confirmed? |
|---|---|---|---|
| Ramos et al. (2024) | 91 papers | Collaborative intelligence for safety-critical industries (manufacturing, automotive, aviation, maritime, nuclear, rail) | Yes — all governance mechanisms binary |
| Newcomb & Ochoa (2026) | 46 papers | Formal methods for safety-critical ML (shielding, CBF, reachability, runtime verification, model checking, SMT) | Yes — all formal methods operate with binary safety boundaries |
| Bengio et al. (2026) | 11 frameworks | International Frontier AI Safety Frameworks (Anthropic, OpenAI, Google DeepMind, Meta, NVIDIA, Cohere, etc.) | Yes — all implement Level 1 only |
| Perez-Cerrolaza et al. (2024) | 294 references | AI safety in industrial and transportation domains (automotive, avionics, railway, industrial robotics) | Yes — all safety mechanisms binary |

These reviews were conducted independently, by different research teams, using different methodologies, covering different bodies of literature. Their convergence on the same finding — binary governance is universal — provides a level of confidence that no single primary search could achieve. If a state-conditioned two-level governance architecture existed, it would appear in at least one of these four surveys.

### 1.3 Forward Citation Chasing of Closest Prior Works

The gap claim was further tested by checking citing papers of the four closest prior works:
- **Flehmig et al. (2024)**: citing papers checked for extensions toward advisory scope governance — none found
- **Könighofer et al. (2025)**: citing papers checked for extensions toward graduated (non-binary) shielding — none found
- **Dalrymple et al. (2024)**: citing papers checked for state-conditioned deployment of the GS AI framework — none found
- **Baxi (2026)**: citing papers checked — minimal citations given recency; no extension to environmental state conditioning found

### 1.4 What Could Be Missing

The search has documented limitations (see `papers/search-methodology.md` §11):
- **Non-English publications** may describe related architectures in Asian or European languages
- **Post-2026 publications** are not included
- **Alternative vocabulary** ("autonomy levels" rather than "AI governance") may have produced different search results
- **Grey literature** beyond arXiv and the one included M.Sc. thesis may contain relevant unpublished work

These limitations are acknowledged transparently. The mitigation is the four-SLR convergence: even if the primary search missed individual papers, the systematic reviews collectively cover the field's breadth.

---

## 2. What Would Happen If Someone Had Already Proposed This?

### 2.1 The Contingency

This is a legitimate concern. If a paper were discovered implementing S = f(E) → (G(S), A_AI(S)) with containment and a Safety Dominance Property, the contribution claim would need revision. The response depends on what the hypothetical prior work implements:

### 2.2 Scenario Analysis

**Scenario A — Prior work implements unified two-level governance but with a different conditioning variable (not environmental state).** This is the Baxi (2026) scenario. The contribution would be reframed as: "the first architecture implementing unified two-level governance *conditioned on classified environmental safety state* in a *physical safety-critical domain*." The conditioning variable difference (environmental state vs. robustness assessment vs. AI confidence) is not cosmetic — it determines the causal basis, independence properties, and formal tractability of the governance architecture (see `justification-environmental-state-governance.md`). The contribution survives.

**Scenario B — Prior work implements environmental-state-conditioned scope restriction but without formal properties.** The contribution would be reframed as: "the first *formally defined* architecture with the Safety Dominance Property and containment hierarchy." The distinction between an informal graduated system and a formal governance architecture with provable properties is substantive — it is the difference between Flehmig's traffic-light (three levels, no formal scope restriction property) and the proposed architecture.

**Scenario C — Prior work implements the full architecture in a different domain.** The contribution would be reframed as: "the first application of two-level governance to low-resource, safety-critical decision support in coastal fisheries, with socio-technical evaluation of the CAUTION mode." The domain application, evaluation framework (PS4, PS5), and the specific operationalisation for fisheries (R = {Go, Delay, DepartureTime, Duration}, E = {w, r, m, o, v, t}) would remain novel.

**Scenario D — Prior work implements the full architecture in the same domain with the same formal properties.** This would be a genuine novelty failure. The appropriate response would be: acknowledge the prior work, position the contribution as an independent derivation with potential methodological or evaluation contributions, and revise the contribution claim. This scenario is extremely unlikely given the four-SLR convergence.

### 2.3 The Structural Resilience of the Contribution

The contribution has multiple independently novel dimensions:
1. Unified two-level governance (G(S) + A_AI(S))
2. Environmental state conditioning (S = f(E))
3. Formal containment property
4. Safety Dominance Property for graduated governance
5. Domain application in low-resource fisheries
6. Socio-technical evaluation of CAUTION mode

For the contribution to be entirely pre-empted, a prior work would need to match on all six dimensions. Matching on any subset still leaves the remaining dimensions as contributions. This multi-dimensional novelty provides structural resilience against partial pre-emption.

---

## 3. Why These Comparison Dimensions?

### 3.1 The Comparison Framework

The literature review compares prior works along specific dimensions. Each dimension is chosen because it maps directly to a formal component of the proposed architecture:

| Comparison dimension | Why it matters | Architectural component |
|---|---|---|
| **Level 1: Does it control AI participation?** | Establishes whether the prior work implements any form of G(S) | G(S) — participation gate |
| **Level 2: Does it control advisory scope?** | Establishes whether the prior work constrains *what* AI may recommend (not just *whether* AI may act) | A_AI(S) — admissible advisory space |
| **Unified under same state?** | Establishes whether Level 1 and Level 2 respond to the same conditioning variable | (G(S), A_AI(S)) as a unified pair |
| **Environmental state conditioning?** | Establishes whether governance is triggered by observable environment, not AI self-assessment | S = f(E) |
| **Graduated (non-binary)?** | Establishes whether an intermediate mode exists between full participation and full blocking | CAUTION mode — {G=1, A_AI restricted} |
| **Formal properties?** | Establishes whether governance guarantees are proved, not assumed | Containment, Safety Dominance Property |
| **Runtime?** | Establishes whether governance operates continuously during system operation, not at design time | Continuous reclassification |

### 3.2 Why Not Other Dimensions?

An examiner might ask why alternative comparison dimensions were not used. The answer is that every dimension used maps to a *formal component* of the contribution. Dimensions that do not map to formal components would be descriptive rather than discriminating:

**Not compared on: accuracy, efficiency, scalability.** These are implementation and performance metrics, not architectural features. The contribution is architectural — it defines governance structure, not computational performance.

**Not compared on: user study results.** No prior work has evaluated a CAUTION mode (because none implements one). There is nothing to compare evaluation results against. PS4 and PS5 address this gap.

**Not compared on: AI model type.** The proposed architecture is algorithm-agnostic. Comparing prior works on their AI models would be comparing something irrelevant to the governance contribution.

### 3.3 The Dimensions Are Exhaustive for the Contribution Claim

The seven dimensions above jointly define the contribution. A prior work that matches on all seven dimensions *is* the proposed architecture. A prior work that differs on any dimension is structurally different in a formally identifiable way. The comparison framework is both necessary and sufficient for differentiating the contribution from prior work.

---

## 4. Are Comparisons Fair Across Domains?

### 4.1 The Fairness Concern

An examiner might argue: "You're comparing a fisheries DSS against papers from automotive, aviation, nuclear, and LLM safety. These are different domains with different requirements. Is it fair to say they don't implement your architecture when they were never trying to?"

### 4.2 The Response: The Comparison Is Structural, Not Evaluative

The comparison does not claim that prior works *should have* implemented two-level governance or that they are *deficient* for not doing so. The comparison establishes a factual claim: *no existing architecture* implements unified state-conditioned two-level governance. This is a gap statement, not a quality judgement.

Each prior work is evaluated on its own terms:
- Shields are evaluated as shields — they achieve their stated goal (binary safety guarantee) excellently
- Guardrails are evaluated as guardrails — they achieve comprehensive output constraint effectively
- Flehmig's traffic-light is evaluated as a degradation indexing framework — it achieves its stated goal of monitoring AI quality
- Baxi's CGAE is evaluated as an economic governance architecture — it proves its stated theorems rigorously

The comparison shows that none of these works, despite their quality, addresses the specific problem the proposed architecture solves: runtime, environment-conditioned restriction of AI advisory recommendation types in a safety-critical decision support context. This is a structural observation about what exists in the literature, not a criticism of what exists.

### 4.3 Cross-Domain Comparison Is Standard Practice

Cross-domain comparison is standard in safety engineering research. The safety-critical AI literature itself operates cross-domain:
- Perez-Cerrolaza et al. (2024) survey across automotive, avionics, railway, and industrial robotics
- Ramos et al. (2024) review across manufacturing, automotive, aviation, maritime, nuclear, and rail
- Bloomfield & Rushby (2025) draw analogies from nuclear, aviation, and medical device safety
- Gyllenhammar et al. (2025) apply automotive safety methods while citing aviation precedents

Cross-domain comparison is not only fair — it is the method by which the safety engineering community identifies universal patterns (like binary governance) and domain-specific gaps (like the absence of graduated governance in any domain).

### 4.4 The Domain-Specific Comparison Is Also Made

Within the fisheries/maritime domain (T8), the comparison is domain-specific:
- No maritime AI decision support system implements state-conditioned governance (Madsen & Kim, 2024 — none of the reviewed systems restrict AI output types based on risk level)
- No fisheries DSS implements any form of formal governance (the domain gap — no paper in the 63-paper corpus addresses coastal fisheries with formal governance)
- The empirical studies (Gao, 2024; Rahim et al., 2024; Yamin et al., 2025) confirm that the tripartite decision pattern exists in practice but has no formal decision support analogue

The cross-domain comparison establishes the architectural gap is universal. The domain-specific comparison establishes the domain need is unmet.

---

## 5. Is the Contribution Incremental or Novel?

### 5.1 Why This Question Arises

The constituent ideas are all established:
- Environmental state classification → standard in weather warning systems
- AI participation control → standard in safety shields
- Output scope restriction → exists in guardrails
- Three-level graduated response → exists in traffic lights, automotive ODD/ROD/MRC
- Formal safety properties → exist for binary governance

An examiner might reasonably argue: "You've assembled existing pieces into a new combination. Is this novel or merely incremental?"

### 5.2 The Novelty Argument: Integration Is the Contribution

The novelty is not in the pieces — it is in their **formal integration** under a single conditioning variable with provable properties that none of the pieces individually possesses.

**Analogy.** The transistor, resistor, and capacitor all existed before the integrated circuit. The integrated circuit's contribution was not any individual component but the formal, manufacturing-level integration that produced emergent properties (miniaturisation, reliability, cost reduction) that individual components could not achieve. Similarly:

- Environmental state classification alone does not produce the Safety Dominance Property
- AI participation control alone does not produce the CAUTION mode
- Output scope restriction alone does not produce the containment hierarchy
- Three-level graduated response alone does not produce state-conditioned scope restriction

The proposed architecture integrates these under S = f(E) → (G(S), A_AI(S)) with formally provable properties. The Safety Dominance Property, the containment hierarchy, and the CAUTION mode are **emergent properties of the integration** — they do not exist in any individual component.

### 5.3 Evidence That This Is Not Incremental

Three lines of evidence distinguish novel integration from incremental combination:

**Line 1 — No one else has done it.** If the integration were incremental — a straightforward assembly of existing pieces — someone in the substantial safety-critical AI community would have done it. Four systematic reviews covering 91 + 46 + 11 + 294-reference bodies of literature confirm that no one has. The fact that the constituent ideas are well-established makes the absence *more* surprising, not less — and therefore *more* indicative of a non-trivial gap rather than a trivial omission.

**Line 2 — The integration requires non-obvious design choices.** The integration is not simply "put the pieces together." It requires:
- Choosing environmental state (not AI confidence, not performance degradation) as the conditioning variable — a design choice justified against seven alternatives in `justification-environmental-state-governance.md`
- Choosing three states (not binary, not continuous, not five-level) — justified against four alternatives in `justification-three-states.md`
- Choosing advisory scope restriction (not blocking, not autonomy reduction) as the CAUTION governance action — justified against two alternatives in `justification-advisory-scope-restriction.md`
- Defining the Safety Dominance Property for graduated (non-binary) governance — no prior definition exists

Each design choice is non-trivial and requires independent justification. An incremental combination would not require four dedicated justification documents.

**Line 3 — The formal properties are new.** The Safety Dominance Property AI(E) ⊆ A_AI(S) for graduated governance has not been defined or proved in any prior work. The closest precedent is Baxi's Theorem 3 (bounded economic exposure), which proves an analogous property for an orthogonally conditioned architecture. Defining a new formal property and proving it holds for a new architecture is a contribution to the formal methods literature, not an incremental extension of existing results.

### 5.4 The Positioning Statement

The contribution is **novel at the integration level and the formal property level**, while building on well-established constituent ideas at the component level. This is the standard pattern for architectural contributions in safety engineering: the architectural innovation is the principled integration of known mechanisms into a configuration with formally provable properties that the individual mechanisms cannot achieve alone.

Bloomfield & Rushby (2025) provide the clearest articulation of this pattern: their taxonomy of guarded AI architectures shows that the same constituent components (AI system, guard, fallback, monitor) can be arranged in nine distinct configurations, each with different assurance properties. The architectural contribution is not the components but the configuration — and the formal properties that the configuration produces. The proposed architecture follows the same pattern: known components (environmental classification, participation gate, scope restriction, formal properties), new configuration ((G(S), A_AI(S)) unified under S = f(E)), new formal properties (containment, Safety Dominance for graduated governance).

---

## 6. Comparative Summary Table

| Question | Answer | Key evidence |
|---|---|---|
| **How is comprehensiveness ensured?** | Four search strands, multiple databases, snowball sampling, forward citation chasing, examiner recommendations — plus four independent SLRs covering 91+46+11+294-ref bodies | `papers/search-methodology.md`; convergence of four independent SLRs |
| **What if already proposed?** | Multi-dimensional contribution provides structural resilience; four scenarios analysed with contingency responses | Six independently novel dimensions; Scenario D (full pre-emption) extremely unlikely given SLR convergence |
| **Why these comparison dimensions?** | Each maps to a formal component of the contribution; jointly exhaustive for the contribution claim | 7 dimensions → 7 architectural components; matching all 7 = same architecture |
| **Fair cross-domain comparison?** | Structural gap statement, not quality judgement; cross-domain comparison is standard safety engineering method | Perez-Cerrolaza, Ramos, Bloomfield all compare cross-domain; domain-specific comparison also made |
| **Incremental or novel?** | Novel at integration and formal property level; constituent ideas are established; integration produces emergent properties (CAUTION mode, Safety Dominance, containment) none possess individually | Four SLRs confirm no one has done it; four non-obvious design choices; new formal property defined and proved |

---

## 7. One-Paragraph Summary (for use in Chapter 2)

> The literature review's comprehensiveness is ensured through a multi-method search strategy: four keyword strands covering the full problem space (safety governance, formal methods, fisheries domain, trust/evaluation), primary search via Scopus with direct arXiv supplementation, backward snowball sampling and forward citation chasing of primary comparators (Flehmig et al., 2024; Könighofer et al., 2025; Dalrymple et al., 2024; Baxi, 2026), and examiner-recommended additions for evaluation methodology — producing a corpus of 63 papers across 30+ venues. The gap claim is confirmed not by the primary search alone but by four independent systematic reviews within the corpus: Ramos et al. (2024) across 91 collaborative intelligence papers, Newcomb & Ochoa (2026) across 46 formal methods studies, Bengio et al. (2026) across 11 international AI safety frameworks, and Perez-Cerrolaza et al. (2024) across automotive, avionics, railway, and industrial domains — all independently confirming binary governance as universal. Cross-domain comparison is structural, not evaluative: prior works are assessed on their own terms (shields are excellent shields; guardrails are comprehensive guardrails), and the comparison establishes the factual absence of unified state-conditioned two-level governance, not a quality deficiency. The comparison dimensions (Level 1, Level 2, unification, environmental conditioning, graduation, formal properties, runtime operation) each map to a formal component of the contribution, making the framework both necessary and sufficient for differentiation. The contribution is novel at the integration level: the constituent ideas (environmental classification, participation control, scope restriction, three-level graduation, formal safety properties) are individually well-established, but their formal integration under a single conditioning variable S = f(E) produces emergent properties — the CAUTION mode, the containment hierarchy, and the Safety Dominance Property for graduated governance — that no individual component possesses and that no prior work implements, as confirmed across four independent systematic reviews covering the full breadth of the safety-critical AI, formal methods, and governance literatures.
