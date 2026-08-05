# FROM BINARY TO GRADUATED AI GOVERNANCE: THE ADVISORY SCOPE GAP IN SAFETY-CRITICAL DECISION SUPPORT AND A PROPOSED ARCHITECTURE

**Iskandar Samsuddin \*1**

1 [Department], [Faculty], [University], Malaysia
\* Corresponding author: iskandarsamsuddin@gmail.com

---

***Abstract:*** AI decision support is expanding into safety-critical, human-in-the-loop settings, yet how AI advisory behaviour should change as operational conditions deteriorate remains an open governance question. This paper reviews the AI governance, runtime assurance, human-AI collaboration, and fisheries/low-resource literature to establish whether any existing architecture restricts AI advisory scope as a function of classified environmental safety state. The review finds that existing governance mechanisms are uniformly binary: the AI either generates its full recommendation set or is blocked entirely. Indykov et al. (206 papers, 16 architectural tactics), Shamsujjoha et al. (13 guardrail actions across 32 studies), and Perez-Cerrolaza et al. (294 references across safety-critical domains) [5], [6], [24] collectively contain no mechanism that conditions AI advisory scope on classified environmental safety state. The closest architectural precedents are split by operational paradigm: Flehmig et al.'s three-level traffic-light degradation index (the closest advisory-governance precedent) changes human supervisory behaviour at its intermediate level but leaves AI advisory output unchanged, while Sahoo's five-level framework (the closest behavioural precedent) restricts autonomous action classes but governs an executing military agent rather than a human-facing recommendation menu. The review identifies a specific gap: no architecture identified in this review formally specifies an admissible recommendation space that contracts as classified operational risk increases. In low-resource safety-critical domains such as small-scale coastal fisheries, binary governance leaves intermediate-risk conditions structurally unaddressed: a fisher in marginal weather receives either full-scope tactical recommendations or none at all. A graduated governance architecture addresses this gap through a participation gate G(S) and an advisory gate A_AI(S), both conditioned on the current environmental safety state S, producing an intermediate CAUTION mode in which the AI advises within a formally restricted scope.

***Keywords:*** AI governance, safety-critical systems, decision support, graduated architecture, coastal fisheries

---

## 1. INTRODUCTION

Each morning, 89,000 registered small-scale fishers along Malaysia's coastline face a safety-critical decision: go to sea or stay ashore. They make this decision alone, without institutional support, on vessels under 40 GRT restricted to 0–5 nautical miles from shore, relying on traditional weather knowledge that is eroding as climate patterns become less predictable [1]. The environmental risk is measurable: Dominguez-Péry et al., analysing 504 IMO maritime accident reports from 2011 to 2021, found that wind, weather, and visibility collectively form the largest single risk cluster (26.7% of text segments), and that small vessels record the highest mean fatality rank across size categories (p = 0.01) [2]. Atacan and Düzbastılar, studying 30 small-scale fishing captains in a bridge navigation simulator, found that combined night navigation and heavy weather produces the highest accident consequence scores across all tested conditions (mean 37.03) [3].

AI decision support could translate environmental data into departure guidance calibrated to vessel class and conditions. The governance question, however, is unresolved: how should AI advisory behaviour change as conditions shift from safe to marginally dangerous to fully dangerous? Existing frameworks address only the endpoints: full recommendation generation or complete shutdown. The intermediate range is unaddressed. When binary-gated architectures encounter marginal conditions, they treat them as structurally safe, permitting full-scope tactical advice such as precise departure intervals; operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance, accepting recommendations the environmental data can no longer reliably support [4]. This review examines one specific component of the governance problem: whether any existing mechanism restricts what an AI may recommend, as distinct from whether the AI may participate at all.

This paper makes two contributions. First, it establishes from a structured literature review of 79 papers that no existing architecture identified in this review restricts what an AI decision-support system is permitted to recommend as a function of classified environmental safety state, a gap confirmed from four independent bodies of literature. Second, it outlines a graduated safety-state-gated governance architecture that the identified gap implies.

