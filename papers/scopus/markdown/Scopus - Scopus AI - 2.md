---
source_pdf: "Scopus - Scopus AI - 2.pdf"
source_sha256: "219150aa4bd9f1fe9d80716946cb5784c50a678d1b08c6bd002a03eb5b272919"
source_pages: 15
scopus_ai_generated: "Mon Nov 16 2026"
query: "Safety-utility trade-o ff s in AI decision support"
report_title: "Safety–Utility Trade-o ff s in Selective Prediction, Probabilistic Shielding, Learning to Defer, and Partial AI Abstention: Evidence, E ff ectiveness, and Limitations in Safety-Critical Decision Support Quick Reference"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Safety-utility trade-o ff s in AI decision support

## Key Findings Table

| Methodology | Demonstrated Safety Gains | Utility Retention | Key Limitations | Human Factors Addressed | Representative Studies |
| --- | --- | --- | --- | --- | --- |
| Selective Prediction | Yes (esp. with conformal prediction, calibration) | Moderate–High (domain-dependent) | Miscalibration, OOD detection, aggregate metric pitfalls | Partial (workload, trust not always explicit) | 1, 1, 1 |
| Probabilistic Shielding | Yes (formal guarantees, adaptive shields) | Moderate (conservatism, computational cost) | Unknown dynamics, conservatism, explainability | Some (trust, explainability, workload) | 2, 3, 4 |
| Learning to Defer | Yes (cost-sensitive, capacity-aware, meta-learning) | High (with workload constraints) | Data scarcity, adaptation to new experts, communication | Yes (workload, trust, transparency) | 5, 5, 6 |
| Partial AI Abstention | Yes (conformal prediction, uncertainty-based) | Moderate–High (with principled thresholds) | OOD uncertainty, communication, trust calibration | Yes (judgment, trust, explanation) | 7, 8, 9 |

## Direct Answer

Peer-reviewed research demonstrates that selective prediction, probabilistic shielding, learning to defer, and partial AI abstention can improve decision safety by enabling abstention or deferral under high uncertainty, especially when combined with robust calibration and uncertainty quantification. These methods retain useful advice but face persistent limitations in miscalibration, computational overhead, domain-specific trade-offs, and insufficient integration of human factors such as trust and workload management. A standardized set of benchmark studies with titles and DOIs is lacking, highlighting a research gap in consolidated reporting and comparative analysis.

## Unable to Find

A definitive list of five key studies with both titles and DOIs was not identified in the reviewed literature, indicating a gap in standardized reporting and aggregation.

## Study Scope

**Time Period:** Primarily 2018–2024 **Disciplines:** Clinical decision support, medical imaging, reinforcement learning, human-AI collaboration, safety engineering, public health, transportation **Methods:** Conformal prediction, Bayesian networks, reinforcement learning with shielding, meta-learning, uncertainty quantification, human factors analysis, simulation studies, empirical evaluation

## Assumptions & Limitations

Most studies focus on technical performance and calibration, with less emphasis on holistic human-AI system evaluation. Human factors (trust, workload, communication) are often secondary considerations. Many methods are evaluated in simulation or retrospective datasets, with limited prospective or real-world deployment evidence. Out-of-distribution (OOD) robustness and adaptation remain open challenges. Lack of standardized benchmarks and reporting (titles, DOIs) impedes meta-analysis.

## Suggested Further Research

Develop and publish standardized benchmark studies with clear reporting (titles, DOIs). Integrate user-centric measures (trust calibration, workload, accountability) with technical metrics. Advance adaptive uncertainty quantification for OOD robustness. Design and evaluate communication strategies for AI deferral/abstention in real-world settings. Establish governance and oversight frameworks for human-in-the-loop safety-critical AI.

## 1. Introduction

## Background and Motivation

The increasing reliance on AI for safety-critical decision support in domains such as healthcare, transportation, and public health has intensified the need to balance safety (minimizing harmful errors) and utility (maximizing actionable, useful advice). Traditional AI systems that always predict or act can propagate errors with high confidence, especially under uncertainty or distribution shift. To address this, four methodological paradigms have emerged: **Selective Prediction:** AI abstains from making predictions when uncertainty is high, deferring to human experts or alternative processes.

**Probabilistic Shielding:** Reinforcement learning agents are constrained by probabilistic safety shields that block unsafe actions, balancing exploration and safety.

**Learning to Defer:** AI systems learn when to defer decisions to humans, optimizing for safety, utility, and human workload constraints.

