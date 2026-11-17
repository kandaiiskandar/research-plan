---
source_pdf: "Search 3 Empirical Measurement of Runtime AI Safety Mechanism Activation- Mechanisms, Metrics, Risk Levels, and Evaluation Settings.pdf"
source_sha256: "610cbb747cf56f219914f4a77f3582f508f531c422e84ac30c8481d848d3f52e"
source_pages: 7
scopus_ai_generated: "Wed Sep 23 2026"
query: "Empirical studies on AI safety mechanisms"
report_title: "Empirical Measurement of Runtime AI Safety Mechanism Activation: Mechanisms, Metrics, Risk Levels, and Evaluation Settings Quick Reference"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Empirical studies on AI safety mechanisms

## Key Findings Table

| Study/Benchmark/Framework | Mechanism Type(s) | Trigger(s) | What is Restricted/Intervened | Activation Frequency Metric(s) | Dataset/Eval Setting | Risk Levels? | Marginal Effect Isolated? | Notes/Citations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SA-ROC (Safety-Aware ROC) | Safety filter, abstention | Model uncertainty, low confidence | Autonomous action, triggers human review | Gray Zone Area (ΓArea), Rule-in/out rates | Clinical AI, LLMs, medical imaging | Yes | Yes (via ΓArea) | 1 |
| DSA-SafetyBench | Shielding, action restriction | Event-triggered, unsafe state | Unsafe actions, system transitions | Decision-level metrics, false alarm rate, multi-seed paired-bootstrap | Power grid, dynamic security assessment | Yes | Yes | 2 3 |
| VerifAI, iHMMs, RTAEval | Runtime assurance, shielding | Formal property violation, unsafe state | System actions, controller switching | Diagnostic coverage, intervention rate, mission success | Autonomous vehicles, aviation, robotics | Yes | Partial | 4 5 6 |
| LLM Abstention Benchmarks | Abstention, fallback | Low confidence, misalignment | Model output, refusal to answer | Safe/unsafe success rate, interception rate | LLMs, prompt datasets | Yes | Partial | 7 8 |
| Automotive ISO 26262 + AI | Safety filter, fallback | Fault detection, adversarial input | System operation, controller override | Diagnostic coverage, fault recovery time | Hardware-in-the-loop, real-world driving | Yes | Partial | 9 |
| Human-in-the-loop (HITL) | Advisory restriction, fallback | Uncertainty, operator workload | AI decision, triggers human review | Intervention rate, override frequency, workload metrics | Clinical decision support, control rooms | Yes | Yes (workload-adaptive) | 10 11 |
| UnsafeBench | Safety filter | Unsafe content detected | Model output, content restriction | Activation rate, false positive/negative | Image classification, curated datasets | Yes | No | 12 |
| LabSafety Bench | Safety filter, action restriction | Hazard/risk detected | Model output, action restriction | Correct/incorrect intervention rate | Laboratory safety, multiple-choice | Yes | No | 13 |

## Direct Answer

Empirical studies measure activation frequency of runtime AI safety mechanisms using metrics such as the Gray Zone Area (ΓArea) in SA-ROC, decision-level and event-triggered metrics in DSA-SafetyBench, diagnostic coverage in automotive and robotics settings, and safe/unsafe success rates in LLM controllers. Datasets and evaluation settings include simulation benchmarks, real-world autonomous vehicle data, clinical decision support logs, and curated adversarial or hazardous scenario datasets. Risk stratification is common, and some studies isolate the marginal effect of intermediate restrictions by comparing activation frequencies and false alarm rates under different constraint levels, though consistent isolation remains a methodological challenge across the literature[1][2][14] [15].

## Study Scope

**Time Period:** 2017–2024 (focus on recent empirical and benchmark-driven studies) **Disciplines:** Autonomous vehicles, robotics, clinical AI, LLMs, industrial control, human factors, regulatory science **Methods:** Simulation, hardware-in-the-loop, formal verification, human-in-the-loop experiments, adversarial stress testing, regulatory analysis

## Assumptions & Limitations

Most studies focus on high-risk, safety-critical domains; generalization to low-risk or consumer AI is limited. Marginal effects of intermediate restrictions are often not isolated in a standardized way. Human factors and organizational accountability are underrepresented in technical benchmarks. Datasets and evaluation settings are often domain-specific, limiting cross-domain comparability.

