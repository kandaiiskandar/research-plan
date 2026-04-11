---
layout: document
---

# Why Unified? Justification for the Two-Level Governance Pair

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 2 (Literature Review), Chapter 3 (Architecture Design), and viva preparation  
**Questions addressed**: What is unified governance? Why must participation and scope be governed together? Could they be independent? What if only one level operates? Is unification necessary or a design choice? Does any existing system do this? How is this proved different? Is this the main contribution? Domain generality?

**Cross-references**: For the novelty gap argument with full corpus evidence, see `justification-novelty-gap.md`. For differentiation from four system classes, see `justification-architecture-differentiation.md`. For why CAUTION restricts scope rather than blocking, see `justification-advisory-scope-restriction.md`. For domain generality of CAUTION, see `justification-caution-mode-operation.md` §7.

---

## 1. What Is Unified Governance?

### 1.1 The Governance Pair

The proposed architecture implements two governance functions:

- **G(S)** — the participation gate (Level 1): determines whether AI may participate at all
- **A_AI(S)** — the admissible advisory space (Level 2): determines what types of recommendations AI is permitted to generate

These two functions are **unified** in a specific, formal sense: both are conditioned on the **same** classified environmental safety state S = f(E). The governance pair (G(S), A_AI(S)) is a single, state-conditioned mechanism — not two independent systems that happen to coexist.

### 1.2 Unified Means State-Coupled

"Unified" does not mean "combined into one function." G(S) and A_AI(S) remain formally distinct — they answer different questions (may AI participate? what may AI recommend?) and produce different outputs (binary gate vs. recommendation type set). "Unified" means:

1. **Same conditioning variable**: Both functions take the same input S, which is itself derived from the same environmental classification f(E)
2. **Consistent governance semantics**: The outputs of G(S) and A_AI(S) are mutually consistent — when G(S) = 0 (no participation), A_AI(S) = ∅ (empty scope); when G(S) = 1, A_AI(S) defines the permitted scope
3. **Single classification, dual governance**: One environmental assessment produces governance decisions at both levels simultaneously

The formal pipeline is:

```
E → S = f(E) → (G(S), A_AI(S)) → AI(E) ⊆ A_AI(S)
```

One classification. Two governance outputs. One formal guarantee (Safety Dominance Property).

### 1.3 What Unification Produces That Separate Levels Cannot

The containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ is a property of the **unified pair**, not of either level independently. Level 1 alone produces binary governance: G(S) ∈ {0, 1}. Level 2 alone produces scope restriction without a participation gate. The containment property requires both levels operating over the same state variable to produce the graduated governance hierarchy that is the architectural contribution.

---

## 2. Why Must Participation and Scope Be Governed Together?

### 2.1 The Complementarity Argument

Participation governance (Level 1) and scope governance (Level 2) address different failure modes. Neither alone is sufficient. Together, they cover the full governance space.

**Level 1 alone creates a false dilemma.** Binary participation governance forces a choice between two extremes: full AI (all recommendation types, regardless of conditions) or no AI (complete withdrawal). Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), reviewing 91 papers on collaborative intelligence for safety-critical industries, find that all safety governance mechanisms in those papers are binary — AI operates or is overridden. This binary paradigm cannot represent the intermediate case where AI participation is valuable but full advisory scope is inappropriate. The fisher who faces elevated-but-not-extreme conditions needs decision support — but needs it *scoped* to what is reliable. Level 1 alone cannot provide this.

**Level 2 alone leaves the shutdown case ungoverned.** Scope governance without a participation gate means AI always participates, with varying scope. But under genuinely unsafe conditions (S = UNSAFE), even directional guidance (go/no-go) may be unreliable — the AI should not participate at all. Without Level 1, the architecture has no mechanism for complete AI withdrawal. The containment hierarchy collapses: without A_AI(UNSAFE) = ∅ enforced by G(S) = 0, the system cannot guarantee zero AI influence under the most dangerous conditions.

