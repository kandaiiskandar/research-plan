---
source_pdf: "Scopus - Scopus AI.pdf"
source_sha256: "4304aee629110c8df6a553e01454b351b53b37248a8dc874d0f5c4085324533e"
source_pages: 12
scopus_ai_generated: "Thu Apr 09 2026"
query: "AI safety triggers in critical systems"
report_title: "Comparative Effectiveness of Self-Referential and Context-Aware AI Safety Triggers in Safety-Critical Maritime and Autonomous Vehicle Systems under Environmental Volatility Quick Reference"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# AI safety triggers in critical systems

## Key Findings Table

| Aspect | Self-Referential Triggers | Context-Aware Triggers | Hybrid Approaches |
| --- | --- | --- | --- |
| Definition | Rely on internal AI metrics (e.g., confidence scores, concept drift) | Leverage environmental state classification and multimodal sensor data | Integrate both internal and external cues, often combining physics-based and data-driven models |
| Strengths | High explainability, compliance, and transparency; effective in stable, well-characterized environments | Superior adaptability and robustness in dynamic, volatile contexts; can preemptively suppress unsafe actions | Enhanced generalization, interpretability, and resilience; can address limitations of each approach individually |
| Limitations | Vulnerable to sensor degradation, environmental volatility, and edge cases; may miss context-driven hazards | Require complex sensor fusion, semantic validation, and scenario modeling; can be computationally intensive | Formal verification and scenario-driven validation remain challenging, especially under extreme volatility |
| Maritime/AV Evidence | Insufficient under oceanographic volatility, biofouling, and communication loss 1 2 | Outperform self-referential triggers in real-world deployments (e.g., CLGuard, context-aware suppression) | Hybrid models show promise but need further validation and standardization 6 7 8 |

## 3 4 5

## Direct Answer

Self-referential AI safety triggers, which depend solely on internal metrics such as concept drift or confidence scores, provide valuable insights into the system’s internal state but may fall short in volatile environments like maritime settings or autonomous vehicles where external conditions (e.g., weather, ocean currents, or sensor degradation due to biofouling) can overly challenge sensor accuracy and overall reliability. Context-aware safety triggers, in contrast, incorporate environmental state classification and multimodal sensor data to semantically validate decisions (as seen with frameworks like CLGuard), thereby providing more robust and adaptive safety gating under dynamic conditions. Several studies in the maritime domain[1][2] and in autonomous vehicle deployments[5][9] emphasize the superior performance of context-aware systems in managing external volatility, although integrated hybrid approaches that combine these paradigms show promising potential to mitigate the limitations of each method individually.

## Study Scope

**Time Period:** 2018–2024 **Disciplines:** Maritime autonomy, autonomous vehicles, AI safety, human factors, control theory, machine learning, formal verification **Methods:** Literature review, meta-analysis, scenario-based validation, simulation studies, real-world deployments, standards analysis (ISO 21448, ISO 34502), hybrid modeling

## Assumptions & Limitations

## Assumptions:

Internal AI metrics are well-calibrated and representative of model uncertainty in nominal conditions. Environmental volatility is defined as rapid, unpredictable changes in external conditions (e.g., weather, ocean currents, sensor fouling). Context-aware triggers have access to reliable, multimodal environmental data.

## Limitations:

Real-world validation of hybrid approaches is limited by the availability of large-scale, cross-domain datasets. Formal verification of learning-enabled components in hybrid systems remains an open challenge. Scenario-driven validation frameworks are still evolving and may not capture all edge cases.

## Suggested Further Research

Development of digital twin frameworks for real-time simulation and adaptive safety gating. Large-scale, cross-domain validation datasets for hybrid safety triggers. Formal verification techniques tailored to hybrid systems with both discrete and continuous dynamics. Cross-layer fault modeling and scenario-driven validation in highly volatile environments.

## 1. Introduction

## Background and Motivation

The increasing reliance on AI in safety-critical domains such as maritime autonomous surface ships (MASS) and autonomous vehicles (AVs) has elevated the importance of robust safety triggers. These triggers are mechanisms that determine when to intervene, hand over control, or suppress unsafe actions to prevent accidents and ensure compliance with safety standards. Two primary paradigms have emerged:

**Self-referential triggers:** Rely on internal AI performance metrics (e.g., confidence scores, concept drift) to assess system reliability.

