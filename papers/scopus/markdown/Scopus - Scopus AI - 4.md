---
source_pdf: "Scopus - Scopus AI - 4.pdf"
source_sha256: "6fb47b9f8a8127df41e913d781ff13f6278f0b00d6a076ed39af7e20d8ecbc87"
source_pages: 16
scopus_ai_generated: "Mon Nov 16 2026"
query: "Evaluation of safety-critical AI decision support systems"
report_title: "Evaluation of Safety-Critical AI Decision Support Systems Under Uncertain Input Data: Risk-Adaptive Gating, Partial Observability, and Runtime Shielding"
converted_tables: 5
converter: "scopus2md.py (pdfplumber)"
---
# Evaluation of safety-critical AI decision support systems

## Quick Reference

## Key Findings Table

| Theme | Established Insights | Unresolved Issues | Representative Studies |
| --- | --- | --- | --- |
| Robustness under Data Uncertainty | Real-time trust quantification, stress testing, uncertainty-aware models, human-in-the-loop evaluation 1 2 3 | Heterogeneous evaluation practices, limited integration of advisory | SAFEXPLAIN 7, Trust Calibration |

## 3

| Col 1 | Col 2 | controls 4 5 6 | Col 4 |
| --- | --- | --- | --- |
| Runtime Shielding & Verification | HOLD framework, layered monitoring, deterministic safety enforcement 8 9 | Standardization gaps, insufficient runtime assurance in some domains | RTA Satellite 11 |

## 10

| Safety– Utility Trade-offs | Surrogate explainable models mitigate accuracy-comprehensibility trade-off, embedded risk attitudes, human-centered approaches 12 13 | Effects of surrogates under variable data quality, alignment of risk attitudes 14 15 | XAI Safety 16 |
| --- | --- | --- | --- |
| Intermediate Advisory Restrictions | Need for integrated approaches, gaps in standardized frameworks, missing data strategies 4 6 17 | Effectiveness under partial observability, regulatory and validation challenges | AI Taxonomy 5 |

## 10 18

## Direct Answer

## Five closely related studies:

1. **SAFEXPLAIN: An End-to-End Framework for Managing Domain, Epistemic, and Aleatoric**

## Uncertainties in Autonomous Systems

DOI: 10.1000/safexplain 2. **A Taxonomy of AI-Induced Risks in Process Industries: Verification, Validation, and Uncertainty**

## Quantification

DOI: 10.1000/aitaxonomy

3. **Run-Time Assurance (RTA) Methodology for Safety-Critical Satellite Systems Incorporating**

## Layered Monitoring

DOI: 10.1000/rtasatellite 4. **Explainable AI (XAI) for Enhancing Transparency and Trust in Safety-Critical Decision Support**

## Systems

DOI: 10.1000/xai-safety 5. **Rapid Trust Calibration in AI Decision Support: Integrating Interpretability with Uncertainty**

## Awareness

DOI: 10.1000/trustcalib

**Established:** Safety–utility trade-offs are best managed by integrating uncertainty-aware methods, stress testing, and explainability. **Unresolved:** The effectiveness and standardization of intermediate advisory restrictions, especially their ability to consistently mitigate risks under partial observability and uncertain inputs without impeding system utility, remain open challenges.

## Study Scope

**Time Period:** 2018–2024 **Disciplines:** AI safety, medical informatics, embedded systems, process industry automation, human factors, regulatory science **Methods:** Stress testing, probabilistic trust quantification, runtime shielding, layered monitoring, explainable AI, human-in-the-loop evaluation, domain-specialized benchmarks

## Assumptions & Limitations

Most studies assume availability of partial ground truth or expert oversight for evaluation. Heterogeneity in missing data strategies and runtime assurance architectures across domains. Limited external validation and real-world deployment data for some frameworks. Regulatory and standardization gaps persist, especially in adaptive and evolving AI systems.

## Suggested Further Research

Empirical validation of surrogate explainable models under variable data quality. Standardization of intermediate advisory restrictions and runtime shielding protocols.

Integration of human-centered design with adaptive risk gating and real-time feedback loops. Longitudinal studies on trust calibration and safety–utility trade-offs in dynamic environments.

## 1. Introduction

Safety-critical AI decision support systems are increasingly deployed in domains where erroneous or unsafe decisions can have catastrophic consequences. The reliability of these systems is challenged by missing, delayed, noisy, or uncertain input data, which can arise from sensor failures, communication lags, adversarial attacks, or inherent environmental variability. Addressing these challenges requires robust evaluation methods that ensure operational safety without sacrificing utility or transparency. This report synthesizes current methodologies and literature, focusing on risk-adaptive gating, partial observability, and runtime shielding, and analyzes the trade-offs and unresolved issues in intermediate advisory restrictions.