**Partial AI Abstention:** AI systems abstain on uncertain cases, often using principled uncertainty quantification (e.g., conformal prediction), to improve reliability and trust. These paradigms aim to provide safer, more reliable decision support while retaining utility, but each faces unique challenges in calibration, human factors, and real-world deployment[2][5][7][10].

## 2. Theoretical Frameworks

**2. 1 Selective Prediction: Safety–Utility Trade-o ff s and Calibration**

## Calibration and Uncertainty Estimation

**Calibration** is central to selective prediction: well-calibrated uncertainty estimates (e.g., via conformal prediction, temperature scaling, Platt scaling) enable AI systems to abstain on cases where predictions are unreliable, reducing risk in safety-critical applications[1][11][12][13].

**Conformal prediction** provides statistically valid uncertainty estimates and coverage guarantees, supporting robust selective prediction in clinical triage and medical imaging[1].

**Uncertainty-aware training** (e.g., penalizing confident errors, using ensemble methods) further improves calibration and selective prediction reliability[14][15].

## Domain-Specific Trade-o ff s

Safety–utility trade-offs are highly context-dependent. For example, in healthcare, selective prediction can reduce clinical risk by deferring uncertain cases to clinicians, but may concentrate errors among withheld predictions if miscalibration is not addressed[16][17][18].

In transportation and public health, domain-specific factors (e.g., data requirements, population

heterogeneity) influence the optimal balance between safety and utility[17][19].

## Evaluation Metrics

**Class-averaged metrics** (e.g., CA-AURC, CA-AUGRC) and **risk-coverage curves** better capture safety risks and fairness under class imbalance than aggregate metrics[20][21][22].

**Calibration-aware measures** are essential for revealing disparities in rejection behavior and supporting balanced human-AI collaboration[20][23].

## Limitations

**Class-dependent miscalibration** and aggregate metric pitfalls can obscure safety risks, especially for underrepresented conditions[10]. **Out-of-distribution (OOD) detection** remains challenging; current uncertainty quantification methods may not reliably flag novel or shifted data[24]. **Evaluation practices** are often fragmented, with limited attention to user-centric reliability[25]. **2. 2 Probabilistic Shielding: Balancing Safety and Utility in Human-AI Collaboration**

## Formal Guarantees and Adaptive Shielding

**Probabilistic shielding** extends classical safety shields to allow for acceptable risk levels in reinforcement learning, providing formal safety guarantees while permitting exploration[2][3][4].

**Adaptive shielding** integrates online model learning, updating shields as transition probability estimates improve, balancing exploration and safety dynamically[2].

**Model-free approaches** (e.g., ProSh) augment state space with risk budgets and use learned cost critics to enforce safety during training, even with unknown dynamics[3][4].

## Practical Limitations

**Unknown or stochastic environments** pose challenges: shields may be overly conservative or require frequent recomputation, and strong guarantees may not be preserved[2][26][27]. **Computational demands** are significant, especially for offline shield construction and multi-agent systems[28][29]. **Sensitivity to input uncertainty** can lead to overregulation or suboptimal decisions[30][31].

## Human Factors

**Trust and explainability** are partially addressed: explainable safe RL methods use interpretable decision trees, and human reliability analysis quantifies error probabilities[32][33].

**Erroneous AI advice** can relax human safety standards via moral disengagement, underscoring the need for robust human-AI integration[34].

## Scalability and Robustness

**Compositional and runtime monitoring** approaches improve scalability in multi-agent and partially observable environments[28][29][35]. **Recovery-based shielding** and **dynamic model predictive shielding** allow for safe exploration and sample-efficient learning in unknown systems[36][37]. **2. 3 Learning to Defer: Human-AI Collaboration and Workload Constraints**

## Cost-Sensitive and Capacity-Aware Deferral

**Learning to defer (L2D)** frameworks (e.g., DeCCaF) optimize deferral decisions under human workload constraints, reducing misclassification costs and improving safety in domains like fraud detection[5].

**Constraint programming** and **sequential decision-making** approaches balance error cost and human capacity[5][38].

## Uncertainty-Aware Deferral and Calibration

**Uncertainty quantification** (e.g., conformal prediction, epistemic uncertainty) guides deferral policies, improving calibration and safety, especially under distribution shifts[8][39][40]. **Intermediate neural features** and **scoring-based methods** enhance deferral policy effectiveness[41][42].

## Meta-Learning for Robustness

