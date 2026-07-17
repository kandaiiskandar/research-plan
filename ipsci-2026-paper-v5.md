# FROM BINARY TO GRADUATED AI GOVERNANCE: THE ADVISORY SCOPE GAP IN SAFETY-CRITICAL DECISION SUPPORT AND A PROPOSED ARCHITECTURE

**Iskandar Samsuddin \*1**

1 [Department], [Faculty], [University], Malaysia
\* Corresponding author: iskandarsamsuddin@gmail.com

---

***Abstract:*** AI decision support is expanding into safety-critical, human-in-the-loop settings, yet how AI advisory behaviour should change as operational conditions deteriorate remains an open governance question. This paper reviews the AI governance, runtime assurance, human-AI collaboration, and fisheries/low-resource literature to establish whether any existing architecture restricts AI advisory scope as a function of classified environmental safety state. The review finds that existing governance mechanisms are uniformly binary: the AI either generates its full recommendation set or is blocked entirely. Mechanistic evidence from the LLM systems and cognition literatures indicates that this limitation cannot be remedied within the AI component itself: the inference pipeline is structurally fixed, reasoning exploration is a property of the decoding procedure rather than a content-conditioned adaptation, and self-assessed confidence is unreliably calibrated and insensitive to past performance. Internal self-restraint cannot be relied upon; state-conditioned restraint must be imposed by an external architectural layer. Indykov et al. (206 papers, 16 architectural tactics), Shamsujjoha et al. (13 guardrail actions across 32 studies), and Perez-Cerrolaza et al. (294 references across safety-critical domains) [5], [6], [24] contain no mechanism that conditions AI advisory scope on classified environmental safety state. The closest architectural precedents are split by operational paradigm: Flehmig et al.'s three-level traffic-light degradation index (the closest advisory-governance precedent) changes human supervisory behaviour at its intermediate level but leaves AI advisory output unchanged, while Sahoo's five-level framework (the closest behavioural precedent) restricts autonomous action classes but governs an executing military agent rather than a human-facing recommendation menu. The review identifies a specific gap: prior research provides robust mechanisms for whether the AI operates (participation gating) and which actions an autonomous agent may execute (action-class restriction), but the distinct dimension of what the AI is permitted to recommend to a human decision-maker (an admissible recommendation space that contracts as classified operational risk increases) remains unaddressed in the reviewed literature. In low-resource safety-critical domains such as small-scale coastal fisheries, binary governance leaves intermediate-risk conditions structurally unaddressed: a fisher in marginal weather receives either full-scope tactical recommendations or none at all. A graduated governance architecture addresses this gap through a participation gate G(S) and an advisory gate A_AI(S), both conditioned on the current environmental safety state S, producing an intermediate CAUTION mode in which the AI advises within a formally restricted scope.

***Keywords:*** AI governance, safety-critical systems, decision support, graduated architecture, coastal fisheries

---

## 1. INTRODUCTION

AI decision support is expanding into safety-critical, human-in-the-loop settings across domains including healthcare, industrial operations, autonomous transportation, and maritime activity. In these settings the AI does not act autonomously: it generates recommendations that a human decision-maker weighs and acts upon. Governance frameworks for such systems determine when the AI may participate in a decision and what safeguards surround its output. The governance that accompanies this expansion, however, is demonstrably under-delivered in practice: in the largest survey of responsible AI adoption to date (1,000 organizations across 20 industries and 19 regions), Reuel et al. found that while 9% of organizations reach the highest stage of organizational AI governance maturity (policies, structures, risk processes), only 0.8% reach it operationally, and none reach both, a systematic gap between governance planning and execution that the authors warn "could lead to increased (public) risks from AI systems" [31]. Governance that depends on organizational processes being faithfully executed cannot, on this evidence, be relied upon; the burden of safety therefore falls on the architecture of the AI system itself. Yet a fundamental architectural question remains unresolved: how should AI advisory behaviour change as operational conditions deteriorate from safe, through marginal, to dangerous?

Existing frameworks address only the endpoints of this continuum: full recommendation generation or complete shutdown. The intermediate range is unaddressed. When binary-gated architectures encounter marginal conditions, they treat them as structurally safe, permitting full-scope tactical advice such as precise departure intervals; operators receiving full-scope AI output under deteriorating conditions tend toward over-reliance, accepting recommendations the environmental data can no longer reliably support [4]. This review examines one specific component of the governance problem: whether any existing mechanism restricts what an AI may recommend, as distinct from whether the AI may participate at all.

The question is particularly acute in low-resource, safety-critical domains, those furthest from the well-resourced organizations where even partial governance maturity is concentrated [31]. In such settings there is no institutional layer, no control room, supervisor, or compliance function, to compensate for a governance failure in the tool itself: whatever governance the system embodies is all the governance the operator has. Each morning, 89,000 registered small-scale fishers along Malaysia's coastline face a safety-critical decision: go to sea or stay ashore. They make this decision alone, without institutional support, on vessels under 40 GRT restricted to 0–5 nautical miles from shore, relying on traditional weather knowledge that is eroding as climate patterns become less predictable [1]. The measurable environmental risk profile of this domain is reviewed in Section 4.5.

