# Paper Extraction: CRANE — Reasoning with Constrained LLM Generation

**Citation:** Banerjee, D., Suresh, T., Ugare, S., Misailovic, S., & Singh, G. (2025). CRANE: Reasoning with constrained LLM generation. *Proceedings of the 42nd International Conference on Machine Learning (ICML)*, Vancouver, Canada. PMLR 267.

**Persistent Identifier:** arXiv:2502.09061v4 [cs.PL]

**Relevance Score:** ⭐⭐⭐⭐ (High)

---

## Section 1: Core Problem Statement

The paper addresses a fundamental tension in constrained LLM generation: enforcing syntactic correctness via formal grammar constraints on LLM outputs (e.g., for code generation, symbolic math, logical reasoning) empirically degrades the model's *functional* correctness — i.e., its reasoning capabilities. Prior work (Tam et al. 2024) observed this empirically but lacked a formal explanation. CRANE poses two research questions: (RQ1) Do LLMs truly lose reasoning capabilities under constrained decoding? (RQ2) How can constrained decoding's syntactic benefits be preserved while maintaining unconstrained reasoning capabilities?

## Section 2: Methodological Approach

Design Science / Formal Methods hybrid. The paper combines:
1. **Theoretical analysis** via circuit complexity classes and Turing machine simulation to formally characterise *why* constrained decoding reduces expressivity.
2. **Algorithm design** — CRANE (Constrained Reasoning Augmented Generation), a practical decoding algorithm that alternates between unconstrained generation (for reasoning) and constrained generation (for structurally correct outputs).
3. **Empirical evaluation** on GSM-Symbolic (math reasoning) and FOLIO (first-order logic reasoning) benchmarks across 9 open-source LLMs.

## Section 3: Key Theoretical Constructs

### 3a. Constrained Decoding Expressivity Limitation (Proposition 3.1)
For any log-precision LLM with constant layers, when the output grammar G_c defines a finite language L(G_c) (e.g., binary decision {0,1}), the constrained output can be computed by a logspace-uniform constant-depth threshold circuit (TC⁰). This means constrained decoding reduces the LLM's problem-solving capability to TC⁰ — a restrictive circuit complexity class. Problems outside TC⁰ (e.g., st-connectivity, which is NL-complete) become unsolvable under constrained decoding, even though the same LLM can solve them unconstrained.

**Root cause identified:** Restrictive output grammars permit only constant-length outputs, collapsing the LLM to a single (or constant number of) autoregressive steps, which eliminates the intermediate reasoning chain that gives LLMs their expressive power.

### 3b. Augmented Grammar Restoration (Proposition 3.3)
For any Turing machine M and valid output grammar G, there exists an augmented grammar G_a of the form G_a → R_M G, where R_M captures reasoning step encodings and G captures the final output. Under G_a, a constant-depth LLM can simulate t(n) steps of M using t(n) autoregressive steps — i.e., full expressivity is restored. The key insight: the grammar must accommodate intermediate reasoning tokens, not just final output tokens.

### 3c. CRANE Algorithm (Algorithm 1)
- Takes an LLM, a constrained decoding algorithm (CSD), output grammar G, and delimiter symbols S₁ (start) and S₂ (end) as input.
- Augments G to G' = S₁GS₂.
- Begins in **unconstrained mode** (free reasoning).
- When S₁ is detected in the generation window, switches to **constrained mode** (grammar-enforced output).
- When S₂ is detected, switches back to **unconstrained mode**.
- This allows multiple constrained/unconstrained windows within a single generation.

## Section 4: Key Findings / Results

### GSM-Symbolic (Table 1)
- CRANE consistently outperforms both unconstrained CoT and constrained generation across all 9 models.
- Best improvement: DeepSeek-R1-Distill-Llama-8B — CRANE achieves 31% accuracy vs. 21% (unconstrained CoT) and 13% (constrained), a +10/+18 percentage point gain.
- Qwen2.5-Math-7B-Instruct: CRANE 38% vs. constrained 29% vs. unconstrained CoT 29%.
- CRANE achieves near-perfect parse rates (94–100%) while maintaining reasoning capability.
- Unconstrained CoT produces 10% syntax errors on average; CRANE eliminates nearly all.

