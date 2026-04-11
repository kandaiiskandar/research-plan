---
layout: document
---

# The Big Questions: Core Viva Defence Preparation

**Document type**: Viva preparation — concise, high-impact answers  
**For**: Viva voce examination — opening and closing exchanges  
**Questions addressed**: Main contribution, problem solved, necessity, novelty, research gap, domain choice, generalisability, limitations, future work, PhD-level justification

**Cross-references**: Each answer below references the detailed justification document where the full argument is developed. This document provides the *examiner-ready one-paragraph answer*; the referenced documents provide the *evidence base* if probed further.

---

## 1. What Is the Main Contribution of Your PhD in One Sentence?

A formal two-level governance architecture — the pair (G(S), A_AI(S)) conditioned on classified environmental safety state S = f(E) — that enables AI decision support to operate in a graduated manner: fully enabled under safe conditions, restricted to robust recommendation types under uncertain conditions, and disabled under dangerous conditions, with the Safety Dominance Property AI(E) ⊆ A_AI(S) guaranteed for all environmental states.

**If pressed for a shorter version**: A governance architecture that controls not only *whether* AI participates but *what* AI is permitted to recommend, conditioned on classified environmental safety state.

**If pressed for the simplest version**: The first architecture where AI gets both a permission gate and a scope restriction, and both are governed by the same environmental safety classification.

**Detailed justification**: `justification-contribution-characterisation.md` §1, `justification-novelty-gap.md` §1.

---

## 2. What Problem Does Your Architecture Solve That Existing Architectures Do Not?

Every existing safety-critical AI governance mechanism implements governance at only one level. Safety shields (Könighofer et al., 2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md), safety filters (Bajcsy & Fisac, 2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md), the Guaranteed Safe AI framework (Dalrymple et al., 2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md), and runtime guardrails (Wang et al., 2026 — AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md); Chen, Kang & Li, 2025 — SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md)) all implement Level 1 governance: whether AI participates at all. Some systems restrict AI output (guardrails, output filters), but this restriction is either static (same constraints regardless of conditions) or per-action (each action evaluated against fixed rules), never conditioned on a classified environmental safety state.

The result is a forced binary choice: AI is either fully enabled (with all recommendation types available) or fully blocked. This is ecologically invalid in domains where conditions are neither uniformly safe nor uniformly dangerous — fishers already operate in a documented tripartite pattern of go, cautious-go, and don't-go (Gao, 2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), but no AI architecture supports the intermediate mode.

The proposed architecture solves this by adding Level 2 governance — state-conditioned restriction of AI advisory scope — unified with Level 1 under the same environmental safety classification. In CAUTION, the AI participates (G(S) = 1, same as SAFE at Level 1) but can only recommend robust threshold-crossing assessments (go/no-go, delay), not precise timing or duration estimates that require environmental certainty the CAUTION state cannot guarantee.

**Detailed justification**: `justification-architecture-differentiation.md`, `justification-novelty-gap.md` §2–4.

---

## 3. Why Is Your Architecture Necessary?

Three converging arguments establish necessity:

**The governance gap argument.** Four independent systematic reviews confirm that no existing architecture implements unified two-level governance conditioned on environmental state: Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) — 91 papers on collaborative intelligence for safety-critical industries, all implement binary governance; Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) — 46 papers on formal methods for safety-critical ML, all operate with binary safety boundaries; Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) — 11 frontier AI safety frameworks, all implement binary participation control; Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) — cross-domain survey of safety-critical AI across automotive, avionics, railway, and medical, confirming binary governance dominance. The gap is not a single literature search result — it is independently confirmed across four bodies of literature totalling hundreds of papers.

**The domain necessity argument.** Fishers in the target population (Terengganu, Malaysia) demonstrate a documented tripartite decision pattern (Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md); Yamin et al., 2025 [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md)), but existing AI decision support provides only binary classification (safe/unsafe). Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that fishers routinely ignore binary governmental warnings because the warnings fail to accommodate the adaptive fishing (near-shore, shortened trips) that fishers already practise under marginal conditions. The architecture is necessary because the binary paradigm structurally cannot support the intermediate operational mode that the target population already uses.

