---
source_pdf: "search 6 Empirical Measurement of AI Governance Controls.pdf"
source_sha256: "4ce9b5df5921619c0e057272bc47a7e8a98b9710ca13607a9a2bb4275c10fd3d"
source_pages: 13
scopus_ai_generated: "Wed Sep 23 2026"
query: "AI governance and system behavior measurement"
report_title: "Empirical Measurement of AI Governance Controls: Operational Impact, Methods, and Outcomes Quick Reference"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# AI governance and system behavior measurement

## Key Findings Table

| Aspect | Empirical Evidence & Methods | Controls Measured | Outcome Types Measured | Comparator Used? | Key References |
| --- | --- | --- | --- | --- | --- |
| Conceptual vs. Technical Frameworks | Quasi-natural experiments, case studies, runtime architectures distinguish technical enforcement from conceptual frameworks | Technical (runtime monitors, LTL), Bureaucratic, Organizational | Action restriction, intervention, abstention, permitted capabilities | Yes (DID, PSM, prompt-based, etc.) | 1 2 3 |
| Causal Impact of Governance Controls | DID regression, fuzzy DEMATEL, process mining, digital twin modeling | Transparency, cybersecurity, risk, explainability, human oversight | Corporate performance, risk reduction, compliance, trust | Yes | 1 4 |
| Runtime Measurement & Activation | A4-Gov, Legitimacy Layer, LTL-based monitors, audit trail analysis | Awareness, assessment, adaptability, accountability | Intervention frequency, auditability, bounded autonomy | Yes | 2 5 6 |
| Sectoral & Contextual Factors | Surveys, realist synthesis, sectoral case studies | Security assurance, algorithmic control, human oversight | Worker autonomy, emotional state, organizational readiness | Yes | 7 8 9 |
| Regulatory Model Comparisons | Comparative policy analysis, prompt-based experiments | Regulatory enforcement, compliance checkpoints | Action restriction, permitted capabilities | Yes | 10 11 12 |
| Outcome Quantification | Runtime logs, compliance metrics, audit trails, MCDA, scenario-based assessments | Action restriction, intervention, abstention, permitted capabilities | Intervention scope, auditability, transparency | Yes | 2 5 13 |

## Direct Answer

Empirical studies demonstrate that the impact of AI governance controls on operational system behavior is measurable primarily through case studies, quasi-natural experiments, and runtime architectures. These studies differentiate technical runtime measurements—such as those using LTL formal methods, runtime monitors (Legitimacy Layer, A4-Gov), and audit trail analysis—from conceptual frameworks that remain prescriptive. Controls are operationalized in forms such as action restrictions, bounded interventions, abstention, and permitted capabilities, with comparators established via difference-in-differences models and other quasi-experimental designs to causally link responsible AI governance adoption with improvements in risk management, transparency, and performance outcomes.

## Study Scope

**Time Period:** Primarily post-2018, with emphasis on studies from 2020 onward. **Disciplines:** Computer science, public administration, organizational studies, industrial engineering, platform/gig economy, regulatory studies. **Methods:** Quasi-experimental (DID, PSM), process mining, digital twin modeling, surveys, case studies, formal methods (LTL), runtime monitoring, prompt-based experiments, MCDA, scenario-based assessments.

## Assumptions & Limitations

**Assumptions:** Studies accurately distinguish between conceptual and operationalized governance; runtime metrics are valid proxies for governance activation; comparator groups are appropriately matched.

**Limitations:** Limited standardization of governance outcome metrics across sectors; context-dependence of governance effectiveness; challenges in integrating legal/regulatory constructs with technical runtime enforcement; gaps in holistic, cross-sector benchmarking.

## Suggested Further Research

Develop standardized, multi-dimensional benchmarking tools integrating technical, operational, and human oversight metrics. Advance hybrid methodologies combining formal methods, machine learning, and process mining for real-time governance effect attribution. Empirically link dynamic regulatory models (e.g., EU AI Act) with quantifiable operational metrics and intervention outcomes. Explore integration of legal, ethical, and technical governance controls in high-risk and frontier AI contexts.

## 1. Introduction

## Scope and Rationale

Empirical research on AI governance and Responsible AI controls has shifted from conceptual frameworks— focused on principles and guidelines—to operational measurement of their real-world impact on system behavior. This transition is critical for ensuring that governance mechanisms are not only well-intentioned but also effective in practice. The distinction between conceptual frameworks and technical runtime measurement is foundational: while the former articulate what should be done, the latter provide evidence of what is actually achieved during AI system operation. This report synthesizes empirical studies that measure the operational impact of AI governance controls, focusing on how controls are activated, quantified, and evaluated using comparators, and what types of system behavior changes are observed (e.g., action restriction, intervention, abstention, permitted capabilities)[1][14][15].