## Suggested Further Research

Develop unified, cross-domain benchmarks for activation frequency and marginal effect isolation. Integrate human factors and organizational accountability metrics into technical evaluation frameworks. Standardize reporting of activation triggers, intervention types, and risk stratification. Explore regulatory-aligned calibration of intermediate restrictions in empirical settings.

## 1. Introduction

Runtime AI safety mechanisms—such as safety filters, shielding, runtime assurance, action restriction, advisory restriction, fallback, and abstention—are increasingly critical for mitigating risks in safety-critical AI applications. Empirical measurement of how often these mechanisms become active is essential for understanding their effectiveness, operational cost, and the trade-offs between safety and autonomy. This report synthesizes empirical evidence on the activation frequency of runtime AI safety mechanisms, the metrics and datasets used, and the role of risk stratification and intermediate restrictions in shaping safety outcomes[14][16][17].

## Scope and Motivation

The motivation for this synthesis is twofold: (1) to bridge the gap between theoretical safety assurance and practical, measurable safety outcomes in deployed AI systems, and (2) to inform the design of robust, risk-aware safety architectures that can adapt to uncertainty and evolving operational contexts[14][16][17]. The report covers empirical studies across autonomous vehicles, robotics, clinical AI, LLMs, and industrial control, with a focus on mechanisms, triggers, restrictions, activation metrics, datasets, risk levels, and the marginal effects of intermediate restrictions.

## 2. Types of Runtime AI Safety Mechanisms

## 2.1 Taxonomy and Functional Characteristics

Empirical studies and systematic reviews identify a broad taxonomy of runtime AI safety mechanisms: **Safety Filters:** Constrain system actions to provably safe sets, often using formal verification or data-driven boundaries[18][19]. **Shielding:** Interpose a safety layer that monitors and overrides unsafe actions, typically in reinforcement learning or control systems[4][6]. **Runtime Assurance:** Switches between high-performance (possibly untrusted) and certified safe controllers based on runtime monitoring[5][6]. **Action/Advisory Restriction:** Limits or flags actions for human review based on uncertainty or risk[1][20]. **Fallback:** Activates a safe, conservative mode or halts operation when risk thresholds are exceeded[8][21]. **Abstention:** Refuses to act or answer when confidence is low or alignment is uncertain, especially in LLMs[7][8]. **Human-in-the-Loop (HITL):** Triggers human intervention or review in ambiguous or high-risk situations[10][11]. These mechanisms are often layered in defense-in-depth architectures, with activation triggers ranging from formal property violations to statistical uncertainty and human workload thresholds[22][23].

## 2.2 Design and Implementation Differences

**Shielding** is typically event-triggered and operates at the control/action level, often in RL or robotics. **Fallback** mechanisms are designed for fail-operational safety, activating when primary systems or human drivers are unable to maintain safe operation[21]. **Abstention** in LLMs and classifiers is triggered by low model confidence or misalignment with human values, and is empirically evaluated using safe/unsafe success rates and interception metrics[7][8]. **Runtime assurance** frameworks (e.g., Simplex, RTAEval) use formal monitors to switch between controllers, with triggers based on runtime property violations or uncertainty estimates[6].

## 2.3 Formal Runtime Monitoring Tools

**VerifAI:** Generates formal runtime monitors for AI/ML-based autonomous systems, validated in aviation and robotics[5]. **Interval Hidden Markov Models (iHMMs):** Predict safety violations in autonomous systems, outperforming model-free monitors[4]. **RTAEval:** Low-code framework for evaluating runtime assurance logics across agent types and scenarios[6].

**BIP, Petri Nets:** Used for runtime verification and predictive fault management in robotics and industrial control[24][25].

## 2.4 Integrated Safety Architectures and Human Oversight

**Layered Control Architectures:** Combine technical safeguards, governance, and human oversight for defense-in-depth[22]. **Human-in-the-Loop:** Empirically shown to improve safety outcomes, especially when adaptive to workload and context[10][11]. **Organizational Accountability:** Embedded through continuous monitoring, clear ownership, and escalation protocols[23][26]. **Synthesis:** The diversity of mechanisms and triggers reflects the complexity of runtime AI safety. Empirical studies increasingly favor integrated, multi-modal architectures that combine technical, human, and organizational controls[1][2][4].

