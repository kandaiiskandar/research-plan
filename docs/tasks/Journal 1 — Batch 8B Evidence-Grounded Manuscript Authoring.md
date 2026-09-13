# Journal 1 — Batch 8B

## Evidence-Grounded Manuscript Authoring

### Role

Act as a scientific manuscript author, evidence auditor, and claim-control reviewer.

You are working on Journal 1:

**A Formally Verified Runtime AI Governance Architecture Based on Graduated Safety-State Gating**

Primary target:

**Safety Science (Elsevier)**

The manuscript is in the research-design / pre-submission stage and has never been submitted.

This batch converts the currently undrafted manuscript sections into evidence-grounded scientific prose while preserving all CLOSED scientific authority established through Batch 8A.

---

# 1. Task Objective

Complete the currently undrafted substantive manuscript sections using only evidence and scientific authority already established in the repository.

The main authoring scope is:

```text
Abstract
Section 1 — Introduction
Section 2 — Related Work
Section 3 — AI Governance Foundations
Section 4 — Problem Formulation
Section 9 — Prototype Implementation
Section 10 — Experimental Design
Section 11 — Results
Section 12 — Ablation and Sensitivity Analysis
Section 13 — Discussion
Section 14 — Threats to Validity
Section 15 — Conclusion
```

Sections 5–8 already contain substantive prose and were synchronised during Batch 8A.

Do not rewrite Sections 5–8 merely for style.

Modify them only if drafting the remaining manuscript exposes a direct scientific contradiction.

If such a contradiction is discovered:

```text
STOP

BATCH_8B_BLOCKED —
EXISTING SYNCHRONISED PROSE CONTRADICTS AUTHORITATIVE EVIDENCE
```

Report the exact conflict before modifying frozen/synchronised scientific content.

---

# 2. Scientific Mode

This is:

```text
EVIDENCE-GROUNDED AUTHORING
```

It is NOT:

```text
new experimentation
new replay analysis
new statistical analysis
new architecture design
new algorithm design
new Layer 3 implementation
new threshold selection
new literature search
Android benchmarking
human-subject evaluation
scientific code modification
```

Do not generate evidence while writing.

The manuscript must reflect the evidence that exists.

The prose must not create evidence that does not exist.

---

# 3. Repository Baseline

Before editing:

record:

```text
branch
HEAD
git status
manuscript hash
```

Verify that Batch 8A is CLOSED.

Verify the active manuscript is:

```text
publications/active/journal-1/submissions/v1-initial-submission/manuscript.md
```

The directory name does NOT mean that the manuscript has been submitted.

Verify repository hygiene before proceeding.

Exclude repository noise such as:

```text
.DS_Store
__pycache__
```

from scientific changes.

---

# 4. Mandatory Authorities

Before writing substantive prose, read the authoritative sources rather than relying on this prompt.

At minimum read:

```text
publications/active/journal-1/evaluation-specification.md

publications/active/journal-1/algorithm-specification.md

publications/active/journal-1/submissions/v1-initial-submission/manuscript.md

docs/canonical/appendix-c-formalisation.md
```

Read the authoritative Layer 3 prototype specification.

Read Batch 5 fidelity evidence.

Read Batch 6 post-fidelity evaluation planning evidence.

Read Batch 7A E5 benchmark evidence.

Read the E3/E4 authority micro-repair.

Read all Batch 8A outputs, especially:

```text
data/journal1-manuscript-evidence-sync/claim-evidence-matrix.csv

data/journal1-manuscript-evidence-sync/manuscript-claim-inventory.csv

data/journal1-manuscript-evidence-sync/quantitative-provenance.csv

data/journal1-manuscript-evidence-sync/claim-change-log.csv

data/journal1-manuscript-evidence-sync/e5-status-audit.md

data/journal1-manuscript-evidence-sync/manuscript-diff-audit.md

data/journal1-manuscript-evidence-sync/verification.json

data/journal1-manuscript-evidence-sync/integrity.json

data/journal1-manuscript-evidence-sync/report.md
```

Where this prompt conflicts with repository authority:

```text
STOP
```

Do not silently choose one.

---

# 5. Frozen Evaluation Status

Expected scientific status entering Batch 8B:

```text
P1 = CLOSED
P2 = CLOSED
P3 = CLOSED
P4 = CLOSED

F1 = CLOSED
F2 = CLOSED
F3 = CLOSED

E1 = CLOSED
E2 = CLOSED
E3 = CLOSED
E4 = CLOSED

E5 = OPEN

E6 = CLOSED
```

Additional E5 status:

```text
E5_HARNESS = CLOSED

MACBOOK_REFERENCE = COMPLETE

target_hardware_evidence = false

E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY

H3 = OPEN/UNSUPPORTED
```

E3 authority after the micro-repair:

```text
E3_SCOPE = {E1, E2, E6}

E4_RESOLUTION =
NOT_REQUIRED_BY_CURRENT_E3_DESIGN
```

Verify these from repository authority before drafting.

---

# 6. Claim-Control Rule

Every material scientific statement introduced in Batch 8B must belong to one of:

```text
FORMAL
IMPLEMENTATION_FIDELITY
EMPIRICAL_TRACE
PERFORMANCE_REFERENCE
DESIGN_INTERPRETATION
LIMITATION
FUTURE_WORK
```

Do not introduce:

```text
PERFORMANCE_TARGET
```

as a completed result because E5 remains OPEN.

Every quantitative result must have an authoritative provenance entry.

Every empirical claim must map to CLOSED evidence.

Every interpretation must be distinguishable from an observed result.

---

# 7. Formal Claims P1–P4

P1–P4 remain formal claims.

Do not convert them into empirical findings.

Preserve the distinction:

```text
formal proof
≠
implementation-fidelity evidence
≠
historical replay evidence
```

The manuscript may state that formal properties are proved where authority supports this.

Do not state that empirical replay "proves" the formal theorems.

Likewise, theorems do not establish empirical safety effectiveness.

---

# 8. Safety Dominance Scope

Preserve the bounded meaning of Safety Dominance.

The architecture establishes:

```text
AI(E) ⊆ A_AI(f(E))
```

under the stated rule-engine and governance assumptions.

This means the AI cannot exceed the configured admissible recommendation scope.

It does NOT establish:

```text
physical safety
correctness of every recommendation
optimality of A_AI
absence of maritime accidents
safe departure
risk elimination
human behavioural compliance
```

Do not use phrases such as:

```text
guarantees safe departure
guarantees fisherman safety
prevents accidents
ensures safe AI decisions
```

unless explicitly bounded to the formal governance property.

---

# 9. UNSAFE Semantics

Preserve exactly:

```text
UNSAFE = governance state in which AI advisory participation is unavailable
```

UNSAFE does NOT necessarily mean:

```text
physical danger is certain
departure is legally prohibited
the human is forbidden to depart
harm will occur
```

UNSAFE may arise from:

```text
environmental hazard bands
required-input faults
valid nighttime policy
```

Human authority remains unconditional.

---

# 10. Human Authority

The architecture is decision support.

The human operator retains final authority.

Do not describe the architecture as:

```text
autonomous decision making
automatic departure control
departure authorisation
AI-enforced human behaviour
```

Layer 4 remains human decision authority.

---

# 11. Layer 3 Semantics

Preserve the frozen Layer 3 model.

Layer 2 computes the governance state.

Layer 3 does not recompute Layer 2.

Layer 3 consumes:

```text
S
G(S)
A_AI(S)
ComponentStateTrace
```

according to the frozen interface.

Preserve:

```text
SAFE:
A_AI = {Go, Delay, DepartureTime, Duration}

CAUTION:
A_AI = {Go, Delay}

UNSAFE:
A_AI = ∅
```

Do not imply:

```text
SAFE → Go automatically

CAUTION → Delay automatically

CAUTION → Go automatically
```

The state determines admissibility, not which advisory must be generated.

---

# 12. CAUTION-Go Semantics

Preserve Resolution B.

If Layer 3 produces:

```text
Go
```

under CAUTION, the recommendation type remains:

```text
Go
```

A caution qualifier may be applied at presentation/interface level.

Do not create a new formal recommendation type such as:

```text
CautiousGo
ConditionalGo
GoWithCaution
```

unless such a type already exists in authority.

---

# 13. Predicate Failure Semantics

Preserve the frozen Layer 3 predicate model:

```text
TRUE
FALSE
ERROR
```

