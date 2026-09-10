# Task — Journal 1 Evaluation Specification Alignment

## Role

Act as an **independent experimental-design and formal-consistency reviewer** for Journal 1.

The following decisions are already established and MUST NOT be reopened in this task:

```text
Canonical Repository Drift Synchronisation — CLOSED
Journal 1 Canonical Consistency Synchronisation — CLOSED
Journal 1 Evaluation Baseline Decision — OPTION C accepted
```

This task converts that accepted design decision into the **final evaluation specification** that Journal 1 will use before experiments, result tables, figures, or implementation benchmarking are created.

Create and work on:

```text
design/journal1-evaluation-specification
```

Suggested final commit:

```text
design: align Journal 1 hypotheses and evaluation conditions
```

This is primarily a **research-design specification task**.

Do not run new experiments.

Do not modify canonical empirical results.

Do not reopen canonical architecture decisions.

---

# 1. Accepted evaluation design

The accepted design is:

## Primary experimental comparison

```text
C0 — Ungated
C1 — Binary-gated
C2 — Proposed graduated advisory-scope architecture
```

## Structural comparator

```text
C3 — Flehmig-style traffic-light governance topology
```

C3 is NOT a fourth experimental arm.

C3 exists as a **structural proposition / comparator** addressing the novelty objection.

Canonical mapping:

```text
C0:
full advisory scope at every state

C1:
FULL at SAFE
FULL at CAUTION
EMPTY at UNSAFE

C2:
FULL at SAFE
{Go, Delay} at CAUTION
EMPTY at UNSAFE

C3:
FULL at green / SAFE-equivalent
FULL at orange / CAUTION-equivalent
EMPTY at red / UNSAFE-equivalent
```

Therefore at the admissible-set level:

```text
C1 ≡ C3
```

and canonical executable confirmation gives:

```text
C1 ↔ C3 = 0.00%
```

Do NOT present that 0.00% as an uncertain empirical discovery.

---

# 2. Main objective

Produce a final, internally coherent Journal 1 evaluation specification covering:

```text
condition definitions
condition labels
research questions
hypotheses
formal propositions
metrics
ablation logic
experimental scope
statistical treatment
implementation-fidelity checks
reporting boundaries
```

The specification must distinguish:

```text
what is proved
what is deterministic
what is descriptively measured
what requires empirical implementation
what requires human validation
```

---

# 3. Freeze protected canonical state

Before editing verify:

```text
Appendix C:
abee8715e842e0d9

Conference manuscript:
27b33b846ae327cb
```

Protect:

```text
prediction register
solar artefact
canonical classifier scripts
canonical_figures.py
condition_comparison.py semantics
raw datasets
canonical empirical outputs
```

Expected canonical empirical state includes:

```text
Level 2:
5.81% / 4.48%

C0↔C1:
42.88%

C0↔C2:
48.69%

C1↔C3:
0.00%

wind:
21.6 kn
2 activations
0 bindings

prediction register:
24
15 CONFIRMED
9 REFUTED
```

No protected scientific state should move.

---

# 4. Freeze the Option C decision

Read:

```text
evaluation-baseline-decision.md
```

Treat the following as accepted:

```text
OPTION C
```

Specifically:

```text
Primary experiment:
C0 / C1 / C2

Structural proposition:
C1 ≡ C3 at admissible-set level
```

Do not reconsider Option A or Option B unless you discover a direct logical contradiction in the accepted decision.

If such a contradiction exists:

```text
JOURNAL1 EVALUATION SPECIFICATION OPEN — ACCEPTED BASELINE DECISION CONFLICT
```

Otherwise proceed.

---

# 5. Correct two wording issues in the decision record

Before using the baseline decision as authority, repair these two bounded wording issues.

## 5.1 Retrospective dataset scope

Do NOT say:

```text
complete population
```

without qualification.

Preferred formulation:

```text
The replay is a deterministic census of all hourly
records in the predefined retrospective study window,
not a random sample from a broader climatological
population.
```

This means values such as:

```text
5.81%
4.48%
0.00%
```

are exact descriptive values for the analysed trace/configuration.

They are not estimates of all future Sabah operating conditions.

---

## 5.2 Layer 3 does not automatically make H1/H2 empirical

Correct any wording equivalent to:

```text
If Layer 3 is implemented,
H1/H2 likely become genuinely empirical.
```

More precise:

```text
Layer 3 implementation makes compliance and violation
rates implementation-fidelity measurements.

It does not convert a formal governance invariant
into a behavioural hypothesis.
```

