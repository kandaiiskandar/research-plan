---
source_pdf: "Scopus - Scopus AI - 1.pdf"
source_sha256: "fc766505cf73a743d258658bb3eb766e28279fcf6d1850443b103f06875f08b3"
source_pages: 11
scopus_ai_generated: "Mon Nov 16 2026"
query: "Incremental safety benefits of AI restrictions"
report_title: "Incremental Safety Benefits of Intermediate and Action-Specific AI Restrictions Versus Binary Gating: A Comparative Review"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Incremental safety benefits of AI restrictions

## Quick Reference

## Key Findings Table

| Study (Title, Authors, Year, DOI) | Methods | Safety Metrics | Main Findings | Safety Outcomes vs. Rule Compliance |
| --- | --- | --- | --- | --- |
| No direct studies identified | N/A | N/A | No peer-reviewed studies have directly isolated and measured the incremental safety benefit of intermediate or action-specific AI restrictions compared to binary gating. | N/A |
| Indirect evidence: refusal-aware evaluation, partial compliance, operational safety frameworks, composite indices (SA-ROC, CAVe) | Simulation, scenario-based, compliance frameworks | Accuracy, refusal rate, composite indices (CCI, Gray Zone Area), robustness, fairness | Intermediate restrictions (e.g., refusal mechanisms) impact safety and user experience differently than binary gating; composite indices and frameworks can distinguish safety from compliance but lack empirical validation in real-world deployments. | Frameworks like SA-ROC and CAVe attempt to distinguish, but robust empirical validation is lacking. |

## Direct Answer

Based on the current body of research, **no peer-reviewed studies have isolated and directly measured the** **incremental safety benefit of intermediate or action-specific AI restrictions compared to binary** **(on/off) gating**. Most studies address broader AI safety concerns, regulatory compliance, and ethical frameworks without conducting targeted experimental comparisons. Indirect evidence suggests that intermediate restrictions (e.g., refusal mechanisms, partial compliance) can affect safety outcomes and user experience, but these effects have not been systematically isolated or quantified in direct comparison to binary gating in real-world deployments[1][2][3][4][5][6].

## Unable to Find

No direct, peer-reviewed experimental studies isolating and measuring the incremental safety benefit of intermediate or action-specific AI restrictions versus binary gating.

## Study Scope

**Time period:** 2018–2024 **Disciplines:** AI safety, human-AI interaction, regulatory science, healthcare, autonomous vehicles, digital health, safety engineering **Methods:** Systematic reviews, simulation studies, scenario-based testing, compliance frameworks, composite safety indices, refusal-aware evaluation

## Assumptions & Limitations

The review is limited by the absence of direct comparative studies; findings are synthesized from indirect evidence and related frameworks. Methodological heterogeneity and lack of standardized safety metrics limit cross-study comparability. Most evidence is drawn from high-level frameworks, simulation, and domain-specific case studies rather than controlled, real-world experiments.

## Suggested Further Research

Controlled, domain-specific experimental designs to isolate and quantify the incremental benefits of action-specific AI safety restrictions over binary gating. Development and validation of standardized benchmarks and composite safety indices across domains. Integration of technical safety measures with socio-technical governance, adaptive monitoring, and human-in-the-loop approaches. Empirical studies distinguishing independent safety outcomes from rule compliance.

## 1. Introduction

## Background and Motivation

The rapid deployment of AI systems in safety-critical domains—such as healthcare, autonomous vehicles, and digital infrastructure—has intensified scrutiny of their safety mechanisms. Traditionally, binary (on/off) gating has been the default approach for restricting AI actions in high-risk scenarios. However, this approach is increasingly viewed as blunt and potentially suboptimal, prompting interest in intermediate or action-specific restrictions (e.g., refusal mechanisms, partial compliance, context-aware gating) that may offer more nuanced risk management[1][2][3].

Despite the theoretical appeal of these intermediate strategies, the literature reveals a striking lack of direct empirical studies that isolate and measure their incremental safety benefits compared to binary gating. Most

research focuses on general safety, regulatory compliance, or ethical frameworks, rather than targeted experimental comparisons. Understanding the true safety impact of these restrictions—distinct from mere rule compliance—remains a critical, unresolved challenge[1][2][3][4].

