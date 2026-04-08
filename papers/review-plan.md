# Literature Review Plan

**Date**: 2026-04-06
**Papers analysed**: 66 (31 full extraction, 27 reduced extraction, 6 methodological foundation, 0 early stop)

---

## 1. Theme Gap Analysis

### Theme Coverage Summary

| Theme | Code | Yes | Partial | No | Coverage |
|-------|------|-----|---------|-----|----------|
| Hybrid AI (rule-based + probabilistic) | T1 | 17 | 21 | 25 | Well-Covered |
| Safety-critical AI decision systems | T2 | 32 | 15 | 16 | Well-Covered |
| AI governance (Level 1 + Level 2) | T3 | 27 | 18 | 18 | Well-Covered |
| Low-resource environments | T4 | 6 | 16 | 41 | Partially Covered |
| Decision architecture formalisation | T5 | 9 | 23 | 31 | Partially Covered |
| Human role in AI-assisted decision-making | T6 | 26 | 27 | 10 | Well-Covered |
| Socio-technical evaluation | T7 | 15 | 23 | 25 | Partially Covered |
| Coastal fisheries / maritime domain | T8 | 14 | 4 | 45 | **Well-Covered** |

### T1: Hybrid AI — Well-Covered

**Key papers (Yes)**: SYNAPSE (Castagnone) [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md), Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md), Punzi [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md), AgentSpec (Wang) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), Bloomfield/Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), SAFEXPLAIN (Abella) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md), Shields (Könighofer) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), Kalmykov [[notes]](../notes/Towards%20eXplicitly%20eXplainable%20Artificial%20Intelligence.md), Yuzui/Kaneko [[notes]](../notes/Toward%20a%20hybrid%20approach%20for%20the%20risk%20analysis%20of%20maritime%20autonomous%20surface%20ships-%20a%20systematic%20review.md), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (verification-guided shielding), SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (shielded RL review)

**Key papers (Partial)**: Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md), Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md), Leppinen [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md), Haque [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md), Bello [[notes]](../notes/Are%20We%20Regulating%20the%20Right%20Digital%20Systems%3F%20Testing%20Emerging%20Artificial%20Intelligence%20Frameworks%20against%20Real-World%20Public%20Sector%20Systems.md), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), Talpur [[notes]](../notes/AI%20in%20Maritime%20Security-%20Applications%2C%20Challenges%2C%20Future%20Directions%2C%20and%20Key%20Data%20Sources.md), Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md), Pitale [[notes]](../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md), Porter [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Wen [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md), Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md), Li [[notes]](../notes/Safety-Enhanced%20Deep%20Reinforcement%20Learning%20for%20Autonomous%20Driving-%20Dare%20to%20Make%20Mistakes%20to%20Learn%20Better%20and%20Faster.md), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md), Vermaelen [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md), Katende [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md)

**Assessment**: Strong coverage across neuro-symbolic, supervisory control, and governance-based hybrid architectures. Sufficient to establish that hybrid AI is well-studied but none implement two-level governance.

### T2: Safety-critical AI — Well-Covered

**Key papers (Yes)**: Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), SAFEXPLAIN [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md), Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md), Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md), Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Wen [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md), Pitale [[notes]](../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md), Abella [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md), Vermaelen [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md), Selvam [[notes]](../notes/Artificial%20Intelligence%20in%20Process%20Safety-%20A%20Review%20of%20Opportunities%2C%20Challenges%2C%20and%20Future%20Directions%20for%20the%20Chemical%20Process%20Industries.md), Leppinen [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md), Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) (HAII SLR), Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) (*Science*), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (verification-guided shielding), SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (shielded RL review)

**Assessment**: Extensive coverage — now 32 Yes papers. The strongest theme in the set. Establishes binary governance as the universal paradigm. The 3 new shielding papers (Corsi, SHIELDAGENT, Odriozola-Olalde) further confirm that all formal safety mechanisms implement binary governance.

### T3: AI Governance — Well-Covered

**Key papers (Yes)**: AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), SAFEXPLAIN [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md), Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md), Intl AI Safety Report (Bengio) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Bello [[notes]](../notes/Are%20We%20Regulating%20the%20Right%20Digital%20Systems%3F%20Testing%20Emerging%20Artificial%20Intelligence%20Frameworks%20against%20Real-World%20Public%20Sector%20Systems.md), Selvam [[notes]](../notes/Artificial%20Intelligence%20in%20Process%20Safety-%20A%20Review%20of%20Opportunities%2C%20Challenges%2C%20and%20Future%20Directions%20for%20the%20Chemical%20Process%20Industries.md), Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md), Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md), INSYTE (Porter) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md), SYNAPSE (Castagnone) [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), Vermaelen [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md), Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md), Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) (*Science* — policy-level governance), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (region-selective shielding), SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (per-action LTL guardrail), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (shielded RL review), **Attard-Frost & Lyons** [[notes]](../notes/AI%20governance%20systems-%20A%20multi-scale%20analysis%20framework%2C%20empirical%20findings%2C%20and%20future%20directions.%20AI%20and%20Ethics.md) (610-topic empirical mapping of national AI governance — zero runtime state-conditioned concepts; guardrails appear only in binary framing)
**Key papers (Partial)**: Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) (4-role taxonomy implies decision authority allocation but no runtime governance)

**Assessment**: Strong coverage — now 28 Yes papers. Critically, ALL implement Level 1 only or static Level 2. No paper implements state-conditioned two-level governance. Attard-Frost & Lyons (2025) provides the strongest empirical confirmation at the institutional layer: a 610-topic mapping of Canada's national AI governance system contains zero references to runtime state-conditioned advisory scope restriction, and governance practitioners frame guardrails exclusively in binary terms. This theme is well-covered precisely because it establishes the gap.

### T4: Low-resource environments — Partially Covered

**Key papers (Yes)**: Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md), Zhao/Yuan [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md), Peskas (Longobardi) [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md), Katende [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md), Tahsin [[notes]](../notes/Towards%20the%20adoption%20of%20AI%2C%20IoT%2C%20and%20Blockchain%20technologies%20in%20Bangladesh%27s%20maritime%20industry-%20Challenges%20and%20insights.md), Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md)
**Key papers (Partial)**: Haque/Al Jufaili [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md), Stage-Gate (Leppinen) [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md), Talpur [[notes]](../notes/AI%20in%20Maritime%20Security-%20Applications%2C%20Challenges%2C%20Future%20Directions%2C%20and%20Key%20Data%20Sources.md), Wing/Woodward [[notes]](../notes/Advancing%20artificial%20intelligence%20in%20fisheries%20requires%20novel%20cross-sector%20collaborations.md), Bossier [[notes]](../notes/How%20much%20time%20and%20who%20will%20do%20it%3F%20Organizing%20the%20toolbox%20of%20climate%20adaptations%20for%20small-scale%20fisheries.md), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), Obi [[notes]](../notes/Overview%20of%20the%20fishery%20and%20aquaculture%20sectors%20in%20Malaysia.md), Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md), Kühn [[notes]](../notes/Machine%20Learning%20Applications%20for%20Fisheries%E2%80%94At%20Scales%20from%20Genomics%20to%20Ecosystems.md), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (runtime efficiency for embedded systems), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (shielding's minimal computational overhead)

**Assessment**: 6 Yes papers cover healthcare, fisheries data platforms, general low-resource AI, and the target population's resource constraints. Yamin et al. (2025) provides the strongest characterisation: half of Terengganu fishers earn <RM 1,000/month, 60% have lower secondary education or below, and technology access is limited to weather apps. But no paper combines low-resource deployment with formal safety governance. Gap exists between the low-resource AI literature and the safety governance literature.

**Search suggestions**:
- "AI deployment resource-constrained safety-critical" in healthcare, disaster response
- "Edge AI safety governance" or "offline-capable decision support systems"
- Maritime/fisheries AI with explicit resource constraint discussion

### T5: Decision architecture formalisation — Partially Covered

**Key papers (Yes)**: AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md), Vermaelen [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (DNN verification problem + LTL shield synthesis + SMT encoding), SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (ASPM + LTL + Markov Logic Network + barrier certificate)
**Key papers (Partial)**: 23 papers with partial formalisation including Castagnone [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md), Leppinen [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md), Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md), Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md), Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md), Punzi [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md), Porter [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), Abella [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md), Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md), Li [[notes]](../notes/Safety-Enhanced%20Deep%20Reinforcement%20Learning%20for%20Autonomous%20Driving-%20Dare%20to%20Make%20Mistakes%20to%20Learn%20Better%20and%20Faster.md), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), Dalrymple, Kalmykov [[notes]](../notes/Towards%20eXplicitly%20eXplainable%20Artificial%20Intelligence.md), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (CMDP formulation, safe policy subspace Γ ⊆ Π)

**Assessment**: 9 Yes papers provide strong formal models but all use binary safety boundaries. Corsi and SHIELDAGENT add sophisticated formal verification (DNN verification, LTL+MLN) but both implement binary governance. Odriozola-Olalde's CMDP formulation covers all shielded RL methods — all binary. No formal model implements tripartite state classification (SAFE/CAUTION/UNSAFE) with graduated recommendation scope. Baxi is closest (K-tier graduated permissions with containment) but conditioned on robustness, not environmental state.

### T6: Human role — Well-Covered

**Key papers (Yes)**: 26 papers including Punzi [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md) (hybrid decision-making taxonomy), Gabriel [[notes]](../notes/Requirements%20Analysis%20for%20an%20Intelligent%20Workforce%20Planning%20System-%20A%20Socio-Technical%20Approach%20to%20Design%20AI-Based%20Systems.md) (socio-technical requirements), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md), Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), INSYTE [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md), Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md), Zhao/Yuan [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), McGrath S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md), McGrath CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md), Bach [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md), Aquilino [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Wen [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md), Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md), Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) (7-factor HAII model, 4-role taxonomy of AI decision authority)
**Key papers (Partial)**: Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) (human oversight of autonomous systems), SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (user-adjustable threshold but no human in runtime loop)

**Assessment**: Well-covered. Bach/Kristiansen et al. (2024) adds the most comprehensive empirical review of human-AI interaction in safety-critical industries (24 studies, 7 influencing factors). Yamin et al. (2025) adds the target population's traditional knowledge as a decision-making framework and documents fishers as active decision agents whose forecasting abilities are declining. Establishes that human-AI decision support is the dominant paradigm. No paper evaluates user response to a system with three distinct governance states.

### T7: Socio-technical evaluation — Partially Covered

**Key papers (Yes)**: Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md), Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), Zhao/Yuan [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md), Gabriel [[notes]](../notes/Requirements%20Analysis%20for%20an%20Intelligent%20Workforce%20Planning%20System-%20A%20Socio-Technical%20Approach%20to%20Design%20AI-Based%20Systems.md), Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md), INSYTE [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md), Intl AI Safety Report (Bengio) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Bach [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md), Aquilino [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md), McGrath S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md), McGrath CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md), Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md), Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) (measurement methods for HAII, TRL assessment of AI system maturity)
**Key papers (Partial)**: Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md), Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) (societal-scale risk assessment and sociotechnical governance need)

