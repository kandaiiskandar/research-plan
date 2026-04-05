# Literature Review Extraction: Bossier et al. (2025)

---

## 1. Paper Identity

- **Title:** How much time and who will do it? Organizing the toolbox of climate adaptations for small-scale fisheries
- **Authors:** Sieme Bossier, Yoshitaka Ota, Ana Lucía Pozas-Franco, Andrés M. Cisneros-Montemayor
- **Year:** 2025
- **Venue:** *Frontiers in Marine Science*, 12:1521526
- **DOI:** 10.3389/fmars.2025.1521526
- **Type:** Original research (literature review + framework development + participatory case study)

---

## 2. Core Contribution

- **Problem addressed:** While many climate adaptation strategies have been proposed for small-scale fisheries (SSFs), there is a gap between adaptation theory and implementation. Existing research focuses on quantifying vulnerability (exposure, sensitivity, adaptive capacity) but rarely considers who bears the burden of implementation, how much time is needed, and what external support is required. Adaptation strategies proposed by outsiders often misalign with what fishers themselves consider important or feasible.
- **Proposed solution / key finding:** A two-part framework: (1) an **adaptation toolbox** organising strategies into five categories (Institutional, Communication, Livelihood, Risk Resilience, Science), adapted from the FAO climate adaptation framework; and (2) a **time-support framework** mapping each strategy along two axes — time required (short/long) and external support required (low/medium/high) — yielding five implementation categories (DIY, Ready-made, Delivered, Cooperative, System Change). The framework was tested via participatory exercise with octopus fishers in Yucatán, Mexico. Key finding: 75% of adaptation actions fishers considered important required high external support, whereas non-fishers assumed fishers could implement more on their own. Livelihood diversification — the most cited strategy in literature — was rated as not important by most fishers.
- **Main contributions:** (1) Five-category adaptation toolbox synthesised from 42 case studies across 46 global locations; (2) Time-support implementation framework; (3) Empirical evidence of mismatch between fisher-prioritised and externally-proposed adaptation strategies; (4) Participatory methodology for eliciting fisher perspectives on adaptation feasibility.
- **Novelty:** Shifts the focus from "what adaptations exist" to "who implements them, how long will it take, and what support is needed" — the implementation dimension of adaptation planning. The participatory validation with fishers reveals systematic mismatches between insider and outsider perceptions of adaptation feasibility.

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | **No** | No AI content |
| Safety-critical AI decision-making | **No** | No AI system; focuses on climate adaptation planning, not operational safety decisions |
| AI governance / control mechanisms | **No** | No AI governance; discusses institutional/policy governance of fisheries adaptation |
| Low-resource environments | **Partial** | Extensively documents resource constraints of SSFs: limited mobility, limited finances, dependence on catches for subsistence, limited capacity for technology adoption. Most case studies from developing countries. Explicitly addresses the burden distribution problem — who pays, who does the work |
| Decision architecture formalisation | **No** | The time-support framework is a 2D classification matrix, not a formal decision architecture |
| Human role in decision-making | **Partial** | Central theme: fishers must be active participants in adaptation decision-making, not passive recipients. Documents mismatch between what fishers want and what outsiders propose. Argues for co-management and participatory approaches |
| Socio-technical evaluation | **Partial** | The participatory exercise methodology (sticky notes, importance ranking, time/support scoring) with fishers in Yucatán is a practical example of co-evaluating adaptation tools with end users — methodologically relevant to socio-technical evaluation design |
| Coastal fisheries / maritime domain | **Yes** | Directly and comprehensively addresses small-scale coastal fisheries adaptation across 46 global locations, with a specific case study in Mexican octopus fisheries |

**Mid-Extraction Relevance Gate:** 1 Yes + 3 Partial → **REDUCED EXTRACTION** (Sections 4–7, 12–13, 16–17 only)

---

## 4. Decision Architecture Analysis

**No computational decision architecture.** The paper proposes a **classification framework** (the time-support matrix), not a decision system. The framework has two dimensions:

- **X-axis: External support required** (Low → Medium → High)
- **Y-axis: Time horizon** (Short → Long)

This produces five implementation categories:
1. **DIY** (low support, short time) — fishers implement themselves
2. **Ready-made** (medium support, short time) — existing tools with moderate help
3. **Delivered** (high support, short time) — externally provided quickly
4. **Cooperative** (medium support, long time) — requires trust-building and collaboration
5. **System Change** (high support, long time) — full institutional transformation

**Comparison to my architecture:** This framework operates at a completely different level of abstraction — it classifies *adaptation strategies* by implementation feasibility, not operational decisions by safety state. However, the underlying principle of **categorising actions into graduated tiers based on context-specific constraints** has a structural parallel to my architecture's graduated advisory scope A_AI(S). The paper's finding that a one-size-fits-all approach fails (fishers reject outsider-proposed strategies) conceptually supports the need for context-sensitive, graduated decision support.

No rule-based constraints, safety checks, fallback mechanisms, or override mechanisms.

---

## 5. Formal Model and Mathematical Representation

**None.** No formal model, no mathematical representation. The time-support framework is a qualitative 2D classification matrix. The participatory exercise uses ordinal scales (1–3 for time, 1–3 for support). Analysis is descriptive (percentage comparisons, importance rankings).

No comparison possible to the DSR pipeline **E → S = f(E) → (G(S), A_AI(S)) → AI(E)**. No state-dependent recommendation restriction. No Safety Dominance Property.

---

## 6. Safety State Classification

**Not applicable in the formal sense.** The paper does not classify operational or environmental conditions into discrete safety levels.

However, the five-category time-support framework (DIY, Ready-made, Delivered, Cooperative, System Change) is a form of **strategy classification by implementation feasibility** — which is conceptually adjacent to but distinct from safety state classification. The classification governs *which adaptation strategies are accessible* to fishers under different support conditions, somewhat analogous to how safety state governs which AI recommendations are admissible.

No thresholds, no dynamic classification, no state-conditioned scope restriction.

---

## 7. Governance Level Analysis

| Level | Question | Does this paper implement it? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI operate at all? | **No** | No AI system |
| **Level 2 — Advisory scope governance** | What may AI recommend? | **No** | No AI recommendations |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | N/A |

The paper discusses **institutional governance** of fisheries adaptation extensively — policies, regulations, external support, co-management, participatory decision-making — but this is human institutional governance, not AI governance. The paper's central concern (who has the power and resources to implement which strategies) is about **governance of adaptation implementation**, not governance of AI behaviour.

**Relevant observation:** The paper documents that institutional governance structures often fail fishers because they are top-down, disconnected from fisher priorities, and impose burdens disproportionately on the most vulnerable. This supports the broader argument that any AI decision support system deployed in this context must be designed *with* fishers, not *for* fishers — directly relevant to the socio-technical evaluation component of my research.

---

## 12. Key Concepts and Definitions

- **Time-support framework:** 2D matrix classifying adaptation strategies by time required (short/long) and external support required (low/medium/high), producing five implementation categories (DIY, Ready-made, Delivered, Cooperative, System Change)
- **Five adaptation categories:** Institutional (policies, regulations, external support), Communication (data generation, knowledge access, collective action, inclusivity), Livelihood (catch value, species/gear/livelihood switching, finance access), Risk Resilience (impact avoidance, well-being improvement), Science (models, technological innovation)
- **Fisher–outsider mismatch:** Systematic divergence between what fishers prioritise (healthcare, law enforcement, government material support) and what outsiders propose (livelihood diversification, gear changes, going further to sea). Fishers rated 75% of important actions as requiring high external support; non-fishers estimated only 49%.
- **Adaptation burden distribution:** The concept that costs and labour of adaptation are unevenly allocated, typically against fishers themselves — those with least capacity bear the most burden
- **Early warning systems as adaptation tools:** Identified under Risk Resilience → Avoiding Impacts category; noted as costly, time-consuming, requiring continuous updating and trained operators — placed in the "System Change" (high support, long time) category
- **Co-management:** Shared governance of fishery resources between government, communities, and other actors; identified as a key success factor for adaptation but requiring strong social capital

