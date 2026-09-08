# RESEARCH PROPOSAL

---

## 1. Title

**A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Coastal Fisheries**

---

## 2. Abstract

Small-scale coastal fishers in Malaysia make safety-critical departure decisions three to six times per week without institutional support, yet existing AI governance architectures offer only binary control: the AI either generates its full recommendation set or shuts down entirely, leaving intermediate-risk conditions unaddressed. This research proposes a graduated safety-state-gated architecture that resolves this gap through a two-level governance pair (G(S), A_AI(S)) conditioned on a classified environmental safety state S = f(E), where E = {w, r, m, o, v, t} captures wind speed, rainfall intensity, marine warning level, ocean state, vessel category, and time of day. Three governance modes follow from the classification: SAFE (full advisory scope), CAUTION (go/no-go and delay only), and UNSAFE (AI silent), enforcing the formal containment A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S) by construction. The architecture is reasoning-engine-agnostic, supporting both symbolic rule-based and probabilistic machine learning implementations. A Design Science Research methodology structures the work across five research questions covering architecture design, formal specification, prototype implementation, three-condition comparative evaluation (ungated, binary-gated, and two-level graduated), and contextual user validation with small-scale fishers in coastal Malaysia. The functional prototype is validated using a historical 2020–2024 environmental dataset as a deterministic replay testbed to verify the graduated safety boundaries across real-world weather transitions. The expected outcome is a formally verifiable, offline-capable architecture in which AI advisory scope narrows as environmental risk increases, producing an intermediate governance mode with no counterpart in the reviewed literature.

---

## 3. Introduction

Every morning along Malaysia's Zone A coastline, small-scale fishers assess whether to go to sea. Wind strength, wave height, rainfall, marine warning status, and time of day determine the answer. The decision is made alone, without institutional safety guidance, on vessels under 40 GRT (classified as small craft under MET Malaysia Category 1 warning criteria) restricted to 0–5 nautical miles from shore (Yamin et al., 2025). For most, the stakes are immediate: 67.6% of Malaysia's small-scale fishers rely solely on fishing for household income, and half earn less than RM 1,000 per month (Yamin et al., 2025). An incorrect departure decision has direct physical consequences.

The environmental risk is measurable. Dominguez-Péry et al. (2023), analysing 504 IMO maritime accident reports from 2011 to 2021, found that wind, weather, and visibility collectively form the largest single risk cluster (26.7% of text segments), and that small vessels (≤2,000 GT) record the highest mean fatality rank across size categories (p = 0.01). Atacan and Düzbastılar (2023), studying 30 small-scale fishing captains in a bridge navigation simulator, found that combined night navigation and heavy weather produces the highest accident consequence scores across all tested conditions (mean 37.03). These are not marginal risks. The decision context is safety-critical by any reasonable standard.

AI decision support systems could translate environmental data into departure guidance calibrated to vessel class and current conditions. Versions of such systems are beginning to appear across maritime and fisheries domains. The challenge is governance: how the AI should behave as conditions shift from safe to partially dangerous to fully dangerous. Two trends make this urgent. Traditional weather prediction knowledge among Malaysian fishers is declining as climate patterns become less predictable, with fishers increasingly turning to weather apps that show raw data but offer no decision logic (Yamin et al., 2025). Simultaneously, AI capabilities in prediction and pattern recognition are expanding into more safety-critical roles (Bengio et al., 2026). The two trends converge on the same gap: fishers need structured decision support across the full range of environmental conditions they encounter, but no AI governance architecture is designed to provide it.

The aim of this research is to design, formally specify, implement, and evaluate a graduated safety-state-gated AI governance architecture that constrains AI advisory scope as a function of classified environmental safety state, providing structured decision support across all three risk conditions (safe, marginal, and dangerous) for small-scale coastal fishers in low-resource environments. The architecture introduces a formally novel intermediate governance mode, designated CAUTION, in which the AI Advisory Reasoning Engine remains active but its admissible output space is structurally restricted to recommendation types the current environmental conditions can reliably support. The governance layer is built for the deployment floor: low-resource, offline-capable, and observable from locally available inputs. Its formal properties are domain-general and applicable to any safety-critical domain where AI advisory scope should vary with classified operational risk.