Any predicate ERROR during an active episode produces bounded advisory refusal:

```text
AI = ∅
```

while preserving:

```text
S
G(S)
A_AI(S)
```

Do not conflate predicate error with:

```text
UNSAFE
configuration failure
Layer 2 input fault
```

---

# 14. Component-State Interface

Preserve:

```text
ComponentStateTrace
```

as the Layer 2 → Layer 3 causal interface.

Layer 3 must not recompute environmental classification.

Preserve:

```text
EXCLUDED ≠ SAFE
```

even where exclusion contributes SAFE to Layer 2 aggregation.

Do not collapse those semantics in explanatory prose.

---

# 15. F1–F3 Implementation-Fidelity Results

F1–F3 are CLOSED.

Verify exact counts from authoritative Batch 5 evidence before writing.

Expected:

```text
primary episodes = 292

SAFE = 32
CAUTION = 260

advisory records = 454

episodes with advisory = 244

CAUTION episodes with empty advisory = 16
```

Expected fidelity:

```text
F1 violations = 0

F2 violations = 0

F3 mismatches = 0
```

Preserve the evaluation scope:

```text
interface-contract exhaustive
```

Do NOT describe this as:

```text
historically exhaustive
environmentally exhaustive
deployment exhaustive
real-world exhaustive
all possible maritime situations
```

---

# 16. F1 244-Count Trap

Be extremely careful with:

```text
conclusion_types_evaluated = 244
```

This does NOT mean:

```text
244 distinct advisory conclusion types
```

It represents per-episode non-empty conclusion-type evaluations / advisory episodes.

The generated advisory conclusion type in this bounded prototype is:

```text
Delay
```

Do not write "244 advisory types".

---

# 17. Layer 3 Rule Activation Results

Verify authoritative values.

Expected:

```text
R-CAUTION-001
selected = 260
true = 130
fired = 130

R-CAUTION-002
selected = 260
true = 108
fired = 108

R-CAUTION-003
selected = 260
true = 108
fired = 108

R-CAUTION-004
selected = 260
true = 108
fired = 108

total advisory records = 454
```

Do not infer behavioural effectiveness from rule activation.

---

# 18. Experimental Conditions

Preserve the canonical experiment structure:

```text
C0 = Ungated

C1 = Binary

C2 = Proposed graduated architecture

C3 = Flehmig structural comparator
```

Primary empirical comparison:

```text
C0
C1
C2
```

C3 is structural comparator/proposition support.

Do not present C3 as a fourth equal experimental arm unless authority explicitly supports that interpretation.

---

# 19. E1 Divergence

Verify exact values before writing.

Expected PRIMARY:

```text
C0 ↔ C1 = 42.88%

C0 ↔ C2 = 48.69%

C1 ↔ C2 = 5.81%

C1 ↔ C3 = 0.00%
```

Expected RESOLUTION:

```text
C0 ↔ C1 = 41.08%

C0 ↔ C2 = 45.56%

C1 ↔ C2 = 4.48%

C1 ↔ C3 = 0.00%
```

These are deterministic replay quantities.

Do not attach:

```text
p-values
confidence intervals
sampling inference
population inference
```

unless separately authorised.

---

# 20. E2 Level-2 Binding

Expected:

```text
PRIMARY = 5.81%

RESOLUTION = 4.48%
```

Interpret as:

```text
additional advisory-scope governance introduced by the graduated architecture relative to binary participation-only governance
```

Do NOT interpret as:

```text
5.81% safer
5.81% risk reduction
5.81% accident prevention
5.81% accuracy improvement
```

---

# 21. E3 Resolution Sensitivity

Use repaired authority.

E3 mandatory scope:

```text
{E1, E2, E6}
```

Do not require E4 dual-configuration reporting.

Correct:

```text
E4 = PRIMARY temporal-dynamics characterisation
```

and:

```text
E4_RESOLUTION =
NOT_REQUIRED_BY_CURRENT_E3_DESIGN
```

Do not claim:

```text
E4 is resolution-insensitive

E4 would reproduce under MFWAM

RESOLUTION E4 equals PRIMARY E4
```

---

# 22. E4 Temporal Dynamics

Verify exact authoritative figures.

Expected PRIMARY:

```text
state transitions = 3661

scheduled transitions = 3439

non-scheduled transitions = 222

oscillations = 26

hysteresis reduction = 10.36%
```

Preserve provenance:

```text
5416
→ 5220 threshold
→ 5201 data
→ 3661 g_t
```

Do not describe:

```text
5416 → 3661
```

as purely caused by g_t.

Do not invent RESOLUTION E4 figures.

---

# 23. E6 Structural Equivalence

Preserve:

```text
C1 ↔ C3 = 0.00%
```

over the authoritative replay horizon.

Interpret this as:

```text
executable confirmation of the structurally established admissible-set equivalence
```

not:

```text
empirical discovery that the architectures are universally identical
```

---

# 24. Replay Semantics

The retrospective replay is:

```text
deterministic census
```

of all hourly records in the predefined retrospective window.

It is not:

```text
random sample
probabilistic trial
clinical-style experiment
population survey
```

Do not report conventional inferential statistics merely because the manuscript is empirical.

PRIMARY and RESOLUTION are sensitivity configurations.

They are not confidence intervals.

---

# 25. E5 — Absolute Boundary

E5 remains OPEN.

This is the most important manuscript boundary in Batch 8B.

Batch 7A established only:

```text
benchmark harness = validated

MacBook development reference = complete
```

It did NOT establish target-hardware performance.

MacBook results may be reported only as:

```text
development-machine reference benchmark
```

or equivalent bounded wording.

Never call them:

```text
deployment performance
target-hardware performance
mobile performance
Android performance
real-time performance
production performance
```

---

# 26. MacBook Reference Benchmark

If included, recover exact authoritative values from Batch 7A.

Do not rely on rounded values in this prompt when higher precision exists in repository evidence.

Hardware context is approximately:

```text
MacBook Pro
Apple M3 Pro
arm64
36 GB RAM
macOS 26.2
Python 3.9.6
AC power
```

Expected workload structure:

```text
W-SAFE
W-CAUTION
W-UNSAFE

500 measured repetitions each
50 warm-up iterations
1500 raw measured rows
```

Do not convert the MacBook reference into evidence about Android feasibility.

---

# 27. E5 Resource Semantics

Preserve measurement semantics.

Peak RSS is:

```text
process-lifetime peak RSS
```

not:

```text
per-episode memory
```

CPU measurement is:

```text
measured-loop user CPU time
```

not:

```text
CPU percentage
per-episode CPU utilisation
```

Do not overinterpret resource measurements.

---

# 28. H3

Preserve:

```text
H3 = OPEN/UNSUPPORTED
```

No authoritative latency threshold exists.

Do not invent:

```text
X ms
real-time threshold
acceptable latency threshold
mobile suitability threshold
deployment requirement
```

Do not convert low MacBook latency into an H3 PASS.

---

# 29. Android Benchmark

Batch 7B remains:

```text
DEFERRED_MANDATORY
```

because representative physical Android hardware is not currently available.

Do not:

```text
simulate Android performance
estimate Android latency
scale MacBook latency
use emulator performance
use CI performance
use cloud performance
```

as target evidence.

Batch 8B may explicitly identify Android target-hardware benchmarking as remaining work.

---

# 30. Section 1 — Introduction

Draft a publication-quality Introduction.

It should establish:

1. safety-critical AI governance problem;
2. distinction between AI participation and AI advisory scope;
3. limitation of binary participation-only governance;
4. proposed graduated governance architecture;
5. why formal verification and executable implementation fidelity are required;
6. empirical replay purpose;
7. bounded contributions of Journal 1;
8. research questions;
9. manuscript organisation.

Do not overstate novelty.

Preserve the established novelty boundary:

> Graduated governance exists; graduated advisory-scope governance is the contribution being investigated.

Do not claim that intermediate safety/governance states themselves are novel.

---

# 31. Section 2 — Related Work

Draft only from literature already present in repository authority and existing cited material.

Do NOT conduct new literature search in Batch 8B.

Do not invent references.

Use existing comparison/review artefacts where authoritative.

Organise the literature around concepts relevant to the paper rather than producing a citation catalogue.

Distinguish:

```text
graduated supervisory control

execution restriction

agent action-space restriction

AI participation gating

human-facing advisory-scope governance
```

The gap must be stated narrowly.

