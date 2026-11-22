---
source_pdf: "Scopus - Scopus AI - AI recommendations and runtime architectures.pdf"
source_sha256: "aa66aa0913772efa33c71e7cfb316fe281b28323a44ac4bc4ee8aabdddc83ed6"
source_pages: 12
scopus_ai_generated: "Thu Apr 16 2026"
query: "AI recommendations and runtime architectures"
report_title: "Runtime Architectures for Pre-generation Restriction of AI Recommendations Based on Environmental and Operational State Classification"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# AI recommendations and runtime architectures

## Quick Reference

## Key Findings Table

| Theme | Key Insights | Representative Citations |
| --- | --- | --- |
| Pre-generation AI Control | Runtime assurance architectures (e.g., ASIF, constraint-based planning, layered safeguards) restrict AI recommendations pre-generation based on classified states, surpassing on/off switches and post-generation filters. | 1 2 3 |
| Foundational Concepts | Admissible action space, operational design domain (ODD), adaptive autonomy, and graduated safety architectures define and dynamically enforce the boundaries for safe AI operation. | 3 4 5 |
| State Classification | Hybrid, supervised, and unsupervised ML models (e.g., random forests, SVM, neural networks, clustering) enable real-time environmental/operational state tagging for AI control. | 6 7 8 |
| Explainability & Traceability | Integration of explainable AI (XAI) and model-based system engineering (MBSE) enhances transparency, trust, and traceability in runtime architectures. | 9 10 11 |
| Runtime Monitoring | Probabilistic, ensemble, and runtime instrumentation methods address uncertainty and optimize decision-making under dynamic conditions. | 12 13 14 |
| Research Gaps | Limited real-world validation, lack of benchmarks, and traceability challenges persist; hybrid models and standardization are needed. | 15 16 17 |

## Direct Answer

There is a growing body of computer science literature focusing on runtime architectures that preemptively restrict the scope or category of AI recommendations based on classified environmental or operational states. These architectures employ mechanisms such as active set invariance filtering, constraint-based planning, and dynamic operational design domain frameworks to restrict which recommendation types the AI may produce at all—prior to generation. Foundational concepts like admissible action space, ODD, adaptive autonomy, and graduated safety architectures are central to these approaches, enabling proactive, context-aware safety controls that go beyond simple on/off switches or post-generation output filters[1][2][3][4].

## Study Scope

**Time Period:** 2015–2024 (emphasis on recent advances) **Disciplines:** Computer Science, AI Safety, Autonomous Systems, Cyber-Physical Systems, Human-AI Interaction **Methods:** Literature review, meta-analysis, synthesis of empirical and theoretical studies, cross-domain comparison

## Assumptions & Limitations

Focus is on runtime architectures for pre-generation restriction, not post-generation filtering or binary safety switches. Emphasis on safety-critical domains (e.g., autonomous vehicles, aerospace, industrial automation). Some cited approaches are conceptual or validated in simulation; real-world deployments remain limited. The field is rapidly evolving; some methods may lack standardized benchmarks or regulatory acceptance.

## Suggested Further Research

Develop standardized benchmarks and scenario-based validation pipelines for pre-generation AI control. Advance hybrid AI models integrating rule-based, neural, and unsupervised learning for dynamic restriction. Enhance traceability frameworks linking safety requirements to runtime ML components. Explore LLM-driven automation for translating operational design documents into formal runtime models. Investigate real-world deployments and longitudinal studies to assess robustness and scalability.

## 1. Introduction

## Background and Motivation

The increasing deployment of AI in safety-critical domains—such as autonomous vehicles, aerospace, and industrial automation—demands robust mechanisms to ensure that AI systems operate safely within their intended boundaries. Traditional safety approaches, such as on/off switches or post-generation output filters, are insufficient for complex, adaptive environments where the consequences of unsafe recommendations can be severe[4][18][19]. Instead, there is a growing emphasis on pre-generation restriction mechanisms: runtime architectures that proactively limit the types of recommendations or actions an AI system can generate, based on real-time classification of environmental or operational states.

This report surveys the state-of-the-art in such architectures, clarifies their theoretical underpinnings, reviews classification methods for environmental and operational states, and identifies research gaps and future directions.

**2. Pre-generation Restriction Mechanisms in AI Runtime Architectures** **2.1 Run-time Assurance Architectures and Active Set Invariance Filtering**

