---
source_pdf: "Scopus - Scopus AI - 6.pdf"
source_sha256: "96b783a528393864d2cac627d16efff18c8b39163eea79132598448be6017237"
source_pages: 15
scopus_ai_generated: "Mon Nov 16 2026"
query: "Empirical studies on safety filtering and risk recommendations"
report_title: "Empirical Comparison of Safety Filtering, Permissive Shielding, and Risk-Adaptive Restrictions Versus Binary Abstention and Full Shutdown: Safety, Utility, and Robustness Under Partial Observability and Degraded Inputs"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Empirical studies on safety filtering and risk recommendations

## Quick Reference

## Key Findings Table

| Mechanism | Safety Outcomes | Retained Utility | Robustness (Partial Observability/Degraded Inputs) | Empirical Evidence Quality |
| --- | --- | --- | --- | --- |
| Action-Specific Safety Filtering | High (smooth CBFs, P-CBFs) | High (continuous operation) | Strong (adaptive, less conservative) | High |
| Permissive Shielding | High (minimal intervention) | High (task performance retained) | Strong (adaptive, modular, sensor fusion) | High |
| Risk-Adaptive Recommendation Restrictions | High (dynamic, context-aware) | High (utility-safety balance) | Strong (risk-aware, robust to uncertainty) | High |
| Binary Abstention | High (near boundaries/adversary) | Low (deadlocks, reduced perf.) | Weak (vulnerable to adversarial/missing data) | Moderate |
| Full Shutdown | Very High (conservative) | Very Low (halts operation) | Moderate (avoids unsafe states, but over-conservative) | Moderate |

## Direct Answer

Empirical studies consistently demonstrate that action-specific safety filtering, permissive shielding, and risk-adaptive recommendation restrictions outperform binary abstention and full shutdown in balancing safety, retained utility, and robustness under partial observability and degraded input data. Smooth and adaptive mechanisms maintain higher operational utility and robustness, while binary and shutdown strategies, though sometimes safer, often result in deadlocks, reduced performance, and vulnerability to adversarial or missing data scenarios. Adaptive, predictive, and learning-based frameworks are key to

achieving robust safety without sacrificing utility[1][2][3][4][5].

## Study Scope

**Time Period:** 2015–2024 **Disciplines:** Control theory, reinforcement learning, robotics, autonomous vehicles, safety-critical AI, cyber-physical systems, biomedical systems **Methods:** Empirical benchmarking, simulation, real-world experiments, robustness testing (metamorphic, reachability, noise stress), comparative analysis, ablation studies

## Assumptions & Limitations

Most studies use simulated or controlled real-world environments; generalization to open-world, high-stakes domains may require further validation[6][7]. Partial observability and degraded input data are often modeled as noise, missingness, or adversarial perturbations; real-world missing data mechanisms (e.g., MNAR) are underexplored[8][9]. Robustness metrics and evaluation protocols are not yet standardized across domains[10][11]. Some advanced mechanisms (e.g., learning-based reusable filters) are still emerging and lack large-scale deployment evidence[12][13].

## Suggested Further Research

Systematic empirical comparison under diverse missing data mechanisms (beyond MCAR/MAR), using real-world failure data[8][9].

Development of unified, multidimensional robustness metrics capturing safety, utility, and environmental uncertainty[11][14].

Standardized datasets and benchmarks for evaluating safety mechanisms under degraded inputs and partial observability[7].

Exploration of hybrid adaptive architectures combining model-based and data-driven safety filters for generalization across tasks[12][13].

## 1. Introduction

Safety-critical AI and control systems increasingly operate in uncertain, dynamic, and partially observable environments. Traditional binary safety mechanisms—such as abstention (refusing to act near decision boundaries) or full system shutdown—offer strong safety guarantees but often at the cost of operational utility and robustness, especially under degraded or incomplete input data. In contrast, advanced mechanisms like action-specific safety filtering, permissive shielding, and risk-adaptive recommendation restrictions promise to balance safety with continued operation, even when sensor data is noisy, missing, or adversarially perturbed[6][10][15].

## Scope and Relevance

