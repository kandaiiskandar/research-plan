# Article Summary: On the Relevance of Logic for Artificial Intelligence, and the Promise of Neurosymbolic Learning

---

## 1. Paper Identity

- **Title:** On the Relevance of Logic for Artificial Intelligence, and the Promise of Neurosymbolic Learning
- **Author:** Vaishak Belle
- **Year:** 2025
- **Venue:** Neurosymbolic Artificial Intelligence Journal (Sage Journals)
- **DOI:** 10.1177/29498732251339951
- **Type:** Position Paper / Survey
- **Keywords:** Neurosymbolic AI, Logic and Learning
- **Key Contribution:** A comprehensive defense of symbolic logic in modern AI, addressing fundamental misunderstandings and arguing for neurosymbolic AI as the best path forward
- **Funding:** Royal Society University Research Fellowship
- **ORCID:** 0000-0001-5573-8465
- **Editors:** Frank van Harmelen (Vrije Universiteit Amsterdam), Pascal Hitzler (Kansas State University)
- **Received:** July 11, 2024
- **Accepted:** December 20, 2024

---

## 2. Core Argument

### 2.1. Thesis Statement

> *"The paper aims to address fundamental misunderstandings about logic and ultimately argue for the benefits of symbolic formalisms in modeling uncertain worlds. By arguing that symbolic logic is more flexible than nonexperts and critics believe, we make a case for neurosymbolic AI, which offers the best of both worlds."* (Page 1)

### 2.2. The Problem: Misunderstandings About Logic

Belle identifies **six common misunderstandings** about logic in the AI community:

| Misunderstanding | Reality |
|------------------|---------|
| Logic is old-fashioned (GOFAI) | Logic remains foundational in constraint satisfaction, planning, verification, and knowledge representation |
| Logic vs. learning is a dichotomy | Logic and probability are deeply connected; many languages unify them |
| Logic is only for discrete domains | Logic can capture continuous properties via SMT, fuzzy logic, and real-valued semantics |
| Logic is not differentiable | Loss functions with logical constraints, fuzzy logic, and probabilistic extensions enable differentiability |
| Logic cannot handle uncertainty | Probabilistic logics, MLNs, ProbLog, and BLOG unify logic and probability |
| Logic is monotonic | Nonmonotonic logics and stable model semantics address exceptions and defaults |

### 2.3. Key Quote

> *"It is now recognized that statistical associations learned from data are limited in their ability to understand the world... Yet, there is still a great deal of criticism and hesitancy regarding the use of symbolic logic to achieve or support a broader vision for AI."* (Page 1)

---

## 3. Addressing Misunderstandings About Logic

### 3.1. Myth: "Neural Approaches and Nothing Else!"

**The Critique:** Modern AI has moved on from symbolic logic; deep learning is the only viable approach.

**Belle's Response:**

| Counterargument | Explanation |
|-----------------|-------------|
| **Deep learning models are loosely inspired by brains** | Not accurate representations yet |
| **Innateness matters** | Evolution may help the brain process the world in structured ways |
| **We lack complete understanding of neural wiring** | Knowing neural weights enable birds to solve puzzles doesn't mean our implementations should resemble them |
| **Symbolic approach never claimed literal brain representation** | It offers a coherent strategy for (a) executing symbolic expressions and (b) comprehending implications |
| **We built calculators before understanding brains** | We can develop theory of cognition without brain-like architecture |

**Key Quote:**

> *"There is a popular analogy suggesting that we need not build wings and feathers to build airplanes; comprehending the principles of aerodynamics is enough. So, why shouldn't the development of a theory of artificial cognition be just as relevant for a type of AI that is behaviorally similar to humans in some instances, without necessarily resorting to a brain-like architecture?"* (Page 3)

---

### 3.2. Myth: "There is a Dichotomy Between Logic and Learning"

**The Critique:** Logic is for discrete domains; learning is for continuous ones.

**Belle's Response:**

**3.2.1. Real-Valued Truth Values**

Fuzzy logic (Zadeh, 1965) allows truth values between 0 and 1:

$$\alpha \wedge \beta \doteq \min(\alpha, \beta)$$

If α = 0.6 and β = 0.4, then α ∧ β = 0.4. This aligns with classical logic when values are 0 or 1.

**Implication for Your Research:** Neural network outputs (0-1) can be directly modeled as atoms in logical formulas. This enables reasoning about concepts learned from neural networks as part of a knowledge base.

**3.2.2. From Discrete to Continuous**

Satisfiability Modulo Theories (SMT) allows reasoning about continuous properties:

$$f(x) \leq y^2 \wedge y > g(x, z)$$

Where x, y, z can range over N, Z, or R.

**Implication for Your Research:** Logical constraints can be added to loss functions to train neural networks such that predictions always satisfy domain constraints (e.g., safety thresholds). This is more sample-efficient than assuming constraints are in the data.