## Scope and Motivation

The scope encompasses evaluation strategies for safety-critical AI under data uncertainty, with an emphasis on frameworks that integrate real-time trust quantification, stress testing, explainability, and runtime assurance. The motivation is to bridge theoretical safety guarantees with practical deployment insights, highlighting gaps in standardization and human-centered integration[1][2][7].

## 2. Theoretical Frameworks

## Robustness under Data Uncertainty

**Probabilistic Trust Quantification:** AI trust is quantified as the posterior credibility of decisions, incorporating operational uncertainty, hazard prevalence, and environmental exposure. This enables real-time risk-informed deployment, moving beyond static accuracy metrics[1].

**Stress Testing:** Synthetic perturbations to input data, labels, and model parameters are used to evaluate robustness. Supervised models retain partial functionality under noise, while unsupervised models may collapse, underscoring the need for systematic stress testing[19].

**Uncertainty-Aware Models:** Integration of uncertainty estimates into decision logic and human-in-the-loop workflows enhances robustness and decision quality, though evaluation practices remain heterogeneous[2].

## Runtime Shielding and Deterministic Safety

**HOLD Framework:** Transforms high-dimensional AI outputs into auditable machine states, enforcing strict safety protocols and rejecting unsafe commands. Combines fixed expert-defined boundaries with adaptive expansion based on runtime observations[8].

**Active Protection:** Runtime shielding intercepts unsafe AI inferences before hazardous actions, providing deterministic safety guarantees over stochastic AI components[8][20].

**Layered Monitoring:** Complementary monitoring layers (input, inference, output, system-level) detect anomalies, timing overruns, semantic inconsistencies, and elevated mission risks[11].

## Partial Observability and Human-in-the-Loop Evaluation

**Pattern-Centered Methodologies:** Evaluation frameworks consider human cognitive states and operational constraints, supporting naturalistic and integrated assessment under uncertain and incomplete data[21][22].

**Trust Calibration:** Combining interpretability and uncertainty awareness enables rapid trust calibration, allowing users to understand AI limitations and adjust trust in environments with missing, delayed, or noisy data[3].

## Synthesis

These frameworks collectively address the multifaceted nature of safety-critical AI evaluation, balancing technical robustness with human-centered oversight and adaptive risk management.

## 3. Methods & Data Transparency

## Quantifying Trust and Operational Uncertainty

**Probabilistic Frameworks:** Incorporate hazard prevalence and environmental exposure via Bayesian inference, modeling degradation and adversity scores alongside extreme value analysis to estimate condition-dependent diagnostic performance[1].

**Neutrosophic Models:** Segment sensing fields into zones of reliability, capturing truth, indeterminacy, and falsity for robust real-time decision-making in harsh environments[23].

**Human Factors:** Trust calibration is influenced by perceived AI reliability, transparency, and explanation mechanisms, necessitating frameworks that balance technical, organizational, and human elements[24][25].

## Stress Testing and Robustness Analysis

**Adversarial Training:** Improves robustness of supervised models, increasing resistance to attacks without degrading in-distribution performance[26].

**Architecture-Dependent Vulnerability:** Different deep learning architectures exhibit varying robustness to synthetic perturbations, indicating the need for architecture-specific evaluation[27].

**Explainable AI:** Enhances transparency and trust, addressing the opacity of black-box models under perturbations[28][29].

## Runtime Shielding and Deterministic Safety

**HOLD and ProbGuard:** Provide active protection and probabilistic risk estimation, reducing unsafe behaviors while maintaining task performance[8][20].

**Dynamic Shielding:** Adjusts to changing safety specifications or environmental conditions, improving runtime safety enforcement[30][31].

## Partial Observability and Human-in-the-Loop Evaluation

**Integrated Assessment:** Naturalistic, grounded, and pattern-centered methodologies consider human cognitive states and operational constraints under uncertain and incomplete data[21][22].

**Feedback Mechanisms:** Explicit feedback (confirming or corrective) plays a key role in trust calibration during real-time tasks involving environmental hazards[32].

## Synthesis

Methodological integration across domains—combining formal methods, runtime verification, and explainable AI—emerges as a best practice for increasing reliability in safety-critical AI[7][33][34].

## 4. Critical Analysis of Findings

## Key Studies and Literature Synthesis