## 2. Empirical Evidence of AI Governance Impact

**Causal Evidence Linking Governance Controls to System Behavior** Recent empirical studies provide robust causal evidence that AI governance controls, when adopted, lead to measurable changes in system behavior: **Quasi-natural experiments** (e.g., multi-period DID regression) show that responsible AI governance adoption causally improves corporate performance, with different governance dimensions (e.g., transparency, accountability) variably impacting outcomes[1].

**Causal mapping** using fuzzy DEMATEL identifies algorithmic transparency and cybersecurity assurance as dominant drivers of quality assurance in AI-enabled industrial systems[4].

**Process mining and digital twin modeling** are used to evaluate the impact of governance interventions on operational metrics such as turnaround times and SLA breaches[16].

**Surveys and structural equation modeling** link governance dimensions (autonomy, transparency, accountability) to organizational decision-making and trust[17]. These studies consistently distinguish technical runtime enforcement (e.g., runtime monitors, LTL-based controls) from conceptual frameworks, emphasizing the need for objective, real-time metrics[2][3].

## Proactive vs Reactive Governance Controls

Case studies and comparative analyses differentiate between: **Proactive controls:** Foresight-based, anticipatory mechanisms (e.g., continuous human oversight, predictive analytics, iterative validation) that enable pre-event prevention, longer-term policy production, and improved planning[14][18].

**Reactive controls:** Incident-driven, post-event remediation mechanisms that rely on manual intervention and retrospective analysis[19][20]. Empirical evidence shows that proactive governance frameworks (e.g., data-centric MLOps with human-in-the-loop annotation) outperform reactive approaches in terms of transparency, accountability, and organizational legitimacy[20].

## Contextual Factors Influencing Governance Effectiveness

Public sector studies highlight that governance effectiveness is mediated by:

**Organizational readiness:** Leadership support, skills development, resistance to change[8][21].

**Regulatory environment:** Privacy regulation, accountability pressures[22].

**Stakeholder perceptions:** Divergent views between citizens (optimistic) and public servants (concerned about accountability and operational risks)[23].

**Institutional legitimacy:** Transparency, oversight, and procedural safeguards are critical for public acceptance and durable policy support[24]. **Synthesis:** Empirical evidence robustly supports the claim that operationalized AI governance controls— especially when proactive and contextually embedded—produce measurable improvements in system behavior, risk management, and organizational outcomes. However, effectiveness is highly context-dependent, requiring alignment with organizational culture, regulatory frameworks, and stakeholder expectations.

## 3. Types and Categories of AI Governance Controls

## Quantitative Measurement and Categorization of Controls

Empirical studies categorize and measure AI governance controls as follows: **Technical controls:** Runtime monitors, formal methods (LTL), explainability tools, audit trail generation[15] [25][26]. **Bureaucratic controls:** Procedural rules, compliance checkpoints, ethical review forums[27][28]. **Organizational controls:** Leadership, cross-functional collaboration, data governance, standards enforcement[29]. **Algorithmic controls:** AI-driven decision-making, risk detection, explainability (e.g., SHAP, LIME)[30][31]. Sectoral differences are evident: **Industrial/Robotics:** Emphasis on safety assurance, risk management, explainability[26][32]. **Gig Economy:** Algorithmic control measured via worker autonomy, emotional state, job demands/resources [7][33]. **Public Sector/Defense:** Security assurance controls aligned with regulatory frameworks (EU AI Act, DoD RMF)[9][34].

## Security Assurance Controls in High-Risk Systems

High-risk AI systems operationalize governance through: **Threat modeling, identity management, code testing, segmented networks, cryptographically signed** **updates**[9][34]. **Compliance mechanisms:** Integration of EU AI Act, ISO/IEC 42001, NIST AI RMF into AI pipelines, with deterministic, reproducible, and verifiable compliance[35][36].

**Auditability:** Tamper-evident, signed artifacts and traceability across the AI lifecycle[37][38]. **Algorithmic Controls and Worker Outcomes in Platform Economies** Algorithmic controls in gig platforms are empirically linked to: **Worker autonomy and emotional state:** Measured via surveys, structural equation modeling, and validated scales for perceived algorithmic autonomy-support and control[33][39]. **Dual effects:** Increased negative emotions and burnout (hindrance stress), but also enhanced work autonomy and engagement (standardized guidance)[7][40]. **Moderators:** Perceived fairness, transparency, and gamification[41][42].

## Technical Runtime Metrics in Robotics and Autonomous Systems

