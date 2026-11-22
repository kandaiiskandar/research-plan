---
source_pdf: "Scopus - Scopus AI -3.pdf"
source_sha256: "27abd9bae271fe67bf2fbeae3c50ab5e5ead875a4d238f82dbc32f651b567b96"
source_pages: 12
scopus_ai_generated: "Thu Apr 09 2026"
query: "Semantic guardrails in AI"
report_title: "State-of-the-Art Methods for Semantic Guardrails and Logic-Constrained Generation in Neuro-Symbolic AI Quick Reference"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Semantic guardrails in AI

## Key Findings Table

| Method/Architecture | Core Mechanism/Property | Deterministic State Rules | Set Containment ($A \subset B$) | Inference- Time Safety | Scalability | Reference(s) |
| --- | --- | --- | --- | --- | --- | --- |
| RLHF & Constitutional AI | Human/AI feedback, runtime enforcement | Partial | No | Yes | Medium | 1 2 |
| Hybrid HITL Architectures | Automated + human oversight | Yes | No | Yes | Medium | 3 4 |
| Retrieval- Augmented Generation | Knowledge grounding, auditability | Partial | No | Yes | High | 5 6 |
| Constrained Decoding (CRANE, etc.) | Grammar-based output restriction | Yes | No | Yes | Medium | 7 |
| Neuro-Symbolic SPL | Semantic Probabilistic Layers | Yes | Yes | Yes | Low- Medium | 8 9 |
| Entropy Regularization | Restrict output to valid structures | Yes | Yes | Yes | Medium | 10 11 |
| Posterior- Constrained NeSy Models | Regularize symbolic structure gen. | Yes | Yes | Yes | Medium | 12 |

## Direct Answer

State-of-the-art methods for semantic guardrails and logic-constrained generation combine approaches like Reinforcement Learning from Human Feedback (RLHF), Constitutional AI, and hybrid neuro-symbolic architectures. Techniques such as input and output filtering, knowledge grounding via retrieval-augmented generation (RAG), and dedicated constrained decoding algorithms (e.g., CRANE) are being used to restrict AI outputs based on deterministic state rules. Neuro-symbolic architectures implement set containment properties ($A \subset B$) through mechanisms like Semantic Probabilistic Layers, neuro-symbolic entropy regularization, and posterior constraint integration to ensure that the probabilistic outputs remain within symbolic safety envelopes at inference.

## Study Scope

**Time Period:** 2021–2024 **Disciplines:** AI safety, neuro-symbolic AI, natural language processing, reinforcement learning, logic programming, hardware-software co-design **Methods:** Meta-analysis, empirical benchmarking, architectural surveys, theoretical synthesis

## Assumptions & Limitations

Most neuro-symbolic architectures are not yet fully scalable or standardized for production-scale deployment. Evaluation protocols for guardrail effectiveness are still emerging and lack universal adoption. Hardware limitations and symbol grounding remain significant bottlenecks. The balance between constraint strictness and model flexibility is highly domain-and task-dependent.

## Suggested Further Research

Develop standardized, domain-agnostic evaluation protocols for guardrail systems. Advance meta-cognitive frameworks for self-monitoring and adaptability in neuro-symbolic AI. Explore hardware-software co-design for scalable neuro-symbolic computation. Integrate richer, context-aware feedback mechanisms (e.g., structured bug reports) into RLHF workflows. Investigate hybrid architectures that dynamically adjust constraint strictness based on context and risk.

## 1. Introduction

## Background and Motivation

The rapid proliferation of large language models (LLMs) and generative AI systems has amplified concerns about unconstrained, unsafe, or non-compliant outputs. Unrestricted generation can lead to hallucinations, ethical violations, and regulatory breaches, especially in high-stakes domains such as healthcare, finance, and public policy. To address these risks, the AI research community has prioritized the development of **semantic guardrails** and **logic-** **constrained generation** methods that formally restrict an AI agent’s admissible recommendation space to a finite set of types, governed by deterministic state rules. These approaches are foundational for building trustworthy, interpretable, and legally compliant AI systems.