Runtime governance frameworks determine whether AI may participate in a decision. Autonomy research determines which actions an autonomous agent may execute. Neither addresses what AI may recommend to a human decision-maker as operating conditions deteriorate. This paper takes up that third question.

It makes two contributions. First, it establishes from a structured literature review of 71 papers that existing architectures govern whether the AI participates, but not what it may recommend as conditions deteriorate (a gap confirmed from four independent bodies of literature and developed fully in Section 4.6) and shows, from mechanistic evidence on how generative AI systems process information, why this gap cannot be closed within the AI component itself. Second, it outlines a graduated safety-state-gated governance architecture that the identified gap implies. The paper proceeds as follows: Section 2 defines the key concepts used throughout; Section 3 describes the review methodology; Section 4 reviews the literature in three stages: the existing governance paradigms (4.1–4.5), a cross-paradigm synthesis characterising the research gap (4.6), and the mechanistic basis for external governance (4.7); Section 4.8 states the study objectives that follow from the gap; Section 5 outlines the proposed architecture; Section 6 concludes.

---

## 2. KEY CONCEPTS

Five concepts recur throughout this review and are defined here to fix terminology.

An **AI decision support system** generates recommendations for a human decision-maker who retains final decision authority; it is distinct from an autonomous agent, which executes actions directly. A **safety-critical system** is one in which incorrect or inappropriately scoped output can contribute to harm to human life, health, or property. **Runtime governance** refers to mechanisms that constrain AI behaviour during operation, as distinct from design-time controls such as training, fine-tuning, or static configuration. Within runtime governance, this paper separates two dimensions: **participation gating** (whether the AI participates in the decision at all) and **advisory scope** (the set of recommendation types the AI is permitted to generate while participating). Advisory scope restriction is the contraction of that set (dimension 2, Figure 1). Finally, an **environmental safety state** is a classified summary S of an environmental observation vector E, produced by a classification function S = f(E) that is computed independently of the AI component; a **low-resource environment** is a deployment context lacking reliable connectivity, computing infrastructure, and institutional support, imposing offline-first and computationally lightweight requirements on any deployed system.

**Figure 1.** Three governance dimensions in AI decision support systems. Dimensions 1 and 3 appear in existing work; dimension 2 is the gap this paper addresses.

```
Governance Dimension 1 — Participation
Whether the AI may operate
(addressed by: shields, safety filters, binary gates)

          ↓

Governance Dimension 2 — Advisory Scope          ← this paper
What the AI is permitted to recommend
(the admissible recommendation space A_AI(S))

          ↓

Governance Dimension 3 — Execution
Which actions an autonomous agent may take
(addressed by: action-class restriction, autonomy levels)
```

---

## 3. METHODOLOGY

This study adopts a Structured Literature Review (StLR) approach, structured rather than systematic: search and coding are disciplined, but the scope is purposive, covering only the bodies of literature where such a mechanism could plausibly appear. The central question is whether any existing architecture restricts an AI system's advisory scope as a function of classified environmental safety state. A systematic review promises completeness and reproducibility; this one promises analytical rigour and transparent reasoning. Reviewers should apply the latter standard.

### 3.1 Search Strategy

Papers were retrieved from Scopus, IEEE Xplore, Web of Science, and ACM Digital Library. Primary search strings included 'AI governance', 'runtime assurance', 'safety filter', 'advisory scope', 'decision support', 'human-AI collaboration', 'autonomy levels', 'guardrails', 'action restriction', and 'AI safety-critical'. Secondary searches for the application domain used 'fisheries AI', 'maritime decision support', and 'low-resource AI deployment'. The search was not date-bounded, though results were weighted toward 2022–2026.

An initial candidate set was assembled through iterative database searches. Three large-scale systematic reviews within that set were retained as secondary evidence: Indykov et al. [5] (206 papers and 16 architectural tactics), Shamsujjoha et al. [6] (13 guardrail actions across 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references covering safety-critical domains). Their reviewed corpora extend coverage to several hundred additional primary studies without requiring individual screening. Papers were then added through backward and forward citation tracing until no new governance mechanisms or architectural patterns emerged. 71 papers proceeded to full review.

### 3.2 Screening, Inclusion, and Coding

Screening proceeded in two stages. At the title and abstract stage, a paper was included if it addressed a mechanism that constrains or shapes AI behaviour during operation, targeted a safety-critical or human-in-the-loop context, or addressed AI deployment in low-resource or resource-constrained environments. Papers dealing only with training-time, fine-tuning, or static-configuration approaches with no runtime governance component were excluded. 71 papers were retained for full review.

Each retained paper was coded on the following four dimensions:

| Dimension | Values |
|---|---|
| **Primary governance target** | Participation / Advisory scope / Execution / Oversight |
| **Runtime adaptation** | Binary (on/off) / Graduated (3+ levels) / None |
| **Conditioning variable** | Environmental state / AI robustness / Task risk / Human authority / None |
| **Recommendation restriction** | Yes (bounded output set) / No |

Table 1 in Section 4.4 presents the full coding of all frameworks that implement graduated adaptation.