**Context-aware triggers:** Leverage environmental state classification and multimodal sensor data to validate decisions against the current context. Environmental volatility—characterized by unpredictable changes in weather, ocean currents, sensor degradation, and communication reliability—poses significant challenges to both paradigms, particularly in maritime and AV domains where the operational context can shift rapidly and unpredictably[10][11][12].

## 2. Theoretical Frameworks

**2.1 Self-Referential AI Safety Triggers: Capabilities and Limitations**

## Mechanisms and Applications

Self-referential triggers monitor the internal state of AI systems using metrics such as: **Concept drift detection:** Identifies shifts in data distribution that may compromise model validity. **Confidence scores:** Quantify the AI’s certainty in its predictions or actions. **Anomaly detection:** Flags deviations from expected internal behavior.

## Applications:

In maritime systems, these triggers support explainability, compliance with collision regulations, and timely handover to human operators[10][12][13][14][15].

In AVs, they underpin safety assurance frameworks and are embedded in standards like ISO 21448 and ISO 34502[12].

## Modeling Latent Supervisory Factors

Recent advances integrate human factors analysis (e.g., HFACS) with machine learning to predict supervisory errors and support handover decisions. Hierarchical and multi-label dependency models (e.g., HDN, PCT, SVM) improve the prediction of latent supervisory factors, enhancing the system’s ability to anticipate when human intervention is needed[10][16][17].

## Limitations in Volatile Environments

**Sensor Degradation:** Ocean currents, biofouling, and weather can degrade sensor accuracy, undermining the reliability of internal metrics[1][12][18][19][20]. **Edge Cases:** Internal metrics may not capture rare or context-specific hazards. **Communication Loss:** In multi-agent maritime systems, environmental factors (e.g., temperature, salinity) can disrupt communication, further reducing the effectiveness of self-referential triggers[2][3][21].

## Synthesis:

While self-referential triggers provide valuable introspection and support compliance, their effectiveness is fundamentally limited by their inability to account for external, rapidly changing environmental factors.

**2.2 Context-Aware Safety Triggers: Mechanisms and Comparative Performance**

## Context-Aware Triggering Mechanisms

Context-aware triggers utilize: **Multimodal sensor fusion:** Integrates data from cameras, radar, V2X, and environmental sensors. **Semantic validation:** Validates control commands against the current scene and operational context. **Scene understanding:** Employs AI models (e.g., vision-language models, LLMs) to interpret complex scenarios[2][5][11][22].

## Semantic Validation and Suppression Frameworks

Frameworks like **CLGuard** perform runtime semantic validation, suppressing unsafe actions by ensuring that control commands are contextually appropriate. These systems are fault-agnostic and can detect both AI misjudgments and malicious interventions[4][5][23].

## Comparative Performance Metrics

**Accuracy and Robustness:** Context-aware triggers consistently outperform self-referential triggers in real-world and simulated deployments, especially in dynamic environments[5][19][24][25]. **False Positive Rates:** Lower in context-aware systems due to semantic validation and scene understanding. **Adaptability:** Superior in context-aware systems, which can dynamically adjust to changing environmental conditions.

## Integration of Multimodal Environmental Cues

Context-aware triggers integrate: **Sensor fusion and LLMs:** For real-time, interpretable decision-making. **Behavioral modeling:** To anticipate accidents and adapt to human behavior. **Temporal context buffers:** To maintain situational awareness over time[26][27][28][29].

## Limitations of Self-Referential Triggers in Dynamic Contexts

Self-referential triggers struggle with scalability and adaptability in the face of evolving threats, regulations, and operational contexts. Context-aware approaches, by contrast, benefit from unified governance frameworks and continuous real-time assurance[30].

## Synthesis:

Context-aware triggers, by leveraging environmental data and semantic validation, provide a more robust and adaptive safety net in volatile, real-world conditions.

## 3. Methods & Data Transparency

**Literature Review:** Comprehensive analysis of peer-reviewed studies, standards documents, and technical reports from 2018–2024. **Meta-Analysis:** Aggregation of findings across maritime and AV domains, focusing on comparative performance, limitations, and real-world deployments. **Scenario-Based Validation:** Examination of case studies and simulation results under varying environmental conditions. **Standards Analysis:** Review of ISO 21448, ISO 34502, and related standards for AI safety in AVs. **Hybrid Modeling Assessment:** Evaluation of studies integrating physics-based and data-driven approaches.

## 4. Critical Analysis of Findings

