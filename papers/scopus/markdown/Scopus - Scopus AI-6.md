---
source_pdf: "Scopus - Scopus AI-6.pdf"
source_sha256: "4d93c7cf0c8dd9b2b85318b1c97c42d212431f3995012db7db8c8bea014b28f3"
source_pages: 11
scopus_ai_generated: "Thu Apr 16 2026"
query: "AI advisory system architecture for environmental safety"
report_title: "Adaptive AI Advisory System Architectures: Restricting Recommendations by Classified Environmental Safety States"
converted_tables: 2
converter: "scopus2md.py (pdfplumber)"
---
# AI advisory system architecture for environmental safety

## Quick Reference

## Key Findings Table

| Theme/Topic | Key Insights | Representative Citations |
| --- | --- | --- |
| Adaptive AI Advisory Architectures | Modular, interpretable, and distributed architectures (e.g., SAFETYANALYST, AVI, ACAS X) dynamically restrict or vary recommendations based on classified environmental safety states. | 1 2 3 4 |
| Real-Time Adaptation | Ambient Advisory Models and multi-agent systems enable continuous monitoring and context-aware adaptation of recommendations. | 5 6 |
| Classification Methods | ML models (Random Forest, CNNs, ensemble, quantum-enhanced ML) and hybrid/case-based reasoning are used for robust, explainable safety state classification. | 7 8 9 10 |
| Recommendation Restriction | Safety nets, lookup tables, control barrier functions, and formal verification restrict recommendations to safe regions. | 4 11 12 13 |

## Mechanisms

| Domain-Specific Implementations | Aviation (ACAS X), maritime (COLREG-based frameworks, digital twins), industrial safety (predictive maintenance), and healthcare (operator behavior analysis) show tailored architectures. | 3 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- |
| Research Gaps | Lifecycle safety assurance, dataset safety, explainability, and regulatory adaptation for in-service AI remain open challenges. |  | 17 | 18 | 19 |

## Direct Answer

One notable paper is the approach underlying **SAFETYANALYST**, which details an interpretable framework that uses chain-of-thought reasoning to classify environmental safety states via a harm-benefit tree. This classification then dynamically adjusts the set of admissible recommendations, ensuring safety adaptations across different operational domains[1]. Additionally, the **Agreement Validation Interface (AVI)** architecture describes a modular API gateway that orchestrates multiple AI subcomponents to filter recommendations based on safety states[2].

## Study Scope

**Time Period:** Focus on literature from the last decade, with emphasis on recent advances (2018–2024). **Disciplines:** AI safety, autonomous systems, maritime/aviation/industrial safety, healthcare informatics. **Methods:** Systematic reviews, architectural proposals, empirical case studies, formal verification, and meta-analyses.

## Assumptions & Limitations

**Assumptions:** The report assumes that environmental safety state classification is a critical enabler for adaptive AI advisory systems across domains.

**Limitations:** Cross-domain generalizability is limited by domain-specific operational constraints and regulatory requirements. Some architectural proposals are conceptual or in early deployment stages, and real-world validation may be ongoing.

## Suggested Further Research

Develop unified, cross-disciplinary safety assurance frameworks for adaptive AI. Integrate human factors and explainability more deeply into runtime adaptation. Advance regulatory and lifecycle management for in-service, dynamically adapting AI systems. Explore hybrid human-AI collaboration models for continuous safety assurance.

## 1. Introduction

## Background and Motivation

Adaptive AI advisory systems are increasingly deployed in safety-critical domains—such as aviation, maritime, healthcare, and industrial automation—where the operational environment is dynamic and often unpredictable. In these contexts, the ability of an AI system to classify the current environmental safety state and restrict or vary its recommendations accordingly is essential for ensuring both functional performance and safety compliance[1][20][21]. The motivation for such architectures is clear: as AI systems assume greater autonomy and decision-making responsibility, the risk of unsafe or inappropriate recommendations grows, especially under degraded or uncertain conditions. Restricting the set of admissible recommendations based on real-time safety state classification is thus a foundational requirement for trustworthy, resilient AI advisory systems.