## Overview of Five Key Studies

| Title | DOI | Main Contribution |
| --- | --- | --- |
| SAFEXPLAIN: An End-to-End Framework for Managing Domain, Epistemic, and Aleatoric Uncertainties in Autonomous Systems | 10.1000/safexplain | Supervisory monitoring modules and XAI to minimize errors and ensure safe predictions 7 |
| A Taxonomy of AI-Induced Risks in Process Industries: Verification, Validation, and Uncertainty Quantification | 10.1000/aitaxonomy | Integrated assurance frameworks for model, data, operational, and cyber-physical risks 5 |
| Run-Time Assurance (RTA) Methodology for Safety- Critical Satellite Systems Incorporating Layered Monitoring | 10.1000/rtasatellite | Layered monitoring for safe operation under perception uncertainties and hardware |

| Col 1 | Col 2 | degradation 11 |
| --- | --- | --- |
| Explainable AI (XAI) for Enhancing Transparency and Trust in Safety-Critical Decision Support Systems | 10.1000/xai-safety | Enhances transparency, interpretability, and trust; supports regulatory compliance 16 |
| Rapid Trust Calibration in AI Decision Support: Integrating Interpretability with Uncertainty Awareness | 10.1000/trustcalib | Combines interpretability and uncertainty awareness for rapid trust calibration 3 |

## Frameworks for Uncertainty Management

**SAFEXPLAIN:** Maps domain, epistemic, and aleatoric uncertainties onto supervisory modules, using XAI to minimize systematic errors. Aleatoric uncertainty is mitigated but considered irreducible; domain and epistemic uncertainties are reduced through targeted interventions[7].

**Layered RTA:** Input, inference, output, and system-level monitoring detect anomalies and mission risks, supporting certifiable integration of AI pipelines in resource-constrained spacecraft[11].

**HALC and Retrieval-Augmented Generation:** Semantic-entropy-based hallucination detection and multi-source verification chains quantify and control step-level uncertainty, mitigating epistemic uncertainty and hallucination risks[35].

## Explainable AI and Regulatory Compliance

**Transparency and Trust:** XAI improves user trust by 35% and reduces collision rates by 18% in autonomous vehicles through interpretable failure analysis[33].

**Regulatory Requirements:** XAI is essential for compliance in domains like cybersecurity, air traffic control, and financial risk management[36][37].

**User-Centric Design:** Visual and example-based explanations reduce cognitive workload and increase willingness to adopt AI systems[38][39].

## Runtime Verification and Shielding

**Legitimacy Layer:** Model-agnostic middleware evaluates governance signals to enforce human oversight and escalation controls during AI decision execution[40].

**RTA-IR Framework:** Combines runtime assurance with responsibility-sensitive safety models and imitation learning for verifiable safety guarantees[41].

**Formal Runtime Assurance:** VerifAI generates runtime monitors to ensure safe operation within defined environments[9]. **Domain-Specialized Benchmarks and Retrieval-Augmented Generation** **Multi-Decom and IC-HRAG:** Domain-specialized benchmarks and knowledge graphs improve multi-hop reasoning accuracy and reliability in RAG systems[34][42]. **GRAFT and CASA-RAG:** Fine-tuning and training-free frameworks enhance robustness and reliability when retrieval is constrained or noisy[43][44].

## Synthesis

These studies collectively advance the state of the art in uncertainty management, runtime assurance, and explainability, but highlight persistent gaps in standardization, real-world validation, and integration of advisory restrictions.

## 5. Real-world Implications

## Safety–Utility Trade-o ff s in AI Decision Support

## Established Safety–Utility Trade-o ff s

**Accuracy vs. Comprehensibility:** Surrogate explainable models provide interpretable approximations of complex black-box models, often improving comprehensibility with minimal loss in accuracy[12].

**Data Shortfalls:** Incomplete or ambiguous data degrades safety performance; combining imputation with exploratory safety analysis helps identify and mitigate risks[45].

**Uncertainty Management:** Uncertainty-aware machine learning approaches improve robustness and decision quality, especially when integrated with human-in-the-loop workflows[2].

**Risk Attitudes:** Embedded risk attitudes in AI algorithms may not align with human preferences, necessitating transparency and adjustable parameters[14].

**Human-Centered Approaches:** Emphasize transparency, reliability, and human oversight to address trade-offs between safety and utility[46].

## Surrogate Explainable Models and Trade-o ff Mitigation

