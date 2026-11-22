---
source_pdf: "Scopus - Scopus AI -Area 2.pdf"
source_sha256: "cf58bdececc34169db1b5104945df5830391b14af4ea3a9d0e6ae1cdf3be026d"
source_pages: 14
scopus_ai_generated: "Thu Apr 09 2026"
query: "Human trust calibration in advisory AI systems"
report_title: "Human Trust Calibration and Reliance vs. Compliance in Advisory AI Systems with Graduated Autonomy and Output Restrictions under Elevated Environmental Risk"
converted_tables: 2
converter: "scopus2md.py (pdfplumber)"
---
# Human trust calibration in advisory AI systems

## Quick Reference

## Key Findings Table

| Theme | Key Findings | Supporting Citations |
| --- | --- | --- |
| Transparency | High transparency about AI limitations and rationale is critical for trust calibration, reducing overtrust/undertrust, and improving safety in high-stakes environments. | 1 2 3 |
| Explicit Output Restrictions | Explicit output restrictions (vs. full disengagement) prompt active trust recalibration, increased vigilance, and more deliberate | 4 5 6 7 |

## 8

verification behaviors. Feedback Type Confirming and corrective feedback both improve trust calibration,[4][9][10][11] but corrective feedback is more effective, especially after errors.

## 12

| Task Risk & Consequence | Elevated risk and error severity increase vigilance, reduce reliance, and modulate compliance; trust is more sensitive to negative events. | 11 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- |
| Individual Differences | User expertise and risk propensity shape trust calibration and reliance; experts are more critical, non-experts may over/under-rely. |  |  | 16 | 17 |
| Psychophysiological Markers | EEG, ECG, and eye tracking can provide real-time indicators of trust calibration, complementing self-report measures. | 18 | 19 | 20 | 21 |
| Trust Recovery | Transparency, explanations, and model updates are effective for trust repair after failures; apologies alone are less effective. | 12 | 22 | 23 | 24 |
| Anthropomorphism | Moderate anthropomorphic cues can enhance trust resilience, but excessive cues may increase risk perception or overtrust. | 25 | 26 | 27 | 28 |

## Direct Answer

Research shows that when an advisory AI system imposes explicit output restrictions due to elevated environmental risk, human operators engage in a more active trust recalibration process compared to situations where the system fully disengages. Explicit cues, transparency about system limitations, and clear feedback foster dynamic trust adjustment and promote vigilance, leading to more deliberate verification behaviors in high-stakes environments. Both confirming and corrective feedback improve calibration, but corrective

feedback is especially effective after errors. User expertise and risk perceptions significantly modulate trust adjustment under these conditions, highlighting the need for adaptive, user-tailored AI interfaces that communicate uncertainty and system limitations effectively to support balanced reliance and compliance without encouraging overdependence[1][4][9][11][16].

## Study Scope

**Time Period:** Primarily 2015–2024 **Disciplines:** Human factors, cognitive engineering, HCI, AI safety, automotive and aviation systems, healthcare, and organizational psychology **Methods:** Experimental studies, simulator trials, field studies, meta-analyses, psychophysiological monitoring, and qualitative interviews

## Assumptions & Limitations

Most studies are conducted in simulated or controlled environments; real-world generalizability may be limited[29]. Individual differences (expertise, risk propensity) are often underrepresented in model development[16]. Current trust calibration models may not fully capture dynamic, relational, and context-dependent aspects of trust[30]. There is limited longitudinal data on trust recovery and adaptation in real-world, high-stakes settings[31].

## Suggested Further Research

Develop and validate continuous, adaptive trust calibration frameworks integrating behavioral, contextual, and psychophysiological data[32][33].

Investigate long-term trust dynamics and recovery trajectories in real-world, high-stakes domains with graduated autonomy and output restrictions[31].

Explore domain-specific sociotechnical design strategies to maintain human agency and skill while supporting trust calibration[34][35].

Assess the effectiveness of explainable AI techniques tailored to user expertise and risk context under explicit output restrictions[3][36].

## 1. Introduction

## Scope and Motivation

Trust calibration—the alignment of human trust with actual system reliability—is a cornerstone of safe and effective human-AI interaction, especially in high-stakes environments such as automated driving, aviation, and

healthcare[4][37][38]. As advisory AI systems increasingly operate under graduated autonomy, they may restrict their output scope (e.g., withhold advice, provide conditional recommendations) in response to elevated environmental risk rather than disengaging entirely. This nuanced operational mode presents unique challenges for human operators, who must dynamically adjust their reliance and compliance behaviors based on explicit system cues, transparency about limitations, and perceived risk[4][38].

This report synthesizes research on how users calibrate trust and modulate reliance versus compliance when interacting with advisory AI systems that explicitly restrict outputs under risk, with a focus on high-stakes human-automation interaction (HAI) contexts.

## 2. Theoretical Frameworks

**Trust Calibration Mechanisms in Advisory AI Systems with Output Restrictions**

## Explicit Output Restrictions vs. Full System Disengagement