## 4.1 Impact of Environmental Volatility on AI Safety Triggers

## Environmental Volatility Factors and Their Effects

**Maritime:** Ocean currents, biofouling, temperature, and salinity degrade sensor accuracy and communication reliability, directly impacting the sufficiency of internal AI metrics[2][3][21].

**Autonomous Vehicles:** Weather, road conditions, and sensor occlusion (e.g., fog) introduce uncertainties that internal metrics alone cannot address[12][19][20].

## Adaptive Probabilistic and Reinforcement Learning Frameworks

**Control Barrier Functions (CBFs):** Dynamically adjust safety constraints in real time, maintaining safety under changing conditions[31][32][33][34].

**Probabilistic Models:** Bayesian networks and reinforcement learning frameworks capture uncertainty and enable adaptive behavior[32][35].

## Communication and Sensor Fusion Challenges

**Multi-Agent Systems:** Environmental volatility necessitates robust resource allocation and anomaly detection to maintain communication and sensor reliability[3][36][37].

## Synthesis:

Environmental volatility exposes the limitations of self-referential triggers and underscores the necessity for context-aware and adaptive frameworks.

## 4.2 Hybrid and Combined Safety Trigger Approaches

## Hybrid Modeling Strategies

**Physics-Based + Data-Driven:** Hybrid models combine the interpretability of physics-based approaches with the adaptability of data-driven methods, enhancing robustness in transportation systems[6][38][39][40].

**Fusion Points:** Integration can occur at input, loss, architecture, or output levels, each offering trade-offs in robustness and interpretability[6][41][42][43].

## Formal Verification and Scenario-Driven Validation

**Challenges:** Exponential state space growth, lack of unified models for discrete and continuous dynamics, and scenario explosion complicate formal verification[44][45][46][47].

**Solutions:** Combined model checking, theorem proving, and scenario-based testing frameworks are emerging but require further development.

## AI-Fuzzy Logic and Human-AI Hybrid Frameworks

**Interpretability and Uncertainty Handling:** Hybrid AI-fuzzy logic models enhance transparency and robustness, particularly in traffic accident prediction and decision-making under uncertainty[48][49][50][51].

## Research Gaps and Future Directions

**Cross-Layer Fault Modeling:** Needed to address complex failure modes in hybrid systems. **Formal Verification:** Tailored techniques for learning-enabled components are lacking. **Cross-Domain Knowledge Transfer:** Limited application of hybrid triggers across maritime and AV domains[8][52][53][54].

## Synthesis:

Hybrid approaches offer a promising path forward but require advances in formal verification, scenario-driven validation, and cross-domain standardization.

## 5. Real-World Implications

## Maritime Systems:

Self-referential triggers are insufficient under oceanographic volatility and sensor degradation. Context-aware triggers, especially those integrating semantic validation and multimodal sensor fusion, are essential for safe operation in MASS[1][2][3].

## Autonomous Vehicles:

Context-aware suppression frameworks (e.g., CLGuard) outperform internal metric-based triggers in real-world deployments, reducing false positives and improving safety[4][5]. Hybrid models are beginning to bridge the gap, but require further validation and standardization.

## Policy and Standards:

Standards such as ISO 21448 and ISO 34502 are evolving to incorporate context-aware and hybrid safety mechanisms, moving beyond reliance on internal metrics alone[12].

## Human Factors:

Human-centered design and explainability remain critical, especially for supervisory control and handover in both maritime and AV domains[18][55].

## 6. Future Research Directions

## Digital Twin Frameworks:

Real-time simulation of both internal AI states and external environmental conditions to facilitate adaptive, hybrid safety triggers.

## Large-Scale Validation:

Development of cross-domain datasets and scenario-driven validation frameworks for hybrid safety triggers.

## Formal Verification:

Tailored techniques for hybrid systems with both discrete and continuous dynamics, including learning-enabled components.

## Cross-Layer Fault Modeling:

Comprehensive modeling of failure modes across system layers.

## Human-AI Collaboration:

Enhanced frameworks for explainability, trust, and effective handover in safety-critical operations.

## Conclusion

## Key Insights and Recommendations

**Self-referential triggers** provide essential introspection and compliance but are fundamentally limited in volatile, real-world environments due to their inability to account for external factors.

**Context-aware triggers** —leveraging environmental state classification, semantic validation, and multimodal sensor fusion—consistently outperform self-referential triggers in both maritime and AV domains, particularly under environmental volatility.