## 3. Measurement Metrics and Activation Frequency

## 3.1 Metrics for Activation Frequency and Intervention

**SA-ROC (Safety-Aware ROC):** Defines Rule-in, Rule-out, and Gray Zones; Gray Zone Area (ΓArea) quantifies the operational cost of indecision (i.e., how often human review is triggered)[1]. **DSA-SafetyBench:** Uses decision-level, event-triggered, and multi-seed paired-bootstrap metrics to measure activation frequency, false alarm rates, and the impact of intermediate restrictions[2][3]. **Diagnostic Coverage:** Percentage of faults detected and recovered by safety mechanisms, used in automotive and robotics[9]. **Safe/Unsafe Success Rate (SSR/USR):** Used in LLMs and RL agents to measure how often safety interventions prevent unsafe actions[27]. **Intervention/Override Rate:** Frequency of human or automated intervention, often measured in HITL and clinical decision support systems[10][28]. **Statistical Distance/Non-parametric Measures:** Capture continuous changes in model behavior, improving over binary threshold methods[29][30].

## 3.2 Benchmarks and Evaluation of Intermediate Restrictions

**DSA-SafetyBench and SA-ROC** both empirically measure the effect of intermediate restrictions (e.g., uncertainty thresholds, event-triggered screening) on activation frequency and false alarm rates[2][3]. **Gray Zone Area** in SA-ROC isolates the marginal effect of requiring human review in ambiguous cases, quantifying the trade-off between safety and operational cost[1]. **Multi-seed, physics-aware metrics** in DSA-SafetyBench allow robust estimation of activation frequency under varying operational conditions[2].

## 3.3 Marginal Effects of Intermediate Restrictions

**Isolation of Marginal Effects:** Some studies explicitly compare activation frequency and safety outcomes with and without intermediate restrictions (e.g., different uncertainty thresholds, event-triggered vs. continuous monitoring)[31][32]. **Human-in-the-loop studies** measure the effect of workload-adaptive intervention policies on activation frequency and safety outcomes[10][11]. **Regulatory frameworks** (e.g., EU AI Act) motivate calibration of restrictions based on risk severity and uncertainty, with empirical support from simulation and risk assessment studies[15][33]. **3.4 Continuous Monitoring: Statistical and Non-Parametric Approaches** **Statistical distance measures** (e.g., empirical CDFs) enable continuous, nuanced monitoring of activation frequency, capturing subtle shifts in model behavior [30]. **Non-parametric methods** are robust to distributional assumptions and support real-time adaptation, though with lower statistical power[29]. **Continuous monitoring** is increasingly favored over binary thresholding for early detection and intervention[34]. **Synthesis:** Empirical measurement of activation frequency is increasingly sophisticated, leveraging event-triggered, decision-level, and continuous metrics. Isolation of marginal effects is possible but not yet standardized across domains[1][2][30].

## 4. Evaluation Settings and Datasets

## 4.1 Scenario-Driven Datasets and Simulation Environments

**Robotic Control Tasks:** Cart-pole, bipedal locomotion, F1Tenth autonomous racing, underwater navigation[19][35][36]. **Autonomous Vehicles:** Hardware-in-the-loop, real-world driving data, accident databases[9][37]. **Image Safety:** UnsafeBench (curated real and synthetic images with unsafe categories)[12]. **Laboratory Safety:** LabSafety Bench (hazard identification, risk assessment, consequence prediction)[13].

**Formal Verification:** VerifAI, high-fidelity simulators for aviation and robotics[5][38]. **Adversarial Stress Testing:** AttaX-Multimodal, TAEFuzz, ParasiteNet[39][40][41]. **Safe RL Benchmarks:** Offline safe RL datasets, CMDPs, OSRL[42][43].

## 4.2 Human-AI Interaction and Experimental Setups

**Clinical Decision Support:** Alert override rates, intervention logs, workload metrics[10][28]. **Human-AI Decision Time:** HCCD-DS v2, decisionTime frameworks[44][45]. **Operator Workload:** Eye tracking, EEG, process logs in control rooms[46][47].

## 4.3 Formal Tools and Real-World Validation

**VerifAI, iHMMs, RTAEval:** Used in both simulation and real-world deployments for runtime assurance validation[5][6][38]. **Hardware-in-the-loop:** Validates diagnostic coverage and fault recovery in automotive and robotics[9].