**Explicit output restrictions** (e.g., “I cannot provide advice under current conditions”) prompt users to actively recalibrate trust, increase vigilance, and engage in manual verification, as opposed to **full system** **disengagement**, which often leads to a temporary trust decline and potential disuse[4][5][6][7]. Ongoing system involvement (even with restricted outputs) supports dynamic trust adjustment and maintains operator engagement, whereas disengagement may foster distrust or overreliance on manual control[8]. **Types of Output Restrictions and Their Impact on Trust Dynamics** **Partial advice withholding** and **conditional recommendations** affect trust calibration differently: Partial withholding can lead to subsystem-specific trust, with users adjusting trust based on perceived reliability and usefulness of each subsystem[39]. Conditional recommendations (e.g., “Advice only valid if X holds”) require users to evaluate context, fostering more nuanced trust calibration[4][40]. Automation performance has a stronger influence on trust than feedback style alone; output restrictions that reduce perceived reliability can have severe negative effects if not well-communicated[40].

## Transparency and Communication of Output Scope Limitations

**Transparency** about AI limitations, rationale, and uncertainty is consistently shown to reduce trust calibration errors, mitigate overtrust/undertrust, and improve task accuracy and acceptance rates[1][5][41] [42][43].

The content and timing of transparency matter: detailed explanations and uncertainty information are most effective, but excessive or poorly timed transparency can increase cognitive load or reduce compliance in critical situations[43].

## Real-Time Cognitive Processing of Output Restrictions

Users process explicit output restrictions by increasing vigilance, reducing reliance, and engaging in more manual verification, especially when error consequences are high[4][11][44][45][46].

Explainable AI methods that provide concrete examples (e.g., nearest-neighbor cases) are more effective for trust calibration than abstract attribution maps, particularly in high-risk tasks[44].

## Confirming vs. Corrective Feedback in Trust Calibration

**Corrective feedback** (explicitly indicating errors or limitations) is more effective than confirming feedback or confidence scores for improving appropriate reliance and trust calibration[4][9].

Incorrect reassurance (false confirmation) can rapidly erode trust and degrade performance, highlighting the importance of accurate, corrective feedback[10].

Trust decreases more rapidly after errors than it increases after corrections, underscoring the need for robust corrective mechanisms[11][12].

## Synthesis:

Explicit output restrictions, when paired with high transparency and corrective feedback, foster active trust recalibration and vigilance. The effectiveness of these mechanisms depends on the clarity of communication, user expertise, and the perceived risk context.

## 3. Methods & Data Transparency

**Experimental Paradigms:** Simulator studies (e.g., automated driving, aviation), controlled lab experiments, and field trials in healthcare and industrial settings[1][2][38].

**Measurement Approaches:** Self-report trust scales, behavioral metrics (reliance, compliance, intervention rates), and psychophysiological monitoring (EEG, ECG, eye tracking)[18][19].

**Meta-Analyses:** Synthesize findings across domains, focusing on transparency, feedback, and risk as moderators of trust calibration[1][3].

**Limitations:** Most studies use simulated environments; real-world complexity and long-term adaptation are less frequently addressed[29].

## 4. Critical Analysis of Findings

**Reliance vs. Compliance Behaviors in Graduated Autonomy under Risk-Aware Constraints** **Patterns of Reliance and Compliance under Risk-Aware Constraints**

**Reliance** (using AI advice as a resource) and **compliance** (following AI recommendations) are modulated by task risk, consequence severity, transparency, and AI reliability[11][37][43][47][48].

Medium-risk tasks elicit higher subjective trust but lower attention to advice; high-risk tasks prompt greater vigilance and preference for human input[37].

## Task Risk Levels and Behavioral Modulation

Increased workload and low task priority increase reliance but reduce verification, potentially leading to overreliance in multitasking environments[49].

Trust generally decreases as task risk increases, leading to more manual control and monitoring[50][51].

## Consequence Severity and User Vigilance

High-consequence errors trigger increased vigilance, reduced reliance, and more manual verification[11][13] [14].

Users anticipate more negative emotions and less positive engagement under high-risk, high-consequence conditions[52].

## Transparency, Situation Criticality, and Compliance Rates

Transparency increases trust and perceived reliability but may reduce compliance in high-criticality situations, as users become more aware of system limitations and environmental uncertainty[2][42][43][53]. Emotional responses mediate the relationship between perceived risk and trust, especially as situation criticality increases[53]. **Behavioral Differences in Reliance and Compliance under Fluctuating AI Reliability** Reliance behaviors adjust more dynamically to changes in AI performance than compliance, which is less sensitive to reliability fluctuations[47][54]. User expertise and risk propensity further modulate these behaviors; experts are more critical, while non-experts may over-or under-rely[16][51].

## Synthesis:

Reliance and compliance are distinct but interrelated behaviors, shaped by risk, transparency, and individual differences. High transparency and explicit output restrictions support calibrated reliance but may reduce compliance in critical situations, highlighting the need for adaptive, context-aware AI communication.

**Human-Automation Interaction Dynamics in High-Stakes Environments**

## Interaction Styles and Trust Stabilization