**Run-time Assurance (RTA):** RTA architectures act as supervisory layers that monitor AI controllers in real time, intervening to restrict or override recommendations before they are generated if safety constraints are at risk[1][3][20][21][22].

**Active Set Invariance Filtering (ASIF):** ASIF minimally modifies unsafe AI commands to ensure safety, supporting certification in aerospace and other domains. It operates pre-generation, filtering out unsafe actions before they are executed[1].

**Applications:** Used in aerospace, autonomous vehicles, and robotics, these architectures enable compliance with safety standards and support continuous verification.

## 2.2 Layered Extrinsic Safeguarding Mechanisms

**Layered Safeguards:** Multi-layered runtime assurance systems act as trust anchors, bounding AI behavior through independent monitors, verifiable fallback paths, and continuous verification[3][23][24].

**Monitor-Controller Independence:** Ensures that safety monitors can independently detect hazards and trigger safe reactions, even if the primary AI controller fails or behaves unpredictably.

**Fallback Paths:** Formally verified safety controllers or fallback mechanisms guarantee system-level safety when the AI controller is uncertain or unsafe.

## 2.3 Constraint-based Planning and Dynamic Control Limits

**Constraint-based Planning:** Approaches like Tumato 2.0 generate policies that guarantee safe behavior by explicitly modeling non-deterministic outcomes and safety constraints, enabling preemptive restriction of AI recommendations[20][25].

**Dynamic Control Limits Application (DCLA):** DCLA strategies classify operational design domains (ODDs) and scenarios in real time, enforcing flexible, scenario-based safety limits that adapt to changing conditions[25].

**2.4 Recent Advances: Modular, Probabilistic, and LLM-based Architectures**

**Modular RTA Frameworks:** New frameworks leverage automatic differentiation (e.g., JAX) for flexible, constraint-based safety filtering, automating the enforcement of user-defined constraints[26].

**Probabilistic Guardrails:** Bayesian runtime risk estimation provides context-dependent bounds on safety violations, enabling cautious rejection of potentially dangerous actions[12].

**Neural Policy Applicability Filtering:** Predicate abstraction and applicability filtering restrict neural network action policies to only those actions deemed safe, improving verification speed and reliability[27].

**LLM-agnostic API Gateways:** Modular interfaces (e.g., Agreement Validation Interface) orchestrate validation and contextual reasoning components to filter unsafe or biased recommendations before

generation, supporting LLM-based systems[2].

## Synthesis:

Pre-generation restriction mechanisms are increasingly sophisticated, combining formal methods, probabilistic reasoning, and modular architectures to enforce safety envelopes dynamically. These approaches move beyond static safety switches, enabling adaptive, context-aware control in complex environments[1][2][3].

**3. Conceptual Foundations: Admissible Action Space, ODD, and Scope-conditioned AI** **3.1 Operational Design Domain (ODD) and Admissible Action Space**

**ODD Frameworks:** ODDs define the environmental and operational conditions under which an AI system is designed to function safely. They provide a formal basis for dynamically restricting the AI’s action space in response to changing contexts[4][5][19][20].

**Admissible Action Space:** This concept limits AI actions to those within predefined safe boundaries, preventing operation outside the system’s conceptual domain and serving as a foundational pre-generation restriction[19][20].

## 3.2 Adaptive Autonomy and Graduated Safety Architecture

**Adaptive Autonomy:** AI systems adjust their autonomy level based on operational context and safety requirements, integrating human oversight and automated decision-making to maintain safety[28][29].

**Graduated Safety Architecture:** Employs layered, independent safeguarding mechanisms (e.g., runtime assurance, safety cages) to enforce safety envelopes and provide verifiable fallback paths, complementing pre-generation restrictions[1][3].

## 3.3 Scope-conditioned AI and Model-based System Engineering

**Scope-conditioned AI:** Tailors AI behavior to specific operational scopes or domains, enhancing predictability and safety by restricting functions to well-understood environments[30][31].

**Model-based System Engineering (MBSE):** Supports transparent, verifiable pre-generation restrictions by embedding explainability and traceability into AI system design[31][32].

## Synthesis:

These foundational concepts provide the theoretical scaffolding for runtime architectures that restrict AI recommendations pre-generation. By formalizing operational boundaries and integrating adaptive, layered safeguards, they enable dynamic, context-aware safety enforcement[3][4].

**4. Operationalization of ODDs and Real-time Restriction of AI Action Spaces**