Key runtime metrics include: **Safety assurance:** Runtime assurance (RTA) architectures, operational design domain (ODD) monitoring, uncertainty quantification[26][43][44]. **Explainability and transparency:** Explainable AI (XAI) techniques, surrogate models, audit trail generation [45][46]. **Risk and reliability assessment:** Dynamic, automated frameworks for evolving AI-enabled robotics[47]. **Synthesis:** AI governance controls are multi-dimensional, spanning technical, bureaucratic, organizational, and algorithmic domains. Their operationalization and measurement are sector-specific, with technical runtime metrics providing the most direct evidence of governance activation and effect.

## 4. Methods for Quantifying Operational Effects

## Runtime Governance Architectures and Activation Metrics

Empirical studies validate several runtime architectures: **A4-Gov:** Implements Awareness, Assessment, Adaptability, and Accountability functions, enabling continuous monitoring, bounded interventions, and audit-ready evidence[2][5]. **Legitimacy Layer:** Evaluates governance signals (uncertainty, impact, reversibility, contestation), routes decisions through a legitimacy controller, and enforces human oversight and escalation[2]. **Dynamic consent mechanisms:** Sub-second enforcement, audit trail generation, persona coherence in multi-agent systems[48]. **Auditability:** Preservation of policy state, intervention rationale, and replayable decision trajectories[5][49].

## Formal Methods and Temporal Logic for Compliance Monitoring

**LTL-based runtime monitoring:** Detects and reduces governance violations, preserves task performance, and enables preemptive intervention[6].

**Formal synthesis pipelines:** Transform LTL specifications into verified neural network controllers, ensuring safety and liveness properties[50].

**Runtime verification:** Online model checking, safety shields, and selective verification for error reduction [51][52].

## Distributed Governance Models and Robustness Evaluation

**Agent-based network models:** Simulate distributed governance, using compliance, risk, and transparency as metrics[15].

**Federated learning frameworks:** Evaluate robustness, privacy, and fairness using loss, MSE, RMSE, and attack success rates[53][54].

**Explainable AI in distributed systems:** Aggregation of local explanations into global, auditable rationales [55].

## Auditability and Human Oversight Metrics

**Human oversight:** Measured via authority, competence, technical capacity, and audit trail linkage[20][56]. **SAFE AI metrics:** Integrate security, accuracy, and explainability for compliance monitoring[57]. **Trust quantification:** Calibration, clinician–AI concordance, patient acceptance in clinical AI governance [58]. **Synthesis:** Quantifying operational effects of AI governance controls relies on sophisticated runtime architectures, formal verification, distributed simulation, and auditability metrics. These methods enable real-time measurement of governance activation, intervention frequency, and compliance outcomes.

## 5. Comparators and Outcome Measures in Governance Studies

## Comparator Designs and Causal Evaluation

**Quasi-experimental designs:** Multi-period DID, PSM, and prompt-based experiments are used to establish causal links between governance adoption and operational outcomes[1][12].

**Comparator groups:** Firms or entities categorized by governance adoption levels, regulatory models (EU vs US), or governance maturity[1][10].

**Baseline conditions:** Human performance baselines, expert elicitation, and organizational case studies[4] [59].

## Regulatory Model Comparisons and Enforcement Outcomes

**EU (Paternal Prevention):** Risk-averse, ex-ante compliance, strong enforcement, action restriction, but potential innovation constraints[10][11].

**US (Guardian Supervision):** Decentralized, post hoc oversight, innovation-friendly, but risks delayed harm mitigation[10][11].

**China:** Centralized, state-driven, content quality and ethics focus[60]. **Outcome differences:** Enforcement timing, scope, permitted capabilities, and regulatory fragmentation[11] [61].

## Empirical Measurement of Governance Outcomes

**Action restriction:** Prohibitions on high-risk AI uses, runtime halting, or escalation[2][6]. **Intervention:** Human oversight, conformity assessments, bounded interventions[5][62]. **Abstention:** Regulatory uncertainty leading to cautious innovation or suppression[12][63]. **Permitted capabilities:** Bounded autonomy, statistical control limits, adaptive compliance[10][64]. **Effectiveness of Governance Principles in Operational Systems** **Transparency:** Measured via traceability, explainability, communication, and auditability[13][65]. **Human oversight:** Structural guarantees, authority mapping, and audit trail linkage[56][66]. **Accountability:** Answerability, context, agent, and standards features[66][67]. **Mixed-methods approaches:** Combine qualitative interviews, quantitative surveys, and scenario-based assessments[68]. **Synthesis:** Empirical studies use robust comparator designs and outcome measures to evaluate the effectiveness of AI governance controls. Action restriction, intervention, abstention, and permitted capabilities are operationalized and quantified using runtime architectures, formal methods, and validated instruments, with regulatory model comparisons providing additional causal insights.

## 6. Discussion: Challenges and Future Directions

## Challenges in Measurement and Operationalization