This report synthesizes empirical evidence comparing these advanced safety mechanisms against binary abstention and full shutdown, focusing on three core dimensions: **Safety outcomes:** Frequency of constraint violations, collisions, or unsafe states. **Retained utility:** Task performance, exploration-exploitation balance, and operational continuity. **Robustness:** Performance under partial observability, sensor degradation, and adversarial or missing data. The findings are highly relevant for the deployment of AI in safety-critical domains such as autonomous vehicles, robotics, and industrial automation, where real-world conditions often deviate from idealized assumptions[6][10][15].

## 2. Definitions and Implementations of Safety Mechanisms

## 2. 1 Action-Specific Safety Filtering

## Definition:

Action-specific safety filtering refers to mechanisms that selectively modify or mask unsafe actions at runtime, rather than halting operation entirely. Key implementations include: **Latent Safety Filters:** Operate in the latent space of learned models, using smooth control barrier functions (CBFs) to enforce safety constraints without abrupt switching[16][17][18][19].

**Smooth CBFs:** Replace hard, binary constraint activation with smooth transitions, reducing control discontinuities and improving safety-utility trade-offs[16][17].

**Soft Action Masking:** Gradually reduces the probability of unsafe actions based on empirical risk estimation, supporting exploration in reinforcement learning[17].

## Key Features:

Continuous intervention, avoiding deadlocks and abrupt shutdowns. Maintains exploration and learning efficiency.

Adaptable to both deterministic and stochastic environments.

## 2. 2 Permissive Shielding Architectures

## Definition:

Permissive shielding minimally intervenes in the nominal control policy, only modifying actions when necessary to ensure safety. Typical architectures include: **CBF-QP Safety Filters:** Use quadratic programming to enforce safety constraints with minimal deviation from the nominal control input[18][20][21][22].

**Modular Architectures:** Combine a high-performance controller (e.g., RL policy) with a safety filter that acts as a shield[20][23].

**Data-Driven Safety Filters:** Learn safety boundaries from data, enabling application to unknown or time-delay systems[21][22].

## Key Features:

Minimal intervention philosophy—preserves nominal performance unless safety is at risk. Supports modularity and reuse across tasks. Can be enhanced with adaptive or predictive elements for robustness.

## 2. 3 Risk-Adaptive Recommendation Restrictions

## Definition:

These mechanisms dynamically adjust safety constraints based on real-time assessments of input uncertainty and environmental context. **CVaR-BF (Conditional Value-at-Risk Barrier Functions):** Adaptively expand safety margins in response to increased risk[24]. **Adaptive MPC (Model Predictive Control):** Online adjustment of risk-sensitive safety margins, mapping risk levels to CBF constraints[25][26]. **Perceptual Risk-Aware Models:** Evaluate scenario risk and adapt safety parameters accordingly[27].

## Key Features:

Context-aware, dynamically balancing safety and utility.

Proactive adaptation to uncertainty, rather than conservative default shutdowns. Supports efficient operation in dynamic, uncertain environments.

## 2. 4 Binary Abstention and Full Shutdown

## Definition:

**Binary Abstention:** The system refuses to act (abstains) when uncertainty is high or near decision boundaries[28][29]. **Full Shutdown:** The system halts all operations upon detecting unsafe conditions[30].

## Limitations:

Can lead to deadlocks, reduced performance, and vulnerability to adversarial exploitation (e.g., boundary reconstruction attacks)[28]. Overly conservative, sacrificing utility for safety, especially problematic in dynamic or partially observable environments.

**3. Comparative Empirical Evidence: Safety Outcomes, Utility, and Robustness**

## 3. 1 Safety Outcomes in Real-World Control Tasks

Empirical studies consistently show that advanced safety mechanisms outperform binary abstention and full shutdown in real-world and simulated control tasks:

## Smooth CBFs and Predictive-Flow CBFs:

Reduce control input discontinuities and improve safety rates (e.g., 97% collision-free episodes in robotic navigation) compared to binary switching[1][31][32]. Avoid deadlocks and undesired equilibria common in binary abstention[1][33]. Enable safe navigation in unknown environments using online sensor data, which is challenging for binary methods[34].