**Assessment**: Several papers address socio-technical considerations but few conduct empirical socio-technical evaluation of AI governance architectures. Yamin et al. (2025) provides the strongest socio-technical characterisation of the target population: five-domain adaptive capacity assessment, governance frustration (fishers feel neglected by government), religious worldview (93.4% Qadr attribution), and questionnaire instrument precedent (α = 0.914). No paper evaluates user understanding of graduated AI participation modes, particularly the CAUTION state.

**Search suggestions**:
- "Trust in AI decision support" with empirical user studies
- "User perception AI automation levels" in safety-critical domains
- "Socio-technical evaluation AI governance" empirical studies

### T8: Coastal fisheries / maritime — Well-Covered

**Key papers (Yes)**: Haque/Al Jufaili [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md), Wing/Woodward [[notes]](../notes/Advancing%20artificial%20intelligence%20in%20fisheries%20requires%20novel%20cross-sector%20collaborations.md), Yuzui/Kaneko [[notes]](../notes/Toward%20a%20hybrid%20approach%20for%20the%20risk%20analysis%20of%20maritime%20autonomous%20surface%20ships-%20a%20systematic%20review.md), Welch [[notes]](../notes/Harnessing%20AI%20to%20map%20global%20fishing%20vessel%20activity.md), Bossier [[notes]](../notes/How%20much%20time%20and%20who%20will%20do%20it%3F%20Organizing%20the%20toolbox%20of%20climate%20adaptations%20for%20small-scale%20fisheries.md), Peskas (Longobardi) [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md), Mandal [[notes]](../notes/The%20Significance%20of%20Artificial%20Intelligence%20(AI)%20in%20Fishing%20Crafts%20and%20Gears.md), Obi [[notes]](../notes/Overview%20of%20the%20fishery%20and%20aquaculture%20sectors%20in%20Malaysia.md), Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), Kühn [[notes]](../notes/Machine%20Learning%20Applications%20for%20Fisheries%E2%80%94At%20Scales%20from%20Genomics%20to%20Ecosystems.md), Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md), Shaffril [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md), Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md), Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md), Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md)
**Key papers (Partial)**: Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), Talpur [[notes]](../notes/AI%20in%20Maritime%20Security-%20Applications%2C%20Challenges%2C%20Future%20Directions%2C%20and%20Key%20Data%20Sources.md)

**Assessment**: 16 fisheries/maritime papers (up from 14), now including Yamin et al. (2025) — the strongest primary empirical study of the exact target population (n=136, Terengganu SSF, Q1 journal, 2023 fieldwork) — and two new empirical papers: Atacan & Düzbastılar (2023), providing simulator-based risk perception data from small-scale fishing vessel captains that directly justifies the t (time of day) variable in E and supports max-severity aggregation; and Dominguez-Péry et al. (2023), providing IMO accident report analysis (504 reports, 2011–2021) confirming that external environmental factors including visibility (captured via time of day) constitute the largest single risk cluster and that small vessels face the highest fatality rates. Yamin supersedes Shaffril et al. (2017) as the primary domain characterisation source. Muhamad et al. (2024) provides temporal continuity. NONE of the domain papers implement any AI governance mechanism — the domain is established as a context lacking formal AI safety governance, which is the motivation for PS3.

---

## 2. Problem Statement Coverage

| Problem Statement | Coverage | Key comparators found | Key gaps |
|---|---|---|---|
| PS1: No intermediate AI participation mode | Well-Supported | Shields, AgentSpec, Dalrymple, Bajcsy, Flehmig, Baxi | Flehmig is named comparator — present in set |
| PS2: No environment-state-conditioned (G(S), A_AI(S)) | Well-Supported | Shields, Bajcsy, Baxi, Shamsujjoha, AgentSpec | All implement binary or differently-conditioned governance |
| PS3: No safety governance for low-resource fisheries | Partially Supported | Bhuvaneswari (healthcare analog), Peskas, Haque, Yamin, Gao, Rahim | No paper combines governance + fisheries; domain context now strongly established |
| PS4: No graduated vs binary comparative evaluation | Partially Supported | McGrath S-TIAS, Schrills, CHAI-T, Bach, Aquilino, Atf & Lewis, Yamin | No direct evaluation of graduated vs binary governance — methodological foundation + domain outcome variable (flexibility) established |
| PS5: No socio-technical evaluation of CAUTION mode | Partially Supported | McGrath S-TIAS, Schrills, CHAI-T, Bach, Aquilino, Atf & Lewis, Yamin | No user study of intermediate governance mode — instruments, trust frameworks, and target population socio-technical context now in set |

### PS1: No architecture formally defines an intermediate AI participation mode with restricted recommendation space

**Coverage: Well-Supported**

| Paper | Role | How it relates |
|-------|------|----------------|
| Shields (Könighofer) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | Comparator | Per-state safe action sets but no discrete governance modes or recommendation-type restriction |
| AgentSpec (Wang) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | Comparator | Per-action binary enforcement; no global state classification |
| Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | Comparator | Policy-level binary verification; no graduated modes |
| Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | Comparator | Binary permit/override via safety filter; most rigorous but no CAUTION mode |
| Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) | **Primary comparator** | Three-level traffic-light model — closest prior art. But governs monitoring intensity, not AI recommendation scope; triggered by AI performance, not environmental state |
| Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | Comparator | K-tier graduated permissions with containment — structurally parallel but conditioned on robustness, not environmental state |
| Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) | Establishes gap | Survey of all industrial/transport domains — binary governance universal |
| Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) | Establishes gap | SLR of 46 formal methods papers — all binary safety boundaries |
| Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) | Establishes gap | SLR of 91 collaborative intelligence papers — all binary |
| Intl AI Safety Report (Bengio) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) | Establishes gap | All 11 Frontier AI Safety Frameworks implement binary participation control |
| Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | Comparator | Region-selective binary shield — partitions input space into safe/unsafe with selective activation, but no intermediate governance mode |
| SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | Comparator | Per-action policy-conditioned guardrail with LTL + probabilistic logic; binary safe/unsafe labels per action, no intermediate mode |
| Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | Establishes gap | Review of all shielded RL methods — all implement binary shield gate (Safety Levels I/II/III refer to constraint strength, not governance graduation) |

**Assessment**: Strong. The gap is convincingly demonstrated across multiple surveys, the primary comparator (Flehmig) is in the set, and the 3 new shielding papers further confirm that all formal safety mechanisms implement binary governance — even sophisticated region-selective (Corsi) and policy-extraction (SHIELDAGENT) approaches.

### PS2: No architecture classifies environmental conditions into safety states that determine AI recommendation scope via (G(S), A_AI(S))

**Coverage: Well-Supported**

| Paper | Role | How it relates |
|-------|------|----------------|
| Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | Comparator | Per-state safe action sets via MDP — closest to A_AI(S) but not discrete modes |
| Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | Comparator | Continuous safety value function V(z^AI), not discrete environmental state classification |
| Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | Comparator | Discrete robustness tiers with nested permissions — formally closest but conditioned on agent properties, not environment |
| Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | Comparator | World model captures environment but verifier produces binary pass/fail, not tripartite classification |
| Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) | Comparator | Most comprehensive Level 2 taxonomy (13 guardrail actions) but not state-conditioned |
| AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | Comparator | Per-action rule enforcement; no global environmental state classifier |
| Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) | Motivates | Maritime AI already classifies risk into discrete levels for display — but not for governance |
| Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | Comparator | Binary partition of input space by DNN verification — not environmental state classification; region categories are safe/unsafe, not SAFE/CAUTION/UNSAFE |
| SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | Comparator | Governance is policy-conditioned (static rules from documents), not environmental-state-conditioned; same rules apply regardless of environmental state |

**Assessment**: Strong. Multiple comparators show individual components exist (state classification, action restriction, gate functions) but none unifies them in a state-conditioned governance pair. Corsi and SHIELDAGENT add further confirmation: even the most sophisticated recent shielding and guardrail architectures do not condition governance on classified environmental state.

### PS3: No safety governance architecture designed for low-resource fisheries environments

**Coverage: Partially Supported**

| Paper | Role | How it relates |
|-------|------|----------------|
| Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) | Analog comparator | Hybrid AI for resource-constrained healthcare — closest domain analog but no governance architecture |
| Haque/Al Jufaili [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md) | Establishes gap | Surveys fisheries AI — no governance, no safety architecture |
| Peskas (Longobardi) [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md) | Establishes gap | Demonstrates feasibility of automated fisheries data in low-resource settings but no decision support or governance |
| Katende [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) | Fills background | Strongest characterisation of low-resource AI constraints |
| Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) | Motivates | Documents fisher decision-making in Penang — informal go/cautious-go/don't-go maps to SAFE/CAUTION/UNSAFE |
| Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) | Motivates | Fisher survival decisions under extreme weather — validates CAUTION concept |
| Obi [[notes]](../notes/Overview%20of%20the%20fishery%20and%20aquaculture%20sectors%20in%20Malaysia.md) | Fills background | Malaysian fisheries sector overview |
| Wing/Woodward [[notes]](../notes/Advancing%20artificial%20intelligence%20in%20fisheries%20requires%20novel%20cross-sector%20collaborations.md) | Fills background | Fisheries AI ecosystem needs |
| **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | **Primary motivator** | Strongest primary data from exact target population (n=136, Terengganu, Q1 journal); documents binary go/no-go status quo, flexibility as weakest adaptive capacity domain, TK erosion creating decision support vacuum; establishes PS3 motivation that CAUTION mode addresses a measured population-level capability gap |
| Shaffril [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) | Background | Historical domain characterisation (2017) — Malaysian SSF population profile, binary cessation during monsoon; retained as contextual background |
| Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) | Supplementary | Temporal continuity — confirms environmental factors remain significant productivity determinants in Malaysian SSF as recently as 2024 |
| Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | **Motivates** | Provides empirical risk data from small-scale fishing vessel captains (n=30, simulator study) confirming nighttime and restricted visibility as primary hazards; night navigation elevates accident probability (mean 4.08 vs 3.43 calm) and consequence (mean 12.80 vs 8.53); proactive risk assessment framing ("if precautions cannot reduce probability, the cruise should be cancelled") maps onto G(S) = 0 at UNSAFE |
| Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md) | Fills background | IMO accident evidence (504 reports) that small vessels (≤2,000 GT) face highest fatality risk (ANOVA p=0.01, mean rank 3.67 vs 1.02 for large vessels); external environmental factors including visibility are the largest risk cluster (26.7% of text segments); multi-variable risk approach supported |