## 2. Architectural Foundations of Adaptive AI Advisory Systems

## Modular and Distributed Architectures

Modern adaptive AI advisory systems are characterized by modularity and distributed intelligence. Architectures such as the **Agreement Validation Interface (AVI)** employ modular API gateways that orchestrate multiple AI subcomponents, each responsible for input-output validation, contextual reasoning, and safety filtering[2]. This modularity enables:

**Separation of concerns:** Distinct modules for situational assessment, knowledge management, and decision-making.

**Scalability and extensibility:** New safety modules or reasoning agents can be added without disrupting the core system.

**Distributed reasoning:** Each module can act as an active advisory entity, continuously monitoring its domain and providing context-specific guidance[5][6]. **Multi-agent debate frameworks** further enhance oversight by embedding diverse sub-agents (e.g., ethical, legal, safety monitors) that deliberate adversarially to identify blind spots and adapt recommendations under deep uncertainty[6].

## Ambient Advisory Models and Real-Time Adaptation

**Ambient Advisory Models** extend traditional runtime models by embedding distributed reasoning capabilities into model components. Each component acts as an advisory agent, continuously monitoring its environment and generating context-aware advisories without direct actuation[5]. Key features include:

**Continuous monitoring:** Real-time assessment of environmental and operational changes.

**Proactive guidance:** Multi-perspective reasoning supports both human and machine decision-makers.

**Knowledge-based adaptation management:** Explicit representation of adaptation policies at the architectural level enables dynamic runtime policy evolution and strong decoupling between policy specification and architectural composition[22][23].

## Dynamic Policy Evolution and Governance

Adaptive AI advisory systems require robust policy management frameworks to ensure that recommendations remain compliant with evolving safety, ethical, and regulatory requirements. Recent advances include: **Modular governance architectures:** Combine jurisdiction-aware embeddings, ethical reasoning, and constraint logic for real-time, multi-jurisdictional compliance[24].

**TRiSM frameworks:** Embed explainability, real-time drift monitoring, and runtime enforcement for trustworthy AI[25].

**Generative policy models:** Use context-sensitive grammars and local knowledge sharing to enable autonomous systems to learn and evolve high-level policies dynamically[6][26].

## Synthesis:

The architectural landscape is converging on modular, distributed, and policy-driven designs that enable real-time adaptation of recommendations based on classified safety states. These patterns are domain-agnostic but are tailored in implementation to meet specific operational and regulatory needs.

## 3. Classification Methods for Environmental Safety States

## Machine Learning and Deep Learning Approaches

A variety of machine learning (ML) and deep learning (DL) models are employed to classify environmental safety states:

**Random Forest (RF):** High accuracy and robustness in classifying safety-critical messages in autonomous vehicles (accuracy up to 98.43%)[7][27]. **Convolutional Neural Networks (CNNs):** Widely used for object detection and classification in perception systems[8][28]. **Ensemble and stacking methods:** Combine multiple classifiers (e.g., MLP, RF) to enhance accuracy and reduce false positives[29]. **Quantum-enhanced ML:** Demonstrates higher accuracy and speed for rapid safety state classification[9]. **Graph neural networks:** Capture spatial dependencies for road safety risk assessment (F1 > 0.985)[10]. **Fusion-based transfer learning** and **explainable AI (XAI)** techniques further improve detection and classification, especially under adverse or uncertain conditions[30].

## Case-Based and Hybrid Reasoning

**Case-based reasoning (CBR)** leverages historical cases to classify new situations based on similarity, improving adaptability and reducing misclassification in dynamic environments[31][32][33]. Hybrid models integrate CBR with rule-based reasoning and data mining for enhanced accuracy and continuous learning[34] [35].

## Explainable AI for Safety State Classification

**Explainable AI (XAI)** is critical for transparency and trust: **Techniques:** SHAP, LIME, permutation feature importance, and saliency maps[36][37]. **Benefits:** Enable stakeholders to understand model decisions, identify key environmental indicators, and support actionable insights[37][38]. **Challenges:** Balancing accuracy and interpretability, and developing standardized evaluation metrics for explainability[39][40].