**The formal necessity argument.** Level 1 governance alone (participation gate) cannot restrict *what* AI recommends when it is permitted to operate. Level 2 governance alone (output scope restriction) cannot disable AI entirely when conditions are dangerous. Only the unified pair (G(S), A_AI(S)) provides both capabilities, and only state conditioning ensures they respond to the same environmental classification — independent implementation produces inconsistent governance where the CAUTION mode structurally cannot activate (see `justification-unified-governance.md` §4–5).

**Detailed justification**: `justification-novelty-gap.md`, `justification-unified-governance.md`, `justification-three-states.md` §2.

---

## 4. What Is Novel in Your Work?

The novelty is at the **integration level** — the combination produces formal properties that none of the components possess individually:

1. **Two-level governance pair (G(S), A_AI(S))** — no existing architecture unifies participation governance with advisory scope governance under the same state variable. This is confirmed across 91 + 46 + 11 + cross-domain survey papers (§3 above).

2. **Environmental-state-conditioned scope restriction** — existing scope restrictions are static (design-time), per-action (rule-by-rule), or AI-performance-triggered. None is conditioned on a classified environmental safety state S = f(E). Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) — the closest structural precedent — triggers by AI performance degradation and governs monitoring intensity, not advisory scope.

3. **The containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅** — a formal invariant guaranteeing graduated restriction. No existing architecture defines or enforces this nesting relationship across safety states.

4. **The Safety Dominance Property AI(E) ⊆ A_AI(S) for all E** — a formal guarantee that AI output is always within the governance-permitted space. Existing safety properties (shield correctness, barrier certificates) apply to binary governance only.

5. **Pre-hoc output space definition** — the governance layer defines the admissible recommendation space *before* AI reasoning occurs, not as a post-hoc filter on AI output. This distinguishes the architecture from guardrails, which intercept and modify AI output after generation.

The contribution is not a new algorithm, not a new AI model, and not a new safety shield. It is a new *governance architecture* — a formally specified layer that sits between environmental sensing and AI reasoning, constraining the AI output space in a graduated, state-conditioned manner that no prior architecture implements.

**Detailed justification**: `justification-contribution-characterisation.md`, `justification-novelty-gap.md` §2–5.

---

## 5. What Is the Research Gap You Are Addressing?

The research gap is stated across five problem statements (PS1–PS5), but the core gap is captured in PS1 and PS2:

**PS1**: No architecture formally defines an intermediate AI participation mode where AI operates under a restricted recommendation space calibrated to classified environmental risk level. All existing safety governance is binary — AI fully on or fully off.

**PS2**: Where graduated AI governance has been attempted (Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md), it is triggered by AI model performance degradation, not by the safety state of the operational environment. No existing architecture classifies environmental conditions into discrete safety states that determine both AI participation mode and the set of permissible AI recommendations.

The gap is at the intersection of two well-established research areas (safety governance and AI advisory systems), not in either area individually. Each area has substantial prior work, but no work occupies the intersection where environmental state classification simultaneously governs both participation and advisory scope.

**Detailed justification**: `justification-novelty-gap.md`, `research-alignment-table.md`.

---

## 6. Why Fisheries? Why Not Aviation or Medical?

### 6.1 Why Fisheries Is the Right Domain

Three reasons, in order of importance:

**First, fisheries exhibits the tripartite operational pattern that motivates the architecture.** Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md), and Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) independently document that small-scale fishers operate in three modes: go freely, go with caution, and don't go. This is not a researcher's imposition — it is the practitioners' own decision structure. Aviation and medical domains have binary regulatory frameworks (cleared/not cleared, approved/contraindicated) that map naturally to binary governance. Fisheries has an empirically documented intermediate mode with no formal governance support, making it the ideal domain to demonstrate and evaluate graduated governance.