Recent advances highlight the convergence of **hybrid neuro-symbolic architectures** —integrating neural pattern recognition with symbolic reasoning—as a promising pathway for robust AI governance. These architectures facilitate the enforcement of deterministic state rules and set containment properties, ensuring that probabilistic outputs remain bounded by symbolic safety envelopes, especially at inference time. This report synthesizes the state-of-the-art in semantic guardrails, logic-constrained generation, and neuro-symbolic architectures, bridging theoretical foundations with practical insights for researchers and practitioners[4][13].

## 2. Semantic Guardrails: Methods and Advances

## Technical and Procedural Guardrails

Modern semantic guardrail systems employ **multilayered architectures** that combine technical, procedural, and human oversight mechanisms: **Input Filtering & Output Validation:** Pre-and post-processing layers filter unsafe or non-compliant content, often using rule-based or classifier-based approaches[4]. **Knowledge Grounding:** Integration with enterprise knowledge bases or regulatory ontologies ensures that outputs are contextually accurate and compliant[14]. **Policy-as-Code:** Machine-readable rule languages (e.g., SHACL, N3) encode regulatory and organizational constraints for automated enforcement[15]. **Hybrid Neuro-Symbolic Enforcement:** Frameworks like PRISM-AI combine symbolic rule engines with neural agents for efficient, accurate enforcement of privacy and safety rules[16]. **Lightweight Inference-Time Filtering:** Methods such as DIESEL apply semantic filtering during generation, improving safety without retraining[17]. **Scenario-Guided Guardrail Training:** Models like CONSCENDI use contrastive learning and scenario-driven data generation to enhance rule coverage and enforcement[18]. **Synthesis:** These approaches collectively improve compliance, auditability, and robustness, but require ongoing integration with evolving policies and domain knowledge[4][14][15].

**Reinforcement Learning from Human Feedback (RLHF) and Constitutional AI** **RLHF** and **Constitutional AI** are central to aligning LLMs with human values and regulatory requirements: **RLHF:** Models are fine-tuned using human (or AI-generated) feedback to prefer outputs that align with ethical and organizational values. Recent advances include: **RLAIF:** Uses AI-generated feedback to reduce human labeling costs[1]. **Bug Report-Enhanced RLHF:** Embeds structured, context-rich feedback for improved alignment in regulated domains[19]. **Automated RLHF Platforms:** Tools like Uni-RLHF support scalable, modular feedback collection and benchmarking[20]. **Constitutional AI:** Moves beyond training-time alignment to runtime enforcement of normative reasoning, using constitutional attention mechanisms for real-time safety validation[2]. **Hybrid RLHF-Constitutional AI:** Combines RLHF’s value alignment with Constitutional AI’s runtime conflict resolution, enhancing safety, interpretability, and adaptability[4]. **Synthesis:** RLHF and Constitutional AI provide complementary layers of semantic guardrails, with RLHF tuning model preferences and Constitutional AI ensuring ongoing compliance and robustness[1][2][4][19].

## Hybrid Human-in-the-Loop Architectures

Hybrid architectures balance automated enforcement with human oversight, crucial for nuanced decision-making:

**Trimodal Thinking:** Combines fast (intuitive) and slow (rational) AI decision systems with a control layer for bias mitigation and context-sensitive responses[21].

**Iterative Refinement:** Human-in-the-loop feedback loops reduce false positives and improve ethical alignment[22].

**Multi-Layered Defense:** Automated detection is paired with human review to catch edge cases and ensure compliance in sensitive domains[23].

**Dynamic Oversight:** HITL systems enable continuous improvement and adaptation, especially in high-stakes or ambiguous scenarios[4][24]. **Synthesis:** HITL architectures are essential for handling exceptions, ambiguous cases, and evolving ethical standards, complementing automated guardrails[3][4][21].

## Retrieval-Augmented Generation (RAG) for Guardrails