Defensive AI behaviors (cautious, risk-averse) facilitate trust stabilization and reduce intervention rates over time, while assertive behaviors may initially erode trust but prompt adaptive recalibration[15][48][55][56]. Users prefer to maintain control, favoring interaction styles that preserve human initiative[57].

## Psychophysiological Markers of Trust Calibration

EEG, ECG, and eye tracking provide real-time indicators of trust calibration, reflecting cognitive workload, stress, and perceived risk[18][19][20][21].

Deep learning models using these signals can predict dynamic trust changes with >70% accuracy in safety-critical settings[21].

## Social Complacency and Behavioral Readiness

Social complacency (high trust but low readiness to act) can undermine safety, especially when emotional engagement is low[53][58][59][60]. Institutional trust and social influence shape trust formation but do not guarantee behavioral readiness[58].

## Mechanisms of Trust Recovery after Automation Failures

Transparency, explanations, and model updates are effective for trust repair; apologies alone are less effective, especially after repeated or ethical violations[5][61][62][63]. Keeping humans in the control loop during failures supports adaptive risk mitigation and trust recovery[62].

## Synthesis:

Trust calibration in high-stakes HAI is a dynamic, multi-layered process influenced by system behavior, social context, and psychophysiological states. Effective trust recovery requires transparency, ongoing feedback, and mechanisms that maintain human engagement and agency.

**Anthropomorphic and Interface Design Factors in Trust Calibration**

## Anthropomorphic Characteristics and Trust Resilience

Moderate anthropomorphic cues (politeness, limited emotional tone) optimize trust and reduce perceived risk; excessive cues can increase risk perception or trigger overtrust[25][26][27][28]. In-group membership and behavioral anthropomorphism (rather than appearance) are stronger predictors of trust[64][65]. **Interface and Training Strategies for Predictable System Behavior** Training that emphasizes system limitations, transparent capability boundaries, and entrainment-based communication improves trust calibration and operator performance[66][67][68][69]. Ecological interfaces and simulation-based training expedite learning and support critical reflection[69][70]. **Differential Impacts of AI Error Types on Trust and Verification** False reassurance errors (AI confirms human mistakes) cause rapid trust degradation and poorer performance; errors that prompt verification can improve overall outcomes despite moderate trust loss[10][56] [71][72]. Continuous or late-stage errors have disproportionate negative effects on trust (peak-end effect)[15].

## Effectiveness of Trust Repair Strategies

Apologies combined with explanations and expressions of regret are more effective than apologies alone; model updates are most effective for restoring trust after performance errors[12][22][23][24]. Trust repair is less effective after ethical or repeated violations[73][74].

## Timing and Continuity of System Errors in Trust Dynamics

Trust decreases sharply after early and late errors but can recover rapidly; late errors allow quicker recovery if overall performance is good[15][75][76][77]. User perception of AI performance, rather than actual performance, strongly influences trust[78].

## Synthesis:

Anthropomorphic and interface design factors can enhance trust resilience and calibration if applied judiciously. Training, transparency, and error management are critical for maintaining appropriate reliance and supporting trust recovery.

## 5. Real-world Implications

**System Design:** Advisory AI systems should prioritize transparency, explicit communication of output restrictions, and corrective feedback, especially under elevated risk. Interfaces should support user understanding of system boundaries and limitations[1][3][68].

**Training:** Operator training should emphasize system limitations, critical reflection, and adaptive trust calibration, using simulation and ecological interface design[67][69].

**Trust Monitoring:** Integrating psychophysiological monitoring with behavioral data can enable real-time trust calibration and adaptive feedback, reducing the risk of overtrust or disuse[18][21].

**Human Agency:** Sociotechnical design approaches must maintain human agency and skill, allowing for graduated autonomy with user initiative and oversight[34][35].

**Trust Repair:** After automation failures, transparent explanations and model updates are more effective for trust recovery than apologies alone, especially in high-stakes contexts[12][22].

## 6. Future Research Directions

**Continuous, Adaptive Trust Calibration:** Develop frameworks that integrate behavioral, contextual, and psychophysiological data for real-time trust monitoring and adaptive feedback[32][33].

**Longitudinal Studies:** Investigate long-term trust dynamics, recovery, and adaptation in real-world, high-stakes domains with graduated autonomy and output restrictions[31].

**Domain-Specific Design:** Explore sociotechnical strategies tailored to specific domains (e.g., healthcare, transportation) to balance transparency, reliability, and human agency[34][35].

**Explainable AI:** Assess the effectiveness of explainable AI techniques tailored to user expertise and risk context, especially under explicit output restrictions[3][36].

**User Expertise:** Examine how user expertise and cognitive traits influence trust calibration and reliance accuracy, informing adaptive AI design and training[16][17].

**Trustworthiness Assurance:** Advance comprehensive frameworks that address ethical, human factors, and operational challenges in high-risk AI systems with output restrictions[79][80][81][82][83].

**Metacognitive AI:** Investigate metacognitive AI designs that foster trust resilience and critical thinking while avoiding over-reliance, leveraging transparency and adaptive feedback[31][41][84][85].

## 7. Conclusion

## Summary of Findings and Implications

**Trust calibration** in advisory AI systems with graduated autonomy and explicit output restrictions is best supported by high transparency, explicit corrective feedback, and adaptive interface design[1][2].

