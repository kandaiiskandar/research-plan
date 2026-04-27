# Justification: Layer 3 AI advisory component and Safety Dominance enforcement

**Decision:** The Layer 3 AI advisory component is implemented as a rule-based engine. The Safety Dominance Property (AI(E) ⊆ A_AI(S)) is enforced by construction: the rule engine holds a distinct rule set RS(S) per safety state, containing only rules capable of producing recommendation types within A_AI(S).

---

## 1. The three options considered

| Option | Description | Enforcement mechanism | Proof approach | Low-resource suitability |
|---|---|---|---|---|
| **A — Rule-based** | Explicit if-then rules per safety state | Rule set RS(S) excludes non-admissible types by configuration | Proof by construction — RS(S) defines the constraint | Excellent — deterministic, O(1), no GPU |
| **B — ML classifier with constrained output** | Learned model with output head restricted to permitted types | Output layer configured per safety state | Architecture-level enforcement — output space physically restricted | Good — lightweight but requires model inference |
| **C — LLM with output grammar** | Language model constrained by output grammar G_A(S) per state | Grammar intersection with model output distribution at decoding | Formal via grammar containment: A_AI(CAUTION) grammar ⊂ A_AI(SAFE) grammar | Poor — too heavy for low-resource deployment |

---

## 2. Justification for Option A

Option A makes the Safety Dominance Property provable by construction rather than by testing or runtime enforcement. RS(CAUTION) contains no rules that produce DepartureTime or Duration recommendations. The property AI(E) ⊆ A_AI(S) holds not because the engine checks its own output, but because no rule that violates it exists in the active configuration. The constraint is built into the reasoning space before generation begins.

The deployment context reinforces this choice. Coastal fisheries in Terengganu and Penang operate on constrained devices with intermittent connectivity. A rule engine runs in O(1) time with no GPU requirement. Options B and C both require model inference pipelines that are heavier to deploy and less reliable when connectivity drops or power is limited.

AgroNova (Toskov and Toskova 2026) [[notes]](../notes/AgroNova-%20An%20Autonomous%20IoT%20Platform%20for%20Greenhouse%20Climate%20Control.md) implements this pattern in a real deployment. A greenhouse climate controller running on constrained IoT nodes with intermittent connectivity, the system uses edge-based rule-driven logic for all real-time decisions while restricting an LLM to bounded advisory suggestions. Over seven months of operation, the rule layer ran locally without cloud dependency; the LLM was never permitted to execute actuator commands directly. That split maps directly to the Layer 2 and Layer 3 division in this architecture, and the deployment record confirms the approach is viable in exactly the kind of low-resource environment this research targets.

Layer 2 already computes S = f(E) through deterministic threshold comparisons. Option A extends that same computational character into Layer 3, so both layers can be verified using the same methods: static analysis and exhaustive testing of a finite classification function. Options B and C introduce probabilistic inference at Layer 3, opening an assurance gap between what Layer 2 can formally guarantee and what Layer 3 can only empirically demonstrate.

---

## 2a. The specific model: production rule system

Section 2 establishes that Layer 3 is rule-based rather than a learned or generative model. That narrows the design space considerably — but "rule-based" still covers at least five distinct model types. The specific model used in Layer 3 is a **production rule system**: a classical AI architecture in which each rule takes the form `IF <condition> THEN <action>`. The rule engine evaluates each rule in the active rule set against the current environmental input E and fires those whose conditions are satisfied.

This is exactly what RS(S) already describes. Each rule in RS(SAFE) has the form: `IF E satisfies threshold conditions for parameter p THEN produce recommendation type X`, where X ∈ {Go, Delay, DepartureTime, Duration}. RS(CAUTION) contains only rules where X ∈ {Go, Delay}. The engine fires rules — it cannot produce outputs not represented by any rule in the active set. The term "production rule" has a specific meaning in AI: it refers to condition-action rules as used in expert systems (MYCIN, CLIPS, Drools), and is distinct from decision trees, decision tables, and fuzzy systems.