**Standardization gaps:** Lack of unified, cross-sector benchmarks for governance outcomes[3][69]. **Integration challenges:** Difficulty in embedding legal/regulatory constructs into technical runtime enforcement[70]. **Role ambiguity:** Unclear responsibilities and uneven distribution of governance tools across stakeholders and lifecycle stages[69]. **Auditability:** Incomplete reporting, weak linkage between audit trails and security outcomes, limited evaluation on heterogeneous data[3].

## Emerging Paradigms and Recommendations

**Sentinel Governance:** Hybrid models supplementing human oversight with innovation and experimentation to manage action restrictions and interventions[71][72].

**Holistic frameworks:** Integration of technical, operational, and human oversight metrics into standardized benchmarking tools[73][74].

**Hybrid methodologies:** Combining formal methods, machine learning, and process mining for real-time governance effect attribution[75][76].

**Regulatory harmonization:** Empirically linking dynamic regulatory models (e.g., EU AI Act) with operational metrics and intervention outcomes[77]. **Synthesis:** While empirical measurement of AI governance controls has advanced, persistent challenges remain in standardization, integration, and auditability. Emerging paradigms advocate for hybrid, holistic approaches that bridge technical, organizational, and regulatory domains, with future research needed to develop robust, cross-sector benchmarking and dynamic compliance instrumentation.

## Conclusion

Empirical studies provide compelling evidence that AI governance and Responsible AI controls, when operationalized through technical runtime architectures, formal methods, and robust comparator designs, produce measurable changes in system behavior. These controls are most effective when proactive, contextually embedded, and supported by continuous monitoring, auditability, and human oversight. However, significant challenges remain in standardizing outcome metrics, integrating legal and technical controls, and ensuring auditability across diverse sectors and regulatory regimes. Future research should prioritize the development of holistic, multi-dimensional benchmarking tools and hybrid methodologies that can robustly attribute governance effects and support dynamic, adaptive compliance in evolving AI ecosystems.

## References

1. Exploring the impact of responsible AI governance on corporate performance: A quasi-natural experiment Xia, H., Chen, H., ZHANG, J.Z., KAMAL, M.M. Technological Forecasting and Social Change, 2026 https://www.scopus.com/pages/publications/105022113566?origin=scopusAI

2. The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems Aarab, H. International Conference on Human Centric Artificial Intelligence, ICHCAI 2026 - 1st International Conference, 2026 https://www.scopus.com/pages/publications/105046217618?origin=scopusAI

3. Toward Trustworthy Privacy-Preserving AI: Security, Ethics, and Governance Perspectives Al Sulaimani, A., Al Sulaimani, A., Elhadef, M. 2026 International Conference on Integrated Intelligence and Cognitive Engineering, ICIICE 2026, 2026 https://www.scopus.com/pages/publications/105043690279?origin=scopusAI

4. Mapping the causal structure of AI governance factors influencing quality assurance under Industry 4.0 regulations Patra, S.P. TQM Journal, 2026 https://www.scopus.com/pages/publications/105041801778?origin=scopusAI

5. A<sup>4</sup>-Gov: A Governance Architecture for AI Service Systems Ahn, M.S., Yoon, Y.I. 2026 IEEE/ACIS 24th International Conference on Software Engineering Research, Management and Applications, SERA 2026, 2026 https://www.scopus.com/pages/publications/105047279989?origin=scopusAI

6. Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems Alamdari, P.A., Klassen, T.Q., McIlraith, S.A. ACM FAccT 2026 - Proceedings of the 9th annual ACM Conference on Fairness, Accountability, and Transparency, 2026 https://www.scopus.com/pages/publications/105044423299?origin=scopusAI

7. Algorithmic Control and Negative Emotions in the Platform Economy: The Moderating Role of Work Gamification Lang, J., Xiao, Y., Cheng, Z., (...), Yang, L. Economics, 2026

https://www.scopus.com/pages/publications/105046706375?origin=scopusAI

8. Transforming public-sector HRM through AI: an integrated TAM–TOE framework Buonocore, F., de Gennaro, D., Del Barone, L., Colombi Evangelista, V. Journal of Managerial Psychology, 2026 https://www.scopus.com/pages/publications/105036985800?origin=scopusAI

9. Structuring AI Risk Management Framework: EU AI Act FRIA, GDPR DPIA and ISO 42001/23894 Parlov, N., Mateša, B., Mladinić, A. 2025 14th Mediterranean Conference on Embedded Computing, MECO 2025 - Proceedings, 2025 https://www.scopus.com/pages/publications/105010456107?origin=scopusAI

10. Paternal Prevention,Guardian Supervision, and Companion Regulation-A Comparative Framework of Global AI Governance Ling, B., Ma, R. Quarterly Journal of Economics and Management, 2025 https://www.scopus.com/pages/publications/105035727907?origin=scopusAI