The four dimensions were derived by decomposing the central research question. A mechanism that restricts AI advisory scope based on environmental safety state would need to: target advisory scope rather than participation or execution (a), use graduated rather than binary adaptation (b), condition its behaviour on the operator's environmental state rather than internal AI properties (c), and produce a formally bounded output set (d). Each requirement corresponds to one coding dimension. A paper coded Yes on all four would constitute a prior instance of the proposed mechanism; the coding determines whether any such paper exists. The label **Primary governance target** is used rather than simply "governance target" because some papers implement multiple mechanisms; the code records only the mechanism central to each paper's contribution.

### 3.3 Theme Development and Synthesis

Papers sharing a governance topology (the same combination of governance target and conditioning variable) were grouped into themes. This produced three governance paradigms (deterministic safety constraints, authority allocation frameworks, adaptive risk-based systems) and one application-domain body (fisheries and low-resource deployment), reviewed in Sections 4.2–4.5.

Within each paradigm, papers were compared against the four coding dimensions to establish the paradigm's collective posture. Section 4.6 synthesises across them, tracing where all four dimensions point to the same absence. The closest structural precedents (papers that graduated some aspect of AI behaviour across three or more levels) were examined in greater detail to establish why they still did not satisfy dimension (d).

The evidence in Section 4.7 is drawn from a separate, non-governance literature (LLM systems and cognition research) and was not subject to the same screening. It addresses a specific question: whether the governance gap could be closed within the AI component itself, rather than through external governance mechanisms.

**Figure 2.** Conceptual review process: from research question to proposed architecture. Sections 3.1–3.3 and 4.2–4.6 trace the gap through the literature; Section 4.7 shows why it cannot be closed at the AI-component level; Section 5 proposes the architecture the gap calls for.

```
Research Question
(Does any architecture restrict AI advisory scope
 as a function of environmental safety state?)
                    │
                    ▼
         Database Search (Section 3.1)
         Scopus · IEEE Xplore · Web of Science · ACM DL
                    │
                    ▼
         Screening & Inclusion (Section 3.2)
         71 papers retained
                    │
                    ▼
         Four-dimension Coding (Section 3.2)
         Primary governance target · Runtime adaptation ·
         Conditioning variable · Output restriction
                    │
                    ▼
         Theme Development (Section 3.3)
         Three paradigms + application domain
         (Sections 4.2 – 4.5)
                    │
                    ▼
         Cross-paradigm Synthesis (Section 4.6)
         All four coding dimensions converge
         on the same absence
                    │
                    ▼
         Mechanistic Evidence (Section 4.7)
         Gap cannot be closed within the AI component
                    │
                    ▼
         Proposed Architecture (Section 5)
         G(S) + A_AI(S) — graduated governance pair
```

---

## 4. LITERATURE REVIEW

### 4.1 Overview of Existing Governance Paradigms

Existing AI governance frameworks in safety-critical systems fall into three main paradigms: **deterministic safety constraints**, which provide provable runtime guarantees by intercepting or blocking unsafe AI behaviour; **authority allocation frameworks**, which distribute decision rights between human and AI; and **adaptive risk-based systems**, which vary some aspect of system behaviour across graduated operational levels. The paradigms differ in what they graduate and what they guarantee: deterministic constraints prioritise provable safety over operational flexibility, authority allocation frameworks prioritise human agency over formal rigour, and adaptive systems attempt to bridge the two. None of them, however, graduates the AI's advisory scope: the semantic content of its recommendations to a human decision-maker. That is the dimension this review examines. A fourth body of literature (fisheries AI and low-resource deployment) is reviewed separately to establish whether the patterns observed in the governance literature persist in the application domain. Sections 4.2–4.5 review each body in turn and evaluate its capacity to handle intermediate-risk conditions; Section 4.6 synthesises across them to characterise the research gap; Section 4.7 examines mechanistic evidence for why the gap cannot be closed within the AI component itself; and Section 4.8 states the study objectives that follow. The review methodology that produced this synthesis is described in Section 3 and summarised in Figure 2.

### 4.2 Deterministic Safety Constraints: Binary by Construction

The deterministic safety constraints literature is the most technically developed and offers the strongest formal guarantees in the field. Könighofer et al. formalise shields: runtime mechanisms that intercept AI actions before they reach the environment [8]. Dalrymple et al. propose Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed [9]. Bajcsy and Fisac implement a control-theoretic safety filter [10]. These approaches differ in where the guarantee is anchored (shields intercept actions at runtime, Guaranteed Safe AI verifies output before deployment, and control-theoretic filters bound behaviour dynamically), but all three share the same governance topology: the AI either operates within its safety boundary or is replaced. Mechanisms vary; the binary pattern does not. Corsi et al. refine shielding using formal DNN verification to reduce overhead by 25–71%, but the shield itself remains binary [11]. Abella et al. implement a supervision function that can switch to a non-AI fallback; it is also binary [12]. These mechanisms deliver what they promise: provable participation-level safety. Among the reviewed paradigms, deterministic safety constraints are the most formally rigorous, and the most structurally constrained. Provable participation-level safety requires sharply bounded behaviour spaces; the binary topology follows from the verification problem itself, not from any design preference. What this paradigm does not address — in any of the 71 reviewed papers, including every paper in this body — is the semantic content of AI output: the question of what the AI may recommend once participation is granted.