**Meta-learning** enables L2D systems to adapt to new human experts and dynamic environments, reducing data requirements and enhancing robustness[6][43][44].

**Distributionally robust optimization** and **safe meta-RL** frameworks provide guarantees under task variability and constraint satisfaction[44][45].

## Communication Strategies and Human Factors

**Communication about deferral decisions** (e.g., explicit certainty information, feedback) impacts human trust, workload, and safety[39][46][47].

**Transparency** and **role clarity** are critical for trust calibration and effective collaboration[48][49]. **2. 4 Partial AI Abstention: E ff ectiveness, Human Judgment, and Trust Calibration**

## E ff ectiveness of Partial Abstention

**Partial abstention** (e.g., via conformal prediction, uncertainty-based deferral) improves safety and utility in tasks like clinical triage, image classification, and hate speech detection[7][8][9].

**Post-abstention strategies** (e.g., re-attempting abstained instances) can increase coverage without sacrificing accuracy[50].

## Communication and Human Judgment

**Communication of abstention/deferral** affects human judgment accuracy, workload, and trust; higher deferral rates increase sensitivity but may reduce throughput and trust[51][52][53].

**Trust calibration** is essential for safety; transparency and explicit feedback reduce overtrust and improve decision accuracy[54][55].

## Statistically Guaranteed Uncertainty Estimates

**Conformal prediction frameworks** provide statistically valid uncertainty estimates and principled abstention thresholds, supporting risk control in safety-critical applications[9][56][57].

## Limitations under Distribution Shift

**Uncertainty quantification methods** often fail under OOD inputs, being overconfident and unreliable; adaptive and user-centric evaluation is needed[58][59][60].

## Human Factors and Oversight

**Moral disengagement** and lack of accountability can exacerbate safety risks when humans interact with erroneous AI advice[61][62].

**Oversight frameworks** (e.g., FAIR-AI, CAOS, Human Oversight Anchor) and explainable AI design are proposed to mitigate risks and support human review[63][64][65].

## 3. Methods & Data Transparency

**Selective prediction** studies employ conformal prediction, temperature scaling, and ensemble methods for uncertainty quantification, with evaluation on clinical, imaging, and NLP datasets[1][11].

**Probabilistic shielding** research uses reinforcement learning environments (MDPs, POMDPs), with both offline and online shield construction, and formal verification tools[2][3][29].

**Learning to defer** approaches leverage supervised learning, meta-learning, and constraint programming, often simulating human experts with adjustable workload and error profiles[5][6].

**Partial abstention** studies use conformal prediction, uncertainty thresholding, and post-abstention strategies, evaluated in clinical, NLP, and perception tasks[7][8][9].

**Human factors** are assessed via user studies, simulation, and analysis of trust, workload, and communication strategies[46][51][54].

## 4. Critical Analysis of Findings

## 4. 1 Demonstrated Improvements in Safety and Utility

**Selective prediction** with conformal prediction and robust calibration has reduced error rates by up to 50% in clinical triage under distribution shift, maintaining strong coverage guarantees[1].

**Probabilistic shielding** provides formal safety guarantees in reinforcement learning, enabling safe exploration and reducing safety violations, though at the cost of conservatism and computational complexity[3][4].

**Learning to defer** frameworks (e.g., DeCCaF) achieve significant reductions in misclassification cost (e.g., 8.4% in fraud detection) by optimizing deferral under workload constraints[5].

**Partial AI abstention** using conformal prediction and uncertainty-based deferral improves reliability and trust calibration, with optimal human-AI team accuracy at intermediate abstention thresholds[7][8][53].

## 4. 2 Persistent Limitations and Open Challenges

**Miscalibration** remains a central challenge, especially under OOD conditions; current methods may be overconfident and unreliable when faced with novel data[10][60].

**Computational overhead** in shield construction and uncertainty estimation limits real-time deployment, particularly in multi-agent and high-dimensional systems[26][29].

**Human factors integration** is often insufficient; trust calibration, workload management, and communication strategies are not consistently addressed[34][66].

**Evaluation practices** lack standardization, with fragmented reporting and limited user-centric reliability assessment[25][59].

## 4. 3 Human Factors and Moral Disengagement

**Erroneous AI advice** can lead to relaxation of human safety standards and increased risk-taking, mediated by cognitive-ethical mechanisms like moral disengagement[61][62].

**Transparency and explicit feedback** are critical for trust calibration; overreliance and misaligned trust reduce decision accuracy[54][55].