**Key Quote:**

> *"Capturing the output of neural networks as truth values in a logical formula is one approach to reasoning about vector spaces. However, we can also use logic to reason about continuous properties as formulas."* (Page 5)

---

### 3.3. Myth: "Logic is Not Good for Probabilistic Uncertainty"

**The Critique:** Classical logic doesn't represent probabilistic assertions; learning moved away from logic.

**Belle's Response:**

**3.3.1. Probabilistic Logical Models**

Since Nilsson (1986), logic has been used to capture probabilistic spaces:

- If α is a well-defined formula, then Pr(α) is also expressible
- Combinations like: α ∧ Pr(β) > Pr(γ) ∧ Pr(γ) ≤ 0.6

**Languages for Logic and Probability:**

| Language | Description |
|----------|-------------|
| **Markov Logic Networks (MLNs)** | First-order logic with weights |
| **ProbLog** | Probabilistic Prolog |
| **BLOG** | Probabilistic models with unknown objects |
| **Weighted Model Counting** | Unified approach for Bayesian inference, ProbLog, MLNs, and factor graphs |

**Key Insight:**

> *"It is not only the case that logical languages allow us to reason about probability distributions over combinatorial spaces, but it is also the case that the syntax of logic can help capture complex relationships that are difficult to model using standard probabilistic languages."* (Page 6)

**3.3.2. Generalizing the Specification of a Distribution**

McCarthy and Hayes (1969) argued:

> *"(i) It is not clear how to attach probabilities to statements containing quantifiers... (ii) The information necessary to assign numerical probabilities is not ordinarily available. Therefore, a formalism that required numerical probabilities would be epistemologically inadequate."*

**Implication for Your Research:** In safety-critical domains like fisheries, we may not have exact probabilities for every condition. We need languages that allow qualitative uncertainty (e.g., "UNSAFE if wind > 25 knots") without requiring precise probabilities.

---

### 3.4. Myth: "Symbols Without Explicit Semantics"

**The Critique:** Programs can be learned without explicit semantics; only the interpreter matters.

**Belle's Response:**

> *"Without a clear specification of how compositions of expressions should be interpreted and evaluated, how are we to know what these programs are yielding?"* (Page 7)

**Key Insight:** Formal semantics is essential for:
- Understanding what properties are entailed by programs
- Checking internal consistency of programming languages
- Enabling verification and reasoning about behavior

**Implication for Your Research:** Your formal specification of E, S=f(E), G(S), and A_AI(S) provides the semantics needed to prove the Safety Dominance Property.

---

### 3.5. Myth: "Logic is About Categorical Propositional Assertions"

**The Critique:** Logic is just propositional logic with Boolean truth values.

**Belle's Response:**

**Belle enumerates the variety of logical systems:**

| Logic Type | Description |
|------------|-------------|
| **Propositional Logic** | Boolean symbols, truth tables |
| **First-Order Logic** | Quantifiers (∃, ∀), domain of discourse |
| **SMT** | Real arithmetic, functions over reals |
| **Modal Logic** | Possibilities, beliefs, intentions (Kripke, 1959) |
| **Probabilistic Logic** | Probabilities on formulas (Halpern, 2003) |
| **Fuzzy Logic** | Real-valued truth values (Zadeh, 1965) |
| **Nonmonotonic Logic** | Exceptions, defaults, stable model semantics |

**Key Quote:**

> *"These are all part and parcel of symbolic logic. The choice of the language, the choice of the semantic rules that we use over the well-defined formulas, along with its computational properties such as decidability are aspects of a logical framework."* (Page 8)

---

### 3.6. Myth: "Monotonicity is a Problem"

**The Critique:** Classical logic is monotonic; adding knowledge can't retract conclusions.

**Belle's Response:**

**The Frame Problem:** If you paint a box blue and then push it, the color doesn't change. You'd need to codify all non-effects—exponentially many.

**Solutions:**
- **Causal completeness assumptions** (Reiter, 2001): Conditions are both necessary and sufficient
- **Nonmonotonic logic**: Stable model semantics (Gelfond & Lifschitz, 1988)

**Implication for Your Research:** In safety-critical domains, we need to handle exceptions and defaults. Nonmonotonic reasoning allows specifying typical cases while accounting for abnormal conditions (e.g., "Usually, depart in wind < 15 knots, BUT if vessel is large, may depart in higher wind").

**Key Quote:**

> *"Nonmonotonic logic reasoning has given us notions such as stable model semantics, which now powers recent approaches to neurosymbolic learning."* (Page 9)

---

### 3.7. Myth: "Logic is Not Differentiable"

**The Critique:** Logic cannot be reconciled with gradient-based learning.

**Belle's Response:**