**Reliance and compliance** behaviors are dynamically modulated by task risk, consequence severity, transparency, and individual differences; high transparency supports calibrated reliance but may reduce compliance in critical situations[2][38].

**Human-automation interaction** in high-stakes environments requires ongoing trust monitoring, robust error management, and mechanisms for trust recovery that maintain human agency and skill[1][80].

**Future research** should focus on continuous, adaptive trust calibration frameworks, domain-specific sociotechnical design, and the integration of behavioral and psychophysiological data for real-time trust management. **In sum,** the effective calibration of human trust in advisory AI systems under graduated autonomy and explicit output restrictions is essential for safe, resilient, and adaptive human-AI collaboration in high-stakes environments. This requires transparent communication, adaptive feedback, and ongoing support for human agency and critical engagement.

## References

1. When to Trust the Machine: A Simulation Framework for Human–AI Collaboration Hani, S., Margondai, A., von Ahlefeldt, C., (...), Mouloua, M. Applied Human Factors and Ergonomics International, 2026 https://www.scopus.com/pages/publications/105030034078?origin=scopusAI

2. Transparency and Explainability in AI-Assisted Decision Making: Effects on Trust, Perceived Reliability, Confidence, and Ease of Understanding Sullivan, V., Weger, K. Proceedings of the Human Factors and Ergonomics Society, 2025 https://www.scopus.com/pages/publications/105031723161?origin=scopusAI

3. Rapid Trust Calibration through Interpretable and Uncertainty-Aware AI Tomsett, R., Preece, A., Braines, D., (...), Kaplan, L. Patterns, 2020 https://www.scopus.com/pages/publications/85090277691?origin=scopusAI

4. When AI Stays Silent: Hidden Agreement May Undermine Trust Building in Adaptive Decision Support and Training Ramon Alaman, J., Lafond, D., Marois, A., Tremblay, S. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105028351776?origin=scopusAI

5. The More You Know: Trust Dynamics and Calibration in Highly Automated Driving and the Effects of Take- Overs, System Malfunction, and System Transparency Kraus, J., Scholz, D., Stiegemeier, D., Baumann, M. Human Factors, 2020 https://www.scopus.com/pages/publications/85068185171?origin=scopusAI

6. Decision Deferral in a Human-AI Joint Face-Matching Task: Effects on Human Performance and Trust Salehi, P., Chiou, E.K., Mancenido, M., (...), Shah, A. Proceedings of the Human Factors and Ergonomics Society, 2021 https://www.scopus.com/pages/publications/85171306011?origin=scopusAI

7. To (Dis)agree with Automation: Effects of Automation Levels on Trust Attitude and Trust Behavior in High- Risk Situations Onnasch, L., Hoesterey, S., Fahrner, V. Proceedings of the Human Factors and Ergonomics Society, 2023 https://www.scopus.com/pages/publications/85190939866?origin=scopusAI

8. Analysis of trust in autonomy for convoy operations Gremillion, G.M., Metcalfe, J.S., Marathe, A.R., (...), Atwater, C. Proceedings of SPIE - The International Society for Optical Engineering, 2016 https://www.scopus.com/pages/publications/84991449473?origin=scopusAI

9. Too Sure for Trust. The Paradoxical Effect of Calibrated Confidence in Case of Uncalibrated Trust in Hybrid Decision Making Cabitza, F., Fregosi, C., Vicente, L. Communications in Computer and Information Science, 2026 https://www.scopus.com/pages/publications/105020244723?origin=scopusAI

10. Exploring Trust and Performance in Human-Automation Interaction: Novel Perspectives on Incorrect Reassurances From Imperfect Automation Kim, J.Y., Chen, S.-T., Lester, C., Yang, X.J. Applied Human Factors and Ergonomics International, 2023 https://www.scopus.com/pages/publications/105031574828?origin=scopusAI

11. Evaluating the Effects of Consequences of Error on Trust in AI-Aided Task: An Eye Tracking Study Kim, J.Y., Kautz, C., Yang, X.J. Proceedings of the Human Factors and Ergonomics Society, 2025 https://www.scopus.com/pages/publications/105031696553?origin=scopusAI

12. Trust Development and Repair in AI-Assisted Decision-Making during Complementary Expertise Pareek, S., Velloso, E., Goncalves, J. 2024 ACM Conference on Fairness, Accountability, and Transparency, FAccT 2024, 2024 https://www.scopus.com/pages/publications/85196662447?origin=scopusAI

13. Impact of EXplainable AI on Trust Evolution with AI Error Severity: Comparing Similar Instances and Saliency Map in a Baggage Screening Task Wang, Y., Zhao, J., Ba, Y., (...), Maciejewski, R. International Journal of Human-Computer Interaction, 2025 https://www.scopus.com/pages/publications/105018825142?origin=scopusAI

14. Towards Adaptive Autonomous Vehicle Systems: Considering Trust and Risk Perception during Failures Lim, C., Rajivan, P. Accident Analysis and Prevention, 2026 https://www.scopus.com/pages/publications/105019666997?origin=scopusAI

