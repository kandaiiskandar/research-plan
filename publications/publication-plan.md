# Publication Plan

**Dissertation**: A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments  
**Target graduation**: 2029  
**Requirement**: Minimum 2 published papers — one in a high-indexed journal (Scopus/WoS/ERA), one in a MyCite-indexed journal  
**Plan**: 3 papers  
**Date**: 2026-04-12

---

## Paper Overview

| # | Paper | Type | Target journal | Quartile / Index | Target submission | Target publication |
|---|-------|------|---------------|------------------|-------------------|--------------------|
| 1 | Binary or Graduated? A Systematic Review of Safety Governance Mechanisms in AI Decision Support Systems | Review / survey | Safety Science (Elsevier) | Scopus Q1 | Q4 2026 | Mid 2027 |
| 2 | The graduated safety-state-gated architecture: formal model and properties | Core contribution | Expert Systems with Applications (Elsevier) | Scopus Q1 | Q2 2027 | Late 2027 – Early 2028 |
| 3 | Applying graduated AI governance to Malaysian coastal fisheries | Domain application | Pertanika JTAS (UPM) | MyCite + Scopus | Q4 2027 | Mid 2028 |

---

## Paper 1 — Binary or Graduated? A Systematic Review of Safety Governance Mechanisms in AI Decision Support Systems

### What it covers

A systematic or scoping review analysing how existing AI safety governance mechanisms (safety shields, runtime verification, guardrails, gating architectures) handle the participation and advisory scope problem. The central finding: governance is universally binary (allow/block) across 75+ papers — no existing work implements graduated, multi-state advisory scope restriction conditioned on environmental state.

### Why this paper comes first

- The literature corpus (75+ papers, 34 full extractions) is already built and analysed
- The review plan, comparison table, and gap analysis are substantially complete
- Publishing the review establishes the gap before the solution paper
- Review papers have high citation potential and establish credibility in the field

### Key arguments

1. AI safety governance mechanisms are binary — confirmed across safety shields, runtime verification, formal methods, and international frameworks
2. No existing mechanism restricts *what* AI recommends (advisory scope) based on operational conditions — only *whether* AI participates
3. The gap between binary governance and graduated, condition-sensitive governance is the space the dissertation fills
4. Low-resource and domain-specific contexts amplify the limitation of binary approaches

### Publishable deliverables from existing work

- Theme-gap analysis (8 themes across 75+ papers)
- Comparison table of governance mechanisms
- Binary governance evidence synthesis (justification documents)
- Formal characterisation of the binary limitation (CRANE TC⁰ result, Kwon et al. adaptive shield analysis)

### Target journals

| Journal | Publisher | Quartile | Fit | Review time |
|---------|-----------|----------|-----|-------------|
| **Safety Science** | Elsevier | Q1 (CiteScore ~10) | Primary target — publishes AI safety governance reviews; strong industrial safety audience | ~3 months |
| **Artificial Intelligence Review** | Springer | Q1 (CiteScore ~19) | Fallback — higher impact but more competitive; good for comprehensive AI reviews | ~4 months |
| **AI & Ethics** | Springer | Q1–Q2 | Alternative — multidisciplinary; good fit if governance framing is emphasised | ~3 months |

### Timeline

| Milestone | Target date |
|-----------|-------------|
| Finalise review protocol (PRISMA/scoping framework) | May 2026 |
| Complete comparison table and gap synthesis | Jun 2026 |
| Draft manuscript | Jul – Sep 2026 |
| Internal review with supervisor | Oct 2026 |
| Submit to Safety Science | Nov 2026 |
| Expected review cycle | Nov 2026 – Feb 2027 |
| Revision and resubmission | Mar 2027 |
| Expected acceptance | Mid 2027 |

---

## Paper 2 — Formal Graduated Safety-State-Gated Architecture

### What it covers

The core dissertation contribution: a formal governance architecture with two-level governance (Level 1: participation gate G(S), Level 2: advisory scope restriction A_AI(S)), three safety states (SAFE, CAUTION, UNSAFE), environmental state classification S = f(E), and the Safety Dominance Property AI(E) ⊆ A_AI(S). This is the architecture paper — formal definitions, provable properties, and worked examples.

### Why this paper comes second

- Depends on the review paper establishing the gap it fills
- The formal model (Appendix C) needs to be finalised and validated
- Can reference Paper 1 as "we previously showed the governance gap; here we address it"

### Key arguments

1. Introduce E = {w, r, m, o, v, t} and the classification function S = f(E)
2. Define the governance pair (G(S), A_AI(S)) and three-state graduated response
3. Prove the Safety Dominance Property and worst-case aggregation correctness
4. Demonstrate that graduated governance is strictly more expressive than binary governance while preserving formal safety guarantees
5. Compare architecturally against shields, runtime verification, and guardrail frameworks

### Publishable deliverables from existing work

- Appendix C formalisation (environmental state, classification, governance pair, properties)
- Justification documents (formal model, safety state design, three states, architecture differentiation, contribution characterisation)
- Comparison with Könighofer shields, Dalrymple guaranteed safe AI, Wang AgentSpec, Baxi comprehension-gated economy

### Target journals

| Journal | Publisher | Quartile | Fit | Review time |
|---------|-----------|----------|-----|-------------|
| **Expert Systems with Applications** | Elsevier | Q1 (IF ~10) | Primary — publishes formal AI architectures and decision support systems | ~3–4 months |
| **Decision Support Systems** | Elsevier | Q1 | Alternative — explicit focus on decision architecture and governance frameworks | ~3 months |
| **Journal of Systems and Software** | Elsevier | Q1 | Fallback — formal design and verification of complex systems | ~3–4 months |