**2. Current Evidence on Incremental Safety Benefits of AI Restrictions**

## Literature Landscape and Key Studies

## Absence of Direct Comparative Studies

A comprehensive review of the literature confirms that **no peer-reviewed studies have directly isolated** **and measured the incremental safety benefit of intermediate or action-specific AI restrictions** **compared to binary gating**. Instead, the field is characterized by: General discussions of AI safety and risk management[1][7] Evaluations of refusal mechanisms and partial compliance strategies[2][4] Operational safety frameworks and composite indices (e.g., SA-ROC, CAVe)[5][6] Domain-specific case studies in healthcare, autonomous vehicles, and digital health[8][9][10]

## Indirect Evidence: Refusal Mechanisms and Safety Controls

**Refusal-aware evaluation**: Studies show that AI models with refusal mechanisms can achieve high accuracy (e.g., 99%) on non-refused queries, but with significant refusal rates (e.g., 29%), indicating that intermediate restrictions affect both safety and user experience differently than binary gating[2].

**Partial compliance**: Providing high-level guidance instead of full refusal reduces negative user perceptions by over 50% compared to flat refusals, suggesting that intermediate restrictions can improve user experience while maintaining safety[4].

**Operational safety frameworks**: Emphasize embedding multiple safety controls (e.g., permission scoping, rate limiting, circuit breakers) rather than relying solely on binary gating[11].

## Domain-Specific Insights and Case Studies

**Healthcare**: Simulation-based studies and clinical trials often compare AI interventions to standard care but do not isolate the effects of intermediate restrictions versus binary gating[9][10].

**Autonomous vehicles**: Discrete-event simulation and scenario-based testing are used to benchmark safety outcomes, but direct comparisons of restriction types are lacking[8].

**Digital health**: Lifecycle-oriented monitoring and refusal-aware evaluation are highlighted as important, but incremental safety benefits of intermediate restrictions remain unquantified[12][13].

## Synthesis

While indirect evidence suggests that intermediate or action-specific restrictions can influence safety outcomes and user experience, the field lacks direct, controlled studies that quantify these effects relative to binary gating. Theoretical frameworks and simulation studies provide valuable insights but fall short of empirical validation in real-world deployments[1][2][3][4][5][6].

## 3. Methodologies and Safety Metrics in AI Safety Evaluation

## Methodological Approaches

**Systematic reviews**: Synthesize evidence across domains but often lack focus on specific restriction types [6][14][15][16][17].

**Simulation and scenario-based testing**: Used in healthcare and autonomous vehicles to benchmark safety outcomes under different AI strategies[8][9].

**Compliance frameworks**: Map regulatory requirements to measurable indicators (e.g., Cross- Compliance Index in CAVe)[6].

**Composite indices**: Integrate multiple safety metrics (accuracy, robustness, fairness, explainability) for holistic assessment[6][18][19][20].

## Safety Metrics: Definitions and Applications

**Accuracy**: Standard metric, but can be misleading if refusals or indecisions are not accounted for[2]. **Refusal rate**: Quantifies the frequency of AI abstaining from action; high refusal rates can indicate over-cautiousness or safety optimization at the expense of utility[3]. **Composite indices**: E.g., Cross-Compliance Index (CCI) in CAVe, Gray Zone Area in SA-ROC, which aggregate multiple safety dimensions and operational costs[5][6]. **Robustness, fairness, explainability**: Increasingly integrated into safety assessments, especially in high-stakes domains[6][18][19][20].

## Comparative Strengths and Limitations

**Strengths**: Composite indices enable multi-dimensional safety assessment and alignment with regulatory requirements[6][18]. Scenario-based and simulation methods allow for controlled benchmarking of safety outcomes[8][9].

**Limitations**: Lack of standardization and external validation limits comparability across studies[18][19][21][22][23]. Domain specificity of metrics and indices hinders cross-domain generalization[24][25][26][27]. Overreliance on compliance metrics can obscure true safety outcomes[18][28][29].

## Composite Safety Indices and Cross-Domain Validation

**CAVe (Cross-Assessment & Verification for Evaluation)**: Maps regulatory requirements to technical indicators, aggregates into a CCI, and applies domain-specific weighting[6].