**RAG** methods enhance factuality, auditability, and semantic guardrails by grounding outputs in external knowledge: **Knowledge Integration:** RAG systems retrieve authoritative context to reduce hallucinations and improve answer quality[5]. **Modular Pipelines:** Combining hybrid retrieval, uncertainty-aware control, and memory modules strengthens grounding and reduces hallucinations[25]. **Limitations:** RAG’s effectiveness is constrained by semantic similarity reliance, document chunking, and lack of temporal reasoning[26]. **Best Practices:** Optimizing retrieval (e.g., increasing retrieved documents, applying confidence thresholds) and integrating reasoning-capable LLMs (e.g., chain-of-thought prompting) further reduce hallucinations[27][28]. **Clinical Applications:** RAG pipelines in healthcare achieve high retrieval accuracy and low hallucination rates, demonstrating practical safety benefits[29]. **Synthesis:** RAG is a mature pattern for grounded, auditable AI, but must be combined with other guardrails for high-stakes applications[5][6][25].

## 3. Logic-Constrained Generation: Algorithms and Trade-offs

## Constrained Decoding and Grammar-Based Methods

Logic-constrained generation techniques enforce deterministic state rules through structured output constraints: **Constrained Decoding (e.g., CRANE):** Augments output grammars with additional rules to preserve reasoning capabilities while ensuring syntactic and semantic correctness[7]. **Other Algorithms (DOMINO, Formatron):** Align constraints with subword vocabularies and dynamically prune invalid states for efficiency[30]. **Finite Automata & OCL:** Logical constraints are often represented as deterministic finite automata or formal languages (e.g., Object Constraints Language) to guide generation[31][32].

**Certified Reasoning:** State and incremental constraints enable certified deductive reasoning and self-improvement by training on certified traces (e.g., LogicGuide)[33].

**Physics-Constrained GANs:** Deterministic constraints embedded in loss functions improve convergence and robustness in physical system emulation[34]. **Synthesis:** These methods ensure output safety and correctness, but require careful design to avoid excessive rigidity [7][31][32][33].

## Balancing Constraint Strictness and Model Flexibility

A central challenge is balancing strict logic constraints with the inherent flexibility of LLMs: **Trade-offs:** Strict grammar-based constraints ensure correctness but can degrade reasoning capabilities and output diversity, especially in instruction-tuned models[7][35]. **Grammar Augmentation:** Carefully designed additional rules can preserve reasoning while maintaining structure [7]. **Prompt Adaptation:** Instruction-tuned models require adapted prompts and few-shot examples to mitigate performance drops under constraints[36]. **Training-Time Integration:** Incorporating constraints during training, rather than only at decoding, helps maintain reasoning capabilities[37]. **Domain-Specific Tuning:** Constraint mechanisms must be tailored to specific tasks and model architectures for optimal performance[38]. **Synthesis:** Effective logic-constrained generation requires dynamic adaptation of constraint strictness, informed by task requirements and model characteristics[7][35][36].

## Integration of Deterministic State Rules

Deterministic state rules are represented and enforced through: **Finite Automata:** Used to encode permissible output sequences and guide generation[31]. **Ontologies & OCL:** Provide structured, machine-readable representations of domain rules for code generation and semantic validation[32]. **Symbolic Rule Engines:** Integrated with neural predictors in neuro-symbolic frameworks for efficient enforcement [16]. **Formal Verification:** Runtime verification and formal methods ensure compliance with deterministic rules during inference[39]. **Synthesis:** Deterministic state rules are foundational for ensuring output safety, correctness, and compliance, especially in regulated domains[31][32][33].

## 4. Neuro-Symbolic Architectures and Set Containment

## Semantic Probabilistic Layers and Set Containment

**Semantic Probabilistic Layers (SPL)** and related neuro-symbolic frameworks guarantee that probabilistic outputs remain within symbolic safety envelopes: **SPL:** Combines exact probabilistic inference with logical reasoning, ensuring predictions are consistent with predefined symbolic constraints[8].

**Set Containment ($A \subset B$):** SPL and similar architectures enforce that the set of admissible outputs (A) is always a subset of the symbolic safety envelope (B)[8][9].