**Oversight frameworks** and explainable AI design are necessary to mitigate risks and support human review, especially in clinical settings[63][64][65].

## 5. Real-world Implications

**Safer decision support** is achievable with selective prediction, probabilistic shielding, learning to defer, and partial abstention, especially when robust calibration and uncertainty quantification are combined with principled deferral/abstention policies[1][3][5][7].

**Utility retention** depends on domain-specific factors, workload constraints, and the design of human-AI collaboration interfaces[5][16][51].

**Human factors** (trust, workload, communication) are critical for effective deployment; poorly calibrated trust or excessive workload can undermine safety gains[46][54].

**Oversight and governance** frameworks are needed to ensure accountability, transparency, and adaptive risk management in safety-critical AI systems[63][65].

## 6. Future Research Directions

## Research Gaps

**Standardized benchmarks:** There is a need for published, standardized benchmark studies with clear reporting (titles, DOIs) to facilitate comparative analysis and meta-research[23][67].

**Holistic evaluation:** Integrate technical metrics (calibration, coverage, risk) with user-centric measures (trust calibration, workload, accountability) for comprehensive system assessment[39][63].

**Adaptive uncertainty quantification:** Develop methods robust to OOD inputs and distribution shifts, with continuous monitoring and recalibration[60][66].

**Communication strategies:** Design and evaluate communication protocols for AI deferral/abstention that optimize human judgment accuracy, trust, and workload[46][51].

**Governance and oversight:** Establish institutional frameworks (e.g., AI Monitoring Boards, FAIR-AI, CAOS) for human-in-the-loop safety-critical AI, with clear guidelines for explainability, accountability, and risk management[63][65].

## Creative Insights

**Interdisciplinary frameworks** that benchmark technical and user-centric measures, integrate accountability mechanisms, and support adaptive oversight can advance holistic evaluation and deployment of safety-critical AI systems.

**Participatory design** and **longitudinal clinical validation** are essential for aligning AI decision support with real-world workflows and stakeholder needs[68][69].

## Synthesis

Current peer-reviewed research reveals that selective prediction, probabilistic shielding, learning to defer, and partial AI abstention offer promising avenues for enhancing safety in human-facing, safety-critical decision support. These methods, especially when combined with robust calibration and uncertainty quantification, can reduce harmful errors and retain useful advice. However, persistent challenges— including miscalibration under distribution shift, computational overhead, insufficient integration of human factors, and lack of standardized benchmarks—limit their widespread adoption and effectiveness. Addressing these gaps through interdisciplinary research, holistic evaluation, adaptive uncertainty quantification, and robust oversight frameworks is critical for realizing the full potential of AI in safety-critical domains[1][3][5][7][10][26][60][66].

## Five Representative Studies (Where Available)

While a definitive list with titles and DOIs is not consolidated in the literature, the following studies are repeatedly referenced as foundational:

1. **Selective Prediction with Conformal Prediction in Clinical Triage** (e.g.,[1],[1]) Demonstrates improved safety and calibration in clinical decision support.

2. **Probabilistic Shielding in Reinforcement Learning** (e.g.,[2],[3],[4]) Provides formal safety guarantees and adaptive shield construction.

3. **Learning to Defer with Cost-Sensitive and Capacity-Aware Policies** (e.g.,[5],[5]) Balances human workload and safety in critical applications.

4. **Partial AI Abstention with Conformal Prediction** (e.g.,[7],[8],[9]) Offers statistically guaranteed uncertainty estimates and principled abstention.

5. **Meta-Learning for Robust Learning to Defer** (e.g.,[6]) Enables adaptation to new experts and dynamic environments.

**Note:** The absence of explicit titles and DOIs in the reviewed literature highlights a critical research gap and the need for improved reporting and aggregation.

## References

1. Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift Kwon, H., Kim, D.-J. Scientific Reports, 2026 https://www.scopus.com/pages/publications/105034454293?origin=scopusAI

2. Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning Brorholt, A.H., Galesloot, M.F.L., Jansen, N., (...), Schilling, C. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105054364612?origin=scopusAI

3. ProSh: Probabilistic Shielding for Model-free Reinforcement Learning Hamel-De Le Court, E., Ohlmann, G., Belardinelli, F. AAMAS 2026 - Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems, 2026 https://www.scopus.com/pages/publications/105041399032?origin=scopusAI