**SA-ROC (Safety-Aware Receiver Operating Characteristic)**: Defines operational safety zones and quantifies the cost of indecision (Gray Zone Area), distinguishing safety from compliance[5].

**Domain-specific indices**: E.g., surrogate safety measures in traffic, patient safety indicators in healthcare, but lack universal standardization[24][25][26][27].

## Synthesis

Methodological heterogeneity and lack of standardized, validated safety metrics remain major barriers to isolating and comparing the incremental benefits of different AI restriction strategies. Composite indices and scenario-based methods offer promise but require further empirical validation and cross-domain harmonization[5][6][18].

**4. Distinguishing Independent Safety Outcomes from Rule Compliance**

## Conceptual Distinctions and Research Gaps

**Independent safety outcomes**: Focus on actual harm prevention and system reliability, regardless of regulatory or ethical rule adherence[30][31].

**Rule compliance**: Emphasizes adherence to predefined standards, which may not guarantee real-world safety[30][31].

**Research gaps**: Lack of standardized benchmarks and validation methods for independent safety outcomes; overemphasis on compliance metrics; limited cross-disciplinary collaboration[15][16][23][32].

## Frameworks for Independent Safety Validation

**SA-ROC**: Quantifies operational safety by defining zones for autonomous action, human review, and indecision, measuring the operational cost of indecision (Gray Zone Area)[5].

**CAVe**: Aggregates technical indicators into a Cross-Compliance Index, enabling transparent evaluation of safety compliance and distinguishing it from technical performance[6].

**Integrated safety and alignment frameworks**: Merge technical safety measures with socio-technical governance, emphasizing adaptability and human-in-the-loop monitoring[5][6][32].

## Empirical Techniques and Assurance Methods

**Scenario-based testing**: Exposes AI systems to critical and rare safety scenarios, improving robustness assessment beyond compliance[33].

**Simulation and continuous monitoring**: Allow for comprehensive evaluation of safety performance across diverse scenarios and operational conditions[34].

**Human-in-the-loop (HITL) frameworks**: Enable continuous performance monitoring and adaptation post-deployment, capturing real-world error patterns[35][36][37].

## Synthesis

Distinguishing true safety outcomes from rule compliance is a recognized challenge. Frameworks like SA- ROC and CAVe provide quantitative tools for this distinction, but robust empirical validation—especially in real-world deployments—remains lacking. Adaptive, continuous monitoring and HITL approaches are emerging as promising strategies for independent safety validation[5][6][35][36].

## 5. Unresolved Research Gaps and Future Directions

## Gaps in Experimental and Comparative Evidence

**No direct experimental studies**: The literature lacks controlled, domain-specific experiments isolating and quantifying the incremental benefits of intermediate or action-specific AI restrictions over binary gating[1][7][15][38].

**Methodological heterogeneity**: Diverse study designs and metrics hinder cross-study comparability and generalizability[23][39][40][41].

**Integration of technical and socio-technical safety validation**: Need for frameworks that combine technical safety measures with adaptive governance, continuous monitoring, and human oversight[32][35] [36][37].

## Recommendations for Future Research

**Experimental designs**: Develop controlled, domain-specific studies to isolate and measure the incremental safety benefits of intermediate restrictions versus binary gating[15][23][30][42].

**Standardized benchmarks**: Create and validate composite safety indices applicable across domains, enabling robust cross-study comparisons[24][25][26][27].

**Multidisciplinary collaboration**: Foster integration of safety engineering, regulatory science, and human factors into AI safety research[15][32][43].

**Adaptive, human-in-the-loop frameworks**: Implement continuous monitoring and oversight to validate safety outcomes independently from compliance[35][36][37].

## Synthesis

The field urgently needs empirical, domain-specific research to quantify the incremental safety benefits of intermediate AI restrictions. Standardization of metrics and integration of technical and socio-technical approaches are essential for advancing both the science and practice of AI safety[1][22][30].

## 6. Conclusion

## Summary of Insights

**No direct evidence**: There are no peer-reviewed studies that have directly isolated and measured the incremental safety benefit of intermediate or action-specific AI restrictions compared to binary gating[1] [2][3].

**Indirect evidence**: Refusal mechanisms, partial compliance, and composite indices suggest that intermediate restrictions can impact safety and user experience, but these effects are not systematically quantified[2][4][5][6].

