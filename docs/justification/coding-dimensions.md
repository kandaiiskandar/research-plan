# Coding Dimensions: Origin, Derivation, and Adequacy

**Date:** 2026-09-07
**Purpose:** Explain where the four coding dimensions in TABLE I of the IPSci 2026 manuscript come from, why these four (and not others), and how each dimension's allowed values were enumerated. This document is self-contained: every source referenced is fully cited in §7 at the end. No inline links to other project files are used; the argument stands on its own.
**Audience:** Supervisor review; viva-defence backup for the reviewer question *"Why these coding dimensions?"*

---

## 1. Statement of the four dimensions

The IPSci 2026 manuscript reports that the reviewed corpus was assessed against four dimensions, presented as TABLE I of the manuscript:

**TABLE I. Coding dimensions applied to all reviewed papers.**

| Dimension | Allowed values |
|---|---|
| Primary governance target | Participation · Advisory scope · Execution · Oversight |
| Runtime adaptation | Binary (on/off) · Graduated (3+ levels) · None |
| Conditioning variable | Environmental state · AI robustness · Task risk · Human authority · None |
| Recommendation restriction | Yes (bounded output set) · No |

This document explains where each dimension came from, why the values inside it are what they are, and why the four together are jointly necessary and sufficient for the differentiation claim the manuscript makes against prior work.

---

## 2. Derivation from the formal architecture

The proposed graduated safety-state-gated architecture is defined by five formal objects (fully specified in the thesis Appendix C):

- **E** — the environmental observation vector, E = {w, r, m, o, v, t} (wind, rainfall, marine warning level, ocean state, vessel category, time of day).
- **S = f(E)** — a deterministic classifier mapping E onto three discrete safety states {SAFE, CAUTION, UNSAFE}.
- **G(S) ∈ {0, 1}** — the participation gate: whether the AI is allowed to participate at all under state S.
- **A_AI(S) ⊆ R** — the admissible recommendation space: the subset of recommendation types R the AI is permitted to produce under state S.
- **Safety Dominance Property: AI(E) ⊆ A_AI(f(E))** — the AI's output must always fall within the admissible space defined by the current safety state.

A prior work is *equivalent* to the proposed architecture if and only if it satisfies four independent conditions, each derived directly from one of the formal objects above:

| Equivalence question the prior work must answer | Which formal object it interrogates | Coding dimension that captures the answer |
|---|---|---|
| Which of {G(S), A_AI(S)} does the mechanism govern? | G(S) and A_AI(S), plus adjacent targets (execution-time filtering, human-oversight allocation) that neither of these captures | **Primary governance target** |
| Is the mechanism binary, or graduated across a discrete-state structure? | The three-valued codomain of S = f(E) | **Runtime adaptation** |
| Does the mechanism condition on classified environmental state, or on something else? | The domain of the classifier f — is it E, or something entirely different? | **Conditioning variable** |
| Does the mechanism define a bounded output set, or does it only check outputs post-hoc? | The set structure of A_AI(S) — is A_AI ⊂ R, or does the mechanism operate without a bounded A_AI? | **Recommendation restriction** |

The four dimensions are therefore not a convenience choice from a general-purpose taxonomy. Each is the coding-time proxy for one of the four questions that the formal architecture forces on any comparator. A prior work matching on all four dimensions matches the architecture; a prior work differing on any single dimension is structurally different in a formally identifiable way. §5 makes this necessary-and-sufficient claim explicit and defends it.

---

## 3. Per-dimension rationale

### 3.1 Primary governance target

**Values:** Participation · Advisory scope · Execution · Oversight

**Why this dimension exists.** The formal architecture defines two governance functions that operate *before* AI output is generated: G(S) (whether the AI participates) and A_AI(S) (what it may recommend). A prior work's primary governance target is the coding-time proxy for which of these (if any) it implements. The dimension is required because governance mechanisms in the reviewed literature target different points in the AI pipeline, and equivalence with the proposed architecture requires targeting either G or A_AI, not adjacent points.

**Why these four values.** The value labels come from exhaustive enumeration of governance targets observed across the reviewed corpus:

- **Participation** — the mechanism decides whether the AI acts at all. Reference implementations: shields formalised by Könighofer et al. [8]; the safety filter of Bajcsy and Fisac [10]; the Guaranteed Safe AI framework of Dalrymple et al. [9].
- **Advisory scope** — the mechanism restricts what the AI may recommend by defining a bounded admissible set before generation. In the reviewed corpus this label is populated only by the proposed architecture; guardrail systems such as the Swiss Cheese taxonomy of Shamsujjoha et al. [6] restrict outputs but not the recommendation *type space*, and are therefore coded under Execution rather than Advisory scope.
- **Execution** — the mechanism filters, blocks, or replaces the AI's output after it has been generated. References: Tumato 2.0 [14]; Pro2Guard [31]; the majority of mitigations in the OWASP Top 10 for Agentic Applications 2026 [S6].
- **Oversight** — the mechanism regulates the intensity of human supervisory attention rather than AI behaviour itself. References: the traffic-light degradation index of Flehmig et al. [7]; the GAIE framework of Kang [22].

No fifth value was required. Every prior work identified in the corpus fell into one of these four categories, cross-checked against the anchor systematic reviews of Ramos et al. [11] (91 papers, 6 industries) and Perez-Cerrolaza et al. [21] (294 references across automotive, aviation, and industrial domains).

### 3.2 Runtime adaptation

**Values:** Binary (on/off) · Graduated (3+ levels) · None

