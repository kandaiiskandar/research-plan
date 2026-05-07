# Extraction Prompt: Production Rule Systems in Safety-Critical Systems
*Targeted extraction for Section 2a of `docs/justification-layer3-enforcement.md`*

---

## Context for the Extractor

This PhD research designs a graduated AI governance architecture for safety-critical decision support in low-resource coastal fisheries. The AI advisory component (Layer 3) is implemented as a **production rule system** — a classical AI architecture where each rule takes the form `IF <condition> THEN <action>`. The rule engine holds a distinct rule set per safety state (RS(SAFE), RS(CAUTION)), and fires only rules present in the active set.

The formal Safety Dominance Property states: for all environmental inputs E, AI(E) ⊆ A_AI(S) — the AI can only produce recommendations within the admissible set defined by the current safety state. This property is proved by construction: RS(CAUTION) contains no rules that generate inadmissible recommendation types, so they cannot appear in the output.

The thesis chapter needs a citation that grounds the claim that production rule systems are an established model type for safety-critical advisory components — one that specifically justifies why production rules (rather than decision trees, decision tables, or fuzzy rules) are the appropriate choice when formal verifiability and explicit auditability are required.

---

## What to Extract

### 1. Paper Identity
- Full title, authors, year, publication venue
- Type: empirical, design, review, case study, system description

---

### 2. Production Rule System — Definition and Architecture
- How does the paper define a production rule system? Quote the definition if available.
- What is the condition-action (IF-THEN) structure? How are rules organised and evaluated?
- Does the paper use the term "production rule system", "production rule", "expert system", "rule engine", or related terms? List all terms used.
- What inference mechanism is described (forward chaining, backward chaining, conflict resolution)?
- Is the rule set static or configurable at runtime? Can different rule sets be loaded for different operating states?

---

### 3. Safety-Critical Application
- In what safety-critical domain is the production rule system applied? (aviation, clinical, maritime, industrial process control, etc.)
- What safety guarantees does the paper claim the rule-based approach provides?
- Does the paper explicitly argue that rule-based approaches are *preferable* to learned or probabilistic models for safety-critical applications? If so, quote the argument.
- Does the paper discuss the relationship between rule structure and formal safety guarantees?

---

### 4. Formal Verifiability and Proof Properties
- Does the paper claim that a production rule system enables **static verification** — checking rule sets without running the engine?
- Does the paper discuss **proof by construction** or **proof by inspection** — the ability to verify a safety property by enumerating and inspecting rules rather than testing runtime behaviour?
- Does the paper state that the rule set itself *is* the safety constraint (not a post-hoc filter applied to outputs)?
- Does the paper compare rule-based verifiability against probabilistic or learned models? Quote directly if possible.

---

### 5. Comparison Against Alternative Rule-Based Models
Does the paper compare production rule systems against any of the following? For each, note what the paper says:

| Model type | Does the paper discuss it? | What does it say? |
|---|---|---|
| Decision table | | |
| Decision tree | | |
| Fuzzy rule system | | |
| Constraint satisfaction / logic programming | | |
| Neural network / ML model | | |

- Does the paper argue that production rules are preferred over decision trees or tables for formal verification? Quote if available.
- Does the paper identify any structural property of production rules (e.g., modularity, atomic condition-action pairs, per-state configurability) as an advantage for safety-critical use?

---

### 6. Auditability and Explainability
- Does the paper argue that production rules support **explicit auditability** — the ability for safety engineers to inspect and trace every constraint?
- Does the paper frame rule transparency as a safety requirement, not just a design preference?
- Is there any discussion of how rule-based transparency compares to the opacity of ML or probabilistic models?

---

### 7. Low-Resource or Resource-Constrained Deployment
- Does the paper discuss deployment on constrained hardware or in low-resource environments?
- Is bounded-time or O(n) inference mentioned as a property of rule-based evaluation?
- Does the paper contrast rule evaluation performance with heavier inference methods (ML inference, search-based reasoning)?

---

### 8. Quotable Claims for Section 2a
List 3–5 specific sentences or short passages from the paper that could be directly cited to support one of these claims:

1. Production rule systems are the established model type for safety-critical advisory components.
2. Rule set inspection enables proof by construction — a formal guarantee that safety constraints hold.
3. Production rules are preferred over decision trees or tables when formal verifiability is required.
4. Rule-based approaches support explicit auditability as a first-order safety requirement.
5. Fuzzy rule systems are incompatible with crisp safety constraints.

For each quotable passage, note the section or page number.

---

### 9. Positioning for Section 2a
In 2–3 sentences: how does this paper support the argument that a production rule system is the appropriate model type for Layer 3? What specific claim in Section 2a does it anchor?

---

### 10. Citation Format
Provide the full citation in this format:
```
Author(s) (Year). Title. Journal/Conference, Volume(Issue), Pages. DOI if available.
```

And the short citation key used in this thesis (e.g., `Smith et al. (2023)`).

---

*Note: If the paper only partially addresses these questions, extract what is available and flag gaps. The most important sections are 3, 4, and 8 — the safety-critical application, formal verifiability claims, and quotable passages.*
