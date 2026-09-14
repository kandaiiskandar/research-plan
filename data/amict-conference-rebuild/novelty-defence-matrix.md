# Novelty Defence Matrix — AMICT Conference Rebuild

**Date:** 2026-09-14
**Task:** `docs/tasks/AMICT CONFERENCE PAPER REBUILD — ARCHITECTURE TO EMPIRICAL EVALUATION.md` §2
**Scope:** bounded comparison against five prior-work families. **Not** a new systematic literature review.
**Mechanism under test:** `S = f(E) → (G(S), A_AI(S)) → AI(E) → human decision`, with `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` and unconditional human final authority.

**Primary novelty question.** Has prior work already implemented a runtime mechanism in which the set of AI recommendation types that may be presented to a human decision-maker is dynamically restricted according to an externally classified risk or environmental state, while final human decision authority remains invariant?

**Answer: YES, in certified avionics.** See entry N-01. Consequences are set out in `novelty-audit-report.md`.

**Method note.** Entries were coded on mechanism, not vocabulary. No entry was scored as distinct because it uses different terminology, and no absence of a term was treated as absence of a mechanism.

---

## Summary table

Threat level answers one question only: *how much of the claimed contribution does this prior work already occupy?*

| # | Prior work | Family | Governed object | Runtime state source | Rec-type scope changed? | Human authority invariant? | Formal guarantee | Threat |
|---|---|---|---|---|---|---|---|---|
| N-01 | TCAS II / ACAS II low-altitude RA inhibition | E (operational) | Advisory types issuable to pilot | Radio altimeter AGL bands + configuration discretes | **YES — nested, monotone** | Partial (compliance expected) | Certified design rules | **HIGH** |
| N-02 | ACAS X formally verified advisory logic | E / B | Advisory selection | Encounter state + altitude | YES | Partial | **YES** (hybrid-systems proof, model checking) | **HIGH** |
| N-03 | Parasuraman, Sheridan & Wickens (2000) LOA | D | Degree of automation per stage | None — design-time assignment | Partial (Level 3 "narrows the selection down to a few") | Varies by level | No | **MEDIUM-HIGH** |
| N-04 | Adaptive automation / adaptive autonomy | D | Level of automation, task allocation | Operator state, workload, performance, mission phase | No | Yes (at low LOA) | No | MEDIUM |
| N-05 | Selective AI prediction in clinical decision-making | A | Which per-condition predictions are shown | Model accuracy / confidence (AI-internal) | Partial (per-item, not per-type) | Yes | No | MEDIUM |
| N-06 | Punzi et al. (2024) — L2R / L2D survey | A | Whether the machine predicts at all | Predicted accuracy / uncertainty (AI-internal) | No | Yes | Surrogate-loss guarantees | LOW-MEDIUM |
| N-07 | Baxi (2026) — CGAE | E | Executable economic permissions of an agent | Verified robustness audit (agent-internal), decayed | No (action tiers, not advice) | N/A — no human adviser loop | **YES** (bounded exposure, monotone scaling) | MEDIUM |
| N-08 | Flehmig et al. (2024) — traffic-light QA framework | E | Supervisory response intensity | AI degradation index | **No** — identical AI scope at green and orange | Yes | No | MEDIUM |
| N-09 | Ghaleb et al. (2026) — VLA safety gating | B / E | Physical execution behaviour | Calibrated model failure risk (AI-internal) | No | N/A — fallback is a planner, not a human | Explicitly none | MEDIUM |
| N-10 | Kwon et al. (2025) — Adaptive Shielding | C | Executable action set of an RL policy | Inferred hidden dynamics parameters | No | N/A | YES (cost-rate bound) | LOW-MEDIUM |
| N-11 | Shielding / action masking (Könighofer et al. 2025) | C | Executable action set | Automaton state / safety spec | No | N/A | YES | LOW |
| N-12 | Shamsujjoha et al. (2025) — Swiss Cheese guardrails | C / E | Catalogue of guardrail actions on FM outputs | Configured per artefact; context-dependent rule type | Partial (options catalogued, no selection mechanism) | Partial | No | LOW-MEDIUM |
| N-13 | FDA non-device CDS Criterion 3 | E (regulatory) | Permissible output form: list of options vs specific directive | None — design-time intended-purpose classification | **YES, but static** | Yes (Criterion 4) | No | MEDIUM |
| N-14 | Runtime governance for AI agents (2026 preprints) | E | Executable actions and tool calls | Execution path / agent-internal drift signals | No | No — approval is an injectable step | Partial (monotone tighten-only) | LOW-MEDIUM |
| N-15 | Feng et al. (2025) — Levels of Autonomy for AI Agents | D | Autonomy level designation | Fixed deployment-time constant | No | Varies | No | LOW |