**Second, fisheries is a safety-critical, low-resource domain where AI governance is absent.** Aviation has DO-178C, DO-254, and decades of formal safety governance. Medical AI has FDA clearance processes, clinical decision support regulations, and established safety frameworks (e.g., SAFEXPLAIN covers automotive, space, and railway). Fisheries — particularly small-scale fisheries in developing countries — has no formal AI safety governance at all. The absence of existing governance means the architecture fills a real deployment gap, not a theoretical one.

**Third, the low-resource constraints force architecturally desirable properties.** The governance layer must be O(1), fully offline, and based on observable environmental parameters — constraints imposed by the deployment context (no reliable connectivity, limited compute, no instrumentation on small vessels). These constraints produce an architecture that is inherently deterministic, verifiable, and interpretable — properties that are formally desirable but that well-resourced domains might achieve through more complex (and less generalisable) mechanisms. The constraints are a design advantage, not a limitation (see `justification-low-resource-environments.md` §8).

### 6.2 Why Not Aviation or Medical?

Aviation and medicine are mature safety-critical domains with established governance frameworks. Demonstrating the architecture in these domains would face two problems: (a) the existing governance infrastructure would obscure whether the architecture itself contributes value, and (b) the regulatory barriers to deploying a new governance mechanism in aviation or medicine are prohibitive for a PhD timescale. Fisheries provides a domain where the gap is both real and accessible.

Additionally, the architecture *is* domain-general in design — the formal components (E, S = f(E), G(S), A_AI(S)) contain no fisheries-specific elements at the architectural level. Domain specificity enters only at the parameterisation level: what E measures, where thresholds are set, and what R contains. The fisheries instantiation demonstrates and evaluates the architecture; it does not define it.

**Detailed justification**: `justification-low-resource-environments.md`, `justification-caution-mode-operation.md` §7, `justification-unified-governance.md` §9.

---

## 7. Can Your Architecture Be Generalised to Other Domains?

Yes. The architecture is domain-general at the formal level and domain-specific only at the parameterisation level.

**Domain-general components** (unchanged across domains):
- The governance pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E)
- The Safety Dominance Property: AI(E) ⊆ A_AI(S) for all E
- The containment property: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- The three-state classification: S ∈ {SAFE, CAUTION, UNSAFE}
- The separation of governance (deterministic) from AI reasoning (probabilistic)
- The pre-hoc output space definition

**Domain-specific parameters** (change per domain):
- The environmental state vector E — different domains have different observable parameters
- The classification thresholds in f(E) — different domains have different safety boundaries
- The recommendation type space R — different domains have different recommendation categories
- The partition of R across A_AI(S) — which recommendation types are robust under uncertainty varies

**Concrete examples:**

| Domain | E | R | A_AI(CAUTION) |
|---|---|---|---|
| **Coastal fisheries** | Wind, rain, marine warnings, ocean state, vessel, time | Go, Delay, DepartureTime, Duration | {Go, Delay} |
| **Mountain rescue** | Temperature, visibility, wind, avalanche risk, team fitness, daylight | Deploy, Delay, Route, Duration | {Deploy, Delay} |
| **Agricultural advisory** | Soil moisture, rainfall forecast, pest risk, crop stage, equipment | Plant, Delay, Timing, Quantity | {Plant, Delay} |

In each case, the CAUTION mode retains threshold-crossing assessments (should you act?) while suppressing precision-dependent recommendations (exactly when and how much?) — the same architectural principle applied to different parameters.

**Detailed justification**: `justification-caution-mode-operation.md` §7, `justification-unified-governance.md` §9, `justification-low-resource-environments.md` §7.

---

## 8. What Are the Limitations of Your Architecture?

### 8.1 Architectural Limitations