### 4.3 Authority Allocation: Who Decides, Not What AI May Recommend

Authority allocation frameworks bring needed precision to the human side of the loop, asking who decides rather than what the AI may recommend. Ramos et al., reviewing 91 collaborative intelligence studies, find AI-assisted decision-making as the dominant mode across safety-critical industries, but no system in their review varies advisory scope by safety state [13]. Feng, McDonald, and Zhang decompose governance into agency (tool access) and autonomy (oversight intensity) and propose five autonomy levels, but both dimensions are configured at design time and do not respond to environmental conditions at runtime [14]. The design-time character of this paradigm is confirmed at cross-domain scale by Mussi et al., whose industry-informed perspective spanning power grids, railway networks, and air traffic management identifies every ingredient of state-conditioned governance (environmental observations and forecasts, safety constraints integrated into knowledge-assisted AI, and automation levels ranging from fully manual to fully autonomous) yet assembles none of them into a runtime governance model: function allocation and automation levels are fixed at design time, and no mechanism conditions AI participation or recommendation scope on a classified environmental state [33]. Authority allocation frameworks have produced the field's most empirically grounded accounts of human-AI collaboration, offering the clearest picture of how humans and AI systems divide work in practice. The limitation is one of timing: function allocation and autonomy levels are set at design time and remain fixed there, with no mechanism to respond to environmental conditions as they change at runtime. No framework in this review conditions what the AI may recommend on a classified environmental state. The adaptive risk-based literature, reviewed next, shows that graduated runtime adaptation is technically feasible, but applies it to a different dimension.

### 4.4 Adaptive Risk-Based Systems: The Closest Precedents

Flehmig et al. propose a three-level traffic-light degradation index (green/orange/red) that classifies AI operational status and triggers different supervisory responses per level [7]. At red, control is transferred to a conventional non-AI backup system, functionally removing the AI from the decision loop; at orange, supervisory checks intensify. The AI's advisory scope, however, is identical at green and orange: the intermediate level governs human supervisory behaviour, not AI recommendation content. The authors themselves state: *"To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner"* [7]. The three-level design is novel by the authors' own account, yet it stops short of using the intermediate level to restrict AI output. Baxi formalises a K-tier permission architecture where permission sets vary by tier, but tiers are determined by the AI's own verified robustness, not by classified environmental state [15]. Vermaelen and Holvoet's Tumato 2.0 gates autonomous robot behaviour through an allowed(a,s) predicate, but as an absolute execution toggle: an action is either completely permitted or entirely blocked [16].

Three 2026 architectures extend this adaptive line and constitute the contemporary state of the art. Contemporary architectures attempting to move beyond binary governance typically deploy an intermediate mode to graduate the system's operational posture; structural analysis reveals, however, that these frameworks graduate human workflows or physical behaviours, leaving the semantic boundaries of AI generation unconstrained. The reviewed architectures cluster into three distinct paradigms.

**Oversight intensification.** Flehmig et al.'s traffic-light index [7] and Kang's Governed AI-Assisted Engineering (GAIE) framework [25] graduate the intensity of human supervisory auditing. GAIE routes agentic code generation tasks through three oversight tiers via a deterministic classification model with monotonicity, fail-safety, and totality properties established by construction. In its intermediate Human-over-the-Loop tier, the human workflow transitions to a deployment-gate check, yet the underlying coding agent continues to generate full-scope, unconstrained code artifacts at every tier [25].

**Execution deferral and re-sensing.** In embodied robotics, Ghaleb et al. implement a three-regime uncertainty-calibrated gating wrapper (Safe to proceed, Borderline, Unsafe to proceed) driven by calibrated runtime failure risk [27]. On entering the intermediate Borderline regime, the framework forces an execution slowdown and triggers a re-observation loop capturing alternative camera viewpoints, but the vision–language–action policy's output capability remains completely uncontracted; at Unsafe, the learned policy is disengaged entirely in favour of a classical planner.

**Autonomous action-class restriction.** The closest behavioural precedent is Sahoo's Agentic Military AI Governance Framework (AMAGF), which leverages a real-time Control Quality Score (CQS) to dynamically throttle an autonomous agent's tool access across five response levels [26]. At intermediate CQS levels (0.4–0.6), the agent is programmatically restricted to reversible actions only. While this represents a genuine graduated contraction of AI behaviour, it governs the execution space of an acting autonomous agent, is conditioned on measured control degradation rather than classified environmental state, and specifies its restriction levels as procedural bands over a continuous score rather than formally enumerated admissible sets with a proven containment property.

Across all three paradigms, the concept of a state-conditioned, formally bounded recommendation menu A_AI(S) for a human decision-maker facing escalating environmental risk has not been identified in the reviewed literature.

