# FROM BINARY TO GRADUATED AI GOVERNANCE: A STRUCTURED LITERATURE REVIEW OF THE ADVISORY SCOPE GAP IN SAFETY-CRITICAL DECISION SUPPORT

*(Times New Roman, 14pt, Bold, All Caps, Centered)*

---

**Iskandar Samsuddin \*1**

1 [Department], [Faculty], [University], Malaysia
\* Corresponding author: iskandarsamsuddin@gmail.com

---

***Abstract:*** AI decision support is expanding into safety-critical, human-in-the-loop settings, yet how AI advisory behaviour should change as operational conditions deteriorate remains an open governance question. This paper reports a structured literature review of 76 papers spanning AI safety architecture, runtime assurance, human-AI collaboration, and fisheries/low-resource deployment, coded against eight themes. The review finds that existing governance mechanisms are uniformly binary: the AI either generates its full recommendation set or is blocked entirely. Three large-scale surveys — Indykov et al. (206 papers, 16 architectural tactics), Shamsujjoha et al. (13 guardrail actions across 32 studies), and Perez-Cerrolaza et al. (294 references across safety-critical domains) — collectively contain no mechanism that conditions AI advisory scope on classified environmental safety state. The closest structural precedent, Flehmig et al.'s three-level traffic-light degradation index, changes human supervisory behaviour at its intermediate level but leaves AI advisory output unchanged. The review identifies a specific gap: no architecture formally specifies an admissible recommendation space that contracts as classified operational risk increases. The gap is consequential in low-resource safety-critical domains such as small-scale coastal fisheries, where binary governance leaves intermediate-risk conditions unaddressed. The paper concludes by outlining a graduated safety-state-gated governance direction — a governance pair (G(S), A_AI(S)) where G(S) gates AI participation and A_AI(S) gates advisory scope, both conditioned on safety state S — producing an intermediate CAUTION mode where the AI advises within a restricted scope.

***Keywords:*** AI governance, literature review, safety-critical systems, decision support, coastal fisheries

---

## 1. INTRODUCTION

Each morning, 89,000 registered small-scale fishers along Malaysia's coastline face a safety-critical decision: go to sea or stay ashore [1]. They make this decision alone, without institutional support, on vessels under 40 GRT restricted to 0–5 nautical miles from shore, relying on traditional weather knowledge that is eroding as climate patterns become less predictable [1]. The environmental risk is measurable: Dominguez-Péry et al., analysing 504 IMO maritime accident reports from 2011 to 2021, found that wind, weather, and visibility collectively form the largest single risk cluster (26.7% of text segments), and that small vessels record the highest mean fatality rank across size categories (p = 0.01) [2]. Atacan and Düzbastılar, studying 30 small-scale fishing captains in a bridge navigation simulator, found that combined night navigation and heavy weather produces the highest accident consequence scores across all tested conditions (mean 37.03) [3].

AI decision support could translate environmental data into departure guidance calibrated to vessel class and conditions. The governance question, however, is unresolved: how should AI advisory behaviour change as conditions shift from safe to marginally dangerous to fully dangerous? Existing frameworks answer only the endpoints — full recommendation generation or complete shutdown — and are silent on the intermediate range. When binary-gated architectures encounter marginal conditions, they default to treating them as structurally safe, permitting full-scope tactical advice such as precise departure intervals; operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance, accepting recommendations the environmental data can no longer reliably support [4].

This paper reviews the AI governance, runtime assurance, human-AI collaboration, and fisheries/low-resource literature to answer one question: **does any existing architecture restrict what an AI decision-support system is permitted to recommend as a function of classified environmental safety state?** The review finds that none does, establishes this absence from multiple independent bodies of literature, and outlines the graduated governance direction the gap implies.

---

## 2. METHODOLOGY

The review analysed 76 papers, classified into four extraction tiers: 34 full extraction, 27 reduced extraction, 7 methodological foundation, and 8 external evidence. Each paper was coded against eight themes — hybrid AI architectures, safety-critical AI decision systems, AI governance, low-resource environments, decision architecture formalisation, the human role in AI-assisted decision-making, socio-technical evaluation, and the coastal fisheries/maritime domain — with per-theme coverage recorded as Yes, Partial, or No.

For synthesis, the governance literature was organised into three lines of work: (i) deterministic safety constraints (shields, verifiers, safety filters), (ii) human-AI authority allocation frameworks, and (iii) adaptive risk-based systems. A fourth body — fisheries AI and low-resource deployment — was reviewed separately to establish whether the gap persists in the application domain. Three large-scale published surveys within the corpus [5], [6], [7] serve as secondary evidence, extending effective coverage to several hundred additional primary studies.

---

## 3. RESULTS & DISCUSSION

### 3.1 Deterministic Safety Constraints: Binary by Construction

The deterministic safety constraints literature is the most technically developed. Könighofer et al. formalise shields — runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. propose Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac implement a control-theoretic safety filter [10]. All three are binary: the AI either operates within its safety boundary or is replaced. Corsi et al. refine shielding using formal DNN verification to reduce overhead by 25–71%, but the shield itself remains binary [11]. Abella et al. implement a supervision function that can switch to a non-AI fallback; it is also binary [12].

### 3.2 Authority Allocation: Who Decides, Not What AI May Recommend

Authority allocation frameworks ask who decides rather than what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, find AI-assisted decision-making as the dominant mode across safety-critical industries, but no system in their review varies advisory scope by safety state [13]. Feng, McDonald, and Zhang decompose governance into agency (tool access) and autonomy (oversight intensity) and propose five autonomy levels, but both dimensions are configured at design time and do not respond to environmental conditions at runtime [14].