### FOLIO (Table 2)
- Llama-3.1-8B-Instruct: CRANE 46.31% vs. constrained 39.41% vs. unconstrained CoT 32.02%.
- Qwen2.5-7B-Instruct: CRANE 42.36% vs. constrained 37.44% vs. unconstrained CoT 36.95%.
- CRANE maintains high compilation rates (~86–88%) comparable to pure constrained generation.

### Token Overhead
- CRANE generates slightly more tokens than constrained generation (due to reasoning chains) but comparable to unconstrained CoT.
- The overhead is modest: typically 5–20 additional tokens over unconstrained CoT.

## Section 5: Formal Governance / Safety Architecture Analysis

**Level 1 governance (participation control — G(S)):** Not directly addressed. The paper operates at the output-level constraint enforcement layer, not at the system participation layer.

**Level 2 governance (advisory scope restriction — A_AI(S)):** The paper's core contribution is directly relevant. CRANE implements a form of *dynamic advisory scope governance* at the output level:
- **Unconstrained windows** = unrestricted advisory scope (full reasoning capability).
- **Constrained windows** = restricted advisory scope (output must conform to grammar G).
- The transition between modes is delimiter-triggered, not environmental-state-conditioned.

**Mapping to dissertation constructs:**
| CRANE Construct | Dissertation Construct | Alignment |
|---|---|---|
| Output grammar G | A_AI(S) restriction on admissible outputs | Structural analogue — both restrict the set of permissible AI outputs |
| G_a = R_M · G (augmented grammar) | CAUTION mode with restricted-but-non-empty advisory scope | Conceptual parallel — both allow intermediate processing while restricting final output |
| Delimiter-triggered mode switching | S = f(E) state classification triggering governance mode | Different conditioning variable (syntactic delimiter vs. environmental state) |
| Proposition 3.1 (expressivity loss under restrictive G) | Theoretical motivation for why binary governance (full/none) is suboptimal | Strong indirect support |

## Section 6: Gap Analysis — Binary vs. Graduated Governance

**Binary governance present?** Yes — the baseline "constrained decoding" is a binary mechanism: every output token is either grammar-permitted or grammar-blocked. There is no intermediate mode.

**Graduated governance present?** CRANE introduces a *two-mode* alternation (unconstrained/constrained) but this is **not** a graduated governance architecture in the dissertation's sense:
- CRANE's modes are **syntactically triggered** (by delimiter symbols), not **environmentally conditioned**.
- There is no intermediate CAUTION-equivalent mode — CRANE switches between full constraint enforcement and no constraint enforcement.
- There is no unified governance pair (G(S), A_AI(S)) conditioned on a classified environmental state.
- The "graduation" is temporal (within a single generation sequence), not state-conditional.

**Gap confirmed:** CRANE does not implement environmental-state-conditioned graduated governance. It does, however, provide the strongest formal theoretical foundation for *why* binary output restriction degrades AI reasoning capability — which is a powerful theoretical motivation for the CAUTION mode.

## Section 7: Environmental State Representation

No environmental state vector. The paper operates in a pure NLP/formal-methods domain. The "state" that triggers mode switching is the presence of delimiter tokens in the generation stream, not an external environmental classification.

## Section 8: Relevance to Safety Dominance Property

**Indirect but significant.** The Safety Dominance Property requires AI(E) ⊆ A_AI(S). CRANE's constrained decoding enforces an analogous set containment: during constrained windows, the LLM's output is guaranteed to be in L(G) — i.e., the actual output is a subset of the grammar-defined admissible set. This is a syntactic analogue of the Safety Dominance Property operating at the token/output level rather than the advisory-scope level.

Proposition 3.1 also provides a formal *cost* of overly restrictive containment: if A_AI(S) is too small (analogous to L(G_c) being finite/restrictive), the AI loses its problem-solving capability entirely. This is direct theoretical motivation for the CAUTION mode — a restricted-but-non-empty advisory scope that preserves reasoning while constraining output.

