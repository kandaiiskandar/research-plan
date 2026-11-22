---
source_pdf: "Search 2 Multi-Level Risk States in AI, Autonomous, and Decision-Support Systems- Frameworks, Implementation, and Evaluation.pdf"
source_sha256: "c81e720885a91d5924fd6a429363e339da9f6b7656ae2b772a25b746d78e6f65"
source_pages: 9
scopus_ai_generated: "Wed Sep 23 2026"
query: "AI risk and safety state studies"
report_title: "Multi-Level Risk States in AI, Autonomous, and Decision-Support Systems: Frameworks, Implementation, and Evaluation Quick Reference"
converted_tables: 4
converter: "scopus2md.py (pdfplumber)"
---
# AI risk and safety state studies

## Key Findings Table

| Study/Framework/Domain | Risk States Defined | Trigger/Indicator | Permitted Actions per State | Runtime Restriction | Activation Frequency Measured | Binary Baseline Exists | Intermediate Level Isolated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hybrid RL-Fuzzy-Neural Models 1 2 | Low, Intermediate, High | Model uncertainty, env. feedback | Full, restricted, abstain/fallback | Yes | Yes (statistical metrics) | Sometimes | Sometimes |
| Supervis# Multi-Level Risk States in AI, Autonomous, and Decision-Support Systems: Frameworks, Implementation, and Evaluation |  |  |  |  |  |  |  |

## Quick Reference

## Key Findings Table

| Study/Framework/Domain | Risk States Defined | Trigger/Indicator | Permitted Actions per State | Runtime Restriction | Activation Frequency Measured | Binary Baseline Exists | Intermediate Level Isolated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hybrid RL-Fuzzy-Neural Models 1 2 | Low, Intermediate, High | Model uncertainty, env. feedback | Full, restricted, abstain/fallback | Yes | Yes (statistical metrics) | Sometimes | Sometimes |
| Supervisory Risk Control (SRC) 3 | Low, Intermediate, High | Online risk assessment | Full, restricted, human override | Yes | Yes (operator workload, events) | Yes | Yes |
| EU AI Act 4 | Minimal, Limited, High, Unacceptable | System type, use case, context | Full, restricted, prohibited | Yes | Not always | Yes | Not always |
| Causal-Counterfactual Decision Support 5 6 | Low, Intermediate, High | Causal inference, scenario analysis | Full, restricted, abstain | Yes | Sometimes | Sometimes | Sometimes |
| Clinical Decision Support (CDSS) 7 8 | Low, Intermediate, High | Patient data, clinical guidelines | Full, restricted, human review | Yes | Yes (gray zone area, events) | Yes | Sometimes |
| Multi-Agent Adaptive Intervention 9 10 | Low, Intermediate, High | Performance metrics, risk thresholds | Full, restricted, fallback | Yes | Sometimes | Sometimes | Sometimes |

| Study/Framework/Domain | Risk States Defined | Trigger/Indicator | Permitted Actions per State | Runtime Restriction | Activation Frequency Measured | Binary Baseline Exists | Intermediate Level Isolated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dynamic Risk Management (Process/Transport) 11 | Low, Intermediate, High | Environmental, operational data | Full, restricted, fallback | Yes | Yes (risk maps, clustering) | Sometimes | Sometimes |

## 12

## Direct Answer

Studies implementing multi-level risk/safety states in AI, autonomous, and decision-support systems define low risk as permitting full actions or advice, intermediate risk as allowing a restricted subset, and high risk as leading to abstention, fallback, or no action. These systems use composite metrics (e.g., model uncertainty, operational context) and triggers such as out-of-distribution inputs or dynamic environmental indicators. Runtime restrictions are enforced via supervisory risk control, hybrid models, or governance frameworks. Activation frequency is measured using statistical methods (e.g., Lorenz curves, clustering, regression), and some studies compare to binary baselines or isolate the intermediate risk level's marginal contribution through scenario-based testing and multi-criteria analysis. However, standardized benchmarking and operational translation of intermediate risk contributions remain research gaps[1][4][13][14] [15][16][17].

## Study Scope

**Time Period:** Primarily 2019–2024, with emphasis on post-2020 implementations and regulatory frameworks. **Disciplines:** Healthcare (clinical decision support), transportation (autonomous vehicles, UAVs), process industries, cybersecurity, and AI governance. **Methods:** Hybrid AI (RL, fuzzy, neural), multi-agent systems, causal inference, scenario-based testing, explainable AI, statistical and machine learning metrics, regulatory analysis.