## 4.1 Formal Models and Real-time Monitoring Techniques

**Formalization:** ODDs are specified using mathematical, tabular, or Petri net models, enabling precise definition of operational boundaries and automatic selection of valid data producers (e.g., sensors, ML components)[33][34][35].

**Real-time Monitoring:** Techniques such as fuzzy sets, predictive monitoring, and scenario generation detect deviations from the ODD, triggering safe fallback or adaptation[36][37][38].

**Context-aware Input Selection:** Dynamically activates or deactivates ML components based on ODD satisfaction, optimizing resource use and restricting AI action spaces[34].

## 4.2 Markov Decision Processes for Long-term ODD Compliance

**MDPs:** Used to model long-term decision-making, ensuring that AI systems plan actions that maintain operation within the ODD over time, not just in the immediate context[39][40].

## 4.3 Implementation Challenges and Design Patterns

**Design Patterns:** Multi-agent debate frameworks, sensor fusion, and adaptive safe state managers are emerging patterns for graduated safety architectures[41][42][43].

**Challenges:** Include managing unpredictability, ensuring compliance with safety standards, and integrating AI with legacy systems. Holistic, multi-layered architectures are needed to address these challenges[44][45].

## Synthesis:

Operationalizing ODDs in real time is central to dynamic restriction of AI action spaces. Formal models, real-time monitoring, and long-term planning frameworks (e.g., MDPs) enable AI systems to adapt safely to evolving operational contexts[33][39].

**5. Classification Methods for Environmental and Operational States**

## 5.1 Supervised and Hybrid Machine Learning Models

**Supervised Learning:** Random forests, SVMs, neural networks, and ensemble methods are widely used for classifying operational states, balancing accuracy and interpretability[6][46][47].

**Hybrid Models:** Combine interpretable models (e.g., decision trees) with high-accuracy models (e.g., deep learning), often using explainability techniques (e.g., SHAP, LIME) to enhance transparency in safety-critical contexts[6][48][49].

## 5.2 Hybrid AI Classification Systems

**Neuro-symbolic Approaches:** Integrate rule-based and neural network methods, leveraging the strengths of both for flexible, robust environmental state recognition[8][50].

**Hierarchical Hybrid Systems:** Use specialized neural networks for continuous attributes and rule-based components for discrete attributes, synthesizing outputs for improved classification[50][51].

## 5.3 Unsupervised Learning for Real-time State Tagging

**Clustering and Dimensionality Reduction:** Unsupervised methods (e.g., k-means, self-supervised learning) enable real-time tagging of environmental states, especially when labeled data is scarce or unavailable[7][52] [53].

**Hybrid Approaches:** Combine unsupervised and supervised learning for robust, adaptive state classification in dynamic environments[7]. **5.4 Explainability Techniques for Safety-critical Classification** **SHAP and LIME:** Widely used for interpreting model predictions in real time, enhancing trust and governance in safety-critical applications[49][54]. **Integration with Predictive Analytics:** Explainability is increasingly embedded in unified analytics stacks for hazardous state classification and operational safety[49].

## Synthesis:

A diverse set of classification methods—spanning supervised, hybrid, and unsupervised learning—enables accurate, interpretable, and real-time identification of environmental and operational states. These classifications are foundational for informing pre-generation AI recommendation restrictions[6][7][49].

**6. Research Gaps and Future Directions in Pre-generation AI Recommendation Control**

## 6.1 Current Limitations and Open Challenges

**Interpretability and Generalizability:** Many AI approaches remain black-box, limiting trust and adoption in safety-critical domains[15][55][56]. **Real-world Validation:** Overreliance on simulation, lack of standardized benchmarks, and limited real-world testing hinder robust evaluation[15][16][17]. **Traceability:** Difficulty in linking safety requirements to ML components complicates assurance and certification[57][58]. **6.2 Integration of Explainable AI and Model-based System Engineering** **Transparency:** Combining MBSE with XAI enables real-time, domain-adapted explanations, improving trust and regulatory compliance[9][59][60]. **Interactive Explanations:** Layered, user-adapted explanation frameworks enhance user comprehension and satisfaction[61][62].

## 6.3 Standardized Benchmarks and Real-world Validation

**Scenario-based Testing:** Scenario generation, simulation, and coverage analysis are essential for validating pre-generation restriction mechanisms[63][64][65].

**Domain-specific Frameworks:** Automotive, aerospace, and rail domains are developing tailored validation pipelines, but cross-domain standards are still emerging[66][67].

