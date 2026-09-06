# Master Coding Table

**Date:** 2026-09-07
**Purpose:** Per-paper coding of the reviewed corpus against the four dimensions in TABLE I of `manuscript-v3.md` (Primary governance target · Runtime adaptation · Conditioning variable · Recommendation restriction). Provides a verifiable audit trail for the manuscript's "assessed against four dimensions" claim in Methodology.

## Coverage

- **18 primary comparators** — formally coded, presented verbatim from Chapter 2 Table 2.1. Each cell is a discrete verdict against one of the four dimensions plus two supplementary columns (Safety Gate, Adaptive Autonomy, Formal Model) that qualify the coding.
- **86 extended-corpus papers** — assessed against the same four dimensions during extraction. Per-paper coding lives inside each paper's extraction notes; Table 3b below is an index that links to the notes and flags whether the notes carry a structured "Governance Mechanism / Level Analysis" section (structured) or code the dimensions in prose only (prose).
- **104 total papers with governance coding.** This encompasses the manuscript-time "72" claim; the corpus grew from 72 to the current active count during thesis-chapter drafting (see `review-protocol.md` §Corpus reconciliation).

## Table 3a. Primary comparators (18) — verbatim from Chapter 2 Table 2.1

**Table 2.1: Architecture Comparison Summary**