**Together, they produce graduated governance with formal bounds.** The unified pair produces three operationally distinct governance configurations:

| State | G(S) | A_AI(S) | Operational meaning |
|---|---|---|---|
| SAFE | 1 | R_full | AI participates with full scope |
| CAUTION | 1 | R_restricted ⊂ R_full | AI participates with restricted scope |
| UNSAFE | 0 | ∅ | AI does not participate |

This is the minimum governance configuration that resolves the binary false dilemma while providing complete coverage. SAFE and UNSAFE are achievable with Level 1 alone. CAUTION requires Level 2. The three configurations together require both levels unified under the same state variable.

### 2.2 The Formal Argument

The Safety Dominance Property AI(E) ⊆ A_AI(S) for all E requires that:
- A_AI(S) is defined for each S (Level 2 provides this)
- G(S) = 0 implies AI(E) = ∅ ⊆ ∅ = A_AI(UNSAFE) (Level 1 enforces this)
- G(S) = 1 implies AI(E) ⊆ A_AI(S) for S ∈ {SAFE, CAUTION} (Level 2 enforces this)

The property is a joint guarantee of both levels. If Level 1 fails (AI participates when it should not), Level 2 cannot compensate — it restricts scope but cannot prevent participation. If Level 2 fails (AI outputs recommendation types outside A_AI(S)), Level 1 cannot compensate — it can only block or permit, not scope-restrict. The Safety Dominance Property requires both levels functioning correctly under the same state classification.

---

## 3. Could These Two Mechanisms Be Implemented Independently?

### 3.1 Technically Yes; Architecturally Harmful

There is no technical barrier to implementing G(S) and A_AI(S) as independent systems with independent triggers. Level 1 could be triggered by AI performance degradation (as in Flehmig et al., 2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md). Level 2 could be triggered by output content analysis (as in guardrail systems: Shamsujjoha et al., 2025 [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al., 2025). Each would function independently.

### 3.2 Why Independent Implementation Fails

**Inconsistent governance states.** If Level 1 and Level 2 are triggered by different variables, they can produce contradictory governance:

| Scenario | Level 1 (performance-triggered) | Level 2 (content-triggered) | Result |
|---|---|---|---|
| AI performs well in dangerous environment | G = 1 (AI performing fine) | A_AI unrestricted (no content violation) | **Full AI in dangerous conditions — governance failure** |
| AI performs poorly in safe environment | G = 0 (AI degraded) | A_AI restricted (content flagged) | **No AI when conditions are safe — unnecessary restriction** |
| AI performs well, environment is CAUTION | G = 1 (AI performing fine) | A_AI unrestricted (no content violation) | **Full scope under CAUTION — the CAUTION mode never activates** |

The third scenario is the critical one: independently triggered levels will almost never produce the CAUTION governance configuration (G = 1, A_AI restricted) because Level 1 has no reason to restrict when AI performs well, and Level 2 has no reason to restrict when individual outputs contain no prohibited content. The CAUTION mode — the novel architectural contribution — *only exists* when both levels respond to the same conditioning variable.

**No formal guarantee across levels.** The Safety Dominance Property is a joint property: AI(E) ⊆ A_AI(S) for all E. If G(S) and A_AI(S) are independently triggered, the "S" in each function is a different variable — there is no single S that determines both. The property becomes: AI(E) ⊆ A_AI(S₂) when G(S₁) = 1, where S₁ ≠ S₂. This is not provable without additional assumptions about the relationship between S₁ and S₂ — assumptions that are unnecessary when both levels use the same S.

**Loss of the containment hierarchy.** The containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ requires that A_AI is indexed by the same state variable as G. If A_AI is indexed by content analysis results and G is indexed by performance metrics, the containment hierarchy has no grounding — the states are not ordered by the same dimension.

### 3.3 The Design Principle

Unified governance is not a convenience — it is a **formal requirement** for the properties that define the architecture's safety guarantee. The same principle appears across the corpus:

- **Dalrymple et al. (2024)** [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md): The Guaranteed Safe AI framework requires that the world model, safety specification, and verifier all operate over the same formal domain — the verifier's guarantee is valid only relative to the world model that generated it. Independent specifications with independent world models cannot produce a unified guarantee.

- **Bajcsy & Fisac (2024)** [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md): The Human-AI Safety Filter's Theorem 1 requires that the safety monitor and intervention scheme share the same state space and safety value function. Independent monitoring and intervention would invalidate the formal guarantee.

- **Könighofer et al. (2025)** [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md): Shields are computed from a single formal specification and environment model. A shield computed from one model cannot govern an agent operating in a different model's state space.

The proposed architecture applies the same principle: governance functions that must provide a joint guarantee must share a common conditioning variable.

---

## 4. What Happens If Only One Level Operates?

### 4.1 Level 1 Only (Participation Without Scope Restriction)

This is the status quo across the entire safety-critical AI literature. Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) confirm it across 91 papers; Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) confirm it across 46 formal methods studies; Bengio et al. (2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) confirm it across 11 Frontier AI Safety Frameworks.