**Inference-Time Correction:** Symbolic reasoning modules can correct neural prediction errors at inference, balancing efficiency and constraint satisfaction[9]. **Synthesis:** SPL and related neuro-symbolic layers provide formal guarantees of set containment, critical for safety in high-stakes applications[8][9].

## Neuro-Symbolic Entropy Regularization

Entropy regularization is applied to restrict probabilistic outputs to valid symbolic structures: **Mechanism:** Entropy regularization loss is computed only over valid structures defined by symbolic constraints, encouraging confident and valid predictions[10][11]. **Integration:** Efficiently computed when constraints are expressed as tractable logic circuits; integrates with other neuro-symbolic losses to eliminate invalid predictions[10][11]. **Impact:** Improves accuracy, validity, and confidence calibration in structured prediction tasks[10]. **Synthesis:** Neuro-symbolic entropy regularization is a powerful tool for maintaining symbolic safety envelopes and improving model reliability[10][11].

**Posterior Constraints in Probabilistic Neural-Symbolic Models** Posterior constraints regularize symbolic structure generation: **Direct Regularization:** Structure posterior is regularized to balance learning from data and integrating domain knowledge[12]. **Adaptive Reweighting:** Handles noisy annotations and improves robustness[12]. **Latent Variable Models:** Symbolic programs are treated as latent stochastic variables, enabling interpretable and counterfactual reasoning[40][41]. **Correction at Inference:** Symbolic modules correct neural outputs, ensuring set containment and constraint satisfaction[9]. **Synthesis:** Posterior-constrained neuro-symbolic models enhance interpretability, robustness, and adherence to symbolic safety envelopes[10][12].

## 5. Research Gaps, Challenges, and Future Directions

## Current Capabilities and Limitations

**Strengths:** Neuro-symbolic AI combines neural pattern recognition with symbolic reasoning, yielding superior performance in structured, safety-critical tasks[42][43][44]. **Limitations:** Major challenges include scalability, reproducibility, symbol grounding, and lack of standardized architectures[42][45]. **Explainability & Trust:** Explainability, trustworthiness, and intervenability remain underdeveloped, limiting deployment in high-stakes domains[44][46]. **Ethical Integration:** Integration of ethical frameworks and real-time adaptation is still nascent[43][46]. **Synthesis:** While current methods are effective in controlled settings, broader adoption requires addressing scalability, explainability, and integration challenges[13][42][43][44].

## Scalability and Reproducibility Challenges

**Hardware Bottlenecks:** Memory-bound vector-symbolic operations and inefficiencies on standard hardware limit scalability[47]. **Symbol Grounding:** Weak generalization and symbol grounding difficulties hinder reproducibility[42]. **Evaluation Protocols:** Lack of standardized benchmarks and protocols impedes consistent assessment[48][49]. **Hardware-Software Co-Design:** Emerging solutions include in-memory computing, neuromorphic architectures, and FPGA-based accelerators[50][51]. **Synthesis:** Addressing scalability and reproducibility requires both algorithmic innovation and hardware-software co-design[47][50].

## Meta-Cognitive Frameworks and Standardized Evaluation

**Meta-Cognition:** TRAP-inspired and PENLPE frameworks enhance adaptability, self-monitoring, and generalization[42][52]. **Cognitive Dynamic Systems:** Mimic human cognitive processes for dynamic adaptation[53]. **Standardized Benchmarks:** GuardBench and formal verification tools (e.g., NNV) provide emerging protocols for safety and effectiveness assessment[48][54]. **Synthesis:** Meta-cognitive frameworks and standardized evaluation are critical for robust, generalizable neuro-symbolic guardrail systems[42][48].

## Open Research Questions and Future Directions

**Meta-Cognitive Capabilities:** Develop scalable, domain-agnostic meta-cognitive frameworks for self-monitoring and adaptation[42][44].