If repository evidence is insufficient for a planned subsection:

```text
OPEN — LITERATURE SUPPORT REQUIRED
```

Do not manufacture supporting prose.

---

# 32. Section 3 — AI Governance Foundations

Draft the theoretical foundation needed by the architecture.

Use only standards and governance material already supported in repository sources.

Do not introduce a new standards framework.

Preserve distinction between:

```text
coding mechanism

governance principle

formal property

runtime enforcement

institutional standard
```

Do not claim compliance/certification with:

```text
ISO
IEC
NIST
EU AI Act
OECD
maritime regulation
```

unless authority actually establishes compliance.

Referencing a standard is not certification against that standard.

---

# 33. Section 4 — Problem Formulation

Provide a precise formal problem statement.

Connect:

```text
observations
resolution
classification
governance
admissible recommendation space
Layer 3 output
human authority
```

Use the canonical formalisation.

Do not create a new mathematical model.

Explicitly state assumptions and scope.

Define "better" only through authorised evaluation quantities.

Do not define safety improvement as accident reduction.

---

# 34. Section 9 — Prototype Implementation

Describe what was actually implemented.

Include:

```text
Layer 2 governance implementation

Layer 3 rule engine

ComponentStateTrace interface

rule-set supply

predicate semantics

configuration-fidelity failure

UNSAFE gate-off

CAUTION rules

implementation-fidelity evaluation
```

Distinguish:

```text
prototype implementation
```

from:

```text
deployed production system
```

Do not imply fishermen used this prototype in operational deployment.

---

# 35. Section 10 — Experimental Design

Describe the evaluation design before presenting results.

Include:

```text
RQ mapping

P1–P4

F1–F3

E1–E6

C0/C1/C2 primary comparison

C3 structural comparator

PRIMARY

RESOLUTION

deterministic replay census

interface-contract exhaustive Layer 3 evaluation

E5 benchmark protocol/status
```

Do not turn P/F/E labels into unsupported hypotheses.

Do not restore retired:

```text
H1
H2
H4
```

H3 remains unsupported/open and should not be framed as passed.

---

# 36. Section 11 — Results

This section must report CLOSED results only.

Recommended structure:

```text
11.1 Formal verification results

11.2 Implementation-fidelity results

11.3 Governance divergence and Level-2 binding

11.4 Resolution sensitivity

11.5 Temporal dynamics and hysteresis

11.6 Structural comparator confirmation

11.7 Performance status / development-machine reference
```

For E5:

either report the MacBook reference in a clearly separated bounded subsection,

or state that target-hardware E5 remains open while giving the development-machine reference only as implementation context.

Do not blur it into the CLOSED empirical results.

---

# 37. Results Tables

Create concise publication-ready tables where useful.

Every number must be provenance-checked.

At minimum consider:

```text
formal/evaluation status table

F1–F3 fidelity table

E1 divergence table

E2 Level-2 binding table

E4 temporal-dynamics table

E5 status/reference table
```

Do not create statistical significance columns.

Do not fabricate uncertainty intervals.

---

# 38. Section 12 — Ablation and Sensitivity Analysis

Use only existing closed analyses.

Potential authorised content includes:

```text
PRIMARY vs RESOLUTION

C0/C1/C2 comparison

C1/C3 structural equivalence confirmation

hysteresis comparison already established

component/gate contributions where closed evidence exists
```

Do not run a new ablation.

Do not create E4 RESOLUTION.

Do not infer causal effects from descriptive differences.

If an intended ablation has no closed evidence, omit it or label it future work.

---

# 39. Section 13 — Discussion

Separate:

```text
RESULT
```

from:

```text
INTERPRETATION
```

Discuss what the architecture demonstrates:

```text
formal advisory-scope governance

difference between binary participation and graduated scope

bounded implementation fidelity

deterministic replay behaviour

importance of policy/environment/fault distinction

implications for low-resource safety-critical decision support
```

Also discuss what it does NOT demonstrate:

```text
human trust
behavioural effectiveness
accident reduction
real-world safety improvement
target-device performance
generalisability to all domains
optimality of thresholds
optimality of A_AI
```

Do not convert design rationale into empirical validation.

---

# 40. Section 14 — Threats to Validity

Draft a substantive threats-to-validity section.

