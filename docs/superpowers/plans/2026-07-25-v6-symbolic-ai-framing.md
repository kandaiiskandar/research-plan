# v6 Symbolic AI Framing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply five targeted edits to `ipsci-2026-paper-v6.md` that resolve two presentation issues — the unlabeled AI component in Fig. 3, and the unexplained LLM/symbolic AI contrast in the Mechanistic Basis section — then run humanizer on the four modified prose passages.

**Architecture:** Six sequential edits to a single file, plus one humanizer pass. Each task is independently verifiable by reading the changed passage. Tasks 1–5 must complete before Task 6 (humanizer) runs.

**Tech Stack:** Plain Markdown editing only.

## Global Constraints

- File to modify: `ipsci-2026-paper-v6.md` only.
- Do not alter: Abstract, Conclusion, formal notation (G(S), A_AI(S), AAI(S), E, S = f(E), Safety Dominance Property), Table I/II/III, Fig. 1/2.
- Citation numbers [1]–[37] must remain unchanged; [38] is the sole new reference.
- Fig. abbreviation style: always "Fig. X" — never "Figure X".
- The humanizer must not alter: formal notation, citation numbers, table content, figure captions and diagrams, the Abstract, Conclusion, and References sections.

---

### Task 1: Add introductory sentence before Fig. 3 (change 1a)

**Files:**
- Modify: `ipsci-2026-paper-v6.md` — Proposed Architecture section, opening paragraph

**What to find:**

The Proposed Architecture section opens with this sentence (currently the very first sentence of the section):

```
The mechanistic evidence above establishes that internal self-restraint cannot be relied upon; the gap requires an external architectural solution.
```

- [ ] **Step 1: Verify the target location**

  Read `ipsci-2026-paper-v6.md` and confirm this exact sentence appears at the start of the `# Proposed Architecture` section. Confirm there is no introductory sentence before it.

- [ ] **Step 2: Insert the new sentence**

  Insert the following sentence immediately before "The mechanistic evidence above establishes...":

  ```
  The proposed architecture employs a Symbolic AI Reasoning Engine, implemented as a knowledge-based expert system within the classical symbolic AI tradition [38], to generate recommendations within the constraints imposed by the participation and advisory-scope gates.
  ```

  The result should be two consecutive sentences at the start of the section:

  ```
  The proposed architecture employs a Symbolic AI Reasoning Engine, implemented as a knowledge-based expert system within the classical symbolic AI tradition [38], to generate recommendations within the constraints imposed by the participation and advisory-scope gates. The mechanistic evidence above establishes that internal self-restraint cannot be relied upon; the gap requires an external architectural solution.
  ```

- [ ] **Step 3: Verify**

  Read the Proposed Architecture opening paragraph. Confirm:
  - The new sentence is the first sentence of the section.
  - `[38]` appears exactly once in the new sentence.
  - No other text in the paragraph has changed.

- [ ] **Step 4: Commit**

  ```bash
  git add ipsci-2026-paper-v6.md
  git commit -m "add: introduce Symbolic AI Reasoning Engine before Fig. 3"
  ```

---

### Task 2: Rename component label in Fig. 3 ASCII diagram (change 1b)

**Files:**
- Modify: `ipsci-2026-paper-v6.md` — Fig. 3 ASCII diagram

**What to find:**

Inside the Fig. 3 code block, locate this box:

```
┌────────▼───────────┐
│  Rule-based engine │
│  (RS(S) supplied   │
│   before inference)│
└────────┬───────────┘
```

- [ ] **Step 1: Verify the target**

  Read the Fig. 3 ASCII diagram and confirm the "Rule-based engine" box exists with this exact text.

- [ ] **Step 2: Replace the box**

  Replace the box with:

  ```
  ┌────────▼───────────────┐
  │  Symbolic AI           │
  │  Reasoning Engine      │
  │  (RS(S) supplied       │
  │   before inference)    │
  └────────┬───────────────┘
  ```

  Note: The box is wider (23 chars interior vs. 19) to accommodate the new label. The connecting lines (│ above, ┌ at top-left, ┘ at bottom-right, ┬ at bottom-center) must remain correctly positioned.

- [ ] **Step 3: Verify**

  Read the updated Fig. 3 diagram. Confirm:
  - "Rule-based engine" no longer appears anywhere in the diagram.
  - "Symbolic AI" and "Reasoning Engine" appear on separate lines inside the box.
  - `(RS(S) supplied` and `before inference)` remain inside the box.
  - The box connects correctly to the `│  AI(E) ⊆ A_AI(S)` box below it.