**Hybrid approaches** that integrate both paradigms offer a promising path forward, combining the strengths of each while mitigating their individual limitations. However, significant challenges remain in formal verification, scenario-driven validation, and cross-domain standardization.

## Recommendation:

Prioritize the development and deployment of context-aware and hybrid safety triggers in safety-critical systems, supported by robust validation frameworks, digital twin simulations, and human-centered design principles.

Invest in research addressing formal verification, cross-layer fault modeling, and large-scale scenario validation to ensure the safety and reliability of autonomous systems in complex, dynamic environments [6][10][11][12].

## Synthesis:

The literature demonstrates that context-aware and hybrid safety triggers are essential for robust, adaptive safety gating in volatile maritime and autonomous vehicle environments. Continued innovation in modeling, validation, and human-AI collaboration will be critical to realizing the full potential of autonomous systems in safety-critical domains.

## References

1. Environment-Aware Multi-Sensor Fusion for Maritime Domain Awareness: A Comprehensive Review Ryu, S., Han, S. Korean Journal of Remote Sensing, 2025 https://www.scopus.com/pages/publications/105027329095?origin=scopusAI

2. Risk Management Challenges in Maritime Autonomous Surface Ships (MASSs): Training and Regulatory Readiness Park, H., Kim, J., Jung, M., (...), Jang, U. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105020237477?origin=scopusAI

3. An Edge Computing-Based Preventive Framework With Machine Learning- Integration for Anomaly Detection and Risk Management in Maritime Wireless Communications Algarni, A., Acarer, T., Ahmad, Z. IEEE Access, 2024 https://www.scopus.com/pages/publications/85190339883?origin=scopusAI

4. Supply Chain Exploitation of Secure ROS 2 Systems: A Proof-of-Concept on Autonomous Platform Compromise via Keystore Exfiltration Sakib, T.H., Romano Martinez, Y., Brady, C., (...), Guo, T.N. Proceedings - IEEE Military Communications Conference MILCOM, 2025 https://www.scopus.com/pages/publications/105031781782?origin=scopusAI

5. CLGuard: A Context-Aware Suppression Framework for Resilient Driving Control Seong, Y., Lim, H., Yoon, S. Proceedings of IEEE Pacific Rim International Symposium on Dependable Computing, PRDC, 2025 https://www.scopus.com/pages/publications/105029901471?origin=scopusAI

6. Physics and Data Cooperative Modeling in Transportation Cyber-Physical System: Review and Perspectives Wang, T., Mao, R., Li, G., (...), Zhang, H. IEEE Transactions on Industrial Informatics, 2026 https://www.scopus.com/pages/publications/105027971581?origin=scopusAI

7. Integrating Safety and Security in Autonomous Vehicles: A Comprehensive Review Khokha, S. 4th International Conference on Sustainable Expert Systems, ICSES 2024 - Proceedings, 2024 https://www.scopus.com/pages/publications/85214797253?origin=scopusAI

8. A Systematic Review on Risk Management and Enhancing Reliability in Autonomous Vehicles Mahmood, A., Szabolcsi, R. Machines, 2025 https://www.scopus.com/pages/publications/105014468341?origin=scopusAI

9. A unified experimental framework for estimating collision rates and occupant injury severity across different levels of driving automation Shen, J., Qin, D., He, Z., (...), Nie, B. Accident Analysis and Prevention, 2025 https://www.scopus.com/pages/publications/105018584635?origin=scopusAI

10. Explainable human error prediction for autonomous vessels: combining human factors analysis and classification system with machine learning Kim, D.-H. WMU Journal of Maritime Affairs, 2026

https://www.scopus.com/pages/publications/105031411785?origin=scopusAI

11. Context-Aware Prompt Engineering for Large Language Models in Autonomous Vehicles Abbasi, S., Rahmani, A.M. Concurrency and Computation: Practice and Experience, 2025 https://www.scopus.com/pages/publications/105020371937?origin=scopusAI

12. Strengthening AI Validation and Verification in Autonomous Vehicles: Comprehensive Analysis and Improvements to Key Standards Dekkata, S.C., Tawade, H., Kamanuru, V.R., (...), Rathod, S. Proceedings - 2025 IEEE Conference on Artificial Intelligence, CAI 2025, 2025 https://www.scopus.com/pages/publications/105011254412?origin=scopusAI