Dalrymple et al. (2024) [[notes]](../notes/Towards%20Guaranteed%20Safe%20AI-%20A%20Framework%20for%20Ensuring%20Robust%20and%20Reliable%20AI%20Systems.md) provide the theoretical foundation for this choice: Guaranteed Safe AI requires that safety constraints be formally specifiable and verifiable before AI output is produced. A production rule system satisfies this directly — every rule is an explicit, readable if-then statement whose action is inspectable without running the engine.

Yang and Zhu (2024) [[notes]](../notes/Industrial%20Expert%20Systems%20Review-%20A%20Comprehensive%20Analysis%20of%20Typical%20Applications.md), reviewing expert system applications across industrial domains including risk assessment, fault diagnosis, and classification, confirm that production rule systems remain the established approach in industrial decision support. Turgunbaev (2025) [[notes]](../notes/Rule-Based%20Reasoning%20and%20Its%20Role%20in%20Intelligent%20Decision%20Making.md) defines rule-based reasoning as the application of predefined IF-THEN rules to derive conclusions, with forward chaining as the standard inference mechanism for data-driven recommendation tasks. The terminology used here (production rule system, inference engine, rule firing) has a settled meaning in the AI literature that distinguishes this model type from decision trees, fuzzy systems, and constraint satisfaction.

### Comparison with alternative rule-based model types

Several rule-based model types could in principle represent RS(S). The table below compares five across seven properties that matter for this architecture.

| Model type | Deterministic output | Statically verifiable | RS(S) per-state configuration | Low-resource fit | Proof by construction | Explicit auditability | Used in safety-critical systems |
|---|---|---|---|---|---|---|---|
| **Production rule system** (chosen) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Decision table | ✓ | ✓ | Partial — rows can be filtered per state but table structure is monolithic | ✓ | ✓ | ✓ | ✓ |
| Decision tree | ✓ | ✓ | ✗ — tree structure is fixed at design time; cannot swap active subtree per safety state | ✓ | Partial | ✓ | ✓ |
| Fuzzy rule system | ✗ — output is a graduated membership value, not a crisp set member | ✗ — formal containment A_AI(CAUTION) ⊂ A_AI(SAFE) requires crisp sets | Partial | ✓ | ✗ | Partial | Limited |
| Constraint satisfaction / logic programming | ✓ | ✓ | ✓ | ✗ — search-based; worst-case runtime unpredictable on constrained devices | Partial | ✗ — solutions are derived, not enumerable by inspection | Limited |

The most important exclusion is fuzzy rules. The Safety Dominance Property AI(E) ⊆ A_AI(S) requires crisp set containment: A_AI(CAUTION) is a set of recommendation types, and AI(E) must be a subset of it. A fuzzy rule system produces graduated membership values — an output degree of 0.7 for "Go" and 0.3 for "DepartureTime" cannot satisfy a binary containment property. Crisp membership is what makes the formal proof in Section 4 work. Fuzzy rules are structurally incompatible with the Safety Dominance Property.

Decision trees fail for a different reason. The RS(S) mechanism requires that the active rule configuration be swapped atomically when S changes — the engine under CAUTION must hold a completely different configuration from the same engine under SAFE. A single fixed decision tree cannot provide this; three separate trees would be needed, each encoding one state's rule set. Three separate trees are equivalent to three separate production rule sets, with no formal advantage and significantly worse readability. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md), surveying AI safety mechanisms across automotive, avionics, railway, and industrial domains, confirm that rule-based approaches used in formal safety guarantees consistently take the form of explicit condition-action specifications rather than tree structures — precisely because the former supports direct inspection and static analysis.

Decision tables are the closest alternative. A decision table could represent RS(S): each row is a condition-action pair, analogous to a production rule. The preference for production rules comes from the input structure. The environmental state vector E has six parameters, each with threshold ranges. The full condition space is combinatorial, and real conditions rarely align with a single parameter in isolation — a CAUTION state may arise from any single parameter, or from several simultaneously. This multi-condition structure is more naturally expressed as independent if-then rules (each rule targets one parameter or combination) than as a flat table with compound condition columns. Klüver et al. (2024) [[notes]](../notes/A%20requirements%20model%20for%20AI%20algorithms%20in%20functional%20safety-critical%20systems%20with%20an%20explainable%20self-enforcing%20network%20from%20a%20developer%20perspective.md), developing requirements models for AI in functional safety-critical systems, identify explicit auditability as a first-order requirement: safety engineers must be able to inspect and trace every constraint. Production rules satisfy this directly; compound-condition decision tables become harder to audit as the condition space grows. The proof by construction is identical for both model types — enumerate all rules/rows and verify none in RS(CAUTION) produce disallowed types — but production rules remain more auditable as the rule set grows.