## 6.4 Architectural Mitigation Strategies for Uncertainty

**Ensemble Learning and Redundancy:** Improve reliability and mitigate prediction errors in ML components [68][69].

**Runtime Monitoring:** Statistical and explainable monitoring frameworks address uncertainty during operation[13][70].

## 6.5 Traceability and Assurance in Runtime AI Architectures

**Models at Runtime (M@RT):** Enable continuous verification and traceability between safety requirements and runtime ML components[11][14].

**Decentralized Instrumentation:** Algorithms like RIARC facilitate reliable monitoring and traceability in distributed systems[71].

## Synthesis:

Despite significant advances, the field faces persistent challenges in interpretability, validation, and traceability. Addressing these gaps will require standardized benchmarks, hybrid AI models, and integrated assurance frameworks[11][15][17].

## 7. Conclusion

## Summary and Outlook

Pre-generation restriction mechanisms in AI runtime architectures represent a paradigm shift in safety assurance for autonomous and safety-critical systems. By leveraging concepts such as ODD, admissible action space, and graduated safety architectures, these systems proactively restrict AI recommendations based on real-time environmental and operational state classification. Advances in runtime assurance, modular architectures, and explainable AI are driving the field forward, but challenges remain in validation, standardization, and traceability.

Future research should focus on developing standardized evaluation pipelines, integrating hybrid and explainable AI models, and operationalizing these architectures in real-world settings. As AI systems become increasingly autonomous and embedded in critical infrastructure, robust pre-generation restriction mechanisms will be essential for ensuring safety, trust, and societal acceptance[4][18][55].

## References

1. Bridging the Gap: Applying Argument to MIL-HDBK-516C Certification of a Neural Network Controller Guarded by ASIF Run Time Assurance Rowanhill, J., Hobbs, K.L., Zutshi, A., Hocking, A.B. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2023 https://www.scopus.com/pages/publications/85178664087?origin=scopusAI

2. Innovative Guardrails for Generative AI: Designing an Intelligent Filter for Safe and Responsible LLM Deployment Shvetsova, O., Katalshov, D., Lee, S.-K. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105010274384?origin=scopusAI

3. Extrinsic Safeguarding Mechanism Requirements for Trustworthy Physical AI Harris, M., Madden, D. Proceedings - 2025 IEEE 33rd International Requirements Engineering Conference Workshops, REW 2025, 2025 https://www.scopus.com/pages/publications/105020927532?origin=scopusAI

4. COMPREHENSIVE MULTI-ENVIRONMENT OPERATIONAL DESIGN DOMAIN TAXONOMY FOR INTELLIGENT SYSTEMS SAFETY DESIGN Al-Shareefy, H., Butler, M., Hoang, T.S. 68th Annual Meeting of the International Society for the Systems Sciences, ISSS 2024, 2024 https://www.scopus.com/pages/publications/105010328018?origin=scopusAI

5. From ConOps to an Operational Domain Model: Harnessing LLMs for Conceptual Model Design Gupta, S., Rezayat, S., Burmester, G., (...), Hartmann, S. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105020665791?origin=scopusAI

6. Explainable AI-driven predictive maintenance for mitigating process safety risks in safety-critical industrial equipment Bu Sinnah, Z.A. Journal of Loss Prevention in the Process Industries, 2026 https://www.scopus.com/pages/publications/105026655381?origin=scopusAI

7. Unsupervised learning Lynch, V., Gibson, M. Elgar Concise Encyclopedia of Artificial Intelligence and the Law, 2025 https://www.scopus.com/pages/publications/105032131137?origin=scopusAI

8. Neuro-Symbolic AI for Military Applications Hagos, D.H., Rawat, D.B. IEEE Transactions on Artificial Intelligence, 2024 https://www.scopus.com/pages/publications/85201789493?origin=scopusAI

9. From Black Box to Glass Box: A Model-Driven Engineering Approach for Explainable AI El Youssr, M.A., El Hamlaoui, M., Laghouaouta, Y. Lecture Notes in Networks and Systems, 2025 https://www.scopus.com/pages/publications/105015722092?origin=scopusAI

10. Designerly Understanding: Information Needs for Model Transparency to Support Design Ideation for AI- Powered User Experience Liao, Q.V., Subramonyam, H., Wang, J., Wortman Vaughan, J. Conference on Human Factors in Computing Systems - Proceedings, 2023 https://www.scopus.com/pages/publications/85160021489?origin=scopusAI