15. Continuous Error Timing in Automation: The Peak-End Effect on Human-Automation Trust Wang, K., Lu, J., Ruan, S., Qi, Y. International Journal of Human-Computer Interaction, 2024 https://www.scopus.com/pages/publications/85162952254?origin=scopusAI

16. First impressions of a financial AI assistant: differences between high trust and low trust users Schreibelmayr, S., Moradbakhti, L., Mara, M. Frontiers in Artificial Intelligence, 2023 https://www.scopus.com/pages/publications/85174567930?origin=scopusAI

17. Examining the Influence of Domain Expertise and Other Antecedents of Trust in a Decision-Aid Assisted Language Translation Task Vazquez, E., Brugh, C.S. Lecture Notes in Computer Science, 2025 https://www.scopus.com/pages/publications/105008493380?origin=scopusAI

18. Adaptive XAI in High Stakes Environments: Modeling Swift Trust with Multimodal Feedback in Human AI Teams Fernando, N., Nakisa, B., Ahmad, A., Rastgoo, M.N. CEUR Workshop Proceedings, 2025 https://www.scopus.com/pages/publications/105019514306?origin=scopusAI

19. Modelling perceived risk and trust in driving automation reacting to merging and braking vehicles He, X., Stapel, J., Wang, M., Happee, R. Transportation Research Part F: Traffic Psychology and Behaviour, 2022 https://www.scopus.com/pages/publications/85125523146?origin=scopusAI

20. Unraveling trust in collaborative human-machine intelligence from neurophysiological perspective: a review of EEG and fNIRS features Chen, H., Chan, I.Y.S., Dong, Z., Samuel, T.-A. Advanced Engineering Informatics, 2025 https://www.scopus.com/pages/publications/105008300789?origin=scopusAI

21. Deep Learning-Based Prediction of Human-Robot Trust Dynamics in Future Construction Using Worker Neuropsychophysiological Responses Chang, W.-C., Gonzalez Garcia, N.F., Hasanzadeh, S. Journal of Computing in Civil Engineering, 2025 https://www.scopus.com/pages/publications/105004653199?origin=scopusAI

22. Trust Repair in Human-Agent Teams: the Effectiveness of Explanations and Expressing Regret Kox, E.S., Kerstholt, J.H., Hueting, T.F., de Vries, P.W. Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems, AAMAS, 2022 https://www.scopus.com/pages/publications/85134348287?origin=scopusAI

23. Modeling Trust Dynamics in Robot-Assisted Delivery: Impact of Trust Repair Strategies Mangalindan, D.H., Kandikonda, K., Rovira, E., Srivastava, V. Proceedings - IEEE International Conference on Robotics and Automation, 2025 https://www.scopus.com/pages/publications/105016610903?origin=scopusAI

24. The Robot That Showed Remorse: Repairing Trust with a Genuine Apology Pompe, B.L., Velner, E., Truong, K.P. RO-MAN 2022 - 31st IEEE International Conference on Robot and Human Interactive Communication: Social, Asocial, and Antisocial Robots, 2022 https://www.scopus.com/pages/publications/85140721985?origin=scopusAI

25. Designing age-inclusive AI tutors: effects of anthropomorphism on trust and risk in elderly health Management–a between-subjects experiment Li, H., Zhang, Y., Chen, H., (...), Bu, L. Interactive Learning Environments, 2025 https://www.scopus.com/pages/publications/105024916051?origin=scopusAI

26. More human-likeness, more trust? The effect of anthropomorphism on self-reported and behavioral trust in continued and interdependent human–agent cooperation Kulms, P., Kopp, S. ACM International Conference Proceeding Series, 2019 https://www.scopus.com/pages/publications/85072802682?origin=scopusAI

27. Balancing Anthropomorphic Design in Healthcare AI Agents Nabavian, S., Grabis, J., Dohan, M. Americas Conference on Information Systems, AMCIS 2025, 2025 https://www.scopus.com/pages/publications/105025351898?origin=scopusAI

28. Overtrust in AI Recommendations About Whether or Not to Kill: Evidence from Two Human-Robot Interaction Studies Holbrook, C., Holman, D., Clingo, J., Wagner, A.R. Scientific Reports, 2024 https://www.scopus.com/pages/publications/85203138007?origin=scopusAI

29. Observations on trust, reliance, and performance measurement in human-automation team assessment Rusnock, C.F., Miller, M.E., Bindewald, J.M. 67th Annual Conference and Expo of the Institute of Industrial Engineers 2017, 2017 https://www.scopus.com/pages/publications/85031007165?origin=scopusAI

30. Trust Calibration for Joint Human/AI Decision-Making in Dynamic and Uncertain Contexts Marusich, L.R., Files, B.T., Bancilhon, M., (...), Raglin, A. Lecture Notes in Computer Science, 2025 https://www.scopus.com/pages/publications/105008225387?origin=scopusAI

31. Enhancing Intuitive Decision-Making and Reliance Through Human–AI Collaboration: A Review Xu, G., Murthy, S.V., Jia, B. Informatics, 2025 https://www.scopus.com/pages/publications/105025883144?origin=scopusAI