**Distinguishing safety from compliance**: Frameworks like SA-ROC and CAVe provide tools for distinguishing independent safety outcomes from rule compliance, but empirical validation is lacking[5] [6].

**Research gaps**: The field lacks controlled, comparative studies, standardized metrics, and integrated technical-socio-technical validation frameworks.

**Future directions**: Emphasize experimental research, standardized benchmarks, multidisciplinary collaboration, and adaptive, human-in-the-loop safety validation.

**In summary**, while the theoretical and practical importance of intermediate and action-specific AI restrictions is widely recognized, the field lacks direct empirical evidence quantifying their incremental safety benefits over binary gating. Addressing this gap will require rigorous experimental designs, standardized metrics, and integrated frameworks that distinguish true safety outcomes from mere rule compliance[1][22][30].

## References

1. Generative AI and Large Language Models in Rehabilitation: A Scoping Review Cha, S.-M. Life, 2026 https://www.scopus.com/pages/publications/105048438827?origin=scopusAI

2. Refusal-aware evaluation of frontier AI models available in June 2026 using the Japanese National License Examination for Pharmacists: a comparative study Sato, H., Ogasawara, K., Sakurai, H. Journal of Educational Evaluation for Health Professions, 2026 https://www.scopus.com/pages/publications/105049066543?origin=scopusAI

3. Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context Zhang, Z., Huang, L., Wu, G., (...), Naseem, U. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 2026 https://www.scopus.com/pages/publications/105053542769?origin=scopusAI

4. Let Them Down Easy! Contextual Effects of LLM Guardrails on User Perceptions and Preferences Zheng, M., Hu, W., Zhao, P., (...), Sap, M. EMNLP 2025 - 2025 Conference on Empirical Methods in Natural Language Processing, Findings of EMNLP 2025, 2025 https://www.scopus.com/pages/publications/105028953387?origin=scopusAI

5. Defining operational safety in clinical artificial intelligence systems Kim, Y.-T., Kim, H., Bahl, M., (...), Do, S. npj Digital Medicine, 2026 https://www.scopus.com/pages/publications/105035569244?origin=scopusAI

6. Cross-Assessment & Verification for Evaluation (CAVe) Framework for AI Risk and Compliance Assessment Using a Cross-Compliance Index (CCI) Min, C.-H., Lee, D.-G., Kwak, J. Electronics (Switzerland), 2026 https://www.scopus.com/pages/publications/105028656618?origin=scopusAI

7. Empirically derived evaluation requirements for responsible deployments of AI in safety-critical settings Morey, D.A., Rayo, M.F., Woods, D.D. npj Digital Medicine, 2025 https://www.scopus.com/pages/publications/105008735288?origin=scopusAI

8. Beyond block time: a head-to-head comparison of reinforcement learning, genetic algorithms, and predict-then-optimize scheduling for operating room workflow using discrete-event simulation Çalışkan, Y.K., Başak, F., Erdem, O., Kudaş, İ. International Journal of Medical Informatics, 2026 https://www.scopus.com/pages/publications/105034730881?origin=scopusAI

9. TITE-safety: a robust time-to-event safety monitoring approach for clinical trials Martens, M.J., Lian, Q., Logan, B.R. Biometrics, 2026 https://www.scopus.com/pages/publications/105040601853?origin=scopusAI

10. The Analytical Framework of Clinical Trials Evaluating Clinical Outcomes of Artificial Intelligence- Based Digital Health Interventions: A Systematic Literature Review Zah, V., Grbic, D., Asche, C., Stanicic, F. Journal of Market Access and Health Policy, 2026 https://www.scopus.com/pages/publications/105046850492?origin=scopusAI

11. Operational Safety for AI Systems: A Framework for Managing Risk in Production Qi, C., Qiao, X. Proceedings of the 2026 2nd International Conference on Sustainable Development and Digital Transformation, SDDT 2026, 2026 https://www.scopus.com/pages/publications/105055161872?origin=scopusAI

12. Validation is not enough: Longitudinal evidence of post-deployment fragility in clinical AI systems Kopanitsa, G. PLOS Digital Health, 2026 https://www.scopus.com/pages/publications/105050397096?origin=scopusAI