Safety Dominance remains:

```text
AI(E) ⊆ A_AI(f(E))
```

under the stated engine assumptions.

An implementation test checks whether the implementation conforms to that specification.

It does not empirically rediscover the theorem.

---

# 6. Condition-label normalisation

The Journal 1 labels currently diverge from the canonical harness.

Migrate maintained Journal 1 design artefacts from:

```text
Journal C1 = Ungated
Journal C2 = Binary
Journal C3 = Proposed
```

to:

```text
C0 = Ungated
C1 = Binary-gated
C2 = Proposed graduated architecture
C3 = Flehmig-style structural comparator
```

This is the last low-cost point to normalise notation because no Journal 1 results, result tables, figures, or scripts have yet been generated under the old labels.

---

# 7. Migration scope

Audit the entire maintained Journal 1 tree for:

```text
C1
C2
C3
condition
baseline
ungated
binary
graduated
proposed
H1
H2
H3
H4
ablation
```

Do NOT blindly replace tokens.

For every occurrence determine what the symbol means.

Classify:

```text
OLD-J1-LABEL
CANONICAL-LABEL
HISTORICAL
AMBIGUOUS
IRRELEVANT
```

Pay particular attention to:

```text
research-design.md
active manuscript
Section 10 plan
Section 11 plan
Section 12 ablation
H1–H4
tables
captions
planned figures
internal cross-references
```

Historical/superseded section plans may remain historical if clearly marked.

---

# 8. Retire the translation table

Once maintained Journal 1 notation uses canonical labels directly, the temporary mapping:

```text
canonical C0 → Journal C1
canonical C1 → Journal C2
canonical C2 → Journal C3
```

must no longer be needed in active prose.

Do not simply delete the history without explanation.

Replace with a concise provenance note if needed:

```text
Journal 1 previously used C1/C2/C3 for
Ungated/Binary/Proposed. The design was normalised
before experiments to the canonical C0/C1/C2 notation.
```

No active result should require manual label translation after closure.

---

# 9. Formalise the Flehmig structural proposition

Create a formal proposition, not an experimental hypothesis.

Suggested structure:

```text
Proposition J1-P1
At the admissible-recommendation-set level,
the binary participation gate C1 and the
Flehmig-style governance topology C3
are output-equivalent under the comparison mapping.
```

Proof should be one-line / finite mapping comparison:

```text
A_C1(SAFE)    = FULL
A_C1(CAUTION) = FULL
A_C1(UNSAFE)  = ∅

A_C3(SAFE)    = FULL
A_C3(CAUTION) = FULL
A_C3(UNSAFE)  = ∅

Therefore:
A_C1(S) = A_C3(S)
for all S.
```

Do not overcomplicate this.

---

# 10. Flehmig fairness qualification

The proposition MUST travel with the qualification that:

Flehmig-style governance is conditioned originally on:

```text
AI degradation
drift
outliers
performance decay
```

The current comparison ports the **governance topology** to a shared state axis solely to compare admissible-output structure.

Do not claim:

```text
Flehmig's actual system was reproduced
Flehmig's architecture was empirically tested
Flehmig is deficient
its orange state is useless
```

Correct framing:

```text
the comparison isolates governance topology
at the admissible-set output level
```

---

# 11. Three levels of C1/C3 evidence

The specification must explicitly separate:

## Analytical

```text
C1 ≡ C3
```

from the mapping definition.

## Executable

The implemented harness preserves the mapping.

## Trace confirmation

```text
C1 ↔ C3 = 0.00%
```

over the retrospective replay.

State explicitly:

```text
The 0.00% replay value is confirmation of
implementation consistency, not discovery of
an uncertain physical phenomenon.
```

---

# 12. Audit RQ-J1–RQ-J4

Read the current Journal 1 research questions.

For each produce:

```text
current wording
construct being measured
evidence type
condition(s)
metric(s)
whether wording remains valid
required change
```

Evidence type must be one of:

```text
FORMAL
DETERMINISTIC
IMPLEMENTATION-FIDELITY
EMPIRICAL-TRACE
PERFORMANCE
HUMAN-EVALUATION
```

Do not allow one RQ to silently mix these without stating it.

---

# 13. H1 redesign

Current H1 concerns:

```text
higher advisory scope compliance
```

This is problematic because the proposed architecture's compliance is constrained by Safety Dominance.

Determine the correct status.

Preferred outcome:

```text
H1 should NOT remain a behavioural comparative hypothesis
if its result follows from the specification.
```