**Assessment**: Partial but significantly strengthened. Domain background is now the strongest in the corpus with Yamin et al. (2025) providing primary empirical data from the exact target population. The gap (no formal governance in fisheries) is easy to argue. There are still no close architectural comparators within fisheries — the argument relies on cross-domain comparison (safety governance from other domains + fisheries deployment context). The domain motivation is now well-grounded.

### PS4: No comparative evaluation of graduated two-level governance vs binary governance

**Coverage: Partially Supported (updated — 6 methodological foundation papers added)**

No paper directly compares graduated vs binary governance. However, 6 new methodological foundation papers now provide the theoretical and empirical grounding for the evaluation design:

| Paper | Role | What it provides |
|-------|------|-----------------|
| McGrath et al. (2025) — S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md) | Primary instrument | Validated 3-item trust scale (S-TIAS) directly adoptable as primary trust measure across all three PS4 conditions; provides trust calibration framework defining "better" as expectation–capability alignment |
| Schrills et al. (2025) — Questioning Trust [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) | Methodological design | Demonstrates trust and behavioural dependence are distinct constructs; provides behavioural dependence metric (Cohen's Kappa); establishes dual-measurement design (attitudinal + behavioural); sample size benchmark: N=150 for 80% power |
| McGrath et al. (2025) — CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) | Evaluation criterion | Trust calibration as the evaluative criterion — graduated governance should produce better calibration than binary; defines overtrust/undertrust as calibration failures, providing PS4's dependent variable vocabulary |
| Bach et al. (2024) — User Trust SLR [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) | Instrument guidance | Recommends validated cross-context instruments (Jian et al. 2000; Gulati et al. 2019) over custom questionnaires; sample size guidance (M=326.80 across 23 studies) |
| Aquilino et al. (2025) — Decoding Trust [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md) | Instrument selection | Cognitive vs affective trust framework; predicts cognitive trust dominates low-anthropomorphism decision support — supports S-TIAS selection |
| Atf & Lewis (2026) — Explainability Meta-analysis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) | Benchmark | r = 0.194 explainability–trust correlation as baseline; PS4 can test whether graduated governance exceeds this baseline |

| Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | Motivates | Flexibility is weakest adaptive capacity domain — PS4 should test whether graduated governance improves fishers' operational flexibility under intermediate risk, not just architectural compliance; binary go/no-go confirmed as sole decision mode in target population |
| Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) | Fills background | 7-factor HAII model provides evaluation framework for PS4; TRL assessment methodology relevant to maturity evaluation; finding that AI-assisted decision-making dominates (16/24 articles) establishes the decision support context |

**What's still missing**: No paper compares graduated vs binary governance specifically. The three-condition design (ungated vs binary-gated vs two-level graduated) remains novel. But the evaluation methodology is now grounded and Yamin et al. (2025) provides the outcome variable motivation: flexibility deficit as a measurable population characteristic that graduated governance should address.

**Status rationale**: Moved from "Unsupported" to "Partially Supported" — methodological foundations established and domain outcome variable (flexibility) identified; direct evaluation precedent still absent.

### PS5: No socio-technical evaluation of graduated AI governance, particularly user response to CAUTION mode

**Coverage: Partially Supported (updated — 6 methodological foundation papers added)**

No paper evaluates user response to graduated AI participation modes. However, 6 new papers now provide the conceptual and instrumental foundations:

| Paper | Role | What it provides |
|-------|------|-----------------|
| McGrath et al. (2025) — S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md) | Primary instrument | Validated S-TIAS for measuring trust across governance states; highlights that performance-lens perception of restriction (CAUTION mode as "unreliability" vs "governance") is a key PS5 measurement challenge |
| Schrills et al. (2025) — Questioning Trust [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) | Critical warning | Self-reported trust has only moderate correlation with behavioural dependence (r = 0.42–0.45); instructed reliability (i.e., communicated governance state) strongly shapes behaviour; PS5 must measure both attitudinal trust and behavioural reliance independently |
| McGrath et al. (2025) — CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) | Trust dynamics framework | Temporal trust dynamics across collaboration episodes; predicts trust from SAFE mode episodes will be miscalibrated for CAUTION mode — a testable PS5 hypothesis; tripartite antecedents (human, technology, context) structure PS5's evaluation dimensions |
| Bach et al. (2024) — User Trust SLR [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) | Measurement catalogue | Three-factor taxonomy (socio-ethical, technical/design, user characteristics); recommends validated instruments (HCTS, TiA scale) over custom questionnaires; Malaysia context addresses geographic concentration gap |
| Aquilino et al. (2025) — Decoding Trust [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md) | Mode-specific trust prediction | CAUTION mode restriction changes system profile → shifts trust from mixed cognitive–affective to primarily cognitive; warns against using purely cognitive instrument in SAFE condition |
| Atf & Lewis (2026) — Explainability Meta-analysis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) | Design risk | Interpretable models can engender distrust as well as trust; making CAUTION restriction transparent may produce appropriate caution OR inappropriate distrust — PS5 must distinguish these outcomes |

| Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | **Primary PS5 context** | Governance frustration (fishers feel neglected by PNK/government — system must be perceived as fisher-empowering, not government-imposed); religious worldview (93.4% Qadr attribution — AI must be culturally compatible); learning willingness (72% agree they need to be progressive — adoption barrier may be lower than assumed); questionnaire instrument precedent (α = 0.914 — benchmark for PS5 instrument reliability in this population); Malay Terengganu dialect requirement and enumerator-administered design |
| Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) | Fills background | Measurement method catalogue for HAII in safety-critical industries (subjective and objective); finding that AI-assisted decision-making is the dominant AI role (16/24 articles) establishes PS5's decision support context; recommends involving target end-users throughout the AI lifecycle |

**What's still missing**: No paper evaluates user response to an *intermediate* governance mode ("AI active but restricted"). The CAUTION mode remains unmapped territory. PS5 is methodologically grounded and Yamin et al. (2025) provides the richest socio-technical context for the target population — but the specific contribution of evaluating the novel intermediate state has no direct precedent.

**Status rationale**: Moved from "Unsupported" to "Partially Supported" — validated instruments, trust dynamics frameworks, and target population socio-technical context established; evaluation of intermediate governance mode remains novel.

---

## 3. Governance Level Analysis

### Governance Level Distribution

| Paper | L1 (G(S)) | L2 (A_AI(S)) | Unified State-cond. | Type |
|-------|-----------|-------------|---------------------|------|
| Shields (Könighofer) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | Yes | Partial | Partial | Binary per-state |
| AgentSpec (Wang) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | Partial | No | No | Per-action binary |
| Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | Yes | Partial | No | Binary policy-level |
| Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | Yes | Partial | Partial | Binary (permit/override) |
| SAFEXPLAIN (Abella) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) | Yes | Partial | No | Binary runtime; graduated design-time |
| Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md) | Partial | No | No | Binary per-output |
| Shamsujjoha (Swiss Cheese) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) | Partial | Yes | No | Binary per-artifact; comprehensive L2 taxonomy |
| Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) | Yes | No | Partial | Binary; traffic-light governs monitoring only |
| Baxi (Comprehension-Gated) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | Yes | Yes | Yes* | Graduated K-tier (*robustness-conditioned, not environment) |
| Bloomfield/Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) | Yes | No | No | Binary (permit/override) |
| Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) | Yes | No | No | Binary across all domains |
| Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) | Yes | No | No | Binary (46 studies) |
| Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md) | Partial | Partial | No | Design-time graduated |
| INSYTE (Porter) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md) | Partial | No | No | Classification only |
| Intl AI Safety Report (Bengio) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) | Yes | No | No | Binary (all 11 frameworks) |
| Chen (AI Safety LLM) [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md) | Yes | Partial | No | Binary (guardrail system) |
| Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) | Yes | Partial | No | Binary (simplex switching) |
| Selvam [[notes]](../notes/Artificial%20Intelligence%20in%20Process%20Safety-%20A%20Review%20of%20Opportunities%2C%20Challenges%2C%20and%20Future%20Directions%20for%20the%20Chemical%20Process%20Industries.md) | Partial | Partial | No | Design-time static autonomy levels |
| Tumato (Vermaelen) [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) | Yes | No | No | Binary per-action |
| Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md) | Partial | No | No | Binary (design-time SIL) |
| Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md) | Partial | Partial | No | Organisational; post-generation |
| Castagnone (SYNAPSE) [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) | Partial | Partial | No | Binary output gating |
| Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) | Yes* | Partial* | Partial* | Informal only — empirical, not architecture |
| Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | Yes* | No | No | Informal binary gate ("if windy, I can't go fishing") — empirical, not architecture |
| Shaffril [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) | Yes* | No | No | Informal binary gate (90% operating day reduction during monsoon) — empirical, not architecture |
| Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) | No | No | No | No governance content — productivity factor validation only |
| Bach/Kristiansen (HAII SLR) [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) | Partial | No | No | Conceptual taxonomy — 4-role decision authority, not runtime governance |
| Bengio/Hinton 2024 (*Science*) [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) | Partial | Partial | No | Policy-level only — licensing, halting, autonomy restriction; not architectural runtime |
| Corsi (Verification-Guided Shielding) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | Yes | No | No | Binary region-selective — shield on/off by verified input region |
| SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | Yes | No | No | Per-action binary — LTL + MLN verification per action trajectory |
| Odriozola-Olalde (Shielded RL Review) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | Yes | No | No | Binary per-action — all reviewed shielding methods implement binary gate |
| Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | No | No | No | Empirical/domain — no governance mechanism; risk perception study of small-scale fishing vessel captains |
| Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md) | No | No | No | Empirical/domain — no governance mechanism; IMO accident report analysis |

### Summary

- **Level 1 only (binary gate)**: ~18 papers implement clear binary participation control (including Corsi, SHIELDAGENT, and all methods reviewed by Odriozola-Olalde)
- **Any form of Level 2**: ~12 papers restrict AI output scope in some form
- **Level 2 state-conditioned**: 2 papers — Shields (per-state action sets, continuous), Baxi (robustness-state tiers)
- **Unified two-level, environment-state-conditioned**: **0 papers**

**Gap confirmed**: No paper in the set implements both levels in a unified governance pair conditioned on classified environmental safety state. The 3 new shielding papers strengthen this finding: Corsi's region-selective activation is binary (shield on/off by verified region), SHIELDAGENT's per-action enforcement produces binary safe/unsafe labels from static policy rules, and Odriozola-Olalde's review confirms all shielded RL methods implement a binary gate. Baxi remains structurally closest (graduated tiers with containment) but conditions on agent robustness, not environmental state. Shields remains formally closest (per-state safe action sets) but does not define discrete governance modes or recommendation-type restriction.

---

## 4. Formal Component Coverage