13. Four Aspirations for Evaluating AI-Infused Technologies: A Narrative Review Morey, D.A., Jalaeian, M., Reynolds, M.E., (...), Rayo, M.F. Journal of Cognitive Engineering and Decision Making, 2026 https://www.scopus.com/pages/publications/105036244793?origin=scopusAI

14. Artificial Intelligence in Occupational Health and Safety: A Systematic Review of Applications, Impacts, and Ethical Considerations Tapia, J., Martínez-Pérez, R.-G., Herrera, Y., Garcia, M.V. Lecture Notes in Networks and Systems, 2026 https://www.scopus.com/pages/publications/105026998255?origin=scopusAI

15. Systematic Review on AI Safety and Future Research Agenda Zhang, S., Lu, H. 2025 7th International Conference on System Reliability and Safety Engineering, SRSE 2025, 2025 https://www.scopus.com/pages/publications/105032891078?origin=scopusAI

16. Safety Assurance of Artificial Intelligence-Based Systems: A Systematic Literature Review on the State of the Art and Guidelines for Future Work Neto, A.V.S., Camargo, J.B., Almeida, J.R., Cugnasca, P.S. IEEE Access, 2022 https://www.scopus.com/pages/publications/85144813199?origin=scopusAI

17. Responsible AI in Construction Safety: Systematic Evaluation of Large Language Models and Prompt Engineering Sammour, F., Xu, J., Wang, X., (...), Zhang, Z. Journal of Construction Engineering and Management, 2026 https://www.scopus.com/pages/publications/105019749357?origin=scopusAI

18. SAFE AI metrics: An integrated approach Giudici, P., Kolesnikov, V. Machine Learning with Applications, 2026 https://www.scopus.com/pages/publications/105027870181?origin=scopusAI

19. A statistical package for safe artificial intelligence Babaei, G., Giudici, P. Statistical Methods and Applications, 2025 https://www.scopus.com/pages/publications/105007246865?origin=scopusAI

20. A Uniform Language for Safety, Robustness and Explainability Belle, V., Barcelo, P. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105023401114?origin=scopusAI

21. Avoiding the Formalism Trap: A Critical Evaluation and Selection of Statistical Fairness Metrics in Public Algorithms Mc Manus, A.C., Ortiz, M.G., Soto, R.T. Revista de Estudios Sociales, 2025 https://www.scopus.com/pages/publications/105012730689?origin=scopusAI

22. Survey of Trustworthy AI Frameworks: Interpretability, Fairness, and Robustness Across Domains Tripathi, S. AI for Decision Intelligence in Critical Systems, 2026 https://www.scopus.com/pages/publications/105044129051?origin=scopusAI

23. Role of artificial intelligence in patient safety outcomes: Systematic literature review Choudhury, A., Asan, O. JMIR Medical Informatics, 2020 https://www.scopus.com/pages/publications/85097462126?origin=scopusAI

24. A framework for reliable traffic surrogate safety assessment based on multi-object tracking data Steinmaßl, M., Beeking, M., Troth, N., Rehrl, K. Traffic Safety Research, 2025 https://www.scopus.com/pages/publications/105028183368?origin=scopusAI

25. A New Ordinal Framework for Real-Time Traffic Risk Assessment Using an Integrated Surrogate Safety Measure Naseralavi, S., Soltanirad, M., Piri, M., (...), Mazaheri, A. IEEE Access, 2026 https://www.scopus.com/pages/publications/105043739338?origin=scopusAI

26. Validating ICD-10 Algorithms for Identifying Patient Safety Indicators Through 10, 655 Charts Review Wu, G., Pan, J., Southern, D.A., (...), Quan, H. Medical Care, 2026 https://www.scopus.com/pages/publications/105035121605?origin=scopusAI

27. BM-ACT: Behavior and Map-Aware Anticipated Collision Time and Fine-Grained Validation for Driving Risk Assessment Xie, C., Lin, C., Zheng, X., (...), López, A.M. IEEE Transactions on Vehicular Technology, 2026 https://www.scopus.com/pages/publications/105043121568?origin=scopusAI

28. Artificial Intelligence in Regulatory Compliance: Comparative Analysis of Benefits and Challenges Ghantous, G.B. Lecture Notes in Networks and Systems, 2027 https://www.scopus.com/pages/publications/105053436796?origin=scopusAI