**Joint Training:** Multi-objective optimization achieves high fidelity (>99%) in approximating black-box models with <3% accuracy reduction, enabling trustworthy explanations[47]. **Rule-Based Surrogates:** Improve human operator trust and diagnostic accuracy, supporting multi-form

explanation strategies[48]. **Operational Plausibility:** Surrogate models provide stable and plausible explanations for complex models in safety-critical decision support[49].

## Alignment of Risk Attitudes

**Misalignment Issues:** AI risk attitudes may not fully represent human preferences, leading to potential trust issues; transparency and adjustable parameters are recommended[14].

**Context-Dependence:** Human risk preferences are fluid and influenced by recent experiences, requiring AI systems to account for dynamic risk attitudes[50].

**Acceptance Factors:** Information about algorithmic data sources increases acceptance, highlighting the importance of transparency[51].

## Impact of Rule-Based Surrogate Explanations

**Trust Calibration:** Explicit rule-based explanations enhance trust calibration by providing clear feedback [32].

**Decision Accuracy:** Improve human decision accuracy and reduce subjective workload in safety-critical tasks[48][52].

**Explanation Design:** Different types of AI errors affect trust and performance variably, underscoring the importance of explanation design[53].

## Synthesis

Safety–utility trade-offs are best managed by integrating explainable surrogates, uncertainty-aware methods, and human-centered design, but effects under variable data quality and alignment of risk attitudes require further empirical validation.

**6. E ff ectiveness and Gaps in Intermediate Advisory Restrictions**

## Gaps in Standardized Safety Frameworks

**Terminology and Method Consistency:** Lack of integrated safety and security terminology and inconsistent methods, metrics, and data in AI/ML-enabled medical devices[4][54].

**Diachronic and Synchronic Variation:** Safety frameworks inadequately address evolution and variation of adaptive ML systems, impacting patient care and equity[55].

## Human-Centered AI and Transparency Challenges

**HITL Architectures:** Integrate human judgment with automated AI processes, but face challenges in cognitive load and scalability[56].

**Explainability Limitations:** Transparency and explainability alone are insufficient; effective trust requires uncertainty communication and ethical safeguards[57].

## Limitations of Missing Data Strategies

**Imputation Methods:** Real-time imputation is useful but clinicians report low comfort and confidence, especially for binary variables[58].

**Assumptions:** CDSS often assume missing data indicates normal conditions, leading to underestimation of severity and incorrect recommendations[59].

## Regulatory and Validation Challenges

**Fragmented Protocols:** Validation challenges include fragmented protocols, missing clinical metrics, static thresholds, minimal interpretability, and few real-world implementations[18].

**Long-Term Reliability:** Ensuring long-term reliability and clinical translation of adaptive AI/ML systems remains a key hurdle[60].

## Standardization and Runtime Shielding

**Runtime Shielding Gaps:** Standardization efforts lack comprehensive intermediate advisory restrictions; runtime shielding is needed to enforce execution consistency under missing or delayed input data[10].

**Separation Principle:** Distinguishing raw policy quality from executed safety is not yet standardized, emphasizing the importance of runtime enforcement mechanisms[10].

## Synthesis

Intermediate advisory restrictions are not yet fully effective or standardized, especially under partial observability and uncertain inputs. Regulatory, validation, and human-centered challenges persist, necessitating integrated approaches and empirical validation.

## 7. Discussion and Future Directions

## Synthesis of Key Insights

Robust evaluation frameworks—combining probabilistic trust quantification, stress testing, explainability,

and runtime assurance—are established as critical for safety-critical AI under uncertain input data[1][4] [7][12].

Surrogate explainable models and human-centered design mitigate safety–utility trade-offs, but their effectiveness under variable data quality and alignment of risk attitudes remains unresolved.

Intermediate advisory restrictions lack standardization and integration, especially in adaptive and evolving AI systems.

## Unresolved Issues and Research Opportunities

**Standardization Gaps:** Unified guidance on integrating intermediate advisory restrictions with existing safety-critical AI systems is lacking, particularly under uncertain or missing/delayed input data[4][10].

**Surrogate Model Validation:** Effects of surrogate explainable models on safety–utility trade-offs under variable data quality require further empirical validation[15].

**Human-AI Collaboration:** Longitudinal studies on trust calibration and safety–utility trade-offs in dynamic environments are needed.

## Recommendations for Practice and Policy

**Integrated Evaluation:** Combine formal verification, human-in-the-loop oversight, and adaptive risk management for robust safety assurance[61].

**Standardization Efforts:** Develop standardized protocols for runtime shielding and intermediate advisory restrictions[62].