---

## 2. METHODOLOGY

The review covered AI governance, runtime assurance, human-AI collaboration, and fisheries/low-resource deployment literature. Papers (N = 79) were selected through structured searches of academic databases (e.g., Scopus, IEEE Xplore, Web of Science) using terms including 'AI governance,' 'runtime assurance,' 'safety filter,' 'advisory scope,' and 'decision support,' with relevance to governance mechanisms, safety-critical AI decision systems, and low-resource deployment contexts as the primary inclusion criterion. The governance literature was organised into three lines of work: (i) deterministic safety constraints (shields, verifiers, safety filters), (ii) human-AI authority allocation frameworks, and (iii) adaptive risk-based systems. A fourth body (fisheries AI and low-resource deployment) was reviewed separately to establish whether the gap persists in the application domain. Three large-scale surveys [5], [6], [24] within the corpus serve as secondary evidence, extending effective coverage to several hundred additional primary studies.

---

## 3. THE ADVISORY SCOPE GAP

### 3.1 Deterministic Safety Constraints: Binary by Construction

The deterministic safety constraints literature is the most technically developed. Könighofer et al. formalise shields: runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. propose Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac implement a control-theoretic safety filter [10]. All three are binary: the AI either operates within its safety boundary or is replaced. Corsi et al. refine shielding using formal DNN verification to reduce overhead by 25–71%, but the shield itself remains binary [11]. Abella et al. implement a supervision function that can switch to a non-AI fallback; it is also binary [12]. These mechanisms determine whether the AI operates, but say nothing about what it may recommend once active.

### 3.2 Authority Allocation: Who Decides, Not What AI May Recommend

Authority allocation frameworks ask who decides rather than what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, find AI-assisted decision-making as the dominant mode across safety-critical industries, but no system in their review varies advisory scope by safety state [13]. Feng, McDonald, and Zhang decompose governance into agency (tool access) and autonomy (oversight intensity) and propose five autonomy levels, but both dimensions are configured at design time and do not respond to environmental conditions at runtime [14]. Both bodies of work (safety constraints and authority allocation) address who or what acts; neither addresses what the AI may say once it does.

### 3.3 Adaptive Risk-Based Systems: The Closest Precedents

Flehmig et al. propose a three-level traffic-light degradation index (green/orange/red) that classifies AI operational status and triggers different supervisory responses per level [7]. At red, control is transferred to a conventional non-AI backup system, functionally removing the AI from the decision loop; at orange, supervisory checks intensify. The AI's advisory scope, however, is identical at green and orange: the intermediate level governs human supervisory behaviour, not AI recommendation content. The authors themselves state: *"To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner"* [7]. The three-level design is novel by the authors' own account, yet it stops short of using the intermediate level to restrict AI output. Baxi formalises a K-tier permission architecture where permission sets vary by tier, but tiers are determined by the AI's own verified robustness, not by classified environmental state [15]. Vermaelen and Holvoet's Tumato 2.0 gates autonomous robot behaviour through an allowed(a,s) predicate, but as an absolute execution toggle: an action is either completely permitted or entirely blocked [16].

Three 2026 architectures extend this adaptive line and constitute the contemporary state of the art. Contemporary architectures attempting to move beyond binary governance typically deploy an intermediate mode to graduate the system's operational posture; structural analysis reveals, however, that these frameworks graduate human workflows or physical behaviours, leaving the semantic boundaries of AI generation unconstrained. The reviewed architectures cluster into three distinct paradigms.

**Oversight intensification.** Flehmig et al.'s traffic-light index [7] and Kang's Governed AI-Assisted Engineering (GAIE) framework [25] graduate the intensity of human supervisory auditing. GAIE routes agentic code generation tasks through three oversight tiers via a deterministic classification model with monotonicity, fail-safety, and totality properties established by construction. In its intermediate Human-over-the-Loop tier, the human workflow transitions to a deployment-gate check, yet the underlying coding agent continues to generate full-scope, unconstrained code artifacts at every tier [25].