**Scalable Architectures:** Design efficient, standardized neuro-symbolic architectures for large-scale deployment [42][47]. **Hardware Acceleration:** Explore novel hardware accelerators and memory-centric computing for neuro-symbolic workloads[50][55]. **Comprehensive Guardrails:** Integrate technical, procedural, and human-in-the-loop mechanisms into unified, adaptive guardrail systems[4][13]. **Evaluation Protocols:** Establish universal benchmarks and protocols for guardrail effectiveness and safety[48][49]. **Synthesis:** Addressing these gaps will be critical for advancing safe, interpretable, and reliable AI systems[13][42][44] [47].

## 6. Conclusion

## Summary and Outlook

Recent advances in semantic guardrails and logic-constrained generation demonstrate a clear trend toward hybrid neuro-symbolic architectures and dynamic runtime enforcement mechanisms. State-of-the-art methods leverage RLHF, Constitutional AI, constrained decoding, and neuro-symbolic layers to restrict AI outputs based on deterministic state rules and ensure set containment within symbolic safety envelopes. However, significant challenges remain in scalability, reproducibility, explainability, and integration of ethical frameworks.

Future progress will depend on the development of standardized evaluation protocols, scalable meta-cognitive frameworks, and hardware-software co-design for neuro-symbolic computation. Multidisciplinary collaboration and ongoing research are essential to realize robust, trustworthy, and adaptable AI guardrail systems for real-world deployment[4][13].

## References

1. Reinforcement learning from human feedback (RLHF) Sivan, D., Kumar, S., Raj, V., Jose, R. Generative AI and LLMs: Natural Language Processing and Generative Adversarial Networks, 2024 https://www.scopus.com/pages/publications/85206221951?origin=scopusAI

2. Toward Constitutional Autonomy in AI Systems: A Theoretical Framework for Aligned Agentic Intelligence Torgbi Agbemabiese, W. IEEE Access, 2026 https://www.scopus.com/pages/publications/105027519739?origin=scopusAI

3. Ontology-based adaptive systems of cyber defense Ben-Asher, N., Oltramari, A., Erbacher, R.F., Gonzalez, C. CEUR Workshop Proceedings, 2015 https://www.scopus.com/pages/publications/84962523274?origin=scopusAI

4. Designing Guardrails: Ensuring Responsible AI Behavior Kumar, A. GenAI and LLMs for Beyond 5G Networks, 2026 https://www.scopus.com/pages/publications/105033305087?origin=scopusAI

5. Best Practices for Constructing Knowledge Graphs in Retrieval-Augmented Generation (RAG) Systems Suresh, Y., Hayath, T.M., Begum, S.S. 2025 2nd International Conference on New Frontiers in Communication, Automation, Management and Security, ICCAMS 2025, 2025 https://www.scopus.com/pages/publications/105030077118?origin=scopusAI

6. From vectors to knowledge graphs: A comprehensive analysis of modern retrieval-augmented generation architectures Kamalipour, A.A., Asadi, S., Amiri Chimeh, M.M. Computer Science Review, 2026 https://www.scopus.com/pages/publications/105029641358?origin=scopusAI

7. CRANE: Reasoning with constrained LLM generation Banerjee, D., Suresh, T., Ugare, S., (...), Singh, G. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105023641848?origin=scopusAI

8. Semantic Probabilistic Layers for Neuro-Symbolic Learning Ahmed, K., Teso, S., Chang, K.-W., (...), Vergari, A. Advances in Neural Information Processing Systems, 2022 https://www.scopus.com/pages/publications/85149400784?origin=scopusAI

9. LEARNING WHERE AND WHEN TO REASON IN NEURO-SYMBOLIC INFERENCE Cornelio, C., Stuehmer, J., Hu, S.X., Hospedales, T. 11th International Conference on Learning Representations, ICLR 2023, 2023 https://www.scopus.com/pages/publications/85199873779?origin=scopusAI

10. Neuro-Symbolic Entropy Regularization Ahmed, K., Wang, E., Chang, K.-W., Van den Broeck, G. Proceedings of the 38th Conference on Uncertainty in Artificial Intelligence, UAI 2022, 2022 https://www.scopus.com/pages/publications/85145444329?origin=scopusAI