11. From Fault Tree Analysis to Runtime Model-Based Assurance Cases Nascimento, L., de Oliveira, A.L., Villela, R., (...), Kelly, T. Lecture Notes on Data Engineering and Communications Technologies, 2024 https://www.scopus.com/pages/publications/85191304239?origin=scopusAI

12. Can a Bayesian Oracle Prevent Harm from an Agent? Bengio, Y., Cohen, M.K., Malkin, N., (...), Kaddar, Y. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105014742006?origin=scopusAI

13. Statistical Analysis and Runtime Monitoring for an AI-based Autonomous Centerline Tracking System He, Y., Schumann, J. International Journal of Prognostics and Health Management, 2024 https://www.scopus.com/pages/publications/85207826528?origin=scopusAI

14. Using models at runtime to address assurance for self-adaptive systems Cheng, B.H.C., Eder, K.I., Gogolla, M., (...), Villegas, N.M. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2014 https://www.scopus.com/pages/publications/84904814843?origin=scopusAI

15. Application of Artificial Intelligence in Control Systems: Trends, Challenges, and Opportunities Fernández Mareco, E.R., Pinto-Roa, D. AI (Switzerland), 2025 https://www.scopus.com/pages/publications/105025646896?origin=scopusAI

16. Challenges of Machine Learning Applied to Safety-Critical Cyber-Physical Systems Pereira, A., Thomas, C. Machine Learning and Knowledge Extraction, 2020 https://www.scopus.com/pages/publications/85108664909?origin=scopusAI

17. The Road to Safe Automated Driving Systems: A Review of Methods Providing Safety Evidence Gyllenhammar, M., Rodrigues de Campos, G., Torngren, M. IEEE Transactions on Intelligent Transportation Systems, 2025 https://www.scopus.com/pages/publications/105001563064?origin=scopusAI

18. Autonomous AI torts: A comparative law and economics approach Kovac, M. Tort Liability and Autonomous Systems Accidents: Common and Civil Law Perspectives, 2023 https://www.scopus.com/pages/publications/85178971683?origin=scopusAI

19. Theoretical considerations in designing operator interfaces for automated systems Norman, S.D. Proceedings of SPIE - The International Society for Optical Engineering, 1987 https://www.scopus.com/pages/publications/0023564153?origin=scopusAI

20. Tumato 2.0 - a constraint-based planning approach for safe and robust robot behavior Vermaelen, J., Holvoet, T. Annals of Mathematics and Artificial Intelligence, 2025 https://www.scopus.com/pages/publications/85199608914?origin=scopusAI

21. Beyond Next-Token Prediction: A Standards-Aligned Survey of Autoregressive LLM Failure Modes, Deployment Patterns, and the Potential Role of World Models Ricciardi Celsi, L., McCann, J. Electronics (Switzerland), 2026 https://www.scopus.com/pages/publications/105032631355?origin=scopusAI

22. ISM, interoperable smart module in δ-Government facilities Liović, I. Proceedings of the 6th European Conference on Product and Process Modelling - eWork and eBusiness in Architecture, Engineering and Construction, ECPPM 2006, 2006 https://www.scopus.com/pages/publications/61849152970?origin=scopusAI

23. Swiss Cheese Model for AI Safety: A Taxonomy and Reference Architecture for Multi-Layered Guardrails of Foundation Model Based Agents Shamsujjoha, M., Lu, Q., Zhao, D., Zhu, L. Proceedings - 2025 IEEE 22nd International Conference on Software Architecture, ICSA 2025, 2025 https://www.scopus.com/pages/publications/105005025283?origin=scopusAI

24. Safety enforcement for the verification of autonomous systems De Niz, D., Andersson, B., Moreno, G. Proceedings of SPIE - The International Society for Optical Engineering, 2018 https://www.scopus.com/pages/publications/85050790755?origin=scopusAI

25. Systematic Selective Limits Application Using Decision-Making Engines to Enhance Safety in Highly Automated Vehicles Garikapati, D., Liu, Y., Huo, Z. SAE International Journal of Connected and Automated Vehicles, 2024 https://www.scopus.com/pages/publications/85201043909?origin=scopusAI

26. A Universal Framework for Generalized Run Time Assurance with JAX Automatic Differentiation Ravaioli, U.J., Dunlap, K., Hobbs, K. Proceedings of the American Control Conference, 2023 https://www.scopus.com/pages/publications/85167788232?origin=scopusAI