## Assumptions & Limitations

Many studies focus on frameworks or prototypes rather than large-scale, real-world deployments. Isolation of intermediate risk contributions is often indirect, relying on statistical or scenario-based methods rather than controlled experiments. Activation frequency and runtime restriction reporting is inconsistent across domains. Binary baselines are sometimes implicit, and not all studies provide direct comparative analysis. Regulatory frameworks (e.g., EU AI Act) provide structure but not always operational detail.

## Suggested Further Research

Develop standardized benchmarks and validation protocols for isolating intermediate risk state contributions. Advance scenario-based and digital twin testing to simulate nuanced risk transitions. Integrate continuous evaluation frameworks and human-in-the-loop oversight for real-world safety-critical applications. Expand operationalization of multi-level risk models into enforceable runtime controls and governance.

## 1. Introduction

Multi-level risk state management is an emerging paradigm in AI, autonomous, and decision-support systems, moving beyond binary safe/unsafe models to enable differentiated actions and oversight. By stratifying risk into low, intermediate, and high states, these systems can optimize performance, safety, and trust, especially in complex, safety-critical domains. This review synthesizes theoretical frameworks, practical implementations, and evaluation methodologies for multi-level risk state systems, highlighting both advances and persistent challenges[4][13][18].

## Scope and Significance

The focus is on systems that: Allow **full actions/advice** at low risk, Restrict to a **subset of actions/advice** at intermediate risk, Enforce **abstention, fallback, or no action** at high risk. Understanding and operationalizing these distinctions is critical for: Safety and reliability in autonomous and decision-support systems, Building user and stakeholder trust, Meeting regulatory and ethical requirements[4][18].

**2. Survey of Multi-Level Risk State Frameworks and Implementations**

## 2.1 Frameworks and Models for Multi-Level Risk States

## Hybrid AI and Tiered Governance

**Hybrid AI Models:** Combine reinforcement learning, fuzzy logic, and neural networks to handle uncertainty and adaptively manage risk states. Fuzzy logic enables nuanced transitions between risk levels, neural networks provide pattern recognition, and RL supports adaptive decision-making[1][2].

**Tiered Governance:** Regulatory frameworks (e.g., EU AI Act) and hospital AI governance models stratify risk into multiple levels, assigning differentiated compliance and oversight obligations[4][8].

**Causal-Counterfactual Decision Support (CCDS):** Integrates prediction and causal inference to prioritize interventions by feasibility and effectiveness, operationalizing multi-level risk advice[5][6].

## Supervisory Risk Control (SRC)

Embeds online risk assessment into control algorithms, enabling systems to perceive, comprehend, and project future risk scenarios, and to act accordingly (full, restricted, or fallback)[3].

## Taxonomies and Standards

**AI Hazard Analysis Taxonomies:** Extend traditional models with layers for AI oversight, design, maintenance, and testing, supporting nuanced risk state differentiation[19].

## 2.2 Practical Implementations Across Domains

## Healthcare

**Clinical Decision Support Systems (CDSS):** Use patient data and clinical guidelines to stratify risk and recommend actions, with intermediate risk often triggering human review or restricted advice[7][8].

**Drug Safety and Oncology:** AI models stratify patient risk and guide therapy, but real-world deployment and external validation remain limited[20][21].

## Transportation and Process Industries

**Autonomous Vehicles:** Risk states are defined by environmental and operational data (e.g., vehicle spacing, driver distraction), with runtime restrictions and fallback mechanisms[11].

**Process Industries:** Integrated assurance frameworks address model, data, and operational risks, with multi-level risk management and differentiated safety actions[18].

## Cybersecurity and Data Governance

**Dynamic Risk-Adaptive Data Governance (DRADG):** Combines static policy with dynamic risk indicators to adapt governance controls at runtime[22].

## 2.3 Hybrid and Multi-Agent Approaches

**Multi-Agent Systems:** Enable adaptive intervention policies, with agents dynamically evaluating risk and tailoring actions (full, restricted, fallback)[9][10].

**Federated and Explainable AI:** Hybrid frameworks balance privacy, interpretability, and adaptability, crucial for managing risk in distributed environments[23].

## Synthesis:

Across domains, multi-level risk state frameworks are converging on hybrid, adaptive, and explainable architectures, often integrating human oversight and regulatory compliance as core components[1][8][17].