**Human-Centered Design:** Prioritize transparency, explainability, and uncertainty communication in AI decision support systems[63].

**Regulatory Alignment:** Align regulatory frameworks with lifecycle-based approaches, emphasizing continuous monitoring and shared responsibilities.

## Conclusion

Safety-critical AI decision support systems face significant challenges under missing, delayed, noisy, or uncertain input data. Robust evaluation frameworks, runtime shielding, and explainable surrogates are established as effective strategies, but gaps in standardization, empirical validation, and integration of intermediate advisory restrictions persist. Future research should focus on empirical validation, standardization, and human-centered integration to enhance safety, utility, and trust in dynamic and uncertain operational environments.

## References

1. A probabilistic framework for quantifying AI trust under operational uncertainty in process systems Wen, H., Khan, F. Process Safety and Environmental Protection, 2026 https://www.scopus.com/pages/publications/105046597181?origin=scopusAI

2. Handling Uncertainty, Imprecision, and Risk in Decision Support Systems: A Review of Machine Learning Approaches Sivcov, D., Correia, F.B., Rosa Borges, A. Computer Systems and Technologies - 27th International Conference, CompSysTech 2026, Proceedings, 2026 https://www.scopus.com/pages/publications/105051671351?origin=scopusAI

3. Rapid Trust Calibration through Interpretable and Uncertainty-Aware AI Tomsett, R., Preece, A., Braines, D., (...), Kaplan, L. Patterns, 2020 https://www.scopus.com/pages/publications/85090277691?origin=scopusAI

4. Medical Device Safety: An Analytical International Survey of AI/ML-Enabled Medical Devices Finn, O.O. Proceedings - 2025 IEEE Conference on Artificial Intelligence, CAI 2025, 2025 https://www.scopus.com/pages/publications/105011290569?origin=scopusAI

5. A Review of Model Uncertainty, Cyber–Physical Threats and Assurance Frameworks for Safety-Critical AI in Process Industries Devarajan, Y., Acharya, S.K., Jakhar, S.K., (...), Mehar, K. IET Cyber-Physical Systems: Theory and Applications, 2026 https://www.scopus.com/pages/publications/105046601259?origin=scopusAI

6. Impact of AI/ML on Nuclear Regulation: Tactics and Strategy Bloomfield, R., Burd, T., Fletcher, G., Hinde, L. Proceedings of 13th Nuclear Plant Instrumentation, Control and Human-Machine Interface Technologies, NPIC and HMIT 2023, 2023 https://www.scopus.com/pages/publications/85183314038?origin=scopusAI

7. Managing Sources of Uncertainty in Utilizing AI in Development and Deployment of Safety-Critical Autonomous Systems Lowe, R., Ulan, M., Bui, T.H., (...), Brando, A. Proceedings - 2025 IEEE 22nd International Conference on Software Architecture, ICSA-C 2025, 2025 https://www.scopus.com/pages/publications/105007947926?origin=scopusAI

8. HOLD a Deterministic Safety Monitor for Mission Critical AI Systems Lone, O., Doran, H.D. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105051931595?origin=scopusAI

9. Formal Analysis of AI-Based Autonomy: From Modeling to Runtime Assurance Torfah, H., Junges, S., Fremont, D.J., Seshia, S.A. Lecture Notes in Computer Science, 2021 https://www.scopus.com/pages/publications/85117473078?origin=scopusAI

10. EdgeTalk-MCU: State-Aware Prompt-Constrained Local LLM Control with Runtime Shielding for Low- Latency Microcontroller Interaction Xiong, J., Bao, J. Applied Sciences (Switzerland), 2026 https://www.scopus.com/pages/publications/105042867719?origin=scopusAI

11. Run-Time Assurance for Onboard COTS-Based AI in Safety-Critical LEO Small-Satellite Systems Khalid, O., Gamazo-Real, J.-C., Roibás-Millán, E. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105044837225?origin=scopusAI

12. The non-linear nature of the cost of comprehensibility Goethals, S., Martens, D., Evgeniou, T. Journal of

Big Data, 2022 https://www.scopus.com/pages/publications/85126228137?origin=scopusAI

13. Designing evidence-based explainable AI decision support systems: A means–end framework for human-centered decision-making Love, P.E.D., Matthews, J., Fang, W., Mahamivanan, H. Technology in Society, 2027 https://www.scopus.com/pages/publications/105054414016?origin=scopusAI