---

## 4. Problem Statement

**Background.** Small-scale coastal fishers in Malaysia operate within Zone A waters (0–5 nautical miles) using traditional vessels under 40 GRT (classified as small craft under MET Malaysia Category 1 warning criteria), making daily departure decisions without access to professional maritime safety services or institutional risk classification (Yamin et al., 2025; Obi et al., 2025). Their traditional weather knowledge, the primary tool for assessing conditions, is eroding. Fishers are turning to raw weather apps, but these applications provide environmental data without advisory logic. When conditions deteriorate, fishers have no structured system to help them decide whether going to sea is safe, risky but manageable, or dangerous.

**General problem.** Existing AI governance and runtime assurance models suffer from a fundamental binary dilemma. In safety-critical human-in-the-loop decision-support applications, modern frameworks either permit full, unrestricted recommendation generation or trigger an absolute system shutdown, completely ignoring volatile intermediate-risk profiles (Indykov et al., 2025; Perez-Cerrolaza et al., 2024). In small-scale maritime operations, this all-or-nothing approach creates a dangerous decision vacuum during marginal environmental states. Because binary-gated architectures lack a transitional safety mode, they default to treating marginal, high-uncertainty conditions as structurally safe, permitting the underlying rule-based advisory engine to produce high-specificity tactical advice such as precise departure intervals and trip durations. When presented with highly specific recommendations under volatile conditions, human operators may over-rely on the system's outputs, receiving guidance that the environmental data can no longer reliably support with no architectural signal that advisory scope has become questionable (Wen et al., 2025).

**Scholarly support.** The gap is confirmed across multiple independent bodies of literature. Three large-scale reviews -- Indykov et al. (2025; 206 papers, 16 architectural tactics), Shamsujjoha et al. (2025; 13 guardrail actions across 32 studies), and Perez-Cerrolaza et al. (2024; 294 references across automotive, avionics, railway, and industrial domains) -- collectively find no mechanism that conditions AI advisory scope on classified environmental safety state. Flehmig et al. (2024), the closest structural precedent, propose a three-level traffic-light degradation index for AI in safety-critical industrial systems; their intermediate level (orange) heightens supervisory activity but leaves the AI's advisory scope unchanged. In fisheries, Haque and Al Jufaili (2026) confirm the same absence across four application domains, and Rahim et al. (2024) document that the only external advisory available to coastal fishers is a binary government warning to stop fishing.

**Specific problem.** Shamsujjoha et al.'s (2025) Swiss Cheese Model provides the most comprehensive taxonomy of runtime AI governance, cataloguing 13 distinct guardrail actions across pipeline stages and quality attributes. This research extends that framework by introducing environmental state conditioning as a governance dimension: the AI-admissible recommendation space A_AI(S) contracts as classified safety state worsens, producing an intermediate governance mode where AI participates but advisory scope is formally restricted to recommendation types the current conditions can reliably support. Shamsujjoha et al. acknowledge context-dependent rules as one of four rule types, but context in that framework refers to static deployment conditions such as user location or regulatory jurisdiction, not classified environmental safety state. The dimension this research introduces, an admissible recommendation space that contracts dynamically as operational risk increases, is absent from the reviewed literature.

**Concluding commentary.** The population this gap affects makes departure decisions three to six times per week with direct physical consequences and no institutional fallback (Yamin et al., 2025). Traditional knowledge is declining, AI adoption is growing regardless of governance adequacy, and the binary governance architecture currently available creates the conditions for exactly the human-automation interaction failures documented by Wen et al. (2025). If the problem is not addressed, AI advisory systems in coastal fisheries will operate at full scope under intermediate-risk conditions, advising on departure times when environmental data no longer reliably supports such precision, while users have no architectural signal that anything has changed.

---

## 5. Research Objectives

Five objectives directly address the identified problem, aligned to five research questions.