11. A question of style? Regulating artificial intelligence in the European Union and the USA Harcourt, A., Radaelli, C.M., Trein, P. Big Data and Society, 2026 https://www.scopus.com/pages/publications/105043828338?origin=scopusAI

12. Governance-Conditioned Prompting and Structured Output Patterns in Large Language Models: A Multi- Domain Evaluation Chung, Y., Seol, K.-H., Paik, W. IEEE Access, 2026 https://www.scopus.com/pages/publications/105045786450?origin=scopusAI

13. Measuring AI responsibility: A cross-country validation of a multidimensional framework Jaturat, N., Na- Nan, K., Hu, B. International Journal of Information Management Data Insights, 2026 https://www.scopus.com/pages/publications/105028330729?origin=scopusAI

14. Evaluation of Enterprise Internal Control Based on Artificial Intelligence Liu, Z., Kong, T. Procedia Computer Science, 2025 https://www.scopus.com/pages/publications/105008865518?origin=scopusAI

15. A Network Model for the Governance of Artificial Intelligence Andrae, S. AI Influence on Governance and Law in the Digital Age, 2026 https://www.scopus.com/pages/publications/105031025690?origin=scopusAI

16. ALGORITHMIC OPTIMIZATION OF MANAGEMENT PROCESSES IN THE PUBLIC SECTOR BASED ON ARTIFICIAL INTELLIGENCE TECHNOLOGIES FOR INCREASING THE EFFICIENCY OF DIGITAL GOVERNANCE Mazur, H., Medvytskyi, O., Kharytonov, O., (...), Marukhlenko, O. Journal of Theoretical and Applied Information Technology, 2026 https://www.scopus.com/pages/publications/105043297452?origin=scopusAI

17. Artificial intelligence (AI) governance in organizational decision-making: balancing autonomy, accountability and transparency Hiremath, S., P, R., Konek, S.S., (...), B, O. Journal of Entrepreneurship and Public Policy, 2025 https://www.scopus.com/pages/publications/105024694657?origin=scopusAI

18. Mapping the landscape of AI governance in higher education Khoza, M.S., Wamba, S.F., Nyawa, S. Assessment and Evaluation in Higher Education, 2026 https://www.scopus.com/pages/publications/105046738415?origin=scopusAI

19. The Shift from Reactive to Proactive Governance Küçükyilmaz, Y.O., Yildirim, A. Artificial Intelligence in Public Administration: From E-Government to Smart Government, 2026 https://www.scopus.com/pages/publications/105037305979?origin=scopusAI

20. Data-centric AI governance for responsible organizational value: evidence from a European public administration Aguilar, R.M., Alayón, S., Torres, J.M., Martín, C.A. AI and Society, 2026 https://www.scopus.com/pages/publications/105033299122?origin=scopusAI

21. AI for the public sector: Readiness, adoption, and the public value promises Jonathan, G.M., Gebremeskel, B.K., Yalew, S.D., Watat, J.K. CEUR Workshop Proceedings, 2025 https://www.scopus.com/pages/publications/105017602201?origin=scopusAI

22. Bridging Governance and Technology: Key Determinants of AI Adoption in Public Administration Ly, B. Chinese Political Science Review, 2025 https://www.scopus.com/pages/publications/105012311324?origin=scopusAI

23. Prospects and Challenges of Future AI-Enabled Government: Perspectives of Citizens and Civil Servants Moon, M.J., Lee, S. Public Performance and Management Review, 2026 https://www.scopus.com/pages/publications/105043405246?origin=scopusAI

24. Institutional legitimacy and governance readiness for public safety AI: beyond technical accuracy in government AI systems Cho, S., Lee, S. Transforming Government: People, Process and Policy, 2026 https://www.scopus.com/pages/publications/105048119120?origin=scopusAI

25. Reducing organizational inequalities associated with algorithmic controls Li, Y., Xiang, B. Discover Artificial Intelligence, 2024 https://www.scopus.com/pages/publications/85193365946?origin=scopusAI

26. Extrinsic Safeguarding Mechanism Requirements for Trustworthy Physical AI Harris, M., Madden, D. Proceedings - 2025 IEEE 33rd International Requirements Engineering Conference Workshops, REW 2025, 2025 https://www.scopus.com/pages/publications/105020927532?origin=scopusAI

27. Digital Transformation: How Leadership Unifies Talent, Data, Ethics, and Governance for Trustworthy AI towards a Responsible AI Framework Abbu, H., Khan, S., Mugge, P., Gudergan, G. IEEE Engineering Management Review, 2026 https://www.scopus.com/pages/publications/105043699630?origin=scopusAI