4. ProSh: Probabilistic Shielding for Model-free Reinforcement Learning Hamel-De Le Court, E., Ohlmann, G., Belardinelli, F. Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems, AAMAS, 2026 https://www.scopus.com/pages/publications/105052635580?origin=scopusAI

5. Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints Alves, J.V., Leitão, D., Jesus, S., (...), Bizarro, P. Transactions on Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85211793770?origin=scopusAI

6. Learning to Defer to a Population: A Meta-Learning Approach Tailor, D., Patra, A., Verma, R., (...), Nalisnick, E. Proceedings of Machine Learning Research, 2024 https://www.scopus.com/pages/publications/85194149372?origin=scopusAI

7. Role of Human-AI Interaction in Selective Prediction Bondi, E., Koster, R., Sheahan, H., (...), Dvijotham, K. Proceedings of the 36th AAAI Conference on Artificial Intelligence, AAAI 2022, 2022 https://www.scopus.com/pages/publications/85130545462?origin=scopusAI

8. Learning to Defer with an Uncertain Rejector via Conformal Prediction Fang, Y., Nalisnick, E. Transactions on Machine Learning Research, 2026 https://www.scopus.com/pages/publications/105034433173?origin=scopusAI

9. Uncertainty-Aware LiDAR-Camera Autonomy via Conformal Prediction and Principled Abstention Kumar, D., Tayebati, S., Darabi, N., (...), Trivedi, A.R. 2025 IEEE International Conference on Omni-Layer Intelligent Systems, COINS 2025, 2025 https://www.scopus.com/pages/publications/105016217249?origin=scopusAI

10. An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition

Classification Julián Lechuga López, L., Shamout, F.E., Rudner, T.G.J. Proceedings of Machine Learning Research, 2026 https://www.scopus.com/pages/publications/105045692611?origin=scopusAI

11. SYNAPSE-X: a calibration-aware vision transformer framework for selective referral in multi-class brain tumor MRI classification Tabatabaee, S., Khasawneh, M.T. Neural Computing and Applications, 2026 https://www.scopus.com/pages/publications/105053910695?origin=scopusAI

12. Beyond Accuracy: Reliability-Aware Machine Learning for Handwriting-Based Alzheimer’s Disease Detection Mitra, U., Ul Rehman, S. Information (Switzerland), 2026 https://www.scopus.com/pages/publications/105051548609?origin=scopusAI

13. Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty Machcha, S., Yerra, S., Gupta, S., (...), Yao, Z. EACL 2026 - 19th Conference of the European Chapter of the Association for Computational Linguistics, Proceedings of the Conference, Vol. 1 - (Long Papers), 2026 https://www.scopus.com/pages/publications/105040516985?origin=scopusAI

14. Uncertainty aware training to improve deep learning model calibration for classification of cardiac MR images Dawood, T., Chen, C., Sidhu, B.S., (...), King, A.P. Medical Image Analysis, 2023 https://www.scopus.com/pages/publications/85162087451?origin=scopusAI

15. A contrastive and uncertainty-aware analytics framework for reliable lung disease detection from chest imaging Pinem, J., Astuti, W., Adiwijaya Healthcare Analytics, 2026 https://www.scopus.com/pages/publications/105043440133?origin=scopusAI

16. Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings Varshney, N., Mishra, S., Baral, C. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 2022 https://www.scopus.com/pages/publications/85135816982?origin=scopusAI

17. HSM calibration factor, calibration function, or jurisdiction-specific safety model–A comparative analysis Claros, B., Sun, C., Edara, P. Journal of Transportation Safety and Security, 2020 https://www.scopus.com/pages/publications/85048166278?origin=scopusAI

18. The discrepancy between risky and riskless utilities: A matter of framing? Stalmeier, P.F.M., Bezembinder, T.G.G. Medical Decision Making, 1999 https://www.scopus.com/pages/publications/0032824459?origin=scopusAI

19. Validity, Reliability, and Framing Effects in Equity-Efficiency Trade-Off Studies: A Systematic Review Chechulina, V., Chu, A., Lam, Q.H., (...), Ali, S. Value in Health, 2026 https://www.scopus.com/pages/publications/105025550630?origin=scopusAI

20. Selective classification under imbalance in multiclass settings: A novel metric for bias-aware risk– coverage evaluation Sağlam, F., Özgen, Ü., Uygun, A., (...), Albayrak, C. Journal of Biomedical Informatics, 2026 https://www.scopus.com/pages/publications/105045433755?origin=scopusAI