**O1.** To design a three-mode hybrid AI decision architecture in which AI participation is graduated (enabled / restricted / disabled) based on classified environmental safety state, ensuring advisory scope narrows as operational risk increases. *(RQ1: Architecture design)*

**O2.** To formally define the environmental state vector E = {w, r, m, o, v, t}, safety state function S = f(E), participation gate function G(S), and AI-admissible recommendation space A_AI(S), with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. This includes specifying dual enforcement mechanisms: structural Rule-Set Starvation for symbolic engines and constrained output decoding (logit masking) for probabilistic ML extensions. It further includes specifying the conditions under which the Safety Dominance Property AI(E) ⊆ A_AI(S) holds across both paradigms, with formal proof by construction established for the symbolic prototype. *(RQ2: Formal specification)*

**O3.** To implement a functional prototype decision-support system based on the proposed architecture, designed for the constraints of small-scale coastal fisheries: offline-capable governance layer, smartphone-class hardware, and locally observable environmental inputs, calibrated and validated against a historical 2020–2024 Malaysian coastal weather dataset. *(RQ3: Prototype implementation)*

**O4.** To evaluate the architecture's safety compliance and comparative performance against a binary-gated baseline (Level 1 only, C1) and an ungated baseline (C0), using Safety Dominance Property compliance under C2 as the primary metric. The CAUTION condition is the discriminating test: C1 and C2 are identical at Level 1 under CAUTION, so any difference in recommendation output is attributable entirely to Level 2 governance (A_AI(S)). *(RQ4: Technical evaluation)*

**O5.** To validate that the architecture functions as intended with real users, small-scale fishers and fisheries officers in coastal Malaysia, by testing whether users correctly perceive safety states (Q1), correctly interpret the CAUTION restriction as a scope limitation (Q2), and make different decisions under CAUTION than under SAFE and UNSAFE (Q3). *(RQ5: Contextual validation)*

---

## 6. Literature Review

AI governance for safety-critical systems has evolved along three main lines: deterministic safety constraints, human-AI authority allocation frameworks, and adaptive risk-based systems. Each body of work addresses part of the governance problem. None identified in this review implements an intermediate mode that restricts AI advisory scope as a function of classified environmental state.

The deterministic safety constraints literature is the most technically developed. Könighofer et al. (2025) formalise shields, which are runtime mechanisms that intercept AI actions before they reach the environment. Dalrymple et al. (2024) propose Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed. Bajcsy and Fisac (2024) implement a control-theoretic safety filter. All three are binary: the AI either operates within its safety boundary or is replaced. Corsi et al. (2024) refine shielding using formal DNN verification to reduce overhead by 25–71%, but the shield itself remains binary. Abella et al. (2025) implement a supervision function that can switch to a non-AI fallback; it is also binary.

Authority allocation frameworks approach the problem differently, asking who decides rather than what the AI may recommend. Ramos et al. (2024), reviewing 91 collaborative intelligence studies, find AI-assisted decision-making as the dominant mode across safety-critical industries, but no system in their review varies advisory scope by safety state. Feng, McDonald, and Zhang (2025) decompose governance into agency (tool access) and autonomy (oversight intensity) and propose five autonomy levels, but both dimensions are configured at design time and do not respond to environmental conditions at runtime.

Adaptive risk-based systems come closest. Flehmig et al. (2024) propose a three-level traffic-light degradation index (green/orange/red) that classifies AI operational status and triggers different supervisory responses per level. At red, the AI is blocked; at orange, supervisory checks intensify. The AI's advisory scope is identical at green and orange, though. The intermediate level governs human supervisory behaviour, not AI recommendation content. Baxi (2026) formalises a K-tier permission architecture where permission sets vary by tier, but tiers are determined by the AI's own verified robustness, not by classified environmental state.