11. Neuro-Symbolic Entropy Regularization Ahmed, K., Wang, E., Chang, K.-W., Van den Broeck, G. Proceedings of Machine Learning Research, 2022 https://www.scopus.com/pages/publications/85163277441?origin=scopusAI

12. Probabilistic Neural-Symbolic Models With Inductive Posterior Constraints Su, K., Su, H., Li, C., (...), Zhang, B. IEEE Transactions on Neural Networks and Learning Systems, 2024 https://www.scopus.com/pages/publications/85135762069?origin=scopusAI

13. Position: Building Guardrails for Large Language Models Requires Systematic Design Dong, Y., Mu, R., Jin, G., (...), Huang, X. Proceedings of Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85203801484?origin=scopusAI

14. A Framework for a Public Service Recommender System Based on Neuro-Symbolic AI Konstantinidis, I., Magnisalis, I., Peristeras, V. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105020911060?origin=scopusAI

15. Semantic Patterns of Prohibited AI Systems in the EU AI Act Golpayegani, D., Pandit, H.J., Lewis, D. CEUR Workshop Proceedings, 2025 https://www.scopus.com/pages/publications/105019644271?origin=scopusAI

16. PRISM-AI: A Dual-Stage Neuro-Symbolic Agentic Framework for Privacy Risk Mitigation in LLMs Amri, S., Boulahia-Cuppens, N., Cuppens, F. Proceedings of IEEE/ACS International Conference on Computer Systems and Applications, AICCSA, 2025 https://www.scopus.com/pages/publications/105032351736?origin=scopusAI

17. DIESEL: A Lightweight Inference-Time Safety Enhancement for Language Models Ganon, B., Zolfi, A., Hofman, O., (...), Shabtai, A. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 2025 https://www.scopus.com/pages/publications/105028596304?origin=scopusAI

18. CONSCENDI: A Contrastive and Scenario-Guided Distillation Approach to Guardrail Models for Virtual Assistants Sun, A.Y., Nair, V., Schumacher, E., Kannan, A. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL 2024, 2024 https://www.scopus.com/pages/publications/85199487861?origin=scopusAI

19. Driving Disruptive LLM Adoption on Technology Markets with Bug Report-Enhanced Human-Value Alignment in RLHF Nikolova, T., Molhova-Vladova, M. International Conference Automatics and Informatics, ICAI 2025 - Proceedings, 2025 https://www.scopus.com/pages/publications/105033011212?origin=scopusAI

20. UNI-RLHF: UNIVERSAL PLATFORM AND BENCHMARK SUITE FOR REINFORCEMENT LEARNING WITH DIVERSE HUMAN FEEDBACK Yuan, Y., Hao, J., Ma, Y., (...), Zheng, Y. 12th International Conference on Learning Representations, ICLR 2024, 2024 https://www.scopus.com/pages/publications/85196893657?origin=scopusAI

21. Trimodal Thinking for Architecting Human-Centric AI Systems: Fast, Slow, and Control Gill, A.Q. IEEE Transactions on Technology and Society, 2025 https://www.scopus.com/pages/publications/105025453779?origin=scopusAI

22. Co-Creation by Human–AI Sophimatics Framework and Applications Iovane, G., Iovane, G. Algorithms, 2026 https://www.scopus.com/pages/publications/105034007727?origin=scopusAI

23. Security Framework for Agentic Home AI in Preventive Healthcare: Cyber Threats Worth Noting Obeng, C.P., Narasinghe, N.M., Striker, R., Vazquez, E.A. 2025 Cyber Awareness and Research Symposium, CARS 2025, 2025 https://www.scopus.com/pages/publications/105033597106?origin=scopusAI

24. Augmenting Intelligent Process Automation through Generative AI for Human-in-the-Loop Decision Systems Alla, P.B. Digital Engineering, 2026 https://www.scopus.com/pages/publications/105023426495?origin=scopusAI

25. A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges Brown, A., Roman, M., Devereux, B. Big Data and Cognitive Computing, 2025 https://www.scopus.com/pages/publications/105025656636?origin=scopusAI