---

## 13. Limitations and Unsolved Problems

**Stated limitations:**
- Toolbox gathered via scoping review (not systematic review), so may not capture all proposed strategies
- Case study in Mexico had small sample size (13 participants across 7 groups) and was intended as a framework test, not an in-depth fishery analysis
- One participant answered yes to almost all tools due to desperation, potentially skewing results
- How much time and support a specific strategy requires is case-specific — the theoretical placement of strategies on the matrix is the authors' interpretation

**Unsolved problems / future work:**
- Need for in-depth implementation research: priority sequencing, funding sources, skills acquisition, responsibility allocation, monitoring and evaluation
- Lack of equity and justice perspectives in climate adaptation literature
- Need for more field applications of the framework in diverse contexts
- Need to understand synergies between adaptation strategies
- Early warning systems and technological innovations placed in "System Change" — requiring highest support and longest time — suggesting that technology-based solutions are the hardest to implement in SSF contexts

**Alignment with my research problem:**
- The paper does **not** identify an AI governance gap
- However, the identification of early warning systems and technological innovations as "System Change" (high support, long time) directly flags the **deployment challenge** my architecture faces: even well-designed AI decision support requires significant implementation infrastructure, training, and sustained support in SSF contexts
- The fisher–outsider mismatch finding is a cautionary signal for my socio-technical evaluation: the AI system I design may be perceived as an outsider-imposed solution unless co-developed with fishers
- The paper's emphasis on participatory methodology is directly relevant to how I should design my evaluation — eliciting fisher perspectives on the architecture's usefulness, not just validating it technically

---

## 16. Relation to My Research and Positioning

- **Level 1 governance:** Not implemented (no AI system)
- **Level 2 governance:** Not implemented
- **State-conditioned governance pair:** Not applicable
- **Formal safety property:** None defined
- **Gap my research addresses:** This paper organises adaptation strategies for SSFs but does not include AI-based decision support among its tools. The "Science" category mentions improved forecasting models and technological innovations but treats these as long-term, high-support "System Change" items — highlighting the implementation challenge rather than the architectural design challenge that my research addresses.

**Positioning paragraph:** This paper serves a dual role as **domain background** and **methodological reference** for my research. As domain background, it provides the most comprehensive taxonomy of climate adaptation strategies for SSFs available, documented across 46 global locations, and positions technology-based solutions (including early warning and forecasting) as the highest-cost, longest-timeline adaptation category — framing the challenge my architecture must overcome. More importantly, the paper's central finding — that adaptation strategies prioritised by fishers systematically diverge from those proposed by outsiders, and that 75% of fisher-important actions require external support — carries a direct design implication for my socio-technical evaluation: any AI decision support architecture must be validated through participatory methods that centre fisher perspectives, not just technical performance metrics. The time-support framework's emphasis on implementation feasibility (who pays, who does the work, how long does it take) provides a useful lens for evaluating the real-world deployability of my architecture in low-resource contexts. This paper is best positioned at the intersection of the **domain background** and **socio-technical evaluation methodology** subsections, and could be cited when discussing both the adaptation context that motivates AI decision support and the participatory evaluation principles that should govern its assessment.

---

## 17. Overall Relevance Score

### ⭐⭐ Low — with methodological utility

**Justification:** The paper contains no AI content, no decision architecture, no formal models, and no safety governance mechanisms. It operates entirely in the adaptation policy domain. However, it surpasses typical ⭐⭐ domain background papers in two specific ways: (1) it provides the broadest available taxonomy of SSF adaptation strategies, contextualising where technology-based decision support fits within the adaptation landscape (and flagging its implementation difficulty); and (2) the participatory methodology and the fisher–outsider mismatch finding carry direct implications for the socio-technical evaluation design of my architecture. The paper provides citable support for the argument that AI systems for SSFs must be co-evaluated with fishers and designed for low-support, short-timeline deployment to avoid becoming "System Change" items that never materialise.