28. Lagged short-run efficacy, sustained long-run inefficacy: how the AI-powered platform government affects the screen-level bureaucratic responsiveness Duan, C., Jia, Z., Chen, S. Global Public Policy and Governance, 2026 https://www.scopus.com/pages/publications/105043694030?origin=scopusAI

29. Embedding AI Governance in Organizations: A Multi-Level Approach to Responsible AI Use Sayan, M.M., Bueechl, J. Procedia Computer Science, 2025 https://www.scopus.com/pages/publications/105024077683?origin=scopusAI

30. Ethical Challenges of AI Adoption in Organizational Leadership and Governance Ramamoorthy, R., Dharuneswaran, R.K., Harshini, S., (...), Kumaran, S. 2025 IEEE 4th World Conference on Applied Intelligence and Computing, AIC 2025, 2025 https://www.scopus.com/pages/publications/105023636622?origin=scopusAI

31. Explainable Artificial Intelligence: A Study of Current State-of-the-Art Techniques for Making ML Models Interpretable and Transparent Thakur, A., Vashisth, R., Tripathi, S. Proceedings - International Conference on Technological Advancements in Computational Sciences, ICTACS 2023, 2023 https://www.scopus.com/pages/publications/85185382789?origin=scopusAI

32. Data Quality Management in Human Centric AI Xu, H. International Conference on Human Centric Artificial Intelligence, ICHCAI 2026 - 1st International Conference, 2026 https://www.scopus.com/pages/publications/105046186101?origin=scopusAI

33. Who’s the Boss? Measuring Gig-Workers’ Perceived Algorithmic Autonomy-Support Jabagi, N., Croteau, A.-M., Audebrand, L., Marsan, J. 42nd International Conference on Information Systems, ICIS 2021 TREOs: "Building Sustainability and Resilience with IS: A Call for Action", 2021 https://www.scopus.com/pages/publications/85191135513?origin=scopusAI

34. From Policy to Pipeline: A Governance Framework for AI Development and Operations Pipelines Butt, T.A., Iqbal, M., Arshad, N. IEEE Access, 2026 https://www.scopus.com/pages/publications/105025805961?origin=scopusAI

35. AI Governance: Achieving EU AI Act Compliance in the Dynamo Project Burns, F., Edelberg, J., Kuivanen, P., (...), Tikanmäki, I. European Conference on Information Warfare and Security, ECCWS, 2025 https://www.scopus.com/pages/publications/105014909444?origin=scopusAI

36. An Engineering Methodology for Verifying Compliance with the EU AI Act in Industrial AI Systems Lomasto, L., Abbruzzese, R., Cappetta, D., (...), Zaccagnino, R. Communications in Computer and Information

Science, 2026 https://www.scopus.com/pages/publications/105042278813?origin=scopusAI

37. THE AUDITING AND CONTROL OF HIGH-RISK ARTIFICIAL INTELLIGENCE SYSTEMS IN THE PUBLIC SECTOR Cañabate Pérez, J. Revista Catalana de Dret Public, 2025 https://www.scopus.com/pages/publications/105025933778?origin=scopusAI

38. Bridging Ethics and Regulation: How VBE Facilitates Compliance with the EU AI Act in High-Risk and General Purpose AI Madl, L., Bargu, S., Cuhadaroglu, M. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105023138472?origin=scopusAI

39. A New Era of Control: Understanding Algorithmic Control in the Gig Economy Weber, M., Remus, U., Pregenzer, M. International Conference on Information Systems, ICIS 2022: "Digitization for the Next Generation", 2022 https://www.scopus.com/pages/publications/85181718187?origin=scopusAI

40. Algorithmic management and gig workers: engagement, exhaustion and citizenship behavior Gong, T. Management Decision, 2025 https://www.scopus.com/pages/publications/105015399980?origin=scopusAI

41. Navigating the light and dark sides of algorithmic control: a double-sided impact on gig worker well-being Liu, S., Wang, Y., Xu, G., Zhao, W. Employee Relations, 2026 https://www.scopus.com/pages/publications/105037762163?origin=scopusAI

42. The double-edged sword effect of algorithmic transparency: An empirical study of gig workers’ work disengagement under algorithmic management Li, Y., Zhao, L., Cao, C., Yang, D. Information and Management, 2025 https://www.scopus.com/pages/publications/85214494285?origin=scopusAI

43. Learning Monitorable Operational Design Domains for Assured Autonomy Torfah, H., Xie, C., Junges, S., (...), Seshia, S.A. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2022 https://www.scopus.com/pages/publications/85142750299?origin=scopusAI