## 3. Characterization and Activation of Risk States

## 3.1 Definitions and Differentiation of Risk States

**Low Risk:** Full autonomy or advice, minimal oversight. **Intermediate Risk:** Restricted actions, human-in-the-loop or additional checks. **High Risk:** No action, abstention, or fallback to human control. Definitions are context-specific, often based on: Severity and likelihood of adverse outcomes, Operational context (e.g., clinical, industrial, environmental), AI-induced risk categories (model uncertainty, data risk, operational risk)[14][24][25].

## 3.2 Triggers and Indicators for Risk State Activation

**Model Uncertainty:** Out-of-distribution inputs, prediction confidence, or data quality issues trigger higher risk states[18][26]. **Operational Hazards:** Environmental changes, system faults, or human-machine interaction challenges[26]. **Composite Risk Assessment:** Weighted indicators (e.g., separation, congestion, speed) and hard safety overrides for critical events [26].

## 3.3 Continuous Monitoring and Runtime Adaptation

**Dynamic Risk Assessment:** Graph neural networks, explainable AI, and bio-inspired frameworks enable real-time risk monitoring and adaptation[12][27][28]. **Runtime Assurance:** Formal monitors (e.g., VerifAI) detect deviations and trigger corrective actions[29]. **Human-in-the-Loop:** Governance frameworks ensure that human oversight is activated at appropriate risk thresholds[3][8].

## Synthesis:

Risk state activation is increasingly data-driven, leveraging continuous monitoring and explainable indicators to support timely and context-appropriate interventions[12][26]. **4. Permitted Actions, Runtime Restrictions, and Activation Frequency**

## 4.1 Permitted Actions and Runtime Restrictions

**Low Risk:** Full set of actions or advice, autonomous operation. **Intermediate Risk:** Restricted subset, often requiring human review or additional validation.

**High Risk:** No action, abstention, or fallback to human or safe state.

## Enforcement Mechanisms:

**Governance Frameworks:** Legitimacy Layer, DRADG, and A4-Gov architectures translate risk assessments into runtime controls (e.g., execute, escalate, halt)[30][31]. **Dynamic Risk Management:** Adaptive control, bounded intervention, and layered monitoring (input, inference, output)[32][33].

## 4.2 Measurement of Activation Frequency

**Statistical Metrics:** Lorenz curves, clustering, Bayesian regression, and risk maps quantify how often intermediate and high risk states are activated[34][35][36]. **Performance Metrics:** Classification accuracy, recall, precision, AUC, and gray zone area in clinical AI[34][36]. **Scenario-Based Testing:** Scenario complexity and risk-driven prioritization in autonomous vehicles[37][38].

## 4.3 Runtime Governance and Control Actions

**Consent and Oversight:** Dynamic consent frameworks and human-in-the-loop systems enforce runtime restrictions and auditability [30][39].

**Multi-Agent Risk Management:** Specialized agents for risk evaluation, threat generation, and control allocation enable continuous mitigation[40][41].

## Synthesis:

Permitted actions and runtime restrictions are increasingly operationalized through dynamic, adaptive, and auditable governance frameworks, with activation frequency measured using advanced statistical and scenario-based methods[30][34]. **5. Evaluation of Baselines and Isolation of Intermediate Risk Contributions**

## 5.1 Binary Baseline Comparisons and Multi-State Analysis

| Beyond Binary: Most studies move beyond simple safe/unsafe baselines, using multi-criteria decision analysis, scenario-based testing, and integrated statistical metrics 17 42 43. | Col 2 |
| --- | --- |
| Taxonomies and Standards: AI hazard analysis frameworks (e.g., TAIHA) and ISO standards support layered risk assessment 19. | 44 |

## 5.2 Isolation of Intermediate Risk State Effects

**Statistical Isolation:** Lorenz curves, Gini coefficients, and reclassification metrics help isolate the impact of intermediate risk states [16][45]. **Scenario-Based Testing:** Scenario complexity indexing, adversarial testing, and digital twins simulate transitions and edge cases to evaluate intermediate risk contributions[37][46]. **Multi-State Modeling:** Markov models, Petri nets, and Monte Carlo simulations capture transitions between multiple risk states[47].

## 5.3 Challenges in Benchmarking and Validation

**Operational Gaps:** Inconsistent reporting, lack of standardized benchmarks, and limited real-world validation hinder robust isolation of intermediate risk effects[48][49][50]. **Complexity:** AI systems' opacity, data quality issues, and context-dependence complicate benchmarking[51][52].