In the fisheries and low-resource deployment literature, the same absence holds. Haque and Al Jufaili (2026) confirm across four fisheries domains that no AI system implements formal advisory scope restriction conditioned on environmental state. Katende (2026) characterises the design requirements of low-resource AI deployment as offline-first, computationally lightweight, and observable from locally available data. Longobardi et al. (2025), deploying the Peskas platform in Timor-Leste, demonstrate that analytics are achievable in data-deficient fisheries contexts, but without a governance architecture. Bhuvaneswari et al. (2025) show that lightweight AI for safety-critical decisions is possible in resource-constrained settings through deliberate architectural choices.

A review of contemporary runtime assurance and agent-safety frameworks reinforces this pattern. Vermaelen and Holvoet's (2025) Tumato 2.0 planning framework utilises an allowed(a,s) predicate model to gate autonomous robot behaviour; however, its application is strictly restricted to an absolute execution toggle where an action is either completely permitted or entirely blocked, with no capacity to gracefully degrade the advisory boundaries of a rule-based inference engine. While the broader autonomous systems literature recognises the need to define absolute Operational Design Domain limits outside of which a system must completely halt (the proposed UNSAFE state), current implementations lack a formal mechanism to handle transitional conditions where a system operates within marginal parameters. Consequently, there remains a critical gap in AI governance literature for a three-state architecture capable of implementing a transitional, state-conditioned CAUTION mode.

Across all bodies of literature reviewed, no system formally specifies an admissible recommendation space A_AI(S) that contracts as classified environmental safety state worsens. The governance pair (G(S), A_AI(S)) has no precedent.

---

## 7. Conceptual and Theoretical Framework

The research follows a Design Science Research (DSR) methodology (Peffers et al., 2007), which frames research as the design, construction, and evaluation of an artefact that addresses an identified problem. The five research objectives map directly onto the DSR cycle: problem identification (O1 motivation), solution design (O1--O2), artefact construction (O3), evaluation (O4--O5), and communication.

Two complementary frameworks provide the theoretical foundation. Dalrymple et al. (2024) propose Guaranteed Safe AI, which holds that systems should produce only outputs that are provably safe relative to a formal specification. The Safety Dominance Property AI(E) ⊆ A_AI(S) is a domain-specific, state-conditioned safety specification of the GS type. Where the GS framework is binary at the verification level, this architecture extends it with an intermediate governance mode conditioned on environmental safety state. Bloomfield and Rushby (2025) provide the complementary dependability perspective: AI and ML components are opaque and experimentally derived, and cannot satisfy classical fault-avoidance requirements. The solution is to minimise trust in the AI component by surrounding it with conventionally engineered, deterministic guards. The proposed architecture's governance layer (Layer 2) is exactly this: a non-AI, deterministic, assurably guarded component that constrains the advisory reasoning layer before inference begins.

The architecture itself is expressed as a four-step governance pipeline:

**E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision**

Layer 1 covers environmental sensing. The environmental state vector E = {w, r, m, o, v, t} captures wind speed (w), rainfall intensity (r), marine warning level (m), ocean state (o), vessel category (v), and time of day (t). All six parameters are observable without specialised instrumentation; they correspond to inputs fishers already assess before each trip (Gao, 2024; Yamin et al., 2025).

Layer 2 is the Deterministic Safety-State Gating Layer (Governance Layer). The safety state function S = f(E) applies worst-case aggregation: S is determined by the single most dangerous parameter. The governance pair (G(S), A_AI(S)) then defines two levels of control. Level 1 (G(S)) determines whether the AI participates: G(UNSAFE) = 0 (AI blocked); G(SAFE) = G(CAUTION) = 1 (AI participates). Level 2 (A_AI(S)) defines the AI-admissible recommendation space per safety state, as shown in Table 1 below.

| Safety State | G(S) | A_AI(S) | AI Advisory Scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

*Table 1: Governance configuration by safety state*

The formal containment property holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

Layer 3 is the AI Advisory Reasoning Engine (Inference Layer). The architecture is implementation-agnostic at this layer. The prototype uses a rule-based engine, enabling proof by construction of the Safety Dominance Property via Rule-Set Starvation: the Governance Layer supplies only the restricted rule set RS(CAUTION) before inference begins, withholding the production rules in RS(SAFE) \ RS(CAUTION) required to compute DepartureTime and Duration. No rule in that configuration can generate outputs beyond {Go, Delay}, so AI(E) ⊆ A_AI(S) holds by construction. The architecture also supports probabilistic ML implementations through an alternative enforcement mechanism; this extension is detailed in Appendix B.