27. Neural Action Policy Safety Verification: Applicablity Filtering Vinzent, M., Hoffmann, J. Proceedings International Conference on Automated Planning and Scheduling, ICAPS, 2024 https://www.scopus.com/pages/publications/85195976605?origin=scopusAI

28. A comprehensive approach to safety for highly automated off-road machinery under Regulation 2023/1230 de Koning, M., Machado, T., Ahonen, A., (...), Ghabcheloo, R. Safety Science, 2024 https://www.scopus.com/pages/publications/85189083993?origin=scopusAI

29. Removing the Big Red Button: Uncrewed Ground Vehicles in Complex Military Environments Banks, A., Menon, P.P., Austen, S. Proceedings - 2024 IEEE 35th International Symposium on Software Reliability Engineering Workshops, ISSREW 2024, 2024 https://www.scopus.com/pages/publications/85215277759?origin=scopusAI

30. Defining an Initial Classification Scheme for Non-Deterministic AI Technologies Tejasen, K.T.J., Raju, P., Ryan, W., (...), Yang, R. Integrated Communications, Navigation and Surveillance Conference, ICNS, 2022 https://www.scopus.com/pages/publications/85130739750?origin=scopusAI

31. Design of flight guidance and control systems using explainable AI Sherry, L., Baldo, J., Berlin, B. Integrated Communications, Navigation and Surveillance Conference, ICNS, 2021 https://www.scopus.com/pages/publications/85107566625?origin=scopusAI

32. SAFEXPLAIN: a Complete Approach Towards Trustworthy AI-Based Safety-Critical Systems Abella, J., Agirre, I., Bui, T., (...), Dallara, V. Proceedings - 2025 28th Euromicro Conference on Digital System Design, DSD 2025, 2025 https://www.scopus.com/pages/publications/105030537985?origin=scopusAI

33. Approach for argumenting safety on basis of an operational design domain Weiss, G., Zeller, M., Schoenhaar, H., (...), Kreutz, A. Proceedings - 2024 IEEE/ACM 3rd International Conference on AI Engineering - Software Engineering for AI, CAIN 2024, 2024 https://www.scopus.com/pages/publications/85196532673?origin=scopusAI

34. Context-Aware Input Selection Using Operational Design Domain Torens, C., Schirmer, S., Durak, U. AIAA Science and Technology Forum and Exposition, AIAA SciTech Forum 2026, 2026 https://www.scopus.com/pages/publications/105030414140?origin=scopusAI

35. A Modeling Framework for Hardware-Software Systems with Machine Learning Components Bedini, F., Jungebloud, T., Maschotta, R., Zimmermann, A. Communications in Computer and Information Science, 2026 https://www.scopus.com/pages/publications/105017374571?origin=scopusAI

36. Operational Design Domain Monitoring with Uncertain Measurements Charmet, T., Cherfaoui, V., Ibanez- Guzman, J., Armand, A. IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC, 2024 https://www.scopus.com/pages/publications/105001673329?origin=scopusAI

37. Towards the Monitoring of Operational Design Domains Using Temporal Scene Analysis in the Realm of Artificial Intelligence in Aviation Girija, A.A., Christensen, J.M., Stefani, T., (...), Krüger, T. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2024 https://www.scopus.com/pages/publications/85211250339?origin=scopusAI

38. Automated Scenario Generation to Maximize Coverage of an Operational Design Domain for an AI-based Aviation Systems Gupta, S., Kountchou, L.V.K., Mbouendeu, M.N., Durak, U. AIAA Science and Technology Forum and Exposition, AIAA SciTech Forum 2026, 2026 https://www.scopus.com/pages/publications/105030414309?origin=scopusAI

39. ODD-Based Long-Term Decision-Making for Intelligent Vehicles Cardenas, R., Adouane, L., Zinoune, C., Benloucif, M.A. IEEE Intelligent Vehicles Symposium, Proceedings, 2025 https://www.scopus.com/pages/publications/105014238593?origin=scopusAI

40. Context-Aware and Reliable Long-Term Decision-Making for Safe Intelligent Vehicles: A Survey Cardenas, R., Adouane, L., Zinoune, C., Benloucif, M.-A. IEEE Transactions on Intelligent Vehicles, 2025 https://www.scopus.com/pages/publications/105008452726?origin=scopusAI