32. Calibrating Trust in Autonomous Systems in a Dynamic Environment Okamura, K., Yamada, S. Proceedings for the 42nd Annual Meeting of the Cognitive Science Society: Developing a Mind: Learning in Humans, Animals, and Machines, CogSci 2020, 2020 https://www.scopus.com/pages/publications/85139478136?origin=scopusAI

33. Empirical Evaluations of Framework for Adaptive Trust Calibration in Human-AI Cooperation Okamura, K., Yamada, S. IEEE Access, 2020 https://www.scopus.com/pages/publications/85097929575?origin=scopusAI

34. Adaptive Cognitive Mechanisms to Maintain Calibrated Trust and Reliance in Automation Lebiere, C., Blaha, L.M., Fallon, C.K., Jefferson, B. Frontiers in Robotics and AI, 2021 https://www.scopus.com/pages/publications/85107438733?origin=scopusAI

35. Trusting Automation: Designing for Responsivity and Resilience Chiou, E.K., Lee, J.D. Human Factors, 2023 https://www.scopus.com/pages/publications/85104981249?origin=scopusAI

36. Communication of Uncertainty Information in Cooperative, Automated Driving: A Comparative Study of Different Modalities Peintner, J., Manger, C., Riener, A. ACM International Conference Proceeding Series,

2023 https://www.scopus.com/pages/publications/85173853784?origin=scopusAI

37. Trusting the Middle in the TNO Trust Task: How Medium Risk and Reliability Shape AI-Assisted Advice- Taking Sun, Z., Ding, J. Human Behavior and Emerging Technologies, 2025 https://www.scopus.com/pages/publications/105022635760?origin=scopusAI

38. Calibrating Reliance on Automated Advice: Transparency and Trust Calibration Feedback Tatasciore, M., Loft, S. International Journal of Human-Computer Interaction, 2025 https://www.scopus.com/pages/publications/105002963214?origin=scopusAI

39. Which partially automated driving function do drivers prefer? Results from two field studies on public highways Ebinger, N., Neuhuber, N., Moser, J., (...), Stocker, A. Transportation Engineering, 2024 https://www.scopus.com/pages/publications/85199921470?origin=scopusAI

40. Why Does the Automation Say One Thing but Does Something Else? Effect of the Feedback Consistency and the Timing of Error on Trust in Automated Driving Manchon, J.B., Beaufort, R., Bueno, M., Navarro, J. Information (Switzerland), 2022 https://www.scopus.com/pages/publications/85140658221?origin=scopusAI

41. Effects of transparency on pilot trust and agreement in the autonomous constrained flight planner Sadler, G., Battiste, H., Ho, N., (...), Smith, D. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2016 https://www.scopus.com/pages/publications/85009433400?origin=scopusAI

42. Are Explanations Helpful Under Uncertainty? Effects of Uncertainty in AI-Assisted Spacecraft Anomaly Diagnosis Dutta, P., Josan, P.K., Wong, R.K.W., (...), Selva, D. Journal of Cognitive Engineering and Decision Making, 2026 https://www.scopus.com/pages/publications/105020414314?origin=scopusAI

43. Effects of agent transparency and situation criticality upon human-autonomy trust and risk perception in decision-making Simon, L., Rauffet, P., Guerin, C. Cognition, Technology and Work, 2025 https://www.scopus.com/pages/publications/85208112346?origin=scopusAI

44. Reassuring, Misleading, Debunking: Comparing Effects of XAI Methods on Human Decisions Humer, C., Hinterreiter, A., Leichtmann, B., (...), Streit, M. ACM Transactions on Interactive Intelligent Systems, 2024 https://www.scopus.com/pages/publications/85205389381?origin=scopusAI

45. Hybrid human–AI decision-making for fire-related disaster risk reduction Shekili, S. Progress in Disaster Science, 2026 https://www.scopus.com/pages/publications/105032584262?origin=scopusAI

46. Innovative Guardrails for Generative AI: Designing an Intelligent Filter for Safe and Responsible LLM Deployment Shvetsova, O., Katalshov, D., Lee, S.-K. Applied Sciences (Switzerland), 2025 https://www.scopus.com/pages/publications/105010274384?origin=scopusAI

47. Human operators' blind compliance, reliance, and dependence behaviors when working with imperfect automation: A meta-analysis Schuler, P.T., Jessie Yang, X. Proceedings of the 2022 IEEE International Conference on Human-Machine Systems, ICHMS 2022, 2022 https://www.scopus.com/pages/publications/85146276625?origin=scopusAI

48. Drivers’ Intervention Tendency and Trust Dynamics During Interactions with Automated Vehicles in Potential Hazard Scenarios Wu, Y., Huang, D., Yu, X., (...), Tan, X. Communications in Computer and Information Science, 2025 https://www.scopus.com/pages/publications/105008658960?origin=scopusAI

49. The Effect of Workload and Task Priority on Multitasking Performance and Reliance on Level 1 Explainable AI (XAI) Use Alami, J., El Iskandarani, M., Riggs, S.L. Human Factors, 2025 https://www.scopus.com/pages/publications/105000178288?origin=scopusAI