**Why this dimension exists.** The formal architecture's classifier S = f(E) has a three-valued codomain {SAFE, CAUTION, UNSAFE}, making it a graduated (specifically ternary) governance mechanism. A prior work's runtime adaptation value distinguishes whether it, too, is graduated or whether it collapses to a binary decision (or has no runtime governance at all). The dimension is required because the CAUTION mode (the manuscript's core novelty) is unreachable without at least three governance states.

**Why these three values.**

- **Binary (on/off)** — two-valued: the mechanism permits the action, or replaces / blocks it. Reference: Könighofer et al.'s shields [8]. Refined variants (verification-guided shielding of Corsi et al. [S2]) remain binary in their governance decision. The universality of binary governance in the shielded-RL literature is confirmed by the systematic review of Odriozola-Olalde et al. [S3].
- **Graduated (3+ levels)** — three or more discrete governance modes. References: the traffic-light index of Flehmig et al. [7] (three levels); Baxi's K-tier permission architecture [13] (K discrete tiers); Kang's GAIE three-tier oversight [22]; Sahoo's five-level agent-action-class scheme [23]. All graduated systems in the reviewed corpus govern *something other than advisory scope*, which is what makes the proposed architecture novel on the joint reading of dimensions 3.1 and 3.2.
- **None** — no runtime governance component; the paper concerns design-time properties only. Reference: Feng, McDonald and Zhang's Levels of Autonomy for AI Agents [12] — a design-time authority-allocation framework whose two governance dimensions (agency and autonomy) are configured before deployment and do not vary at runtime.

The lower bound "3+" for the Graduated value comes directly from the codomain size of S = f(E). Two-valued mechanisms are Binary; three or more discrete modes count as Graduated, regardless of whether they number three (Flehmig), four, five (Sahoo), or K (Baxi).

### 3.3 Conditioning variable

**Values:** Environmental state · AI robustness · Task risk · Human authority · None

**Why this dimension exists.** The proposed architecture's governance functions are conditioned specifically on the classifier output S = f(E), where E is a vector of *observable environmental parameters*. A prior work with the same structural governance shape but conditioned on a different variable is not equivalent. The closest such case is Baxi's Comprehension-Gated Agent Economy [13], which uses the identical containment structure but conditions on verified agent robustness rather than environmental state. This dimension makes that difference explicit in the coding.

**Why these five values.** The value labels enumerate the conditioning variables actually observed across the reviewed literature:

- **Environmental state** — the governance function is triggered by observable properties of the operating environment. Closest reviewed near-miss: the adaptive shielding framework of Kwon et al. [S1], whose SafetyScore incorporates environment-centric features E ∈ ℝⁿ² but remains binary in its governance decision. Cited in the thesis Chapter 2 §2.4 as the closest architectural precedent to the proposed work.
- **AI robustness** — the governance function is triggered by properties of the AI system itself (verified accuracy, degradation metrics, robustness certifications). References: Baxi's K-tier CGAE [13] (verified agent robustness); Flehmig et al.'s degradation index [7] (AI performance monitoring, not environmental state).
- **Task risk** — the governance function is triggered by properties of the task at hand (regulatory impact, criticality classification). Reference: Kang's GAIE tiers [22], which cascade code generation across three oversight tiers based on task regulatory impact.
- **Human authority** — the governance function is set by allocated roles rather than by any runtime measurement. Reference: Feng et al.'s Levels of Autonomy [12].
- **None** — the mechanism has no runtime conditioning variable (typically because it has no runtime component at all).

The dimension is exhaustive within the reviewed set. Cross-checked against the anchor systematic reviews (Ramos et al. [11], Perez-Cerrolaza et al. [21], and the formal-methods SLR by Newcomb & Ochoa [S5], which covers 46 studies across five years and eight categories of formal methods), no conditioning variable outside these five was identified.

### 3.4 Recommendation restriction

**Values:** Yes (bounded output set) · No

**Why this dimension exists.** The Safety Dominance Property AI(E) ⊆ A_AI(f(E)) requires that A_AI be a *defined bounded set* the AI cannot generate outside. A prior work that restricts individual outputs (a guardrail that blocks specific unsafe generations) but does not define a bounded output type space is not equivalent — it enforces safety per-output rather than by pre-hoc scope containment. This dimension is the single most discriminating coding: the vast majority of the reviewed corpus scores No.

**Why binary.** *Bounded* is a set-theoretic property that admits only two values: either A_AI is a defined subset of the recommendation type space R, or it is not. There is no meaningful intermediate value.

- **Yes (bounded output set)** — the mechanism defines the admissible recommendation type space *before* the AI reasons. Positive case in the reviewed corpus: the proposed architecture itself. The closest formal analogue is CRANE [S4], whose augmented grammar G_a = R_M·G produces a containment relationship over token sequences that is structurally analogous to A_AI(CAUTION) ⊂ A_AI(SAFE); however, CRANE's alternation between constrained and unconstrained generation is syntactically triggered by delimiter tokens rather than conditioned on classified environmental state, so it is coded Yes on this dimension but not equivalent on dimension 3.3.
- **No** — the mechanism operates on individual outputs after generation, or does not restrict outputs at all. This includes every shield, safety filter, guardrail, and post-hoc validator identified in the corpus.

---

## 4. Consolidated mapping: dimension → formal component → equivalence question

| Coding dimension | Formal component it discriminates | Equivalence question |
|---|---|---|
| Primary governance target | G(S), A_AI(S), and adjacent target points | Which formal governance function does the mechanism implement? |
| Runtime adaptation | Codomain of S = f(E) | Does the mechanism have the tripartite (or larger) mode structure required for a CAUTION analogue? |
| Conditioning variable | Domain of f — is it E, or something else? | Is governance conditioned on classified environmental state? |
| Recommendation restriction | Set structure of A_AI(S) — bounded or not? | Does the mechanism enforce Safety Dominance by construction (pre-hoc), or only per-output (post-hoc)? |

Matching all four rows on the right-hand column is the operational definition of *equivalence with the proposed architecture* used throughout the review. It is the criterion the manuscript's absence claim ("no reviewed system implements the two-level governance pair conditioned on classified environmental safety state") is measured against.

---

## 5. Joint adequacy: why four dimensions are necessary and sufficient

### Necessary

Dropping any single dimension leaves a class of prior works that could pass the reduced coding and yet not be equivalent to the proposed architecture:

- **Drop Primary governance target** → Baxi's CGAE [13] passes (it is graduated, uses a specific conditioning variable, and defines a bounded permission set) but is not equivalent because its governance target is execution-time permission enforcement rather than advisory-scope restriction.
- **Drop Runtime adaptation** → Shamsujjoha et al.'s multi-layered guardrails [6] pass (they can be argued to target output restriction, condition on content, and are bounded per-rule) but are not equivalent because they are binary per-action rather than graduated across a discrete-state structure.
- **Drop Conditioning variable** → Baxi's CGAE [13] passes again, on the same reasoning as above, plus scope restriction; the CGAE containment structure E(T_k) ⊂ E(T_{k+1}) is a formal analogue of A_AI(CAUTION) ⊂ A_AI(SAFE), but the tier T is conditioned on agent robustness, not environmental state. Without this dimension, the coding cannot distinguish the two.
- **Drop Recommendation restriction** → Kwon et al.'s adaptive shielding [S1] passes on adaptation (via runtime shield adjustment) and conditioning (via environment-centric features E ∈ ℝⁿ²) but is not equivalent because its SafetyScore is binary and it does not define a bounded A_AI at all.

Each dimension carries a specific discriminating load; none is redundant.

### Sufficient

A prior work matching all four values as the proposed architecture requires — Primary governance target = **Advisory scope**; Runtime adaptation = **Graduated (3+ levels)**; Conditioning variable = **Environmental state**; Recommendation restriction = **Yes** — is by construction an architecture that governs advisory scope via a graduated function of classified environmental state with a bounded admissible recommendation space. That is exactly the proposed architecture. No fifth dimension is required to identify equivalence, and none of the reviewed comparators satisfies all four.

The sufficiency claim is a *coverage* claim about the reviewed set, not a formal proof over all possible architectures; it can be tested against any prior work by trying to construct a counter-example.

---

## 6. Relationship to the seven-dimension comparison matrix (thesis Chapter 2 Table 2.1)

The thesis Chapter 2 uses a *different* set of dimensions — seven — to build the primary-comparator differentiation matrix (Table 2.1 of the thesis). The seven dimensions are: Safety Gate · Adaptive Autonomy · AI Participation Controlled (L1) · Advisory Scope Restricted (L2) · Unified Governance · Formal Model · Domain. Two dimension sets exist because they serve different roles and are applied at different stages of the review.

| Aspect | Four coding dimensions (this document, manuscript TABLE I) | Seven comparison dimensions (thesis Chapter 2 Table 2.1) |
|---|---|---|
| When applied | Extraction time — as each paper is read | Analysis time — during Chapter 2 drafting |
| Granularity | Coarse — 4 questions, small value sets | Fine — 7 questions, per-comparator Yes / Partial / No |
| Scope | All papers assessed during extraction | 18 primary comparators |
| Function | Classify papers into paradigms and identify which of {SAFE gate / L2 restriction / graduated adaptation} they exemplify | Establish per-paper which formal component the comparator matches or fails to match |
| Overlap | *Primary governance target* ≈ L1 + L2 combined; *Runtime adaptation* ≈ Adaptive Autonomy; *Recommendation restriction* ≈ L2; *Conditioning variable* — no direct one-to-one equivalent (partially subsumed within Unified Governance) | The seven dimensions elaborate the four into per-formal-component discriminators |

Both taxonomies are internally coherent and mutually consistent: a paper coded *Advisory scope + Yes + Graduated* under the four-dimension scheme will code L2 = Yes and Unified Governance = Yes under the seven-dimension matrix. The four-dimension set is the coarse extraction-time filter; the seven-dimension set is the fine-grained architectural comparison for the 18 papers that survived to comparator status. The seven-dimension set is separately justified in a companion document; this document covers only the four-dimension set.

---

## 7. Sources

All sources referenced above, in full bibliographic form. Reference numbers [1]–[35] match the numbering used in the IPSci 2026 manuscript; supplementary items [S1]–[S6] are papers or standards cited in the thesis Chapter 2 or the notes that were not carried into the manuscript reference list, and are given in full here so this document remains self-contained.

### Cited from the IPSci 2026 manuscript reference list

- **[6]** Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE 22nd Int. Conf. Software Architecture (ICSA)*, 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014
- **[7]** N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024: 50th Annual Conf. IEEE Industrial Electronics Society*, 2024. doi: 10.1109/IECON55916.2024.10906021
- **[8]** B. Könighofer et al., "Shields for safe reinforcement learning," *Communications of the ACM*, vol. 68, no. 11, pp. 80–90, 2025. doi: 10.1145/3715958
- **[9]** D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint* arXiv:2405.06624, 2024.
- **[10]** A. Bajcsy and J. F. Fisac, "Human–AI safety: A descendant of generative AI and control systems safety," *arXiv preprint* arXiv:2405.09794, 2024.
- **[11]** I. F. Ramos, G. Gianini, M. C. Leva, and E. Damiani, "Collaborative intelligence for safety-critical industries: A literature review," *Information*, vol. 15, no. 11, p. 728, 2024. doi: 10.3390/info15110728
- **[12]** Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents," *arXiv preprint* arXiv:2506.12469, 2025.
- **[13]** A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for AI economic agency," *arXiv preprint* arXiv:2603.15639, 2026.
- **[14]** J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe and robust robot behavior," *Annals of Mathematics and Artificial Intelligence*, vol. 93, pp. 541–567, 2025. doi: 10.1007/s10472-024-09949-3
- **[21]** J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J. Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," *ACM Computing Surveys*, vol. 56, no. 7, article 176, 2024. doi: 10.1145/3626314
- **[22]** R. Kang, "Governed AI-assisted engineering: Graduated human oversight for agentic code generation in regulated domains," *arXiv preprint* arXiv:2606.22484v2 [cs.HC], Jul. 2026.
- **[23]** S. Sahoo, "The controllability trap: A governance framework for military AI agents," in *Proc. ICLR 2026 Workshop on Agents in the Wild*, Mar. 2026. arXiv:2603.03515.
- **[31]** H. Wang, C. M. Poskitt, J. Sun, and J. Wei, "Pro2Guard: Proactive runtime enforcement of LLM agent safety via probabilistic model checking," *arXiv preprint* arXiv:2508.00500, 2025.

### Cited as supplementary (not in the manuscript reference list; used in the thesis Chapter 2)

- **[S1]** M. Kwon, T. Ingebrand, U. Topcu, and L. Feng, "Adaptive shielding for safe reinforcement learning under hidden-parameter dynamics shifts," *arXiv preprint* arXiv:2506.11033v2, 30 Jan. 2026 (v1 Jun. 2025).
- **[S2]** D. Corsi, G. Amir, A. Rodríguez, C. Sánchez, G. Katz, and R. Fox, "Verification-guided shielding for deep reinforcement learning," in *Proc. 1st Reinforcement Learning Conference (RLC)*, 2024. doi: 10.48550/arXiv.2406.06507
- **[S3]** H. Odriozola-Olalde, M. Zamalloa, and N. Arana-Arexolaleiba, "Shielded reinforcement learning: A review of reactive methods for safe learning," in *Proc. 2023 IEEE/SICE Int. Symp. System Integration (SII)*, 2023. doi: 10.1109/SII55687.2023.10039301
- **[S4]** D. Banerjee, T. Suresh, S. Ugare, S. Misailovic, and G. Singh, "CRANE: Reasoning with constrained LLM generation," in *Proc. 42nd Int. Conf. Machine Learning (ICML)*, Vancouver, Canada, 2025. PMLR 267. arXiv:2502.09061v4 [cs.PL]
- **[S5]** A. Newcomb and O. Ochoa, "Formal methods for safety-critical machine learning: A systematic literature review," *Frontiers in Artificial Intelligence*, vol. 9, art. 1749956, 18 Feb. 2026. doi: 10.3389/frai.2026.1749956
- **[S6]** OWASP GenAI Security Project — Agentic Security Initiative (J. Sotiropoulos, K. Katz, R. F. Del Rosario, leads), *OWASP Top 10 for Agentic Applications 2026*, Version 2026, Dec. 2025. Available: genai.owasp.org. Licence: CC BY-SA 4.0.

---

## 8. Provenance and limitations

**Provenance.** The formal-derivation argument in §2 and §4 was constructed on 2026-09-07 as part of building the review-protocol audit trail. Prior to this document, the four dimensions appeared in the manuscript (TABLE I), the master coding table (Table 3a), and the review protocol (§Coding) as facts about the coding, without a written derivation. This document supplies the derivation.

The per-dimension rationales in §3 draw on the coding rules actually used at extraction time; where those rules were not formally documented at the time, the rationale reconstructs the intended reasoning from the observed coding outputs (visible in the thesis Chapter 2 Table 2.1, in the master coding table, and in the extraction notes for individual papers).

**Limitations.**
- The joint-adequacy argument in §5 is a coverage claim about the reviewed corpus. A prior work outside the reviewed corpus that matches all four dimensions and is nevertheless not equivalent would refute sufficiency. No such counter-example is currently known, but the argument is not a formal proof over all possible architectures; it is a structural claim about the reviewed set.
- The correspondence table in §6 uses "≈" for the mapping between the four-dimension and seven-dimension sets. The correspondence is close but not identity — a rigorous cross-walk would require inspecting every per-paper coding under both schemes.
- The Conditioning-variable dimension has no direct one-to-one equivalent in the seven-dimension set; the seven-dimension matrix folds this into "Unified Governance" alongside the pairing of L1 and L2. This is a known asymmetry between the two taxonomies rather than an inconsistency.