## 4.4 Stress Testing and Adversarial Evaluation

**Adversarial Benchmarks:** AttaX-Multimodal, TAEFuzz, ParasiteNet[39][40][41]. **Incident Analysis:** Used to estimate activation frequency under adversarial or perturbed conditions[48][49]. **Synthesis:** Evaluation settings are diverse, with a trend toward scenario-driven, high-fidelity, and adversarially robust benchmarks. Human factors and real-world deployment are increasingly represented but remain less standardized[19][38][44].

## 5. Risk Levels and Marginal Effects of Restrictions

## 5.1 Risk Categorization and Activation Frequency

**Risk Levels:** AI applications are categorized from minimal to high risk, with high-risk systems requiring stricter oversight and more frequent activation of safety mechanisms[14]. **Risk Frameworks:** EU AI Act, Failure Mode and Effect Analysis (FMEA), and Lorenz curve-based metrics are used for risk stratification[50][51]. **Incident Analysis:** Reveals that high-risk cases (e.g., physical harm, loss of life) have higher activation frequencies and stricter safety requirements[52]. **5.2 Calibration of Intermediate Restrictions in Regulatory Frameworks** **Regulatory Calibration:** Intermediate restrictions (e.g., uncertainty thresholds, human review requirements) are calibrated based on risk severity and uncertainty, as in the EU AI Act[15][33]. **Uncertainty Quantification:** Empirically shown to improve reliability and reduce unnecessary interventions in high-risk settings[53]. **Defense-in-Depth:** Multi-layered restrictions empirically reduce residual risk in high-stakes environments[33].

## 5.3 Marginal Effects in Multi-Risk-Level Systems

**Empirical Isolation:** Some studies compare activation frequency and safety outcomes before and after applying intermediate restrictions, using benchmarks like DSA-SafetyBench and SA-ROC[2]. **Integrated Assurance:** Emphasizes the need for holistic frameworks that combine technical, organizational, and regulatory controls to manage marginal effects [31][54]. **Human-in-the-Loop:** Workload-adaptive policies empirically reduce unnecessary interventions while preserving responsiveness to critical events[10][11].

## 5.4 Human Oversight and Accountability

**Human Factors:** Training, fatigue, and workload significantly influence the effectiveness and timing of safety interventions[10][11]. **Parallel Safety Systems:** Independent safety monitors improve accountability and resilience, especially in high-risk environments[55]. **Dynamic Safety Cases:** Incorporate runtime data and adapt to new knowledge, supporting ongoing assurance but introducing sociotechnical challenges[56]. **Synthesis:** Risk stratification and regulatory calibration are central to effective safety mechanism activation. Empirical evidence supports the value of intermediate restrictions and human oversight, but standardization and integration remain research challenges[2][11][15].

## 6. Discussion and Future Directions

## 6.1 Research Gaps and Limitations

**Benchmarking Gaps:** Lack of standardized, cross-domain benchmarks for activation frequency and marginal effect isolation[57][58]. **Reporting Inconsistency:** Heterogeneity in reporting triggers, interventions, and risk levels complicates meta-analysis[57][58]. **Human Factors:** Underrepresented in technical benchmarks; need for integration with organizational and regulatory metrics[10][11]. **Marginal Effects:** Isolation of intermediate restriction effects is often ad hoc and not standardized[2].

## 6.2 Recommendations for Future Research

**Unified Evaluation Frameworks:** Develop benchmarks that integrate formal methods, continuous statistical monitoring, and human-factor assessments[54][57]. **Standardized Reporting:** Require explicit reporting of mechanism type, trigger, restriction, activation metric, dataset, risk level, and marginal effect isolation. **Regulatory Alignment:** Empirically test regulatory frameworks (e.g., EU AI Act) in real-world and simulation settings to calibrate intermediate restrictions. **Human-in-the-Loop Integration:** Expand empirical studies on workload-adaptive and accountability-driven safety interventions. **Cross-Domain Synthesis:** Bridge technical, organizational, and regulatory perspectives for holistic safety assurance.

## Synthesis and Real-World Implications