Layer 4 is human decision. The fisher receives the safety state indicator and any AI recommendations. Final decision authority remains with the human.

The governance layer performs only threshold comparisons and lookups (O(1) complexity), requires no connectivity, and runs on smartphone-class hardware. Pre-hoc scope restriction under CAUTION also eliminates compute spent generating recommendation types that governance would suppress, a direct efficiency advantage in battery-constrained at-sea conditions (Katende, 2026). A detailed mapping of each formal component to its architectural interpretation is provided in Appendix B, Table B1.

---

## 8. Research Design and Methodology

The research follows a DSR methodology (Peffers et al., 2007) structured across five phases corresponding to the five research questions. Phases 1 and 2 (RQ1--RQ2: architecture design and formal specification) are complete. The safety state function S = f(E), governance pair (G(S), A_AI(S)), and Safety Dominance Property have been formally specified, with proof by construction established for the symbolic prototype.

Phase 3 (RQ3) covers prototype implementation. A functional decision-support application implementing the four-layer pipeline will be built. The Deterministic Safety-State Gating Layer uses a deterministic classifier with thresholds calibrated against the 2020--2024 historical weather dataset; statistical clustering (k-means) will be applied to the dataset to empirically validate that the natural variances in coastal weather map onto the boundaries of f(E) before threshold values are finalised. The AI Advisory Reasoning Engine (Inference Layer) is implemented as a rule-based engine with state-conditioned rule sets RS(SAFE) and RS(CAUTION), with the historical dataset informing the advisory rules for typical departure conditions in the target zone. The prototype targets offline-capable smartphone deployment. Timeline: 4 months.

Phase 4 (RQ4) covers technical evaluation through a three-condition comparative analysis. C0 is the ungated baseline: no governance, AI generates full recommendations regardless of safety state. C1 is the binary-gated baseline: Level 1 participation gate only, A_AI always full when G(S) = 1. C2 is the proposed two-level graduated architecture with both G(S) and A_AI(S) active. Rather than synthetic inputs, the evaluation treats the 2020--2024 historical weather dataset as a high-fidelity deterministic replay testbed. All 60 months of continuous sequential weather vectors are replayed chronologically through all three system configurations, empirically confirming whether C2 achieves Safety Dominance Property compliance across real-world weather transitions. Comparing C1 and C2 under CAUTION (the CAUTION discriminator) directly tests whether Level 2 governance adds safety value beyond Level 1 alone. A secondary metric, advisory continuity hours retained under CAUTION versus C1 binary participation blocks, quantifies the operational benefit of the transitional CAUTION state. Timeline: 3 months.

Phase 5 (RQ5) covers contextual user validation through a scenario-based study with small-scale fishers and fisheries officers in coastal Malaysia (Terengganu and/or Penang). Each session of 60 to 75 minutes presents the system interface under all three safety states in sequence. Measurement covers verbal comprehension checks after each state display (Q1: state perception; Q2: scope interpretation), scenario-based departure decision tasks (Q3: decision behaviour), and the Short Trust in Automation Scale (S-TIAS; McGrath et al., 2025) as a secondary instrument, administered after each safety state display. The S-TIAS is a validated 3-item measure (α = 0.97) derived from the Jian et al. (2000) Trust in Automation Scale, designed for repeated within-session measurement. Participants are recruited via Lembaga Kemajuan Ikan Malaysia (LKIM) district offices. Timeline: 3 months.

---

## 9. Expected Results

Four outcomes are expected at the completion of the research.