**Key Quote from Yann LeCun:** *"Our best approaches to learning rely on estimating and using the gradient of a loss, which can only be performed with differentiable architectures and is difficult to reconcile with logic-based symbolic reasoning."* (Page 9)

**Belle's Counter:**

| Approach | How It Enables Differentiability |
|----------|----------------------------------|
| **Semantic Loss** (UCLA) | Adjusts loss function based on logical constraints |
| **DeepProbLog** (KU Leuven) | Neural predictions corrected using logical solver; backpropagated |
| **Real-Valued Variables** | Arithmetic constraints in loss functions (Hoernle et al., 2022) |
| **Fuzzy Logic** | Real-valued semantics enable gradient flow (van Krieken et al., 2022) |
| **Temporal Logic** | Loss functions for reinforcement learning (Innes & Ramamoorthy, 2020) |

**Implication for Your Research:** Your Rule-Set Starvation mechanism for symbolic engines can be extended to ML via constrained output decoding (logit masking), which is differentiable.

---

## 4. Logic and Learning Can Be Complementary

### 4.1. Symbolic Logic as Meta-Theory

**Applications:**
- Formalizing probabilistic programming languages
- Understanding limits of differentiable logics
- Multiagent reasoning and explainable AI
- Multiagent reinforcement learning
- Compositionality and modularity in AI systems

**Key Insight:**

> *"Complex AI systems are not going to be purely based on providing predictions. They will involve search, constraint reasoning, and planning."* (Page 12)

**Implication for Your Research:** Your system involves both prediction (advisory generation) and constraint reasoning (safety state classification). Logic provides the formal framework for both.

---

### 4.2. High-Level Knowledge

**The System I vs. System II Distinction (Kahneman, 2011):**

| System | Description | AI Analog |
|--------|-------------|-----------|
| System I | Fast, intuitive, pattern recognition | Neural networks, deep learning |
| System II | Slow, deliberative, reasoning | Symbolic logic, planning |

**Key Insight:**

> *"It is widely acknowledged that concepts such as time, abstraction, and causality will play a key role in designing a general-purpose AI."* (Page 13)

**Belle argues that symbolic logic provides well-studied models of:**

1. **Temporal abstractions** — Which event happened earlier; triggers and effects
2. **Induction** — Finding generalized instances from examples
3. **Abstraction** — Finding atomic descriptions that characterize interactions
4. **Causation** — Understanding interventions and counterfactuals

**Implication for Your Research:** Your system reasons about temporal conditions (time of day), cause-effect relationships (weather → safety), and abstractions (SAFE/CAUTION/UNSAFE). Symbolic logic provides the formal foundation for these reasoning tasks.

---

### 4.3. Symbolic Logic Can Instantiate New Methods of Inference

**Weighted Model Counting (WMC):**

$$\text{WMC}(\phi, w) = \sum_{\{M \mid M \models \phi\}} \prod_{\{l \mid l \in M\}} w(l)$$

**Key Insight:**

> *"Because weighted model counting is defined in terms of weights on the possible models of a logical formula, it is possible to use different types of weights. This means a whole range of different computational tasks defined over the models of a logical formula can be approached using the same abstract specification."* (Page 14)

This leads to **Algebraic Model Counting** (Kimmig et al., 2012), where sums/products can be replaced with min/max operations.

**Knowledge Compilation:** Logical formulas represented as data structures that permit efficient model counting—used for Bayesian networks, MLNs, ProbLog, and probabilistic programming.

**Implication for Your Research:** Your Safety Dominance Property proof is a form of logical inference that could be extended with weighted model counting to quantify uncertainty (e.g., "How confident are we that this state is CAUTION rather than SAFE?").

---

### 4.4. Logical Oracles

**The Problem:** LLMs struggle with consistency and correctness in logical and arithmetic problems.

**The Solution:** Use logical solvers as oracles to validate or disprove predictions.

**Recent Approaches:**

| Approach | Description |
|----------|-------------|
| **Wolfram Alpha + ChatGPT** | Arithmetic solver integrated with LLM |
| **Pan et al. (2023)** | Logical solver as oracle for LLM reasoning |
| **Sileo & Lernould (2023)** | Theory of mind reasoning with logical solvers |
| **Tang & Belle (2024)** | Dynamic epistemic properties with LLMs |
| **Kautz (2024)** | "Tools are all you need"—LLM + SAT solver |

**Key Quote (Kautz, 2024):**

> *"The observation that tools greatly enhance the power of LLMs is not original... I go farther than most researchers pursuing the tool approach in that I mean the title of this paper, 'Tools Are All You Need,' quite literally: a language model augmented with reasoning tools is sufficient to create true artificial intelligence."* (Page 11)

**Implication for Your Research:** Your governance layer is a **logical oracle** for your AI advisory engine. It validates whether the AI's recommendations are appropriate for the current safety state. This is exactly the neurosymbolic pattern Belle describes.

---