| Limitation | Explanation | Why it is acceptable |
|---|---|---|
| **Three states may be insufficient for some domains** | Some domains may require finer granularity (4+ states). The architecture's formal properties hold for any finite number of states with a total ordering, but only three are demonstrated. | Three is the minimum needed to break the binary false dilemma. Additional states can be added without architectural change — they extend the containment chain. Empirical evidence (Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md)) confirms three is ecologically valid for the target domain. |
| **Threshold-based classification may not capture all risk patterns** | S = f(E) uses threshold comparisons with worst-case aggregation. It cannot represent non-monotonic risk relationships (where risk increases then decreases with a parameter). | Worst-case aggregation is a safety-conservative design: it over-classifies (assigns higher severity), never under-classifies. Over-classification is safe — it restricts AI unnecessarily, not dangerously. |
| **The partition of R into recommendation types is domain-expert-dependent** | Which recommendation types belong in A_AI(CAUTION) vs are suppressed requires domain expertise. The architecture does not provide a method for determining this partition. | The architecture separates governance structure (domain-general) from governance parameterisation (domain-specific). Providing the partition method would conflate the two. |
| **No learning or adaptation** | The governance layer is static once parameterised — it does not learn from experience or adapt thresholds based on outcomes. | This is a design choice: governance must be deterministic and verifiable. Adaptive governance would require verifying that the adapted governance still satisfies the Safety Dominance Property, which is an open research problem. |
| **Single-agent architecture** | The architecture governs a single AI advisory system. It does not address multi-agent scenarios where multiple AI systems provide competing recommendations. | The target domain (individual fisher decision-making) involves a single advisory system. Multi-agent extension is future work. |

### 8.2 Evaluation Limitations

| Limitation | Explanation |
|---|---|
| **Scenario-based, not operational** | The socio-technical evaluation uses controlled scenarios, not live fishing decisions. Ecological validity is limited. |
| **Small sample** | 30–40 participants is sufficient for mixed-methods but cannot support population-level generalisation. |
| **Single domain evaluation** | Generalisability is argued structurally but demonstrated only in fisheries. |
| **No longitudinal trust data** | Trust calibration is measured in a single session, not over extended use. |

### 8.3 Formal Limitations

The formal model makes seven explicit assumptions (see `justification-formal-model.md` §8): observability of E, discreteness of S, determinism of f(E), independence of governance from AI, monotonicity of risk (severity ordering), stationarity of thresholds within a decision episode, and completeness of E. Each assumption is stated, justified, and its violation consequences analysed.

**Detailed justification**: `justification-formal-model.md` §8–9, `justification-low-resource-environments.md` §5.

---

## 9. If You Had More Time, What Would You Improve?

Five extensions, in priority order:

1. **Longitudinal field deployment** — Deploy the prototype with actual fishers over 6–12 months to measure trust calibration dynamics, adoption trajectory, and decision quality in ecological conditions. The current evaluation is scenario-based; extended deployment would provide real-world validity.

2. **Adaptive threshold calibration** — Develop a method for adjusting the classification thresholds in f(E) based on observed outcomes, while maintaining a formal proof that the adapted governance still satisfies the Safety Dominance Property. This addresses the "no learning" limitation.

3. **Multi-domain instantiation** — Implement the architecture in a second domain (e.g., mountain rescue or agricultural advisory) to empirically demonstrate domain generality beyond structural argument.

4. **Hysteresis and transition dynamics** — Formally characterise the state transition behaviour, including hysteresis width optimisation and the user experience of mode transitions. The current architecture specifies hysteresis at boundaries but does not optimise it.

5. **Multi-agent governance** — Extend the architecture to govern multiple AI advisory systems operating under the same environmental classification, addressing scenarios where different AI models provide recommendations for different aspects of the same decision.

---

## 10. Why Is This a PhD and Not a Master's Project?

A Master's project typically implements a known solution in a new context or evaluates an existing approach. This work creates a *new kind of governance mechanism* that does not exist in the literature, formalises it mathematically, demonstrates it in a domain, and evaluates it both technically and socio-technically. The distinction is in the contribution type and its validation depth.

### 10.1 Novel Formal Contribution

The two-level governance pair (G(S), A_AI(S)), the containment property, and the Safety Dominance Property are original formal constructs. They are not adaptations of existing formalisms — no prior work defines graduated advisory scope governance conditioned on environmental state. Four independent systematic reviews (Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md); Newcomb & Ochoa, 2026 [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md); Bengio et al., 2026 [[notes]](../notes/International%20AI%20Safety%20Report%202026.md); Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)) confirm that the architectural mechanism is new. A Master's project does not produce new formal constructs confirmed as novel by four independent literature surveys.