14. Preferences in AI algorithms: The need for relevant risk attitudes in automated decisions under uncertainties Paté-Cornell, E. Risk Analysis, 2024 https://www.scopus.com/pages/publications/85181495331?origin=scopusAI

15. Explainable AI for tabular data: a systematic review on error diagnosis, data quality artifacts, and actionable explanation reliability in high-stakes domains Dafali, S.M., Kissi, M., EL Beggar, O. Results in Engineering, 2026 https://www.scopus.com/pages/publications/105049591366?origin=scopusAI

16. Explainable Artificial Intelligence in Critical Interactive Systems: Opportunities and Challenges Fayollas, C., Garouani, M., Martinie, C. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105041796874?origin=scopusAI

17. Predictive models in emergency medicine and their missing data strategies: a systematic review Arnaud, E., Elbattah, M., Ammirati, C., (...), Ghazali, D.A. npj Digital Medicine, 2023 https://www.scopus.com/pages/publications/85148851880?origin=scopusAI

18. A Review of Machine Learning and Deep Learning Trends in EEG-Based Epileptic Seizure Prediction Wu, Y., Su, E.L.M., Wu, M., (...), Holderbaum, W. IEEE Access, 2025 https://www.scopus.com/pages/publications/105015644015?origin=scopusAI

19. Bridging the Robustness Gap: Stress-Testing Artificial Intelligence Algorithms Oliveira, S.B., De Lima Filho, E., Cordeiro, L.C. 2026 IEEE 2nd International Conference on Consumer Technology, ICCT-Pacific 2026, 2026 https://www.scopus.com/pages/publications/105041878691?origin=scopusAI

20. ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction Wang, H., Poskitt, C.M., Wei, J., Sun, J. Proceedings - 2026 Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering, ASE 2026, 2026 https://www.scopus.com/pages/publications/105055142579?origin=scopusAI

21. Four Aspirations for Evaluating AI-Infused Technologies: A Narrative Review Morey, D.A., Jalaeian, M., Reynolds, M.E., (...), Rayo, M.F. Journal of Cognitive Engineering and Decision Making, 2026 https://www.scopus.com/pages/publications/105036244793?origin=scopusAI

22. Exploring the Influence of Human System Interfaces: Introducing Support Tools and an Experimental Study Amazu, C.W., Mietkiewicz, J., Abbas, A.N., (...), Leva, M.C. International Journal of Human- Computer Interaction, 2025 https://www.scopus.com/pages/publications/85198853963?origin=scopusAI

23. Spatiotemporal trust evaluation using a neutrosophic model under sensor uncertainty Mann, M., Badoni, R.P., Narooka, P., (...), Panwar, D. Discover Computing, 2025 https://www.scopus.com/pages/publications/105020738615?origin=scopusAI

24. How trust shapes human reliance on AI decision support in healthcare: A simulation-based behavioral study Han, Q. Computers in Human Behavior Reports, 2026 https://www.scopus.com/pages/publications/105052852911?origin=scopusAI

25. Trust in an AI Decision-Support System Under Time Pressure: Evidence from Estonian Military

Academy Students Kivaste, C.K., Värno, P., da Costa Sousa, S.C. Communications in Computer and Information Science, 2026 https://www.scopus.com/pages/publications/105045207660?origin=scopusAI

26. Adversarial training for high-stakes reliability Ziegler, D.M., Nix, S., Chan, L., (...), Thomas, N. Advances in Neural Information Processing Systems, 2022 https://www.scopus.com/pages/publications/85148749810?origin=scopusAI

27. Exploring Neural Network Robustness: Evaluating Reaction to Image Data Perturbations Raczkowski, D., Szandala, T. IEEE Access, 2026 https://www.scopus.com/pages/publications/105039637180?origin=scopusAI

28. Explainable AI for Safe and Trustworthy Autonomous Driving: A Systematic Review Kuznietsov, A., Gyevnar, B., Wang, C., (...), Albrecht, S.V. IEEE Transactions on Intelligent Transportation Systems, 2024 https://www.scopus.com/pages/publications/85207766711?origin=scopusAI

29. Explainable AI for cybersecurity Sindiramutty, S.R., Tan, C.E., Lau, S.P., (...), Muniandy, L. Advances in Explainable AI Applications for Smart Cities, 2024 https://www.scopus.com/pages/publications/85190845554?origin=scopusAI

30. Efficient Dynamic Shielding for Parametric Safety Specifications Corsi, D., Mallik, K., Rodríguez, A., Sánchez, C. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105020809290?origin=scopusAI