| Formal Component | Papers that address it | Papers that come close | Gap? |
|---|---|---|---|
| Environmental state vector E | Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (z), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) (S, Omega), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) (world model), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (MDP state), Tumato [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) (state vars), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (input space partition — verification-derived, not environmental) | Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) (X_t input vector) | No — concept exists but not as E = {w,r,m,o,v,t} |
| Safety state classification S = f(E) | None (tripartite) | Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (safe/dangerous/unsafe partition), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (V(z^AI) continuous), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) (traffic-light) | **Yes** — no discrete tripartite classification of environmental state |
| Participation gate G(S) | Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (winning region), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (safety filter), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) (verifier), Tumato [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) (allowed predicate), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) (backup guard), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (region-selective shield), SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (per-action guardrail), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (all reviewed shields) | AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) (per-action), Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md) (per-output) | No — binary gate concept well-established; now confirmed across 18+ papers |
| AI-admissible recommendation space A_AI(S) | None (state-conditioned) | Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (per-state safe action sets — closest), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (nested permission tiers), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) (guardrail taxonomy) | **Yes** — no state-conditioned recommendation-type restriction |
| Containment: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ | None | Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (E(T_k) ⊂ E(T_{k+1}) — structurally identical property), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (inductive winning region) | **Yes** — no tripartite containment for recommendation types |
| Two-level governance pair (G(S), A_AI(S)) | None | Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (f(R), E(T_k)) — closest structural analog | **Yes** — core novel contribution |
| Safety Dominance Property: AI(E) ⊆ A_AI(S) | None (graduated) | Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (Theorem 1 — binary), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (never visit unsafe states — binary), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (bounded exposure — robustness-conditioned), Tumato [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) (soundness), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (CBFs — binary) | **Yes** — safety dominance for graduated governance is novel |

### Assessment

**Components with precedent (not novel)**:
- Environmental state representation (E) — well-established in multiple formalisms
- Participation gate (G(S)) — binary gate is universal

**Components with structural analogs but no direct precedent (partially novel)**:
- Safety state classification (S = f(E)) — Flehmig's traffic-light and Shields' state partition come closest but neither classifies environmental state into discrete governance-triggering modes

**Components with no precedent (novel contributions)**:
- State-conditioned recommendation space A_AI(S) with recommendation-type restriction
- Tripartite containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- Unified two-level governance pair (G(S), A_AI(S))
- Safety Dominance Property for graduated (non-binary) governance

---

## 5. Argumentative Chain

### Link 1: Safety-critical systems increasingly use AI
**Papers**: Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) (cross-domain survey), Intl AI Safety Report/Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) (global assessment), Bloomfield/Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) (dependability perspective), Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) (*Science* — high-authority call to action from 25 leading AI researchers on extreme AI risks)
**PS mapping**: Background
**Transition**: *"But AI in safety-critical contexts creates a governance problem: when should AI be allowed to participate, and what should it be allowed to recommend?"*

### Link 2: Hybrid AI combines deterministic rules with probabilistic reasoning
**Papers**: SYNAPSE/Castagnone [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) (neuro-symbolic), Punzi [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md) (hybrid taxonomy), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (rule-filtered RL), Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) (hybrid triage), Kalmykov [[notes]](../notes/Towards%20eXplicitly%20eXplainable%20Artificial%20Intelligence.md) (XXAI), Yuzui/Kaneko [[notes]](../notes/Toward%20a%20hybrid%20approach%20for%20the%20risk%20analysis%20of%20maritime%20autonomous%20surface%20ships-%20a%20systematic%20review.md) (hybrid risk analysis)
**PS mapping**: Background
**Transition**: *"But the boundary between deterministic safety control and probabilistic AI reasoning must itself be governed — raising the question of how AI participation is controlled."*

### Link 3: Existing governance is binary — AI on/off (Level 1 participation governance)
**Papers**: Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (winning region gate), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) (verifier gate), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (safety filter), SAFEXPLAIN [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) (supervision function), Bloomfield [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) (backup guard), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) (per-action enforcement), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) (binary across all domains), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (binary in all 46 studies), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) (binary in all 91 studies), Intl AI Safety Report/Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) (binary in all 11 frameworks), Tumato/Vermaelen [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) (binary allowed predicate), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (binary safe/unsafe region partition with selective shield activation), SHIELDAGENT/Chen/Kang/Li [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (per-action binary safe/unsafe labels from LTL + probabilistic logic), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (reviews all shielded RL methods — all implement binary gate)
**PS mapping**: PS1
**Transition**: *"Level 1 governance — whether AI operates at all — is well-established. But controlling what AI may recommend (Level 2) is a separate governance question."*

### Link 4: Some systems restrict AI output scope (Level 2), but statically
**Papers**: Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) (13 guardrail action types — most comprehensive Level 2 taxonomy), Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md) (guardrail system architecture), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) (per-action rules), Selvam [[notes]](../notes/Artificial%20Intelligence%20in%20Process%20Safety-%20A%20Review%20of%20Opportunities%2C%20Challenges%2C%20and%20Future%20Directions%20for%20the%20Chemical%20Process%20Industries.md) (four autonomy levels — design-time), SAFEXPLAIN [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) (DL usage levels — design-time), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md) (hierarchical action constraints — design-time), SHIELDAGENT/Chen/Kang/Li [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (per-action policy-conditioned LTL rule enforcement — rules extracted from static documents, not state-conditioned)
**PS mapping**: PS1, PS2
**Transition**: *"Level 2 governance exists — but it is applied per-action or configured at design-time, not conditioned on classified environmental safety state. No architecture dynamically adjusts AI advisory scope based on operational conditions."*

### Link 5: No architecture unifies both levels conditioned on environmental safety state
**Papers**: Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) (closest — traffic-light but governs monitoring intensity, not recommendation scope; triggered by AI performance, not environmental state), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (graduated tiers with containment but robustness-conditioned, not environment-conditioned), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (per-state safe actions but continuous, not discrete governance modes)
**PS mapping**: PS1, PS2
**Transition**: *"Flehmig et al. is the closest prior art: a three-level traffic-light governance model. But it is triggered by AI performance degradation, governs monitoring intensity rather than recommendation scope, and operates at a single governance level. No architecture implements both participation governance G(S) and advisory scope governance A_AI(S) as a unified pair conditioned on environmental safety state."*

### Link 6: No formal Safety Dominance Property for graduated governance
**Papers**: Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (Theorem 1 — binary), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (safety guarantee — binary), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (CBFs, reachability — binary), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (bounded exposure — robustness-conditioned), Tumato/Vermaelen [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) (soundness — binary)
**PS mapping**: PS2
**Transition**: *"Formal safety properties exist for binary governance (shields, safety filters, CBFs), but none defines a Safety Dominance Property for graduated governance where AI outputs must fall within a state-dependent recommendation space that narrows as risk increases."*

### Link 7: This gap matters in low-resource, safety-critical domains
**Papers**: Katende [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) (low-resource AI constraints), Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) (healthcare in resource-constrained settings), Haque/Al Jufaili [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md) (fisheries AI — no governance), Peskas/Longobardi [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md) (feasibility of fisheries data platforms), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) (fisher decision-making in Penang), Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) (fisher survival decisions under extreme weather), **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) (primary empirical data from target population — binary status quo, flexibility deficit, TK erosion, decision support vacuum), Shaffril [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) (historical domain characterisation), Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) (temporal continuity for environmental factors)
**PS mapping**: PS3
**Transition**: *"Small-scale coastal fisheries represent a safety-critical, low-resource domain where AI must operate under intermittent connectivity, limited data, and varying environmental risk — yet no formal safety governance architecture exists for this context. Yamin et al. (2025) confirm that fishers' traditional weather prediction abilities are declining while their reliance on weather apps grows, creating a decision support vacuum that no current system fills."*

### Link 8: No evaluation compares graduated vs binary governance
**Papers**: (Gap — no paper directly addresses this)
**PS mapping**: PS4
**Transition**: *"Existing evaluations compare gated versus ungated AI (does governance help at all?), but none isolates the contribution of Level 2 advisory scope governance beyond Level 1 participation governance — does the CAUTION mode add value beyond a binary gate?"*

### Link 9: No socio-technical evaluation of user response to CAUTION mode
**Papers**: (Gap — no paper directly addresses this)
**PS mapping**: PS5
**Transition**: *"Users have interacted with AI that is fully on or fully off, but never with a system that communicates 'AI is active but operating under restriction.' How users understand, trust, and respond to this intermediate state is unknown."*

---

## 6. Citation Chain

### Cluster 1: Safety Governance

```
Dalrymple (2024) "Guaranteed Safe AI" [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md)
    ├── cited by → Liang (2025) "Safeguarded AI" [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md) (implements as per-output gatekeeper)
    ├── cited by → Intl AI Safety Report/Bengio (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) (references as theoretical foundation)
    └── gap: binary verifier; no state-conditioned graduated governance
         └── USER'S CONTRIBUTION: state-conditioned two-level governance pair

Könighofer (2025) "Shields" [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md)
    └── gap: per-state safe action sets but no discrete modes or recommendation-type restriction
         └── USER'S CONTRIBUTION: discrete safety modes with recommendation-type restriction

Bajcsy/Fisac (2024) "Human-AI Safety" [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md)
    ├── cited by → Ramos (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) (as Fisac et al. for Bayesian prediction)
    └── gap: binary permit/override; no CAUTION mode
         └── USER'S CONTRIBUTION: graduated governance with CAUTION mode

Odriozola-Olalde (2023) "Shielded RL Review" [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md)
    ├── reviews → Alshiekh et al. (base shielded RL — foundational)
    ├── reviews → Hasanbeig et al. (probabilistic shield)
    └── gap: all reviewed methods implement binary shield gate
         └── Corsi (2024) "Verification-Guided Shielding" [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md)
              ├── extends → shielding with region-selective activation
              ├── uses → Marabou (formal verification framework)
              └── gap: binary safe/unsafe partition; no CAUTION mode
                   └── USER'S CONTRIBUTION: tripartite state classification with graduated scope
```

### Cluster 2: Guardrails & Runtime Enforcement

```
Shamsujjoha (2025) "Swiss Cheese Model" [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md)
    ├── cited by → Chen (2025) [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md) (references guardrail taxonomy)
    └── gap: comprehensive L2 taxonomy but no state-conditioned activation
         └── USER'S CONTRIBUTION: state-conditioned activation of L2 governance

AgentSpec (Wang 2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md)
    └── gap: per-action binary enforcement; no global environmental state classifier
         └── USER'S CONTRIBUTION: global state classification layer

SHIELDAGENT (Chen/Kang/Li 2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md)
    ├── extends → guardrail literature (LlamaGuard, GuardAgent)
    ├── uses → LTL + formal verification (Stormpy, Prover9)
    └── gap: per-action binary enforcement from static policy documents; no environmental state conditioning
         └── USER'S CONTRIBUTION: state-conditioned scope restriction
```

### Cluster 3: Safety-Critical AI Architecture