Empirical research on runtime AI safety mechanisms reveals a rich landscape of technical, human, and organizational controls. Activation frequency is increasingly measured using sophisticated, scenario-driven, and risk-aware metrics. While integrated architectures and regulatory frameworks are emerging, there is a pressing need for standardized benchmarks, unified reporting, and deeper integration of human factors. Real-world deployment in high-risk domains (e.g., autonomous vehicles, clinical AI) demonstrates both the promise and the complexity of runtime safety assurance. Future research should focus on developing robust, cross-domain methodologies that can adapt to evolving risks, operational contexts, and regulatory requirements[1][15][16][54].

**Table and section references correspond to detailed empirical findings and meta-analytical evidence from the synthesized literature**[1][2][4][11][15][16] [19].

## References

1. Defining operational safety in clinical artificial intelligence systems Kim, Y.-T., Kim, H., Bahl, M., (...), Do, S. npj Digital Medicine, 2026 https://www.scopus.com/pages/publications/105035569244?origin=scopusAI

2. DSA-SafetyBench: A safety-aware benchmark for artificial-intelligence-based dynamic security assessment in energy systems Shamseldein, M. Energy and AI, 2026 https://www.scopus.com/pages/publications/105042250249?origin=scopusAI

3. Safety risk assessment of wharf construction based on combined weighting and cloud model Hu, S., Zhang, Y., Sheng, X., Mao, X. Journal of Safety and Environment, 2026 https://www.scopus.com/pages/publications/105043618523?origin=scopusAI

4. Learning Robust Markov Models for Safe Runtime Monitoring Skurka, A., van der Maas, L., Junges, S., Torfah, H. AAMAS 2026 - Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems, 2026 https://www.scopus.com/pages/publications/105041373777?origin=scopusAI

5. Formal Analysis of AI-Based Autonomy: From Modeling to Runtime Assurance Torfah, H., Junges, S., Fremont, D.J., Seshia, S.A. Lecture Notes in Computer Science, 2021 https://www.scopus.com/pages/publications/85117473078?origin=scopusAI

6. RTAEval: A Framework for Evaluating Runtime Assurance Logic Miller, K., Zeitler, C.K., Shen, W., (...), Mitra, S. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85176002441?origin=scopusAI

7. Know Your Limits: A Survey of Abstention in Large Language Models Wen, B., Yao, J., Feng, S., (...), Wang, L.L. Transactions of the Association for Computational Linguistics, 2025 https://www.scopus.com/pages/publications/105011522141?origin=scopusAI

8. Certifiers Make Neural Networks Vulnerable to Availability Attacks Lorenz, T., Kwiatkowska, M., Fritz, M. AISec 2023 - Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security, 2023 https://www.scopus.com/pages/publications/85179583230?origin=scopusAI

9. AI-Enhanced Functional Safety in ADAS Controllers: Predictive Fault Management under ISO 26262 Abdul Karim, A.S. SAE Technical Papers, 2026 https://www.scopus.com/pages/publications/105036838026?origin=scopusAI

10. Adaptive Human Oversight for Maritime Agentic AI Systems: Balancing Operator Workload and Safety Through Risk-Aware Governance Miller, T., Durlik, I., Biczak, P. Applied Sciences (Switzerland), 2026 https://www.scopus.com/pages/publications/105045853571?origin=scopusAI

11. Reasoning about Human Participation in Self-Adaptive Systems Cámara, J., Moreno, G., Garlan, D. Proceedings - 10th International Symposium on Software Engineering for Adaptive and Self-Managing Systems, SEAMS 2015, 2015 https://www.scopus.com/pages/publications/84953339677?origin=scopusAI

12. UnsafeBench: Benchmarking Image Safety Classifiers on Real-World and AI-Generated Images Qu, Y., Shen, X., Wu, Y., (...), Zhang, Y. CCS 2025 - Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security, 2025 https://www.scopus.com/pages/publications/105023877360?origin=scopusAI

13. Benchmarking large language models on safety risks in scientific laboratories Zhou, Y., Yang, J., Huang, Y., (...), Zhang, X. Nature Machine Intelligence, 2026 https://www.scopus.com/pages/publications/105027566731?origin=scopusAI

14. Risk, regulation, and governance: evaluating artificial intelligence across diverse application scenarios Szadeczky, T., Bederna, Z. Security Journal, 2025 https://www.scopus.com/pages/publications/105007148824?origin=scopusAI