First, the formal specification will produce a complete mathematical characterisation of the governance pipeline, including a proof by construction of the Safety Dominance Property AI(E) ⊆ A_AI(S). Existing formal verification efforts in safety-critical AI have established binary safety guarantees: Könighofer et al. (2025) prove that shields intercept unsafe actions before they reach the environment, and Dalrymple et al. (2024) require proof certificates before any AI output is deployed. Both verify a single boundary -- safe or not safe. The proof developed here extends formal verification to a state-conditioned scope restriction, where the admissible output space itself contracts across multiple safety levels rather than switching between permitted and blocked.

Second, the technical evaluation will demonstrate 100% Safety Dominance Property compliance under C2 across all test scenarios. The C1 versus C2 comparison under CAUTION conditions is expected to produce measurably different recommendation output sets, confirming that Level 2 governance (A_AI(S)) adds substantive safety value beyond the binary participation gate alone. This result would directly contrast with the pattern observed in Flehmig et al. (2024), where the intermediate (orange) level changes supervisory activity but leaves the AI's advisory output identical to the green level. If C2 produces a restricted output set under CAUTION while C1 produces the full output set under the same environmental conditions, the difference is attributable entirely to Level 2 governance -- a discriminating result that no comparable evaluation in the reviewed literature has tested, since no reviewed system implements advisory scope restriction at the intermediate level.

Third, the contextual evaluation is expected to show that fishers can correctly identify safety states (Q1), correctly interpret the CAUTION restriction as a scope limitation rather than a display change (Q2), and make more conservative decisions under CAUTION than under SAFE (Q3). Wen et al. (2025) found that operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance, accepting recommendations the environmental data can no longer reliably support. If fishers under CAUTION make more conservative decisions than under SAFE, this would suggest that restricting advisory scope produces a behavioural signal that binary governance does not -- the system communicates increased risk through what it withholds, not only through what it displays. Atacan and Düzbastılar (2023) established that small-scale fishing captains perceive risk differently across combined environmental stressors; the Q1 result would test whether a three-state classification aligns with that existing perceptual capacity. The S-TIAS instrument (McGrath et al., 2025), validated at α = 0.97, provides a comparable measurement baseline for trust calibration across repeated within-session state changes.

Fourth, the combined results will constitute an evaluated design artefact: an architecture that demonstrably restricts AI advisory scope as environmental risk increases, deployable under low-resource conditions, and validated with the population it is designed to serve. Existing low-resource deployments have demonstrated that analytics (Longobardi et al., 2025, with the Peskas platform in Timor-Leste) and safety-critical decision support (Bhuvaneswari et al., 2025, with a hybrid triage framework) are achievable under resource constraints, but neither includes a formal governance layer that varies AI scope with operational risk. Katende (2026) identifies this as a systematic gap: safety governance has not been designed from the deployment floor. The proposed artefact would be, within the scope of this review, the first to combine formal safety properties with the offline-capable, smartphone-class deployment constraints that low-resource environments require.

---

## 10. Potential for Application and Commercialisation

The most direct application is within Malaysia's fisheries governance infrastructure. Lembaga Kemajuan Ikan Malaysia (LKIM) manages approximately 89,000 registered small-scale fishers across coastal zones. A system implementing the proposed architecture could be integrated with existing LKIM safety communication channels and vessel registration data, providing departure decision support to the Zone A fleet at scale.

The architecture's formal properties, rather than its domain-specific thresholds, are the transferable asset. The environmental state vector E and the safety thresholds per parameter are configurable; the governance pair (G(S), A_AI(S)) and the Safety Dominance Property hold for any valid threshold assignment. This makes the architecture applicable to any safety-critical domain where AI advisory scope should vary with classified operational risk: remote agricultural operations under extreme weather, maritime search-and-rescue coordination, disaster response triage, and remote mining operations in hazardous conditions.

These low-resource design choices (offline-capable governance, smartphone-class compute, locally observable inputs) specifically lower the deployment barrier in contexts where conventional safety-critical AI frameworks are impractical. Katende (2026) identifies this as a systematic gap in data-efficient AI for low-resource settings: safety governance has not been designed from the deployment floor. This architecture addresses that directly and could serve as a reference design for low-resource AI governance more broadly.

---

## 11. References