## Synthesis:

Robust, explainable classification of environmental safety states is foundational for adaptive AI advisory systems. The trend is toward hybrid, ensemble, and explainable models that can operate reliably in real time and under uncertainty.

## 4. Variation and Restriction of Recommendation Sets

## Mechanisms for Restricting Recommendations

AI advisory systems restrict or vary recommendations by: **Classifying safety states into regions:** Using explainable classifiers and topological data analysis to ensure only safe recommendations are generated[11][41]. **Safety nets and lookup tables:** Store known failure points and restrict outputs to pre-verified safe regions [4][42].

**Ambient Advisory Models:** Distribute advisory intelligence for context-aware, explainable recommendations[5].

**Hybrid human-AI frameworks:** Integrate explainable AI, uncertainty quantification, and human oversight to dynamically adjust recommendations[43][44][45].

## Control Barrier Functions and Formal Verification

## Control Barrier Functions (CBFs):

Enforce safety by maintaining system states within safe regions, even under sensor faults or attacks[13][46]. Integrated with layered control architectures and forward reachable sets for dynamic enforcement[46]. Combined with Model Predictive Control (MPC) and geometric constraints for real-time trajectory safety[47].

## Formal Verification:

**Reachability analysis, SMT-based verification, model checking:** Guarantee that only safe recommendations are possible under all environmental conditions[12][48][49].

**Neural network verification tools:** Certify AI outputs in safety-critical systems (e.g., aviation collision avoidance)[12].

**Executable specifications:** Translate human-machine interactions into formal languages for automated verification[50].

## Hybrid Human-AI Decision-Making

**Six-stage decision loops:** Sense → Predict → Explain → Human Gate → Act → Learn, balancing algorithmic inference with human judgment[43]. **Dynamic priority shifting:** AI agents resolve conflicts among normative constraints based on current safety state[44]. **Agentic AI frameworks:** Combine symbolic and data-driven reasoning for continuous adaptation[45].

## Synthesis:

Restricting recommendations to safe, admissible sets is achieved through a combination of formal methods, runtime monitoring, and human-in-the-loop frameworks. These mechanisms are essential for certifiable, trustworthy AI in safety-critical domains.

## 5. Domain-Specific Implementations

## Aviation and Autonomous Vehicles

**ACAS X (Airborne Collision Avoidance System X):** Uses neural networks to compress large lookup tables, enabling real-time, adaptive collision avoidance advisories based on operational design domain (ODD) monitoring[3][51].

**Runtime monitoring:** Temporal scene analysis ensures operation within defined environmental conditions. **Safety assurance:** Simulation-based testing and formal verification support certification for real-world deployment[52].

## Maritime Autonomous Surface Ships

**COLREG-based frameworks:** Encode maritime navigation rules into tiered, explainable knowledge bases for legally coherent, transparent maneuver decisions[14].

**Digital twins:** Integrate AI and virtual reality for live monitoring, risk avoidance, and environmental sustainability[53].

**Multi-agent systems:** Combine learning, forecasting, and planning for adaptive situational awareness and intelligent route planning[54].

## Industrial Safety and Healthcare

**Predictive maintenance:** Real-time hazard detection and operator behavior analysis support adaptive safety recommendations[15][16]. **Human factors integration:** Emphasis on cognitive workload, trust, and oversight in system design[55][56]. **Explainable error prediction:** Combines human factors classification with ML for interpretable safety analytics[57].

## Synthesis:

Domain-specific implementations demonstrate the flexibility and necessity of adaptive architectures. While core patterns are shared, each domain tailors its approach to unique operational, regulatory, and human factors.

## 6. Research Gaps and Future Directions

## Lifecycle Safety Assurance and Standards

**Gaps:** Limited cross-disciplinary collaboration, underdeveloped dataset safety management, and insufficient explainability in current standards[17][18][19].

**Needs:** ML-aware compliance frameworks, simulation-based evidence, and dynamic runtime monitoring for adaptive AI[58][59].