26. RAG is not the answer An Analytical Review of the Conceptual Limitations of Retrieval-Augmented Generation and its Implications for Forensic Investigations Krawczyk, T., Honekamp, W. Lecture Notes in Informatics (LNI), Proceedings - Series of the Gesellschaft fur Informatik (GI), 2025 https://www.scopus.com/pages/publications/105031168817?origin=scopusAI

27. Enhancing RAG-Retrieval to Improve LLMs Robustness and Resilience to Hallucinations Njeh, C., Nakouri, H., Jaafar, F. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2025 https://www.scopus.com/pages/publications/85207653929?origin=scopusAI

28. Evaluation of LLMs' Reasoning for Retrieval Augmented Generation (RAG) Systems Mulakala, B., Saini, M.L., Bhukya, V., (...), Chand, N.P. 2025 World Skills Conference on Universal Data Analytics and Sciences, WorldSUAS 2025, 2025 https://www.scopus.com/pages/publications/105022295316?origin=scopusAI

29. Evaluating Retrieval-Augmented Generation Variants for Clinical Decision Support: Hallucination Mitigation and Secure On-Premises Deployment Wołk, K. Electronics (Switzerland), 2025 https://www.scopus.com/pages/publications/105021593463?origin=scopusAI

30. Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation Beurer-Kellner, L., Fischer, M., Vechev, M. Proceedings of Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85203788511?origin=scopusAI

31. Adaptable Logical Control for Large Language Models Zhang, H., Kung, P.-N., Yoshida, M., (...), Peng, N. Advances in Neural Information Processing Systems, 2024 https://www.scopus.com/pages/publications/105000534620?origin=scopusAI

32. Coding by Design: GPT-4 Empowers Agile Model Driven Development Sadik, A.R., Brulin, S., Olhofer, M. International Conference on Model-Driven Engineering and Software Development, 2024 https://www.scopus.com/pages/publications/85190369863?origin=scopusAI

33. Certified Deductive Reasoning with Language Models Poesia, G., Gandhi, K., Zelikman, E., Goodman, N.D. Transactions on Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85214721943?origin=scopusAI

34. Enforcing imprecise constraints on generative adversarial networks for emulating physical systems Zeng, Y., Wu, J.-L., Xiao, H. Communications in Computational Physics, 2021 https://www.scopus.com/pages/publications/85110331089?origin=scopusAI

35. Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models Tam, Z.R., Wu, C.-K., Tsai, Y.-L., (...), Chen, Y.-N. EMNLP 2024 - 2024 Conference on Empirical Methods in Natural Language Processing, Proceedings of the Industry Track, 2024 https://www.scopus.com/pages/publications/85213118197?origin=scopusAI

36. "We Need Structured Output": Towards User-centered Constraints on Large Language Model Output Liu, M.X., Liu, F., Fiannaca, A.J., (...), Cai, C.J. Conference on Human Factors in Computing Systems - Proceedings, 2024 https://www.scopus.com/pages/publications/85194170410?origin=scopusAI

37. The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance Schall, M., de Melo, G. International Conference Recent Advances in Natural Language Processing, RANLP, 2025 https://www.scopus.com/pages/publications/105034125174?origin=scopusAI

38. Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts Schmidt, D.M., Cimiano, P. Frontiers in Artificial Intelligence, 2024 https://www.scopus.com/pages/publications/85215524351?origin=scopusAI

39. Watchdogs and Oracles: Runtime Verification Meets Large Language Models for Autonomous Systems Ferrando, A. Electronic Proceedings in Theoretical Computer Science, EPTCS, 2025

https://www.scopus.com/pages/publications/105023156059?origin=scopusAI

40. Probabilistic neural-symbolic models for interpretable visual question answering Vedantam, R., Desai, K., Lee, S., (...), Parikh, D. 36th International Conference on Machine Learning, ICML 2019, 2019 https://www.scopus.com/pages/publications/85078028204?origin=scopusAI