The consequences are documented throughout the corpus:

**False precision under elevated conditions.** When AI participates with full scope under CAUTION conditions, it generates departure time and trip duration recommendations whose underlying models are compromised by environmental uncertainty. These precise-looking recommendations anchor human decisions. Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) demonstrate that communicated system capability shapes reliance more than subjective trust — a precise recommendation communicates high capability implicitly.

**Binary over-restriction.** Without Level 2, the only governance response to elevated conditions is to block AI entirely (G = 0). This removes go/no-go and delay guidance that remains reliable — valuable decision support discarded along with unreliable detail. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) document that binary blocking creates "new system-level hazards" from excessive false alarms and cognitive overload.

**No proportionate response.** The ALARP principle requires risk controls proportionate to the risk level. Level 1 alone provides only two responses (full AI or no AI) for three or more distinct risk conditions — violating proportionality.

### 4.2 Level 2 Only (Scope Restriction Without Participation Gate)

This would mean AI always participates (no shutdown mode), but with varying scope. This is problematic:

**No complete withdrawal under extreme conditions.** Under genuinely UNSAFE conditions — severe storm, vessel damage, zero visibility — even go/no-go guidance from the AI is inappropriate. The human should rely entirely on their own assessment and any emergency protocols. Level 2 alone can restrict scope to {Go, Delay} but cannot withdraw AI entirely. The A_AI(UNSAFE) = ∅ endpoint requires Level 1.

**No formal shutdown guarantee.** Safety-critical systems require a well-defined safe state — the minimal risk condition (MRC) in Gyllenhammar et al.'s (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) terminology. For an advisory system, the MRC is "AI does not advise." Level 2 alone has no mechanism to reach this state because it governs scope, not participation. The system has no off switch.

**Trust confusion at extremes.** If the system continues providing (increasingly restricted) guidance under extreme conditions, users cannot distinguish "AI has no useful guidance" from "AI is providing the most restricted guidance." McGrath et al. (2025 — CHAI-T) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) establish that trust calibration requires clearly distinguishable system modes. A system that always participates but with varying scope produces a continuum of behaviour rather than the discrete modes that enable calibration.

### 4.3 Both Levels Together

The unified pair eliminates both failure modes:
- Level 1 provides complete withdrawal at UNSAFE (the formal shutdown mechanism)
- Level 2 provides proportionate restriction at CAUTION (the intermediate governance mechanism)
- Together, they produce three discrete, distinguishable governance configurations
- The Safety Dominance Property provides a formal guarantee that spans both levels

---

## 5. Is Unified Governance Necessary or Just a Design Choice?

### 5.1 Necessary for the Formal Properties