15. Uncertainty-Calibrated Safety Gating for Vision–Language– Action Manipulation Under Domain Shift: Reliability Gains and Intervention–Efficiency Trade- Offs Ghaleb, A.M., Allahloh, A.S., Mejjaouli, S., (...), Al-Shayea, A. Sensors, 2026 https://www.scopus.com/pages/publications/105040252138?origin=scopusAI

16. Systematic Review on AI Safety and Future Research Agenda Zhang, S., Lu, H. 2025 7th International Conference on System Reliability and Safety Engineering, SRSE 2025, 2025 https://www.scopus.com/pages/publications/105032891078?origin=scopusAI

17. Designing AI to Prevent Harm (Safety) Andrae, S. AI Safety and Preventing Harm in AI Systems, 2026 https://www.scopus.com/pages/publications/105031334967?origin=scopusAI

18. Safety filters as a means for ensuring functional safety in data-driven control: an overview Hess, M., Piscol, B.-M., Bohn, C., Hohmann, S. At- Automatisierungstechnik, 2026 https://www.scopus.com/pages/publications/105040974990?origin=scopusAI

19. Constraint-Guided Online Data Selection for Scalable Data-Driven Safety Filters in Uncertain Robotic Systems Choi, J.J., Castañeda, F., Jung, W., (...), Sreenath, K. IEEE Transactions on Robotics, 2025 https://www.scopus.com/pages/publications/105007624568?origin=scopusAI

20. Runtime Assurance for Intelligent Cyber-Physical Systems Dementyeva, V., Hickert, C., Sarfaraz, N., (...), Sookoor, T. Proceedings - 13th ACM/IEEE International Conference on Cyber-Physical Systems, ICCPS 2022, 2022 https://www.scopus.com/pages/publications/85134207376?origin=scopusAI

21. Strategy for the limits of automated driving terminal stop, system shut down – all out please? Peters, B., Khalil, M., Rink, K., Kern, S. VDI Berichte, 2017 https://www.scopus.com/pages/publications/85105958152?origin=scopusAI

22. Layered Control Architectures for AI Safety: A Cybersecurity-Oriented Systems Framework Choi, Y.B., Hong, P.C., Park, Y.S. Systems, 2026 https://www.scopus.com/pages/publications/105036813457?origin=scopusAI

23. Towards Responsible Ai in Safety-Critical Human-Machine Systems: A Literature-Based Governance Framework Panner, E., Scheffer, S., Matyas, K. 2026 IEEE International Conference on Human-Machine Systems, ICHMS 2026, 2026 https://www.scopus.com/pages/publications/105045585962?origin=scopusAI

24. Runtime Verification of Timed Properties in Autonomous Robots Foughali, M., Bensalem, S., Combaz, J., Ingrand, F. 2020 18th ACM-IEEE International Conference on Formal Methods and Models for System Design, MEMOCODE 2020, 2020 https://www.scopus.com/pages/publications/85100685120?origin=scopusAI

25. Predictive Runtime Verification of Skill-based Robotic Systems using Petri Nets Pelletier, B., Lesire, C., Grand, C., (...), Rognant, M. Proceedings - IEEE International Conference on Robotics and Automation, 2023 https://www.scopus.com/pages/publications/85168712012?origin=scopusAI

26. Human -in-theLoop Frameworks for AI Mitigation and Accountability Kushwaha, A., Nair, N.R., Sharma, K., (...), Sharma, R. Hallucination-Aware AI for Truthful and Aligned Systems, 2026 https://www.scopus.com/pages/publications/105039711847?origin=scopusAI

27. The Verifier Tax: Horizon Dependent Safety - Success Tradeoffs in Tool Using LLM Agents Sah, T., Srivastava, V., Sah, D., Jordan, K. Proceedings of the ACM Conference on AI and Agentic Systems, CAIS 2026, 2026 https://www.scopus.com/pages/publications/105046431304?origin=scopusAI

28. Medication Errors and Patient Safety: Evaluation of Physicians' Responses to Medication-Related Alert Overrides in Clinical Decision Support Systems Justinia, T., Qattan, W., Almenhali, A., (...), Alharbi, T. Acta Informatica Medica, 2021 https://www.scopus.com/pages/publications/85122138627?origin=scopusAI