## Synthesis:

While methods for isolating intermediate risk contributions are advancing, especially through integrated metrics and scenario-based testing, significant challenges remain in benchmarking, validation, and operational translation[16][37][48].

## 6. Discussion and Future Directions

## 6.1 Synthesis of Patterns and Methodologies

**Hybrid and Adaptive Models:** Integration of RL, fuzzy logic, and neural networks is common for dynamic risk management[1][17]. **Human-in-the-Loop Oversight:** Tiered governance and supervisory risk control frameworks ensure accountability and safety[8][13]. **Scenario-Based and Statistical Evaluation:** Scenario complexity, Lorenz curves, and multi-state modeling are key for nuanced risk assessment[17][34].

## 6.2 Research Gaps and Open Challenges

**Benchmarking Intermediate Risk:** Lack of standardized protocols for isolating and quantifying intermediate risk contributions[48] [51]. **Operationalization:** Translating nuanced risk models into enforceable runtime controls remains a challenge[53]. **Real-World Validation:** Limited deployment and external validation in safety-critical domains[50].

## 6.3 Recommendations for Future Research

**Standardized Benchmarks:** Develop and adopt protocols for evaluating intermediate risk state contributions across domains[54]. **Digital Twin and Simulation:** Use digital twins to simulate and analyze risk state transitions and interventions[6]. **Continuous Evaluation:** Integrate real-time monitoring, explainable AI, and human oversight into operational frameworks[55]. **Human-AI Collaboration:** Advance frameworks for shared accountability and adaptive oversight in multi-level risk systems[8][54].

## Conclusion

Multi-level risk state management in AI, autonomous, and decision-support systems is rapidly evolving, with hybrid models, adaptive governance, and scenario-based evaluation at the forefront. While significant progress has been made in defining, operationalizing, and measuring differentiated risk states, persistent gaps in benchmarking, validation, and operational translation—especially for intermediate risk—highlight the need for continued research and standardization. Bridging these gaps will be essential for safe, trustworthy, and effective deployment of AI in safety-critical domains[4][13][17][48].

## References

1. Modified reinforcement learning-hierarchical Neuro-Fuzzy politree model for control of autonomous agents Figueiredo, K., dos Santos, M.L.R., Vellasco, M.M.B.R., Pacheco, M.A.C. International Journal of Simulation: Systems, Science and Technology, 2005 https://www.scopus.com/pages/publications/77956946324?origin=scopusAI

2. Hybrid Fuzzy Neural Systems for Real Time Decision Making in Autonomous Vehicles Indhumathi, R., Jeyalakshmi, M.S., Hemalatha, N., (...), Yadav, K. Journal of Machine and Computing, 2025 https://www.scopus.com/pages/publications/105016722043?origin=scopusAI

3. Towards Risk-based Rationality in Autonomous Systems and Operations Utne, I.B., Johansen, T.A., Sørensen, A.J. Proceedings - Annual Reliability and Maintainability Symposium, 2025 https://www.scopus.com/pages/publications/105002271566?origin=scopusAI

4. Risk, Reasonableness and Residual Harm under the EU AI Act: A Conceptual Framework for Proportional Ex-Ante Controls Teichmann, F. European Journal of Risk Regulation, 2026 https://www.scopus.com/pages/publications/105028035734?origin=scopusAI

5. Causal-Counterfactual Explainable AI for Actionable Decision Support Bedmutha, K.S., Jagdale, R.S. Proceedings of 4th International Conference on Computing, Communication, Security and Intelligent Systems, IC3SIS 2026, 2026 https://www.scopus.com/pages/publications/105046146951?origin=scopusAI

6. From prediction to intervention: causal digital twins for personalized clinical decision support Vallée, A. Journal of Translational Medicine, 2026 https://www.scopus.com/pages/publications/105034773676?origin=scopusAI

7. Assuring the safety of AI-based clinical decision support systems: A case study of the AI Clinician for sepsis treatment Festor, P., Jia, Y., Gordon, A.C., (...), Komorowski, M. BMJ Health and Care Informatics, 2022 https://www.scopus.com/pages/publications/85134556000?origin=scopusAI

8. Risk-Tiered Governance for Hospital Artificial Intelligence: A Framework Synthesis and Implementation Pathway Zhu, M., Luo, B., Wu, X., (...), Li, Y. Applied Clinical Informatics, 2026 https://www.scopus.com/pages/publications/105046176748?origin=scopusAI