## Permissive Shielding:

Minimally invasive, reducing unnecessary interventions and maintaining safety in dynamic, multi-agent, and uncertain environments[20][21].

Adaptive shielding (e.g., Fear Field) reduces safety violations by an order of magnitude compared to static shields[35].

## Risk-Adaptive Restrictions:

Dynamically adjust safety margins, achieving zero safety violations and higher goal-reaching rates compared to full shutdown or static constraints[24][25][26].

## Synthesis:

Smooth, adaptive, and predictive safety mechanisms consistently achieve high safety rates while avoiding the operational pitfalls of binary abstention and shutdown[1][2][24]. **3. 2 Retained Utility and Exploration-Exploitation Trade-o ff s**

## Soft Action Masking:

Maintains exploration and learning efficiency, outperforming hard masking and shutdown in RL tasks [3][17][36][37]. Adaptive entropy regularization further improves reward accumulation without extra tuning[3].

## Permissive Shielding:

Preserves nominal controller performance, only intervening when necessary[20][23]. Modular architectures allow for shielded training, reducing overdependence on runtime interventions [20].

## Risk-Adaptive Restrictions:

Balance safety and utility by adjusting risk levels in real time, avoiding the conservatism of full shutdown[24][25][26].

Empirical studies show that risk-adaptive strategies reduce operating costs and improve reliability compared to strict shutdown[38].

## Binary Abstention/Full Shutdown:

Lead to reduced utility, deadlocks, and hindered exploration, especially in RL and dynamic environments[28][29][30].

## Synthesis:

Advanced mechanisms maintain higher retained utility and support efficient exploration, while binary and

shutdown strategies often sacrifice performance for safety[3][5][37]. **3. 3 Robustness Under Partial Observability and Degraded Inputs**

## Adaptive Safety Filters:

Incorporate sensor fusion, Bayesian uncertainty estimation, and robust optimization to maintain safety under noisy, missing, or adversarial data[29][35][39][40].

Permissive shielding with adaptive sensor fusion rapidly recovers from sensor faults, maintaining control performance[39].

## Conformal Prediction Frameworks:

Provide statistically guaranteed uncertainty estimates and adaptive abstention, maintaining high detection performance under perturbations[29].

Vulnerable to adversarial attacks and data contamination, but ensemble and active data-cleaning strategies can mitigate these issues[41][42].

## Robustness Metrics and Testing:

Metamorphic testing, reachability analysis, and structured singular value techniques effectively capture performance degradation under partial observability[10][11].

Robustness-aware evaluation metrics (e.g., worst-case reachability, violation value metrics) provide probabilistic safety guarantees under uncertainty[43][44].

## Synthesis:

Adaptive, predictive, and learning-based safety mechanisms demonstrate strong robustness under degraded input conditions, outperforming binary and shutdown strategies that lack adaptivity[11][35][40].

## 4. Evaluation Metrics and Methodologies

## 4. 1 Safety and Utility Metrics

**Collision-Free Rate:** Percentage of episodes without safety violations (e.g., collisions)[1][12]. **Constraint Violation Rate:** Frequency of unsafe state or action occurrences[37]. **Task Completion/Goal-Reaching Rate:** Success in achieving task objectives while maintaining safety [32].

**Safety-Weighted Utility:** Composite metric balancing task performance and safety adherence[37].

## 4. 2 Robustness Evaluation Methodologies

**Metamorphic Testing:** Simulates environmental and sensor degradations to uncover safety-critical failures[10][45]. **Reachability Analysis:** Quantifies the set of states reachable under uncertainty, supporting probabilistic safety guarantees[11]. **Structured Singular Value Techniques:** Analyze robustness under parametric uncertainty and unmodeled dynamics[46]. **Multidimensional Robustness Metrics:** Integrate performance, complexity, and stability for holistic assessment[14].

**4. 3 Testing Under Partial Observability and Degraded Inputs** **Noise Stress Tests:** Evaluate performance under varying noise levels[47]. **Bootstrap Evaluation:** Assess stability and reliability under resampled data[47]. **Simulation-Based Fault Injection:** Test system response to sensor failures and data corruption[48][49]. **Self-Referential Robustness Measures:** Compare degraded input outputs to baseline for real-time monitoring[50].