44. Improving Robustness of Deep Neural Networks for Aerial Navigation by Incorporating Input Uncertainty Arnez, F., Espinoza, H., Radermacher, A., Terrier, F. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2021 https://www.scopus.com/pages/publications/85115176040?origin=scopusAI

45. Who's in Charge Here? A Survey on Trustworthy AI in Variable Autonomy Robotic Systems Methnani, L., Chiou, M., Dignum, V., Theodorou, A. ACM Computing Surveys, 2024 https://www.scopus.com/pages/publications/85191097717?origin=scopusAI

46. Surrogate model framework for explainable autonomous behaviour in maritime robotic systems Gavriilidis, K., Munafo, A., Pang, W., Hastie, H. Maritime Autonomous Vehicles: Methods and Measurements, 2025 https://www.scopus.com/pages/publications/105028085372?origin=scopusAI

47. RISK AND RELIABILITY ASSESSMENT FOR AI-CONTROLLED OR RECONFIGURABLE ROBOTIC SYSTEMS: A SURVEY OF METHODS AND CHALLENGES Littmann, T., Grimmeisen, P., Morozov, A. ASME International Mechanical Engineering Congress and Exposition, Proceedings (IMECE), 2025 https://www.scopus.com/pages/publications/105035993405?origin=scopusAI

48. Implementing Dynamic Consent Mechanisms in Multi-Agent AI Systems: A Practical Framework Bumpus, M.A. Conference Proceedings - IEEE SOUTHEASTCON, 2026 https://www.scopus.com/pages/publications/105037874145?origin=scopusAI

49. Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines Miller, T. Machine Learning and Knowledge Extraction, 2026 https://www.scopus.com/pages/publications/105040121699?origin=scopusAI

50. Automated Synthesis of Verified Neural Network Controllers from Linear Temporal Logic Specifications O’Quinn, A., Taylor, M. RICSS 2025 - Proceedings of the 2025 Workshop on Re-design Industrial Control Systems with Security, 2025 https://www.scopus.com/pages/publications/105021937167?origin=scopusAI

51. Enhancing Decision-Making Safety in Autonomous Driving Through Online Model Checking Tran, D.D., Hasegawa, A., Riviere, P., (...), Aoki, T. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105015743109?origin=scopusAI

52. Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks Ganguly, D., Singh, V., Sankar, S., (...), Chaudhary, V. Advances in Neural Information Processing Systems, 2025 https://www.scopus.com/pages/publications/105048543381?origin=scopusAI

53. Secure Hierarchical Federated Learning for Large-Scale AI Models: Poisoning Attack Defense and Privacy Preservation in AIoT Han, C., Yang, T., Sun, X., Cui, Z. Electronics (Switzerland), 2025 https://www.scopus.com/pages/publications/105003663134?origin=scopusAI

54. Federated AI Framework for Privacy-Preserving Healthcare Prediction with Shuffle-Split Attention Networks Dhakshinamoorthy, S., Periyasami, K. KSII Transactions on Internet and Information Systems, 2026 https://www.scopus.com/pages/publications/105035004358?origin=scopusAI

55. Explainable Deep Learning in Cloud-Based Distributed Architectures: A Decision-Support Perspective Arfaoui, S., Jouini, M. 2026 Intelligence in Business and Industry, IBI 2026, 2026 https://www.scopus.com/pages/publications/105046148422?origin=scopusAI

56. Human Oversight in the AI Act: From Legal Obligation to Operational Safeguards for Fundamental Rights Trapani, S.T., Inverardi, N., Penco, I., Zaidan, M. International Conference on Agents and Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105041734919?origin=scopusAI

57. SAFE AI metrics: An integrated approach Giudici, P., Kolesnikov, V. Machine Learning with Applications, 2026 https://www.scopus.com/pages/publications/105027870181?origin=scopusAI

58. Ethical and Governance Challenges of AI in Medical Imaging and Diagnostics: A Systematic Survey and Policy Framework Recommendations Athukorala, D., Ahmed, K., Nowrozy, R. Healthcare (Switzerland), 2026 https://www.scopus.com/pages/publications/105045286844?origin=scopusAI

59. Position: Human Baselines in Model Evaluations Need Rigor and Transparency (With Recommendations & Reporting Checklist) Wei, K.L., Paskov, P., Dev, S., (...), Deshpande, C. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105023477148?origin=scopusAI

60. Legal Aspects of Biometric and Artificial Intelligence Deployment: A Comparative Analysis of EU and China Milenković, M., Vukuša, P. 2026 49th MIPRO ICT and Electronics Convention, MIPRO 2026 - Proceedings, 2026 https://www.scopus.com/pages/publications/105046218997?origin=scopusAI

61. How and why governments are regulating AI: a comparison of legislative frameworks Dylag, M. Information Communication and Society, 2025 https://www.scopus.com/pages/publications/105016745546?origin=scopusAI