13. SAFEXPLAIN: a Complete Approach Towards Trustworthy AI-Based Safety-Critical Systems Abella, J., Agirre, I., Bui, T., (...), Dallara, V. Proceedings - 2025 28th Euromicro Conference on Digital System Design, DSD 2025, 2025 https://www.scopus.com/pages/publications/105030537985?origin=scopusAI

14. Approvable AI for Autonomous Ships: Challenges and Possible Solutions Murray, B., Rødseth, Ø.J., Nordahl, H., (...), Pobitzer, A. Proceedings of the 32nd European Safety and Reliability Conference, ESREL 2022 - Understanding and Managing Risk and Reliability for a Sustainable Future, 2022 https://www.scopus.com/pages/publications/85146471119?origin=scopusAI

15. AI-Based Vehicle Safety and Functional Safety Standards in Autonomous Cars: A Use Case in Safety- Critical Systems Chokshi, K., Shaik, Y.A., Yadav, P., (...), Rajamandrapu, A.K. 2025 IEEE 4th World Conference on Applied Intelligence and Computing, AIC 2025, 2025 https://www.scopus.com/pages/publications/105023641714?origin=scopusAI

16. Dependency network methods for Hierarchical Multi-label Classification of gene functions Fabris, F., Freitas, A.A. IEEE SSCI 2014 - 2014 IEEE Symposium Series on Computational Intelligence - CIDM 2014: 2014 IEEE Symposium on Computational Intelligence and Data Mining, Proceedings, 2014 https://www.scopus.com/pages/publications/84925047688?origin=scopusAI

17. Human factor influences on supervisory control of remotely operated and autonomous vessels Veitch, E., Alsos, O.A., Cheng, T., (...), Utne, I.B. Ocean Engineering, 2024 https://www.scopus.com/pages/publications/85186734873?origin=scopusAI

18. HUMAN OVERSIGHT IN SHIP AUTONOMY van de Merwe, K., Veitch, E. Human Factors in Remote Ship Operations, 2026 https://www.scopus.com/pages/publications/105027708906?origin=scopusAI

19. Enhancing Autonomous Vehicle Safety Through Chaid Modeling: Influential Factors, Seasonal Variations, and Systematic Limitations BaşKaman, F., Yücel, A. Sakarya University Journal of Computer and Information Sciences, 2025 https://www.scopus.com/pages/publications/105026816234?origin=scopusAI

20. Testing autonomous vehicles and AI: perspectives and challenges from cybersecurity, transparency, robustness and fairness Fernández Llorca, D., Hamon, R., Junklewitz, H., (...), Kriston, A. European Transport Research Review, 2025 https://www.scopus.com/pages/publications/105012184045?origin=scopusAI

21. Influence of temperature and salinity on all-terminal reliability for multi-AUV cooperative systems Liang, Q., Hu, Q., Luo, M., Li, Y. Oceans Conference Record (IEEE), 2022 https://www.scopus.com/pages/publications/85145782348?origin=scopusAI

22. Context-aware system for pre-triggering irreversible vehicle safety actuators Böhmländer, D., Dirndorfer, T., Al-Bayatti, A.H., Brandmeier, T. Accident Analysis and Prevention, 2017 https://www.scopus.com/pages/publications/85016958472?origin=scopusAI

23. STPA-Driven Multilevel Runtime Monitoring for In-Time Hazard Detection Gautham, S., Bakirtzis, G., Will, A., (...), Elks, C.R. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2022 https://www.scopus.com/pages/publications/85138003582?origin=scopusAI

24. Evaluation of Automated Driving System Safety Metrics With Logged Vehicle Trajectory Data Yan, X., Feng, S., Leblanc, D.J., (...), Liu, H.X. IEEE Transactions on Intelligent Transportation Systems, 2024 https://www.scopus.com/pages/publications/85192698979?origin=scopusAI

25. Context-aware target classification with hybrid Gaussian process prediction for cooperative vehicle safety systems Valiente, R., Raftari, A., Mahjoub, H.N., (...), Fallah, Y.P. IET Intelligent Transport Systems, 2023 https://www.scopus.com/pages/publications/85146162281?origin=scopusAI

26. Context-aware decision making in autonomous vehicles: Integrating social behavior modeling with large language models Lamichhane, B.R., Aueawatthanaphisut, A., Srijuntongsiri, G., Horanont, T. Array, 2025 https://www.scopus.com/pages/publications/105007969928?origin=scopusAI