**5. Challenges and Research Gaps in Partial Observability and Degraded Inputs**

## 5. 1 Challenges in Real-World Deployments

**Simulation Bias and Data Drift:** Simulated environments may not capture real-world complexity; data drift and sensor degradation complicate validation[6][51].

**Incomplete Data Mechanisms:** Most studies assume MCAR/MAR; MNAR and systematic missingness are underexplored, leading to potential bias[52][53].

**Sensor Degradation:** Noise, blur, and adversarial perturbations reduce robustness; real-world sensor failures are difficult to model and mitigate[40][54].

## 5. 2 Mitigation Strategies and Solutions

**Robust Filtering and Sensor Fusion:** Adaptive sensor fusion and robust filtering techniques improve estimation accuracy and resilience to sensor faults[55][56][57][58].

**Bayesian and Double Robust Methods:** Quantitative frameworks for handling incomplete or noisy data, improving inference validity[55][56].

**Learning-Based Safety Filters:** Enable reuse across tasks and adapt to changing environments without retraining[12][13].

**Active Data Cleaning and Ensemble Methods:** Mitigate adversarial and contaminated data effects in conformal prediction frameworks[41][42].

## 5. 3 Gaps and Future Research Directions

**Validation Under Real-World Missing Data:** Need for empirical studies using real-world failure data and systematic missingness mechanisms (beyond MCAR)[8][9].

**Unified Robustness Metrics:** Development of standardized, multidimensional metrics capturing safety, utility, and robustness[11][14].

**Standardized Benchmarks:** Creation of datasets and protocols for evaluating safety mechanisms under degraded inputs and partial observability[7].

**Hybrid Adaptive Architectures:** Exploration of architectures combining model-based and data-driven safety filters for generalization and scalability[12][13].

## 6. Discussion and Synthesis

## 6. 1 Trade-o ff s and Practical Implications

Empirical evidence demonstrates that advanced safety mechanisms—particularly those that are smooth, adaptive, and predictive—offer superior trade-offs between safety, utility, and robustness compared to binary abstention and full shutdown. Key practical implications include: **Continuous Operation:** Smooth and adaptive filters avoid deadlocks and maintain operational continuity, critical for real-world deployment[1][2].

**Efficient Exploration:** Soft action masking and risk-adaptive restrictions support efficient learning and adaptation, essential in dynamic environments[3][37].

**Robustness to Degradation:** Adaptive sensor fusion, robust filtering, and Bayesian methods enhance resilience to sensor faults and data corruption[39][58].

**Modularity and Reuse:** Learning-based safety filters enable modular architectures, reducing retraining costs and supporting scalability[12][13]. However, challenges remain in validating these mechanisms under real-world missing data mechanisms and in developing unified robustness metrics[8][14].

## 6. 2 Recommendations for Robust Safety Mechanism Design

**Prioritize Adaptive and Predictive Mechanisms:** Use smooth CBFs, risk-adaptive restrictions, and permissive shielding to balance safety and utility under uncertainty[20][39].

**Integrate Robustness Evaluation Early:** Employ metamorphic testing, reachability analysis, and multidimensional metrics during development[11][59].

**Design for Modularity and Reuse:** Separate safety and performance components to enable reuse and rapid adaptation across tasks[12][13].

**Address Real-World Data Challenges:** Develop and validate methods under diverse missing data mechanisms, using real-world failure data where possible[8][60].

**Combine Model-Based and Data-Driven Approaches:** Hybrid architectures can leverage the strengths of both paradigms for robust, scalable safety[12][13].

## Synthesis

Adaptive and predictive safety mechanisms—such as smooth CBF filters, permissive shielding, and risk-adaptive recommendation restrictions—consistently outperform binary abstention and full shutdown in balancing safety, retained utility, and robustness under partial observability and degraded input data. The convergence of learning-based safety filters with traditional control theory offers promising avenues for reusable, flexible safety architectures. However, further empirical research is needed to address real-world missing data mechanisms and to develop unified robustness evaluation metrics, ensuring reliable deployment in safety-critical domains[1][8][12][14].