### 10.2 Multi-Method Validation

The evaluation spans:
- **Formal verification** (O2): mathematical proof that the Safety Dominance Property holds
- **Technical evaluation** (O4): three-condition comparative testing (ungated vs binary-gated vs two-level graduated)
- **Socio-technical evaluation** (O5): user study with target population measuring trust, comprehension, and decision behaviour across governance modes

This triangulation — formal proof + technical comparison + human evaluation — exceeds Master's-level validation, which typically involves one method.

### 10.3 Design Science Research Methodology

The work follows Peffers et al.'s DSR methodology across the full cycle: problem identification (PS1–PS5), objective definition (O1–O5), design and development (architecture + prototype), demonstration (fisheries instantiation), and evaluation (O4 + O5). Each phase produces an independently assessable contribution. A Master's project typically executes one or two phases.

### 10.4 The Contribution Test

The simplest PhD test: does this change what the field knows? Before this work, the field had binary safety governance (AI on/off) and separate output filtering (guardrails). After this work, the field has a formally specified mechanism for graduated advisory scope governance conditioned on environmental state, with formal properties (containment, Safety Dominance), empirical demonstration in a novel domain, and socio-technical evaluation of the intermediate mode. This is a knowledge contribution, not an application of existing knowledge.

**Detailed justification**: `justification-contribution-characterisation.md`, `justification-novelty-gap.md`, `justification-formal-model.md`.

---

## 11. The Most Important Question: Why Is This Better Than Existing Safety Gating, Adaptive Autonomy, or Guardrail Systems?

### 11.1 The Prepared Answer

This architecture is not "better" than safety gating, adaptive autonomy, or guardrails in the sense of replacing them — it solves a different problem that none of them addresses. Each existing class governs AI at only one level; this architecture governs at two levels simultaneously, conditioned on the same environmental state. The specific structural gap in each class is:

**Safety gating** (shields, safety filters, GS AI) implements Level 1: whether AI participates. Könighofer et al.'s (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) shields partition states into a winning region (AI operates) and a dangerous region (fallback activated). Bajcsy & Fisac's (2024) [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md) safety filter either permits or replaces AI actions. Dalrymple et al.'s (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) GS AI verifier either certifies a policy or blocks it. In every case, when AI is permitted, it operates with *unrestricted advisory scope*. Könighofer et al. empirically show that intermediate-restrictiveness shields (ε = 0.03, 0.05) outperform both no restriction and maximum restriction — directly motivating a CAUTION mode — but their shield has no mechanism to implement one. The governance is binary: inside the winning region or outside it.

**Adaptive autonomy** (Flehmig et al., Gyllenhammar et al.) recognises that binary is too coarse and introduces graduated modes. Flehmig et al.'s (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) traffic-light model — the closest structural precedent — classifies AI status into three levels (green/orange/red). But at both green and orange, the AI operates with *identical, unrestricted scope*. The orange level changes what the *human supervisor* does (more thorough checks), not what the *AI may recommend*. The graduation is in supervisory intensity, not advisory scope. Gyllenhammar et al.'s (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) ODD → ROD → MRC restricts what the *system may operationally attempt*, not what *types of recommendations the AI generates*. Neither implements A_AI(S) — the state-conditioned admissible recommendation space.

**Guardrails** (AgentSpec, SHIELDAGENT, LlamaGuard) implement output-level control: intercepting AI output and filtering or modifying it per individual rules. Wang et al.'s (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md) AgentSpec evaluates each planned action against each rule (r = (η_r, P_r, E_r)). Chen, Kang & Li's (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md) SHIELDAGENT applies per-action LTL verification. These are sophisticated — but they are *per-action* and *static-rule-based*, not *state-conditioned*. The rule set does not change based on classified environmental state. The AI's admissible action space A is the same regardless of whether conditions are safe or dangerous. And they are *post-hoc*: they filter after the AI generates output, rather than defining the output space before reasoning begins.

**What this architecture does differently:**