| Framework | Governance target | Conditioning variable | Runtime adaptation | Intermediate mode variable | AI status at max risk | Output restriction |
|---|---|---|---|---|---|---|
| Shields [8], GS AI [9], safety filter [10] | Participation | Safety boundary | Binary (on/off) | None | Blocked | No |
| Tumato 2.0 [16] | Execution | Constraint predicate | Binary per action | None | — | No |
| Flehmig et al. traffic-light [7] | Oversight | AI degradation index | Graduated (3 levels) | **Human** supervisory intensity | Control → non-AI backup | No |
| Kang GAIE [25] | Oversight | Task regulatory impact | Graduated (3 tiers) | **Human** audit and approval | Full scope, HITL-gated | No |
| Ghaleb et al. safety gate [27] | Execution | Epistemic uncertainty | Graduated (3 regimes) | **System** re-sensing loop | Switched to classical planner | No |
| Sahoo AMAGF [26] | Execution | Control quality score | Graduated (5 bands) | **Agent** reversible actions only | Autonomy disablement | No (action classes only) |
| Baxi K-tier [15] | Execution | AI robustness (verified) | Graduated (K tiers) | **Agent** permission set | — | No (economic actions) |
| **Proposed architecture** | **Advisory scope** | **Environmental safety state** | **Graduated (3 states)** | **AI** admissible recommendation space | Disabled (G(S) = 0, A_AI = ∅) | **Yes** (A_AI(CAUTION) = {Go, Delay}) |

**Table 1.** Coding of reviewed architectures against the four governance dimensions from Section 3.2. The proposed architecture is the only framework in the corpus that targets advisory scope and formally bounds the output set a human decision-maker may receive, conditioned on environmental safety state.

*Shamsujjoha et al.'s Swiss Cheese Model [6] describes 13 guardrail actions applied to agent artifacts (prompts, plans, tools, FMs) and pipeline stages. All actions are content-focused (block, filter, flag, modify, validate); none condition AI advisory scope on environmental safety state.*

Adaptive risk-based systems are the closest precedent the reviewed literature offers for the architecture proposed here. Graduated operational posture has been shown to be technically feasible and useful. The gap is in where the graduation is applied: intermediate governance levels across every reviewed system target human supervisory workflows, physical execution deferral, or agent action classes. The semantic content of the AI's recommendation output is left uncontracted at every tier.

### 4.5 Fisheries and Low-Resource Deployment: The Gap Persists in the Application Domain

The application domain carries a measurable environmental risk profile. Dominguez-Péry et al., analysing 504 IMO maritime accident reports from 2011 to 2021, found that wind, weather, and visibility collectively form the largest single risk cluster (26.7% of text segments), and that small vessels record the highest mean fatality rank across size categories (p = 0.01) [2]. Atacan and Düzbastılar, studying 30 small-scale fishing captains in a bridge navigation simulator, found that combined night navigation and heavy weather produces the highest accident consequence scores across all tested conditions (mean 37.03) [3].

Against this risk profile, the domain's AI literature shows the same governance pattern observed above. Haque and Al Jufaili confirm across four fisheries AI application domains that no system implements formal advisory scope restriction conditioned on environmental state [17]. Rahim et al. document that the only external advisory available to coastal fishers is a binary government warning to stop fishing [18]. Katende characterises low-resource AI deployment requirements as offline-first, computationally lightweight, and observable from locally available data, and identifies safety governance as a systematic gap: it has not been designed from the deployment floor [19]. Longobardi et al. demonstrate that analytics are achievable in data-deficient fisheries contexts, but without a governance architecture [20]; Bhuvaneswari et al. show lightweight AI for safety-critical decisions is feasible in resource-constrained settings, also without one [21].

The fisheries and low-resource deployment literature makes a clear contribution: it establishes that AI deployment in these environments is achievable and documents the risk profile that makes a governance question worth asking. But it does not answer that question. No paper reviewed in this body was designed with formal runtime governance in mind, and the coding in Section 3.2 finds no paper that scores Yes on any of the four governance dimensions.

### 4.6 Synthesis: Cross-Paradigm Comparison and the Research Gap

When compared across paradigms, a consistent pattern emerges: deterministic constraints prioritise provable safety over flexibility and remain binary by construction; authority allocation frameworks graduate human decision rights but leave AI output untouched; adaptive risk-based systems graduate operational posture but divert their intermediate levels away from advisory content; and the fisheries/low-resource literature demonstrates deployment feasibility without any formal governance architecture at all. Prior research thus provides robust mechanisms for **whether** the AI operates (participation gating) and **which actions** an autonomous agent may execute (action-class restriction), but not for **what the AI is permitted to recommend** to a human decision-maker under deteriorating environmental conditions.

Four independent literature streams confirm this same absence. First, Indykov et al. [5] (16 architectural tactics across 206 papers), Shamsujjoha et al. [6] (13 guardrail actions across 32 agent studies), and Perez-Cerrolaza et al. [24] (294 references across safety-critical domains) record no mechanism that conditions the internal semantic boundaries of an AI's advisory scope on an environmental safety state. Indykov et al.'s trade-off matrix records AT11 (rule-based models) → Safety = 0: despite Safety being one of the two most frequently cited quality attributes, no architectural tactic has demonstrated a formally positive impact on it [5]. Shamsujjoha et al.'s Swiss Cheese Model identifies 13 guardrail actions, yet their "context-dependent" rules refer strictly to static deployment parameters (e.g., organisational policy, user location, regulatory jurisdiction), not dynamic environmental risk [6]. This absence extends beyond architectures to governance systems themselves: Attard-Frost and Lyons' empirical mapping of a national AI governance system, spanning 610 topics from expert interviews, contains no runtime state-conditioned advisory scope concepts; guardrails appear only in binary framing [22]. Even where governance is planned, it is not executed: Reuel et al.'s 1,000-organization survey documents a systematic planning–execution gap in which formal AI governance structures exist but operational implementation lags [31], reinforcing the case for governance properties enforced by construction, as architectural invariants, rather than through organizational process.