## References

1. Smooth Barrier-Certificate Reinforcement Learning for Safe Multi-Agent Control Under Input Constraints Son, H., Jung, S. ICMIC 2026 - International Conference on Mobile, Military, Maritime IT

Convergence - Connecting Worlds: The IT Horizon of M3, Mobile, Military, Maritime, 2026 https://www.scopus.com/pages/publications/105055200024?origin=scopusAI

2. Predictive Control Barrier Functions: Bridging model predictive control and control barrier functions Huang, J., Wang, H., Margellos, K., Goulart, P. European Control Conference (Piscataway, N.J. Online), ECC, 2025 https://www.scopus.com/pages/publications/105031008980?origin=scopusAI

3. Learning to Optimize Entropy in the Soft Actor-Critic Zhou, Z., Heywood, M.I. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105016620872?origin=scopusAI

4. Adapting to Misspecification Armstrong, T.B., Kline, P., Sun, L. Econometrica, 2025 https://www.scopus.com/pages/publications/105023364706?origin=scopusAI

5. Empirical study on car-following characteristics of commercial automated vehicles with different headway settings Shi, X., Li, X. Transportation Research Part C: Emerging Technologies, 2021 https://www.scopus.com/pages/publications/85105054182?origin=scopusAI

6. Machine Learning Observability in Practice Leest, J., Gerostathopoulos, I., Lago, P., Raibulet, C. Proceedings - 2026 IEEE/ACM 5th International Conference on AI Engineering - Software Engineering for AI, CAIN 2026, 2026 https://www.scopus.com/pages/publications/105052306876?origin=scopusAI

7. A systematic literature review of RAM+ analysis: methodologies, applications, and gaps Bachega Cruz, J.P., González Rodríguez, D., Abreu, D.T.M.P., (...), Martins, M.R. Journal of Quality in Maintenance Engineering, 2026 https://www.scopus.com/pages/publications/105054479379?origin=scopusAI

8. Testing the missingness mechanism in longitudinal surveys: a case study using the Health and Retirement Study Lu, P., Shelley, M. International Journal of Social Research Methodology, 2023 https://www.scopus.com/pages/publications/85126790940?origin=scopusAI

9. Identifiable Generative Models for Missing Not at Random Data Imputation Ma, C., Zhang, C. Advances in Neural Information Processing Systems, 2021 https://www.scopus.com/pages/publications/85123334169?origin=scopusAI

10. Modal Contributions to the Robustness of Fusion Perceptions in Autonomous Driving Nguyen, T.M., Luu, Q.-H., Vu, H.L. IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC, 2025 https://www.scopus.com/pages/publications/105037018012?origin=scopusAI

11. Statistical Reachability Analysis of Stochastic Cyber-Physical Systems Under Distribution Shift Hashemi, N., Lindemann, L., Deshmukh, J.V. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2024 https://www.scopus.com/pages/publications/85209571506?origin=scopusAI

12. Safety Filters for Black-Box Dynamical Systems by Learning Discriminating Hyperplanes Lavanakul, W., Choi, J.J., Sreenath, K., Tomlin, C.J. Proceedings of Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85203697060?origin=scopusAI

13. Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones Thananjeyan, B., Balakrishna, A., Nair, S., (...), Goldberg, K. IEEE Robotics and Automation Letters, 2021 https://www.scopus.com/pages/publications/85103795957?origin=scopusAI

14. Multidimensional robustness analysis for optimizing complex systems Paiva, J.R.B., Pacheco, V.M.G., Bulhões, J.S., (...), Calixto, W.P. Knowledge-Based Systems, 2025 https://www.scopus.com/pages/publications/105003011919?origin=scopusAI

15. Bounced Check Risk Prediction via Multi-Objective Hyperparameter Optimization: Balancing Macro F1 and Business Uplift Kaya, K., Memiş, E.C., Ertu ǧ rul, S., (...), Çakar, T. Proceedings of the International Symposium on Digital Forensics and Security, ISDFS, 2026 https://www.scopus.com/pages/publications/105038360257?origin=scopusAI