| Study | Domain | Safety Gate | Adaptive Autonomy | AI Participation Controlled (L1) | Advisory Scope Restricted (L2) | Unified Governance | Formal Model |
|---|---|---|---|---|---|---|---|
| Bajcsy & Fisac (2024) [[notes]](../../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) | General AI / AV | Yes | No | Yes | No | No | Yes |
| Dalrymple et al. (2024) [[notes]](../../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) | General AI safety | Yes | No | Yes | No | No | Yes |
| Könighofer et al. (2025) [[notes]](../../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | Robotics / UAV / AV | Yes | No | Yes | No | No | Yes |
| Wang et al. (2026) — AgentSpec [[notes]](../../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) | LLM agents | Yes | No | Yes | No | No | Yes |
| Abella et al. (2025) — SAFEXPLAIN [[notes]](../../notes/SAFEXPLAIN-%20a%20Complete%20Approach%20Towards%20Trustworthy%20AI-Based%20Safety-Critical%20Systems.md) | Automotive / Space | Yes | No | Yes | No | No | No |
| Shamsujjoha et al. (2025) [[notes]](../../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) | LLM / FM agents | Partial | No | Partial | Yes | No | No |
| Ramos et al. (2024) *(91 papers)* [[notes]](../../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) | Multi-domain | Yes | No | Yes | No | No | Partial |
| Perez-Cerrolaza et al. (2024) *(survey)* [[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) | Automotive / Aviation / Industrial | Yes | No | Yes | No | No | Partial |
| Gyllenhammar et al. (2025) [[notes]](../../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) | Automated driving | Partial | Yes | Partial | No | No | Partial |
| Flehmig et al. (2024) [[notes]](../../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) | Industrial safety-critical | Yes | Yes | Partial | No | No | No |
| Baxi (2026) — CGAE [[notes]](../../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) | AI economic agency | Yes | Yes | Yes | Yes | Partial | Yes |
| Corsi et al. (2024) [[notes]](../../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md) | Robotics / DRL | Yes | No | Yes | No | No | Yes |
| Chen, Kang & Li (2025) — SHIELDAGENT [[notes]](../../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) | LLM agents | Yes | No | Yes | No | No | Yes |
| Odriozola-Olalde et al. (2023) [[notes]](../../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md) | General RL / robotics | Yes | No | Yes | No | No | Yes |
| Banerjee et al. (2025) — CRANE [[notes]](../../notes/CRANE-%20Reasoning%20with%20Constrained%20LLM%20Generation.md) | NLP / Formal methods | No | No | Yes | No | No | Yes |
| Hamel-De le Court et al. (2025) [[notes]](../../notes/Probabilistic%20Shielding%20for%20Safe%20Reinforcement%20Learning.md) | General RL | Yes | No | Yes | No | No | Yes |
| Kwon et al. (2025) [[notes]](../../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md) | General RL / robotics | Yes | Yes | Yes | No | No | Yes |
| Feng et al. (2025) [[notes]](../../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md) | General AI agents | No | No | Partial | No | No | Partial |
| **Proposed Architecture** | **Coastal fisheries** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |

*Column definitions: Safety Gate = binary mechanism to block AI participation. Adaptive Autonomy = switches between operational modes (e.g., normal → degraded → minimal risk) at runtime based on risk or context. L1 = formal mechanism governing when AI participates (G(S)). L2 = formal mechanism governing what AI recommends (A_AI(S)). Unified Governance = L1 and L2 as a formally coordinated pair conditioned on the same classified state. Formal Model = mathematical model with stated safety property. "Partial" indicates the system addresses the dimension incompletely, e.g., participation control without formal specification (L1 Partial), design-time configuration only (Formal Model Partial), or governance without environmental state conditioning (Unified Governance Partial).*


## Table 3b. Extended-corpus governance assessments (86)

Each row below is a paper that was assessed against the four dimensions during extraction but is not among the 18 primary comparators tabulated in Table 3a. The per-paper coding lives in the paper's extraction notes — open the linked file to see the Governance Mechanism Analysis (structured) or the prose-embedded coding (prose).

| Paper | Coding source in notes |
|---|---|
| Aquilino et al. (2025) [[notes]](../../notes/Decoding%20Trust%20in%20Artificial%20Intelligence-%20A%20Systematic%20Review%20of%20Quantitative%20Measures%20and%20Related%20Variables.md) | prose |
| Atacan & Düzbastılar (2023) [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | prose |
| Atf & Lewis (2026) [[notes]](../../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) | prose |
| Attard-Frost & Lyons (2025) [[notes]](../../notes/AI%20governance%20systems-%20A%20multi-scale%20analysis%20framework%2C%20empirical%20findings%2C%20and%20future%20directions.%20AI%20and%20Ethics.md) | prose |
| Bach et al. (2024) [HCI trust SLR] [[notes]](../../notes/A%20Systematic%20Literature%20Review%20of%20User%20Trust%20in%20AI-Enabled%20Systems-%20An%20HCI%20Perspective.md) | prose |
| Bach, Kristiansen et al. (2024) [HAII SLR] [[notes]](../../notes/Unpacking%20Human-AI%20Interaction%20in%20Safety-Critical%20Industries-%20A%20Systematic%20Literature%20Review.md) | structured |
| Batool et al. (2025) [AI governance SLR, external evidence] [[notes]](../../notes/AI%20governance-%20a%20systematic%20literature%20review.md) | prose |
| Belle (2025) [[notes]](../../notes/On%20the%20Relevance%20of%20Logic%20for%20Artificial%20Intelligence%2C%20and%20the%20Promise%20of%20Neurosymbolic%20Learning.md) | prose |
| Bello y Villarino et al. (2025) [[notes]](../../notes/Are%20We%20Regulating%20the%20Right%20Digital%20Systems%3F%20Testing%20Emerging%20Artificial%20Intelligence%20Frameworks%20against%20Real-World%20Public%20Sector%20Systems.md) | structured |
| Bengio et al. (2026) [Intl AI Safety Report] [[notes]](../../notes/International%20AI%20Safety%20Report%202026.md) | structured |
| Bengio, Hinton et al. (2024) [Science] [[notes]](../../notes/Managing%20extreme%20AI%20risks%20amid%20rapid%20progress.md) | structured |
| Bhuvaneswari et al. (2025) [[notes]](../../notes/A%20human-centered%20hybrid%20AI%20framework%20for%20optimizing%20emergency%20triage%20in%20resource-constrained%20settings.md) | structured |
| Bloomfield & Rushby (2025) [[notes]](../../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) | structured |
| Bossier et al. (2025) [[notes]](../../notes/How%20much%20time%20and%20who%20will%20do%20it%3F%20Organizing%20the%20toolbox%20of%20climate%20adaptations%20for%20small-scale%20fisheries.md) | structured |
| Cash et al. (2025) [LLM confidence judgments, external evidence] [[notes]](../../notes/Quantifying%20uncert-AI-nty-%20Testing%20the%20accuracy%20of%20LLMs%27%20confidence%20judgments.md) | prose |
| Castagnone & Nitti (2026) [[notes]](../../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) | structured |
| Chandran et al. (2025) [[notes]](../../notes/Smart%20technologies%20in%20aquaculture-%20An%20integrated%20IoT%2C%20AI%2C%20and%20blockchain%20framework%20for%20sustainable%20growth.md) | structured |
| Chen et al. (2025) [LLM Safety Survey] [[notes]](../../notes/AI%20Safety%20Landscape%20for%20Large%20Language%20Models-%20Taxonomy%2C%20State-of-the-art%2C%20and%20Future%20Directions.md) | structured |
| Di Paco et al. (2026) [AISAFETY] [[notes]](../../notes/AISAFETY-%20An%20AI-based%20smart%20system%20for%20enhancing%20operator%20safety%20in%20production%20processes.md) | structured |
| Dominguez-Péry et al. (2023) [[notes]](../../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md) | prose |
| Engin & Hand (2025) [dimensional governance, external evidence] [[notes]](../../notes/Towards%20Adaptive%20Categories-%20Dimensional%20Governance%20for%20Agentic%20AI.md) | prose |
| Gabriel et al. (2022) [[notes]](../../notes/Requirements%20Analysis%20for%20an%20Intelligent%20Workforce%20Planning%20System-%20A%20Socio-Technical%20Approach%20to%20Design%20AI-Based%20Systems.md) | structured |
| Gao (2024) [[notes]](../../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) | structured |
| Ghaleb et al. (2026) [[notes]](../../notes/Uncertainty-Calibrated%20Safety%20Gating%20for%20Vision%E2%80%93Language%E2%80%93Action%20Manipulation%20Under%20Domain%20Shift-%20Reliability%20Gains%20and%20Intervention%E2%80%93Efficiency%20Trade-Offs.md) | structured |
| Haque & Al Jufaili (2026) [[notes]](../../notes/Applications%20of%20Artificial%20Intelligence%20in%20Fisheries-%20From%20Data%20to%20Decisions.md) | structured |
| Herbold et al. (2024) [contrastive explanations] [[notes]](../../notes/Generating%20Context-Aware%20Contrastive%20Explanations%20in%20Rule-based%20Systems.md) | prose |
| Hildebrandt et al. (2026) [XHAILe] [[notes]](../../notes/XHAILe%20%E2%80%94%20Explainable%20Hybrid%20AI%20for%20Computational%20Law%20and%20Accurate%20Legal%20Chatbots.md) | prose |
| Indykov et al. (2025) [[notes]](../../notes/Architectural%20tactics%20to%20achieve%20quality%20attributes%20of%20machine-learning-enabled%20systems-%20a%20systematic%20literature%20review.md) | prose |
| Jeong & Im (2023) [wave height departure restrictions, Korea small fishing vessels] [[notes]](../../notes/Proposal%20of%20Restrictions%20on%20the%20Departure%20of%20Korea%20Small%20Fishing%20Vessel%20according%20to%20Wave%20Height.md) | prose |
| Kalmykov & Kalmykov (2025) [[notes]](../../notes/Towards%20eXplicitly%20eXplainable%20Artificial%20Intelligence.md) | structured |
| Kamath et al. (2025) [POD-Attention, external evidence] [[notes]](../../notes/POD-Attention-%20Unlocking%20Full%20Prefill-Decode%20Overlap%20for%20Faster%20LLM%20Inference.md) | prose |
| Kang (2026) [[notes]](../../notes/Governed%20AI-Assisted%20Engineering-%20Graduated%20Human%20Oversight%20for%20Agentic%20Code%20Generation%20in%20Regulated%20Domains.md) | structured |
| Katende (2026) [[notes]](../../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) | structured |
| Klüver et al. (2024) [[notes]](../../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md) | structured |
| Kolt et al. (2025) [complex systems AI governance, external evidence] [[notes]](../../notes/Lessons%20from%20complex%20systems%20science%20for%20AI%20governance.md) | prose |
| Koohestani (2025) [AgentGuard, runtime verification, workshop PoC] [[notes]](../../notes/AgentGuard-%20Runtime%20Verification%20of%20AI%20Agents.md) | prose |
| Kühn et al. (2025) [[notes]](../../notes/Machine%20Learning%20Applications%20for%20Fisheries%E2%80%94At%20Scales%20from%20Genomics%20to%20Ecosystems.md) | structured |
| Leppinen et al. (2026) [[notes]](../../notes/A%20Stage-Gate%20Decision%20Process%20for%20Guiding%20the%20Development%20of%20AI%20Solutions%20for%20Preventive%20Maintenance.md) | structured |
| Li et al. (2026) [[notes]](../../notes/Safety-Enhanced%20Deep%20Reinforcement%20Learning%20for%20Autonomous%20Driving-%20Dare%20to%20Make%20Mistakes%20to%20Learn%20Better%20and%20Faster.md) | structured |
| Liang et al. (2025) [[notes]](../../notes/Safeguarded%20AI-Driven%20Semantic%20Communication-%20Design%20Principles%2C%20Architecture%2C%20and%20Challenges.md) | structured |
| Longobardi et al. (2025) [Peskas] [[notes]](../../notes/Peskas-%20Automated%20analytics%20for%20small-scale%2C%20data-deficient%20fisheries.md) | structured |
| Madsen & Kim (2024) [[notes]](../../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) | structured |
| McGrath et al. (2025) [S-TIAS] [[notes]](../../notes/Measuring%20trust%20in%20artificial%20intelligence-%20validation%20of%20an%20established%20scale%20and%20its%20short%20form.md) | prose |
| Muhamad et al. (2024) [[notes]](../../notes/Validation%20of%20Factor%20Weights%20Affecting%20Productivity%20Efficiency%20in%20Malaysia%27s%20Small-Scale%20Fisheries%20Sector.md) | prose |
| Mussi et al. (2025) [[notes]](../../notes/Human-AI%20interaction%20in%20safety-critical%20network%20infrastructures.md) | structured |
| NIST (2023) [AI RMF 1.0] [[notes]](../../notes/Artificial%20Intelligence%20Risk%20Management%20Framework%20%28AI%20RMF%201.0%29.md) | prose |
| Nastoska et al. (2025) [[notes]](../../notes/Evaluating%20Trustworthiness%20in%20AI-%20Risks%2C%20Metrics%2C%20and%20Applications%20Across%20Industries.md) | structured |
| Newcomb & Ochoa (2026) [[notes]](../../notes/Formal%20methods%20for%20safety-critical%20machine%20learning-%20a%20systematic%20literature%20review.md) | structured |
| OWASP (2025) [[notes]](../../notes/OWASP%20Top%2010%20for%20Agentic%20Applications%202026.md) | structured |
| Obi et al. (2025) [[notes]](../../notes/Overview%20of%20the%20fishery%20and%20aquaculture%20sectors%20in%20Malaysia.md) | structured |
| Ogenyi et al. (2025) [[notes]](../../notes/Securing%20the%20future-%20AI-driven%20cybersecurity%20in%20the%20age%20of%20autonomous%20IoT.md) | structured |
| Pappula & Rusum (2024) [[notes]](../../notes/AI-Assisted%20Address%20Validation%20Using%20Hybrid%20Rule-Based%20and%20ML%20Models.md) | prose |
| Paz (2025) [complexity governance white paper, external evidence, unreviewed] [[notes]](../../notes/From%20Linear%20Risk%20to%20Emergent%20Harm-%20Complexity%20as%20the%20Missing%20Core%20of%20AI%20Governance.md) | prose |
| Pitale et al. (2025) [[notes]](../../notes/HySAFE-AI-%20Hybrid%20Safety%20Architectural%20Analysis%20Framework%20for%20AI%20Systems-%20A%20Case%20Study.md) | structured |
| Porter et al. (2025) [INSYTE] [[notes]](../../notes/INSYTE-%20A%20Classification%20Framework%20for%20Traditional%20to%20Agentic%20AI%20Systems.md) | structured |
| Punzi et al. (2024) [[notes]](../../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md) | structured |
| Rahim et al. (2024) [[notes]](../../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) | structured |
| Reuel et al. (2025) [RAI maturity survey, external evidence] [[notes]](../../notes/Responsible%20AI%20in%20the%20Global%20Context-%20Maturity%20Model%20and%20Survey.md) | prose |
| Robles & Mallinson (2025) [UAIGF, abstract-level only, full text pending] [[notes]](../../notes/Advancing%20AI%20governance%20with%20a%20unified%20theoretical%20framework-%20a%20systematic%20review.md) | prose |
| Rozenfeld et al. (2026) [GAVEL] [[notes]](../../notes/GAVEL-%20Rule-Based%20Activation-Level%20Safety%20for%20AI%20Systems.md) | prose |
| Ryu & Han (2025) [[notes]](../../notes/Environment-Aware%20Multi-Sensor%20Fusion%20for%20Maritime%20Domain%20Awareness-%20A%20Comprehensive%20Review.md) | prose |
| Sabiri et al. (2025) [hybrid quality recommender SLR] [[notes]](../../notes/Hybrid%20Quality-Based%20Recommender%20Systems-%20A%20Systematic%20Literature%20Review.md) | prose |
| Sahoo (2026) [[notes]](../../notes/The%20Controllability%20Trap-%20A%20Governance%20Framework%20for%20Military%20AI%20Agents.md) | structured |
| Saup et al. (2026) [[notes]](../../notes/From%20pilots%20to%20decision%20systems-%20embedding%20generative%20AI%20into%20strategic%20decision-making%20through%20a%20socio-technical%20and%20governance%20lens.md) | structured |
| Schrills et al. (2025) [[notes]](../../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) | prose |
| Selvam et al. (2026) [[notes]](../../notes/Artificial%20Intelligence%20in%20Process%20Safety-%20A%20Review%20of%20Opportunities%2C%20Challenges%2C%20and%20Future%20Directions%20for%20the%20Chemical%20Process%20Industries.md) | structured |
| Seong, Lim & Yoon (2025) [CLGuard] [[notes]](../../notes/CLGuard-%20A%20Context-Aware%20Suppression%20Framework%20for%20Resilient%20Driving%20Control.md) | prose |
| Shaffril et al. (2017) [[notes]](../../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia.md) | prose |
| Tahsin et al. (2025) [[notes]](../../notes/Towards%20the%20adoption%20of%20AI%2C%20IoT%2C%20and%20Blockchain%20technologies%20in%20Bangladesh%27s%20maritime%20industry-%20Challenges%20and%20insights.md) | structured |
| Talpur et al. (2025) [[notes]](../../notes/AI%20in%20Maritime%20Security-%20Applications%2C%20Challenges%2C%20Future%20Directions%2C%20and%20Key%20Data%20Sources.md) | structured |
| Tandel et al. (2025) [[notes]](../../notes/Smart%20Aquaculture-%20IoT%20and%20AI%20Application%20for%20Sustainable%20Fisheries.md) | structured |
| Tatasciore & Loft (2025) [[notes]](../../notes/Calibrating%20Reliance%20on%20Automated%20Advice-%20Transparency%20and%20Trust%20Calibration%20Feedback.md) | structured |
| Toskov & Toskova (2026) [AgroNova] [[notes]](../../notes/AgroNova-%20An%20Autonomous%20IoT%20Platform%20for%20Greenhouse%20Climate%20Control.md) | structured |
| Turgunbaev (2025) [rule-based reasoning] [[notes]](../../notes/Rule-Based%20Reasoning%20and%20Its%20Role%20in%20Intelligent%20Decision%20Making.md) | prose |
| Vermaelen & Holvoet (2025) [[notes]](../../notes/umato%202.0%20%E2%80%94%20A%20Constraint-Based%20Planning%20Approach%20for%20Safe%20and%20Robust%20Robot%20Behavior.md) | structured |
| Wang, Poskitt et al. (2025) [Pro2Guard, proactive enforcement, preprint] [[notes]](../../notes/Pro2Guard-%20Proactive%20Runtime%20Enforcement%20of%20LLM%20Agent%20Safety%20via%20Probabilistic%20Model%20Checking.md) | prose |
| Welch et al. (2024) [[notes]](../../notes/Harnessing%20AI%20to%20map%20global%20fishing%20vessel%20activity.md) | structured |
| Wen et al. (2025) [[notes]](../../notes/Risk%20Perception%20in%20Complex%20Systems-%20A%20Comparative%20Analysis%20of%20Process%20Control%20and%20Autonomous%20Vehicle%20Failures.md) | structured |
| Wing & Woodward (2024) [[notes]](../../notes/Advancing%20artificial%20intelligence%20in%20fisheries%20requires%20novel%20cross-sector%20collaborations.md) | structured |
| Wu et al. (2025) [single-threaded reasoners, external evidence, preprint] [[notes]](../../notes/LLMs%20are%20Single-threaded%20Reasoners-%20Demystifying%20the%20Working%20Mechanism%20of%20Soft%20Thinking.md) | prose |
| Yaakob et al. (2015) [seakeeping stability Malaysian small fishing boats, Tier 1 hydrodynamics] [[notes]](../../notes/Stability%2C%20Seakeeping%20and%20Safety%20Assessment%20of%20Small%20Fishing%20Boats%20Operating%20in%20Southern%20Coast%20of%20Peninsular%20Malaysia.md) | prose |
| Yamin et al. (2025) [[notes]](../../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) | prose |
| Yang & Zhu (2024) [industrial expert systems] [[notes]](../../notes/Industrial%20Expert%20Systems%20Review-%20A%20Comprehensive%20Analysis%20of%20Typical%20Applications.md) | prose |
| Yuzui & Kaneko (2025) [[notes]](../../notes/Toward%20a%20hybrid%20approach%20for%20the%20risk%20analysis%20of%20maritime%20autonomous%20surface%20ships-%20a%20systematic%20review.md) | structured |
| Zhang et al. (2025) [[notes]](../../notes/Developing%20real-time%20IoT-based%20public%20safety%20alert%20and%20emergency%20response%20systems.md) | structured |
| Zhao & Yuan (2025) [[notes]](../../notes/AI%20in%20Healthcare%20for%20Resource%20Limited%20Settings-%20An%20Exploration%20and%20Ethical%20Evaluation.md) | structured |

## Coverage caveats

- The manuscript's "72" figure is a snapshot from submission time. The current coded corpus is 104, of which 18 are primary comparators (Table 3a) and 86 are extended-corpus (Table 3b). The 32-paper growth (104 − 72) reflects added comparators and background references during thesis-chapter drafting.
- Six corpus papers have thin extraction notes and are not represented in the coded set (five are recommender-system papers cited as domain background rather than governance comparators; the sixth is CRANE, which is a primary comparator and is included in Table 3a even though its notes use a non-standard heading structure).
- One archived stub (Agent Governance Toolkit — Runtime Security for Autonomous AI Agents) is excluded from both tables; it was superseded by OWASP Top 10 for Agentic Applications 2026 (see `review-protocol.md` §Corpus reconciliation).
- The "structured" vs "prose" flag in Table 3b indicates only whether the notes file uses an explicit Governance Mechanism / Level Analysis section header, not the quality or depth of the coding. Some prose-flagged papers carry deeper analysis than some structured-flagged ones.