50. Risk and trust in artificial intelligence technologies: A case study of autonomous vehicles Ajenaghughrure, I.B., Da Costa Sousa, S.C., Lamas, D. International Conference on Human System Interaction, HSI, 2020 https://www.scopus.com/pages/publications/85091400643?origin=scopusAI

51. Does the Propensity to Take Risks Influence Human Interactions with Autonomous Systems? Ferronato, P., Bashir, M. Advances in Intelligent Systems and Computing, 2020 https://www.scopus.com/pages/publications/85088496588?origin=scopusAI

52. The effects of risk and role on users’ anticipated emotions in safety-critical systems Albayram, Y., Khan, M.M.H., Jensen, T., (...), Coman, E. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2018 https://www.scopus.com/pages/publications/85050335424?origin=scopusAI

53. Do emotions matter in AI? The mediating role of emotional response between perceived risk and trust Babiker, A., Basel Almourad, M., AlShakhsi, S., (...), Ali, R. AI and Society, 2026 https://www.scopus.com/pages/publications/105033552617?origin=scopusAI

54. Knowing When to Pass: The Effect of AI Reliability in Risky Decision Contexts Elder, H., Canfield, C., Shank, D.B., (...), Hines, C. Human Factors, 2024 https://www.scopus.com/pages/publications/85130864838?origin=scopusAI

55. Almost human: Anthropomorphism increases trust resilience in cognitive agents de Visser, E.J., Monfort, S.S., McKendrick, R., (...), Parasuraman, R. Journal of Experimental Psychology: Applied, 2016 https://www.scopus.com/pages/publications/84986260158?origin=scopusAI

56. Beyond Binary Decisions: Evaluating the Effects of AI Error Type on Trust and Performance in AI-Assisted Tasks Kim, J.Y., Lester, C., Yang, X.J. Human Factors, 2025 https://www.scopus.com/pages/publications/105000513290?origin=scopusAI

57. Designing Trust in Highly Automated Virtual Assistants: A Taxonomy of Levels of Autonomy Galdon, F., Hall, A., Wang, S.J. Studies in Computational Intelligence, 2021 https://www.scopus.com/pages/publications/85102052192?origin=scopusAI

58. Measuring Social Trust in AI: How Institutions Shape the Usage Intention of AI-Based Technologies Amir, S., Luk, S.C.Y., Saha, S., (...), Teo, M.T.L. Human Behavior and Emerging Technologies, 2025 https://www.scopus.com/pages/publications/105018519210?origin=scopusAI

59. Exploring the mechanism of sustained consumer trust in AI chatbots after service failures: a perspective based on attribution and CASA theories Gu, C., Zhang, Y., Zeng, L. Humanities and Social Sciences Communications, 2024 https://www.scopus.com/pages/publications/85207519693?origin=scopusAI

60. A Society that Encourages AI: The Impact of Social Influence Factors on the Adoption of Generative AI Based on Cognitive Appraisal Theory Lee, S., Suh, S., Chun, J.-S. Asian Communication Research, 2025 https://www.scopus.com/pages/publications/105007013768?origin=scopusAI

61. How Can I Trust You? The Effect of Risk and Automation Failures on Trust and Reliance Behavior Ebinger, N., Neuhuber, N., Kubicek, B. Human Factors, 2026 https://www.scopus.com/pages/publications/105023571891?origin=scopusAI

62. Differential Impact of Autonomous Vehicle Malfunctions on Human Trust Seet, M., Harvy, J., Bose, R., (...), Thakor, N. IEEE Transactions on Intelligent Transportation Systems, 2022 https://www.scopus.com/pages/publications/85108304647?origin=scopusAI

63. Trust strategies in consumer multiple-component systems Lopez, J., Pak, R. Proceedings of the Human Factors and Ergonomics Society, 2018 https://www.scopus.com/pages/publications/85072751546?origin=scopusAI

64. The effect of group membership, system reliability and anthropomorphic appearance on user’s trust in intelligent decision support system Zou, X., Lv, C., Zhang, J. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2020 https://www.scopus.com/pages/publications/85088535598?origin=scopusAI

65. Gender similarity effects in human–AI interaction: Development and validation of the Behavioral AI Anthropomorphism Scale (BAAS) and implications for trust and gender attribution Ibrahim, F., Telle, N.-T., Lauckner, M., (...), Daseking, M. Computers in Human Behavior Reports, 2026 https://www.scopus.com/pages/publications/105033602437?origin=scopusAI

66. Efficient Human-Robot Interaction for Robust Autonomy in Task Execution Banerjee, S., Chernova, S. ACM/IEEE International Conference on Human-Robot Interaction, 2018 https://www.scopus.com/pages/publications/85045280202?origin=scopusAI

67. The Impact of Training on Human–Autonomy Team Communications and Trust Calibration Johnson, C.J., Demir, M., McNeese, N.J., (...), Cooke, N.J. Human Factors, 2023 https://www.scopus.com/pages/publications/85116070507?origin=scopusAI

68. Building an effective operator interface for complex APC applications Percell, E.S., Michaud, L.M. AIChE Annual Meeting, Conference Proceedings, 2006 https://www.scopus.com/pages/publications/77953021105?origin=scopusAI