16. How to Train Your Latent Control Barrier Function: Smooth Safety Filtering Under Hard-to-Model Constraints Nakamura, K., Bishop, A.L., Man, S., (...), Bajcsy, A. Proceedings of Machine Learning Research, 2026 https://www.scopus.com/pages/publications/105046074510?origin=scopusAI

17. Action Masking Methods for Safe Reinforcement Learning in a Non-Stationary Configurable Environment Leon, F. 2025 29th International Conference on System Theory, Control and Computing, ICSTCC 2025 - Proceedings, 2025 https://www.scopus.com/pages/publications/105028738940?origin=scopusAI

18. Enhanced safe control for arbitrary relative degree: A generalized discrete-time CBF approach Ma, Q., Li, J., Liu, Q., (...), Sun, J. Automatica, 2026 https://www.scopus.com/pages/publications/105037771499?origin=scopusAI

19. Finite-Time Formation Tracking with CBF-Based Safety Filtering for Multi-Agent Systems Xu, Z., Zhang, K., Yan, B., Shi, P. IEEE International Conference on Computational Intelligence and Cybernetics, ICCC, 2026 https://www.scopus.com/pages/publications/105041989135?origin=scopusAI

20. Safety-Enhanced COLREGs-Compliant Path Planning for USVs with a CBF-Based Safety Shield Yun, S.-J., Kim, H., Kwon, J.-W., (...), Choi, J.-H. Journal of Marine Science and Engineering, 2026 https://www.scopus.com/pages/publications/105048465787?origin=scopusAI

21. From Raw Data to Safety: Reducing Conservatism by Set Expansion Bajelani, M., van Heusden, K. Proceedings of Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85203714642?origin=scopusAI

22. Data-Driven Safety Filter: An Input-Output Perspective Bajelani, M., Van Heusden, K. Proceedings of the American Control Conference, 2024 https://www.scopus.com/pages/publications/85204423134?origin=scopusAI

23. Modular control architecture for safe marine navigation: Reinforcement learning with predictive safety filters Vaaler, A., Husa, S.J., Menges, D., (...), Rasheed, A. Artificial Intelligence, 2024 https://www.scopus.com/pages/publications/85201239744?origin=scopusAI

24. Safe Navigation in Uncertain Crowded Environments Using Risk Adaptive CVaR Barrier Functions Wang, X., Kim, T., Hoxha, B., (...), Panagou, D. IEEE International Conference on Intelligent Robots and Systems, 2025 https://www.scopus.com/pages/publications/105029925284?origin=scopusAI

25. Learning-Guided Risk-Adaptive MPC with Control Barrier Functions for Safe Navigation in Uncertain Dynamic Environments Sun, Z., Wang, S., Pang, Y., (...), Wang, J. IEEE International Conference on Robotics and Biomimetics, ROBIO, 2025 https://www.scopus.com/pages/publications/105034724917?origin=scopusAI

26. Risk-Aware Adaptive Safety Margins for Model Predictive Control with Orientation–Motion Coupled Barrier Functions in Dynamic Environments Xu, N., Yang, Z., Zhuo, H., (...), He, N. Actuators, 2026 https://www.scopus.com/pages/publications/105031234729?origin=scopusAI

27. Perceptual Risk-Aware Adaptive Responsibility Sensitive Safety for Autonomous Driving Li, X., Wu,

X., Zhao, Y., Li, Y. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85164038110?origin=scopusAI

28. Information Design Against Gaming and Learning Adversaries Gaikwad, M. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105055110368?origin=scopusAI

29. Uncertainty-Aware LiDAR-Camera Autonomy via Conformal Prediction and Principled Abstention Kumar, D., Tayebati, S., Darabi, N., (...), Trivedi, A.R. 2025 IEEE International Conference on Omni-Layer Intelligent Systems, COINS 2025, 2025 https://www.scopus.com/pages/publications/105016217249?origin=scopusAI