9. SAFE AI Agentic System Babaei, G., Giudici, P., Piergallini, A., Zieni, R. Communications in Computer and Information Science, 2026 https://www.scopus.com/pages/publications/105029083649?origin=scopusAI

10. Agentic AI: A Survey of Autonomous Agents, Architectures, and Emerging Applications Deshmukh, S., Kuri, M., Vanarote, V., (...), Yadav, S. 2025 IEEE 5th International Conference on ICT in Business Industry and Government, ICTBIG 2025, 2025 https://www.scopus.com/pages/publications/105032904698?origin=scopusAI

11. A Multi-Scenario Identification Strategy for High-Risk Vehicles Based on Vehicle Networking Data Yanru, L., Jingshuo, Z., Yicong, Z., (...), Yu, L. IEEE Transactions on Intelligent Transportation Systems, 2025 https://www.scopus.com/pages/publications/105013262147?origin=scopusAI

12. Graph Neural Networks and Fault Tree Analysis for Runtime Dynamic Risk Assessment of Autonomous Systems Grimstad, J., Morozov, A. Proceedings - Annual Reliability and Maintainability Symposium, 2025 https://www.scopus.com/pages/publications/105002274315?origin=scopusAI

13. User-model interaction in decision support systems for risk management von Winterfeldt, D. Annals of Operations Research, 1988 https://www.scopus.com/pages/publications/34250092841?origin=scopusAI

14. Autonomous Artificial Intelligence Safety and Trust Abramoff, M.D. Artificial Intelligence in Ophthalmology, 2025 https://www.scopus.com/pages/publications/105023357275?origin=scopusAI

15. From Architecture to Compliance: A Model-Driven Assessment of AI Systems Ekeh, I.F., Matulevičius, R., Affia-Jomants, A.-A., Karagjaur, M. Lecture Notes in Business Information Processing, 2026 https://www.scopus.com/pages/publications/105041852166?origin=scopusAI

16. A statistical package for safe artificial intelligence Babaei, G., Giudici, P. Statistical Methods and Applications, 2025 https://www.scopus.com/pages/publications/105007246865?origin=scopusAI

17. Structuring Research Related to Dynamic Risk Management for Autonomous Systems Adler, R., Reich, J., Hawkins, R. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85172415041?origin=scopusAI

18. A Review of Model Uncertainty, Cyber–Physical Threats and Assurance Frameworks for Safety-Critical AI in Process Industries Devarajan, Y., Acharya, S.K., Jakhar, S.K., (...), Mehar, K. IET Cyber-Physical Systems: Theory and Applications, 2026 https://www.scopus.com/pages/publications/105046601259?origin=scopusAI

19. A Taxonomy for AI Hazard Analysis Cummings, M.L. Journal of Cognitive Engineering and Decision Making, 2024 https://www.scopus.com/pages/publications/85181908086?origin=scopusAI

20. Artificial Intelligence for Drug Safety Across the Lifecycle and Decision Type: A Scoping Review Kim, T.W., Park, S., Kim, M. Pharmaceuticals, 2026 https://www.scopus.com/pages/publications/105031112365?origin=scopusAI

21. Using Artificial Intelligence to Develop Clinical Decision Support Systems—The Evolving Road of Personalized Oncologic Therapy Chitoran, E., Rotaru, V., Gelal, A., (...), Simion, L. Diagnostics, 2025 https://www.scopus.com/pages/publications/105017475750?origin=scopusAI

22. DRADG: A Dynamic Risk-Adaptive Data Governance Framework for Modern Digital Ecosystems Gharib, J., Gahi, Y. Information (Switzerland), 2026 https://www.scopus.com/pages/publications/105028654837?origin=scopusAI

23. Federated Learning Explainable AI and Low Resource Models for Trustworthy Systems Ghorai, R., Pal, U., Gupta, S., (...), Patra, S.S. Proceedings of International Conference on Sustainable Communication Networks and Application, ICSCN 2025, 2025 https://www.scopus.com/pages/publications/105032742785?origin=scopusAI

24. Risk, regulation, and governance: evaluating artificial intelligence across diverse application scenarios Szadeczky, T., Bederna, Z. Security Journal, 2025 https://www.scopus.com/pages/publications/105007148824?origin=scopusAI