Evaluate whether it should become:

```text
implementation-fidelity criterion
```

such as:

```text
F1 — The implementation produces no recommendation type
outside A_AI(S) across the exhaustive test suite / replay.
```

Do not call this evidence that the architecture gives better advice.

It tests specification conformance.

---

# 14. H2 redesign

Current H2 concerns:

```text
false positive recommendations outside A_AI(S)
```

This has the same circularity.

Under a conforming implementation:

```text
expected violations = 0
```

because this is what Safety Dominance specifies.

Reclassify H2 as:

```text
implementation-fidelity / invariant check
```

unless a genuinely uncertain construct exists.

Do not merely rename H2 while preserving the same logical problem.

---

# 15. H3 — governance latency

H3 is genuinely empirical:

```text
governance overhead < [X ms]
```

However `[X ms]` is currently unsupported.

Do NOT invent a threshold.

Determine whether H3 should temporarily become:

```text
RQ / descriptive performance metric
```

until an externally justified acceptance threshold exists.

Possible form:

```text
What runtime latency and computational overhead
does Layer 2 introduce on the target deployment hardware?
```

If a threshold is required for hypothesis form and no evidence currently supports one:

```text
H3 threshold = OPEN
```

Do not guess.

---

# 16. H4 — Level 2 contribution

H4 is currently the strongest genuine architectural comparison.

Preserve the principle:

```text
Removing advisory-scope restriction
reduces C2 toward C1 behaviour.
```

Formalise the metric.

Canonical isolated Level 2 contribution:

```text
Δ_L2 =
divergence(C0,C2)
-
divergence(C0,C1)
```

Current canonical:

```text
PRIMARY:
48.69 - 42.88 = 5.81%

RESOLUTION:
corresponding isolated contribution = 4.48%
```

Check whether H4 wording accurately corresponds to this metric.

If necessary, rewrite H4 so that it tests an uncertain/dataset-dependent quantity rather than merely restating a definition.

---

# 17. Candidate final evidence structure

Assess whether Journal 1 should ultimately use something like:

```text
FORMAL PROPOSITIONS
P1 Totality
P2 Monotonicity
P3 Safety Dominance
P4 C1/C3 admissible-set equivalence

IMPLEMENTATION-FIDELITY CHECKS
F1 no output outside A_AI(S)
F2 gate produces no output under UNSAFE
F3 rule-set implementation matches configured mapping

EMPIRICAL / TRACE RESULTS
E1 pairwise divergence C0/C1/C2
E2 isolated Level 2 contribution
E3 resolution sensitivity
E4 transitions / hysteresis characterisation

PERFORMANCE
E5 runtime latency / resource cost

HUMAN / FUTURE VALIDATION
advisory utility
trust
decision quality
real-world safety outcomes
```

Do not adopt this structure automatically.

Evaluate it against existing RQs and journal narrative.

---

# 18. Metrics audit

Current metrics:

```text
advisory scope compliance
false positive rate
decision-support utility
governance overhead
```

Canonical metrics:

```text
pairwise admissible-set divergence
isolated Level 2 contribution
```

For every metric classify:

```text
FORMAL
FIDELITY
DESCRIPTIVE
PERFORMANCE
HUMAN-OUTCOME
```

Determine whether it:

```text
answers an RQ
supports a hypothesis
duplicates a theorem
requires Layer 3
requires user data
requires incident/outcome data
```

Delete/reclassify metrics that answer no research question.

---

# 19. Decision-support utility

This metric requires special scrutiny.

Do not assume it can be measured from replay alone.

Ask:

```text
What is utility?
```

Possible meanings might require:

```text
ground-truth recommendation correctness
fisher preference
decision quality
actionability
task completion
real-world outcome
```

If none is operationally defined in current design:

mark:

```text
OPEN — CONSTRUCT DEFINITION REQUIRED
```

Do not invent a utility formula.

Determine whether this belongs in:

```text
RQ4 replay
```

or later:

```text
RQ5 socio-technical/user study
```

---

# 20. Statistical treatment

Correct the population wording.

Use:

```text
The historical replay is a deterministic census
of all hourly observations within the predefined
retrospective study window.
```

Do NOT generalise that to all future weather.

For deterministic replay metrics:

```text
pairwise divergence
binding rate
component shares
transition counts
```

report exact descriptive values for the analysed trace.

Do not automatically apply:

```text
p-values
confidence intervals
significance testing
```

to deterministic full-window enumeration.

---