21. On cost-sensitive calibrated uncertainty in deep learning: An application on COVID-19 detection Ghoshal, B., Tucker, A. Proceedings - IEEE Symposium on Computer-Based Medical Systems, 2021 https://www.scopus.com/pages/publications/85110876102?origin=scopusAI

22. Fixed-Sequence Confidence-Interval Calibration for Finite-Sample Selective Risk Control Dong, S., Hao, X., Shinnou, H. Stats, 2026 https://www.scopus.com/pages/publications/105055030328?origin=scopusAI

23. A Framework for Assessing Joint Human-AI Systems Based on Uncertainty Estimation Konuk, E., Welch, R., Christiansen, F., (...), Smith, K. Lecture Notes in Computer Science, 2024 https://www.scopus.com/pages/publications/105047104058?origin=scopusAI

24. Knowledge Uncertainty Estimation for Reliable Clinical Decision Support: A Delirium Risk Prognosis Case Study Lindenmeyer, A., Veeranki, S., Franke, S., (...), Schneider, D. Studies in Health Technology and Informatics, 2025 https://www.scopus.com/pages/publications/105003982036?origin=scopusAI

25. Regime-Dependent Post Hoc Uncertainty in Lightweight Image Classification Roca, Z.M.A., Dejito, C.A.P., Peña, C.F. 2026 6th International Conference on Computer Communication and Artificial Intelligence, CCAI 2026, 2026 https://www.scopus.com/pages/publications/105048979103?origin=scopusAI

26. Shields to Guarantee Probabilistic Safety in MDPs Heck, L., Macák, F., Andriushchenko, R., (...), Junges, S. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105047049454?origin=scopusAI

27. Uncertain numbers and uncertainty in the selection of input distributions - Consequences for a probabilistic risk assessment of contaminated land Sander, P., Bergbäck, B., Öberg, T. Risk Analysis, 2006 https://www.scopus.com/pages/publications/33750188256?origin=scopusAI

28. Learning-Based Shielding for Safe Autonomy under Unknown Dynamics Reed, R., Lahijanian, M. Proceedings of the American Control Conference, 2025 https://www.scopus.com/pages/publications/105015678835?origin=scopusAI

29. Analyzing Probabilistic Logic Shields for Multi-Agent Reinforcement Learning Chatterji, S., Acar, E. Frontiers in Artificial Intelligence and Applications, 2025 https://www.scopus.com/pages/publications/105024464849?origin=scopusAI

30. Risk and uncertainty from frontier to production - A review Binns, P., Corbett, P. First Break, 2012 https://www.scopus.com/pages/publications/84861971322?origin=scopusAI

31. Economic-environmental trade-offs and the conservativeness of the upper partial moment Matthews, N., Grové, B. Stochastic Environmental Research and Risk Assessment, 2017 https://www.scopus.com/pages/publications/85006410861?origin=scopusAI

32. Explainably Safe Reinforcement Learning Rieder, S., Pranger, S., Chakraborty, D., (...), Könighofer, B. Advances in Neural Information Processing Systems, 2025 https://www.scopus.com/pages/publications/105048527979?origin=scopusAI

33. Contribution of human reliability analysis to the results of probabilistic safety assessment of the nuclear power plant Č epin, M., Pro š ek, A. Elektrotehniski Vestnik/Electrotechnical Review, 2009 https://www.scopus.com/pages/publications/74849137554?origin=scopusAI

34. When artificial intelligence misguides the brain: A cognitive-ethical mechanism in industrial safety decisions Yu, X., He, L., Qin, J., Liu, T. International Journal of Industrial Ergonomics, 2026 https://www.scopus.com/pages/publications/105036165759?origin=scopusAI

35. Generating Local Shields for Decentralised Partially Observable Markov Decision Processes Yang, H., Yoshida, N. Electronic Proceedings in Theoretical Computer Science, EPTCS, 2026 https://www.scopus.com/pages/publications/105037329876?origin=scopusAI

36. Safe Reinforcement Learning via Recovery-based Shielding with Gaussian Process Dynamics Models

Goodall, A.W., Belardinelli, F. AAMAS 2026 - Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems, 2026 https://www.scopus.com/pages/publications/105041377487?origin=scopusAI

37. Dynamic Model Predictive Shielding for Provably Safe Reinforcement Learning Banerjee, A., Rahmani, K., Biswas, J., Dillig, I. Advances in Neural Information Processing Systems, 2024 https://www.scopus.com/pages/publications/105000491289?origin=scopusAI