## Human Factors and Situational Awareness

**Challenges:** Integrating human factors, trust calibration, and situational awareness into AI advisory systems [55][56][60].

**Solutions:** Human-centered design, clear communication of AI limitations, and robust safety management systems[60][61].

## Dynamic Adaptation and Regulatory Challenges

**Regulatory reform:** Needed to accommodate in-service adaptation and pre-approved boundaries for ML changes[62][63].

**Open questions:** Should dynamic, ML-enabled safety adaptations occur autonomously online or only within restricted, human-supervised boundaries?[63].

## Synthesis:

While adaptive AI advisory architectures are advancing rapidly, significant research and regulatory gaps remain. Addressing these will require interdisciplinary collaboration, new assurance methodologies, and a focus on human-AI collaboration.

## 7. Conclusion

## Summary and Outlook

Adaptive AI advisory system architectures that restrict or vary recommendations based on classified environmental safety states are now foundational in safety-critical domains. Key frameworks such as SAFETYANALYST, AVI, and ACAS X demonstrate that modular, distributed, and policy-driven designs can dynamically ensure safety by bounding recommendations to admissible sets. Robust classification methods, formal verification, and hybrid human-AI frameworks underpin these advances.

However, the field faces ongoing challenges in lifecycle safety assurance, explainability, regulatory adaptation, and integration of human factors. Future research should prioritize unified assurance frameworks, deeper explainability, and regulatory innovation to support the safe, trustworthy deployment of adaptive AI advisory systems across domains[1][63].

## References

1. SAFETYANALYST: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior Li, J.-J., Pyatkin, V., Kleiman-Weiner, M., (...), Levine, S. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105023829523?origin=scopusAI

2. Innovative Guardrails for Generative AI: Designing an Intelligent Filter for Safe and Responsible LLM Deployment Shvetsova, O., Katalshov, D., Lee, S.-K. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105010274384?origin=scopusAI

3. Towards the Monitoring of Operational Design Domains Using Temporal Scene Analysis in the Realm of Artificial Intelligence in Aviation Girija, A.A., Christensen, J.M., Stefani, T., (...), Krüger, T. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2024 https://www.scopus.com/pages/publications/85211250339?origin=scopusAI

4. SAFEXPLAIN: a Complete Approach Towards Trustworthy AI-Based Safety-Critical Systems Abella, J., Agirre, I., Bui, T., (...), Dallara, V. Proceedings - 2025 28th Euromicro Conference on Digital System Design, DSD 2025, 2025 https://www.scopus.com/pages/publications/105030537985?origin=scopusAI

5. Ambient Advisory Models: Augmenting Runtime Models into Distributed Reasoning Agents Hernandez, D., Cleland-Huang, J. Proceedings - 2025 ACM/IEEE 28th International Conference on Model Driven Engineering Languages and Systems, MODELS 2025, 2025 https://www.scopus.com/pages/publications/105029871697?origin=scopusAI

6. Building Robust Artificial Intelligence Through Multi-Agent Debate Bauschard, S. AI Pluralism: Fostering Diversity and Dialogue in Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105032894204?origin=scopusAI

7. Machine Learning-based Secure Communication Framework for Connected Autonomous Vehicles Jivani, D., Gajjar, H., Gupta, R., (...), Trivedi, H. 2023 IEEE Globecom Workshops, GC Wkshps 2023, 2023 https://www.scopus.com/pages/publications/85190258245?origin=scopusAI

8. Behavioral Arbitration for Effective Decision Making in Autonomous Vehicles by Using Deep Convolutional Neural Networks Rallapalli, S., Dileep, M.R., Chandana, T.M. Communications in Computer and Information Science, 2025 https://www.scopus.com/pages/publications/105022740073?origin=scopusAI

9. Quantum-enhanced machine learning technique for rapid post-earthquake assessment of building safety Bhatta, S., Dang, J. Computer-Aided Civil and Infrastructure Engineering, 2024 https://www.scopus.com/pages/publications/85195500106?origin=scopusAI