# 21. Sensitivity versus uncertainty

Preserve:

```text
PRIMARY = 5-year ERA5-Ocean
RESOLUTION = 3.25-year MFWAM
```

Their difference is a:

```text
resolution-sensitivity result
```

not a confidence interval.

Do not call:

```text
5.81 ± something
```

unless a separate statistical model actually justifies it.

---

# 22. Implementation fidelity

Define clearly what must later be tested once Layer 3 exists.

At minimum consider:

```text
RS(SAFE) produces only FULL-set types
RS(CAUTION) produces only {Go, Delay}
UNSAFE produces no advisory output
classification state received by Layer 3 matches Layer 2
rule-set switching follows state transitions correctly
no stale rule-set persists across transition
```

These are implementation tests.

They are not new proofs of Safety Dominance.

---

# 23. Layer 3 status

Current state:

```text
Layer 3 specified
not fully implemented
```

Therefore distinguish:

```text
formal architecture evidence
```

from:

```text
prototype fidelity evidence
```

Do not write future-tense planned implementation as completed experimental evidence.

---

# 24. Evaluation design table

Create a final master table with columns:

```text
ID
question_or_claim
evidence_type
conditions
metric
current_status
expected_source
analytical_or_empirical
requires_layer3
requires_humans
reporting_boundary
```

This table should become the single source of truth for Journal 1 evaluation.

---

# 25. Hypothesis naming

Do not force every claim into `H1/H2/H3/H4`.

Use appropriate types:

```text
Theorem
Proposition
Invariant
Fidelity criterion
Research question
Empirical hypothesis
Performance criterion
```

A formal proposition should not be called an empirical hypothesis merely for stylistic symmetry.

---

# 26. Preserve novelty framing

Current novelty:

```text
graduated governance exists;
graduated advisory-scope governance is the gap
```

Option C should support this through:

```text
literature comparison
+
structural proposition
+
primary C0/C1/C2 evaluation
```

Do not claim that the experiment independently validates the entire literature-derived novelty statement.

---

# 27. Keep domain-transfer boundary

Preserve:

```text
structural re-instantiability
≠
empirical portability
```

No evaluation metric in this task should be described as validating transfer to other safety-critical domains.

---

# 28. Files to inspect

At minimum:

```text
evaluation-baseline-decision.md
research-design.md
active Journal 1 manuscript
README.md
section-5-plan.md
section-6-plan.md
canonical evaluation-design-rq4.md
condition_comparison.py
canonical empirical findings
```

Use historical plans only for provenance.

Do not allow them to override maintained design.

---

# 29. Expected maintained-file changes

Likely:

```text
evaluation-baseline-decision.md
research-design.md
active Journal 1 manuscript
```

Potentially README if it lists the design.

Do not edit canonical scripts.

Do not edit submitted conference artefacts.

---

# 30. Evidence directory

Create:

```text
data/journal1-evaluation-specification/
```

Produce:

```text
integrity-before.json
integrity-after.json

condition-label-audit.csv
rq-audit.csv
hypothesis-audit.csv
metric-audit.csv
evaluation-specification.csv
change-map.csv

formal-vs-empirical-verification.json
condition-mapping-verification.json
parser-test.json
closure.json
build.py
```

---

# 31. CSV parser requirements

Every CSV must pass:

```text
csv.DictReader
pandas.read_csv
```

with strict field-count checking.

---

# 32. Decision document

Create:

```text
publications/active/journal-1/evaluation-specification.md
```

Suggested structure:

```text
1. Purpose
2. Accepted baseline decision
3. Condition definitions
4. Structural comparator
5. Research questions
6. Formal propositions
7. Implementation-fidelity criteria
8. Empirical hypotheses
9. Metrics
10. Ablation design
11. Performance evaluation
12. Statistical treatment
13. PRIMARY / RESOLUTION reporting
14. Layer 3 dependency
15. Human-validation boundary
16. Threats and limitations
17. Open items
18. Final evaluation matrix
```

This file should become the **single maintained design authority** for Journal 1 evaluation.

---

# 33. Update active manuscript plans

Synchronise the manuscript's planned sections:

```text
Section 10 Experimental Design
Section 11 Results
Section 12 Ablation
Section 13 Discussion
Section 14 Threats to Validity
```

Do not write results that do not yet exist.

Only update design instructions.

---

# 34. Open items allowed at closure

The specification may close while explicitly carrying bounded OPEN items such as:

```text
H3 acceptance latency threshold
decision-support utility construct
future user-study measures
Layer 3 implementation details
```