If the architecture's value were purely conceptual — "it would be nice to have graduated governance" — unification would be a design choice. But the architecture claims specific formal properties:

- **Containment**: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- **Safety Dominance**: AI(E) ⊆ A_AI(S) for all E
- **Graduated governance**: three discrete configurations with qualitatively different AI behaviour

These properties are **only achievable** with unified governance — both levels conditioned on the same S. As shown in §3.2, independent levels with different conditioning variables cannot produce the containment hierarchy or the Safety Dominance Property without additional (unnecessary) assumptions. The formal properties define the architecture; unified governance is necessary to achieve them.

### 5.2 Necessary for the CAUTION Mode

The CAUTION mode is the novel governance configuration: G(S) = 1, A_AI(S) = R_restricted. This configuration *only exists* when Level 1 permits participation AND Level 2 restricts scope simultaneously, both responding to the same environmental state classification. Independent levels, as shown in §3.2, will almost never coincidentally produce this configuration for the right environmental conditions.

### 5.3 The Baxi Parallel

Baxi (2026 — CGAE) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) provides independent confirmation that unified governance is necessary, not merely convenient. CGAE's gate function f(R) → T_k and permission sets E(T_k) are unified under the same robustness assessment — the tier determines both access (Level 1 analogue) and economic permission scope (Level 2 analogue) simultaneously. Baxi does not consider implementing these independently, because the formal properties (Theorem 3: bounded economic exposure; Theorem 6: monotonic safety scaling) require both levels to be determined by the same conditioning variable. The necessity of unification is independently derived in a structurally parallel but domain-orthogonal architecture.

---

## 6. Does Any Existing System Already Do This?

### 6.1 The Short Answer

No. This is the core novelty claim, supported by four independent systematic reviews.

### 6.2 The Detailed Evidence

The gap argument is presented in full in `justification-novelty-gap.md`. The summary:

**Safety shields** (Könighofer et al., 2025 [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Bajcsy & Fisac, 2024 [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Corsi et al., 2024 [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md)): Implement Level 1 (binary participation gate) with formal guarantees. Per-state safe action sets vary — the closest mechanism to A_AI(S) — but governance is per-action binary (safe/unsafe), not per-state-type graduated. No CAUTION mode exists. No system classifies environmental state into three discrete governance modes with different advisory scope types.

**Guardrails and safety filters** (Shamsujjoha et al., 2025 [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al., 2025; Chen, Kang & Li, 2025 — SHIELDAGENT [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md); Wang et al., 2026 — AgentSpec [[notes]](../notes/AgentSpec-%20Customizable%20Runtime%20Enforcement%20for%20Safe%20and%20Reliable%20LLM%20Agents.md); Liang et al., 2025): Implement Level 2 (output constraint) statically. The prohibited output set does not vary with classified environmental state. Per-output binary pass/block, not state-conditioned scope restriction.

**Adaptive autonomy** (Flehmig et al., 2024 [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md); Gyllenhammar et al., 2025 [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md)): Implement graduated modes but govern supervisory intensity or operational domain restriction — not AI advisory scope. Flehmig's Level 2 (orange) changes monitoring behaviour; AI advisory scope is identical at Levels 1 and 2.

**Shielded RL review** (Odriozola-Olalde et al., 2023 [[notes]](../notes/Shielded%20Reinforcement%20Learning-%20A%20review%20of%20reactive%20methods%20for%20safe%20learning.md)): Reviews all reactive shielding methods for safe learning and confirms that every method implements a binary safety gate. No reviewed method conditions the shield on classified environmental states or restricts recommendation types rather than individual actions.

**Formal methods** (Newcomb & Ochoa, 2026 [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)): All 46 reviewed studies operate with binary safety boundaries across eight formal method categories. No graduated safety states; no state-conditioned scope restriction.

**International governance** (Bengio et al., 2026 [[notes]](../notes/International%20AI%20Safety%20Report%202026.md)): All 11 Frontier AI Safety Frameworks implement Level 1 (capability-triggered participation decisions). None implements state-conditioned Level 2.

**Closest prior work** (Baxi, 2026 — CGAE [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md)): Implements unified graduated governance with formal properties — but conditioned on verified agent robustness, not environmental state. Economic domain, not physical safety. ArXiv preprint, not peer-reviewed. Structurally parallel but orthogonally conditioned.

### 6.3 What "Already Does This" Would Require

For an existing system to fill the gap, it would need to:
1. Classify environmental conditions into discrete safety states (S = f(E))
2. Use those states to determine AI participation (G(S))
3. Use those *same* states to determine AI advisory recommendation scope (A_AI(S))
4. Define a containment hierarchy over recommendation types (A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅)
5. Operate at runtime, with continuous reclassification as conditions change

No system in the reviewed literature satisfies all five requirements. Most satisfy at most one. The closest (Flehmig) satisfies 1 and 2 but not 3 — the decisive gap.

---

## 7. How Do You Prove This Architecture Is Different?

### 7.1 The Five-Point Differentiation Method

The differentiation is demonstrated through five independent lines of evidence:

**Line 1 — Structural comparison.** Each candidate prior work is compared against the formal definition of the governance pair. The comparison identifies which components (S = f(E), G(S), A_AI(S), containment, Safety Dominance) each prior work implements and which it lacks. This is the method used in `justification-novelty-gap.md` §2–§8, producing the 22-row summary table (§12).

**Line 2 — Systematic review confirmation.** Four independent systematic reviews — covering 91 collaborative intelligence papers (Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)), 46 formal methods studies (Newcomb & Ochoa, 2026 [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)), 11 international safety frameworks (Bengio et al., 2026 [[notes]](../notes/International%20AI%20Safety%20Report%202026.md)), and cross-domain safety-critical AI (Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)) — each independently confirm binary governance as universal. The gap is not inferred from a handful of papers; it is confirmed across four independent surveys of the field.

**Line 3 — Closest-prior-work analysis.** Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) and Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) receive extended treatment as the two closest prior works. Each is compared on the specific dimensions where it approaches the proposed architecture, and the precise point of divergence is identified: Flehmig governs supervisory intensity, not advisory scope; Baxi conditions on robustness, not environmental state.

**Line 4 — Formal property uniqueness.** The Safety Dominance Property AI(E) ⊆ A_AI(S) for graduated (non-binary) governance has no precedent. Binary analogues exist (shield winning regions, safety filter Theorem 1, GS AI verifier certificates), and Baxi's Theorem 3 is a graduated analogue in a different domain. But no prior work defines or proves this property for environment-conditioned governance of AI advisory scope in a physical safety-critical domain.

**Line 5 — Domain validation.** The tripartite go/cautious-go/don't-go decision pattern is independently documented in two national fisheries contexts (Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md)) and the binary governance failure is documented empirically (Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md): binary warnings overridden; Yamin et al., 2025 [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md): decision support vacuum at intermediate conditions). No prior architecture addresses this documented domain need.

---

## 8. Is Unified Governance the Main Contribution?

### 8.1 Yes — Precisely Stated

The main contribution is:

> A formal governance architecture implementing a two-level governance pair (G(S), A_AI(S)) conditioned on classified environmental safety state S = f(E), with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S).

Every element of this statement is necessary:
- "Two-level governance pair" — not just Level 1 or just Level 2
- "Conditioned on classified environmental safety state" — not AI confidence, not robustness, not performance
- "S = f(E)" — deterministic, from observable environmental parameters
- "Containment property" — graduated, not binary
- "Safety Dominance Property" — formally guaranteed, not empirically observed

### 8.2 What Is Not the Main Contribution