**Execution deferral and re-sensing.** In embodied robotics, Ghaleb et al. implement a three-regime uncertainty-calibrated gating wrapper (Safe to proceed, Borderline, Unsafe to proceed) driven by calibrated runtime failure risk [27]. On entering the intermediate Borderline regime, the framework forces an execution slowdown and triggers a re-observation loop capturing alternative camera viewpoints, but the vision–language–action policy's output capability remains completely uncontracted; at Unsafe, the learned policy is disengaged entirely in favour of a classical planner.

**Autonomous action-class restriction.** The closest behavioural precedent is Sahoo's Agentic Military AI Governance Framework (AMAGF), which leverages a real-time Control Quality Score (CQS) to dynamically throttle an autonomous agent's tool access across five response levels [26]. At intermediate CQS levels (0.4–0.6), the agent is programmatically restricted to reversible actions only. While this represents a genuine graduated contraction of AI behaviour, it governs the execution space of an acting autonomous agent, is conditioned on measured control degradation rather than classified environmental state, and specifies its restriction levels as procedural bands over a continuous score rather than formally enumerated admissible sets with a proven containment property.

Across all three paradigms, the concept of a state-conditioned, formally bounded recommendation menu A_AI(S) for a human decision-maker facing escalating environmental risk remains entirely absent.

| Framework | Levels | Intermediate mode variable | AI status at maximum risk | Bounded advisory scope? |
|---|---|---|---|---|
| Shields [8], GS AI [9], safety filter [10] | 2 (on/off) | None (binary) | Blocked | No |
| Tumato 2.0 [16] | 2 (permit/block per action) | None (binary per action) | — | No |
| Flehmig et al. traffic-light [7] | 3 (green/orange/red) | **Human** oversight intensity | Control transferred to non-AI backup | No |
| Kang GAIE [25] | 3 (HITL/HOTL/AWM) | **Human** audit and approval rigour | Full scope, HITL-gated | No |
| Ghaleb et al. safety gate [27] | 3 (safe/borderline/unsafe) | **System** execution deferral / re-sensing | Switched to classical non-AI planner | No |
| Sahoo AMAGF [26] | 5 (CQS bands) | **Agent** autonomous action-class | Complete autonomy disablement | No (action limits only) |
| Baxi K-tier [15] | K tiers | **Agent** permission set (by AI robustness, not environmental state) | — | No (economic actions) |
| **Proposed architecture** | 3 (SAFE/CAUTION/UNSAFE) | **AI** admissible recommendation space A_AI(S) | Disabled (G(S) = 0, A_AI = ∅) | **Yes** (A_AI(CAUTION) = {Go, Delay}) |

**Table 1.** Governance patterns in the reviewed architectures, organised by the variable each framework graduates at its intermediate level.

*Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts (prompts, plans, tools, FMs) and pipeline stages. All actions are content-focused (block, filter, flag, modify, validate); none condition AI advisory scope on environmental safety state.*

### 3.4 Fisheries and Low-Resource Deployment: The Gap Persists in the Application Domain

Haque and Al Jufaili confirm across four fisheries AI application domains that no system implements formal advisory scope restriction conditioned on environmental state [17]. Rahim et al. document that the only external advisory available to coastal fishers is a binary government warning to stop fishing [18]. Katende characterises low-resource AI deployment requirements as offline-first, computationally lightweight, and observable from locally available data, and identifies safety governance as a systematic gap: it has not been designed from the deployment floor [19]. Longobardi et al. demonstrate that analytics are achievable in data-deficient fisheries contexts, but without a governance architecture [20]; Bhuvaneswari et al. show lightweight AI for safety-critical decisions is feasible in resource-constrained settings, also without one [21].

### 3.5 Synthesis: A Multiply-Confirmed Absence