62. Operationalizing Responsible AI Policies With LLMs: An End-To-End Monitoring Prototype Zieliński, P., Roesti, M., Barreto, R., Tahaei, M. Conference on Human Factors in Computing Systems - Proceedings, 2026 https://www.scopus.com/pages/publications/105038116552?origin=scopusAI

63. Balancing innovation and safeguards for public legitimacy: A typology of sentiment toward AI regulation in the EU and US Hermanns, L., Degen, K., Teubner, T. Government Information Quarterly, 2026 https://www.scopus.com/pages/publications/105036891741?origin=scopusAI

64. Human-AI governance (HAIG): A trust-utility approach Engin, Z. Journal of Responsible Technology, 2026 https://www.scopus.com/pages/publications/105037863617?origin=scopusAI

65. Evaluating Transparency in the Development of Artificial Intelligence Systems: A Systematic Literature Review Karanxha, G., Ofem, P. International Journal of Advanced Computer Science and Applications, 2025 https://www.scopus.com/pages/publications/105026618642?origin=scopusAI

66. Accountability in artificial intelligence: what it is and how it works Novelli, C., Taddeo, M., Floridi, L. AI and Society, 2024 https://www.scopus.com/pages/publications/85147578609?origin=scopusAI

67. BEYOND TRANSPARENCY: GOVERNANCE TENSIONS AND A TYPOLOGY OF ACCOUNTABILITY GAPS IN ARTIFICIAL INTELLIGENCE FOR HIGH-STAKES SERVICE SECTORS Urrutia-Onate, D., Bollain, J., Onieva, E., Perallos, A. Journal of Governance and Regulation, 2026 https://www.scopus.com/pages/publications/105047789948?origin=scopusAI

68. Sustainable and Inclusive AI Governance in Municipal Self-Service Systems: Ethical, Smart-Government, and Generative AI Perspectives Alyileili, M., Opoku, A. Sustainability (Switzerland), 2026 https://www.scopus.com/pages/publications/105028669571?origin=scopusAI

69. The ''Who", ''What", and ''How" of Responsible AI Governance: A Systematic Review and Meta-Analysis of (Actor, Stage)-Specific Tools Kuehnert, B., Kim, R., Forlizzi, J., Heidari, H. ACMF AccT 2025 - Proceedings of the 2025 ACM Conference on Fairness, Accountability,and Transparency, 2025 https://www.scopus.com/pages/publications/105010830141?origin=scopusAI

70. Strategies for Harmonizing Fragmented AI Ethics Frameworks, Standards, and Regulations Schiff, D.S. Handbook of Human-Centered Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105043079266?origin=scopusAI

71. COMPLIANCE THEATRE: RETHINKING EVALUATION AND ENFORCEMENT IN FRONTIER AI REGULATION Bartlett, M. Cambridge Law Journal, 2026 https://www.scopus.com/pages/publications/105046305123?origin=scopusAI

72. From Silicon Valley to Seoul: Contrasting Models, Shared Visions in Global AI Governance Lheem, H. Korean Studies in the Artificial Intelligence Era Volume 1: Innovations in Science, Engineering, Health, Business, Industry, and Ethics, 2026 https://www.scopus.com/pages/publications/105037283586?origin=scopusAI

73. Data governance for sustainable AI in organizations: a measurement-oriented capability method with benchmarkability robustness checks and marketplace-microdata operationalization Dockara, T.R., Malhotra, M. Discover Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105042432578?origin=scopusAI

74. Overview of transparency and inspectability mechanisms to achieve accountability of artificial intelligence systems Hauer, M.P., Krafft, T.D., Zweig, K. Data and Policy, 2023 https://www.scopus.com/pages/publications/85179908538?origin=scopusAI

75. Responsible AI Governance in the Public Sector: Explaining Contextual Dynamics through a Realist Synthesis Review Gagua, A., van der Voort, H., Goyal, N., Verbraeck, A. Proceedings of the 8th AAAI/ACM Conference on AI, Ethics, and Society, AIES 2025, 2025 https://www.scopus.com/pages/publications/105040255641?origin=scopusAI

76. A Learner-Verifier Framework for Neural Network Controllers and Certificates of Stochastic Systems Chatterjee, K., Henzinger, T.A., Lechner, M., Žikelić, Đ. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85161373548?origin=scopusAI

77. Global AI Regulations for FAIR and Ethics in High-Risk Use Cases: A Comparative Review Sharma, A.K., Koysev, D., Anich, C., (...), Kunkel, J. Proceedings - 2026 IEEE 50th Annual Computers, Software, and Applications Conference, COMPSAC 2026, 2026 https://www.scopus.com/pages/publications/105048943991?origin=scopusAI