The governance pair (G(S), A_AI(S)) operates at two levels simultaneously:
- **Level 1** — G(S): Does the AI participate at all? (Same function as safety gating — but conditioned on environmental state, not AI performance)
- **Level 2** — A_AI(S): What *types* of recommendations may the AI produce? (No existing class implements this conditioned on environmental state)

Both levels are conditioned on the *same* classified environmental state S = f(E), producing a unified governance mechanism. The containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ formally guarantees that advisory scope narrows as conditions deteriorate. The Safety Dominance Property AI(E) ⊆ A_AI(S) formally guarantees that AI output never exceeds the governance-permitted space.

The result is an intermediate mode — CAUTION — that none of the existing classes can produce:
- Safety gating cannot produce it because it has no Level 2 (when AI is permitted, scope is unrestricted)
- Adaptive autonomy cannot produce it because its graduation governs supervisory behaviour, not advisory scope
- Guardrails cannot produce it because their rules are static (not state-conditioned) and post-hoc (not pre-hoc output space definition)

This is not a marginal improvement. It is a *structurally different governance mechanism* that enables a category of AI behaviour — graduated, state-conditioned advisory scope restriction — that is formally impossible under any existing paradigm.

### 11.2 Examiner Challenge: "Baxi (2026) Has Both L1 and L2 Under the Same Variable — Why Is It Only 'Partial' on Unified Governance?"

This is the hardest challenge at the comparison table. An examiner who has read Baxi carefully will press this point.

**The short answer**: Baxi has the right *structure* for unified governance but the wrong *conditioning variable*. "Partial" means the architectural form is correct but the governance trigger is orthogonal to environmental safety state.

**The full answer in four parts:**

**1. What Baxi gets right.** Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) implements a K-tier permission architecture where a gate function maps a verified robustness score to a discrete tier T_k. Both L1 (participation) and L2 (permission scope) are conditioned on the *same* T_k. The containment structure E(T_k) ⊂ E(T_{k+1}) is formally analogous to A_AI(CAUTION) ⊂ A_AI(SAFE). This is genuine structural unification — both governance levels respond to the same classified variable — and it is why the table shows L1 = Yes, L2 = Yes, and Formal Model = Yes.

**2. What "Partial" means precisely.** The four-column test for Unified Governance in this review is: *L1 and L2 operate as a coordinated pair conditioned on classified environmental safety state S = f(E)*. Baxi satisfies three of the four conditions:
- ✅ L1 and L2 are coordinated (both conditioned on T_k)
- ✅ Formal containment structure present
- ✅ Runtime-adaptive (tier can change)
- ❌ Conditioning variable is not S = f(E) — it is agent robustness, not environmental state

**3. Why the conditioning variable matters.** T_k in Baxi is determined by the agent's own verified robustness score — an offline-assessed measure of AI trustworthiness. It answers: *How capable and reliable is this AI system?* The proposed architecture's S = f(E) answers: *How dangerous is the current physical environment?* These are orthogonal questions with different governance consequences:

| | Baxi (2026) | Proposed Architecture |
|---|---|---|
| **What triggers governance?** | Agent robustness degradation | Environmental danger increase |
| **When does scope narrow?** | When the AI becomes less reliable | When conditions become more dangerous |
| **Can a storm narrow scope?** | No — storm doesn't change robustness score | Yes — storm raises S from SAFE to CAUTION |
| **Can a robust AI in a hurricane get full scope?** | Yes — top-tier agent retains full permissions | No — CAUTION state overrides agent capability |
| **Who drives the governance?** | The AI's own properties | The environment's observable state |

**4. The functional consequence.** A maximally robust agent in Baxi (T_k = highest tier) retains full permissions regardless of whether it operates on a calm morning or in a Force 9 storm. Environmental danger does not trigger governance. The architecture is *capability-gated*, not *safety-state-gated*. The proposed architecture is the reverse: a highly capable AI under CAUTION state is still restricted to go/no-go and delay guidance — environmental danger overrides agent capability. This is the architectural distinction that environmental state conditioning adds over robustness-tier conditioning.