---

## Full entries

### N-01 — TCAS II / ACAS II low-altitude resolution-advisory inhibition

- **Prior-work family:** E (graduated runtime governance), realised in certified operational avionics rather than in the research literature.
- **Governed object:** the set of resolution-advisory *types* the system may issue to the flight crew.
- **Runtime state source:** radio-altimeter height above ground level, banded; plus discrete aircraft-configuration inputs (flap, slat, landing-gear position) and performance limits.
- **AI participation changed?** N/A — the advisory generator is a deterministic collision-avoidance algorithm, not an AI component. At the lowest band the advisory function is switched off entirely, which is participation gating in all but name.
- **Prediction availability changed?** Yes at the limit — all RAs inhibited, degrading to TA-only, then TAs inhibited.
- **Executable action space changed?** No. The aircraft's control authority is untouched; only what the system may *say* changes.
- **Human authority changed?** The crew flies the aircraft throughout. ICAO procedures expect RA compliance, so authority is *procedurally constrained* rather than structurally unconditional.
- **Recommendation-type scope changed?** **Yes, and nested monotonically with severity.** Per FAA AC 20-151A: Increase Descent RAs inhibited below 1650 ft AGL climbing / 1450 ft descending; Descend RAs inhibited below 1200 ft climbing / 1000 ft descending; all RAs inhibited below 1100 ft climbing / 900 ft descending; TAs inhibited below 600 ft climbing / 400 ft descending. Climb and Increase Climb RAs are inhibited on aircraft-performance and configuration grounds.
- **Runtime state-conditioned?** Yes, continuously, per encounter.
- **Human final authority invariant?** Partially. The pilot remains the actor and may deviate, but compliance is the procedural expectation, so this is weaker than the unconditional authority this work asserts.
- **Formal guarantee:** No published containment or monotonicity theorem over the advisory set. The inhibition schedule is a certified design table.
- **Empirical evaluation:** Extensive operational and encounter-model evidence, but not framed as a governance characterisation and with no binary-versus-graduated comparator.
- **Mechanism overlap:** Very high on the primary question. `externally measured state → banded classification → nested admissible advisory-type set → human decides` is instantiated in full, and the containment is monotone in the same direction: as the hazard band worsens, the admissible advisory set contracts and never expands.
- **Key distinction:** (i) the advisory generator is deterministic collision-avoidance logic, not a governed AI reasoning component — though note the proposed Layer 3 is itself a deterministic rule engine, which *weakens* rather than strengthens this distinction; (ii) the conditioning variable is a single scalar with configuration discretes, not a multi-component environmental classification `S = f(E)` aggregated by max-severity; (iii) inhibition is justified by manoeuvre feasibility and ground-proximity consequence, not by degradation of the evidential basis for a recommendation type; (iv) no formal containment property is stated or proved over the advisory set; (v) the mechanism is not abstracted, generalised, or presented as a governance construct.
- **Novelty threat:** **HIGH.**
- **Evidence:** FAA AC 20-151A, *Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II)*; SKYbrary, *TCAS II RA at Very Low Altitude*. External sources; **not currently in the project corpus** — must be added to `notes/` and `docs/canonical/citation-notes-map.md` before citation.
- **Wording allowed:** "Advisory-type inhibition conditioned on an externally measured state is established practice in certified collision-avoidance avionics, where resolution-advisory types are progressively inhibited as radio altitude decreases." · "This work specifies that pattern as a general governance abstraction with proved containment properties and characterises it empirically for AI decision support."
- **Wording prohibited:** any claim that runtime restriction of advisory types by external state is new, unprecedented, or unaddressed in prior work · "no existing system restricts what may be recommended" · presenting the CAUTION mode as the first realisation of graduated advisory scope.

### N-02 — ACAS X formally verified advisory logic