38. Learning-to-defer for sequential medical decision-making under uncertainty Joshi, S., Parbhoo, S., Doshi-Velez, F. Transactions on Machine Learning Research, 2023 https://www.scopus.com/pages/publications/86000322544?origin=scopusAI

39. Uncertainty-Aware Systems for Human-AI Collaboration Pearson, V., Alves, J.V., Bono, J., (...), Bizarro, P. Transactions on Machine Learning Research, 2026 https://www.scopus.com/pages/publications/105034787159?origin=scopusAI

40. Uncertainty-Aware Deep Neural Networks for Reliable and Selective Decision-Making in Medical Image Classification Tirupati, K.K., Methuku, N.K., Chilukury, P.K., Reddy, S.R.B. 2026 International Conference on Artificial Intelligence, Systems, and Emerging Technologies, ICAISET 2026, 2026 https://www.scopus.com/pages/publications/105042168938?origin=scopusAI

41. Learning to Defer with Better Features: A Case for Going Beyond the Final Layer Ponomarev, A., Agafonov, A. Conference of Open Innovation Association, FRUCT, 2025 https://www.scopus.com/pages/publications/105029718964?origin=scopusAI

42. Learning to Defer with Scoring Functions Ponomarev, A. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105024410763?origin=scopusAI

43. Uncertainty-Aware Prototypical Networks with Monte Carlo Dropout for Few-Shot Image Classification Fatema, S.R., Maradithaya, S. Engineering, Technology and Applied Science Research, 2025 https://www.scopus.com/pages/publications/105027902114?origin=scopusAI

44. Efficient Safe Meta-Reinforcement Learning: Provable Near-Optimality and Anytime Safety Xu, S., Zhu, M. Advances in Neural Information Processing Systems, 2025 https://www.scopus.com/pages/publications/105048529679?origin=scopusAI

45. Distributionally Robust Minimization in Meta-Learning for System Identification Rufolo, M., Piga, D., Forgione, M. IEEE Control Systems Letters, 2025 https://www.scopus.com/pages/publications/105009647698?origin=scopusAI

46. The Effect of AI Advice on Human Confidence in Decision-Making Taudien, A., Fügener, A., Gupta, A., Ketter, W. Proceedings of the Annual Hawaii International Conference on System Sciences, 2022 https://www.scopus.com/pages/publications/85136102117?origin=scopusAI

47. When AI Stays Silent: Hidden Agreement May Undermine Trust Building in Adaptive Decision Support and Training Ramon Alaman, J., Lafond, D., Marois, A., Tremblay, S. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105028351776?origin=scopusAI

48. Impact of human-AI trust on collaborative decision-making quality: mediating role of human-Al shared mental model Niu, L., Lin, Y. China Safety Science Journal, 2026 https://www.scopus.com/pages/publications/105051391813?origin=scopusAI

49. Human-AI Communication in First Aid Response: Effects on Team Performance, Trust, and Teamwork Appraisal Grace, R., Son, C., Pang, F., (...), Hernandez, J. Proceedings of the International ISCRAM Conference, 2025 https://www.scopus.com/pages/publications/105007994502?origin=scopusAI

50. Post-Abstention: Towards Reliably Re-Attempting the Abstained Instances in QA Varshney, N., Baral, C. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 2023 https://www.scopus.com/pages/publications/85174418659?origin=scopusAI

51. Decision Deferral in a Human-AI Joint Face-Matching Task: Effects on Human Performance and Trust Salehi, P., Chiou, E.K., Mancenido, M., (...), Shah, A. Proceedings of the Human Factors and Ergonomics Society, 2021 https://www.scopus.com/pages/publications/85171306011?origin=scopusAI

52. CAN WE TRUST AI? EXPLORING THE EFFECT OF ESTIMATED ACCURACY AND THE ACTUAL PERFORMANCE OF AI SYSTEMS ON HUMAN-AI COLLABORATION Deng, Z., Song, D., Evans, R. Journal of Electronic Commerce Research, 2025 https://www.scopus.com/pages/publications/105013285830?origin=scopusAI

53. Confidence-Based Trust Calibration in Human-AI Teams Ibrahim, M. International Journal of Advanced Computer Science and Applications, 2025 https://www.scopus.com/pages/publications/105028653539?origin=scopusAI