69. Levelling up: Progress from operator training to competency management Roffel, J.J., Ross, M.J. American Fuel and Petrochemical Manufacturers, AFPM - AFPM Annual Meeting 2016, 2016 https://www.scopus.com/pages/publications/84987781395?origin=scopusAI

70. Ecological approach to train air traffic control novices in conflict detection and resolution Borst, C., Visser, R., Van Paassen, M.M., Mulder, M. SESAR Innovation Days, 2016 https://www.scopus.com/pages/publications/85076479093?origin=scopusAI

71. Automation failures on tasks easily performed by operators undermine trust in automated aids Madhavan, P., Wiegmann, D.A., Lacson, F.C. Human Factors, 2006 https://www.scopus.com/pages/publications/33745939673?origin=scopusAI

72. Toward Quantifying Trust Dynamics: How People Adjust Their Trust After Moment-to-Moment Interaction With Automation Yang, X.J., Schemanske, C., Searle, C. Human Factors, 2023 https://www.scopus.com/pages/publications/85166373149?origin=scopusAI

73. Towards Ethical AI: Empirically Investigating Dimensions of AI Ethics, Trust Repair, and Performance in Human-AI Teaming Schelble, B.G., Lopez, J., Textor, C., (...), Freeman, G. Human Factors, 2024 https://www.scopus.com/pages/publications/85135816118?origin=scopusAI

74. Purpose Outweighs Performance: Trust Drops More When AI Teammates Fail to Cooperate, but Explanations Can Repair It Li, M., Lee, J.D. International Journal of Human-Computer Interaction, 2026 https://www.scopus.com/pages/publications/105012479025?origin=scopusAI

75. How Misclassification Severity and Timing Influence User Trust in AI Image Classification: User Perceptions of High-And Low-Stakes Contexts Freel, A., Pias, S.B.H., Šabanović, S., Kapadia, A. ACMF AccT 2025 - Proceedings of the 2025 ACM Conference on Fairness, Accountability,and Transparency, 2025 https://www.scopus.com/pages/publications/105010827277?origin=scopusAI

76. Trust Formation, Error Impact, and Repair in Human–AI Financial Advisory: A Dynamic Behavioral Analysis Han, J., Ko, D. Behavioral Sciences, 2025 https://www.scopus.com/pages/publications/105020202078?origin=scopusAI

77. The Trust Recovery Journey. The Effect of Timing of Errors on the Willingness to Follow AI Advice. Kahr, P.K., Rooks, G., Snijders, C., Willemsen, M.C. ACM International Conference Proceeding Series, 2024 https://www.scopus.com/pages/publications/85190969348?origin=scopusAI

78. How Does Variation in AI Performance Affect Trust in AI-infused Systems: A Case Study With In-Vehicle Voice Control Systems Gu, F., Xu, H., He, D. Proceedings of the Human Factors and Ergonomics Society, 2024 https://www.scopus.com/pages/publications/85214823516?origin=scopusAI

79. Towards Trustworthy AI Decision-Making: A Unified Framework for Counterfactual Resilience, Neuro-symbolic Constraints, and Ethical Alignment Jiang, H., Zhu, J., Wang, J., Lei, J. Proceedings of 2025 International Conference on Digital Society and Intelligent Computing, ICDSIC 2025, 2026 https://www.scopus.com/pages/publications/105032174862?origin=scopusAI

80. Trustworthiness Assurance Assessment for High-Risk AI-Based Systems Stettinger, G., Weissensteiner, P., Khastgir, S. IEEE Access, 2024 https://www.scopus.com/pages/publications/85185548837?origin=scopusAI

81. AI_TAF: A Human-Centric Trustworthiness Risk Assessment Framework for AI Systems Seralidou, E., Kioskli, K., Fotis, T., Polemi, N. Computers, 2025 https://www.scopus.com/pages/publications/105011646942?origin=scopusAI

82. Trust by Design: An Ethical Framework for Collaborative Intelligence Systems in Industry 5.0 Merchán- Cruz, E.A., Gabelaia, I., Savrasovs, M., (...), Aragón-Camarasa, G. Electronics (Switzerland), 2025 https://www.scopus.com/pages/publications/105006840720?origin=scopusAI

83. Evaluating Trustworthiness in AI: Risks, Metrics, and Applications Across Industries Nastoska, A., Jancheska, B., Rizinski, M., Trajanov, D. Electronics (Switzerland), 2025 https://www.scopus.com/pages/publications/105011944822?origin=scopusAI

84. The Impact of Metacognitive AI on Appropriate Reliance in AI-Assisted Decision-Making: The Role of Trust Resilience and Critical Thinking Mehri, B., Ghasemaghaei, M. Americas Conference on Information Systems, AMCIS 2025, 2025 https://www.scopus.com/pages/publications/105025195706?origin=scopusAI

85. The Complexities of Human Factors in Automation Trust Hayes, R., Burrell, D.N. Cyber Risk Management and AI Governance in the Digital Era, 2026 https://www.scopus.com/pages/publications/105031329876?origin=scopusAI