At minimum consider:

```text
Construct validity
Internal validity
External validity
Data validity
Implementation validity
Temporal validity
Policy/configuration validity
Performance validity
```

Explicit limitations should include where applicable:

```text
D = {m} historical marine-warning exclusion

historical replay rather than prospective deployment

threshold dependence

configured A_AI rather than empirically optimised A_AI

single coastal case context

PRIMARY/RESOLUTION coverage differences

E4 PRIMARY-only temporal characterisation

Layer 3 interface-contract state-space evaluation

absence of human behavioural evaluation

E5 target-hardware evidence pending

Android benchmark deferred

MacBook reference not deployment evidence
```

Do not minimise limitations.

A strong limitations section strengthens the paper.

---

# 41. Section 15 — Conclusion

The Conclusion must be bounded.

Summarise:

```text
problem
architecture
formal contribution
implementation-fidelity evidence
replay evidence
main empirical distinction
limitations
remaining E5 dependency
future human/deployment evaluation
```

Do not claim:

```text
architecture validated for real-world deployment

system proven safe for fishermen

accidents reduced

human trust established

mobile feasibility established

all safety-critical domains supported
```

End with the bounded general contribution:

a formally specified and executable pattern for separating AI participation from state-dependent advisory scope.

---

# 42. Abstract

Write the Abstract LAST.

Only after Sections 1–15 are coherent.

The Abstract should contain:

```text
Background/problem

Method/architecture

formal contribution

evaluation design

most important CLOSED results

bounded conclusion
```

Quantitative claims must be traceable.

E5 target-hardware performance must NOT appear as completed evidence.

If mentioning performance:

state only that target-hardware characterisation remains pending.

Do not put the MacBook reference in the Abstract unless there is a compelling manuscript-level reason and it is explicitly labelled development-machine reference evidence.

---

# 43. Keywords

After completing the Abstract, draft 5–8 keywords.

Keywords must reflect the manuscript actually written.

Do not introduce concepts absent from the paper.

---

# 44. Citation Rule

Do not perform new literature search.

Do not invent citations.

Do not fabricate DOI, author, year, standard clause, regulation, or publication.

Use only citations already supported by repository sources.

If a statement requires literature support that is unavailable:

```text
[CITATION SUPPORT REQUIRED]
```

and record it in the Batch 8B report.

Do not silently solve it with general knowledge.

---

# 45. Style

Target publication-quality scientific prose appropriate for Safety Science.

Prefer:

```text
precise
bounded
formal
evidence-led
reviewer-readable
```

Avoid:

```text
marketing language
AI hype
absolute safety claims
repetitive novelty claims
unnecessary adjectives
overlong methodological narration
```

Do not optimise for word count before scientific correctness.

---

# 46. Cross-Section Consistency Audit

After drafting, verify consistency across:

```text
Abstract
Introduction
Related Work
Foundations
Problem Formulation
Formal Architecture
Theoretical Analysis
Algorithms
Research Design
Prototype
Experimental Design
Results
Ablation
Discussion
Threats
Conclusion
```

Search specifically for contradictions involving:

```text
SAFE
CAUTION
UNSAFE

G(S)

A_AI(S)

RS(S)

E3

E4

E5

H3

PRIMARY

RESOLUTION

C0
C1
C2
C3

F1
F2
F3

Safety Dominance

human authority

Android

MacBook

latency

real-time

validation

deployment

safety
```

---

# 47. Overclaim Audit

Search the completed manuscript for phrases equivalent to:

```text
proved safe

validated safety

guarantees safety

safe to depart

prevents accidents

risk reduction

accuracy improvement

real-time

deployment-ready

mobile-ready

Android performance

acceptable latency

statistically significant

confidence interval

human trust

user acceptance

universally applicable
```

For every occurrence:

```text
justify
bound
replace
or remove
```

Record the outcome.

---

# 48. Quantitative Audit

Every quantitative value introduced into the manuscript must be mapped to:

```text
claim
metric
value
configuration
source artefact
status
manuscript location
```

Create:

```text
data/journal1-manuscript-authoring/
quantitative-provenance.csv
```

No orphan number is permitted.

---

# 49. Claim-Evidence Audit

Create:

```text
data/journal1-manuscript-authoring/
claim-evidence-audit.csv
```