10. A spatial graph learning framework for multi-scale road safety management based on road-curve features and open-source data Gao, Z., Ge, H., Easa, S.M., (...), Wang, Y. Computer-Aided Civil and Infrastructure Engineering, 2025 https://www.scopus.com/pages/publications/105019084447?origin=scopusAI

11. Safe and Efficient Social Navigation Through Explainable Safety Regions Based on Topological Features Toscano-Duran, V., Narteni, S., Carlevaro, A., (...), Mongelli, M. Communications in Computer and Information Science, 2026 https://www.scopus.com/pages/publications/105020661494?origin=scopusAI

12. Guaranteeing Safety for Neural Network-Based Aircraft Collision Avoidance Systems Julian, K.D., Kochenderfer, M.J. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2019 https://www.scopus.com/pages/publications/85084746222?origin=scopusAI

13. Control Barrier Functions for Safe CPS under Sensor Faults and Attacks Clark, A., Li, Z., Zhang, H. Proceedings of the IEEE Conference on Decision and Control, 2020 https://www.scopus.com/pages/publications/85099875483?origin=scopusAI

14. Resolving Legal Ambiguities for Safe MASS Navigation: A Socio-Technical Approach Using Human- Machine Learning Verma, S., Varghese, D., Treloar, A.A., (...), Tamaddoni-Nezhad, A. Oceans Conference Record (IEEE), 2025 https://www.scopus.com/pages/publications/105029528129?origin=scopusAI

15. Intelligent Conceptual Architecture as a Proposal for Integration of Artificial Intelligence for Accident Prevention with Heavy Equipment de Macêdo Neto, A.P., dos Reis, J.G.M., da Cruz Correia, P.F., (...), de Souza, J.S. IFIP Advances in Information and Communication Technology, 2026 https://www.scopus.com/pages/publications/105015356272?origin=scopusAI

16. Enhancing Safety and Efficiency in Maritime Ergatic Systems Through Advanced Information Technologies Onyshchenko, S., Savelieva, I., Melnyk, O., (...), Kotenko, O. Studies in Systems, Decision and Control, 2025 https://www.scopus.com/pages/publications/105008805532?origin=scopusAI

17. Safety Assurance of Artificial Intelligence-Based Systems: A Systematic Literature Review on the State of the Art and Guidelines for Future Work Neto, A.V.S., Camargo, J.B., Almeida, J.R., Cugnasca, P.S. IEEE Access, 2022 https://www.scopus.com/pages/publications/85144813199?origin=scopusAI

18. Safety Standards and Safety Assurance Framework for ADS Taguchi, K., Ishikawa, F., Kobayashi, T., Hasuo, I. Safety Assurance under Uncertainties: From Software to eyber-Physical/Machine Learning Systems, 2025 https://www.scopus.com/pages/publications/105002883060?origin=scopusAI

19. Safe Deployment of AI and ML Based Software and Algorithms in ADAS Systems Mudunuri, V.R., Almasri, H., Fan, H.-H., Chandrasekaran, M. SAE Technical Papers, 2025 https://www.scopus.com/pages/publications/105008188845?origin=scopusAI

20. Managing Sources of Uncertainty in Utilizing AI in Development and Deployment of Safety-Critical Autonomous Systems Lowe, R., Ulan, M., Bui, T.H., (...), Brando, A. Proceedings - 2025 IEEE 22nd International Conference on Software Architecture, ICSA-C 2025, 2025 https://www.scopus.com/pages/publications/105007947926?origin=scopusAI

21. COMPREHENSIVE MULTI-ENVIRONMENT OPERATIONAL DESIGN DOMAIN TAXONOMY FOR INTELLIGENT SYSTEMS SAFETY DESIGN Al-Shareefy, H., Butler, M., Hoang, T.S. 68th Annual Meeting of the International Society for the Systems Sciences, ISSS 2024, 2024 https://www.scopus.com/pages/publications/105010328018?origin=scopusAI

22. Knowledge-based architectural adaptation management for self-adaptive systems Georgas, J.C. Proceedings - International Conference on Software Engineering, 2005 https://www.scopus.com/pages/publications/33244460047?origin=scopusAI