```
Perez-Cerrolaza (2024) "AI Safety-Critical Survey" [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)
    ├── shares authors with → SAFEXPLAIN (Abella 2025) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md)
    ├── cited by → Newcomb (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (in SLR)
    └── gap: binary governance universal across all industrial/transport domains

Flehmig (2024) "Implementing AI in SCS" [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md)
    ├── cited by → Newcomb (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (in SLR)
    └── gap: traffic-light governs monitoring, not recommendation scope
         └── USER'S CONTRIBUTION: traffic-light governs recommendation scope via A_AI(S)
```

### Cluster 4: Trust & Evaluation Methodology

```
McGrath et al. (2025) — S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md)
    ├── builds on → Bach et al. (2024) [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) (trust measurement SLR)
    ├── complemented by → McGrath et al. (2025) — CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) (trust calibration framework)
    └── Schrills et al. (2025) — Questioning Trust [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) (trust vs dependence distinction)
         └── triad: S-TIAS + CHAI-T + Schrills = evaluation methodology for PS4/PS5

Atf & Lewis (2026) — Explainability Meta-analysis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md)
    └── provides baseline: r = 0.194 (explainability–trust correlation)
         └── PS4 benchmark: can graduated governance exceed this baseline?

Aquilino et al. (2025) — Decoding Trust [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md)
    └── cognitive vs affective framework → mode-specific instrument selection for PS5
```

### Cluster 5: Fisheries/Maritime

```
Haque/Al Jufaili (2026) [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md) → Wing/Woodward (2024) [[notes]](../notes/Advancing%20artificial%20intelligence%20in%20fisheries%20requires%20novel%20cross-sector%20collaborations.md) → Kühn (2025) [[notes]](../notes/Machine%20Learning%20Applications%20for%20Fisheries%E2%80%94At%20Scales%20from%20Genomics%20to%20Ecosystems.md)
    (isolated cluster — no cross-citations with safety governance literature)
    └── gap: entire fisheries AI domain lacks governance architecture
         └── USER'S CONTRIBUTION: first formal governance architecture for fisheries

Welch (2024) [[notes]](../notes/Harnessing%20AI%20to%20map%20global%20fishing%20vessel%20activity.md) + Kühn (2025) [[notes]](../notes/Machine%20Learning%20Applications%20for%20Fisheries%E2%80%94At%20Scales%20from%20Genomics%20to%20Ecosystems.md) → shared Watson co-authorship
    └── small fisheries AI research community

Gao (2024) "Penang fisher decisions" [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md)
    └── empirical basis: documents go/cautious-go/don't-go → maps to SAFE/CAUTION/UNSAFE

Yamin (2025) "Terengganu fishers" [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) — supersedes Shaffril (2017) as primary domain source
    ├── cites → Shaffril et al. (2017) [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) (in secondary references for domain continuity)
    ├── cites → Noor et al. (2023) (rainfall classification for East Coast Malaysia)
    └── provides primary evidence: binary go/no-go, flexibility deficit, TK erosion
         └── USER'S CONTRIBUTION: CAUTION mode addresses measured adaptive capacity deficit

Shaffril (2017) "Malaysian SSF climate adaptation" [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) — historical background
    └── superseded by Yamin (2025) for population characterisation
    └── retained for: objective climate data (wind speed stations, rainfall percentiles)

Muhamad (2024) "SSF productivity factors" [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) — temporal continuity
    └── confirms environmental factors remain significant as of 2024
    └── fuzzy logic precedent for S = f(E) implementation
```

### Cluster 6: International Governance & Policy

```
Bengio, Hinton et al. (2024) — "Managing extreme AI risks" (Science) [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md)
    ├── preceded by → early AI governance calls
    ├── followed by → Bengio et al. (2026) International AI Safety Report [[notes]](../notes/International%20AI%20Safety%20Report%202026.md)
    └── advocates: capability-triggered institutional governance (if-then commitments)
         └── categorically distinct from: runtime environmental-state-conditioned architectural governance

Bengio et al. (2026) — International AI Safety Report [[notes]](../notes/International%20AI%20Safety%20Report%202026.md)
    ├── references → Dalrymple et al. [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) as theoretical foundation
    ├── builds on → Bengio/Hinton (2024) Science call to action [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md)
    ├── documents: 11 Frontier AI Safety Frameworks — all binary
    └── gap: no graduated governance in any international framework
```

### Citation Chain Summary

- **Foundational papers** (cited by others in set): Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) (2), Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (1), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)/SAFEXPLAIN [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) (shared authorship + 1 citation), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) (foundational review for shielding sub-cluster)
- **Recent extensions** (cite others in set): Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md), Intl AI Safety Report/Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md), Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) (extends guardrail literature), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) (extends shielding with region-selective activation), Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) (precedes Intl AI Safety Report)
- **Isolated** (no citation links): Most fisheries papers, most low-resource papers, HySAFE/Pitale [[notes]](../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md), Stage-Gate/Leppinen [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md), SYNAPSE/Castagnone [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md), Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md)
- **Entry points for user's contribution**: The safety governance cluster (Dalrymple → Liang lineage) breaks where binary governance is implemented — user's work extends this lineage with graduated governance. The shielding sub-cluster (Odriozola-Olalde → Corsi) breaks at the binary partition — user's work extends with tripartite state classification. The fisheries cluster has no connection to safety governance — user's work bridges these two disconnected bodies of literature.

---

## 7. Literature Review Outline

### Suggested Section Structure (Chapter 2 — 9 sections)

*Aligned with `improvement-plan/literature_review_improvement_plan-2.md`. The logical flow builds step-by-step toward the research gap: AI is used for decision support → safety constraints exist but govern actions not advisory scope → human-AI authority is contested → some systems adapt autonomy to risk but without formal advisory containment → governance and guardrails operate at policy level not runtime → hybrid AI focuses on accuracy not governance → low-resource environments add constraints → fisheries is the right domain → evaluation methodology is established → therefore a graduated safety-state-gated architecture is needed.*

---

#### Section 2.1: AI Decision Support in Safety-Critical Systems (Link 1)
**Purpose**: Establish that AI is increasingly used for decision support in safety-critical systems and that incorrect AI recommendations can have serious consequences.

| Paper | Role |
|-------|------|
| Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) | Fills background — cross-domain AI safety survey establishing scope |
| Intl AI Safety Report (Bengio) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) | Fills background — current global assessment of AI in critical systems |
| Bloomfield/Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) | Fills background — dependability and assurance perspective |
| Gabriel [[notes]](../notes/Requirements%20Analysis%20for%20an%20Intelligent%20Workforce%20Planning%20System-%20A%20Socio-Technical%20Approach%20to%20Design%20AI-Based%20Systems.md) | Fills background — socio-technical requirements for AI systems |
| Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) | Fills background — systematic review of 46 formal methods papers (scope of field) |
| Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) | Fills background — systematic review of 91 collaborative intelligence papers |
| Selvam [[notes]](../notes/Artificial%20Intelligence%20in%20Process%20Safety-%20A%20Review%20of%20Opportunities%2C%20Challenges%2C%20and%20Future%20Directions%20for%20the%20Chemical%20Process%20Industries.md) | Fills background — process safety AI in industrial context |
| Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) | Fills background — high-authority *Science* call to action from 25 leading AI researchers (incl. 2 Turing Award winners) on extreme AI risks and governance urgency |

**Key conclusion**: AI decision support improves decision quality but incorrect or poorly governed AI recommendations in safety-critical environments can lead to serious consequences. This motivates the need for formal governance of when and how AI participates.

**Transition**: *"AI decision support improves decision quality — but as AI moves into safety-critical environments, the question of how to constrain AI behaviour becomes critical. The first response in the literature has been deterministic safety constraints."*

---

#### Section 2.2: Deterministic Safety Constraints and Rule-Based Safety Systems (Links 2–3)
**Purpose**: Show how safety rules and constraints are used to prevent unsafe actions — and identify the key limitation: these systems block unsafe actions but do not restrict AI advisory reasoning scope.

| Paper | Role |
|-------|------|
| Shields (Könighofer) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | **Primary comparator** — formal binary shield, inductive winning region |
| AgentSpec (Wang) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | **Primary comparator** — per-action enforcement with soundness theorem |
| Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | **Comparator** — guaranteed safe AI via world model + binary verifier |
| Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | **Comparator** — Hamilton-Jacobi safety filter, binary permit/override |
| SAFEXPLAIN (Abella) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) | **Comparator** — supervision function, design-time DL usage levels |
| Liang [[notes]](../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md) | Fills background — per-output guardrail for LLM safety |
| Bloomfield/Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) | Fills background — safety case and assurance argument |
| Tumato (Vermaelen) [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) | **Comparator** — soundness by construction, binary allowed predicate |
| Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | **Comparator** — region-selective binary shielding combining offline DNN verification (Marabou) with online LTL shield; binary safe/unsafe partition |
| SHIELDAGENT (Chen/Kang/Li) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | **Comparator** — per-action LTL guardrail with probabilistic logic (Markov Logic Network); binary safe/unsafe labels from static policy documents |
| Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | Fills background — structured review confirming all shielded RL methods implement binary gate (Safety Levels I/II/III refer to constraint strength, not governance graduation) |
| Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) | Establishes gap — all 46 formal methods papers implement binary gate |

**Citation cluster**: Safety governance cluster (Dalrymple → Liang → Intl AI Safety) + Shielding sub-cluster (Odriozola-Olalde → Corsi)

**Key limitation**: These systems block unsafe actions at the participation level (Level 1 — AI on/off). They do not restrict AI advisory reasoning scope (Level 2 — what AI is allowed to recommend). Governance is binary: AI participates fully or not at all.

**Transition**: *"Safety constraints govern whether AI acts — but they do not govern what AI is allowed to recommend, or when AI should participate based on conditions. This raises a deeper question: how should decision authority be allocated between human and AI?"*

---

#### Section 2.3: Human–AI Decision Authority and Decision Support Systems (Link 3 continued)
**Purpose**: Discuss how decision authority is allocated between human and AI — and identify the limitation that these systems do not define when AI should participate based on safety conditions.

| Paper | Role |
|-------|------|
| Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md) | Fills background — socio-technical governance lens for decision authority |
| Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) | Fills background — collaborative intelligence taxonomy (91 papers) |
| INSYTE (Porter) [[notes]](../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md) | Fills background — AI system classification including governance dimensions |
| Leppinen [[notes]](../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md) | Fills background — stage-gate decision support in project contexts |
| Zhao/Yuan [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md) | Motivates — ethical question of varying governance by severity |
| Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) | Motivates — maritime AI transparency (risk display ≠ risk governance) |
| Bach/Kristiansen [[notes]](../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) | Fills background — 4-role taxonomy of AI decision authority in safety-critical industries (collaborative AI, AI-assisted decision-making, human-controlled AI, emotional AI); 7-factor HAII model; finding that AI-assisted decision-making dominates (16/24 articles) |

**Key limitation**: Human-in-the-loop and supervisory control frameworks define who decides, but do not specify when AI should participate based on environmental safety conditions. Decision authority is allocated at design time, not adapted to runtime risk.