## Section 9: Relevance to CAUTION Mode Design

**High relevance as theoretical motivation.** The augmented grammar construction G_a = R_M · G is the formal analogue of the CAUTION mode's design principle: allow reasoning/processing within a constrained scope, then restrict the final output. Key parallels:
- G_a permits reasoning tokens (R_M) followed by restricted output tokens (G) — CAUTION permits advisory generation within a restricted recommendation space.
- Proposition 3.3 proves that this structure preserves full computational expressivity — analogous to claiming that CAUTION preserves decision support quality while restricting scope.
- The paper proves that the *binary alternative* (pure constrained = UNSAFE-equivalent full restriction, or pure unconstrained = SAFE-equivalent no restriction) is strictly inferior.

## Section 10: Trust, Transparency, and Human Factors

Not addressed. The paper is purely technical (formal methods + empirical NLP evaluation). No user studies, trust measurements, or socio-technical evaluation.

## Section 11: Evaluation Design and Metrics

- **Functional correctness** (Accuracy %): expressions verified against ground truth via Z3 solver (GSM-Symbolic) or Prover9 (FOLIO).
- **Syntactic correctness** (Parse % / Compiles %): percentage of outputs that are well-formed.
- **Token efficiency** (average tokens generated).
- Ablation on few-shot examples (2, 4, 8 shots).
- Sampling ablation: CRANE with greedy decoding vs. unconstrained CoT with temperature sampling (t=0.7), pass@1/2/3.
- 9 models evaluated, ranging from 1.5B to 32B parameters.

## Section 12: Methodological Strengths

1. **Formal theoretical grounding** — Propositions 3.1 and 3.3 provide complexity-theoretic proofs, not just empirical observations. The expressivity loss is shown to hold for *any* constant-layer LLM, not specific models.
2. **Practical algorithm** — CRANE is simple, model-agnostic, compatible with any constrained decoding backend (IterGen, SynCode), and requires no fine-tuning.
3. **Comprehensive evaluation** — 9 models, 2 benchmarks, 4 baselines, ablations on few-shot and sampling.
4. **Reproducibility** — code available, grammars provided in appendix, prompts fully specified.

## Section 13: Methodological Limitations

1. **Proposition 3.1 scope:** Only proven for finite output languages L(G_c). Extension to infinite grammars is an open question (acknowledged by authors).
2. **Logit access required:** CRANE requires access to output logits, making it inapplicable to closed-source models (e.g., GPT-4, Claude).
3. **Delimiter dependence:** The unconstrained/constrained transition relies on the LLM generating delimiter tokens, which is incentivised via prompting/few-shot examples but not guaranteed.
4. **No semantic governance:** CRANE only enforces syntactic constraints. There is no mechanism for restricting the *semantic content* of outputs based on contextual risk assessment.
5. **No environmental conditioning:** Mode switching is syntactically triggered, not environmentally conditioned.

## Section 14: Cross-Paper Connections

| Connected Paper | Relationship |
|---|---|
| **Könighofer et al. (2025)** — probabilistic shielding | Both demonstrate that intermediate constraint levels outperform binary extremes. Könighofer shows this empirically for ε-shield parameters; CRANE proves it formally for grammar constraints. Complementary evidence for CAUTION mode optimality. |
| **Liang et al. (2025, SAFEXPLAIN)** — gatekeeper | SAFEXPLAIN's gatekeeper is a binary output-level filter; CRANE's constrained decoding is also output-level but with formal grammar backing. Both are Level 2 (A_AI) implementations without Level 1 (G(S)). |
| **Abella et al. (SAFEXPLAIN automotive)** — safe envelope | The "safe envelope" concept maps to CRANE's grammar G as a formal specification of the admissible output space. CRANE provides the formal proof that this envelope must not be too restrictive. |
| **Bloomfield & Rushby (2025)** — binary permit/override | CRANE's baseline constrained decoding is the token-level analogue of Bloomfield & Rushby's binary governance. CRANE's theoretical contribution (Proposition 3.1) formally explains why such binary approaches are suboptimal. |
| **Baxi (2026, preprint)** — graduated governance conditioned on agent robustness | Both propose graduated constraint architectures. Baxi conditions on agent robustness; CRANE conditions on syntactic position in the generation stream. Neither conditions on environmental state. |