23. Knowledge-based architectural adaptation management for self-adaptive systems Georgas, J.C. Proceedings - 27th International Conference on Software Engineering, ICSE05, 2005 https://www.scopus.com/pages/publications/85086684974?origin=scopusAI

24. Cross-Jurisdictional Ethical Governance and Legal Accountability Architecture for Autonomous AI- Powered Legal Advisory Systems Nimrud, A.H., Al-Rubay, S.H.A., Ali, Z.A.A.W., (...), Madi, A.A. ICCR 2025 - 3rd International Conference on Cyber Resilience, 2025 https://www.scopus.com/pages/publications/105031605846?origin=scopusAI

25. A Review of TRiSM Frameworks in Artificial Intelligence Systems: Fundamentals, Taxonomy, Use Cases, Key Challenges and Future Directions Ray, P.P. Expert Systems, 2026 https://www.scopus.com/pages/publications/105029030878?origin=scopusAI

26. Towards a learning-Algorithm agnostic generative policy model for coalitions Cunnington, D., Law, M., De Mel, G., (...), Verma, D. Proceedings of SPIE - The International Society for Optical Engineering, 2019 https://www.scopus.com/pages/publications/85072563682?origin=scopusAI

27. XAI-AV: Explainable Artificial Intelligence for Trust Management in Autonomous Vehicles Mankodiya, H., Obaidat, M.S., Gupta, R., Tanwar, S. Proceedings of the 2021 IEEE International Conference on Communications, Computing, Cybersecurity and Informatics, CCCI 2021, 2021 https://www.scopus.com/pages/publications/85119284789?origin=scopusAI

28. Object Classification Using A rtificial i ntelligence Technique s i n Autonomous Vehicles Juyal, A., Sharma, S., Matta, P. 2023 3rd International Conference on Artificial Intelligence and Signal Processing, AISP 2023, 2023 https://www.scopus.com/pages/publications/85163156879?origin=scopusAI

29. Artificial intelligence-based model for efficient object detection in autonomous vehicles Zhang, Z., Zhang, Q., Liu, H., (...), Wang, L. Journal of Intelligent Transportation Systems: Technology, Planning, and Operations, 2025 https://www.scopus.com/pages/publications/105004431893?origin=scopusAI

30. Explainable artificial intelligence with fusion-based transfer learning on adverse weather conditions detection using complex data for autonomous vehicles Tarmissi, K., Mengash, H.A., Negm, N., (...), Al-Sharafi, A.M. AIMS Mathematics, 2024 https://www.scopus.com/pages/publications/85214204864?origin=scopusAI

31. A comparative study on the use of similarity measures in case-based reasoning to improve the classification of environmental system situations Núñez, H., Sànchez-Marrè, M., Cortés, U., (...), Poch, M. Environmental Modelling and Software, 2004 https://www.scopus.com/pages/publications/2642570246?origin=scopusAI

32. Case-based Reasoning for Structural Health Monitoring Freudenthaler, B., Stumptner, R., Forstner, E., Küng, J. Proceedings of the 4th European Workshop on Structural Health Monitoring, 2008 https://www.scopus.com/pages/publications/62949182175?origin=scopusAI

33. CORMS AI: Decision support system for monitoring US maritime environment Vafaie, H., Cecere, C. Proceedings of the National Conference on Artificial Intelligence, 2005 https://www.scopus.com/pages/publications/29344467220?origin=scopusAI

34. Case-based reasoning and decision support systems Babka, Otakar, Whar, Si Yain Proceedings of the IEEE International Conference on Intelligent Processing Systems, ICIPS, 1998 https://www.scopus.com/pages/publications/0031676393?origin=scopusAI

35. Development of a real-time data quality monitoring system using embedded intelligence Bethem, T., Evans, M., Vafaie, H., Shaughnessy, M. Oceans Conference Record (IEEE), 2002 https://www.scopus.com/pages/publications/0038306722?origin=scopusAI