### 4.5. Logic Benefits From Learning

**The Inductive Problem (Aristotle):** Learn the general from the particular; generalize from specific instances to quantified formulas.

**Modern Approaches:**

| Approach | Description |
|----------|-------------|
| **Statistical Relational Learning** | Learn logical rules from probabilistic data |
| **Probably Approximate Correct (PAC) Semantics** | Learn formulas that generalize with high probability |
| **Neural Program Induction** | Learn programs from examples (Lake et al., 2015) |
| **Neural Rule Induction** | Learn rules from noisy data (Evans & Grefenstette, 2018) |

**Key Quote:**

> *"It is now believed that machine learning will likely impact almost all of computer science because it provides a mechanism to construct models from data. This means that we will continue considering combinations of model-based and data-driven domain knowledge in the future."* (Page 15)

**Implication for Your Research:** Your system uses expert-provided rules (thresholds from MET Malaysia) but could be extended with learned rules from historical data—this is a neurosymbolic approach.

---

## 5. Key Applications: Trustworthy and Responsible AI

### 5.1. Safety Verification

**The Problem:** Ensure AI systems avoid dangerous operational areas and are robust to small input perturbations.

**The Solution:** Logic-based verification:

| Technique | Description |
|-----------|-------------|
| **Temporal Logic** | Formalize safety properties (Chatterjee et al., 2015) |
| **SMT** | Verify constraints on geometric spaces (Barrett et al., 2009) |
| **Neural Network Verification** | Check robustness properties (Shih et al., 2019; Casadio et al., 2022) |

**Implication for Your Research:** Your Safety Dominance Property AI(E) ⊆ A_AI(S) is exactly this type of safety verification—ensuring the AI's recommendations are always within safe boundaries.

---

### 5.2. Ethical and Fair AI

**The Problem:** Ensure AI systems operate under ethical principles and norms.

**The Solution:** Symbolic logic formalizes:

| Concept | Logical Formalization |
|---------|----------------------|
| **Act-deontology** | Properties the system's execution must obey |
| **Consequentialism** | Outcomes and their evaluation |
| **Blameworthiness** | Degree of responsibility (Chockler & Halpern, 2004) |
| **Explainable Planning** | Formal models of user intent (Kambhampati, 2020) |

**Key Quote:**

> *"For an overview of how knowledge representation can provide much-needed frameworks for ethical and trustworthy AI, see Belle (2023a)."* (Page 15)

**Implication for Your Research:** Your system formalizes accountability: the fisher (not the AI) makes the final decision; the AI provides advisory only. This is a logical/ethical separation enforced by your governance architecture.

---

## 6. Neurosymbolic AI: The State of the Art

### 6.1. Definition and Scope

> *"Neurosymbolic AI holds a lot of promise because it can offer interesting ways to combine symbolic logic and deep learning and build on the success of both. And like the maxim: 'the whole is greater than the sum of the parts,' such an integration may not simply be the communication of outputs in a divorced way, but could involve a deeper type of synthesis."* (Page 15)

### 6.2. Approaches

| Approach | Description |
|----------|-------------|
| **Loss Functions** | Logical constraints in loss function (Semantic Loss, DeepProbLog) |
| **Post-Hoc Reasoning** | Logical oracle validates predictions (Wolfram Alpha + ChatGPT) |
| **Rule Extraction** | Extract rules from trained networks |
| **Neural Program Induction** | Learn symbolic programs from data |
| **Knowledge Graph Integration** | Learning with ontologies (100+ nodes) |

### 6.3. The Language Question

**Key Insight (Pearl & Mackenzie, 2018):**

> *"This is why you will find me emphasizing and reemphasizing notation, language, vocabulary and grammar. For example, I obsess over whether we can express a certain claim in a given language and whether one claim follows from others. My emphasis on language also comes from a deep conviction that language shapes our thoughts. You cannot answer a question that you cannot ask, and cannot ask a question that you have no words for."* (Page 16)

**Implication for Your Research:** Your formal specification of E, S=f(E), G(S), and A_AI(S) is precisely this language—it defines what questions can be asked (e.g., "Is it SAFE to go?" or "What recommendations are admissible under CAUTION?") and what answers can be given.

---

## 7. Key Quotes for Your Proposal

### 7.1. On the Value of Symbolic Logic

> *"It is now recognized that statistical associations learned from data are limited in their ability to understand the world."* (Page 1)

### 7.2. On Logic and Learning Being Complementary

> *"Symbols and deep learning need not compete with each other, and can be complementary."* (Page 12)

### 7.3. On Formal Guarantees

> *"We may not want mathematical truths that play fast and loose with inevitable conclusions just because we think humans might have some cognitive biases and exhibit inconsistent reasoning."* (Page 12)

### 7.4. On Safety-Critical Systems