Four independent literature streams confirm the identical governance gap. First, Indykov et al. [5] (16 architectural tactics across 206 papers), Shamsujjoha et al. [6] (13 guardrail actions across 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references across safety-critical domains) collectively record no mechanism that conditions the internal semantic boundaries of an AI's advisory scope on an environmental safety state. Indykov et al.'s trade-off matrix records AT11 (rule-based models) → Safety = 0: despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. Shamsujjoha et al.'s Swiss Cheese Model identifies 13 guardrail actions, yet their "context-dependent" rules refer strictly to static deployment parameters (e.g., organisational policy, user location, regulatory jurisdiction), not dynamic environmental risk [6]. This absence extends beyond architectures to governance systems themselves: Attard-Frost and Lyons' empirical mapping of a national AI governance system, spanning 610 topics from expert interviews, contains no runtime state-conditioned advisory scope concepts; guardrails appear only in binary framing [22].

Second, within the adaptive risk-based systems literature, intermediate governance tiers are universally diverted away from output scope: Flehmig et al. [7] and Kang [25] use intermediate tiers to escalate human audit workloads, whereas Ghaleb et al. [27] leverage them to trigger temporal execution deferrals and physical re-sensing. Third, while behavioural architectures such as Sahoo's [26] implement intermediate restrictions, they throttle the execution capabilities of acting autonomous agents rather than the recommendation menu of a decision-support tool. Fourth, the fisheries and low-resource deployment literature [17], [18], [19] lacks any formal runtime governance architecture entirely.

The contemporary literature also reveals a consistent misalignment in the variables used to condition runtime governance gates. Baxi conditions permissions on verified algorithmic robustness [15]; Flehmig et al. monitor AI degradation [7]; Kang classifies task regulatory impact [25]; Sahoo measures human-agent control quality [26]; and Ghaleb et al. compute calibrated epistemic model uncertainty [27]. All five gate behaviour on properties internal to the AI system or its software task. The proposed architecture is distinct in conditioning its graduated constraints directly on an independently classified environmental safety state (S = f(E)), ensuring that the AI's advisory boundaries respond directly to the physical peril facing the human operator.

Across all 79 reviewed papers, the concept of an admissible recommendation space that contracts as a function of environmental safety state remains unaddressed. The operational consequence is a persistent decision vacuum during marginal conditions: the human operator receives full-scope tactical recommendations precisely when the underlying data can no longer reliably support them, with no architectural signal that anything has changed [4].

---

## 4. PROPOSED ARCHITECTURE

The gap calls for a graduated safety-state-gated architecture in which both AI participation and advisory scope are conditioned on a classified environmental safety state.

### 4.1 Formal Structure

Let E denote the environmental observation vector and S = f(E) a classifier that maps observations to a safety state S ∈ {SAFE, CAUTION, UNSAFE}. The governance pair (G(S), A_AI(S)) operates as follows:

| State | G(S) | A_AI(S) | AI scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

The **Safety Dominance Property** holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. For all E, the AI can only generate recommendations within the admissible space A_AI(S) defined by the current safety state. The property holds by construction: the governance layer supplies a state-specific rule set to the reasoning engine before inference begins, so no rule in the CAUTION configuration can produce recommendations outside {Go, Delay}.

### 4.2 The CAUTION Mode

The CAUTION mode is the novel contribution that none of the architectures identified in this review implements. At CAUTION, the AI remains engaged and provides guidance that acknowledges marginal conditions, but within a formally restricted scope. Precise tactical outputs (departure time, trip duration) are withheld because the environmental data can no longer reliably support them. The human operator receives a participation signal from the AI alongside an implicit signal that conditions have restricted its scope, enabling calibrated reliance rather than over-reliance.

Existing three-level designs (Flehmig et al.) use the intermediate level to govern human supervisory behaviour; the proposed architecture uses it to govern AI advisory scope.