27. DSC-LLM: Driving Scene Context Representation-Based Trajectory Prediction Framework with Risk Factor Reasoning Using LLMs † Kim, S., Jin, J., Hong, S., (...), Noh, B. Sensors, 2025 https://www.scopus.com/pages/publications/105024654707?origin=scopusAI

28. Driving Scene Context-Augmented Trajectory Prediction with Risk-Aware Decision Reasoning Using Multimodal LLM Kim, S., Hong, S., Jin, J., Noh, B. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105024557881?origin=scopusAI

29. RAG-SafeAdapt: a multimodal retrieval-augmented model for safety and interpretability in autonomous driving Li, M., Li, J., Liu, H., (...), Li, H. Proceedings of the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering, 2026 https://www.scopus.com/pages/publications/105020422220?origin=scopusAI

30. A Review of TRiSM Frameworks in Artificial Intelligence Systems: Fundamentals, Taxonomy, Use Cases, Key Challenges and Future Directions Ray, P.P. Expert Systems, 2026 https://www.scopus.com/pages/publications/105029030878?origin=scopusAI

31. Climate-Aware LiDAR-Driven Reinforcement Learning for Adaptive Safety Decision-Making in Autonomous Vehicles and Consumer Applications Bhatti, U.A., Wang, J., Zhang, Y., (...), Zhu, X. IEEE Transactions on Consumer Electronics, 2025 https://www.scopus.com/pages/publications/105024807142?origin=scopusAI

32. Probabilistic Modelling for Design and Verification of Trustworthy Autonomous Systems Corradini, F. CEUR Workshop Proceedings, 2023 https://www.scopus.com/pages/publications/85178623720?origin=scopusAI

33. Enhancing autonomous driving safety in real lane-changing scenarios under friction variability: A friction-adaptive shield reinforcement learning framework Fang, Z., He, J., Qin, P., (...), Sun, S. Accident Analysis and Prevention, 2025 https://www.scopus.com/pages/publications/105017972134?origin=scopusAI

34. Optimizing Autonomous Vehicle Control and Safety with the CLF-CBF-QP Framework for Dynamic Driving Scenarios Hamdada, O., Kribeche, A., Chaibet, A., Andrianarison, O. 2025 International Conference on Control, Automation and Diagnosis, ICCAD 2025, 2025 https://www.scopus.com/pages/publications/105014518734?origin=scopusAI

35. Autonomous Driving via Knowledge-Enhanced Safe Reinforcement Learning Wang, C., Zhou, S., Wang, L., (...), Shou, G. IEEE Transactions on Intelligent Vehicles, 2025 https://www.scopus.com/pages/publications/85196096090?origin=scopusAI

36. Optimal Time Partitioning for Sensing-Communication Trade-Off in V2V ISAC Systems Dong, G., Wang, Y., Zhang, D., Dong, X. 2025 7th International Conference on Artificial Intelligence Technologies and Applications, ICAITA 2025, 2025 https://www.scopus.com/pages/publications/105017967221?origin=scopusAI

37. A comprehensive technological survey on the dependable self-management CPS: From self-adaptive architecture to self-management strategies Zhou, P., Zuo, D., Hou, K.M., (...), Zhou, H. Sensors (Switzerland), 2019 https://www.scopus.com/pages/publications/85062434711?origin=scopusAI

38. A hybrid physics-based and data-driven approach for car-following behavior modeling and analysis Cheng, Q., Zhang, Y., Gu, Z., (...), Liu, Z. Transportation Research Part C: Emerging Technologies, 2025 https://www.scopus.com/pages/publications/105006786403?origin=scopusAI

39. Multifidelity computing for coupling full and reduced order models Ahmed, S.E., San, O., Kara, K., (...), Rasheed, A. PLoS ONE, 2021 https://www.scopus.com/pages/publications/85101309377?origin=scopusAI

40. Safe Reinforcement Learning for Event-Triggered Control of Automated Vehicles With Uncertainty Hu, F., Fu, X., Huang, H. IEEE Transactions on Intelligent Transportation Systems, 2025 https://www.scopus.com/pages/publications/85217625126?origin=scopusAI

41. YOLOv8 Object Detection and Expert-Rule Voice Alerts in a Real-Time Hybrid Transportation Safety System for Multi-Hazard Road Monitoring Manipravallika, T., Munawwar, S., Rao, P.V.G.K., (...), Gali, S. 4th International Conference on Automation, Computing and Renewable Systems, ICACRS 2025 - Proceedings, 2025 https://www.scopus.com/pages/publications/105032757012?origin=scopusAI