Constraint satisfaction is eliminated on resource grounds. Katende (2026) [[notes]](../notes/Rethinking%20data-efficient%20artificial%20intelligence%20for%20low-resource%20settings.md) identifies bounded-time inference as a hard requirement for AI systems deployed on constrained devices with intermittent connectivity. A production rule engine with a finite rule set evaluates each rule once against the input — O(n) in the size of the rule set, bounded and predictable. Search-based inference (constraint propagation, backtracking) has unpredictable worst-case runtime on resource-constrained hardware. This cannot be accepted in a system where the governance layer must respond reliably at any time, including when conditions are deteriorating and device resources are under pressure.

### Why production rules satisfy the proof

The proof by construction in Section 4 depends on one property: the ability to enumerate all rules in RS(CAUTION) and verify that none produce DepartureTime or Duration. Production rules are transparent by design — every rule is an explicit, readable if-then statement. Static analysis of RS(CAUTION) is a finite check over a bounded rule set. This is what makes the proof architectural rather than empirical: you do not test the engine's behaviour; you inspect the rules.

Newcomb and Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md), reviewing 46 formal methods studies for safety-critical machine learning, confirm that enforceability requires constraints built into the reasoning structure, not applied post-hoc. A production rule system satisfies this at the model level: the constraint is the rule set itself. Castagnone and Nitti (2026) [[notes]](../notes/A%20Neuro-Symbolic%20Framework%20for%20Ensuring%20Deterministic%20Reliability%20in%20AI-Assisted%20Structural%20Engineering-%20The%20SYNAPSE%20Architecture.md) make the parallel argument in their SYNAPSE architecture — a deterministic rule layer governs all safety-critical structural calculations, while a neural component handles natural language and presentation. Their design principle is that determinism is not a property you verify at runtime; it is a property you build in by choosing a model type whose outputs are fully determined by explicit, inspectable rules. Layer 3 follows the same principle. The production rule system is not chosen because it performs well under evaluation. It is chosen because its outputs are structurally determined by its rule set, and that rule set is under the designer's direct control.

> **Viva note — likely question:** *"What kind of rule-based model does Layer 3 use, and why not a decision tree or fuzzy system?"*
>
> "Layer 3 uses a production rule system — each rule takes the form *if these conditions hold, then produce this recommendation type*. The governance layer supplies a specific rule set to the engine before it reasons: RS(SAFE), RS(CAUTION), or RS(UNSAFE). The engine fires only the rules in its active set.
>
> Fuzzy rules are immediately out because they produce graduated membership values, not crisp set members. The Safety Dominance Property requires AI(E) ⊆ A_AI(S) — a crisp set containment. You cannot have a subset relationship over a probability distribution.
>
> Decision trees fail for a different reason. RS(S) needs to be swapped atomically when the safety state changes — the engine under CAUTION must have a completely different configuration than under SAFE. A single fixed decision tree cannot provide this; you would need three separate trees, one per state, which is just three production rule sets with worse readability and no formal advantage.
>
> Decision tables are the closest alternative. The reason I went with production rules is the input structure — six environmental parameters, each with threshold ranges, and conditions that can arise from any single parameter or from combinations. That is more naturally expressed as independent if-then rules than as a flat table with compound condition columns, which grows harder to audit as the rule set expands.
>
> The deeper reason is the proof. I enumerate every rule in RS(CAUTION) and verify that none produce DepartureTime or Duration. That is only possible because every rule is an explicit, inspectable statement. You are not testing the engine's behaviour — you are reading the rules. That is what makes the guarantee architectural rather than empirical."

---

## 3. The enforcement mechanism

The governance layer (Layer 2) configures Layer 3 before reasoning begins. Given S = f(E):