- The three-state classification itself (traffic-light classifications exist: Flehmig et al., 2024 [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md))
- Level 1 governance alone (extensively studied: shields, safety filters, guardrails)
- Level 2 governance alone (addressed by guardrail literature: Shamsujjoha et al., 2025 [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md))
- The fisheries application domain (domain choice enables validation, not novelty)
- The AI recommendation algorithm (the architecture is algorithm-agnostic)

The novelty is the **unification** of Level 1 and Level 2 under environmental state with formal properties — the specific mechanism by which the same classified state simultaneously governs participation and advisory scope.

---

## 9. Could Unified Governance Be Applied Outside Fisheries?

### 9.1 The Architecture Is Domain-General

The governance pair (G(S), A_AI(S)) conditioned on S = f(E) requires only:
- An observable environment with measurable parameters (E)
- A classification of those parameters into safety states (f(E))
- An AI system generating typed recommendations from a defined space (R)
- Recommendation types with different reliability profiles under elevated conditions

These requirements are met in any safety-critical AI decision support context where environmental conditions affect recommendation reliability. See `justification-caution-mode-operation.md` §7 for domain-specific examples (agriculture, maritime navigation, emergency response).

### 9.2 What Changes Across Domains

| Component | Domain-general (fixed) | Domain-specific (varies) |
|---|---|---|
| Governance pair (G(S), A_AI(S)) | Structure and formal properties | Specific recommendation types in R |
| State classification S = f(E) | Three-state structure and containment | Environmental parameters in E, threshold values |
| Safety Dominance Property | Formal definition and proof structure | Domain-specific instantiation of "safe" |
| Layered architecture | Three-layer separation | Specific sensor types, AI methods |

### 9.3 Why Fisheries Is the Validation Domain

Fisheries is not chosen because the architecture only works there. It is chosen because:

1. **Strongest empirical evidence for tripartite decisions** — go/cautious-go/don't-go independently documented across two national contexts (Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md))
2. **Documented binary governance failure** — binary warnings routinely overridden (Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md))
3. **Documented decision support vacuum** — TK erosion creates unmet need at intermediate conditions (Yamin et al., 2025 [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md))
4. **Low-resource constraints test architectural parsimony** — the architecture must work with limited compute, intermittent connectivity, and minimal sensor infrastructure
5. **Under-studied domain** — no formal AI governance architecture exists for small-scale fisheries (the domain gap is confirmed: no paper in the 63-paper corpus addresses coastal fisheries with formal governance)

The validation demonstrates the architecture works in a challenging, under-resourced domain. Domain generality is argued by structural analysis (§9.1–9.2) and supported by the cross-domain evidence that the binary governance gap is universal (Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md): six domains; Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md): four domains).

---

## 10. Comparative Summary Table

| Question | Answer | Key evidence |
|---|---|---|
| **What is unified governance?** | Both G(S) and A_AI(S) conditioned on the same S = f(E); single classification, dual governance output | Formal pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E) ⊆ A_AI(S) |
| **Why govern together?** | Level 1 alone is binary (false dilemma); Level 2 alone has no shutdown; together they produce three graduated configurations | Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md): L1-only is universal and insufficient; containment property requires both levels |
| **Could they be independent?** | Technically yes; architecturally harmful — inconsistent states, no joint formal guarantee, CAUTION never activates | Independent triggers produce L1=permit + L2=unrestricted under CAUTION conditions |
| **Level 1 only?** | False precision under elevated conditions; binary over-restriction; violates ALARP | Status quo across 91 papers (Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)), 46 studies (Newcomb & Ochoa, 2026 [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)), 11 frameworks (Bengio et al., 2026 [[notes]](../notes/International%20AI%20Safety%20Report%202026.md)) |
| **Level 2 only?** | No complete withdrawal; no formal shutdown; trust confusion at extremes | No MRC equivalent (Gyllenhammar et al., 2025 [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md)); no off switch for genuinely unsafe conditions |
| **Necessary or design choice?** | Necessary for formal properties (containment, Safety Dominance) and for CAUTION mode to exist | Independently confirmed by Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md): unified governance required for analogous formal properties |
| **Any existing system?** | No — confirmed by four independent systematic reviews covering 91 + 46 + 11 + cross-domain bodies | Closest: Flehmig (governs monitoring, not scope); Baxi (robustness-conditioned, not environment-conditioned) |
| **How proved different?** | Five-point method: structural comparison, SLR confirmation, closest-prior-work analysis, formal property uniqueness, domain validation | 22-row comparison table in `justification-novelty-gap.md` §12 |
| **Main contribution?** | Yes — the unification of L1 + L2 under environmental state with formal properties is the precise novelty | Not the states, not L1 alone, not L2 alone, not the domain, not the algorithm |
| **Domain-general?** | Architecture is domain-general; fisheries is the validation domain with strongest empirical grounding | Binary gap confirmed across 6 domains (Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)) and 4 domains (Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)); three-level response independently derived in automotive and industrial AI |