**Transition**: *"If static authority allocation is insufficient, the natural next step is systems that adapt the level of autonomy or AI participation based on the risk or context at runtime."*

---

#### Section 2.4: Risk-Adaptive and Graduated Autonomy Systems (Links 4–5)
**Purpose**: Review systems that change autonomy level based on risk or context. This section contains the closest literature to the proposed architecture. Identify the key limitations: autonomy level changes but advisory scope is not formally restricted, no containment relationship between advisory capabilities, and governance functions are not formally defined.

| Paper | Role |
|-------|------|
| Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) | **Primary comparator** — traffic-light graduated governance (3-level), triggered by AI performance, governs monitoring intensity not recommendation scope |
| Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | **Structural comparator** — graduated K-tier permissions with formal containment (E(T_k) ⊂ E(T_{k+1})), but conditioned on agent robustness not environmental state |
| Shields (Könighofer) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | **Formal comparator** — per-state safe action sets, but continuous MDP states not discrete governance modes |
| Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) | Fills background — operational design domains and authority switching in automotive |
| Li [[notes]](../notes/Safety-Enhanced%20Deep%20Reinforcement%20Learning%20for%20Autonomous%20Driving-%20Dare%20to%20Make%20Mistakes%20to%20Learn%20Better%20and%20Faster.md) | Fills background — risk-adaptive autonomy in intelligent transport |
| Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md) | Highlights gap — design-time SIL assessment, not runtime graduated governance |

**Key limitations (why this section does not resolve the gap)**:
- Autonomy level changes exist (Flehmig: 3-level; Baxi: K-tier) — but advisory scope is not formally restricted
- No containment relationship between advisory capabilities across governance modes (A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ does not appear in any paper)
- Governance functions are not formally defined as a unified pair (G(S), A_AI(S))
- No architecture conditions both levels on classified environmental safety state simultaneously

**First-principles argument — why binary governance is structurally inadequate**:

Binary governance (Level 1 only) forces a false dilemma:
- **Over-restriction**: Disabling AI entirely under elevated but manageable conditions wastes a scarce resource — particularly costly in low-resource settings.
- **Under-restriction**: Permitting full AI participation under elevated risk exposes users to recommendations that assume conditions the system cannot reliably assess.

The CAUTION mode resolves this: AI remains active but advisory scope narrows to recommendation types that remain reliable under elevated conditions. This is a structurally distinct governance solution that binary governance cannot provide.

**Comparator summary** — key architectures across governance dimensions:

| Architecture | Governance trigger | Level | Mode | Runtime | Formal property |
|---|---|---|---|---|---|
| Shields (Könighofer) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | MDP state | L1 + partial L2 | Binary per-state | Yes | Inductive winning region |
| Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | World model | L1 only | Binary | Yes | Verifier pass/fail |
| Bajcsy/Fisac [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | System state z | L1 only | Binary | Yes | Theorem 1 (HJ reachability) |
| Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) | AI performance | L1 only | Graduated (3-level) | Yes | Weighted index threshold |
| Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | Agent robustness | L1 + L2 | Graduated (K-tier) | Design-time | Bounded exposure theorem |
| Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) | Per-artifact | Partial L1 + L2 | Binary per-layer | Yes | None (defence-in-depth) |
| AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | Per-action rule | L1 + partial L2 | Binary per-action | Yes | Soundness theorem |
| Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | Verification region | L1 only | Binary (region-selective) | Yes | DNN verification + LTL shield |
| SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | Per-action policy | L1 only | Binary per-action | Yes | LTL + MLN + barrier certificate |
| Odriozola-Olalde (review) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | Per-state/action | L1 only | Binary | Yes | CMDP + LTL (all reviewed methods) |
| **Proposed** | **Environmental state** | **L1 + L2 unified** | **Graduated (3-mode)** | **Yes** | **Safety Dominance Property** |

**Baxi differentiator — why conditioning variable matters architecturally**:

| Dimension | Environmental state (proposed) | Agent robustness (Baxi) |
|---|---|---|
| **Observation mechanism** | Real-time sensor inputs (weather, sea state, visibility) | Offline evaluation / benchmark testing |
| **Update frequency** | Continuous — reclassification occurs during operation | Static — tier assigned at deployment |
| **Governance response** | Immediate scope adjustment as conditions change | Tier persists; no real-time response |
| **Failure mode** | Wrong governance mode applied in real-time | Overestimation of robustness persists |
| **Applicability** | Dynamic environments with varying external risk | Controlled environments with stable agent properties |

**Forward reference**:
> *"The gap established above — no architecture implements both participation governance G(S) and advisory scope governance A_AI(S) as a unified pair conditioned on classified environmental safety state — motivates the two-level governance architecture proposed in this research. The formal pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) addresses this gap by classifying environmental conditions into discrete safety states that simultaneously determine whether AI may operate and what it may recommend."*

**Transition**: *"The graduated autonomy literature reveals the architectural gap clearly: systems change autonomy level but never formally restrict what AI is allowed to recommend, and no governance pair (G(S), A_AI(S)) is conditioned on classified environmental safety state. Before examining the domain and evaluation dimensions of this gap, two further bodies of literature require review: AI governance at the policy level, and hybrid AI as the enabling architecture."*

---

#### Section 2.5: AI Governance, Guardrails, and Safety Architectures (Link 3 continued)
**Purpose**: Introduce AI governance and guardrail concepts — and identify the limitation that most governance operates at policy or system level, not runtime decision architecture level.

| Paper | Role |
|-------|------|
| Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) | Fills background — most comprehensive guardrail taxonomy (Swiss cheese model) |
| Chen [[notes]](../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md) | Fills background — AI safety LLM landscape and guardrail architecture |
| Bello [[notes]](../notes/Are%20We%20Regulating%20the%20Right%20Digital%20Systems%3F%20Testing%20Emerging%20Artificial%20Intelligence%20Frameworks%20against%20Real-World%20Public%20Sector%20Systems.md) | Fills background — legal and regulatory AI governance frameworks |
| Intl AI Safety Report (Bengio) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) | Establishes gap — 11 frontier safety frameworks, all binary |
| Abella (SAFEXPLAIN) [[notes]](../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) | Highlights gap — supervision function defined at design-time only |
| Klüver [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md) | Highlights gap — SIL assessment at design time, not runtime |
| Bengio/Hinton 2024 [[notes]](../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) | Fills background — policy-level governance with "if-then" capability-triggered commitments; categorically distinct from runtime architectural governance |

**Citation cluster**: Guardrails cluster (Shamsujjoha → Chen → SHIELDAGENT) + Policy cluster (Bengio/Hinton 2024 → Intl AI Safety Report)

**Key limitation**: AI governance frameworks operate at policy level (what AI should be allowed to do in principle) or at design-time (what DL usage level is permitted). None implement runtime governance conditioned on classified environmental safety state.

**Transition**: *"Governance frameworks define what AI should be permitted to do — but the mechanism by which AI combines deterministic rules with probabilistic inference (the hybrid architecture) determines what is technically possible to govern."*

---

#### Section 2.6: Hybrid AI and Neuro-Symbolic Systems (Links 1–2)
**Purpose**: Review hybrid AI approaches combining deterministic rules and machine learning — and establish that most hybrid AI research focuses on improving prediction accuracy and explainability, not on governing whether AI is allowed to participate and what AI is allowed to recommend.

| Paper | Role |
|-------|------|
| SYNAPSE (Castagnone) [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) | Fills background — neuro-symbolic hybrid for building management |
| Punzi [[notes]](../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md) | Fills background — hybrid decision-making taxonomy |
| Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md) | Highlights gap — hierarchical rule + ML constraints, but not state-conditioned governance |
| Kalmykov [[notes]](../notes/Towards%20eXplicitly%20eXplainable%20Artificial%20Intelligence.md) | Fills background — information fusion with rule-based and probabilistic components |
| Pitale (HySAFE-AI) [[notes]](../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md) | Fills background — hybrid safety AI architecture |
| Vermaelen (Tumato) [[notes]](../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) | **Comparator** — hybrid temporal logic + ML, soundness by construction |
| Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) | Analog — hybrid AI in resource-constrained healthcare |
| Yuzui/Kaneko [[notes]](../notes/Toward%20a%20hybrid%20approach%20for%20the%20risk%20analysis%20of%20maritime%20autonomous%20surface%20ships-%20a%20systematic%20review.md) | Fills background — hybrid risk analysis in maritime |

**Key positioning**: Most hybrid AI research focuses on combining rules and ML to improve accuracy and explainability. The governance question — whether AI is allowed to participate and what AI is allowed to recommend — is not addressed.

**Transition**: *"Hybrid AI is the enabling architecture. The deployment context determines the constraints. In low-resource environments, those constraints are particularly severe."*

---

#### Section 2.7: AI Systems in Low-Resource Environments (Link 7)
**Purpose**: Justify the low-resource environment context in the research title — and establish the additional constraints that AI systems must satisfy in these contexts.

| Paper | Role |
|-------|------|
| Katende [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) | Fills background — comprehensive low-resource AI constraint taxonomy |
| Haque/Al Jufaili [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md) | Establishes gap — fisheries AI has no formal governance; low-resource context |
| Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) | Analog comparator — hybrid AI in resource-constrained healthcare (cross-domain) |
| Talpur [[notes]](../notes/AI%20in%20Maritime%20Security-%20Applications%2C%20Challenges%2C%20Future%20Directions%2C%20and%20Key%20Data%20Sources.md) | Fills background — ICT adoption in developing region fisheries |
| Mandal [[notes]](../notes/The%20Significance%20of%20Artificial%20Intelligence%20(AI)%20in%20Fishing%20Crafts%20and%20Gears.md) | Fills background — environmental AI in low-data contexts |
| Nastoska [[notes]](../notes/Evaluating%20Trustworthiness%20in%20AI-%20Risks%2C%20Metrics%2C%20and%20Applications%20Across%20Industries.md) | Fills background — edge AI deployment constraints |
| Tahsin [[notes]](../notes/Towards%20the%20adoption%20of%20AI%2C%20IoT%2C%20and%20Blockchain%20technologies%20in%20Bangladesh%27s%20maritime%20industry-%20Challenges%20and%20insights.md) | Fills background — AI in resource-limited industrial settings |
| Wen [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) | Fills background — AI deployment in data-deficient environments |
| **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | **Primary domain characterisation** — strongest primary data from target population (n=136, 2023 fieldwork, Q1 journal); half earn <RM 1,000/month; 60% lower secondary education or below; limited technology access but actively using weather apps |
| Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) | Supplementary — temporal continuity for environmental factor significance in Malaysian SSF (2024) |

**Key idea**: AI systems in low-resource environments must operate with limited connectivity, limited compute, and users with varying digital literacy. Binary governance is particularly costly in this context — disabling AI entirely under moderate risk wastes a scarce resource when partial AI assistance would be safe and valuable.