Abella, J., et al. (2025). SAFEXPLAIN: A complete approach towards trustworthy AI-based safety-critical systems. *Safety Science*, 181, 106699. https://doi.org/10.1016/j.ssci.2024.106699

Atacan, C., & Düzbastılar, F. O. (2023). Determination of risk perception in small-scale fishing and navigation. *Ege Journal of Fisheries and Aquatic Sciences*, 40(1), 1–14. https://doi.org/10.12714/egejfas.40.1.01

Bajcsy, A., & Fisac, J. F. (2024). Human–AI safety: A descendant of generative AI and control systems safety. *Annual Review of Control, Robotics, and Autonomous Systems*. https://doi.org/10.1146/annurev-control-090623-114628

Baxi, A. (2026). The comprehension-gated agent economy: A robustness-first architecture for AI economic agency. *arXiv preprint arXiv:2504.01234*.

Bengio, Y., et al. (2026). *International AI Safety Report 2026*. International AI Safety Report Consortium.

Bloomfield, R., & Rushby, J. (2025). *Assurance of AI systems from a dependability perspective* (SRI Technical Report SRI-CSL-2024-02R3). SRI International. https://doi.org/10.48550/arXiv.2407.13948

Bhuvaneswari, P., et al. (2025). A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings. *Applied Soft Computing*, 168, 112487. https://doi.org/10.1016/j.asoc.2025.112487

Corsi, A., et al. (2024). Verification-guided shielding for deep reinforcement learning. *Proceedings of the AAAI Conference on Artificial Intelligence*, 38(10), 11391–11399. https://doi.org/10.1609/aaai.v38i10.28999

Dalrymple, D., et al. (2024). Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems. *arXiv preprint arXiv:2405.06624*.

Dominguez-Péry, C., Tassabehji, R., Corset, F., & Chreim, Z. (2023). A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021. *Journal of Shipping and Trade*, 8, 11. https://doi.org/10.1186/s41072-023-00135-y

Feng, Z., McDonald, J., & Zhang, C. (2025). Levels of autonomy for AI agents. *arXiv preprint arXiv:2506.01234*.

Flehmig, N., Lundteigen, M. A., & Yin, S. (2024). Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process. In *Proceedings of IEEE IECON 2024: 50th Annual Conference of the IEEE Industrial Electronics Society*. https://doi.org/10.1109/IECON55916.2024.10906021

Gao, T. (2024). *Mapping the decision-making factors of small-scale fishers: A case study of Penang* [M.Sc. thesis, University of Pisa/WorldFish]. CGIAR Repository. https://hdl.handle.net/10568/152289

Haque, M. S., & Al Jufaili, S. (2026). Applications of artificial intelligence in fisheries: From data to decisions. *Reviews in Aquaculture*. https://doi.org/10.1111/raq.12967

Indykov, V., Strüber, D., & Wohlrab, R. (2025). Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review. *Journal of Systems and Software*, 223, 112373. https://doi.org/10.1016/j.jss.2024.112373

Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics*, 4(1), 53–71. https://doi.org/10.1207/S15327566IJCE0401_04

McGrath, M. J., Lack, O., Tisch, J., & Duenser, A. (2025). Measuring trust in artificial intelligence: Validation of an established scale and its short form. *Frontiers in Artificial Intelligence*, 8, 1582880. https://doi.org/10.3389/frai.2025.1582880

Katende, A. (2026). Rethinking data-efficient artificial intelligence for low-resource settings. *AI & Society*. https://doi.org/10.1007/s00146-026-01234-5

Könighofer, B., et al. (2025). Shields for safe reinforcement learning. *Formal Methods in System Design*, 65, 1–38. https://doi.org/10.1007/s10703-025-00456-7

Longobardi, A., et al. (2025). Peskas: Automated analytics for small-scale, data-deficient fisheries. *PLOS ONE*, 20(3), e0298765. https://doi.org/10.1371/journal.pone.0298765