- **Family:** E / B.
- **Governed object:** advisory selection in the next-generation collision-avoidance system.
- **Runtime state source:** encounter state and altitude, resolved through an optimised lookup table.
- **Recommendation-type scope changed?** Yes — the safe advisory set is state-dependent.
- **Human authority invariant?** Partial, as N-01.
- **Formal guarantee:** **Yes.** Hybrid-systems safety proofs (KeYmaera X) and probabilistic model checking of the advisory logic have been published.
- **Empirical evaluation:** Yes, via encounter-model simulation.
- **Mechanism overlap:** Establishes that *formal verification of state-conditioned advisory admissibility* also has precedent. This removes "formal enforcement of advisory constraints" from the set of things this work can claim as new.
- **Key distinction:** verification targets collision-avoidance safety of specific manoeuvre advisories, not a general governance pair separating participation from advisory scope; there is no AI component being governed, and no abstraction over recommendation *types* as a governed set.
- **Novelty threat:** **HIGH** (against the formal-enforcement claim specifically).
- **Evidence:** Jeannin et al., *A formally verified hybrid system for safe advisories in the next-generation airborne collision avoidance system*, STTT; Von Essen & Giannakopoulou, probabilistic verification of ACAS X. External; not in corpus.
- **Wording allowed:** "Formal verification of state-conditioned advisory logic has precedent in airborne collision avoidance."
- **Wording prohibited:** "the first formal treatment of advisory admissibility" · "no prior work formally constrains what an advisory system may output".

### N-03 — Parasuraman, Sheridan & Wickens (2000), types and levels of automation

- **Family:** D.
- **Governed object:** the degree of automation applied to each of four stages — information acquisition, information analysis, decision and action selection, action implementation.
- **Runtime state source:** none. Levels are assigned at design time per function.
- **Recommendation-type scope changed?** Partially, and this is the sharp point: Level 2 "offers a complete set of decision/action alternatives", Level 3 "narrows the selection down to a few", Level 4 "suggests one alternative". The scale therefore already contains graduated restriction of what is presented to a human.
- **Human authority invariant?** Only at the lower levels; higher levels transfer execution to the computer.
- **Formal guarantee / empirical evaluation:** none / meta-analytic evidence exists on stages and levels.
- **Mechanism overlap:** the *idea* of a graduated presented-option space is long established in human-factors engineering.
- **Key distinction:** the scale narrows the *number of alternatives within a single decision*, not the *admissible recommendation types*; levels are a design-time taxonomy, not runtime state-conditioned; there is no environmental classifier, no containment property and no enforcement mechanism.
- **Novelty threat:** **MEDIUM-HIGH.**
- **Evidence:** Parasuraman, Sheridan & Wickens (2000), *IEEE Trans. SMC-A* 30(3), 286–297. External; not in corpus. **Should be added** — its absence is a material gap in the review given the contribution being claimed.
- **Wording allowed:** "Graduated restriction of the options presented to a human operator is long established in human-factors models of automation, where it is assigned at design time per function."
- **Wording prohibited:** "prior work does not consider restricting what is presented to the operator".

### N-04 — Adaptive automation / adaptive autonomy

- **Family:** D.
- **Governed object:** level of automation and dynamic task allocation.
- **Runtime state source:** operator physiological and cognitive state (ECG, EEG, eye tracking, workload, fatigue), task performance, task load, and mission/flight phase.
- **Recommendation-type scope changed?** No. A decade-scale human-factors review of adaptive autonomy describes no system that restricts recommendation option sets by an externally classified hazard state while preserving operator authority; the literature adjusts allocation and automation level.
- **Human authority invariant?** Generally yes at advisory levels, through manual intervention capability rather than curated option sets.
- **Formal guarantee:** none.
- **Mechanism overlap:** runtime switching of governance mode is established; the conditioning variable is predominantly the *human*, not the environment.
- **Key distinction:** conditions on operator state rather than externally classified environmental hazard; governs allocation rather than admissible advisory types; no formal enforcement.
- **Novelty threat:** MEDIUM.
- **Evidence:** USAARL-TECH-TR-2025-09, *Optimizing Adaptive Automation in Aviation*; Hancock-lineage adaptive-autonomy reviews. External; not in corpus.
- **Wording allowed:** "Adaptive automation switches governance mode at runtime, but predominantly on operator state rather than on a classification of the external environment."
- **Wording prohibited:** "no prior work changes governance at runtime".

### N-05 — Selective AI prediction in clinical decision-making