Columns:

```text
claim_id
manuscript_section
claim_text_summary
claim_type
authority
evidence_status
allowed_scope
prohibited_interpretation
verification
```

All material new claims must appear.

---

# 50. New-Prose Audit

Create:

```text
data/journal1-manuscript-authoring/
new-prose-audit.md
```

For each newly authored section report:

```text
section
authoring status
authoritative sources used
new quantitative claims
interpretive claims
limitations introduced
open dependencies
```

---

# 51. Citation Audit

Create:

```text
data/journal1-manuscript-authoring/
citation-audit.md
```

Report:

```text
existing citations reused

new citations added = 0 expected

unsupported citation placeholders

citation-dependent claims requiring future repair
```

Do not hide unsupported literature gaps.

---

# 52. E5 Audit

Create:

```text
data/journal1-manuscript-authoring/
e5-boundary-audit.md
```

Verify every manuscript mention of:

```text
E5
benchmark
performance
latency
milliseconds
CPU
memory
MacBook
M3
Android
mobile
target hardware
real-time
deployment
```

For each occurrence classify:

```text
ALLOWED
REVISED
REMOVED
```

Success requires:

```text
no target-hardware result invented

no Android result invented

no H3 threshold invented

no MacBook→Android extrapolation

E5 remains OPEN
```

---

# 53. Stub Audit

After authoring, identify remaining:

```text
(Draft here)
UNDRAFTED
Purpose:
Key content to include:
To be written
placeholder
TODO
TBD
```

Classify every remaining occurrence.

Substantive manuscript sections should no longer contain drafting stubs unless there is a scientifically justified OPEN dependency.

Do not remove an OPEN marker merely for cosmetic completeness.

---

# 54. Integrity

Create:

```text
data/journal1-manuscript-authoring/integrity.json
```

Hash relevant files before and after.

Expected scientific changes:

```text
active manuscript

new Batch 8B evidence/audit artefacts
```

Expected unchanged:

```text
canonical formalisation

evaluation specification

algorithm specification

Layer 3 implementation

Batch 5 evidence

Batch 6 evidence

Batch 7A evidence

E3/E4 repair authority

evaluation scripts

governance code
```

If scientific authority changes unexpectedly:

```text
FAIL
```

Do not silently absorb it into manuscript authoring.

---

# 55. Verification

Create:

```text
data/journal1-manuscript-authoring/verification.json
```

Use:

```text
PASS
FAIL
OPEN
```

At minimum verify:

```text
batch8a_closed

e3_e4_repair_closed

abstract_authored_last

section1_authored
section2_authored_or_supported_gap_explicit
section3_authored
section4_authored

section9_authored
section10_authored
section11_authored
section12_authored
section13_authored
section14_authored
section15_authored

sections5_8_not_unnecessarily_rewritten

P1_P4_formal_scope_preserved

F1_F3_closed_results_accurate

F1_244_semantics_correct

E1_primary_values_accurate
E1_resolution_values_accurate

E2_primary_5_81
E2_resolution_4_48

E3_scope_correct

E4_primary_only

E4_values_accurate

E6_equivalence_bounded

replay_described_as_deterministic_census

no_p_values_invented

no_confidence_intervals_invented

UNSAFE_governance_semantics_preserved

human_authority_unconditional

Safety_Dominance_bounded

Layer3_does_not_recompute_Layer2

ComponentStateTrace_boundary_preserved

predicate_ERROR_semantics_preserved

CAUTION_Go_semantics_preserved

E5_open

MacBook_reference_bounded

Android_deferred

H3_open_unsupported

no_latency_threshold

no_real_time_claim

no_deployment_ready_claim

no_human_validation_claim

no_accident_reduction_claim

no_new_experiment

no_new_replay

no_scientific_code_change

no_new_external_citation

all_quantitative_claims_provenanced

all_material_new_claims_audited

remaining_stubs_classified

cross_section_consistency_pass

overclaim_audit_pass

frozen_authority_unchanged
```

---

# 56. Stop Conditions

STOP immediately if:

### A. Evidence contradiction

Two CLOSED authorities materially disagree.

```text
BATCH_8B_BLOCKED —
CONFLICTING CLOSED AUTHORITIES
```

### B. Missing load-bearing evidence