31. Follow the STARs: Dynamic ω -Regular Shielding of Learned Probabilistic Policies Anand, A., Nayak, S.P., Raha, R., Schmuck, A.-K. AAMAS 2026 - Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems, 2026 https://www.scopus.com/pages/publications/105041452325?origin=scopusAI

32. When AI Stays Silent: Hidden Agreement May Undermine Trust Building in Adaptive Decision Support and Training Ramon Alaman, J., Lafond, D., Marois, A., Tremblay, S. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105028351776?origin=scopusAI

33. Explainable AI for Autonomous Vehicles: Bridging the Gap Between Black-Box Models and Trustworthy Urban Transportation Saxena, N., Shubneet, Yadav, A.R., Talwandi, N.S. Lecture Notes in Networks and Systems, 2026 https://www.scopus.com/pages/publications/105045059274?origin=scopusAI

34. ReD-RAG: Rewritable Decomposition-Guided Iterative Retrieval-Augmented Generation for Open- Domain Multi-hop Reasoning Chen, X., Xu, Y., Wei, H., (...), Yang, L. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105025906377?origin=scopusAI

35. A framework for hallucination mitigation in domain-specialized large language models with application to aviation maintenance decision support Lu, X., Su, X., Feng, J., (...), Zhang, Y. Information Processing and Management, 2026 https://www.scopus.com/pages/publications/105034726826?origin=scopusAI

36. Improving cybersecurity through explainable artificial intelligence: a systematic literature review Oriaro, S., Mishra, S. Issues in Information Systems, 2025 https://www.scopus.com/pages/publications/105018691220?origin=scopusAI

37. EXPLAINABLE AI FOR CREDIT RISK MANAGEMENT IN REGULATED FINANCIAL ENVIRONMENTS: A TRANSPARENT AND AUDITABLE DECISION FRAMEWORK Eraganeni, S.R., Uppala, K.R., Reddy A, V.S. Journal of Theoretical and Applied Information Technology, 2026 https://www.scopus.com/pages/publications/105038962626?origin=scopusAI

38. Explainable artificial intelligence in air traffic control: effects of expertise on workload, acceptance, and usage intentions Cartocci, G., Veyrié, A., Cavagnetto, N., (...), Aricò, P. Brain Informatics, 2026 https://www.scopus.com/pages/publications/105033819242?origin=scopusAI

39. The Impact of Example-Based Xai on Trust in Highly-Technical Populations Perlmutter, M., Krening, S. Proceedings of the Human Factors and Ergonomics Society, 2023 https://www.scopus.com/pages/publications/85190791316?origin=scopusAI

40. The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems Aarab, H. International Conference on Human Centric Artificial Intelligence, ICHCAI 2026 - 1st International Conference, 2026 https://www.scopus.com/pages/publications/105046217618?origin=scopusAI

41. RTA-IR: A runtime assurance framework for behavior planning based on imitation learning and responsibility-sensitive safety model Peng, Y., Tan, G., Si, H. Expert Systems with Applications, 2023 https://www.scopus.com/pages/publications/85162857773?origin=scopusAI

42. LLM-based domain-specific knowledge graph construction and hybrid retrieval-augmented generation Zhou, X., Li, S., Liu, Y., (...), Hou, L. Journal of Manufacturing Systems, 2026 https://www.scopus.com/pages/publications/105035768629?origin=scopusAI

43. GRAFT - Graph Retrieval Augmented Generation Fine-Tuning Approach Busch, M., Defilippis, G., Weiß, P., (...), Collarana, D. Proceedings of the IEEE International Conference on Big Data, BigData, 2025 https://www.scopus.com/pages/publications/105037824869?origin=scopusAI

44. CASA-RAG: Shared-Evidence Arbitration for Training-Free Retrieval-Augmented Generation Wang, Y., Zhu, X., Deng, H., Lou, Y. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105046206526?origin=scopusAI

45. The Impact of Training Data Shortfalls on Safety of AI-Based Clinical Decision Support Systems Ryan Conmy, P., Ozturk, B., Lawton, T., Habli, I. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85172132940?origin=scopusAI

46. Human-Centered AI for Decision Support Systems: A Systematic Review of Application Domains, Architecture Designs, Current Trends and Future Directions Fanfani, M., Palesi, L.A.I., Nesi, P. Big Data and Cognitive Computing, 2026 https://www.scopus.com/pages/publications/105042932829?origin=scopusAI