29. Extensions of multinomial processing tree models for continuous variables: A simulation study comparing parametric and non-parametric approaches Gutkin, A., Heck, D.W. Behavior Research Methods, 2026 https://www.scopus.com/pages/publications/105024145741?origin=scopusAI

30. Toward Improving Confidence in Autonomous Vehicle Software: A Study on Traffic Sign Recognition Systems Aslansefat, K., Kabir, S., Abdullatif, A., (...), Papadopoulos, Y. Computer, 2021 https://www.scopus.com/pages/publications/85111955117?origin=scopusAI

31. A Review of Model Uncertainty, Cyber–Physical Threats and Assurance Frameworks for Safety-Critical AI in Process Industries Devarajan, Y., Acharya, S.K., Jakhar, S.K., (...), Mehar, K. IET Cyber-Physical Systems: Theory and Applications, 2026 https://www.scopus.com/pages/publications/105046601259?origin=scopusAI

32. A Hybrid FMEA-AHP Framework for Risk Prioritization in Nontransparent Artificial Intelligence Systems Gonçalves, H.O., Amaral, R., Pereira, J.C. Risk Analysis, 2026 https://www.scopus.com/pages/publications/105043508918?origin=scopusAI

33. Defense-in-Depth Management of Radioactive Atmospheric Emissions in an Urban Medical Cyclotron Facility Montero-Díaz, F., Torres-Valle, A., Jauregui- Haza, U. Technologies, 2026 https://www.scopus.com/pages/publications/105040122541?origin=scopusAI

34. AI Safety Assurance for Automated Vehicles: A Survey on Research, Standardization, Regulation Ullrich, L., Buchholz, M., Dietmayer, K., Graichen, K. IEEE Transactions on Intelligent Vehicles, 2025 https://www.scopus.com/pages/publications/105021531239?origin=scopusAI

35. A Hierarchical Approach for Strategic Motion Planning in Autonomous Racing Reiter, R., Hoffmann, J., Boedecker, J., Diehl, M. 2023 European Control Conference, ECC 2023, 2023 https://www.scopus.com/pages/publications/85166469663?origin=scopusAI

36. A safety framework for autonomous underwater vehicle navigation based on safety-constrained reinforcement learning Huang, J., Liu, T., Zhao, J., (...), Li, Z. Engineering Applications of Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105044158593?origin=scopusAI

37. AI-Based Vehicle Safety and Functional Safety Standards in Autonomous Cars: A Use Case in Safety-Critical Systems Chokshi, K., Shaik, Y.A., Yadav, P., (...), Rajamandrapu, A.K. 2025 IEEE 4th World Conference on Applied Intelligence and Computing, AIC 2025, 2025 https://www.scopus.com/pages/publications/105023641714?origin=scopusAI

38. Verification and Validation of a Vision-Based Landing System for Autonomous VTOL Air Taxis Bansal, A., Wang, D., Yeghiazaryan, M., (...), Hovakimyan, N. AIAA Science and Technology Forum and Exposition, AIAA SciTech Forum 2025, 2025 https://www.scopus.com/pages/publications/86000031694?origin=scopusAI

39. AttaX-Multimodal: End-to-End Evaluation of Multimodal AI Safety with Threatscore and Resiliencescore Karne, R. International Conference on Connected Intelligence for Industrial Applications, CI2A 2026, 2026 https://www.scopus.com/pages/publications/105044847735?origin=scopusAI

40. TAEFuzz: Automatic Fuzzing for Image-based Deep Learning Systems via Transferable Adversarial Examples Ji, S., Huang, C., Ren, B., (...), Zhang, P. Lecture Notes in Informatics (LNI), Proceedings - Series of the Gesellschaft fur Informatik (GI), 2026 https://www.scopus.com/pages/publications/105045457072?origin=scopusAI

41. Parasitenet: A Modular Trigger-Responsive Framework for Latent-Space Corruption in Neural Networks Patel, A.P., Patel, M.J., Soni, R.R., (...), Patel, S.M. 2025 17th IEEE International Conference on Computational Intelligence and Communication Networks, CICN 2025, 2025 https://www.scopus.com/pages/publications/105034661602?origin=scopusAI

42. Game-Theoretic Constrained Policy Optimization for Safe Reinforcement Learning Zhang, C., Zhang, X., Lan, Y., (...), Xu, X. IEEE Transactions on Neural Networks and Learning Systems, 2025 https://www.scopus.com/pages/publications/105011736046?origin=scopusAI