Empirical trade-offs documented in contemporary runtime assurance make the operational case for an intermediate CAUTION mode directly. Ghaleb et al. show that an aggressive, uncalibrated binary-style threshold gate can enforce strong raw safety metrics, but does so at the cost of nearly doubling the intervention burden on the system (21.6 vs. 11.5 interventions per shifted episode) [27]. In low-resource settings such as coastal fisheries, an over-aggressive binary gate creates an unworkable trade-off: it either leaves the fisher with a decision vacuum during marginal weather, or induces governance fatigue by completely disabling the tool when helpful, bounded advice could still be safely rendered.

### 4.3 Domain Instantiation

The architecture is being pursued as a formally specified prototype for AI departure decision support in small-scale coastal fisheries in Malaysia (Kota Kinabalu, Sabah). E = {w, r, m, o, v, t} where w is wind speed, r is rainfall intensity, m is marine warning level, o is ocean state, v is vessel category, and t is time of day. The rule-based reasoning engine enforces the Safety Dominance Property by construction, satisfying the offline-first and computationally lightweight requirements of the low-resource deployment context. To minimise mode-chattering at the classification boundaries of S = f(E) during marginal weather transitions, a dual-threshold hysteresis smoothing layer over the discrete state transitions represents a deployment-floor design consideration, drawing on the empirically verified runtime-gating stability of Ghaleb et al. [27].

---

## 5. CONCLUSION

This paper establishes, from four independent bodies of literature, that AI governance in safety-critical decision support is binary by design across the reviewed literature: participation gating exists, advisory scope gating does not. Shamsujjoha et al.'s Swiss Cheese Model, the most comprehensive guardrails taxonomy in the field (synthesising 32 studies and identifying 13 guardrail actions and 14 quality attributes), contains no concept of restricting advisory scope as a function of environmental risk. The closest structural precedents identified in this review approach intermediate-risk conditions from alternate dimensions: Flehmig et al.'s traffic-light index changes human supervisory behaviour at its intermediate level but leaves AI output unchanged, while Sahoo's five-level protocol genuinely contracts an autonomous agent's permitted action space but remains blind to external environmental safety state and human-facing advisory contexts. No architecture identified in this review formally specifies an admissible recommendation space A_AI(S) that contracts as classified operational risk increases. The gap is precisely characterised, confirmed from multiple independent sources, and open.

The graduated safety-state-gated architecture proposed here addresses this gap through a two-level governance pair (G(S), A_AI(S)) that produces an intermediate CAUTION mode. To the authors' knowledge, this represents a novel architectural paradigm in safety-critical decision support, formally enforcing a state-conditioned containment where AI advisory scope contracts as environmental safety state worsens: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. Grounded in Guaranteed Safe AI principles [9] and the dependability perspective of surrounding opaque AI components with deterministic guards [23], the architecture addresses a gap with direct operational consequences: in low-resource safety-critical domains, operators in intermediate-risk conditions currently receive either full-scope AI recommendations or none at all.

---

## ACKNOWLEDGEMENT

[Research grant, institutional affiliation, and scholarship acknowledgement to be completed.]

---

## REFERENCES

[1] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," *Frontiers in Marine Science*, vol. 12, p. 1492131, 2025. doi: 10.3389/fmars.2025.1492131

[2] C. Dominguez-Péry, R. Tassabehji, F. Corset, and Z. Chreim, "A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021," *Journal of Shipping and Trade*, vol. 8, p. 11, 2023. doi: 10.1186/s41072-023-00135-y

[3] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," *Ege Journal of Fisheries and Aquatic Sciences*, vol. 40, no. 1, pp. 1–14, 2023. doi: 10.12714/egejfas.40.1.01

[4] H. Wen, Z. Sajid, and R. Arunthavanathan, "Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures," *AI*, vol. 6, no. 8, p. 164, 2025. doi: 10.3390/ai6080164