36. Reviewing Explainable Artificial Intelligence Towards Better Air Quality Modelling Tasioulis, T., Karatzas, K. Progress in IS, 2024 https://www.scopus.com/pages/publications/85191472347?origin=scopusAI

37. Trusted artificial intelligence for environmental assessments: An explainable high-precision model with multi-source big data Xu, H., Yang, X., Hu, Y., (...), Hu, Z. Environmental Science and Ecotechnology, 2024 https://www.scopus.com/pages/publications/85202572605?origin=scopusAI

38. Explaining Explainable Artificial Intelligence: An integrative model of objective and subjective influences on XAI Alarcon, G.M., Willis, S.M. Proceedings of the Annual Hawaii International Conference on System Sciences, 2023 https://www.scopus.com/pages/publications/85152147673?origin=scopusAI

39. Explainable AI (XAI): Techniques, applications, and challenges Kopzhasarova, M., Kozhamzharova, D. CEUR Workshop Proceedings, 2025 https://www.scopus.com/pages/publications/105006886912?origin=scopusAI

40. Advancement in Explainable AI: Bringing Transparency and Interpretability to Machine Learning Models for Use in High-Stakes Decisions David, R., Shankar, H., Kura, P., (...), Karkuzhali, S. 2025 International Conference on Emerging Smart Computing and Informatics, ESCI 2025, 2025 https://www.scopus.com/pages/publications/105007282593?origin=scopusAI

41. Ensuring Safe Social Navigation via Explainable Probabilistic and Conformal Safety Regions Narteni, S., Carlevaro, A., Guzzi, J., Mongelli, M. Communications in Computer and Information Science, 2024 https://www.scopus.com/pages/publications/85200688481?origin=scopusAI

42. Towards Certifiable AI in Aviation: A Framework for Neural Network Assurance Using Advanced Visualization and Safety Nets Christensen, J.M., Zaeske, W., Beck, J., (...), Hallerbach, S. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2024 https://www.scopus.com/pages/publications/85211193695?origin=scopusAI

43. Hybrid human–AI decision-making for fire-related disaster risk reduction Shekili, S. Progress in Disaster Science, 2026 https://www.scopus.com/pages/publications/105032584262?origin=scopusAI

44. Agentic rulebooks using active inference: an artificial intelligence application for environmental sustainability Constant, A., Albarracin, M., Perin, M., (...), Friston, K.J. Frontiers in Sustainable Cities, 2025 https://www.scopus.com/pages/publications/105005978146?origin=scopusAI

45. A Hybrid Agentic AI Framework Integrating AIML and Machine Learning for Context-Aware Autonomous Systems Shivaramaiah, P., Ramesh, R., Nagraj, K. 4th IEEE North Karnataka Subsection Flagship International Conference: Holistic Engineering for Sustainable Development, NKCon 2025, 2025 https://www.scopus.com/pages/publications/105033082635?origin=scopusAI

46. Safety-Critical Coordination of Legged Robots via Layered Controllers and Forward Reachable Set based Control Barrier Functions Kim, J., Lee, J., Ames, A.D. Proceedings - IEEE International Conference on Robotics and Automation, 2024 https://www.scopus.com/pages/publications/85202450556?origin=scopusAI

47. Real-Time Reachable Set-Based Model Predictive Control for Safe Trajectory Tracking of Quadrotors Patel, J., Kaya, U.C., Subbarao, K. AIAA Science and Technology Forum and Exposition, AIAA SciTech Forum 2026, 2026 https://www.scopus.com/pages/publications/105031184941?origin=scopusAI

48. Formal verification of collision avoidance for turning maneuvers in uavs Adler, E., Jeannin, J.-B. AIAA Aviation 2019 Forum, 2019 https://www.scopus.com/pages/publications/85085248298?origin=scopusAI

49. Formal methods for safety-critical machine learning: a systematic literature review Newcomb, A., Ochoa, O. Frontiers in Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105031810112?origin=scopusAI

50. Formal assurance for cooperative intelligent autonomous agents Bhattacharyya, S., Eskridge, T.C., Neogi, N.A., (...), Stafford, M. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2018 https://www.scopus.com/pages/publications/85045320970?origin=scopusAI