## Section 15: Key Quotes / Formalisations for Citation

- Augmented grammar structure: G_a → R_M G — directly citable as formal precedent for "reasoning-then-restricted-output" architecture.
- Proposition 3.1: Formal proof that restrictive output constraints reduce LLM capability to TC⁰ — citable as theoretical motivation for avoiding binary advisory scope restriction.
- CRANE algorithm structure: alternating unconstrained/constrained windows — citable as closest algorithmic analogue to dynamic advisory scope governance.

## Section 16: Relevance to Dissertation Themes

| # | Theme | Relevant? |
|---|---|---|
| T1 | AI safety governance architecture | ✅ Yes — output-level constraint governance with formal expressivity analysis |
| T2 | Formal methods / verification | ✅ Yes — circuit complexity proofs, grammar-based constraint specification |
| T3 | Environmental state conditioning | ❌ No — no environmental state; mode switching is syntactically triggered |
| T4 | Low-resource / domain-specific | ❌ No — general NLP benchmarks, not domain-specific |
| T5 | Runtime governance mechanisms | ✅ Yes — CRANE operates at runtime during autoregressive generation |
| T6 | Binary vs. graduated governance | ✅ Yes — core contribution is demonstrating binary constraint inferiority |
| T7 | Human-AI decision support | ❌ No — no human factors component |
| T8 | Maritime / fisheries domain | ❌ No |

**Theme match count:** 4/8 → Full extraction warranted (confirmed).

## Section 17: Dissertation Integration Recommendations

### Citation Role: **Core architecture reference + gap evidence**

### Placement:
- **Section 2.2 (Literature Review — AI safety governance mechanisms):** Cite as the strongest formal proof that binary output constraint reduces AI reasoning capability. Frame Proposition 3.1 as theoretical motivation for the CAUTION mode: "Banerjee et al. (2025) formally prove that restricting AI outputs to a grammar encoding only valid final answers collapses the system's problem-solving capability to a restrictive complexity class (TC⁰), demonstrating at the computational-theoretic level why binary advisory scope governance is suboptimal."
- **Section 2.3 (Structural precursors):** Cite the augmented grammar G_a = R_M G as a structural precursor to the two-level governance pair. The R_M component (reasoning within constraints) maps conceptually to the CAUTION mode's restricted-but-non-empty advisory scope. Acknowledge this as the closest formal analogue while differentiating: CRANE's graduation is syntactic/temporal, not environmental-state-conditioned.
- **Formalisation chapter:** The set containment property AI(E) ⊆ A_AI(S) has a direct analogue in CRANE's guarantee that constrained output ∈ L(G). Cite as formal precedent for output-level set containment guarantees under governance constraints.

### Gap differentiation:
CRANE implements **syntactically-triggered temporal alternation** between two modes (unconstrained/constrained). The dissertation's contribution is **environmentally-conditioned graduated governance** with three discrete modes including an intermediate CAUTION state with a formally specified restricted advisory scope. Key differences:
1. Conditioning variable: syntactic delimiter (CRANE) vs. environmental state S = f(E) (dissertation)
2. Number of modes: 2 (CRANE) vs. 3 (dissertation — SAFE/CAUTION/UNSAFE)
3. Governance scope: output-level grammar enforcement (CRANE) vs. system-level participation + advisory scope governance (dissertation's two-level pair)
4. Domain: general NLP benchmarks (CRANE) vs. safety-critical decision support in low-resource environments (dissertation)

### Tracker Entry:
```
| Banerjee et al. (2025) | CRANE: Reasoning with constrained LLM generation | ICML 2025 | ⭐⭐⭐⭐ | Core architecture ref + gap evidence | Formal proof that binary output constraints reduce LLM expressivity (Prop. 3.1); augmented grammar G_a = R_M·G as structural precursor to CAUTION mode; 2-mode temporal alternation, not env-state-conditioned → gap preserved | Sections 2.2, 2.3, formalisation |
```