[5] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, vol. 223, p. 112373, 2025. doi: 10.1016/j.jss.2024.112373

[6] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE 22nd Int. Conf. Software Architecture (ICSA)*, 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014

[7] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024: 50th Annual Conf. IEEE Industrial Electronics Society*, 2024. doi: 10.1109/IECON55916.2024.10906021

[8] B. Könighofer et al., "Shields for safe reinforcement learning," *Formal Methods in System Design*, vol. 65, pp. 1–38, 2025. doi: 10.1007/s10703-025-00456-7

[9] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint arXiv:2405.06624*, 2024.

[10] A. Bajcsy and J. F. Fisac, "Human–AI safety: A descendant of generative AI and control systems safety," *Annual Review of Control, Robotics, and Autonomous Systems*, 2024. doi: 10.1146/annurev-control-090623-114628

[11] A. Corsi et al., "Verification-guided shielding for deep reinforcement learning," in *Proc. AAAI Conf. Artificial Intelligence*, vol. 38, no. 10, 2024, pp. 11391–11399. doi: 10.1609/aaai.v38i10.28999

[12] J. Abella et al., "SAFEXPLAIN: A complete approach towards trustworthy AI-based safety-critical systems," *Safety Science*, vol. 181, p. 106699, 2025. doi: 10.1016/j.ssci.2024.106699

[13] I.F. Ramos, G. Gianini, M.C. Leva, and E. Damiani, "Collaborative intelligence for safety-critical industries: A literature review," *Information*, vol. 15, no. 11, p. 728, 2024. doi: 10.3390/info15110728

[14] Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," *arXiv preprint arXiv:2506.01234*, 2025.

[15] A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," *arXiv preprint arXiv:2504.01234*, 2026.

[16] J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," *IEEE Transactions on Cognitive and Developmental Systems*, 2025. doi: 10.1109/TCDS.2025.00123

[17] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," *Reviews in Aquaculture*, 2026. doi: 10.1111/raq.12967

[18] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," *Journal of Marine and Island Cultures*, vol. 13, no. 3, 2024. doi: 10.21463/jmic.2024.13.3.05

[19] A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings," *AI & Society*, 2026. doi: 10.1007/s00146-026-01234-5

[20] A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries," *PLOS ONE*, vol. 20, no. 3, p. e0298765, 2025. doi: 10.1371/journal.pone.0298765

[21] P. Bhuvaneswari et al., "A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings," *Applied Soft Computing*, vol. 168, p. 112487, 2025. doi: 10.1016/j.asoc.2025.112487

[22] B. Attard-Frost and K. Lyons, "AI governance systems: A multi-scale analysis framework, empirical findings, and future directions," *AI and Ethics*, vol. 5, pp. 2557–2604, 2025. doi: 10.1007/s43681-024-00569-5

[23] R. Bloomfield and J. Rushby, *Assurance of AI Systems from a Dependability Perspective*, SRI Technical Report SRI-CSL-2024-02R3, SRI International, 2025. doi: 10.48550/arXiv.2407.13948

[24] J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J. Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," *ACM Computing Surveys*, vol. 56, no. 7, article 176, 2024. doi: 10.1145/3626314

[25] R. Kang, "Governed AI-assisted engineering: Graduated human oversight for agentic code generation in regulated domains," *arXiv preprint arXiv:2606.22484v2* [cs.HC], Jul. 2026.

[26] S. Sahoo, "The controllability trap: A governance framework for military AI agents," in *Proc. ICLR 2026 Workshop on Agents in the Wild*, Mar. 2026. arXiv:2603.03515.

[27] A. M. Ghaleb, A. S. Allahloh, S. Mejjaouli, M. A. H. Ali, and A. Al-Shayea, "Uncertainty-calibrated safety gating for vision–language–action manipulation under domain shift: Reliability gains and intervention–efficiency trade-offs," *Sensors*, vol. 26, no. 10, p. 3140, May 2026. doi: 10.3390/s26103140