**Transition**: *"Within the class of low-resource, safety-critical environments, coastal fisheries is the domain that most directly motivates and empirically validates the proposed architecture."*

---

#### Section 2.8: Technology and Decision Support in Small-Scale Fisheries (Link 7 continued)
**Purpose**: Justify the case study domain — and establish that no formal safety governance architecture exists in fisheries AI.

**Centrepiece pair**: Gao (2024) — *"Fisher Decision-Making in Penang"* + Yamin et al. (2025) — *"Traditional Knowledge and Adaptive Capacity in Terengganu"*

Gao's empirical finding is the cornerstone of the domain justification: Penang fishers already make tripartite decisions — *go*, *cautious-go*, and *don't-go* — based on weather and sea conditions. This maps directly to SAFE/CAUTION/UNSAFE. Yamin et al. (2025) — the strongest primary empirical study of the exact target population — provides the quantitative reinforcement: 95% of 136 Terengganu fishers identify stronger winds/waves as a primary hazard, the empirical knowledge item "if it's suddenly windy/change of weather, I can't go fishing" confirms the binary go/no-go as the sole decision mode, and flexibility is the weakest adaptive capacity domain. Together, these two studies establish that the proposed architecture formalises a decision structure that practitioners already use informally (Gao) and addresses a measured adaptive capacity deficit in the population (Yamin).

**Four pillars of domain argument**:
1. **Environmental variability as first-class concern** — fisheries face continuously varying conditions (weather, sea state, visibility, tidal patterns) that directly determine operational safety. Yamin et al. (2025) confirm this with near-unanimous fisher-reported agreement: wind/waves (95%), weather intensity (91%), rainfall (91%).
2. **Existing informal tripartite decision-making** — Gao (2024) documents go / cautious-go / don't-go; Rahim (2024) documents survival decisions under extreme weather. SAFE/CAUTION/UNSAFE formalises existing practice, not an imposed abstraction.
3. **Resource constraints make binary governance costly** — in low-resource settings, a binary gate that disables AI under moderate risk wastes the resource precisely when partial assistance would be most valuable.
4. **Decision support vacuum at intermediate risk** — Yamin et al. (2025) document that fishers' traditional weather prediction abilities are declining while reliance on weather apps grows. No current system translates environmental data into scope-restricted advisory governance. The CAUTION mode fills this specific gap.

| Paper | Role |
|-------|------|
| **Gao** [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) | **Co-centrepiece** — empirical tripartite fisher decision-making validates SAFE/CAUTION/UNSAFE |
| **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | **Co-centrepiece** — primary quantitative validation of E vector via fisher-reported hazards (95% wind/waves, 91% rainfall); confirms binary go/no-go; flexibility as weakest adaptive capacity domain; TK erosion creating decision support vacuum |
| Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) | Supports centrepiece — survival decisions under extreme weather validate CAUTION concept |
| Haque/Al Jufaili [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md) | Establishes gap — no formal governance in fisheries AI |
| Wing/Woodward [[notes]](../notes/Advancing%20artificial%20intelligence%20in%20fisheries%20requires%20novel%20cross-sector%20collaborations.md) | Fills background — fisheries AI ecosystem needs and data gaps |
| Welch [[notes]](../notes/Harnessing%20AI%20to%20map%20global%20fishing%20vessel%20activity.md) | Fills background — fisheries AI monitoring technology |
| Kühn [[notes]](../notes/Machine%20Learning%20Applications%20for%20Fisheries%E2%80%94At%20Scales%20from%20Genomics%20to%20Ecosystems.md) | Fills background — fisheries AI state of the art review |
| Bossier [[notes]](../notes/How%20much%20time%20and%20who%20will%20do%20it%3F%20Organizing%20the%20toolbox%20of%20climate%20adaptations%20for%20small-scale%20fisheries.md) | Fills background — marine AI decision support |
| Obi [[notes]](../notes/Overview%20of%20the%20fishery%20and%20aquaculture%20sectors%20in%20Malaysia.md) | Fills background — Malaysian small-scale fisheries sector |
| Peskas (Longobardi) [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md) | Fills background — fisheries data platform in low-resource settings |
| Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) | Fills background — maritime AI transparency and safety (adjacent domain) |
| Shaffril [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) | Historical background — 2017 domain characterisation of Malaysian SSF (background context, not primary) |
| Muhamad [[notes]](../papers/sources/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) | Supplementary — fuzzy logic domain precedent for S = f(E) implementation; temporal continuity for environmental factors (2024) |
| Atacan & Düzbastılar (2023) [[notes]](../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | Fills background — empirical risk perception data from small-scale fishing vessel captains (simulator study, n=30); night navigation and restricted visibility as primary accident risk factors; justifies t variable in E |
| Dominguez-Péry et al. (2023) [[notes]](../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md) | Fills background — IMO accident investigation evidence (504 reports, 2011–2021); small vessels face highest fatality risk; external environmental factors including visibility are the largest risk cluster; justifies t and v in E |

**Citation cluster**: Fisheries/maritime cluster (isolated from safety governance cluster — proposed work bridges these two disconnected bodies of literature)

**Transition**: *"The fisheries domain validates and motivates the proposed architecture — but the architecture must also be evaluated. The following section establishes the methodological foundations for that evaluation."*

---

#### Section 2.9: Trust Measurement and Evaluation Methodology (Links 8–9)
**Purpose**: Ground the evaluation methodology (PS4/PS5) in the human factors and trust literature — establishing that while no prior work evaluates graduated AI governance specifically, validated instruments and frameworks exist that can be extended to this context.

| Paper | Role |
|-------|------|
| McGrath et al. (S-TIAS) [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md) | **Methodological foundation** — validated 3-item trust instrument (S-TIAS) for PS5; trust calibration framework |
| McGrath et al. (CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) | **Methodological foundation** — trust calibration as evaluation criterion; temporal trust dynamics across governance mode transitions |
| Bach et al. [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) | **Methodological foundation** — trust measurement SLR; instrument catalogue; sample size guidance for PS5 design |
| Schrills et al. [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) | **Methodological foundation** — trust ≠ dependence; behavioural dependence metric; dual-measurement design for PS4 |
| Aquilino et al. [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md) | **Methodological foundation** — cognitive vs affective trust; mode-specific instrument selection |
| Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) | **Methodological foundation** — explainability–trust baseline (r = 0.194); trustworthiness vs trust distinction |
| Saup [[notes]](../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md) | Fills background — socio-technical governance framework for evaluation design |
| Gabriel [[notes]](../notes/Requirements%20Analysis%20for%20an%20Intelligent%20Workforce%20Planning%20System-%20A%20Socio-Technical%20Approach%20to%20Design%20AI-Based%20Systems.md) | Fills background — socio-technical requirements methodology |
| Zhao/Yuan [[notes]](../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md) | Motivates — ethical question of governance varying by severity (PS5 context) |
| Madsen/Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) | Motivates — maritime AI transparency gap (no governance display) |
| Yamin [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | Fills background — questionnaire instrument precedent (Cronbach's α = 0.914) in exact target population; Malay Terengganu dialect requirement for PS5 questionnaire design; enumerator-administered approach required given education profile (60% lower secondary or below); sample size benchmark (n = 136 from ~800 fishers, 17% coverage) |

**Citation cluster**: Trust & evaluation methodology cluster (Bach → McGrath S-TIAS ↔ McGrath CHAI-T ↔ Schrills)

**Evaluation gaps established**:
- **PS4 gap**: No study compares graduated two-level governance (ungated vs binary-gated vs two-level graduated) — methodological foundations established but not yet applied to governance architectures
- **PS5 gap**: No user study addresses the CAUTION mode specifically — AI active but operating under recommendation scope restriction is a novel governance state with no precedent in the automation trust literature

**Transition**: *"The human factors literature provides validated instruments and frameworks for measuring trust, calibration, and behavioural dependence. What remains is their application to graduated governance states — particularly the CAUTION mode — which no prior study has examined."*

---

#### Section 2.10: Literature Summary and Research Gap
**Purpose**: Synthesise limitations across all sections and state the research gap.

**Literature Summary Table**:

| Area | What Exists | Limitation |
|------|-------------|------------|
| Safety constraints (§2.2) | Block unsafe actions — binary gate | Do not control AI advisory scope |
| Human-AI authority (§2.3) | Supervisory control, automation levels | Do not define participation based on safety conditions |
| Adaptive autonomy (§2.4) | Change authority level based on risk | Advisory scope not formally restricted; no containment relationship; governance not formally defined |
| AI governance (§2.5) | Policy-level and design-time governance | Not runtime decision architecture conditioned on environmental state |
| Hybrid AI (§2.6) | Combine rules and ML | Focus on accuracy and explainability, not governance |
| Low-resource AI (§2.7) | Focus on deployment constraints | Not safety-gated decision architecture |
| Fisheries AI (§2.8) | Decision support and monitoring tools | No formal safety governance |
| Evaluation methodology (§2.9) | Validated trust instruments and frameworks | Not applied to graduated governance states |

**Research Gap Statement**:

Existing studies implement safety constraints, decision support systems, adaptive autonomy, AI governance frameworks, and hybrid AI approaches independently. However, the literature does not present an architectural model in which environmental safety state simultaneously governs both AI participation and AI advisory recommendation scope as a unified governance mechanism. Specifically, no architecture defines both G(S) (participation gate) and A_AI(S) (admissible recommendation space) as a formally unified pair conditioned on classified environmental safety state S ∈ {SAFE, CAUTION, UNSAFE}, with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S). Furthermore, no evaluation study compares graduated two-level governance against binary governance (PS4), and no socio-technical study examines user response to the CAUTION mode — a novel governance state in which AI participates under recommendation scope restriction (PS5).

Therefore, there is a lack of a formally defined graduated safety-state-gated architecture for AI decision support in safety-critical and low-resource environments, and a corresponding gap in the evaluation methodology for assessing its comparative performance and user acceptance.

---

### Positioning Summary

The literature establishes that: (1) hybrid AI is well-studied in safety-critical domains; (2) Level 1 participation governance (binary AI on/off) is universally implemented via shields, safety filters, and supervision functions, confirmed across 46 formal methods papers (Newcomb), 91 collaborative intelligence papers (Ramos), and 11 international safety frameworks (Bengio); (3) Level 2 advisory scope governance exists in the form of guardrails and runtime enforcement but is applied statically or per-action, never conditioned on classified environmental safety state; (4) risk-adaptive systems change autonomy level but do not formally restrict advisory scope or define containment relationships between governance modes.

Binary governance is structurally inadequate because it forces a false dilemma: over-restriction (disabling AI entirely when partial assistance would be safe and valuable) or under-restriction (permitting full AI participation under elevated risk). The CAUTION mode resolves this dilemma — AI remains active but advisory scope narrows to recommendation types that remain reliable under elevated conditions.

The closest prior art — Flehmig et al.'s traffic-light model — governs monitoring intensity triggered by AI performance, not recommendation scope triggered by environmental state. Baxi's comprehension-gated architecture implements the closest formal structure (graduated tiers with containment) but conditions on agent robustness — a static, offline-assessed property — rather than environmental state, which is dynamic and continuously observable. These conditioning strategies demand fundamentally different observation mechanisms, update dynamics, and failure handling — constituting architecturally distinct approaches.

The fisheries domain is not merely a convenient application context: it is the domain where environmental-state-conditioned governance is most natural (continuous environmental variability), most empirically motivated (Gao 2024 documents existing tripartite informal decision-making — go / cautious-go / don't-go; Yamin et al. 2025 confirms the binary go/no-go as the sole decision mode among 136 Terengganu fishers and identifies flexibility as the weakest adaptive capacity domain), and most valuable (binary governance wastes scarce AI resources under moderate risk in low-resource settings). Yamin et al. (2025) reframe the CAUTION mode's significance: it does not merely restrict AI advisory scope — it addresses a measured population-level adaptive capacity deficit by enabling a graduated response that fishers currently cannot execute without decision support. The proposed architecture bridges the safety governance literature and the fisheries AI literature, which have no prior citation connection.

The evaluation methodology is grounded in the human factors literature on trust in automation — validated instruments (S-TIAS), trust calibration frameworks (CHAI-T), and dual-measurement designs distinguishing attitudinal trust from behavioural dependence (Schrills et al. 2025) — extended to the novel context of graduated governance states and the CAUTION mode specifically.

The proposed two-level governance pair (G(S), A_AI(S)), conditioned on classified environmental safety state with the Safety Dominance Property AI(E) ⊆ A_AI(S), fills a gap confirmed across multiple independent bodies of literature. The evaluation gaps (PS4, PS5) extend this contribution: no prior work provides comparative evidence for graduated vs binary governance, and no prior user study examines AI participation under recommendation scope restriction as a distinct governance state.

---

## 8. Coverage Summary Tables

### Theme Coverage

| Theme | Code | Yes | Partial | No | Coverage |
|-------|------|-----|---------|-----|----------|
| Hybrid AI | T1 | 17 | 21 | 25 | Well-Covered |
| Safety-critical AI | T2 | 32 | 15 | 16 | Well-Covered |
| AI governance | T3 | 27 | 18 | 18 | Well-Covered |
| Low-resource | T4 | 6 | 16 | 41 | Partially Covered |
| Formalisation | T5 | 9 | 23 | 31 | Partially Covered |
| Human role | T6 | 26 | 27 | 10 | Well-Covered |
| Socio-technical | T7 | 15 | 23 | 25 | Partially Covered |
| Fisheries/maritime | T8 | 14 | 4 | 45 | **Well-Covered** |

### Problem Statement Coverage

| PS | Coverage | Comparators / foundations found | Key gaps |
|---|---|---|---|
| PS1 | Well-Supported | Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md), SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md), Odriozola-Olalde [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | None — gap well-argued; 3 new shielding papers further confirm binary |
| PS2 | Well-Supported | Shields [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md), Corsi [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md), SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | None — gap well-argued; new papers confirm no environmental state conditioning |
| PS3 | Partially Supported | Bhuvaneswari [[notes]](../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) (analog), Peskas [[notes]](../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md), Haque [[notes]](../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | No architectural comparator within fisheries; domain context now strongly established |
| PS4 | **Partially Supported** | McGrath S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md), CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md), Bach [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md), Aquilino [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md), **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | No direct evaluation of graduated vs binary governance; flexibility as outcome variable identified |
| PS5 | **Partially Supported** | McGrath S-TIAS [[notes]](../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md), CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md), Bach [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md), Aquilino [[notes]](../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md), **Yamin** [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | No user study of intermediate governance mode; target population socio-technical context now established |

### Governance Level Distribution

| Category | Count |
|----------|-------|
| Level 1 only (binary gate) | ~18 papers |
| Any form of Level 2 | ~12 papers |
| Level 2 state-conditioned | 2 papers (Shields: continuous; Baxi: robustness) |
| Unified two-level, environment-state-conditioned | **0 papers** |

---

## 10. Justification Alignment Note

This section maps each of the four justification documents to their load-bearing corpus citations and checks whether any justification argument relies on a paper not yet positioned in the Chapter 2 outline.

### a) justification-environmental-state-governance.md

**Why governance is conditioned on environmental state rather than AI confidence, risk score, or model uncertainty.**

Load-bearing citations: Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (calibration impossibility — AI confidence fails as trigger), Bloomfield & Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) (self-referential governance critique), Bach [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) (trust requires interpretability — confidence scores lack it), McGrath CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) (predictability as trust determinant), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (causal primacy of environment over model state), Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) (causal structure — environment drives outcomes regardless of AI), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) (independence — verifier must not share failure modes with AI), Könighofer [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (shield separation principle), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) (trust empowerment — observable triggers build appropriate trust), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) (instructed reliability — users calibrate better when trigger is transparent), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) (tripartite environmental decision framework), Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) (fisher-reported hazard hierarchy mapping to E vector; TK erosion creating decision support vacuum; flexibility deficit), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) (ODD confinement — environmental boundaries define operational scope), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) (gap confirmation — 91 papers, none condition on environmental state), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) (gap — 11 international frameworks, all binary), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) (SWaP constraints in low-resource deployment).