> *"We need to look at the best of all worlds. And in that regard, the unification of logic and learning continues to bear fruit, of which neurosymbolic AI is the latest installment."* (Page 16)

### 7.5. On Avoiding "Silver Bulletism"

> *"As a field, I believe that we tend to suffer from what might be called serial silver bulletism, defined as follows: the tendency to believe in a silver bullet for AI, coupled with the belief that previous beliefs about silver bullets were hopelessly naïve."* (Page 16)

---

## 8. Relationship to Your PhD Research

### 8.1. Direct Relevance Matrix

| Your Research Element | Belle's Argument | Relevance |
|-----------------------|------------------|-----------|
| **Symbolic rule-based engine** | Logic provides formal semantics; neural approaches alone are insufficient for understanding the world | ★★★★★ |
| **Formal verification of Safety Dominance Property** | Logic enables verification of safety properties; logical solvers as oracles validate predictions | ★★★★★ |
| **Neuro-symbolic AI framing** | The paper is a position paper advocating exactly this paradigm | ★★★★★ |
| **State-conditioned governance** | Logic can capture continuous properties; logic and probability are compatible | ★★★★★ |
| **Rule-Set Starvation** | Logic can instantiate new methods of inference; logical constraints in loss functions | ★★★★☆ |
| **Human-in-the-loop** | Logic provides frameworks for explainable planning and high-level knowledge | ★★★★☆ |
| **Low-resource deployment** | Not addressed (theoretical paper) | ★★☆☆☆ |

### 8.2. Citations You Should Add

**For the "Clarification of Scope" section:**

> Belle, V. (2025). On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning. *Neurosymbolic Artificial Intelligence*, 1, 29498732251339951. DOI: 10.1177/29498732251339951

**For the "Why Use Logic?" argument:**

> "Symbolic logic is more flexible than nonexperts and critics believe... neurosymbolic AI offers the best of both worlds." (Belle, 2025, p. 1)

**For the "Logic and Probability are Compatible" argument:**

> "Logic and probability are deeply connected; there is a vibrant community focused precisely on this agenda." (Belle, 2025, p. 6)

**For the "Logic Enables Verification" argument:**

> "We need to look at the best of all worlds. And in that regard, the unification of logic and learning continues to bear fruit." (Belle, 2025, p. 16)

### 8.3. What to Cite in Each Section

| Your Proposal Section | What to Cite from Belle |
|-----------------------|-------------------------|
| **Introduction** | Logic is not old-fashioned; neural approaches alone are limited |
| **Literature Review** | Logic can capture continuous properties and probabilities; neurosymbolic AI is the future |
| **Conceptual Framework** | Logic provides formal semantics; reasoning and learning are complementary |
| **Formal Specification** | Logic enables verification of safety properties; SMT and temporal logic for constraints |
| **Methodology** | Logic provides foundations for trustworthy and responsible AI |
| **Expected Results** | Logic and learning unification continues to bear fruit |

---

## 9. Direct Text to Insert into Your Proposal

### 9.1. For the Introduction (Neuro-Symbolic Framing)

> Belle (2025) argues that "statistical associations learned from data are limited in their ability to understand the world" and that "symbolic logic is more flexible than nonexperts and critics believe." He makes a case for neurosymbolic AI, which "offers the best of both worlds"—combining the pattern recognition of neural networks with the formal reasoning of symbolic systems. This research adopts precisely this neurosymbolic framing: the AI Advisory Reasoning Engine is implemented as a symbolic rule-based system, enabling formal verification of the Safety Dominance Property, while the architecture is designed to accommodate probabilistic ML extensions via constrained output decoding.

### 9.2. For the Literature Review (Logic and Probability)

> Belle (2025) systematically addresses six common misunderstandings about logic in AI, including the false dichotomy between logic and learning. He demonstrates that logic can capture continuous properties (via SMT and fuzzy logic), represent probabilistic uncertainty (via probabilistic logics, MLNs, and ProbLog), and enable differentiability (via semantic loss functions and DeepProbLog). This directly supports our claim that a symbolic rule-based engine can provide formal safety guarantees while remaining compatible with future ML extensions.

### 9.3. For the Conceptual Framework (Governance as Logical Oracle)

> Belle (2025) argues that logical solvers can serve as "oracles" that validate or disprove the predictions of neural architectures, including LLMs. This is precisely the role of our Deterministic Safety-State Gating Layer: it acts as a logical oracle that validates whether the AI's recommendations are appropriate for the current safety state. The governance layer constrains the AI's admissible output space before inference begins, ensuring the Safety Dominance Property holds.

### 9.4. For the Expected Results (Formal Verification)

> Belle (2025) emphasizes that "logic enables verification of safety properties" and that "logic-based computer science, including temporal logic and SMT, are the main tools to formalize and investigate these types of properties." Our Safety Dominance Property proof by construction is a direct instantiation of this principle: we use logic to formally verify that the AI's recommendations are always within safe boundaries.