41. Probabilistic Neural-symbolic Models for Interpretable Visual Question Answering Vedantam, R., Desai, K., Lee, S., (...), Parikh, D. Proceedings of Machine Learning Research, 2019 https://www.scopus.com/pages/publications/105020257487?origin=scopusAI

42. Neuro-symbolic agentic AI: Architectures, integration patterns, applications, open challenges and future research directions Hakim, S.B., Adil, M., Velasquez, A., Song, H.H. Computer Science Review, 2026 https://www.scopus.com/pages/publications/105029047807?origin=scopusAI

43. A review of neuro-symbolic AI integrating reasoning and learning for advanced cognitive systems Nawaz, U., Anees-ur-Rahaman, M., Saeed, Z. Intelligent Systems with Applications, 2025 https://www.scopus.com/pages/publications/105007106617?origin=scopusAI

44. Neuro-Symbolic AI in 2024: A Systematic Review Colelough, B.C., Regli, W. CEUR Workshop Proceedings, 2024 https://www.scopus.com/pages/publications/85209357516?origin=scopusAI

45. Artificial Intelligence techniques based on the integration of symbolic logic and deep neural networks: A systematic literature review Negro, P., Pons, C. Inteligencia Artificial, 2022 https://www.scopus.com/pages/publications/85126808479?origin=scopusAI

46. A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability Acharya, K., Song, H. Arabian Journal for Science and Engineering, 2025 https://www.scopus.com/pages/publications/105024318310?origin=scopusAI

47. Towards Cognitive AI Systems: Workload and Characterization of Neuro-Symbolic AI Wan, Z., Liu, C.-K., Yang, H., (...), Raychowdhury, A. Proceedings - 2024 IEEE International Symposium on Performance Analysis of Systems and Software, ISPASS 2024, 2024 https://www.scopus.com/pages/publications/85191076521?origin=scopusAI

48. GuardBench: A Large-Scale Benchmark for Guardrail Models Bassani, E., Sanchez, I. EMNLP 2024 - 2024 Conference on Empirical Methods in Natural Language Processing, Proceedings of the Conference, 2024 https://www.scopus.com/pages/publications/85217749850?origin=scopusAI

49. Effective Continuous Quantitative Measures for End-to-End AI Guardrails Pittman, J. Proceedings of the 4th International Conference on AI Research, ICAIR 2024, 2024 https://www.scopus.com/pages/publications/85215695720?origin=scopusAI

50. Efficient Neuro-Symbolic Policy using In-Memory Computing Molom-Ochir, T., Saxena, N., Kim, J., (...), Helen, H. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105014733669?origin=scopusAI

51. Efficient Processing of Neuro-Symbolic AI: A Tutorial and Cross-Layer Co-Design Case Study Wan, Z., Liu, C.- K., Yang, H., (...), Krishna, T. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105014742893?origin=scopusAI

52. Cognitive system management: The Polymorphic, Evolutionary, Neural Learning and Processing Environment (PENLPE) Crowder, J.A. AIAA SPACE Conference and Exposition 2012, 2012 https://www.scopus.com/pages/publications/84880968951?origin=scopusAI

53. Cognitive Dynamic Systems: A Review of Theory, Applications, and Recent Advances Hilal, W., Andrew Gadsden, S., Yawney, J. Proceedings of the IEEE, 2023 https://www.scopus.com/pages/publications/85162798746?origin=scopusAI

54. Tutorial: Safe, Secure, and Trustworthy Artificial Intelligence (AI) via Formal Verification of Neural Networks and Autonomous Cyber-Physical Systems (CPS) with NNV Johnson, T.T., Lopez, D.M., Tran, H.-D. Proceedings - 2024 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks - Supplemental Volume, DSN-S 2024, 2024 https://www.scopus.com/pages/publications/85203803070?origin=scopusAI

55. Towards efficient and reliable artificial intelligence through neuromorphic principles Rajendran, B., Simeone, O., Al-Hashimi, B. Philosophical transactions. Series A, Mathematical, physical, and engineering sciences, 2026 https://www.scopus.com/pages/publications/105031737963?origin=scopusAI