**Placement check**: All citations positioned in Chapter 2 outline (Sections 2.2–2.6 for governance/formal papers; Section 2.7–2.8 for domain papers). No placement gaps.

### b) justification-advisory-scope-restriction.md

**Why CAUTION mode restricts advisory scope rather than blocking AI or reducing autonomy.**

Load-bearing citations: Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) (ALARP principle — restriction proportional to risk; false alarm costs), Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) (binary warning override — fishers ignore all-or-nothing alerts), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) (gap — 91 papers, no intermediate advisory restriction), Madsen & Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) (display ≠ governance — information presentation alone insufficient), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) (ODD/ROD/MRC envelope — scope restriction as standard safety practice), Bloomfield & Rushby [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) (nuclear safety precedent — limitation of advisory scope in safety-critical domains), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) (anchoring bias — unrestricted AI creates over-reliance; instructed reliability), Wen [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) (human intervention ineffective under time pressure — scope restriction preferable to human override), Mussi [[notes]](../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md) (progressive disclosure — graduated information reduces cognitive overload), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) (VOI — value of information decreases under uncertainty; false precision harmful), McGrath CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) (trust calibration — mode-appropriate trust requires visible scope boundaries), Bach [[notes]](../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) (expectation mismatch — users assume AI is fully capable unless scope is visibly restricted), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) (cautious-go as informal scope restriction precedent), Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) (flexibility deficit — weakest adaptive capacity domain; TK erosion; binary status quo confirmed), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (gap — 46 formal methods papers, none implement graduated advisory restriction).

**Placement check**: All citations positioned in Chapter 2 outline (Sections 2.4–2.6 for governance mechanism papers; Section 2.8 for domain papers; Section 2.9 for evaluation papers). No placement gaps.

### c) justification-three-states.md

**Why three discrete safety states (SAFE/CAUTION/UNSAFE) rather than binary, continuous, 5-level, or probabilistic alternatives.**

Load-bearing citations: Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) (gap — 91 papers, binary governance universal), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) (11 frameworks, all binary), Gao [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) (tripartite go/cautious-go/don't-go — empirical precedent for three states), Rahim [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) (tripartite seasonal pattern — monsoon/transition/fair as natural three-state structure), Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) (binary go/no-go confirmed as status quo; flexibility = weakest domain; CAUTION as capacity-building), McGrath CHAI-T [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) (calibration failure modes — too few states under-calibrate, too many overwhelm), Wen [[notes]](../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) (mode confusion risk — cognitive overload increases with state count), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (formal methods — binary safety boundaries amenable to verification; three states preserve tractability), Madsen & Kim [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) (categorical maritime risk classification — precedent for discrete states), Gyllenhammar [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) (ODD→ROD→MRC — three operational domains as automotive precedent), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) (traffic-light 3-level — closest structural precedent, but governs monitoring not scope), Schrills [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) (probability matching — users approximate discrete categories, not continuous distributions), Atf & Lewis [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) (weak explainability-trust correlation — simpler state space aids explanation), Könighofer [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (winning region — binary formal property extendable to three states), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (K≥3 comprehension tiers — formal precedent for graduated governance beyond binary), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) (Class I/II/III device classification — regulatory three-tier precedent).

**Placement check**: All citations positioned in Chapter 2 outline. Flehmig appears in Section 2.5 (two-level governance gap); Baxi in Sections 2.5–2.6; Gao and Rahim in Section 2.8. No placement gaps.

### d) justification-novelty-gap.md

**Comprehensive gap argument confirming the two-level governance architecture is new.**

Load-bearing citations: Shields/Könighofer [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) (Level 1 only — binary shield), AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) (per-action binary constraint — Level 2 mechanism but not state-conditioned), Dalrymple [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) (binary verifier — Level 1), Bajcsy [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) (binary safety filter — Level 1), Flehmig [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) (primary comparator — three-level traffic-light but governs monitoring intensity, not advisory scope; triggered by AI performance, not environmental state; single governance level), Baxi [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) (5-point differentiation — comprehension-gated, robustness-conditioned, static assessment, no environmental state, no advisory scope restriction), Shamsujjoha [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) (static Level 2 — guardrails defined at design time, not state-conditioned), Ramos [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) (91 papers — systematic gap confirmation), Newcomb [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) (46 papers — formal methods gap confirmation), Bengio [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) (11 frameworks — international governance gap confirmation), Perez-Cerrolaza [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) (cross-domain survey — safety-critical AI gap confirmation across automotive, aerospace, medical, industrial). Additionally confirmed by Corsi et al. (2024) [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) — region-selective shielding (binary safe/unsafe partition), Chen, Kang & Li (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) — SHIELDAGENT per-action LTL guardrail (binary), and Odriozola-Olalde et al. (2023) [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) — review of all shielded RL methods (all binary gate).

**Placement check**: All citations positioned in Chapter 2 outline. The four independent SLR gap confirmations (Ramos, Newcomb, Bengio, Perez-Cerrolaza) appear in Section 2.5 (the two-level governance gap). Flehmig and Baxi as primary comparators appear in Sections 2.5–2.6. Corsi, SHIELDAGENT, and Odriozola-Olalde positioned in Section 2.2. No placement gaps.

### Overall Assessment

All load-bearing justification citations are positioned in the Chapter 2 outline (Sections 2.2–2.10). Yamin et al. (2025) is newly load-bearing in justifications (a), (b), and (c) — positioned in Sections 2.7 and 2.8. No unpositioned citations found. The justification documents and Chapter 2 outline are fully aligned.
