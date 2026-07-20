# Literature Review Extraction (Reduced)
## Paper: Pro2Guard: Proactive Runtime Enforcement of LLM Agent Safety via Probabilistic Model Checking

---

## 1. Paper Identity

- **Full title:** Pro2Guard: Proactive Runtime Enforcement of LLM Agent Safety via Probabilistic Model Checking
- **Authors:** Haoyu Wang, Christopher M. Poskitt, Jun Sun, Jiali Wei
- **Affiliations:** Singapore Management University; Xi'an Jiaotong University
- **Year:** 2025
- **Venue:** arXiv:2508.00500 (1 Aug 2025) — ACM template, venue placeholder unfilled; **preprint at time of extraction** (verify publication status before citing in a manuscript)
- **Type:** Runtime enforcement framework + empirical evaluation (embodied household agents; autonomous vehicles); open-source implementation
- **Relation to corpus:** Same group as AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) (Sun); explicitly positions itself as the *proactive* successor to reactive rule-based enforcement (AgentSpec, GuardAgent, ShieldAgent)
- **Extraction category:** Reduced extraction — governance-adjacent (runtime enforcement family)

---

## 2. Core Contribution

- **Problem:** Existing rule-based enforcement (AgentSpec, GuardAgent, ShieldAgent) is *reactive* — rules trigger only when a violation is imminent or has occurred; they lack foresight and struggle with long-horizon dependencies and distribution shift.
- **Proposal:** Proactive enforcement via probabilistic reachability. Pro2Guard abstracts agent behaviour into symbolic states (predicate-based abstraction), learns a Discrete-Time Markov Chain from execution traces, and at runtime estimates the probability of reaching unsafe states, **triggering intervention before violation when predicted risk exceeds a user-defined threshold**. PAC bounds and semantic validity checks give statistical reliability.
- **Intervention repertoire (configurable modes):** halt execution ("stop"), alert/prompt user verification, or invoke LLM-based self-assessment ("reflect").
- **Results:** Embodied agents — early intervention enforces safety on up to 93.6% of unsafe tasks at low thresholds, but the aggressive **stop** mode collapses task completion to **17.54%**, while threshold tuning plus the **reflect** mode maintains up to **80.4%** completion. Autonomous driving — 100% prediction of traffic-law violations and collisions, up to 38.66 s ahead.

**Key quote (Abstract):** *"[Pro2Guard] anticipates future risks by estimating the probability of reaching unsafe states, triggering interventions before violations occur when the predicted risk exceeds a user-defined threshold."*

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Safety-critical AI decision-making | **Partial** | Safety-critical domains (embodied agents, AVs), but acting agents — not human decision support |
| AI governance / control mechanisms | **Yes** | Runtime enforcement with predictive gating — the current frontier of the shields/AgentSpec line |
| Pre-generation advisory scope restriction | No | Governs execution of actions; no concept of a recommendation menu |
| Environmental state classification | No | Risk signal = probability of the *agent's own trajectory* reaching unsafe states (learned DTMC over agent behaviour), not classified external environmental state |
| Decision architecture formalisation | **Partial** | Formal DTMC + reachability + PAC machinery — for behaviour prediction, not governance structure |
| Human role in decision-making | No | User verification is one intervention option; no decision-support framing |
| Low-resource / fisheries | No | — |

**Extraction decision:** Reduced extraction, governance-adjacent. The strongest recent member of the enforcement family; belongs beside AgentSpec, GAVEL, AgentGuard [[notes]](../notes/AgentGuard-%20Runtime%20Verification%20of%20AI%20Agents.md).

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- **The frontier moved from reactive to proactive — and still governs execution, not advisory scope.** Even with predictive foresight (probabilistic reachability, intervention before violation), the object of governance is what the agent *does*; nothing conditions or contracts what an AI may *recommend to a human decision-maker*. One more, and the strongest, member of the pattern.
- **Empirical support for the CAUTION-mode operational case.** Pro2Guard's own results document the binary-intervention trade-off at scale: aggressive stop-mode intervention enforces safety but collapses task completion to 17.54%, while a softer intervention mode recovers 80.4%. This directly parallels Ghaleb et al.'s intervention-burden finding and strengthens the argument that an all-or-nothing gate is operationally unworkable — bounded intermediate operation preserves utility.
- **Misalignment datapoint:** its gating variable is the predicted behaviour of the AI system itself (learned DTMC of the agent's trajectories), extending the §4.6 finding that contemporary frameworks condition governance on AI-internal properties, not independently classified environmental state.
- **Pre-emptive nuance:** the configurable stop/alert/reflect modes and tunable threshold superficially resemble graduation. The distinction: modes are design-time-selected intervention *strategies* over a single threshold, not formally enumerated, state-conditioned admissible sets with a containment property; and the graduated element governs *intervention style*, not the AI's advisory scope. Same measurement-vs-response logic as for AgentGuard.

**What this paper CANNOT be cited for (overreach guard):**

- **Quote verification failure:** the claim that the authors state existing frameworks "rely on formal abstractions to anticipate violations" but none use this for advisory content **does not appear in the paper** — the words "advisory" and "recommend" occur nowhere in it. The advisory-scope absence is real but established by *our* structural analysis of the framework, not by any author statement. Do not attribute this quote.
- arXiv preprint with unfilled venue placeholder — verify publication status before it enters a submitted reference list; until then, weight below the published enforcement papers (AgentSpec, Könighofer).
- It governs executing agents (household robots, AVs); do not describe it as a decision-support governance framework, and do not place it in the authority-allocation paradigm.

---

## 5. Positioning for This Research

**Positioning paragraph:** Wang et al. (2025) advance the runtime enforcement line from reactive to proactive: Pro2Guard learns a Discrete-Time Markov Chain of agent behaviour from execution traces and intervenes before violations occur, when the estimated probability of reaching an unsafe state exceeds a user-defined threshold, with configurable intervention modes ranging from halting execution to LLM self-reflection. Two aspects of this frontier design reinforce the pattern documented in this review. First, the object of governance remains execution behaviour — even with predictive foresight, nothing conditions what an AI may recommend to a human decision-maker, and the risk signal derives from the agent's own predicted trajectory rather than an independently classified environmental state. Second, its empirical results quantify the cost of binary intervention: aggressive stopping enforces safety on 93.6% of unsafe tasks but collapses task completion to 17.54%, while softer intervention recovers 80.4% — direct evidence, from the enforcement literature's own frontier, that all-or-nothing governance is operationally unworkable and that formally bounded intermediate operation is the missing alternative.

---

## 6. Overall Relevance Score

### ⭐⭐⭐ Medium (governance-adjacent, reduced)

**Justification:** The strongest recent enforcement-family paper: full formal machinery, two safety-critical evaluation domains, and — unusually valuable — empirical numbers (17.54% vs 80.4% completion) that independently support the CAUTION-mode operational argument from within the enforcement literature itself. Cite in the conference paper either in §4.2/§4.4 as the proactive frontier of the enforcement line, or in §5.2 beside Ghaleb et al. for the intervention-burden trade-off. Preprint status and the fabricated-quote risk (see §4) are the two handling cautions.