**The one-sentence examiner answer**: "Baxi has the right containment structure across two governance levels, but conditions on agent robustness rather than on classified environmental safety state — meaning a storm cannot trigger advisory scope restriction, only AI performance degradation can. That is why it is 'Partial': the structure is correct, the conditioning variable is orthogonal."

**Detailed justification**: `justification-advisory-scope-restriction.md` §6 (Baxi comparator row), `justification-architecture-differentiation.md` §4.

---

### 11.3 The Evidence Base (If Probed)

| Claim | Evidence |
|---|---|
| All safety gating is binary | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md): 91 papers, all binary; Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md): 46 papers, all binary safety boundaries |
| Adaptive autonomy governs supervision, not scope | Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md): traffic-light governs monitoring intensity; AI scope identical at green and orange |
| Guardrails are per-action and static | Wang et al. (2026) [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md): per-action rule evaluation; Chen et al. (2025) [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md): per-action LTL; neither varies rules by environmental state |
| No existing system implements A_AI(S) | Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md): 11 frontier frameworks, all binary deployment control; Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md): cross-domain survey confirms |
| CAUTION mode is ecologically valid | Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md): fishers operate go/cautious-go/don't-go; Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md): binary warnings ignored because no intermediate support |
| Containment and Safety Dominance are novel | No prior work defines these properties for graduated (non-binary) governance |

---

## 12. One-Minute Thesis

### 12.0 The Abstract Statement

> This research proposes a graduated safety-state-gated architecture for AI decision support in safety-critical operations. The architecture introduces a unified governance mechanism where environmental safety state controls both whether AI is allowed to participate and what AI is allowed to recommend. Unlike existing safety gating, adaptive autonomy, or guardrail systems, the proposed architecture implements a state-conditioned containment structure for advisory action spaces, enabling graduated risk-sensitive AI governance instead of binary safety control. The architecture is designed for low-resource environments and is evaluated through both technical simulation and socio-technical field studies in coastal fisheries.

**Terminology note**: "advisory action spaces" in this abstract corresponds to the formal construct A_AI(S) — the admissible recommendation space. "Technical simulation" corresponds to O4 scenario-based technical evaluation.

### 12.1 The Expanded Statement (For Oral Delivery)

> Every existing AI safety mechanism answers the same question: *should AI be allowed to act?* The answer is always binary — yes or no, permitted or blocked, inside the safety boundary or outside it. Four independent systematic reviews covering hundreds of papers confirm this.
>
> But real-world decision-makers don't operate in binary. Fishers go freely in good conditions, go with caution in marginal conditions, and stay home in dangerous conditions. They have three modes, but their AI systems have only two.
>
> This research introduces a second governance question: *what should AI be allowed to recommend?* The architecture classifies environmental conditions into three safety states — SAFE, CAUTION, and UNSAFE — and uses this classification to control both whether AI participates and what types of recommendations AI may produce. In SAFE conditions, AI provides full decision support. In CAUTION conditions, AI participates but is restricted to robust recommendation types — go/no-go and delay guidance — while precision-dependent recommendations like departure timing and trip duration are suppressed. In UNSAFE conditions, AI is disabled entirely.
>
> The key formal property is containment: the set of recommendations AI may produce in SAFE conditions is strictly larger than in CAUTION, which is strictly larger than the empty set in UNSAFE. This guarantees graduated restriction — AI capability narrows as risk increases — and the Safety Dominance Property guarantees that AI output never exceeds the governance-permitted space.
>
> This is the first architecture that unifies participation governance and advisory scope governance under the same environmental safety classification. It is designed for low-resource environments — the governance layer is deterministic, runs offline, and requires no cloud computing — and is evaluated through both technical simulation and socio-technical field studies with coastal fishers in Malaysia.

### 12.2 The 30-Second Version (If Time-Pressed)

> Existing AI safety governance is binary: AI is either fully on or fully off. This research introduces a two-level governance architecture where environmental safety state controls not only *whether* AI participates but *what* AI is permitted to recommend. The result is a formally guaranteed intermediate mode — CAUTION — where AI operates under restricted advisory scope, providing only recommendation types that remain reliable under environmental uncertainty. No existing architecture — safety shields, adaptive autonomy, or guardrails — implements this state-conditioned advisory scope restriction. The architecture is demonstrated and evaluated in coastal fisheries, a safety-critical domain where practitioners already operate in three modes but have no formal AI governance support for the intermediate one.

