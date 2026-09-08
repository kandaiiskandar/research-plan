# Implementation Plan: Layer 3 Rule-Based Model Type — New Section 2a

**Target file:** `docs/justification-layer3-enforcement.md`  
**Purpose:** Add a new Section 2a that names the specific rule-based model used in Layer 3, provides a comparison table against alternative rule-based model types, and adds citations supporting the choice.

---

## Context

`docs/justification-layer3-enforcement.md` currently justifies *why* Layer 3 is rule-based (over ML or LLM) in Section 2, but does not specify *which kind* of rule-based model is used. A PhD examiner who accepts "rule-based" will immediately ask: "What kind? Decision table? Decision tree? Fuzzy rules? Production rules? Why that one and not the others?" This section closes that gap.

The document's current Section 2 ends with a justification for Option A (rule-based). The new Section 2a goes immediately after the current Section 2 and before the current Section 3 ("The enforcement mechanism").

---

## What to write: Section 2a

**Section heading:**

```
## 2a. The specific model: production rule system
```

---

### Part 1 — Name and define the model

Write a paragraph that:

1. Names the specific model as a **production rule system** — a classical AI architecture in which each rule takes the form `IF <condition> THEN <action>`. The rule engine evaluates each rule in the active rule set against the current input and fires those whose conditions are satisfied.

2. Explains that this is exactly what RS(S) already describes. Each rule in RS(SAFE) has the form: `IF E satisfies threshold conditions for parameter p THEN produce recommendation type X ∈ {Go, Delay, DepartureTime, Duration}`. RS(CAUTION) contains only rules where X ∈ {Go, Delay}. The engine fires rules; it cannot produce outputs not represented by any rule in the active set.

3. States that the term "production rule" has a specific meaning in AI: it refers to condition-action rules as used in expert systems (e.g., MYCIN, CLIPS, Drools), distinct from decision trees, decision tables, and fuzzy systems.

---

### Part 2 — Comparison table

Write a paragraph introducing the comparison, then insert this table comparing five rule-based model types across seven properties relevant to this architecture:

| Model type | Deterministic output | Statically verifiable | RS(S) per-state configuration | Low-resource fit | Proof by construction | Explicit auditability | Used in safety-critical systems |
|---|---|---|---|---|---|---|---|
| **Production rule system** (chosen) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Decision table | ✓ | ✓ | Partial — table is fixed; rows can be filtered per state but structure is monolithic | ✓ | ✓ | ✓ | ✓ |
| Decision tree | ✓ | ✓ | ✗ — tree structure is fixed at design time; cannot swap active subtree per safety state | ✓ | Partial | ✓ | ✓ |
| Fuzzy rule system | ✗ — output is a graduated membership value | ✗ — formal containment A_AI(CAUTION) ⊂ A_AI(SAFE) requires crisp set membership | Partial | ✓ | ✗ | Partial | Limited |
| Constraint satisfaction (logic programming) | ✓ | ✓ | ✓ | ✗ — search-based; runtime unpredictable on constrained devices | Partial | ✗ — solutions are derived, not enumerable by inspection | Limited |

After the table, write a short paragraph explaining the key discriminators:

- **Fuzzy rules are eliminated** because the Safety Dominance Property AI(E) ⊆ A_AI(S) requires crisp set containment. A fuzzy output degree of 0.7 for "Go" and 0.3 for "DepartureTime" cannot satisfy a binary containment property — A_AI(S) is a set, not a distribution.
- **Decision trees are eliminated** because the tree structure is fixed at design time. RS(S) requires that the active rule set be swapped atomically when S changes — the engine operating under CAUTION must have a completely different configuration from SAFE. A single fixed tree cannot provide this; you would need three separate trees, which is equivalent to three separate production rule sets with worse readability and no formal advantage.
- **Decision tables are the closest alternative.** A decision table could represent RS(S) — each row is a condition-action pair. The reason production rules are preferred: multi-condition environmental inputs (six parameters, each with threshold ranges) produce a combinatorial condition space that is more naturally expressed as independent condition-action rules than as a flat table with compound condition columns. The proof by construction is identical for both — enumerate all rows/rules and verify none in RS(CAUTION) produce disallowed types.
- **Constraint satisfaction is eliminated** on low-resource grounds. Search-based inference has unpredictable worst-case runtime on resource-constrained devices. The architecture requires O(1) or bounded-time inference (consistent with Layer 2's threshold classification). A rule engine with a finite rule set evaluates each rule once — bounded and predictable.

---

### Part 3 — Why production rules satisfy the proof

Write a short paragraph explaining:

The proof by construction in Section 4 depends on one property: the ability to enumerate all rules in RS(CAUTION) and verify that none produce DepartureTime or Duration. Production rule systems are transparent by design — every rule is an explicit, readable if-then statement. Static analysis of RS(CAUTION) is a finite check over a bounded rule set. This is what makes the proof architectural rather than empirical: you do not test the engine; you inspect the rules. Castagnone & Nitti (2026) [[notes]](../../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) make the same argument for their deterministic rule layer in SYNAPSE — determinism is not a property you verify at runtime; it is a property you build in by choosing a model type whose outputs are fully determined by explicit, inspectable rules.

---

## Citations to include

All citations must follow the project's `[[notes]]` link format as defined in `CLAUDE.md`. Use the quick links below exactly as written.

### From the existing corpus (use these):

| Paper | Where to cite | Quick link |
|---|---|---|
| Dalrymple et al. (2024) | Part 1 or Part 3 — theoretical basis for why verifiable safety requires formally specifiable constraints | `[[notes]](../../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md)` |
| Newcomb & Ochoa (2026) | Part 3 — formal methods SLR confirms that enforceability requires constraints built into reasoning structure, not applied post-hoc | `[[notes]](../../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)` |
| Castagnone & Nitti (2026) | Part 3 — SYNAPSE uses a deterministic rule layer for structural safety; parallel to this architecture's Layer 3 | `[[notes]](../../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md)` |
| Klüver et al. (2024) | Part 2 or Part 3 — requirements model for AI in functional safety-critical systems; discusses auditability of rule-based components | `[[notes]](../../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md)` |
| Perez-Cerrolaza et al. (2024) | Part 2 — survey of AI in safety-critical systems; confirms rule-based systems are the established choice for formal safety guarantees in safety-critical domains | `[[notes]](../../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)` |
| Katende (2026) | Part 2 (low-resource column) — data-efficient AI for low-resource settings; supports the low-resource fit argument | `[[notes]](../../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md)` |

### New papers to add to the corpus (flag as needed):

The corpus does not currently contain a foundational paper on production rule systems or expert system architectures. The agent writing this section should flag this gap explicitly in a comment or note within the document — do not fabricate a citation. Suggested papers to find and add:

1. A paper on **production rule systems or expert systems in safety-critical domains** — e.g., clinical decision support (MYCIN lineage), aviation rule engines, or process control expert systems. This would anchor the claim that production rules are the established model type for formal safety guarantees.
2. A paper distinguishing production rules from decision tables and decision trees in the context of formal verification — this strengthens the comparison table.

If these cannot be found and added during the same session, add a `> **Citation needed:**` note in the relevant paragraph as a placeholder.

---

## Insertion point

Insert the new Section 2a **between** the current Section 2 and the current Section 3. The current Section 2 ends with:

```
Options B and C both require model inference pipelines that are heavier to deploy and less reliable when connectivity drops or power is limited.

Layer 2 already computes S = f(E) through deterministic threshold comparisons. Option A extends that same computational character into Layer 3, so both layers can be verified using the same methods: static analysis and exhaustive testing of a finite classification function. Options B and C introduce probabilistic inference at Layer 3, opening an assurance gap between what Layer 2 can formally guarantee and what Layer 3 can only empirically demonstrate.
```

The current Section 3 begins with:

```
## 3. The enforcement mechanism
```

The new Section 2a goes between these two blocks.

---

## Consistency checks after writing

1. All `[[notes]]` links must use the exact paths from `docs/citation-notes-map.md` — do not reconstruct paths from memory.
2. Do not redefine any formal variables (E, S, G(S), A_AI(S), RS(S)) — use them as defined in `docs/appendix-c-formalisation.md`.
3. Do not introduce socio-technical framing — this section is a pure CS architecture justification.
4. Section numbers after 2a must remain unchanged (Section 3, 4, 5, 6 stay as they are).
5. The term "production rule system" must be used consistently throughout — not "expert system", "rule engine", or "if-then system" alone (these can appear as synonyms in parentheses but "production rule system" is the primary term).

---

## File locations (for the agent)

- **Target file to edit:** `/Users/iskandar/Documents/my_stuff/research-test-2/docs/justification-layer3-enforcement.md`
- **Citation map:** `/Users/iskandar/Documents/my_stuff/research-test-2/docs/citation-notes-map.md`
- **Formal definitions:** `/Users/iskandar/Documents/my_stuff/research-test-2/docs/appendix-c-formalisation.md`
- **CLAUDE.md (project rules):** `/Users/iskandar/Documents/my_stuff/research-test-2/CLAUDE.md`