29. SCRAM: A Scenario-Based Framework for Evaluating Regulatory and Fairness Risks in AI Surveillance Systems Kesgin, K., Kosunalp, S., Beloev, I. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105014415174?origin=scopusAI

30. Designing AI to Prevent Harm (Safety) Andrae, S. AI Safety and Preventing Harm in AI Systems, 2026 https://www.scopus.com/pages/publications/105031334967?origin=scopusAI

31. How Can We Make AI Understand Safety? Stathis, M., Marc, B., Anthony, S., Erwin, L. SpringerBriefs in Applied Sciences and Technology, 2027 https://www.scopus.com/pages/publications/105051829240?origin=scopusAI

32. Safety and Alignment Frameworks for High- Autonomy AI Systems Chatterjee, S., Bansal, P., Shrivastva, R., Shah, N. 2026 IEEE/ACIS 24th International Conference on Software Engineering Research, Management and Applications, SERA 2026, 2026 https://www.scopus.com/pages/publications/105047280141?origin=scopusAI

33. Toward Standardized Benchmarking of Search-Based Scenario Selection Methods in Autonomous System Validation Autenrieth, D., Paland, D., Mentjes, J., Zlocki, A. Journal of Marine Science and Engineering, 2026 https://www.scopus.com/pages/publications/105047279341?origin=scopusAI

34. Safety validation for connected autonomous vehicles using large-scale testing tracks in high-fidelity simulation environment Xu, Z., Wang, X., Wang, X., Zheng, N. Accident Analysis and Prevention, 2025 https://www.scopus.com/pages/publications/105000049532?origin=scopusAI

35. A Human-in-the-Loop Monitoring and Validation Framework for AI-Based ECG Annotation Systems Kontou, A., Miroshnikova, N., Matheou, C., (...), Kolios, P. 2026 15th Asian Control Conference, ASCC 2026, 2026 https://www.scopus.com/pages/publications/105054243560?origin=scopusAI

36. Adaptive Human Oversight for Maritime Agentic AI Systems: Balancing Operator Workload and Safety Through Risk-Aware Governance Miller, T., Durlik, I., Biczak, P. Applied Sciences (Switzerland), 2026 https://www.scopus.com/pages/publications/105045853571?origin=scopusAI

37. Co-Lifecycle Governance for Learning Medical AI: A Hybrid Convergence Framework for Adaptive Regulatory Oversight Lee, J.H., Choi, B., Jeong, K., (...), Son, D.-S. Journal of Medical Internet Research, 2026 https://www.scopus.com/pages/publications/105039744005?origin=scopusAI

38. A new four-arm within-study comparison: Design, implementation, and data Keller, B., Wong, V.C., Park, S., (...), Steiner, P.M. Observational Studies, 2025 https://www.scopus.com/pages/publications/105011851226?origin=scopusAI

39. Artificial Intelligence for Drug Safety Across the Lifecycle and Decision Type: A Scoping Review Kim, T.W., Park, S., Kim, M. Pharmaceuticals, 2026 https://www.scopus.com/pages/publications/105031112365?origin=scopusAI

40. AI Safety Assurance for Automated Vehicles: A Survey on Research, Standardization, Regulation Ullrich, L., Buchholz, M., Dietmayer, K., Graichen, K. IEEE Transactions on Intelligent Vehicles, 2025 https://www.scopus.com/pages/publications/105021531239?origin=scopusAI

41. Decoding the safety matrix: A conceptualisation of safety indicator-based variables for highway prediction models Bortey, L., Edwards, D.J., Roberts, C., Rillie, I.M. Journal of Traffic and Transportation Engineering (English Edition), 2026 https://www.scopus.com/pages/publications/105042578545?origin=scopusAI

42. Establish legal and regulatory standards for the testing and validation of AI systems to ensure their reliability and safety in operational environments Ranjitsingh, L.M., Rao, T.V.S. International Journal of System Assurance Engineering and Management, 2025 https://www.scopus.com/pages/publications/105009425998?origin=scopusAI

43. AI Safety Firmansyah, R. Encyclopedia of Modern Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105050678787?origin=scopusAI