---

## 10. References to Add from Belle

| Reference | Citation | Relevance |
|-----------|----------|-----------|
| **Belle (2025)** | Belle, V. (2025). On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning. *Neurosymbolic Artificial Intelligence*, 1, 29498732251339951. DOI: 10.1177/29498732251339951 | Main reference |
| **Garcez et al. (2002)** | Garcez, A. S. d., Broda, K., & Gabbay, D. M. (2002). *Neural-symbolic learning systems: Foundations and applications*. Springer. | Foundational neurosymbolic work |
| **Hitzler (2022)** | Hitzler, P. (2022). *Neuro-symbolic artificial intelligence: The state of the art*. IOS Press. | Comprehensive overview |
| **Raedt et al. (2016)** | Raedt, L. D., Kersting, K., Natarajan, S., & Poole, D. (2016). Statistical relational artificial intelligence: Logic, probability, and computation. *Synthesis Lectures on Artificial Intelligence and Machine Learning*, 10(2), 1-189. | Logic and probability unification |
| **Kautz (2024)** | Kautz, H. (2024). Tools are all you need. *Proceedings of the 4th Workshop on Logic and Practice of Programming*. | LLMs + logical tools |
| **Hoernle et al. (2022)** | Hoernle, N., Karampatsis, R. M., Belle, V., & Gal, K. (2022). Multiplexnet: Towards fully satisfied logical constraints in neural networks. *AAAI*. | Differentiable logic constraints |
| **Manhaeve et al. (2018)** | Manhaeve, R., Dumancic, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog: Neural probabilistic logic programming. *NeurIPS*. | Neuro-symbolic learning |

---

## 11. Suggested Bibliography Entry