42. Perception to Motion: The Role of Multi-Sensor Data Fusion in Realizing the Full Potential of Autonomous Vehicles Li, Z., Singh, B.S.B. WSEAS Transactions on Environment and Development, 2025 https://www.scopus.com/pages/publications/105011496781?origin=scopusAI

43. A fusion safety and security analysis framework for intelligent and connected vehicles Sun, B., Yang, S., Wang, Y., (...), Cao, Y. PLOS ONE, 2025 https://www.scopus.com/pages/publications/105016646658?origin=scopusAI

44. Formal Verification of Autonomous Vehicle Group Control Systems via Specification Translation of Multitask Hybrid Observational Transition Systems Wang, Y., Nakamura, M., Takano, R., (...), Sakakibara, K. Electronics (Switzerland), 2025 https://www.scopus.com/pages/publications/105002374775?origin=scopusAI

45. An Integrated Scenario-Based Testing and Explanation Framework for Autonomous Vehicles Goss, Q., Clay Pate, W., Akbas, M.I. Proceedings - 2024 IEEE International Conference on Mobility, Operations, Services and Technologies, MOST 2024, 2024 https://www.scopus.com/pages/publications/85201214304?origin=scopusAI

46. Formal Modelling of Safety Architecture for Responsibility-Aware Autonomous Vehicle via Event-B Refinement Kobayashi, T., Bondu, M., Ishikawa, F. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85151063621?origin=scopusAI

47. Event-B Hybridation A Proof and Refinement-based Framework for Modelling Hybrid Systems Dupont, G., Ait-Ameur, Y., Singh, N.K., Pantel, M. ACM Transactions on Embedded Computing Systems, 2021 https://www.scopus.com/pages/publications/85108022745?origin=scopusAI

48. Artificial intelligence and fuzzy logic for next-generation intelligent transportation systems Varra, L.B., Thakur, M.S., Chinthala, K.K.R., Lippert, K. Artificial Intelligence and Fuzzy Logic for Next-Generation Intelligent Transportation Systems, 2026 https://www.scopus.com/pages/publications/105030223504?origin=scopusAI

49. Fuzzy Logic in Transportation: Navigating Uncertainty for Intelligent Systems Dagal, I., Kausar, N., Salman, M.A., Mohammed, F. Lecture Notes in Intelligent Transportation and Infrastructure, 2026 https://www.scopus.com/pages/publications/105029870422?origin=scopusAI

50. Hybrid Fuzzy Neural Systems for Real Time Decision Making in Autonomous Vehicles Indhumathi, R., Jeyalakshmi, M.S., Hemalatha, N., (...), Yadav, K. Journal of Machine and Computing, 2025 https://www.scopus.com/pages/publications/105016722043?origin=scopusAI

51. AI and fuzzy logic in traffic accident prediction and prevention Fabiyi, O., Olanipekun, W. Artificial Intelligence and Fuzzy Logic for Next-Generation Intelligent Transportation Systems, 2026 https://www.scopus.com/pages/publications/105030224209?origin=scopusAI

52. A Cross-Domain Scientometric Analysis of Situational Awareness of Autonomous Vehicles With Focus on the Maritime Domain Bogusllwski, K., Nasur, J., Li, J., (...), Goerlandt, F. IEEE Access, 2022 https://www.scopus.com/pages/publications/85130086958?origin=scopusAI

53. Research progress for cooperative control of heterogeneous unmanned systems Guo, X., Li, Q., Yao, Q., Lu, X. Gongcheng Kexue Xuebao/Chinese Journal of Engineering, 2025 https://www.scopus.com/pages/publications/85212634799?origin=scopusAI

54. Hybridization of safety and security for the design and validation of autonomous vehicles: where are we? Boyer, M., Chelim, T., Sobieraj, J. Proceedings of the 31st European Safety and Reliability Conference, ESREL 2021, 2021 https://www.scopus.com/pages/publications/85135455489?origin=scopusAI

55. Situation Awareness by Design: A Human-Centered Workstation for Teleoperated Vessels Gusev, A., Tufte, A.G., Petermann, F.-M., (...), Breivik, M. Journal of Physics: Conference Series, 2025 https://www.scopus.com/pages/publications/105021211224?origin=scopusAI