provided they are clearly marked and do not create contradictions.

Do not fabricate values merely to achieve a fully filled table.

---

# 35. Stop conditions

## JES-R1 — canonical authority conflict

If canonical condition meanings conflict across authoritative sources:

```text
JOURNAL1 EVALUATION SPECIFICATION OPEN — CONDITION AUTHORITY CONFLICT
```

## JES-R2 — baseline decision contradiction

If Option C is logically inconsistent with the canonical harness:

```text
JOURNAL1 EVALUATION SPECIFICATION OPEN — BASELINE DECISION CONFLICT
```

## JES-R3 — unsupported empirical threshold

If H3 or another hypothesis requires a numerical threshold without evidence:

mark OPEN.

Do not invent one.

## JES-R4 — utility construct undefined

If decision-support utility has no defensible operational definition:

```text
OPEN — UTILITY CONSTRUCT REQUIRES DESIGN
```

This does not necessarily block the rest of the specification.

## JES-R5 — new experiment required

Do not run it.

Record what experiment will later be required.

## JES-R6 — protected canonical change required

STOP:

```text
JOURNAL1 EVALUATION SPECIFICATION OPEN — PROTECTED CANONICAL CHANGE REQUIRED
```

---

# 36. Closure criteria

Do not close until:

```text
[ ] Option C remains accepted
[ ] retrospective-window census wording corrected
[ ] Layer 3/H1/H2 wording corrected

[ ] active condition notation normalised to C0/C1/C2/C3
[ ] no active Journal-specific inverted label mapping remains
[ ] historical labels scoped appropriately

[ ] C3 treated as structural comparator, not fourth experimental arm
[ ] C1≡C3 proposition explicitly stated
[ ] analytical/executable/trace evidence separated
[ ] fairness qualification preserved

[ ] RQ-J1–RQ-J4 audited
[ ] H1 no longer circular behavioural hypothesis
[ ] H2 no longer circular behavioural hypothesis
[ ] H3 unsupported threshold not invented
[ ] H4 aligned to isolated Level 2 contribution

[ ] formal claims separated from fidelity tests
[ ] fidelity tests separated from behavioural outcomes

[ ] metric set answers actual RQs
[ ] pairwise divergence included where justified
[ ] isolated Level 2 contribution included
[ ] utility metric resolved or explicitly OPEN

[ ] deterministic replay statistics correctly framed
[ ] retrospective window not called a broader population census
[ ] no meaningless significance test prescribed

[ ] PRIMARY / RESOLUTION roles preserved
[ ] Layer 3 unbuilt status preserved
[ ] no human-outcome validation implied

[ ] evaluation-specification.md created
[ ] active manuscript plans aligned
[ ] evaluation master table complete

[ ] protected hashes unchanged
[ ] canonical scripts unchanged
[ ] empirical results unchanged
[ ] prediction register unchanged
[ ] all edited files mapped
[ ] CSV parser PASS
[ ] no unexpected changes
```

---

# 37. Final recommendation required

End the report with a concise final specification:

```text
PRIMARY EXPERIMENT:
C0 Ungated
C1 Binary
C2 Proposed

STRUCTURAL COMPARATOR:
C3 Flehmig-style topology

FORMAL:
Totality
Monotonicity
Safety Dominance
C1≡C3 proposition

FIDELITY:
implementation conformance to A_AI(S)

EMPIRICAL:
pairwise divergence
isolated Level 2 contribution
resolution sensitivity
transition/hysteresis characterisation

PERFORMANCE:
governance latency/resource overhead

HUMAN VALIDATION:
separate future socio-technical evaluation
```

---

# 38. Final closure line

If all mandatory items pass:

```text
JOURNAL 1 EVALUATION SPECIFICATION CLOSED — CONDITIONS, CLAIM TYPES AND METRICS ALIGNED
```

Otherwise:

```text
JOURNAL 1 EVALUATION SPECIFICATION REMAINS OPEN — EXPERIMENTAL DESIGN INCONSISTENCY REMAINS
```

and name the exact blockers.

---

# Guiding principles

A theorem is not a hypothesis.

An invariant is not a behavioural outcome.

A deterministic census value is not a population estimate.

A structural comparator is not necessarily an experimental arm.

Implementation fidelity is evidence that code matches the specification; it is not evidence that the specification is epistemically correct.

The smallest defensible evaluation is better than the largest possible evaluation.

And no experiment should begin until every condition label, hypothesis and metric has exactly one meaning.