- [ ] **Step 4: Commit**

  ```bash
  git add ipsci-2026-paper-v6.md
  git commit -m "rename: Rule-based engine → Symbolic AI Reasoning Engine in Fig. 3 diagram"
  ```

---

### Task 3: Extend Fig. 3 caption (change 1c)

**Files:**
- Modify: `ipsci-2026-paper-v6.md` — Fig. 3 caption line

**What to find:**

The Fig. 3 caption currently reads:

```
Fig. 3. The graduated safety-state-gated architecture. Before any inference begins, a deterministic external classifier computes the environmental safety state S = f (E) outside the AI component. Both gates, G(S) and AAI(S), are conditioned on S and together bound what the AI may recommend for the current observation.
```

- [ ] **Step 1: Verify the target**

  Read the Fig. 3 caption and confirm it ends with "...for the current observation." and contains no existing explanatory sentence about the Symbolic AI Reasoning Engine.

- [ ] **Step 2: Append the explanatory sentence**

  Append the following sentence directly after "...for the current observation.":

  ```
  The Symbolic AI Reasoning Engine is a knowledge-based expert system that applies predefined decision rules to generate recommendations within the advisory scope enforced by the governance layer.
  ```

  The full caption should now read:

  ```
  Fig. 3. The graduated safety-state-gated architecture. Before any inference begins, a deterministic external classifier computes the environmental safety state S = f (E) outside the AI component. Both gates, G(S) and AAI(S), are conditioned on S and together bound what the AI may recommend for the current observation. The Symbolic AI Reasoning Engine is a knowledge-based expert system that applies predefined decision rules to generate recommendations within the advisory scope enforced by the governance layer.
  ```

- [ ] **Step 3: Verify**

  Read the updated caption. Confirm:
  - The appended sentence follows immediately after the existing caption with a single space.
  - The caption still begins with "Fig. 3." (not "Figure 3.").
  - No formal notation has been altered.

- [ ] **Step 4: Commit**

  ```bash
  git add ipsci-2026-paper-v6.md
  git commit -m "extend: add Symbolic AI Reasoning Engine explanation to Fig. 3 caption"
  ```

---

### Task 4: Update body text reference in Domain Instantiation (change 1d)

**Files:**
- Modify: `ipsci-2026-paper-v6.md` — Domain Instantiation subsection

**What to find:**

In the Domain Instantiation subsection, locate this sentence:

```
The rule-based reasoning engine enforces the Safety Dominance Property by construction, satisfying the offline-first and computationally lightweight requirements of the low-resource deployment context.
```

- [ ] **Step 1: Verify the target**

  Read the Domain Instantiation subsection and confirm this exact sentence exists.

- [ ] **Step 2: Update the label**

  Replace "The rule-based reasoning engine" with "The Symbolic AI Reasoning Engine":

  ```
  The Symbolic AI Reasoning Engine enforces the Safety Dominance Property by construction, satisfying the offline-first and computationally lightweight requirements of the low-resource deployment context.
  ```

- [ ] **Step 3: Verify**

  Read the Domain Instantiation subsection. Confirm:
  - "The rule-based reasoning engine" no longer appears in this sentence.
  - "The Symbolic AI Reasoning Engine" replaces it with no other changes to the sentence.
  - All other descriptive uses of "reasoning engine" or "rule set" elsewhere in the paper remain unchanged (they are descriptions, not component labels).

- [ ] **Step 4: Commit**

  ```bash
  git add ipsci-2026-paper-v6.md
  git commit -m "update: rename rule-based reasoning engine → Symbolic AI Reasoning Engine in body text"
  ```

---

### Task 5: Add transition sentence in Mechanistic Basis (change 2a) and add reference [38]

**Files:**
- Modify: `ipsci-2026-paper-v6.md` — Mechanistic Basis opening paragraph; References section

**What to find (transition sentence):**

The Mechanistic Basis section opens with a paragraph ending in this sentence:

```
Evidence from the LLM systems and cognition literatures (external to the governance corpus reviewed above) indicates it cannot be relied upon to do so, at any of the three points where such self-restraint would have to arise.
```

**What to find (References):**

The References section ends with:

```
[37] T. Gao, "Mapping the Decision-Making Factors of Small-Scale Fishers: A Case Study of Penang," M.Sc. thesis, International Master of Science in Rural Development, University of Pisa / WorldFish (CGIAR), 2024. [Online]. Available: https://hdl.handle.net/10568/152289
```