### 3.3 Adaptive Risk-Based Systems: The Closest Precedents

Flehmig et al. propose a three-level traffic-light degradation index (green/orange/red) that classifies AI operational status and triggers different supervisory responses per level [7]. At red, control is transferred to a conventional non-AI backup system, functionally removing the AI from the decision loop; at orange, supervisory checks intensify. The AI's advisory scope, however, is identical at green and orange—the intermediate level governs human supervisory behaviour, not AI recommendation content. The authors themselves state: *"To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner"* [7] — confirming the three-level design is novel, while stopping short of using the intermediate level to restrict AI output. Baxi formalises a K-tier permission architecture where permission sets vary by tier, but tiers are determined by the AI's own verified robustness, not by classified environmental state [15]. Vermaelen and Holvoet's Tumato 2.0 gates autonomous robot behaviour through an allowed(a,s) predicate, but as an absolute execution toggle — an action is either completely permitted or entirely blocked [16].

| Framework | Levels | Intermediate level exists? | AI advisory scope at intermediate level | AI status at maximum risk |
|---|---|---|---|---|
| Shields [8], GS AI [9], safety filter [10] | 2 (on/off) | No | — | Blocked |
| Flehmig et al. traffic-light [7] | 3 (green/orange/red) | Yes (orange) | Unchanged — full scope | Control transferred to non-AI backup |
| Baxi K-tier [15] | K tiers | Yes | Varies by AI robustness, not environmental state | — |
| Tumato 2.0 [16] | 2 (permit/block per action) | No | — | — |

**Table 1.** Governance patterns in the reviewed architectures.

*Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts (prompts, plans, tools, FMs) and pipeline stages. All actions are content-focused (block, filter, flag, modify, validate)—none condition AI advisory scope on environmental safety state.*

### 3.4 Fisheries and Low-Resource Deployment: The Gap Persists in the Application Domain

Haque and Al Jufaili confirm across four fisheries AI application domains that no system implements formal advisory scope restriction conditioned on environmental state [17]. Rahim et al. document that the only external advisory available to coastal fishers is a binary government warning to stop fishing [18]. Katende characterises low-resource AI deployment requirements as offline-first, computationally lightweight, and observable from locally available data, and identifies safety governance as a systematic gap: it has not been designed from the deployment floor [19]. Longobardi et al. demonstrate that analytics are achievable in data-deficient fisheries contexts (Peskas, Timor-Leste), but without a governance architecture [20]; Bhuvaneswari et al. show lightweight AI for safety-critical decisions is feasible in resource-constrained settings, also without one [21].

### 3.5 Synthesis: A Multiply-Confirmed Absence

Four independent sources confirm the same absence. First, the three large-scale surveys [5], [6], [7] collectively find no mechanism conditioning AI advisory scope on classified environmental safety state. Notably, Indykov et al.'s trade-off matrix records AT11 (rule-based models) → Safety = 0 — despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. Shamsujjoha et al.'s Swiss Cheese Model, the most comprehensive guardrails taxonomy synthesising 32 studies, identifies 13 guardrail actions and 14 quality attributes — none of which address environmental-risk-based scope restriction; their "context-dependent" rules refer to static deployment conditions (user location, regulatory jurisdiction, organisational policy), not dynamic environmental safety state [6]. Second, Flehmig et al.'s traffic-light index, the closest structural precedent, classifies AI degradation into three levels but uses the intermediate level to intensify supervisory checks while leaving AI output unchanged; at red, control transfers to a non-AI backup, functionally but not technically blocking the AI [7]. Third, Attard-Frost and Lyons' 610-topic empirical mapping of a national AI governance system contains no runtime state-conditioned advisory scope concepts; guardrails appear only in binary framing [22].

Across all bodies of literature reviewed, no system formally specifies an admissible recommendation space that contracts as classified environmental safety state worsens. Even three-level designs give the AI itself only two modes: fully on or blocked. The consequence in safety-critical decision support is a decision vacuum during marginal conditions: full-scope advice is produced when its evidential basis has degraded, with no architectural signal to the human operator that anything has changed [4].

---

## 4. CONCLUSION

This review establishes, from multiple independent bodies of literature, that AI governance in safety-critical decision support is binary by design: participation gating exists, advisory scope gating does not. The most comprehensive guardrails taxonomy in the field — Shamsujjoha et al.'s Swiss Cheese Model, synthesising 32 studies and identifying 13 guardrail actions and 14 quality attributes — contains no concept of restricting advisory scope as a function of environmental risk. The closest structural precedent, Flehmig et al.'s traffic-light index, changes human supervisory behaviour at its intermediate level but leaves AI output unchanged; at red, control transfers to a non-AI backup rather than blocking the AI directly. The identified gap — an admissible recommendation space A_AI(S) that contracts dynamically as classified operational risk increases — implies a specific research direction: a graduated safety-state-gated architecture in which a two-level governance pair (G(S), A_AI(S)) conditions both AI participation and AI advisory scope on a classified environmental safety state S = f(E), producing an intermediate CAUTION mode where the AI participates within a formally restricted scope, enforcing the containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. Grounded in Guaranteed Safe AI principles [9] and the dependability perspective of surrounding opaque AI components with deterministic guards [23], this direction is being pursued by the authors as a formally specified architecture for AI departure decision support in low-resource coastal fisheries, where the gap's consequences are most acute. The review's contribution is the gap itself: precisely characterised, confirmed from four independent sources, and open.

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

[13] G. Ramos et al., "Collaborative intelligence for safety-critical industries: A literature review," *Safety Science*, vol. 175, p. 106518, 2024.

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