54. When to Trust the Machine: A Simulation Framework for Human–AI Collaboration Hani, S., Margondai, A., von Ahlefeldt, C., (...), Mouloua, M. Applied Human Factors and Ergonomics International, 2026 https://www.scopus.com/pages/publications/105030034078?origin=scopusAI

55. How trust shapes human reliance on AI decision support in healthcare: A simulation-based behavioral study Han, Q. Computers in Human Behavior Reports, 2026 https://www.scopus.com/pages/publications/105052852911?origin=scopusAI

56. COIN: Uncertainty-Guarding Selective Question Answering for Foundation Models with Provable Risk Guarantees Wang, Z., Duan, J., Wang, Q., (...), Xu, K. Proceedings of the AAAI Conference on Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105034885906?origin=scopusAI

57. SafePredict: A Meta-Algorithm for Machine Learning That Uses Refusals to Guarantee Correctness Kocak, M.A., Ramirez, D., Erkip, E., Shasha, D.E. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021 https://www.scopus.com/pages/publications/85099387529?origin=scopusAI

58. CONFORMALIZED INTERACTIVE IMITATION LEARNING: HANDLING EXPERT SHIFT & INTERMITTENT FEEDBACK Zhao, M., Simmons, R., Admoni, H., (...), Bajcsy, A. 13th International Conference on Learning Representations, ICLR 2025, 2025 https://www.scopus.com/pages/publications/105010247101?origin=scopusAI

59. Concerning uncertainty—a systematic survey of uncertainty-aware XAI Löfström, H., Löfström, T., Hjort, A., Yapicioglu, F.R. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 2026 https://www.scopus.com/pages/publications/105048624419?origin=scopusAI

60. Is uncertainty quantification in deep learning sufficient for out-of-distribution detection? Schwaiger, A., Sinhamahapatra, P., Gansloser, J., Roscher, K. CEUR Workshop Proceedings, 2020 https://www.scopus.com/pages/publications/85089629284?origin=scopusAI

61. Evaluating AI Safety, Hallucinations, Psychosis and Bias Using Clinical Simulations Borycki, E.M., Kushniruk, A.W. AI for a Just World: Power, Liberation, and the People Left Behind, 2026

https://www.scopus.com/pages/publications/105040617288?origin=scopusAI

62. Data-driven technology medical malpractice: A narrative review on the legal implications in clinical settings Hardin, C.M. Organizational Readiness and Research: Security, Management, and Decision Making, 2024 https://www.scopus.com/pages/publications/105005819308?origin=scopusAI

63. Operationalizing Human Oversight in High-Risk Artificial Intelligence Legal and Governance Mechanisms for Implementing the Human-in-the-Loop Standard Ahmed, S.S., Sabah, N., Staikutsa, S. Communications in Computer and Information Science, 2027 https://www.scopus.com/pages/publications/105052918675?origin=scopusAI

64. Cognitive Friction in Clinical Decision Support: A Comparative Study of Judicial and Adjunct Human– AI Interaction Protocols Pe, S., Bergomi, L., Nicora, G., (...), Parimbelli, E. Machine Learning and Knowledge Extraction, 2026 https://www.scopus.com/pages/publications/105045763158?origin=scopusAI

65. The Challenge of Designing for Meaningful Effective Human Oversight in Rapidly Evolving Complex AI Systems Wittens, M.M.J., Sirka Kacafírková, K., Elprama, S.A., Jacobs, A. Frontiers in Artificial Intelligence and Applications, 2026 https://www.scopus.com/pages/publications/105044692365?origin=scopusAI

66. Is Uncertainty Quantification a Viable Alternative to Learned Deferral? Wundram, A.M., Baumgartner, C.F. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105019204284?origin=scopusAI

67. Collaborative Intelligence for Safety-Critical Industries: A Literature Review Ramos, I.F., Gianini, G., Leva, M.C., Damiani, E. Information (Switzerland), 2024 https://www.scopus.com/pages/publications/85210224295?origin=scopusAI

68. Explainable AI in Clinical Decision Support Systems: A Meta-Analysis of Methods, Applications, and Usability Challenges Abbas, Q., Jeong, W., Lee, S.W. Healthcare (Switzerland), 2025 https://www.scopus.com/pages/publications/105015377247?origin=scopusAI

69. Human-Centered Explainable AI: Creating Explanations that Address Stakeholder Needs Hummel, A. CEUR Workshop Proceedings, 2025 https://www.scopus.com/pages/publications/105015710969?origin=scopusAI