Second, within the adaptive risk-based systems literature, intermediate governance tiers are universally diverted away from output scope: Flehmig et al. [7] and Kang [25] use intermediate tiers to escalate human audit workloads, whereas Ghaleb et al. [27] leverage them to trigger temporal execution deferrals and physical re-sensing. Third, while behavioural architectures such as Sahoo's [26] implement intermediate restrictions, they throttle the execution capabilities of acting autonomous agents rather than the recommendation menu of a decision-support tool. Fourth, the fisheries and low-resource deployment literature [17], [18], [19] lacks any formal runtime governance architecture entirely.

The contemporary literature also reveals a consistent misalignment in the variables used to condition runtime governance gates. Baxi conditions permissions on verified algorithmic robustness [15]; Flehmig et al. monitor AI degradation [7]; Kang classifies task regulatory impact [25]; Sahoo measures human-agent control quality [26]; and Ghaleb et al. compute calibrated epistemic model uncertainty [27]. All five gate behaviour on properties internal to the AI system or its software task. The same centring appears in governance theory itself: Engin and Hand's dimensional governance (the most adaptive strand of current governance thinking, arguing that static risk tiers and autonomy levels are insufficient and that governance categories should instead be explicit thresholds over continuously monitored dimensions) nonetheless defines its dimensions (decision authority, process autonomy, accountability) as properties of the human-AI relationship, not of the operator's physical environment [32]. The proposed architecture conditions its graduated constraints on an independently classified environmental safety state (S = f(E)), ensuring that the AI's advisory boundaries respond to the physical peril facing the human operator.

Across the 71 reviewed papers, prior work addresses adjacent governance dimensions (participation, oversight intensity, execution deferral, and action classes), while an admissible recommendation space that contracts as a function of environmental safety state has no equivalent in any of the surveyed paradigms. The operational consequence is direct: during marginal conditions, the human operator receives full-scope tactical recommendations at the moment when the underlying data can no longer support them, with no architectural signal that anything has changed [4].

### 4.7 The Mechanistic Basis for External Governance

Can the AI component itself be expected to narrow its advisory scope as conditions deteriorate, making external governance unnecessary? Evidence from the LLM systems and cognition literatures (external to the governance corpus reviewed above) indicates it cannot be relied upon to do so, at any of the three loci where such self-restraint would have to arise.

#### Fixed inference pipeline

LLM inference proceeds through two structurally fixed phases: a compute-bound prefill phase that processes the input prompt, followed by a memory-bandwidth-bound decode phase that generates output tokens one at a time, autoregressively [28]. The pipeline is mechanically identical for every request; serving-level decisions (batching, scheduling, kernel selection) are driven by token counts and hardware utilisation, never by the semantic content or operational risk of the input [28]. No architectural hook exists in the inference process at which advisory behaviour could be conditioned on environmental safety state.

#### Reasoning dynamics are not risk-adaptive

Probing studies of reasoning LLMs show that how broadly a model explores alternative reasoning paths is a mechanical property of its decoding procedure, not a content-conditioned adaptation. Wu et al. find that even when inputs carry full probability distributions over concepts, models collapse onto the single highest-probability component at each step, a self-reinforcing greedy pattern, and that exploration is restored only by externally injected, undirected randomness [29]. Undirected randomness is itself uncontrolled with respect to safety state: it can scatter reasoning, but it cannot produce systematically more conservative advice under deteriorating conditions.

#### Self-assessed uncertainty is unreliable and non-learning

In five preregistered studies comparing four LLMs with human participants, Cash et al. find that LLM confidence judgments are unpredictably calibrated across domains and models, biased toward overconfidence, and (for the models tested most extensively) insensitive to the models' own past performance: unlike humans, ChatGPT and Gemini failed to improve their calibration after completing a task, a deficit the authors attribute to LLMs' lack of access to mnemonic cues, the internal experiential signals that ground human metacognitive updating [30]. A safety-critical system therefore cannot delegate risk sensitivity to the AI component's self-reported uncertainty, and repeated operation does not make that self-assessment more trustworthy.

#### Internal versus external governance

The analysis above establishes a distinction between two classes of governance mechanism. **Internal governance** would rely on the AI component itself to modify its advisory behaviour through dynamic adaptation of the inference pipeline to environmental conditions, content-conditioned exploration of alternative reasoning paths, or reliable, self-calibrating expression of uncertainty. The evidence reviewed here indicates that none of these three capabilities can be relied upon in current generative AI systems [28], [29], [30]: the pipeline is fixed, reasoning exploration is a mechanical property of decoding rather than a risk-adaptive process, and confidence judgments are unreliably calibrated and insensitive to past performance. **External governance**, by contrast, imposes constraints from outside the AI component: an independent architectural layer that classifies environmental risk deterministically, defines an admissible recommendation space A_AI(S) as a function of that classification, and enforces the restriction before inference begins. This approach requires nothing of the AI's self-knowledge or adaptivity; it simply bounds what the AI is permitted to generate.