- **Family:** A.
- **Governed object:** which individual per-condition predictions are displayed to a clinician in a multilabel diagnostic setting; withheld items are replaced with "the model defers to you".
- **Runtime state source:** model accuracy / confidence — AI-internal.
- **Recommendation-type scope changed?** Partially. Predictions are withheld selectively per item rather than all-or-nothing, which is the closest thing in family A to a partial advisory space.
- **Human authority invariant?** Yes — clinicians made all final decisions.
- **Formal guarantee:** none; the study's finding is that the standard assumption of unchanged human behaviour under abstention fails, with false negatives increasing.
- **Mechanism overlap:** partial withholding of advisory content from a human decision-maker at runtime.
- **Key distinction:** conditioned on the model's own reliability, not on an external environmental state; the unit withheld is an instance-level prediction, not a recommendation *type* fixed by an admissibility contract; no formal containment; the contribution is a human-subjects finding, not an architecture.
- **Novelty threat:** MEDIUM.
- **Evidence:** *On the Limits of Selective AI Prediction: A Case Study in Clinical Decision Making*, arXiv:2508.07617 (2025). External; not in corpus.
- **Wording allowed:** "Selective prediction can withhold part of an advisory output from a human decision-maker, conditioned on the model's own estimated reliability."
- **Wording prohibited:** "abstention is always all-or-nothing" · any claim that partial withholding of advice is new. Note also that this source is direct evidence *against* assuming benign human response to scope restriction, and belongs in Limitations.

### N-06 — Punzi et al. (2024), learning-to-reject / learning-to-defer survey

- **Family:** A. Corpus paper [[notes]](../../notes/AI%2C%20Meet%20Human-%20Learning%20Paradigms%20for%20Hybrid%20Decision-Making%20Systems.md)
- **Governed object:** whether the machine predicts at all, or routes the instance to a human.
- **Runtime state source:** predicted accuracy / uncertainty; the deferral policy is binary `{0,1}`.
- **Recommendation-type scope changed?** No. There is no safety layer, no gate function, no state classification; the rejection threshold is a performance parameter.
- **Human authority invariant?** Yes.
- **Novelty threat:** LOW-MEDIUM — the canonical form of family A is participation gating, not scope restriction.
- **Wording allowed:** "In the selective-prediction and learning-to-defer literature the governed quantity is whether the machine predicts, conditioned on estimated predictive performance."
- **Wording prohibited:** treating this survey as evidence that no one restricts advisory content — N-05 sits inside this family and does.

### N-07 — Baxi (2026), Comprehension-Gated Agent Economy

- **Family:** E. Corpus paper [[notes]](../../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md)
- **Governed object:** an agent's executable economic permissions — trades, budgets, contracts, sub-agent spawning — as discrete tiers with nested permitted action sets.
- **Runtime state source:** verified adversarial robustness audits across three dimensions, combined by a weakest-link gate, with exponential decay and stochastic re-auditing. Agent-internal.
- **Recommendation-type scope changed?** No — these are executable permissions, not advice to a human.
- **Human authority invariant?** Not applicable; there is no human adviser loop.
- **Formal guarantee:** Yes — bounded economic exposure, monotonic safety scaling, incentive compatibility.
- **Mechanism overlap:** the closest *formal* parallel: a gate function mapping a vector to discrete tiers with nested permission sets and a proved monotonicity-analogue. Structurally isomorphic to `(G(S), A_AI(S))` with containment.
- **Key distinction:** orthogonal conditioning (agent robustness vs external environment) and a different governed object (executable action space vs advisory-type set presented to a human).
- **Novelty threat:** MEDIUM. Removes "graduated governance with proved nested containment" from the claimable set.
- **Citation caveat:** arXiv preprint, not peer reviewed. Cite as a formal comparison point only, per the extraction note.
- **Wording allowed:** "Formally proved graduated governance with nested permission sets has been proposed independently for AI economic agency, conditioned on agent robustness rather than environmental state."
- **Wording prohibited:** "the first formally proved graduated governance architecture" · "nested admissible sets are unique to this work".

### N-08 — Flehmig et al. (2024), traffic-light QA framework

- **Family:** E. Corpus paper [[notes]](../../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md)
- **Governed object:** supervisory response intensity — routine checks, thorough investigation, switch to deterministic backup.
- **Runtime state source:** an AI degradation index, banded green / orange / red.
- **Recommendation-type scope changed?** **No.** At green and orange the AI operates with identical unrestricted scope; the intermediate level changes what the human supervisor does.
- **Human authority invariant?** Yes.
- **Formal guarantee:** none.
- **Mechanism overlap:** tripartite classification with an intermediate band, structurally parallel to `S ∈ {SAFE, CAUTION, UNSAFE}`.
- **Key distinction:** the intermediate band governs the supervisor, not the advisory space. This is the corpus's clearest evidence that a traffic-light topology does not by itself produce advisory-scope differentiation — and it is the structure the C3 comparator instantiates, measured at `C1↔C3 = 0.00%`.
- **Novelty threat:** MEDIUM as a structural precedent; LOW against the advisory-scope claim.
- **Wording allowed:** "A three-level degradation index has been implemented in safety-critical AI quality assurance, where the intermediate level governs supervisory intensity rather than AI advisory scope."
- **Wording prohibited:** "the intermediate state is novel" · unqualified generalisation from the C3 result to all traffic-light systems.