41. Building Robust Artificial Intelligence Through Multi-Agent Debate Bauschard, S. AI Pluralism: Fostering Diversity and Dialogue in Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105032894204?origin=scopusAI

42. New Contribution to the Analysis and Evaluation of Safety Architectures: Scientific Investigation of a Safety Architecture Krini, O. New Contribution to the Analysis and Evaluation of Safety Architectures: Scientific Investigation of a Safety Architecture, 2025 https://www.scopus.com/pages/publications/105005676009?origin=scopusAI

43. Safety-Centric Architecture for AI-Enabled Autonomous Driving Systems Arora, J., Esper, A., Santos, V. IEEE/IFIP International Conference on Dependable Systems and Networks Workshops, DSN-W, 2025 https://www.scopus.com/pages/publications/105029832334?origin=scopusAI

44. Safety-Assured Design and Adaptation of Learning-Enabled Autonomous Systems Zhu, Q., Huang, C., Jiao, R., (...), Xu, S. Proceedings of the Asia and South Pacific Design Automation Conference, ASP-DAC, 2021 https://www.scopus.com/pages/publications/85100524891?origin=scopusAI

45. On Architectural Tactics for Resource-Constrained and Safety-Critical AI-Based Systems Straub, P., Decker, C., Kuhrmann, M. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105016669324?origin=scopusAI

46. On the interpretability of machine learning methods in crash frequency modeling and crash modification factor development Wen, X., Xie, Y., Jiang, L., (...), Ge, T. Accident Analysis and Prevention, 2022 https://www.scopus.com/pages/publications/85124910019?origin=scopusAI

47. Taxonomy of Machine Learning Safety: A Survey and Primer Mohseni, S., Wang, H., Xiao, C., (...), Yadawa, J. ACM Computing Surveys, 2022 https://www.scopus.com/pages/publications/85177739654?origin=scopusAI

48. Explainable Deep Fuzzy Systems Applied to Sulfur Recovery Unit Júnior, J.S.S., Mendes, J., Souza, F., Premebida, C. Studies in Big Data, 2024 https://www.scopus.com/pages/publications/85204960527?origin=scopusAI

49. AI-Driven Predictive Safety Analytics for Accident Prevention in Smart Manufacturing Leong, W.Y. Advances in Transdisciplinary Engineering, 2026 https://www.scopus.com/pages/publications/105035198829?origin=scopusAI

50. A hybrid system based on FMM and MLP to diagnose heart disease Aggarwal, S., Azad, V. Fuzzy Systems: Concepts, Methodologies, Tools, and Applications, 2017 https://www.scopus.com/pages/publications/85021345595?origin=scopusAI

51. A Hybrid System Based on FMM and MLP to Diagnose Heart Disease Aggarwal, S., Azad, V. Fuzzy Systems: Concepts, Methodologies, Tools, and Applications, 2017 https://www.scopus.com/pages/publications/105012496844?origin=scopusAI

52. Revisiting Unsupervised Temporal Action Localization: The Primacy of High-Quality Actionness and Pseudolabels Jiang, H., Tang, H., Yan, M., (...), Nie, L. MM 2024 - Proceedings of the 32nd ACM International Conference on Multimedia, 2024 https://www.scopus.com/pages/publications/85206106715?origin=scopusAI

53. Environmental Learning for Autonomous Navigation Kumar, S., Goyal, S.B. Advances in Autonomous Navigation through Intelligent Technologies, 2025 https://www.scopus.com/pages/publications/105001753699?origin=scopusAI

54. Enhancing aviation safety with artificial intelligence: A systematic literature review on recent advances, challenges and future perspectives Yiu, C.Y., Li, W.-C., Ng, K.K.H., (...), Schiefele, J. Advanced Engineering Informatics, 2026 https://www.scopus.com/pages/publications/105028438522?origin=scopusAI

55. Emerging artificial intelligence and machine learning paradigms in environmental pollution control and abatement Aravind, J., Nouri, J., Tehrani, S.M. Global Journal of Environmental Science and Management, 2026 https://www.scopus.com/pages/publications/105034508379?origin=scopusAI

56. Artificial Intelligence Algorithms for Space Missions Intelisano, A. Springer Optimization and Its Applications, 2025 https://www.scopus.com/pages/publications/105013107991?origin=scopusAI