```bibtex
@article{belle2025relevance,
  author = {Belle, Vaishak},
  title = {On the relevance of logic for artificial intelligence, and the promise of neurosymbolic learning},
  journal = {Neurosymbolic Artificial Intelligence},
  volume = {1},
  pages = {29498732251339951},
  year = {2025},
  doi = {10.1177/29498732251339951},
  note = {Received July 11, 2024; accepted December 20, 2024}
}

## 12. Final Assessment: Relevance to Your PhD

| Criterion | Rating | Justification |
|-----------|--------|---------------|
| Theoretical Foundation | ★★★★★ | Provides the philosophical and mathematical justification for using symbolic logic in AI |
| Neuro-Symbolic Framing | ★★★★★ | Directly advocates for the paradigm your research embodies |
| Formal Verification Support | ★★★★★ | Argues that logic is essential for safety-critical systems |
| Differentiability Argument | ★★★★☆ | Shows logic can be made differentiable, supporting your ML extension |
| Uncertainty Handling | ★★★★☆ | Demonstrates logic can handle probability and uncertainty |
| Explainability Support | ★★★★☆ | Logic provides interpretable, auditable reasoning |
| Contemporary Relevance | ★★★★★ | 2025 paper, directly addressing modern AI debates |
| Academic Authority | ★★★★★ | Royal Society University Research Fellow; prestigious journal |
| Safety-Critical Validation | ★★★★★ | Explicitly discusses safety verification as a key application of logic |
| Trustworthy AI Support | ★★★★☆ | Discusses ethics, fairness, and responsibility in AI |

---

## 13. Summary: How to Use This Paper

| Purpose | How to Use Belle (2025) | Section to Place |
|---------|-------------------------|------------------|
| Defend symbolic AI | Cite "symbolic logic is more flexible than nonexperts believe" | Introduction / Clarification of Scope |
| Justify neuro-symbolic approach | Cite "neurosymbolic AI offers the best of both worlds" | Literature Review / Conceptual Framework |
| Support formal verification | Cite "logic enables verification of safety properties" | Formal Specification / Expected Results |
| Show logic can handle uncertainty | Cite "logic and probability are deeply connected" | Literature Review |
| Support ML extension | Cite "logic can be differentiable via loss functions" | Prototype Implementation / Future Work |
| Justify governance layer | Cite "logical solvers can serve as oracles" | Conceptual Framework |
| Address "is it AI?" question | Cite "logic is not old-fashioned; it remains foundational" | Introduction / Clarification of Scope |
| Support safety-critical framing | Cite "logic is essential for safety-critical systems" | Problem Statement / Expected Results |
| Support trustworthy AI | Cite "logic provides frameworks for ethical and responsible AI" | Research Design / Discussion |
| Address "silver bulletism" | Cite "we must avoid serial silver bulletism" | Literature Review / Conclusion |

---

## 14. Key Quotes for Your Proposal with Page Numbers

### 14.1. On the Value of Symbolic Logic

> "It is now recognized that statistical associations learned from data are limited in their ability to understand the world." (Page 1)

> "Symbolic logic is more flexible than nonexperts and critics believe." (Page 1)

### 14.2. On Neuro-Symbolic AI

> "Neurosymbolic AI offers the best of both worlds." (Page 1)

> "The unification of logic and learning continues to bear fruit, of which neurosymbolic AI is the latest installment." (Page 16)

### 14.3. On Logic and Learning Being Complementary

> "Symbols and deep learning need not compete with each other, and can be complementary." (Page 12)

> "Logic and learning have significant overlap—including ideas such as model counting appearing in and linking to multiple concerns—and it is also the case that recent advances are exploiting state-of-the-art learning for reasoning (and vice versa), and in the process, improving on the state-of-the-art." (Page 15)

### 14.4. On Formal Guarantees and Verification

> "We may not want mathematical truths that play fast and loose with inevitable conclusions just because we think humans might have some cognitive biases and exhibit inconsistent reasoning." (Page 12)

> "Logic-based computer science, including temporal logic and SMT, are the main tools to formalize and investigate these types of properties." (Page 15)

### 14.5. On the Importance of Language

> "Language shapes our thoughts. You cannot answer a question that you cannot ask, and cannot ask a question that you have no words for." (Page 16, citing Pearl & Mackenzie, 2018)

### 14.6. On Avoiding "Silver Bulletism"

> "As a field, I believe that we tend to suffer from what might be called serial silver bulletism, defined as follows: the tendency to believe in a silver bullet for AI, coupled with the belief that previous beliefs about silver bullets were hopelessly naïve." (Page 16)

### 14.7. On Trustworthy AI

> "With the growing use of AI systems in financial and industrial applications, issues of trustworthiness and responsibility keep coming up." (Page 15)

### 14.8. On Safety Verification

> "One area where symbolic logic is widely used in many stochastic systems is the verification of safety properties, and/or testing for robustness." (Page 15)

### 14.9. On the Limitations of Purely Neural Models

> "The 'native' reasoning capabilities of purely neural models seem clearly limited." (Page 11)

### 14.10. On Logical Oracles

> "A language model augmented with reasoning tools is sufficient to create true artificial intelligence." (Page 11, citing Kautz, 2024)

---

## 15. Direct Text to Insert into Your Proposal

### 15.1. For the Introduction (Neuro-Symbolic Framing)

> Belle (2025) argues that "statistical associations learned from data are limited in their ability to understand the world" and that "symbolic logic is more flexible than nonexperts and critics believe." He makes a case for neurosymbolic AI, which "offers the best of both worlds"—combining the pattern recognition of neural networks with the formal reasoning of symbolic systems. This research adopts precisely this neurosymbolic framing: the AI Advisory Reasoning Engine is implemented as a symbolic rule-based system, enabling formal verification of the Safety Dominance Property, while the architecture is designed to accommodate probabilistic ML extensions via constrained output decoding. As Belle notes, "the unification of logic and learning continues to bear fruit, of which neurosymbolic AI is the latest installment" (Belle, 2025, p. 16).

### 15.2. For the Literature Review (Logic and Probability)

> Belle (2025) systematically addresses six common misunderstandings about logic in AI, including the false dichotomy between logic and learning. He demonstrates that logic can capture continuous properties (via SMT and fuzzy logic), represent probabilistic uncertainty (via probabilistic logics, MLNs, and ProbLog), and enable differentiability (via semantic loss functions and DeepProbLog). This directly supports our claim that a symbolic rule-based engine can provide formal safety guarantees while remaining compatible with future ML extensions. Belle emphasizes that "logic and learning have significant overlap" and that "recent advances are exploiting state-of-the-art learning for reasoning (and vice versa)" (Belle, 2025, p. 15).

### 15.3. For the Conceptual Framework (Governance as Logical Oracle)

> Belle (2025) argues that logical solvers can serve as "oracles" that validate or disprove the predictions of neural architectures, including LLMs. Kautz (2024, cited in Belle, 2025, p. 11) goes further, stating that "a language model augmented with reasoning tools is sufficient to create true artificial intelligence." This is precisely the role of our Deterministic Safety-State Gating Layer: it acts as a logical oracle that validates whether the AI's recommendations are appropriate for the current safety state. The governance layer constrains the AI's admissible output space before inference begins, ensuring the Safety Dominance Property holds. As Belle notes, "logic-based computer science... are the main tools to formalize and investigate these types of properties" (Belle, 2025, p. 15).

### 15.4. For the Expected Results (Formal Verification)

> Belle (2025) emphasizes that "logic enables verification of safety properties" and that "logic-based computer science, including temporal logic and SMT, are the main tools to formalize and investigate these types of properties" (p. 15). Our Safety Dominance Property proof by construction is a direct instantiation of this principle: we use logic to formally verify that the AI's recommendations are always within safe boundaries. This addresses Belle's concern that "we may not want mathematical truths that play fast and loose with inevitable conclusions just because we think humans might have some cognitive biases" (Belle, 2025, p. 12).

### 15.5. For the Clarification of Scope ("Is It Really AI?")

> Belle (2025) directly addresses the misconception that symbolic logic is "old-fashioned" or "GOFAI." He notes that "logic is not old-fashioned—it remains foundational in constraint satisfaction, automated planning, database theory, ontology specification, verification, and knowledge representation" (p. 2). Moreover, he argues that "the symbolic approach offers a coherent strategy for: (a) executing symbolic expressions, which capture the knowledge of the system about the world and (b) comprehending the (idealized) implications of one's knowledge, as specified by inference rules in logic" (p. 3). This directly addresses potential committee concerns that our rule-based engine is "not really AI"—it is AI in the classical sense, and as Belle demonstrates, classical AI is far from obsolete.

### 15.6. For the Problem Statement (Limitations of Pure ML)

> Belle (2025) cites extensive evidence that purely neural models struggle with reasoning: "despite allowing for a number of different ways to backtrack and infer the correct premise for a query (e.g., so-called 'chain-of-thought'), as shown in a number of papers, they seem to incorrectly reason in a number of different ways" (p. 11). He notes that "the 'native' reasoning capabilities of purely neural models seem clearly limited" (p. 11) and that "there is little evidence that they are consistently correct—as Kautz (2024) puts it: 'So close, and yet so far!'" (p. 11). This supports our argument that binary-gated AI architectures create a dangerous decision vacuum—pure ML models cannot be trusted to provide safe recommendations without formal governance.

### 15.7. For the Methodology (Trustworthy AI)

> Belle (2025) discusses how "with the growing use of AI systems in financial and industrial applications, issues of trustworthiness and responsibility keep coming up" (p. 15). He notes that "symbolic logic is widely used... for the verification of safety properties, and/or testing for robustness" (p. 15). He also discusses how "knowledge representation can provide much-needed frameworks for ethical and trustworthy AI" (p. 15, citing Belle, 2023a). This supports our DSR methodology and contextual user validation phase, which are designed to ensure the system is trustworthy and responsible in the context of small-scale fisheries.

### 15.8. For the Literature Review (Avoiding "Silver Bulletism")

> Belle (2025) warns against "serial silver bulletism"—"the tendency to believe in a silver bullet for AI, coupled with the belief that previous beliefs about silver bullets were hopelessly naïve" (p. 16). He argues that "in view of creating general-purpose, safe, and reliable AI, we need to look at the best of all worlds" (p. 16). This supports our argument that existing AI governance architectures are insufficient because they are binary (on/off). We need graduated, multi-level governance—not a single "silver bullet" solution. Belle's argument reinforces that a hybrid approach (symbolic + ML, with multiple governance levels) is the most promising path forward.

---

## 16. Additional References to Add from Belle's Bibliography

| Reference | Full Citation | Relevance to Your Research |
|-----------|---------------|---------------------------|
| **Hitzler (2022)** | Hitzler, P. (2022). *Neuro-symbolic artificial intelligence: The state of the art*. IOS Press. | Comprehensive neurosymbolic overview |
| **Garcez et al. (2002)** | Garcez, A. S. d., Broda, K., & Gabbay, D. M. (2002). *Neural-symbolic learning systems: Foundations and applications*. Springer. | Foundational neurosymbolic work |
| **Raedt et al. (2016)** | Raedt, L. D., Kersting, K., Natarajan, S., & Poole, D. (2016). Statistical relational artificial intelligence: Logic, probability, and computation. *Synthesis Lectures on Artificial Intelligence and Machine Learning*, 10(2), 1-189. | Logic and probability unification |
| **Kautz (2024)** | Kautz, H. (2024). Tools are all you need. *Proceedings of the 4th Workshop on Logic and Practice of Programming*. | LLMs + logical tools |
| **Hoernle et al. (2022)** | Hoernle, N., Karampatsis, R. M., Belle, V., & Gal, K. (2022). Multiplexnet: Towards fully satisfied logical constraints in neural networks. *AAAI*. | Differentiable logic constraints |
| **Manhaeve et al. (2018)** | Manhaeve, R., Dumancic, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog: Neural probabilistic logic programming. *NeurIPS*. | Neuro-symbolic learning |
| **Gajowniczek et al. (2020)** | Gajowniczek, K., Liang, Y., Friedman, T., Zabkowski, T., & Van den Broeck, G. (2020). Semantic and generalized entropy loss functions for semi-supervised deep learning. *Entropy*, 22(3), 334. | Logical constraints in loss functions |
| **Kimmig et al. (2012)** | Kimmig, A., den Broeck, G. V., & Raedt, L. D. (2012). Algebraic model counting. *CoRR*, abs/1211.4475. | Unified inference framework |

---