- If G(S) = 0, Layer 3 receives no input and produces no output. AI(E) = ∅.
- If G(S) = 1, Layer 3 receives E and the rule set RS(S):

```
RS(SAFE)    = rules producing recommendations in {Go, Delay, DepartureTime, Duration}
RS(CAUTION) = rules producing recommendations in {Go, Delay}
RS(UNSAFE)  = ∅  (never passed — G(UNSAFE) = 0)
```

The rule engine fires only rules present in RS(S). Since RS(CAUTION) contains no rules for DepartureTime or Duration, those types cannot appear in AI(E) when S = CAUTION. Their absence is not the result of checking and rejecting outputs after the fact — no rule that generates those types exists in the active configuration. There is nothing to filter.

This is what the architecture description means when it states that recommendations are restricted "structurally — before the AI reasons, not filtered after the fact."

---

## 4. Proof of the Safety Dominance Property

**Claim:** For all E, AI(E) ⊆ A_AI(f(E)).

**Proof by construction.** Let S = f(E) for arbitrary E.

**Case 1: S = UNSAFE.**
G(UNSAFE) = 0. Layer 3 receives no input. AI(E) = ∅. Since A_AI(UNSAFE) = ∅, the containment holds trivially. ∎

**Case 2: S = CAUTION.**
G(CAUTION) = 1. Layer 3 receives E and RS(CAUTION). RS(CAUTION) contains only rules producing recommendations in {Go, Delay}. The rule engine can produce only types present in its active rule set. Therefore AI(E) ⊆ {Go, Delay} = A_AI(CAUTION). ∎

**Case 3: S = SAFE.**
G(SAFE) = 1. Layer 3 receives E and RS(SAFE). RS(SAFE) contains only rules producing recommendations in {Go, Delay, DepartureTime, Duration}. Therefore AI(E) ⊆ {Go, Delay, DepartureTime, Duration} = A_AI(SAFE). ∎

The property holds in all three cases. The proof requires no runtime checking, no output filtering, and no reasoning about probabilistic AI behaviour. It depends only on the definition of RS(S), which is fully under the designer's control.

At the viva, the likely question is: "How do you guarantee AI(E) ⊆ A_AI(S) in your implementation?" The answer: the rule engine in CAUTION mode holds only rules that produce {Go, Delay}. No other recommendation type can appear because no rule that generates it exists in the active configuration. The guarantee is architectural, not behavioural.

---

## 5. What this means for the architecture description

Layer 3 in `architecture-illustration.md` was previously described as a "probabilistic / learned component." Layer 3 is a rule-based engine whose active rule set RS(S) is supplied by the governance layer before any reasoning occurs. The formal pipeline is unchanged:

```
E → S = f(E) → (G(S), A_AI(S)) → AI(E) → Human Decision
```

The difference is in how AI(E) is generated: by a rule engine configured with RS(S), not by a probabilistic model. The Safety Dominance Property follows from the rule set definition.

---

## 6. Limitations of the rule-based choice

Option A gives a clean proof but narrows the advisory component's expressiveness.

A rule engine handles threshold-based, categorical, and logical combinations of environmental parameters well. What it cannot do, without explicit encoding, is capture non-linear interactions or patterns learned from historical catch data. For the departure decision problem in its current scope — directional guidance and threshold-based timing — this is sufficient. If future work extends R to include recommendation types that require learned generalisation (fishing area selection, species-specific guidance), a hybrid design with a constrained ML output layer would need to be considered. That extension would require a separate enforcement argument, since a constrained ML layer cannot rely on the construction proof above.

The rule sets also require ongoing maintenance. As R expands or threshold values are recalibrated, RS(S) must be updated across all three safety states in a way that preserves A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅. This is a design responsibility, not an architectural defect, but it should be documented explicitly.

The closest deployed analogue, AgroNova (Toskov and Toskova 2026) [[notes]](../notes/AgroNova-%20An%20Autonomous%20IoT%20Platform%20for%20Greenhouse%20Climate%20Control.md), illustrates the same trade-off: over seven months of operation, deterministic rule control proved viable in low-resource conditions, but the system defines no formal governance model for its rule layer. Formalising that structure is the gap this architecture fills.