57. A Case Study on Defining Traceable Machine Learning Safety Requirements for an Automotive Perception Component Shahbeigi, S., Hawkins, R., Burton, S., (...), Habli, I. Proceedings - 2025 IEEE 36th International Symposium on Software Reliability Engineering Workshops, ISSREW 2025, 2025 https://www.scopus.com/pages/publications/105030542348?origin=scopusAI

58. On the Necessity of Explicit Artifact Links in Safety Assurance Cases for Machine Learning Gauerhof, L., Gansch, R., Heinzemann, C., (...), Heyl, A. Proceedings - 2021 IEEE International Symposium on Software Reliability Engineering Workshops, ISSREW 2021, 2021 https://www.scopus.com/pages/publications/85126975972?origin=scopusAI

59. Towards a Standardized Interactive AI Transparency Label Goram, M. Lecture Notes in Networks and Systems, 2025 https://www.scopus.com/pages/publications/105021001456?origin=scopusAI

60. Trustworthy AI in Design: Introducing Explainable Agent Systems Ribeiro, E., Pinto, T., Reis, A., Barroso, J. Communications in Computer and Information Science, 2026 https://www.scopus.com/pages/publications/105029079158?origin=scopusAI

61. The Effect of Progressive Disclosure in the Transparency of Large Language Models Muralidhar, D., Belloum, R., de Oliveira, K.M., (...), Mohammad, P.B. Communications in Computer and Information Science, 2025 https://www.scopus.com/pages/publications/105000694717?origin=scopusAI

62. One Explanation Does Not Fit All: The Promise of Interactive Explanations for Machine Learning Transparency Sokol, K., Flach, P. KI - Kunstliche Intelligenz, 2020 https://www.scopus.com/pages/publications/85088051328?origin=scopusAI

63. An Optimization and Validation Method to Detect the Collision Scenarios and Identifying the Safety Specification of Highly Automated Driving Vehicle Khatun, M., Caldeira, G.B., Jung, R., Glab, M. International Conference on Control, Automation and Systems, 2021 https://www.scopus.com/pages/publications/85124244041?origin=scopusAI

64. Medium-Fidelity Evaluation and Modeling for Perception Systems of Intelligent and Connected Vehicles Sun, C., Cui, Y., Dao, N.-D., (...), Khajepour, A. IEEE Transactions on Intelligent Vehicles, 2024 https://www.scopus.com/pages/publications/85171740526?origin=scopusAI

65. ODD and Behavior Based Scenario Generation for Automated Driving Systems Zhang, X., Khastgir, S., Tiele, J.-K., (...), Jennings, P. IEEE Access, 2024 https://www.scopus.com/pages/publications/85182362123?origin=scopusAI

66. Knowledge-Based Approach to Generate Scenarios for Testing Highly Automated On-Sight Train Operations Greiner-Fuchs, L., Cichon, M. International Conference on Vehicle Technology and Intelligent Transport Systems, VEHITS - Proceedings, 2024 https://www.scopus.com/pages/publications/85194036396?origin=scopusAI

67. Virtual Railway Scenario: Testing Automated on-Sight Train Operation Greiner-Fuchs, L., Feldhoff, J., Schäfer, S., (...), Cichon, M. IAVVC 2025 - IEEE International Automated Vehicle Validation Conference, Proceedings, 2025 https://www.scopus.com/pages/publications/105025135767?origin=scopusAI

68. Error-Driven Design of AI-based Systems for Airborne Applications Sprockhoff, J., Ahlbrecht, A., Gupta, S., (...), Pham, T.T. AIAA Science and Technology Forum and Exposition, AIAA SciTech Forum 2025, 2025 https://www.scopus.com/pages/publications/105001282375?origin=scopusAI

69. A Review on AI Miniaturization: Trends and Challenges Tang, B., Du, S., Smith, A.J. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105020245724?origin=scopusAI

70. Explainable Artificial Intelligence for Identification of Human Errors in Nuclear Power Plants Kotla, B.R., Gursel, E., Daniels, K., (...), Madadi, M. Proceedings of 13th Nuclear Plant Instrumentation, Control and Human-Machine Interface Technologies, NPIC and HMIT 2023, 2023 https://www.scopus.com/pages/publications/85183313693?origin=scopusAI

71. Runtime Instrumentation for Reactive Components Aceto, L., Attard, D.P., Francalanza, A., Ingólfsdóttir, A. Leibniz International Proceedings in Informatics, LIPIcs, 2024 https://www.scopus.com/pages/publications/85203493749?origin=scopusAI