This mechanistic evidence converts the gap documented in Sections 4.2–4.6 from a contingent design omission (something that might be remedied by better prompting or fine-tuning) into a structural requirement for external enforcement, and it motivates two design decisions in the architecture proposed in Section 5: the safety state S is computed by a deterministic external classifier rather than derived from AI self-assessment, and the admissible recommendation space A_AI(S) is enforced before inference begins rather than expected to emerge within it.

### 4.8 Objectives of This Study

The literature reviewed in Sections 4.1–4.7 establishes a research gap: the reviewed AI governance and decision-support architectures provide mechanisms for AI participation gating and autonomous action restriction, but do not restrict AI advisory scope according to classified environmental safety state. The mechanistic evidence presented in Section 4.7 further indicates that this gap cannot be resolved within the AI component itself, motivating the need for an externally enforced governance mechanism. To address this gap, this study has three objectives:

1. **To determine whether existing AI governance and decision-support architectures implement mechanisms that restrict AI advisory scope according to classified environmental safety state.**

2. **To characterise the advisory scope gap through a structured comparison across deterministic safety constraints, authority allocation frameworks, adaptive risk-based systems, and low-resource application domains.**

3. **To derive a graduated safety-state-gated governance architecture that addresses the identified gap by separating AI participation from advisory scope through an externally enforced governance mechanism.**

The structured literature review addresses the first two objectives, while the architecture proposed in Section 5 addresses the third.

---

## 5. PROPOSED ARCHITECTURE

Section 4.7 establishes that internal self-restraint (relying on the AI component to narrow its own advisory scope) cannot be relied upon; the gap documented in Sections 4.2–4.6 must therefore be addressed through external governance. This section proposes a graduated safety-state-gated architecture that implements such an external approach: both AI participation and advisory scope are conditioned on a classified environmental safety state, by an architectural layer outside the AI component (Figure 3). The design also answers a call from governance theory: where Engin and Hand argue that governance categories should be built as explicit thresholds over continuously monitored dimensions rather than as static classifications [32], the proposed architecture realises this pattern as an enforced runtime mechanism: continuous environmental observation E, deterministic thresholding S = f(E), and three actionable categories each carrying formally differentiated constraints. This supplies what the dimensional-governance proposal itself lacks: by-construction enforcement.

**Figure 3.** The graduated safety-state-gated architecture. Before any inference begins, a deterministic external classifier computes the environmental safety state S = f(E) outside the AI component. Both gates, G(S) and A_AI(S), are conditioned on S and together bound what the AI may recommend for the current observation.

```
Environmental observation vector E = {w, r, m, o, v, t}
                    │
                    ▼
         ┌─────────────────────┐
         │  Safety Classifier  │  S = f(E)
         │  (deterministic,    │
         │   external to AI)   │
         └─────────┬───────────┘
                   │
         ┌─────────▼───────────┐
         │  S ∈ {SAFE,         │
         │       CAUTION,      │
         │       UNSAFE}       │
         └──┬──────┬───────────┘
            │      │
     ┌──────▼──┐ ┌─▼──────────────┐
     │ G(S) = 0│ │   G(S) = 1     │
     │ UNSAFE  │ │ SAFE / CAUTION │
     │ AI off  │ └────────┬───────┘
     └─────────┘          │
                 ┌────────▼───────────────────────┐
                 │  Advisory Gate A_AI(S)          │
                 │  SAFE:    {Go, Delay,           │
                 │            DepartureTime,       │
                 │            Duration}            │
                 │  CAUTION: {Go, Delay}           │
                 └────────┬───────────────────────┘
                          │
                 ┌────────▼───────────┐
                 │  Rule-based engine │
                 │  (RS(S) supplied   │
                 │   before inference)│
                 └────────┬───────────┘
                          │
                 ┌────────▼───────────┐
                 │  AI(E) ⊆ A_AI(S)   │
                 │  Recommendations   │
                 │  to human operator │
                 └────────────────────┘
```

### 5.1 Formal Structure

Let E denote the environmental observation vector and S = f(E) a classifier that maps observations to a safety state S ∈ {SAFE, CAUTION, UNSAFE}. The governance pair (G(S), A_AI(S)) operates as follows:

| State | G(S) | A_AI(S) | AI scope |
|---|---|---|---|
| SAFE | 1 (enabled) | {Go, Delay, DepartureTime, Duration} | Full |
| CAUTION | 1 (enabled) | {Go, Delay} | Restricted |
| UNSAFE | 0 (disabled) | ∅ | None |

The **Safety Dominance Property** holds: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. For all E, the AI can only generate recommendations within the admissible space A_AI(S) defined by the current safety state. The property holds by construction: the governance layer supplies a state-specific rule set to the reasoning engine before inference begins, so no rule in the CAUTION configuration can produce recommendations outside {Go, Delay}.

### 5.2 The CAUTION Mode

The CAUTION mode is the novel contribution that none of the architectures identified in this review implements. At CAUTION, the AI remains engaged and provides guidance that acknowledges marginal conditions, but within a formally restricted scope. Precise tactical outputs (departure time, trip duration) are withheld because the environmental data can no longer reliably support them. The human operator receives a participation signal from the AI alongside an implicit signal that conditions have restricted its scope, enabling calibrated reliance rather than over-reliance.