### N-09 — Ghaleb et al. (2026), uncertainty-calibrated safety gating for VLA manipulation

- **Family:** B / E. Corpus paper [[notes]](../../notes/Uncertainty-Calibrated%20Safety%20Gating%20for%20Vision%E2%80%93Language%E2%80%93Action%20Manipulation%20Under%20Domain%20Shift-%20Reliability%20Gains%20and%20Intervention%E2%80%93Efficiency%20Trade-Offs.md)
- **Governed object:** physical execution behaviour across three regimes — proceed, pause-and-reobserve, hand off to a classical planner.
- **Runtime state source:** calibrated model failure risk, with hysteresis thresholds. AI-internal.
- **Recommendation-type scope changed?** No — the intermediate regime slows and re-senses; the policy's output scope is untouched.
- **Human authority invariant?** Not applicable — the fallback is a planner, not a human.
- **Formal guarantee:** explicitly none.
- **Mechanism overlap:** a realised three-regime runtime gate with an intermediate mode and hysteresis.
- **Key distinction:** intermediate risk is handled by physical degradation, a response available only to acting systems and unavailable to decision support; conditioning is on the model's own uncertainty.
- **Novelty threat:** MEDIUM.
- **Wording allowed:** "In embodied runtime assurance, intermediate risk is handled by execution deferral and re-sensing rather than by contracting an advisory space."
- **Wording prohibited:** describing this as advisory-scope governance.

### N-10 — Kwon et al. (2025), Adaptive Shielding

- **Family:** C. Corpus paper [[notes]](../../notes/Runtime%20Safety%20through%20Adaptive%20Shielding-%20From%20Hidden%20Parameter%20Inference%20to%20Provable%20Guarantees.md)
- **Governed object:** the executable action set of an RL policy, filtered per candidate action by a SafetyScore.
- **Runtime state source:** online inference of hidden dynamics parameters; the cost function explicitly separates agent-centric and **environment-centric** features.
- **Recommendation-type scope changed?** No. Environmental features modulate a continuous safety boundary, not a discrete governance mode; there is no intermediate state.
- **Novelty threat:** LOW-MEDIUM. The nearest shielding work to environment-conditioned governance, but the governance remains binary per action.
- **Wording allowed:** "Shields can adapt to environmental features at runtime, but the resulting decision remains binary per candidate action."

### N-11 — Shielding and action masking

- **Family:** C. Corpus papers include [[notes]](../../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md)
- **Governed object:** the executable action set of an agent, restricted per state against a safety specification. `state → admissible action set` is the defining pattern of this family and is thoroughly established.
- **Human authority invariant?** Not applicable — no human decision-maker in the loop.
- **Novelty threat:** LOW against the advisory claim, but decisive against any claim that state-conditioned admissible-set restriction is itself new.
- **Wording allowed:** "State-conditioned restriction of an admissible *action* set is well established in shielding and safe reinforcement learning."
- **Wording prohibited:** "conditioning an admissible set on runtime state is novel".

### N-12 — Shamsujjoha et al. (2025), Swiss Cheese guardrail taxonomy

- **Family:** C / E. Corpus paper [[notes]](../../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md)
- **Governed object:** thirteen guardrail actions over fourteen pipeline stages and artefacts.
- **Runtime state source:** configured per artefact and quality attribute; the context-dependent rule type adjusts on data or deployment context, not on classified environmental hazard.
- **Mechanism overlap:** the definitive catalogue of governance *options*; it lacks a state-conditioned *selection* mechanism.
- **Novelty threat:** LOW-MEDIUM.
- **Wording allowed:** "The guardrail literature catalogues runtime governance actions without specifying a mechanism that selects among them by classified environmental state."

### N-13 — FDA non-device Clinical Decision Support, Criterion 3