43. VQ-SSR: Offline Safe Reinforcement Learning via Discrete Skill Quantization Hou, D., Yang, Y., Zhang, J., Wu, W. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105046482448?origin=scopusAI

44. HCCD-DS v2: a transparent synthetic benchmark for human–AI decision support under contextual uncertainty Kesgin, K. Scientific Reports, 2026 https://www.scopus.com/pages/publications/105046549443?origin=scopusAI

45. "decisionTime": A Configurable Framework for Reproducible Human-AI Decision-Making Studies Salimzadeh, S., Gadiraju, U. UMAP 2024 - Adjunct Proceedings of the 32nd ACM Conference on User Modeling, Adaptation and Personalization, 2024 https://www.scopus.com/pages/publications/85198940138?origin=scopusAI

46. Decision support impact and error prediction in control room: A behavioural data analysis Amazu, C.W., Mietkiewicz, J., Abbas, A.N., (...), Leva, M.C. Reliability Engineering and System Safety, 2026 https://www.scopus.com/pages/publications/105033556990?origin=scopusAI

47. Analyzing Operator States and the Impact of AI-Enhanced Decision Support in Control Rooms: A Human-in-the-Loop Specialized Reinforcement Learning Framework for Intervention Strategies Abbas, A.N., Amazu, C.W., Mietkiewicz, J., (...), Leva, M.C. International Journal of Human-Computer Interaction, 2025 https://www.scopus.com/pages/publications/85203065482?origin=scopusAI

48. A Survey on Adversarial Attacks and Defense Mechanisms in Artificial Intelligence Pandey, A.S.R., Udyavar, S.K., Varma, A., (...), Padmavathi, S. 17th International Conference on Advances in Computing, Control, and Telecommunication Technologies, ACT 2026, 2026 https://www.scopus.com/pages/publications/105047261840?origin=scopusAI

49. Adversarial Machine Learning in Healthcare: Risks to AI-Driven Diagnostics and Treatment Plans Soberano, K.T., Condes, K.A. International Journal of Statistics in Medical Research, 2025 https://www.scopus.com/pages/publications/105024379732?origin=scopusAI

50. High-Risk AI Systems Szostek, D., Prabucki, R.T. Law, Governance and Technology Series, 2025 https://www.scopus.com/pages/publications/105020419549?origin=scopusAI

51. AI Risk Measurement Giudici, P. Handbook of Human-Centered Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105043223635?origin=scopusAI

52. Risk Management Framework-Based Failure Mode and Effect Analysis for AI Risk Assessment Anang, Y., Suadaa, L.H., Maghfiroh, L.R., (...), Watanabe, Y. Advances in Technology Innovation, 2025 https://www.scopus.com/pages/publications/105019223111?origin=scopusAI

53. The Role of Uncertainty Quantification for Trustworthy AI Deuschel, J., Foltyn, A., Roscher, K., Scheele, S. Unlocking Artificial Intelligence: From Theory to Applications, 2024 https://www.scopus.com/pages/publications/85211889843?origin=scopusAI

54. Towards risk-aware artificial intelligence and machine learning systems: An overview Zhang, X., Chan, F.T.S., Yan, C., Bose, I. Decision Support Systems, 2022 https://www.scopus.com/pages/publications/85129983675?origin=scopusAI

55. Artificial intelligence (AI) safety system for safe & trustworthy autonomy Thakur, R., Sajid, Z., Khan, F. Digital Chemical Engineering, 2026 https://www.scopus.com/pages/publications/105035625605?origin=scopusAI

56. Safe autonomous systems in a changing world: Operationalising dynamic safety cases Buysse, L., Habli, I., Vanoost, D., Pissoort, D. Safety Science, 2025 https://www.scopus.com/pages/publications/105013537295?origin=scopusAI

57. Role of artificial intelligence in patient safety outcomes: Systematic literature review Choudhury, A., Asan, O. JMIR Medical Informatics, 2020 https://www.scopus.com/pages/publications/85097462126?origin=scopusAI

58. Artificial Intelligence for Drug Safety Across the Lifecycle and Decision Type: A Scoping Review Kim, T.W., Park, S., Kim, M. Pharmaceuticals, 2026 https://www.scopus.com/pages/publications/105031112365?origin=scopusAI
