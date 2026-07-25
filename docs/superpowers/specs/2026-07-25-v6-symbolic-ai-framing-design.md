---
name: v6-symbolic-ai-framing
description: Two targeted presentation fixes to v6 paper — rename rule-based engine to Symbolic AI Reasoning Engine, and add LLM/symbolic AI framing in Mechanistic Basis
metadata:
  type: project
---

# v6 Paper — Symbolic AI Framing Fixes

**Goal:** Two targeted changes to `ipsci-2026-paper-v6.md` that resolve the two remaining presentation issues identified in pre-submission review. No structural changes; no new sections; no changes to Abstract or Conclusion. One new reference is added (Belle, 2025 [38]) to support the Symbolic AI terminology in change 1a.

## Context

The v6 restructure plan has been fully executed. The paper's research question, literature gap, architecture, and formalisation are internally consistent. Two presentation gaps remain:

1. **Fig. 3 labeling:** "Rule-based engine" does not signal to reviewers that this is the AI component. The paper repeatedly refers to "AI advisory" and "AI reasoning," so a reviewer unfamiliar with symbolic AI may momentarily think the AI component is absent.
2. **Mechanistic Basis framing:** The section builds its case around LLM-specific limitations (fixed inference pipeline, non-adaptive reasoning, unreliable self-assessment). The proposed architecture uses a rule-based (symbolic AI) engine. Without an explicit framing sentence, a reviewer could ask "why discuss LLM limitations if the system doesn't use LLMs?"

Both issues are **presentation and framing**, not conceptual weaknesses.

---

## Change Set 1: Fig. 3 and surrounding text

Four precise edits to the Proposed Architecture section. No other section is touched.

### 1a — Introductory sentence (new, before Fig. 3 paragraph)

Add one sentence at the start of the opening paragraph of the Proposed Architecture section, before the existing sentence "The mechanistic evidence above establishes that internal self-restraint cannot be relied upon...":

> *The proposed architecture employs a Symbolic AI Reasoning Engine, implemented as a knowledge-based rule system in the classical symbolic AI tradition [38], to generate recommendations within the constraints imposed by the participation and advisory-scope gates.*

**Purpose:** Introduces the term before the figure so readers understand Fig. 3 immediately on first contact. The Belle (2025) citation anchors "Symbolic AI" in published literature, pre-empting any reviewer query about the term.

### 1b — Fig. 3 ASCII diagram label rename

In the ASCII diagram inside Fig. 3, rename the component box:

- **From:**
  ```
  ┌────────▼───────────┐
  │  Rule-based engine │
  │  (RS(S) supplied   │
  │   before inference)│
  └────────┬───────────┘
  ```

- **To:**
  ```
  ┌────────▼───────────────┐
  │  Symbolic AI           │
  │  Reasoning Engine      │
  │  (RS(S) supplied       │
  │   before inference)    │
  └────────┬───────────────┘
  ```

**Purpose:** The component label now unambiguously identifies this as the AI component.

### 1c — Fig. 3 caption extension

Extend the Fig. 3 caption by appending one explanatory sentence after the existing caption text:

Existing: *"The graduated safety-state-gated architecture. Before any inference begins, a deterministic external classifier computes the environmental safety state S = f(E) outside the AI component. Both gates, G(S) and A_AI(S), are conditioned on S and together bound what the AI may recommend for the current observation."*

Append: *"The Symbolic AI Reasoning Engine is a knowledge-based expert system that applies predefined decision rules to generate recommendations within the advisory scope enforced by the governance layer."*

**Purpose:** Removes all ambiguity for reviewers who read captions before body text.

### 1d — Body text reference update

In the Domain Instantiation subsection, update one sentence for consistency with the new label:

- **From:** "The rule-based reasoning engine enforces the Safety Dominance Property by construction..."
- **To:** "The Symbolic AI Reasoning Engine enforces the Safety Dominance Property by construction..."

All other descriptive references to "reasoning engine" or "rule set" in the body are left unchanged — they are descriptions, not component labels.

---

## Change Set 2: Mechanistic Basis transition sentence

One sentence addition to the Mechanistic Basis section. No subsection content is removed or altered.

### 2a — Transition sentence placement

At the end of the section's opening paragraph (after "...at any of the three points where such self-restraint would have to arise."), append:

> *Although the proposed architecture employs a Symbolic AI Reasoning Engine rather than an LLM, these limitations illustrate a broader principle: AI governance should not depend on the AI component's ability to self-regulate, regardless of the underlying technique.*

**Purpose:** Preempts the reviewer question before they read through the three LLM-specific subsections. Establishes LLM evidence as motivation for a general principle, not as a description of the implementation.

**Narrative effect:** Creates an explicit symbolic AI / statistical AI contrast throughout the paper:
- Statistical AI (LLMs) → used in Mechanistic Basis to motivate external governance
- Symbolic AI (Reasoning Engine) → used in the proposed architecture because its reasoning can be constrained by explicit governance rules

---

## Constraints

- Do not alter Abstract or Conclusion.
- Do not alter formal notation (G(S), A_AI(S), AAI(S), E, S = f(E), Safety Dominance Property, containment expressions).
- Do not alter Table I, II, III or Fig. 1, 2.
- Preserve all citation numbers [1]–[37]; append [38] as the sole new reference.
- Fig. abbreviation style: always "Fig. X", never "Figure X".
- After all edits: invoke the humanizer skill on the four modified prose passages only — the intro sentence (1a), the caption addition (1c), the body sentence (1d), and the transition sentence (2a). The ASCII diagram (1b) is excluded from humanizer.

## New reference to add

Append as [38] at the end of the References section:

> [38] V. Belle, "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning," *Neurosymbolic Artificial Intelligence*, 2025. doi: 10.1177/29498732251339951

Source: `notes/On the Relevance of Logic for Artificial Intelligence, and the Promise of Neurosymbolic Learning.md`

---

## Scope exclusions

The following are explicitly out of scope for this change set:

- Introduction
- Literature Review
- Methodology
- Overall paper structure
- The Conclusion (which correctly summarises the contribution without naming the engine type — leave as-is)

---

## Verification checklist

- [ ] "Symbolic AI Reasoning Engine" appears in: intro sentence before Fig. 3, Fig. 3 diagram, Fig. 3 caption, Domain Instantiation body text
- [ ] "Rule-based engine" label no longer appears in Fig. 3 diagram
- [ ] Mechanistic Basis opening paragraph ends with the transition sentence
- [ ] Citation [38] (Belle, 2025) added to References; numbers [1]–[37] unchanged
- [ ] No changes to Abstract or Conclusion
- [ ] Formal notation unchanged throughout
- [ ] Humanizer applied to the four modified paragraphs