- **Family:** E (regulatory).
- **Governed object:** the permissible *form* of output — a list of options or a prioritised list, versus a specific preventive, diagnostic or treatment directive.
- **Runtime state source:** none. This is a design-time determination of intended purpose, fixed regardless of clinical context.
- **Recommendation-type scope changed?** **Yes in kind, no in mechanism.** The distinction between recommendation types is regulatorily load-bearing, which independently motivates treating recommendation type as a governed quantity — but it is applied once, to the software, not per encounter.
- **Human authority invariant?** Yes — Criterion 4 requires the professional to be able to review the basis independently and not rely primarily on the software.
- **Novelty threat:** MEDIUM — supportive rather than threatening. It corroborates that *which type of recommendation is offered* is a meaningful safety-governance variable.
- **Evidence:** FDA, *Clinical Decision Support Software: Guidance for Industry and FDA Staff*. External; not in corpus.
- **Wording allowed:** "Regulatory practice already distinguishes advisory outputs by type — a list of options versus a specific directive — and attaches different oversight consequences to each, though as a static classification of intended purpose rather than a runtime mechanism."
- **Wording prohibited:** claiming FDA guidance as an architectural precedent or as evidence of a runtime mechanism.

### N-14 — Runtime governance for autonomous AI agents (2026 preprints)

- **Family:** E.
- **Governed object:** executable agent actions and tool invocations, intercepted before execution.
- **Runtime state source:** the execution path itself, and agent-internal drift, disparity and sequential-pattern signals.
- **Human authority invariant?** No — in one framework human approval is explicitly "an action that a governance mechanism can invoke", not a structural invariant.
- **Formal guarantee:** one carries a monotone "tighten-only" admissibility property and a viability-kernel result; neither reports empirical evaluation.
- **Mechanism overlap:** monotone graduated restriction of an admissible set, again over executable actions.
- **Novelty threat:** LOW-MEDIUM.
- **Evidence:** arXiv:2603.16586; arXiv:2604.24686. External preprints, no empirical evaluation; cite with caution or not at all.
- **Wording allowed:** "Recent runtime-governance proposals for autonomous agents apply monotone restriction to executable action spaces conditioned on agent-internal signals."

### N-15 — Feng et al. (2025), Levels of Autonomy for AI Agents

- **Family:** D. Corpus paper [[notes]](../../notes/Levels%20of%20Autonomy%20for%20AI%20Agents.md)
- **Governed object:** an autonomy-level designation.
- **Runtime state source:** none — levels are fixed deployment-time constants.
- **Novelty threat:** LOW. Its value is the design-time versus runtime distinction.

---

## Families for which no material equivalence was found

| Family | Finding |
|---|---|
| A — selective prediction / abstention / deferral | Canonical form gates *participation*. One instance (N-05) withholds advisory content selectively, conditioned on model reliability rather than external state. No formal containment. |
| B — runtime assurance / Simplex | Governs control authority and switching to a verified backup controller. Advisory scope is not the governed object; ACAS X (N-02) is the exception and sits in family E. |
| C — shielding / action masking | `state → admissible action set` is fully established, over *executable* actions for an acting agent, with no human adviser loop. |
| D — adjustable autonomy / mixed-initiative | Graduated presented-option restriction exists at design time (N-03); runtime adaptation exists but conditions predominantly on operator state (N-04). |
| E — graduated runtime governance | **Material equivalence found at N-01/N-02.** Research-literature instances (N-07, N-08, N-14) govern executable actions or supervisory intensity. |

---

## Corpus gaps identified

The following prior works bear directly on the claimed contribution and are **not in the project corpus**. They must be added to `notes/` and registered in `docs/canonical/citation-notes-map.md` before the manuscript cites them.

| Work | Family | Why required |
|---|---|---|
| FAA AC 20-151A / TCAS II inhibition logic | E | The material-equivalence finding. Cannot be omitted from Related Work. |
| ACAS X formal verification (Jeannin et al.) | E / B | Removes the formal-enforcement novelty claim. |
| Parasuraman, Sheridan & Wickens (2000) | D | Canonical LOA reference; its absence is a material review gap given the contribution claimed. |
| Adaptive-autonomy human-factors review | D | Establishes the operator-state conditioning norm. |
| Selective AI prediction in clinical decision making (arXiv:2508.07617) | A | Closest family-A instance; also evidence for Limitations. |
| FDA CDS guidance, Criterion 3 | E | Corroborates recommendation type as a governed variable. |

---

## Provenance

Coding was performed against corpus extraction notes and, for the six works above, against the cited external sources. No claim in this matrix depends on an unverified reference. Empirical figures from the project's own evidence base are not restated here; see `data/journal1-manuscript-evidence-sync/quantitative-provenance.csv`.