- [ ] **Step 1: Verify both targets**

  Read the Mechanistic Basis section opening paragraph and confirm it ends with "...at any of the three points where such self-restraint would have to arise." Read the References section and confirm [37] is the last entry.

- [ ] **Step 2: Append the transition sentence**

  Append the following sentence immediately after "...at any of the three points where such self-restraint would have to arise.":

  ```
  Although the proposed architecture employs a Symbolic AI Reasoning Engine rather than an LLM, these limitations illustrate a broader principle: effective AI governance should not depend on an AI system's ability to self-regulate, regardless of the underlying implementation technique.
  ```

  The closing two sentences of the opening paragraph should now read:

  ```
  Evidence from the LLM systems and cognition literatures (external to the governance corpus reviewed above) indicates it cannot be relied upon to do so, at any of the three points where such self-restraint would have to arise. Although the proposed architecture employs a Symbolic AI Reasoning Engine rather than an LLM, these limitations illustrate a broader principle: effective AI governance should not depend on an AI system's ability to self-regulate, regardless of the underlying implementation technique.
  ```

- [ ] **Step 3: Add reference [38]**

  Append the following entry at the end of the References section, after [37]:

  ```
  [38] V. Belle, "On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning," Neurosymbolic Artificial Intelligence, 2025. doi: 10.1177/29498732251339951
  ```

- [ ] **Step 4: Verify**

  Read the Mechanistic Basis opening paragraph. Confirm:
  - The transition sentence immediately follows "...at any of the three points where such self-restraint would have to arise."
  - The three subsection headings (Fixed inference pipeline, Reasoning dynamics are not risk-adaptive, Self-assessed uncertainty is unreliable and non-learning) are untouched.

  Read the References section. Confirm:
  - [38] appears after [37] with no gap.
  - [37] text is unchanged.
  - No other reference numbers have changed.

- [ ] **Step 5: Commit**

  ```bash
  git add ipsci-2026-paper-v6.md
  git commit -m "add: LLM/symbolic AI framing in Mechanistic Basis; add Belle [38] to References"
  ```

---

### Task 6: Run humanizer on the four modified prose passages

**Files:**
- Modify: `ipsci-2026-paper-v6.md` — four prose passages only (not the diagram, not Abstract/Conclusion/References)

The four passages subject to humanizer:
1. The new introductory sentence (1a) — "The proposed architecture employs a Symbolic AI Reasoning Engine..."
2. The caption addition (1c) — "The Symbolic AI Reasoning Engine is a knowledge-based expert system..."
3. The body sentence update (1d) — "The Symbolic AI Reasoning Engine enforces the Safety Dominance Property..."
4. The transition sentence (2a) — "Although the proposed architecture employs a Symbolic AI Reasoning Engine rather than an LLM..."

- [ ] **Step 1: Invoke the humanizer skill**

  Run `/humanizer` on `ipsci-2026-paper-v6.md`. Use Research Writing Mode. Scope: the four passages listed above only.

- [ ] **Step 2: Confirm off-limits content is untouched**

  After humanizer completes, verify:
  - Formal notation (G(S), A_AI(S), AAI(S), E, S = f(E), Safety Dominance Property, containment expressions) unchanged.
  - Citation numbers unchanged.
  - Table I, II, III and Fig. 1, 2, 3 diagrams unchanged.
  - Abstract, Conclusion, and References unchanged.
  - `[38]` still present in the introductory sentence.

- [ ] **Step 3: Commit**

  ```bash
  git add ipsci-2026-paper-v6.md
  git commit -m "humanize: apply research writing style to four new prose passages"
  ```

---

## Self-Review Checklist

- [ ] Change 1a: introductory sentence with [38] appears as the first sentence of the Proposed Architecture section
- [ ] Change 1b: "Rule-based engine" label gone from Fig. 3 diagram; "Symbolic AI / Reasoning Engine" in its place
- [ ] Change 1c: Fig. 3 caption extended with explanatory sentence
- [ ] Change 1d: "The Symbolic AI Reasoning Engine enforces..." in Domain Instantiation
- [ ] Change 2a: transition sentence at end of Mechanistic Basis opening paragraph
- [ ] Reference [38]: Belle (2025) appended after [37], citations [1]–[37] unchanged
- [ ] Humanizer applied to all four prose passages only
- [ ] No changes to Abstract, Conclusion, or any section not listed above
- [ ] Formal notation unchanged throughout