Existing three-level designs (Flehmig et al.) use the intermediate level to govern human supervisory behaviour; the proposed architecture uses it to govern AI advisory scope.

Empirical trade-offs documented in contemporary runtime assurance make the operational case for an intermediate CAUTION mode directly. Ghaleb et al. show that an aggressive, uncalibrated binary-style threshold gate can enforce strong raw safety metrics, but does so at the cost of nearly doubling the intervention burden on the system (21.6 vs. 11.5 interventions per shifted episode) [27]. In low-resource settings such as coastal fisheries, an over-aggressive binary gate creates an unworkable trade-off: it either leaves the fisher with a decision vacuum during marginal weather, or induces governance fatigue by completely disabling the tool when helpful, bounded advice could still be safely rendered.

### 5.3 Domain Instantiation

The architecture is being pursued as a formally specified prototype for AI departure decision support in small-scale coastal fisheries in Malaysia (Kota Kinabalu, Sabah). E = {w, r, m, o, v, t} where w is wind speed, r is rainfall intensity, m is marine warning level, o is ocean state, v is vessel category, and t is time of day. The rule-based reasoning engine enforces the Safety Dominance Property by construction, satisfying the offline-first and computationally lightweight requirements of the low-resource deployment context. To minimise mode-chattering at the classification boundaries of S = f(E) during marginal weather transitions, a dual-threshold hysteresis smoothing layer over the discrete state transitions is a deployment-floor design consideration, drawing on the empirically verified runtime-gating stability of Ghaleb et al. [27].

---

## 6. CONCLUSION

This paper establishes, from four independent bodies of literature, that AI governance in safety-critical decision support is binary by design across the reviewed literature: participation gating exists, advisory scope gating does not. Shamsujjoha et al.'s Swiss Cheese Model, the most comprehensive guardrails taxonomy in the field (synthesising 32 studies and identifying 13 guardrail actions and 14 quality attributes), contains no concept of restricting advisory scope as a function of environmental risk. The closest structural precedents identified in this review approach intermediate-risk conditions from alternate dimensions: Flehmig et al.'s traffic-light index changes human supervisory behaviour at its intermediate level but leaves AI output unchanged, while Sahoo's five-level protocol genuinely contracts an autonomous agent's permitted action space but remains blind to external environmental safety state and human-facing advisory contexts. Prior research thus governs whether the AI operates and which actions an agent may execute; an admissible recommendation space A_AI(S) that contracts as classified operational risk increases has not appeared in any of the reviewed architectures. The gap is characterised, confirmed from multiple independent sources, and open; the mechanistic evidence reviewed in Section 4.7 indicates it cannot be closed within the AI component itself.

The graduated safety-state-gated architecture proposed here addresses this gap through a two-level governance pair (G(S), A_AI(S)) that produces an intermediate CAUTION mode. To the authors' knowledge, this is a novel architectural paradigm in safety-critical decision support, formally enforcing a state-conditioned containment where AI advisory scope contracts as environmental safety state worsens: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. The architecture draws on Guaranteed Safe AI principles [9] and the dependability perspective of surrounding opaque AI components with deterministic guards [23], and addresses a gap with direct operational consequences: in low-resource safety-critical domains, operators in intermediate-risk conditions currently receive either full-scope AI recommendations or none at all.

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

[28] A. K. Kamath, R. Prabhu, J. Mohan, S. Peter, R. Ramjee, and A. Panwar, "POD-Attention: Unlocking full prefill-decode overlap for faster LLM inference," in *Proc. 30th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems, Volume 2 (ASPLOS '25)*, Rotterdam, Netherlands, 2025, pp. 897–912. doi: 10.1145/3676641.3715996

[29] C. Wu, J. Lu, Z. Ren, G. Hu, Z. Wu, D. Dai, and H. Wu, "LLMs are single-threaded reasoners: Demystifying the working mechanism of soft thinking," *arXiv preprint arXiv:2508.03440*, 2025.

[30] T. N. Cash, D. M. Oppenheimer, S. Christie, and M. Devgan, "Quantifying uncert-AI-nty: Testing the accuracy of LLMs' confidence judgments," *Memory & Cognition*, vol. 54, pp. 375–400, 2025. doi: 10.3758/s13421-025-01755-4

[31] A. Reuel, P. Connolly, K. J. Meimandi, S. Tewari, J. Wiatrak, D. Venkatesh, and M. Kochenderfer, "Responsible AI in the global context: Maturity model and survey," in *Proc. 2025 ACM Conf. Fairness, Accountability, and Transparency (FAccT '25)*, Athens, Greece, 2025, pp. 2505–2541. doi: 10.1145/3715275.3732165

[32] Z. Engin and D. Hand, "Towards adaptive categories: Dimensional governance for agentic AI," *arXiv preprint arXiv:2505.11579*, 2025.

[33] M. Mussi et al., "Human-AI interaction in safety-critical network infrastructures," *iScience*, vol. 28, p. 113400, 2025. doi: 10.1016/j.isci.2025.113400