30. Analysis of shutdown mode at barsebäck 2; An approach to a combined PSA, HFA and deterministic analysis Bäckström, O., Ingemarson, I., Olsson, A. Proceedings of the 8th International Conference on Probabilistic Safety Assessment and Management, PSAM 2006, 2006 https://www.scopus.com/pages/publications/84892633525?origin=scopusAI

31. Smooth Transition of Safety Controllers Filtered by Control Barrier Functions Li, S., Yuan, Z., Ye, Q., (...), Li, M. Journal of Physics: Conference Series, 2023 https://www.scopus.com/pages/publications/85151680204?origin=scopusAI

32. Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control Safari, A., Hoagg, J.B. IEEE Open Journal of Control Systems, 2026 https://www.scopus.com/pages/publications/105051591077?origin=scopusAI

33. Circulation-embedded Control Barrier Function for safe navigation: A solution to avoid undesired equilibria and dysfunctional circulation Keyumarsi, S., Atman, M.W.S., Gusrialdi, A. Robotics and Autonomous Systems, 2025 https://www.scopus.com/pages/publications/105013513332?origin=scopusAI

34. LiDAR-Based Online Control Barrier Function Synthesis for Safe Navigation in Unknown Environments Keyumarsi, S., Atman, M.W.S., Gusrialdi, A. IEEE Robotics and Automation Letters, 2024 https://www.scopus.com/pages/publications/85179782194?origin=scopusAI

35. Fear Field: Adaptive constraints for safe environment transitions in Shielded Reinforcement Learning Odriozola-Olalde, H., Arana-Arexolaleiba, N., Zamalloa, M., (...), Arozamena-Rodríguez, J. CEUR Workshop Proceedings, 2023 https://www.scopus.com/pages/publications/85175724579?origin=scopusAI

36. Pure-Past Action Masking Varricchione, G., Alechina, N., Dastani, M., (...), Perelli, G. Proceedings of the AAAI Conference on Artificial Intelligence, 2024 https://www.scopus.com/pages/publications/85189645873?origin=scopusAI

37. Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery Zhang, X., Zhang, H., Zhou, H., (...), Zhao, J. IEEE Robotics and Automation Letters, 2024 https://www.scopus.com/pages/publications/85177065846?origin=scopusAI

38. Impacts of Risk Metrics for Wildfire-Driven Public Safety Power Shutoffs Cheng, C., Zhao, J. IEEE Power and Energy Society General Meeting, 2026 https://www.scopus.com/pages/publications/105053363758?origin=scopusAI

39. Adaptive Sensor Fusion-Enhanced Deep Reinforcement Learning for Fault-Tolerant Autonomous Control Marrah, S.A., Wang, J., Lahai, J.I., (...), Wei, J. IEEE Access, 2026 https://www.scopus.com/pages/publications/105039011764?origin=scopusAI

40. GUARDIAN: Safety Filtering for Systems With Perception Models Under Adversarial Attack Rober, N., Rose, A., How, J.P. IEEE Control Systems Letters, 2026 https://www.scopus.com/pages/publications/105039556044?origin=scopusAI

41. Robust Yet Efficient Conformal Prediction Sets Zargarbashi, S.H., Akhondzadeh, M.S., Bojchevski, A. Proceedings of Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85203804523?origin=scopusAI

42. Robust Conformal Outlier Detection under Contaminated Reference Data Bashari, M., Sesia, M., Romano, Y. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105023639175?origin=scopusAI

43. A data-driven approach to preserve safety and reference tracking for constrained cyber-physical systems under network attacks Attar, M., Lucia, W. European Journal of Control, 2026 https://www.scopus.com/pages/publications/105051685683?origin=scopusAI

44. Verifying Online Safety Properties for Safe Deep Reinforcement Learning Marzari, L., Cicalese, F., Farinelli, A., (...), Marchesini, E. ACM Transactions on Intelligent Systems and Technology, 2025 https://www.scopus.com/pages/publications/105029754373?origin=scopusAI