### Timeline

| Milestone | Target date |
|-----------|-------------|
| Finalise formal model (Appendix C) and proofs | Dec 2026 – Jan 2027 |
| Draft architecture paper with worked examples | Feb – Apr 2027 |
| Internal review with supervisor | May 2027 |
| Submit to Expert Systems with Applications | Jun 2027 |
| Expected review cycle | Jun – Sep 2027 |
| Revision and resubmission | Oct 2027 |
| Expected acceptance | Late 2027 – Early 2028 |

---

## Paper 3 — Domain Application: Malaysian Coastal Fisheries

### What it covers

Applying the graduated governance architecture to AI-assisted go/no-go decisions for Malaysian small-scale fishers. This paper grounds the formal architecture in a concrete low-resource, safety-critical domain — using Malaysian weather data, marine conditions, fisher practices, and vessel categories. It demonstrates how E = {w, r, m, o, v, t} maps to real Malaysian coastal conditions and how A_AI(S) produces contextually appropriate advisory scope.

### Why this paper comes third

- Depends on the formal architecture (Paper 2) being defined
- Requires domain-specific data collection or case study design
- Best suited for a MyCite-indexed journal to fulfil the Malaysian publication requirement
- Positions the work within Malaysian fisheries policy and practice

### Key arguments

1. Malaysian small-scale fishers operate in a low-resource, safety-critical context (Shaffril et al. 2017; Yamin et al. 2025; Obi et al. 2025)
2. Instantiate E vector with Malaysian-specific thresholds (MetMalaysia weather data, marine warnings, vessel categories under Malaysian fisheries regulations)
3. Demonstrate graduated governance producing differentiated advisory output (SAFE: full recommendations including distant fishing grounds; CAUTION: restricted to near-shore, conservative recommendations; UNSAFE: no AI advisory, human-only decision)
4. Socio-technical evaluation: how graduated governance fits fisher decision-making practices (Gao 2024; Rahim et al. 2024)

### Target journals

| Journal | Publisher | Indexed | Fit | Review time |
|---------|-----------|---------|-----|-------------|
| **Pertanika JTAS** | UPM | MyCite + Scopus | Primary — covers fisheries and agricultural technology; strong Malaysian recognition | ~4–6 months |
| **Pertanika JST** | UPM | MyCite + Scopus | Alternative — broader science and technology scope; accepts marine/AI applications | ~4–6 months |
| **Malaysian Journal of Computer Science** | UM | MyCite + Scopus Q3 | Fallback — if the paper leans more toward AI/computing than fisheries | ~3–4 months |

### Timeline

| Milestone | Target date |
|-----------|-------------|
| Design case study / domain instantiation | Jun – Aug 2027 |
| Collect or compile Malaysian environmental data | Sep – Oct 2027 |
| Draft manuscript with domain-specific examples | Nov – Dec 2027 |
| Internal review with supervisor | Jan 2028 |
| Submit to Pertanika JTAS | Feb 2028 |
| Expected review cycle | Feb – Jun 2028 |
| Revision and resubmission | Jul 2028 |
| Expected acceptance | Mid – Late 2028 |

---

## Master Timeline

```
2026
  Apr–Jun    Finalise review protocol + comparison table
  Jul–Sep    Draft Paper 1 (systematic review)
  Oct        Supervisor review
  Nov        Submit Paper 1 → Safety Science
  Dec–Jan    Finalise formal model (Appendix C)

2027
  Feb–Apr    Draft Paper 2 (formal architecture)
  May        Supervisor review
  Jun        Submit Paper 2 → Expert Systems with Applications
  Mid 2027   Paper 1 accepted (estimated)
  Jun–Aug    Design Paper 3 case study
  Sep–Oct    Compile Malaysian domain data
  Nov–Dec    Draft Paper 3 (domain application)

2028
  Jan        Supervisor review
  Feb        Submit Paper 3 → Pertanika JTAS
  Late 2027– Paper 2 accepted (estimated)
  Early 2028
  Mid 2028   Paper 3 accepted (estimated)

2028–2029
  Compile dissertation chapters from published work
  Viva preparation
  2029       Graduation
```

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Paper 1 rejected at Safety Science | Resubmit to Artificial Intelligence Review or AI & Ethics within 2 weeks |
| Paper 2 rejected at Expert Systems | Resubmit to Decision Support Systems or Journal of Systems and Software |
| Paper 3 rejected at Pertanika JTAS | Resubmit to Pertanika JST or Malaysian Journal of Computer Science |
| Review cycles longer than expected | 6-month buffer built into the 2029 graduation target |
| Formal proofs need strengthening | Address during Dec 2026 – Jan 2027 dedicated formalisation period |
| Domain data difficult to compile | Use publicly available MetMalaysia data + published fisher studies as secondary sources |

---

## Graduation Checklist

- [ ] Paper 1 published in Scopus-indexed journal (high-indexed requirement)
- [ ] Paper 3 published in MyCite-indexed journal (MyCite requirement)
- [ ] Paper 2 published in Scopus-indexed journal (exceeds minimum — strengthens dissertation)
- [ ] All dissertation chapters written and integrated
- [ ] Viva completed

---

## Notes

- Paper 1 and Paper 2 together satisfy the high-indexed requirement. Either one is sufficient, but both provide a stronger publication record.
- Paper 3 satisfies the MyCite requirement. Pertanika journals are both MyCite and Scopus-indexed, providing dual recognition.
- The 3-paper strategy provides redundancy: even if one paper faces delays, the minimum 2-paper requirement can still be met on time.
- All timelines include buffer for one round of major revision per paper.