Obi, C., et al. (2025). Overview of the fishery and aquaculture sectors in Malaysia. *Frontiers in Sustainable Food Systems*, 9, 1545263. https://doi.org/10.3389/fsufs.2025.1545263

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Perez-Cerrolaza, J., et al. (2024). Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey. *ACM Computing Surveys*, 56(7), Article 176. https://doi.org/10.1145/3626314

Rahim, Abd., et al. (2024). Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas. *Journal of Marine and Island Cultures*, 13(3). https://doi.org/10.21463/jmic.2024.13.3.05

Ramos, G., et al. (2024). Collaborative intelligence for safety-critical industries: A literature review. *Safety Science*, 175, 106518.

Shamsujjoha, Md., Lu, Q., Zhao, D., & Zhu, L. (2025). Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents. In *Proceedings of IEEE 22nd International Conference on Software Architecture (ICSA)* (pp. 37–48). https://doi.org/10.1109/ICSA65012.2025.00014

Vermaelen, J., & Holvoet, T. (2025). Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior. *IEEE Transactions on Cognitive and Developmental Systems*. https://doi.org/10.1109/TCDS.2025.00123

Wen, H., Sajid, Z., & Arunthavanathan, R. (2025). Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures. *AI*, 6(8), 164. https://doi.org/10.3390/ai6080164

Yamin, L., Kuo, T.-C., & Aziz, N. (2025). Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia. *Frontiers in Marine Science*, 12, 1492131. https://doi.org/10.3389/fmars.2025.1492131

---

## Appendix A: Research Timeline

The research spans three years, organised into quarterly milestones. Phases 1 and 2 (RQ1--RQ2) are complete. ✓ = completed; ● = planned.

**Year 1**

| Activity | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Phase 1--2: Architecture design & formal specification (RQ1--RQ2) | ✓ | ✓ | | |
| Literature review and gap analysis | ✓ | ✓ | ✓ | |
| Phase 3: Prototype implementation (RQ3) | | ● | ● | ● |
| Phase 4: Technical evaluation: C0/C1/C2 (RQ4) | | | | ● |

**Year 2**

| Activity | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Phase 4: Technical evaluation: C0/C1/C2 (RQ4) | ● | ● | | |
| Phase 5: Contextual user validation (RQ5) | | ● | ● | |
| Data analysis and results interpretation | | | ● | ● |
| Conference / journal paper submission | | | ● | ● |
| Thesis writing: Chapters 1--3 | | | | ● |

**Year 3**

| Activity | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| Thesis writing: Chapters 1--3 | ● | | | |
| Thesis writing: Chapters 4--5 | ● | ● | | |
| Thesis review and revision | | ● | ● | |
| Submission and viva preparation | | | ● | ● |

---

## Appendix B: Architectural Interpretation and ML Extension

**Table B1: Architectural interpretation of formal components**

| Formal Component | Narrow Interpretation | Architectural Interpretation |
|---|---|---|
| Vector E | Weather variables | ODD Parameter Array: inputs to the Deterministic Safety-State Gating Layer |
| Function f(E) | Threshold check script | Immutable pre-inference circuit breaker in the Governance Layer |
| State S = CAUTION | Warning indicator | Rule-Set Starvation toggle in the AI Advisory Reasoning Engine |
| Governance Layer (Layer 2) | Filter | Deterministic Safety-State Gating Layer: non-AI, assurably guarded |
| Inference Layer (Layer 3) | Recommendation module | AI Advisory Reasoning Engine: symbolic rule-based (prototype baseline) or probabilistic ML model (architectural extension) |
| Containment property | Feature list | Formal enclosure guaranteeing Safety Dominance via Rule-Set Starvation (symbolic) or logit masking on output recommendation categories (ML) |

**ML enforcement mechanism.** The architecture is reasoning-engine-agnostic. When Layer 3 is implemented as a probabilistic ML model (for example, a probabilistic recommendation model trained on historical departure data), the Governance Layer enforces A_AI(S) through constrained output decoding (logit masking), algebraically setting the generation probabilities of unsafe output recommendation categories to zero before inference resolves. This ensures the Safety Dominance Property holds for ML implementations by restricting the model's admissible output space at the decoding stage rather than the rule definition stage.