A planned manuscript claim requires evidence that does not exist.

Do not invent it.

Either omit the claim or, if manuscript logic depends on it:

```text
BATCH_8B_BLOCKED —
LOAD-BEARING CLAIM LACKS AUTHORITATIVE EVIDENCE
```

### C. New experiment required

```text
BATCH_8B_BLOCKED —
AUTHORING REQUIRES NEW EMPIRICAL WORK
```

### D. Frozen scientific code would need modification

```text
BATCH_8B_BLOCKED —
SCIENTIFIC IMPLEMENTATION CHANGE REQUIRED
```

### E. E5 accidentally becomes necessary for a completed scientific conclusion

Do not fabricate closure.

Record the dependency and preserve E5 OPEN.

---

# 57. Batch 8B Report

Create:

```text
data/journal1-manuscript-authoring/report.md
```

Include:

```text
objective

baseline

authorities read

sections authored

sections preserved

formal claims represented

fidelity results represented

empirical results represented

E3 treatment

E4 treatment

E5 treatment

MacBook reference treatment

Android status

H3 status

citation gaps

remaining OPEN items

quantitative audit summary

claim audit summary

overclaim audit summary

verification totals

changed files

unexpected changes

manuscript hash before

manuscript hash after

final scientific status
```

---

# 58. Success Condition

Batch 8B succeeds only if:

```text
all intended manuscript sections contain evidence-grounded prose

formal and empirical claims remain correctly separated

all CLOSED evidence used is accurately represented

no unsupported scientific result is introduced

no target-hardware performance is fabricated

E5 remains OPEN

H3 remains OPEN/UNSUPPORTED

Android benchmark remains DEFERRED_MANDATORY

limitations are explicit

every quantitative claim is traceable

all material new claims are audited

no new experiment was performed

no scientific code was changed

frozen scientific authority remains unchanged
```

The manuscript may become:

```text
DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY
```

It must NOT become:

```text
FINAL_REVIEWER_READY
```

while mandatory target-hardware E5 remains unresolved.

---

# 59. Exact Closure

If all required checks pass:

```text
JOURNAL 1 MANUSCRIPT BATCH 8B CLOSED —
EVIDENCE-GROUNDED MANUSCRIPT AUTHORING COMPLETED WITH E5 TARGET-HARDWARE DEPENDENCY PRESERVED
```

Post-batch status:

```text
P1–P4 = CLOSED

F1–F3 = CLOSED

E1–E4 = CLOSED

E5 = OPEN

E6 = CLOSED

E3_SCOPE = {E1, E2, E6}

E4_RESOLUTION =
NOT_REQUIRED_BY_CURRENT_E3_DESIGN

E5_HARNESS = CLOSED

MACBOOK_REFERENCE = COMPLETE

E5_ANDROID_TARGET_BENCHMARK =
DEFERRED_MANDATORY

H3 = OPEN/UNSUPPORTED

MANUSCRIPT_AUTHORING = CLOSED

MANUSCRIPT_STATUS =
DRAFT_COMPLETE_WITH_OPEN_E5_DEPENDENCY

FINAL_REVIEWER_READY = false
```

---

# 60. Final Response

Return a concise but complete report containing:

1. branch;
2. HEAD before;
3. HEAD after;
4. manuscript hash before;
5. manuscript hash after;
6. sections authored;
7. sections preserved;
8. P1–P4 status;
9. F1–F3 status;
10. F1–F3 authoritative counts;
11. E1 PRIMARY results;
12. E1 RESOLUTION results;
13. E2 PRIMARY/RESOLUTION;
14. E3 scope;
15. E4 values and PRIMARY-only status;
16. E6 result and interpretation;
17. E5 status;
18. MacBook reference status;
19. Android status;
20. H3 status;
21. number of quantitative claims audited;
22. number of material claims audited;
23. citation gaps;
24. remaining manuscript stubs;
25. overclaim audit result;
26. cross-section consistency result;
27. verification PASS/FAIL/OPEN totals;
28. changed files;
29. unexpected changes;
30. exact closure statement.

Then recommend **exactly one next task**.

Because physical Android hardware is currently unavailable, the next task must be the highest-value executable manuscript/reviewer task that does NOT require Android hardware.

Do not execute that next task automatically.
