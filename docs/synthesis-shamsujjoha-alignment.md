# Research Synthesis: Architectural Alignment with Shamsujjoha et al. (2025)

**Document type:** Architectural alignment synthesis  
**For:** Chapter 2 (Literature Review), Chapter 3 (Architecture Design), and viva preparation  
**Paper:** Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) — *Swiss Cheese Model for AI Safety: A Taxonomy and Reference Architecture for Multi-Layered Guardrails of Foundation Model Based Agents*

**Cross-references:** `docs/justification-architectural-comparison.md` (broader four-architecture comparison), `docs/justification-novelty-gap.md` (full gap argument), `docs/appendix-c-formalisation.md` (formal variable definitions)

---

## 2.1 Architectural Formalisation

Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) identify the necessary components for multi-layered AI safety — Agent Components and Multi-layered Runtime Guardrails — but leave the activation logic implicit. Their reference architecture does not specify a mechanism that connects a specific operational context to a specific guardrail configuration; guardrail activation is determined per artifact and per quality attribute, not by classified environmental state.

This research introduces a **State-Conditioned Selection Mechanism** as a formal logic layer that makes this activation explicit. Specifically, the function S = f(E) classifies the current environmental state and the governance pair (G(S), A_AI(S)) determines which guardrail configuration applies. This formalises what Shamsujjoha et al.'s architecture leaves implicit: the transition logic between different safety configurations based on environmental risk.

---

## 2.2 Targeted Artifact Restriction: Reasoning vs. Knowledge Base

The Shamsujjoha taxonomy identifies multiple agent artifacts as potential guardrail targets, including Goals, Plans, Memory, Knowledge Bases, and Reasoning. This architecture anchors its intervention primarily at the **Reasoning artifact level**.

The mechanism — **Rule-set Starvation** — is defined as: *a pre-inference guardrail that restricts the Reasoning artifact (as categorised by Shamsujjoha et al., 2025) by supplying only the rule-set RS(S) corresponding to the current safety state S before inference begins, such that no rule in RS(S) can produce recommendations outside A_AI(S).*

By conditioning the rule-set on the classified safety state — RS(SAFE) ⊃ RS(CAUTION) ⊃ RS(UNSAFE) = ∅ — the architecture prevents the formation of high-specificity recommendations at the reasoning stage. This is a higher-tier intervention than standard post-generation filtering: the inadmissible recommendation is never generated, not merely withheld after generation. The Safety Dominance Property AI(E) ⊆ A_AI(S) holds by construction, not by runtime enforcement.

This indirectly limits the effective Knowledge Base as well — RS(CAUTION) does not include rules that draw on departure time or duration knowledge — but the primary mechanism is a Reasoning-level constraint using Shamsujjoha et al.'s own taxonomy vocabulary.

---

## 2.3 Addressing the Formal Gap

The primary technical novelty of this research lies in moving beyond informal context-dependent safety to a formal, state-conditioned governance framework.

**Defense statement:** While Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) acknowledge "context-dependent rules" as a valid guardrail category within their taxonomy, their reference architecture lacks a **formal**, state-conditioned activation mechanism. This research fills that gap by introducing an environmental state classification function S = f(E) and a governance pair (G(S), A_AI(S)) that provides a mathematical guarantee — the Safety Dominance Property AI(E) ⊆ A_AI(S) — that the AI's admissible advisory scope is structurally restricted across all possible environmental states.

The two contributions are complementary. Shamsujjoha et al. taxonomise the governance action space — what governance actions exist, what targets they apply to, what rule types are possible. This architecture provides the state-conditioned selection mechanism — when to apply which governance configuration, governed by formally classified environmental state.

---

## 2.4 Comparative Summary

| Feature | Reference Architecture (Shamsujjoha et al., 2025) | This Architecture |
|---|---|---|
| **Structural logic** | Structured across quality × pipeline × artifact dimensions, but activation is not conditioned on classified environmental state | Explicit: selection logic formalised via S = f(E) |
| **Primary target** | General artifacts (Plans, Tools, Memory, Reasoning) | Reasoning artifact: conditioned rule-sets RS(S) |
| **Activation trigger** | Policy-based / contextual (not formalised as environmental state) | State-conditioned: discrete safety states {SAFE, CAUTION, UNSAFE} |
| **Safety guarantee** | Multi-layered defence-in-depth | Safety Dominance Property: AI(E) ⊆ A_AI(S) by construction |

**The single discriminating row is Activation Trigger.** Shamsujjoha et al.'s context-dependent rules adjust guardrails based on data or deployment context. This architecture activates governance configurations based on classified environmental safety state S = f(E) — a formally different trigger with a formally defined output (A_AI(S)) and a provable safety property.