---

## 11. One-Paragraph Summary (for use in Chapter 2 or Chapter 3)

> The main contribution is the unified two-level governance pair (G(S), A_AI(S)) — a single, state-conditioned mechanism where the same classified environmental safety state S = f(E) simultaneously determines whether AI may participate (Level 1: G(S)) and what types of recommendations AI is permitted to generate (Level 2: A_AI(S)), with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S) guaranteed formally. Unification is not a design convenience but a formal necessity: the containment hierarchy and Safety Dominance Property are joint properties of both levels operating over the same state variable, and independent implementation with different triggers cannot produce them — Level 1 triggered by performance and Level 2 triggered by content analysis would almost never coincidentally produce the CAUTION configuration (G = 1, A_AI restricted) under the environmental conditions that warrant it. Level 1 alone — the universal paradigm across 91 collaborative intelligence papers (Ramos et al., 2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), 46 formal methods studies (Newcomb & Ochoa, 2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), and 11 Frontier AI Safety Frameworks (Bengio et al., 2026) [[notes]](../notes/International%20AI%20Safety%20Report%202026.md) — forces a binary false dilemma between full AI and no AI, violating ALARP and discarding reliable go/no-go guidance when binary blocking activates. Level 2 alone has no shutdown mechanism for genuinely unsafe conditions, no minimal risk condition (Gyllenhammar et al., 2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md), and produces trust confusion at the extremes (McGrath et al., 2025) [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md). No existing system implements both levels unified under classified environmental state: safety shields (Könighofer et al., 2025 [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md); Corsi et al., 2024 [[notes]](../notes/Verification-Guided%20Shielding%20for%20Deep%20Reinforcement%20Learning.md)) and safety filters (Bajcsy & Fisac, 2024 [[notes]](../notes/Human%E2%80%93AI%20Safety-%20A%20Descendant%20of%20Generative%20AI%20and%20Control%20Systems%20Safety.md); Dalrymple et al., 2024 [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md)) implement Level 1 only; guardrails (Shamsujjoha et al., 2025 [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md); Chen et al., 2025; SHIELDAGENT: Chen, Kang & Li, 2025 [[notes]](../notes/SHIELDAGENT-%20Shielding%20Agents%20via%20Verifiable%20Safety%20Policy%20Reasoning.md)) implement Level 2 statically without environmental state conditioning; Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) implement three-level classification but govern supervisory intensity, not advisory scope; Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) implements unified graduated governance with analogous formal properties but conditions on agent robustness, not environmental state. The architecture is domain-general — the binary governance gap it resolves is confirmed across six safety-critical domains (Ramos et al., 2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) and four industrial/transportation domains (Perez-Cerrolaza et al., 2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) — with coastal fisheries as the validation domain where empirical evidence for tripartite decision-making (Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md)) and the binary governance failure (Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md): binary warnings overridden; Yamin et al., 2025 [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md): decision support vacuum at intermediate conditions) is strongest.