25. Fuzzifying the Operational Design Domain: A Scalable Situation Hyperspace Generation Proma, N.M., Firoz, H.B., Paterson, C., (...), Alexander, R. 2026 IEEE International Conference on Fuzzy Systems, FUZZ-IEEE 2026 - Conference Proceedings: Part of the 2026 IEEE World Congress on Computational Intelligence, IEEE WCCI 2026, 2026 https://www.scopus.com/pages/publications/105047242560?origin=scopusAI

26. Adaptive Human Oversight for Maritime Agentic AI Systems: Balancing Operator Workload and Safety Through Risk-Aware Governance Miller, T., Durlik, I., Biczak, P. Applied Sciences (Switzerland), 2026 https://www.scopus.com/pages/publications/105045853571?origin=scopusAI

27. Integrating Explainable AI to Enhance Dynamic Risk Assessment in Automated Driving Systems Patel, A.R., Gohler, T., Liggesmeyer, P. 2024 IEEE International Conference on Vehicular Electronics and Safety, ICVES 2024, 2024 https://www.scopus.com/pages/publications/105002127575?origin=scopusAI

28. Risk dynamics for marine systems: Towards a bio-inspired framework for dynamic risk assessment Ventikos, N.P., Louzis, K. Transportation Safety and Environment, 2022 https://www.scopus.com/pages/publications/85145361685?origin=scopusAI

29. Formal Analysis of AI-Based Autonomy: From Modeling to Runtime Assurance Torfah, H., Junges, S., Fremont, D.J., Seshia, S.A. Lecture Notes in Computer Science, 2021 https://www.scopus.com/pages/publications/85117473078?origin=scopusAI

30. The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems Aarab, H. International Conference on Human Centric Artificial Intelligence, ICHCAI 2026 - 1st International Conference, 2026 https://www.scopus.com/pages/publications/105046217618?origin=scopusAI

31. A<sup>4</sup>-Gov: A Governance Architecture for AI Service Systems Ahn, M.S., Yoon, Y.I. 2026 IEEE/ACIS 24th International Conference on Software Engineering Research, Management and Applications, SERA 2026, 2026 https://www.scopus.com/pages/publications/105047279989?origin=scopusAI

32. Establishing a framework for dynamic risk management in 'intelligent' aero-engine control Kurd, Z., Kelly, T., McDermid, J., (...), Kwiatkowska, M. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2009 https://www.scopus.com/pages/publications/70350448148?origin=scopusAI

33. Run-Time Assurance for Onboard COTS-Based AI in Safety-Critical LEO Small-Satellite Systems Khalid, O., Gamazo-Real, J.-C., Roibás-Millán, E. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105044837225?origin=scopusAI

34. Uncertainty-aware risk assessment and GRU-based risk level map generation for RSU-assisted vehicles Cao, Y., Shangguan, W., Visser, A., (...), Cai, B. Accident Analysis and Prevention, 2026 https://www.scopus.com/pages/publications/105044413882?origin=scopusAI

35. A highway crash risk assessment method based on traffic safety state division Sun, D., Ai, Y., Sun, Y., Zhao, L. PLoS ONE, 2020 https://www.scopus.com/pages/publications/85077899188?origin=scopusAI

36. Explainable artificial intelligence (XAI) to find optimal in-silico biomarkers for cardiac drug toxicity evaluation Pramudito, M.A., Fuadah, Y.N., Qauli, A.I., (...), Lim, K.M. Scientific Reports, 2024 https://www.scopus.com/pages/publications/85206279787?origin=scopusAI

37. Structured expert scenario methodology for autonomous system validation applied to a multi-UAS ground control station design Rinehart, D., Smith, P., Peters, M., Spencer, A. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2016 https://www.scopus.com/pages/publications/85009486484?origin=scopusAI

38. ReinSeed: Reinforcement Fuzz Testing With Multiphase Seed Optimization for Autonomous Driving Systems Jin, Q., Wu, T., Dong, Y., (...), Xu, Y. IET Software, 2025 https://www.scopus.com/pages/publications/105021245814?origin=scopusAI

39. Implementing Dynamic Consent Mechanisms in Multi-Agent AI Systems: A Practical Framework Bumpus, M.A. Conference Proceedings - IEEE SOUTHEASTCON, 2026 https://www.scopus.com/pages/publications/105037874145?origin=scopusAI