45. Safety-Critical Oracles for Metamorphic Testing of Deep Learning LiDAR Point Cloud Object Detectors Speth, S., Trien, M., Kufer, D., Pretschner, A. IEEE Open Journal of Intelligent Transportation Systems, 2025 https://www.scopus.com/pages/publications/85215975722?origin=scopusAI

46. Robustness analysis methods for underwater vehicle control systems Appleby, Brent, Bonnice, William, Bedrossian, Nazareth Proceedings of the Symposium on Autonomous Underwater Vehicle Technology, 1990 https://www.scopus.com/pages/publications/0025626683?origin=scopusAI

47. Protocol to assess robustness of ST analysers: A case study Jager, F., Moody, G.B., Mark, R.G. Physiological Measurement, 2004 https://www.scopus.com/pages/publications/3142619210?origin=scopusAI

48. A deductive method for diagnostic analysis of digital instrumentation and control systems Yang, J., Aldemir, T., Smidts, C. IEEE Transactions on Reliability, 2018 https://www.scopus.com/pages/publications/85052651253?origin=scopusAI

49. Quantization Robustness to Input Degradations for Object Detection Karimov, T., Imani, H., Kazakov, A. 2025 Innovations in Intelligent Systems and Applications Conference, ASYU 2025, 2025 https://www.scopus.com/pages/publications/105022477321?origin=scopusAI

50. A Novel Robustness Measure for Evaluating Perceptions in Autonomous Driving Nguyen, M.T., Luu, Q.-H., Vu, H.L. IEEE Transactions on Intelligent Transportation Systems, 2025 https://www.scopus.com/pages/publications/105020419068?origin=scopusAI

51. Output analysis for terminating simulations with partial observability Kami ń ski, B., Koloch, G. Simulation Modelling Practice and Theory, 2017 https://www.scopus.com/pages/publications/85002323845?origin=scopusAI

52. On the Importance of Using Realistic Data for Safety System Calculations Hauge, S., Håbrekke, S., Ottermo, M.V., (...), Lundteigen, M.A. Proceedings of the 31st European Safety and Reliability Conference, ESREL 2021, 2021 https://www.scopus.com/pages/publications/85135494965?origin=scopusAI

53. Observability Informed Partial-Update Schmidt Kalman Filter Ramos, J.H., Adams, D.W., Brink, K.M., Majji, M. Proceedings of 2021 IEEE 24th International Conference on Information Fusion, FUSION 2021, 2021 https://www.scopus.com/pages/publications/85206939284?origin=scopusAI

54. Automated Vehicular Safety Systems: Robust Function and Sensor Design Stockle, C., Herrmann, S., Dirndorfer, T., Utschick, W. IEEE Signal Processing Magazine, 2020 https://www.scopus.com/pages/publications/85087828195?origin=scopusAI

55. Simplified analysis of incomplete data on risk Reer, B. Handbook of Advanced Performability Engineering, 2020 https://www.scopus.com/pages/publications/85149354481?origin=scopusAI

56. Introduction to double robust methods for incomplete data Seaman, S.R., Vansteelandt, S. Statistical Science, 2018 https://www.scopus.com/pages/publications/85046767867?origin=scopusAI

57. Robust Data-Driven Control Barrier Functions for Unknown Continuous Control Affine Systems Jin, Z., Khajenejad, M., Yong, S.Z. IEEE Control Systems Letters, 2023 https://www.scopus.com/pages/publications/85147200424?origin=scopusAI

58. Enhancing filter robustness in cascaded GPS-INS integrations Karatsinides, S.P. IEEE Transactions on Aerospace and Electronic Systems, 1994 https://www.scopus.com/pages/publications/0028530659?origin=scopusAI

59. On the Challenges of Monitoring Robust Systems Klampfl, L., Perko, A., Wotawa, F. Proceedings - 2025 12th International Conference on Dependable Systems and Their Applications, DSA 2025, 2025 https://www.scopus.com/pages/publications/105032965901?origin=scopusAI

60. Methodological Pathways for Safety and Risk Mitigation in Reduced Crew Aviation Operations Zolghadri, A. Conference on Control and Fault-Tolerant Systems, SysTol, 2025 https://www.scopus.com/pages/publications/105030234663?origin=scopusAI