### 12.3 Alignment Check

| Element | One-Minute Thesis | Justification Alignment |
|---|---|---|
| Binary governance gap | "Four independent systematic reviews" | `justification-novelty-gap.md` §2–4: Ramos, Newcomb, Bengio, Perez-Cerrolaza |
| Tripartite domain pattern | "Fishers go freely... go with caution... stay home" | `justification-three-states.md` §2: Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), Rahim (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md), Yamin (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md) |
| Two governance levels | "Whether AI participates and what AI may recommend" | `justification-unified-governance.md` §1–3: G(S) + A_AI(S) |
| Environmental state conditioning | "Classifies environmental conditions into three safety states" | `justification-environmental-state-governance.md`: why environmental state, not AI confidence |
| Containment property | "Strictly larger... strictly larger... empty set" | `justification-formal-model.md` §1.4: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ |
| Safety Dominance | "AI output never exceeds governance-permitted space" | `justification-formal-model.md` §1.5: AI(E) ⊆ A_AI(S) |
| CAUTION mode specifics | "Go/no-go and delay... timing and duration suppressed" | `justification-caution-mode-operation.md` §1–2: A_AI(CAUTION) = {Go, Delay} |
| Low-resource design | "Deterministic, runs offline, no cloud computing" | `justification-low-resource-environments.md` §2: O(1), fully offline |
| Novelty claim | "First architecture that unifies..." | `justification-novelty-gap.md` §1: 4 SLR confirmations |
| Evaluation | "Technical simulation and socio-technical field studies" | `justification-socio-technical-evaluation.md`: O4 + O5 design |
| Domain choice | "Coastal fishers in Malaysia" | `justification-low-resource-environments.md` §1: Terengganu target population |

---

## Comparative Summary

| Question | Core Answer | Key Evidence | Detailed Document |
|---|---|---|---|
| Main contribution? | Two-level governance pair (G(S), A_AI(S)) conditioned on environmental safety state | Formal definitions + 4 SLR gap confirmations | `justification-contribution-characterisation.md` |
| What problem? | Binary governance forces false dilemma; no support for intermediate operational mode | Ramos (91 papers), Newcomb (46 papers), Bengio (11 frameworks), Perez-Cerrolaza (cross-domain) | `justification-novelty-gap.md` |
| Why necessary? | Governance gap + domain necessity + formal necessity | Gao tripartite pattern, Rahim binary warning failure, 4 SLR confirmations | `justification-three-states.md`, `justification-unified-governance.md` |
| What is novel? | Five-point novelty: unified pair, state-conditioned scope, containment, Safety Dominance, pre-hoc definition | No existing architecture implements any of the five | `justification-novelty-gap.md` |
| Research gap? | PS1+PS2: no intermediate mode, no environmental-state-conditioned scope restriction | Alignment table, 4 independent confirmations | `research-alignment-table.md` |
| Why fisheries? | Tripartite pattern, no existing governance, low-resource constraints force good design | Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md), Rahim (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md), Yamin (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md), Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) | `justification-low-resource-environments.md` |
| Generalisable? | Yes — domain-general at formal level, domain-specific only at parameterisation | Pipeline, properties, separation all domain-independent | `justification-caution-mode-operation.md` §7 |
| Limitations? | 3-state only, threshold-based, no adaptation, single-agent, scenario-based evaluation | Explicitly stated with justification for acceptability | `justification-formal-model.md` §8–9 |
| More time? | Longitudinal deployment, adaptive thresholds, multi-domain, hysteresis optimisation, multi-agent | Prioritised by impact | — |
| Why PhD not Master's? | New formal constructs + multi-method validation + full DSR cycle + knowledge contribution | 4 SLR novelty confirmation, triangulated evaluation, 5 PS | `justification-contribution-characterisation.md` |