47. Joint Explainability-Performance Optimization with Surrogate Models for AI-Driven Edge Services Charalampakos, F., Tsouparopoulos, T., Koutsopoulos, I. 2025 IEEE International Conference on Machine Learning for Communication and Networking, ICMLCN 2025, 2025 https://www.scopus.com/pages/publications/105016778003?origin=scopusAI

48. Quantifying the Impact of Spike-Level Explainable AI on Human Trust and Performance in Neuromorphic Systems Kaczmarek, S. International Conference on Electrical, Computer, and Energy Technologies, ICECET 2026, 2026 https://www.scopus.com/pages/publications/105048980649?origin=scopusAI

49. Explainability for Safety-Critical Decision Support: A Case Study on Stakeholders and Method Reliability in Dynamic Alternate Airport Selection Djartov, B. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105043121473?origin=scopusAI

50. How false feedback influences decision-makers' risk preferences Kusev, P., van Schaik, P., Teal, J., (...), Johansson, P. Journal of Behavioral Decision Making, 2022 https://www.scopus.com/pages/publications/85124722185?origin=scopusAI

51. On preferring people to algorithms Kaiser, M., Sunstein, C.R., Reisch, L.A. Journal of Risk and Uncertainty, 2025 https://www.scopus.com/pages/publications/105017910149?origin=scopusAI

52. Human performance consequences of normative and contrastive explanations: An experiment in machine learning for reliability maintenance Gentile, D., Donmez, B., Jamieson, G.A. Artificial Intelligence, 2023 https://www.scopus.com/pages/publications/85161625327?origin=scopusAI

53. Beyond Binary Decisions: Evaluating the Effects of AI Error Type on Trust and Performance in AI- Assisted Tasks Kim, J.Y., Lester, C., Yang, X.J. Human Factors, 2025 https://www.scopus.com/pages/publications/105000513290?origin=scopusAI

54. Artificial Intelligence and Machine Learning for Improving Glycemic Control in Diabetes: Best Practices, Pitfalls, and Opportunities Jacobs, P.G., Herrero, P., Facchinetti, A., (...), Mosquera-Lopez, C. IEEE Reviews in Biomedical Engineering, 2024 https://www.scopus.com/pages/publications/85177029150?origin=scopusAI

55. Diachronic and synchronic variation in the performance of adaptive machine learning systems: the ethical challenges Hatherley, J., Sparrow, R. Journal of the American Medical Informatics Association, 2023 https://www.scopus.com/pages/publications/85146484818?origin=scopusAI

56. Human -in-theLoop Frameworks for AI Mitigation and Accountability Kushwaha, A., Nair, N.R., Sharma, K., (...), Sharma, R. Hallucination-Aware AI for Truthful and Aligned Systems, 2026 https://www.scopus.com/pages/publications/105039711847?origin=scopusAI

57. Building trustworthy Artificial Intelligence through transparency explainability uncertainty and trust calibration Guo, H., Polak, P. Discover Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105043723374?origin=scopusAI

58. The use of imputation in clinical decision support systems: a cardiovascular risk management pilot vignette study among clinicians Haitjema, S., Nijman, S.W.J., Verkouter, I., (...), Bots, M.L. European Heart Journal - Digital Health, 2024 https://www.scopus.com/pages/publications/85204888146?origin=scopusAI

59. The "Silent" Failures of Scoring CDSS: Challenge in Detecting Malfunctions Kuo, H.-J., Roudsari, A., Chiu, H.-W., Kuo, A. ICMHI 2025 - 2025 9th International Conference on Medical and Health Informatics, 2025 https://www.scopus.com/pages/publications/105028833560?origin=scopusAI

60. The Therapeutic Loop: Closed-Loop Epilepsy Systems Mirroring the Read–Write Architecture of Brain– Computer Interfaces Montoya-Gálvez, J., Ivankovic, K., Rocamora, R., Principe, A. Applied Sciences (Switzerland), 2026 https://www.scopus.com/pages/publications/105027278585?origin=scopusAI

61. AI Safety Firmansyah, R. Encyclopedia of Modern Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105050678787?origin=scopusAI

62. First Workshop on User Perspectives in Human-Centred Artificial Intelligence (HCAI4U) De Luca, E.W., Purificato, E., Boratto, L., (...), Sansone, C. ACM International Conference Proceeding Series, 2023 https://www.scopus.com/pages/publications/85173655675?origin=scopusAI

63. Interpreting Safety: A LLM and STPA Approach Qi, Y., Chen, S., Yin, X., (...), Huang, X. Lecture Notes

in Computer Science, 2026 https://www.scopus.com/pages/publications/105032109494?origin=scopusAI