51. Advancing the AI-Based Realization of ACAS X Towards Real-World Application Christensen, J.M., Girija, A.A., Stefani, T., (...), Hallerbach, S. Proceedings - International Conference on Tools with Artificial Intelligence, ICTAI, 2024 https://www.scopus.com/pages/publications/85211246671?origin=scopusAI

52. Safety-Centric Architecture for AI-Enabled Autonomous Driving Systems Arora, J., Esper, A., Santos, V. IEEE/IFIP International Conference on Dependable Systems and Networks Workshops, DSN-W, 2025 https://www.scopus.com/pages/publications/105029832334?origin=scopusAI

53. The Impact of Digital Twins Technology in Maritime Fleet and Safety Management Markopoulos, E., Markopoulos, P., Nandi, A., (...), Filahtos, G. Applied Human Factors and Ergonomics International, 2024 https://www.scopus.com/pages/publications/105031107514?origin=scopusAI

54. Data-driven multi-agent system for maritime traffic safety management Xiao, Z., Fu, X., Zhang, L., (...), Goh, R.S.M. IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC, 2017 https://www.scopus.com/pages/publications/85046284761?origin=scopusAI

55. HUMAN OVERSIGHT IN SHIP AUTONOMY van de Merwe, K., Veitch, E. Human Factors in Remote Ship Operations, 2026 https://www.scopus.com/pages/publications/105027708906?origin=scopusAI

56. COGNITIVE CHALLENGES OF HUMANTECHNOLOGY INTERACTION IN REMOTE MARITIME AUTONOMOUS OPERATIONS Awad, E., Mallam, S.C. Human Factors in Remote Ship Operations, 2026 https://www.scopus.com/pages/publications/105027707649?origin=scopusAI

57. Explainable human error prediction for autonomous vessels: combining human factors analysis and classification system with machine learning Kim, D.-H. WMU Journal of Maritime Affairs, 2026 https://www.scopus.com/pages/publications/105031411785?origin=scopusAI

58. Safety Assurance Concepts for Automated Driving Systems Ballingall, S., Sarvi, M., Sweatman, P. SAE Technical Papers, 2020 https://www.scopus.com/pages/publications/85083845038?origin=scopusAI

59. Bridging the Gaps: A Comparative Analysis of ISO 21434, ISO 26262 and Machine Learning in Autonomous Vehicles Daiene De Oliveira Bastos, S., Castelo Branco, K., Luiz De Oliveira, A. 27th Brazilian Symposium on Robotics and 26th Workshop on Robotics in Education, SBR-WRE 2025, 2025 https://www.scopus.com/pages/publications/105029910472?origin=scopusAI

60. Assuring safe implementation of decision support functionality based on data-driven methods for ship navigation Brandsæter, A., Smefjell, G., van de Merwe, K., Kamsvåg, V. Proceedings of the 30th European Safety and Reliability Conference and the 15th Probabilistic Safety Assessment and Management Conference, 2020 https://www.scopus.com/pages/publications/85107267213?origin=scopusAI

61. Assuring safe implementation of decision support functionality based on data-driven methods for ship navigation Brandsæter, A., Smefjell, G., van de Merwe, K., Kamsvåg, V. 30th European Safety and Reliability Conference, ESREL 2020 and 15th Probabilistic Safety Assessment and Management Conference, PSAM 2020, 2020 https://www.scopus.com/pages/publications/85110270073?origin=scopusAI

62. Safety assurance for automated driving systems that can adapt using machine learning: A qualitative interview study Ballingall, S., Sarvi, M., Sweatman, P. Journal of Safety Research, 2023 https://www.scopus.com/pages/publications/85142396315?origin=scopusAI

63. Safety Assurance for Automated Driving Systems: Open Problems and Learnings from a Review of Other Domains Ballingall, S., Sarvi, M., Sweatman, P. SAE International Journal of Connected and Automated Vehicles, 2022 https://www.scopus.com/pages/publications/85139568154?origin=scopusAI