40. Multi-Agent Generative AI Systems for Cyber Risk Evaluation and Control Faisal, S.M., Khan, W., Ishrat, M., Shaikh, A.A. Generative AI for Cyber Risk Management, 2026 https://www.scopus.com/pages/publications/105044415175?origin=scopusAI

41. Risk Management Ligo, A.K., Kott, A., Dozier, H., Linkov, I. Advances in Information Security, 2023 https://www.scopus.com/pages/publications/85162054713?origin=scopusAI

42. A Risk Management Based on Artificial Intelligence Tools and Multi-criteria Decision Making Methods: Systematic Literature Review Waguaf, A., Benabbou, R., Benhra, J. Lecture Notes in Networks and Systems, 2023 https://www.scopus.com/pages/publications/85174437106?origin=scopusAI

43. Risk-averse autonomous systems: A brief history and recent developments from the perspective of optimal control Wang, Y., Chapman, M.P. Artificial Intelligence, 2022 https://www.scopus.com/pages/publications/85134154584?origin=scopusAI

44. Strengthening AI Validation and Verification in Autonomous Vehicles: Comprehensive Analysis and Improvements to Key Standards Dekkata, S.C., Tawade, H., Kamanuru, V.R., (...), Rathod, S. Proceedings - 2025 IEEE Conference on Artificial Intelligence, CAI 2025, 2025 https://www.scopus.com/pages/publications/105011254412?origin=scopusAI

45. Clinical Evaluation of an Artificial Intelligence-Based Decision Support System for the Diagnosis and American College of Radiology Thyroid Imaging Reporting and Data System Classification of Thyroid Nodules Fernández Velasco, P., Pérez López, P., Torres Torres, B., (...), Díaz Soto, G. Thyroid, 2024 https://www.scopus.com/pages/publications/85188555798?origin=scopusAI

46. Digital Twin Based Unmanned Vehicle AI Safety Testing Platform Yu, Z., Qian, Y., Zhong, Y., (...), Zou, X. Proceedings of 2025 2nd International Conference on Intelligent Driving and Smart Transportation, IDST 2025, 2025 https://www.scopus.com/pages/publications/105037608953?origin=scopusAI

47. Extensions to Production Availability and Functional Safety Analyses Signoret, J.-P., Leroy, A. Springer Series in Reliability Engineering, 2021 https://www.scopus.com/pages/publications/85103236065?origin=scopusAI

48. Reliable Edge Intelligence in Unreliable Environment Lee, M., She, X., Chakraborty, B., (...), Mukhopadhyay, S. Proceedings - Design, Automation and Test in Europe, DATE, 2021 https://www.scopus.com/pages/publications/85111049725?origin=scopusAI

49. The PacifAIst Benchmark: Do AIs Prioritize Human Survival over Their Own Objectives? Herrador, M. AI (Switzerland), 2025 https://www.scopus.com/pages/publications/105019960188?origin=scopusAI

50. Can We Trust AI Benchmarks? An Interdisciplinary Review of Current Issues in AI Evaluation Eriksson, M., Purificato, E., Noroozian, A., (...), Fernandez-Llorca, D. Proceedings of the 8th AAAI/ACM Conference on AI, Ethics, and Society, AIES 2025, 2025 https://www.scopus.com/pages/publications/105040217141?origin=scopusAI

51. Rethinking the Maturity of Artificial Intelligence in Safety-Critical Settings Cummings, M.L. AI Magazine, 2021 https://www.scopus.com/pages/publications/85167507918?origin=scopusAI

52. Is it safe to deploy AI in safety-critical systems? Kolda, T.G. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 2026 https://www.scopus.com/pages/publications/105045688462?origin=scopusAI

53. Safety-Critical Optimal Control for Autonomous Systems Xiao, W., Cassandras, G.C., Belta, C. Journal of Systems Science and Complexity, 2021 https://www.scopus.com/pages/publications/85117912536?origin=scopusAI

54. Exploring AI safety in degrees: Generality, capability and control Burden, J., Hernández-Orallo, J. CEUR Workshop Proceedings, 2020 https://www.scopus.com/pages/publications/85081638123?origin=scopusAI

55. A Survey on Risk-Adaptive Approaches in Autonomous Ecosystems Zhang, R., Halasz, D., Van Landuyt, D. Proceedings - 2026 IEEE 23rd International Conference on Software Architecture Companion, ICSA-C 2026, 2026 https://www.scopus.com/pages/publications/105048462655?origin=scopusAI
