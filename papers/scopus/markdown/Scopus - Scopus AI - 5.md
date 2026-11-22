---
source_pdf: "Scopus - Scopus AI - 5.pdf"
source_sha256: "65d112a41ccfc0c9b55df54fab7c49ca56c68b36852d435c9ad961d5daa14809"
source_pages: 12
scopus_ai_generated: "Mon Nov 16 2026"
query: "AI advisory restrictions and safety outcomes"
report_title: "Comparative Analysis of Intermediate AI Advisory Restrictions and Calibrated Binary Gating: Safety Outcomes and Advice Retention under Degraded Input Conditions Quick Reference"
converted_tables: 2
converter: "scopus2md.py (pdfplumber)"
---
# AI advisory restrictions and safety outcomes

## Key Findings Table

| Criterion | Intermediate Advisory Restrictions | Calibrated Binary Gating | Evidence Strength | Closest Competing Studies (Title/DOI) |
| --- | --- | --- | --- | --- |
| Direct | None found | None found | High (gap) | N/A |

## comparative

## studies

| Safety outcomes (degraded input) | Improved trust, nuanced oversight; explainability reduces under-reliance but not hallucinations; no direct link to input degradation | Improved reliability, reduced calibration error; robust to domain shift/noise; trade-off with intervention frequency | Moderate (separate strands) | 1, | 2 |
| --- | --- | --- | --- | --- | --- |
| Advice retention | Verification scaffolding, trust calibration, explainability; risk of over-reliance | Uncertainty communication, hedging, calibrated confidence; reduces blind trust | Moderate (separate strands) | 3, | 4 |
| Input data quality impact | Explainability helps, but hallucinations and unsafe advice persist; imputation not directly linked | Noise-induced regularization, multiple imputation, uncertainty-aware gating; robust to missing/noisy data | Moderate (separate strands) | 5, | 6 |
| Regulatory frameworks | Human oversight, explainability, risk-based controls | Calibration, confidence thresholds, escalation protocols | High (established) | 7, | 8 |

## Direct Answer

Peer-reviewed research has **not yet established clear conditions** under which intermediate AI advisory

restrictions outperform calibrated binary gating regarding independent safety outcomes and useful advice retention under missing, stale, or noisy inputs. The closest competing studies address either advisory restrictions (e.g., explainable AI and trust calibration[2][9]) or calibrated binary gating mechanisms in vision–language–action tasks[1][10], but **no single study directly compares these approaches under** **similar experimental conditions with verifiable titles and DOIs**.

## Unable to Find

No direct head-to-head peer-reviewed studies comparing intermediate advisory restrictions and calibrated binary gating in safety outcomes or advice retention under degraded input conditions. No definitive benchmarking references with verifiable DOIs addressing both methods simultaneously.

## Study Scope

**Time Period:** 2018–2024 **Disciplines:** AI safety, explainable AI, clinical decision support, vision-language-action, human factors, regulatory science **Methods:** Empirical evaluation, simulation, human-in-the-loop studies, imputation techniques, uncertainty quantification, regulatory analysis

## Assumptions & Limitations

Evidence is synthesized from separate strands; direct comparison is absent. Safety and advice retention outcomes are context-dependent and influenced by task risk, user expertise, and input quality. Imputation and noise-resilience methods are evaluated independently, not in direct relation to advisory restrictions or gating. Regulatory frameworks provide high-level guidance but lack operationalized comparative metrics.

## Suggested Further Research

Design controlled experiments directly comparing intermediate advisory restrictions and calibrated binary gating under systematically degraded input conditions.

Develop standardized benchmarking protocols for safety and advice retention. Integrate uncertainty quantification, explainability, and human-in-the-loop mechanisms in comparative studies. Operationalize regulatory requirements into measurable controls for both advisory and gating mechanisms.

## 1. Introduction

## Scope and Motivation

The increasing deployment of AI in safety-critical domains—such as healthcare, autonomous systems, and decision support—necessitates robust mechanisms for managing advice and interventions, especially when input data is missing, stale, or noisy. Two prominent strategies are **intermediate AI advisory restrictions** (providing nuanced, explainable, or hedged advice) and **calibrated binary gating** (accept/reject decisions based on calibrated risk or confidence thresholds). Understanding their comparative effectiveness in safety outcomes and advice retention is crucial for optimizing AI-human collaboration and regulatory compliance, yet direct comparative evidence remains elusive[10][11][12].

**2. Conceptual Foundations: Advisory Restrictions and Binary Gating**

## Intermediate AI Advisory Restrictions

**Definition:** Mechanisms that provide nuanced, explainable, or hedged advice rather than binary accept/reject outputs. **Use Cases:** Clinical decision support, air traffic control, high-stakes diagnostics. **Challenges:** Over-reliance, under-reliance, hallucinations, explainability trade-offs, human oversight requirements[4][13]. **Explainability:** Visual/textual explanations reduce cognitive workload and improve trust, but may also increase over-reliance if not carefully designed[9][14].

## Calibrated Binary Gating Mechanisms

**Definition:** Systems that make binary decisions (accept/reject) based on calibrated risk or confidence thresholds, often using uncertainty quantification. **Role:** Safety-critical decision-making, especially under domain shifts or noisy inputs. **Empirical Validation:** Improved reliability and reduced calibration error in vision-language-action and clinical tasks; trade-off with intervention frequency[1][10].

## Comparative Framework

**Criteria:** Safety outcomes, advice retention, user trust, intervention frequency, robustness to input degradation.

**Input Data Quality Effects:** Both mechanisms are affected by missing, stale, or noisy inputs, but mitigation strategies differ[9][15][16]. **Synthesis:** While both approaches aim to optimize safety and advice retention, their theoretical underpinnings and practical implementations diverge, with advisory restrictions emphasizing explainability and trust calibration, and binary gating focusing on reliability and calibrated interventions.

## 3. Methods & Data Transparency

**Empirical Studies:** Human-in-the-loop experiments, clinical trials, simulation of domain shifts, benchmarking of imputation methods. **Data Quality Handling:** Multiple imputation, noise-induced regularization, uncertainty-aware gating. **Evaluation Metrics:** Calibration error, intervention frequency, trust scores, advice retention rates, safety benchmarks. **Transparency:** Most studies report methodological details, but direct comparative protocols are lacking; evaluation frameworks are diverse and non-standardized[17][18][19]. **Synthesis:** Methodological diversity is high, but the absence of standardized comparative metrics limits the ability to draw definitive conclusions about relative performance.

## 4. Critical Analysis of Findings

## Safety Outcomes in AI Systems

## Intermediate Advisory Restrictions

**Evidence:** Explainable AI reduces under-reliance and improves diagnostic performance, especially in difficult cases; human oversight is critical for safety[12][20][21].

**Limitations:** Hallucinations and unsafe recommendations persist under degraded input conditions; explainability alone does not guarantee safety[22][23].

**Trade-offs:** Over-refusal of benign queries can reduce utility; nuanced guidance may better balance safety and helpfulness than binary gating[24].

## Calibrated Binary Gating

**Evidence:** Empirically validated in vision-language-action tasks; improves reliability and reduces calibration error under domain shifts and noisy inputs[10][25].

**Trade-offs:** Higher reliability comes with reduced intervention frequency; residual failures occur during pause/fallback states[10].

**Imputation:** Multiple imputation methods outperform complete case analysis for missing binary outcome data, but are not directly linked to advisory restrictions[5].

## Trade-o ff s and Limitations

**Safety vs. Utility:** Both approaches exhibit trade-offs; intermediate restrictions optimize trust and advice retention, binary gating optimizes reliability and intervention efficiency[10][18][22].

**Unresolved Questions:** No direct comparative studies; precise conditions under which one approach outperforms the other remain unclear. **Synthesis:** Both mechanisms have strengths and limitations, but the lack of direct comparison under degraded input conditions is a major gap.

## Advice Retention and User Trust

## Advice Retention under Intermediate Advisory Restrictions

**Evidence:** Verification scaffolding, trust calibration, explainability features improve advice retention and user trust; human-in-the-loop mechanisms are critical[2][16].

**Risks:** Over-reliance and cognitive biases can undermine safety; explanations must be contextually appropriate[13][26].

## Advice Retention under Calibrated Binary Gating

**Evidence:** Uncertainty communication (linguistic hedging, calibrated confidence) reduces blind trust and optimizes advice retention; dynamic transparency and feedback improve trust calibration[3][4][27].

**Limitations:** Users may still overrely on AI advice even when input quality is poor; calibration alone does not fully prevent reliance on stale/noisy inputs[28].

## Human Factors and Trust Calibration

**Socio-technical Factors:** Trust calibration is influenced by transparency, feedback, anthropomorphic cues, and context; dynamic interaction is required[29][30][31].

**Cognitive Biases:** Overtrust increases with task difficulty; interventions like performance feedback and chain-of-thought explanations can reduce under-trust and over-trust[32]. **Synthesis:** Advice retention and trust calibration are complex, context-dependent, and influenced by both system design and human factors. Intermediate restrictions offer nuanced calibration, while binary gating provides clear thresholds but may not fully address trust issues.

## E ff ects of Input Data Quality

## Impact of Degraded Inputs on Safety and Advice Retention

**Evidence:** Degraded input data (missing, stale, noisy) negatively impacts advice retention and trust; explainability and imputation methods help but are not directly linked to comparative performance[5][33] [34].

**Risks:** Hallucinations and unsafe advice persist; users tend to overrely on AI even when data quality is poor[35][36].

## Mitigation Strategies for Input Quality Issues

**Approaches:** Multiple imputation, noise-induced regularization, uncertainty-aware gating improve robustness to degraded inputs[6][25][37].

**Limitations:** No direct evaluation of these strategies in the context of advisory restrictions vs. binary gating.

## Unresolved Questions and Research Gaps

**Gaps:** Direct comparison of advisory restrictions and binary gating under degraded input conditions is absent; standardized safety and advice retention metrics are needed[5][38][39]. **Synthesis:** Input data quality is a critical factor affecting both safety and advice retention, but current research does not directly link mitigation strategies to comparative performance between advisory restrictions and binary gating.

## Regulatory and Governance Frameworks

## Regulatory Standards and Risk Management

**Frameworks:** EU AI Act, ISO/IEC 24001, NIST AI RMF require human oversight, robustness, and calibrated controls; risk-based models calibrate requirements to severity and uncertainty[7][8][40].

**Obligations:** Organizations must implement architecture-level controls, including advisory restrictions and gating mechanisms.

## Operationalization of Advisory Restrictions and Gating

**Implementation:** Task allocation, escalation protocols, confidence calibration thresholds operationalize regulatory requirements; three-layer standards framework integrates technical, procedural, and accountability standards[41][42][43]. **Synthesis:** Regulatory frameworks provide high-level guidance but lack operationalized comparative metrics; implementation varies by context and system design.

## 5. Real-world Implications

**Clinical Decision Support:** Intermediate advisory restrictions improve trust and safety with human oversight, but hallucinations and unsafe advice persist; binary gating improves reliability but may reduce utility and advice retention[10][12][20].

**Vision-Language-Action Tasks:** Calibrated binary gating mechanisms validated for reliability and robustness under domain shifts and noisy inputs; trade-off with intervention frequency[1][10].

**Human Factors:** Trust calibration and advice retention are influenced by transparency, feedback, and context; over-reliance and cognitive biases are risks in both approaches[29][30].

**Regulatory Compliance:** High-level standards require both advisory restrictions and gating mechanisms; operationalization depends on system design and risk context[7][8]. **Synthesis:** Real-world deployment requires balancing safety, utility, trust, and regulatory compliance; both mechanisms have strengths and limitations, but direct comparative evidence is lacking.

## 6. Future Research Directions

**Direct Comparative Studies:** Design controlled experiments comparing intermediate advisory restrictions and calibrated binary gating under systematically degraded input conditions. **Standardized Metrics:** Develop unified benchmarking protocols for safety and advice retention. **Integrated Approaches:** Combine uncertainty quantification, explainability, and human-in-the-loop mechanisms in comparative studies. **Regulatory Operationalization:** Translate high-level regulatory requirements into measurable controls for both advisory and gating mechanisms. **Human Factors Research:** Investigate socio-technical and psychological factors influencing trust

calibration and advice retention in diverse contexts. **Synthesis:** Addressing these gaps will enable evidence-based optimization of AI advisory and gating mechanisms, improving safety, advice retention, and trust in high-stakes applications.

## Discussion: Synthesis and Future Directions

## Established Findings

**Separate Evidence:** Intermediate advisory restrictions improve trust and advice retention through explainability and verification scaffolding; binary gating improves reliability and safety through calibrated interventions[10][12][13].

**Trade-offs:** Both approaches exhibit trade-offs between safety, utility, intervention frequency, and trust calibration.

**Regulatory Standards:** High-level frameworks require both mechanisms but lack operationalized comparative metrics.

## Unresolved Questions and Competing Studies

**Research Gap:** No direct comparative studies; precise conditions under which one approach outperforms the other remain unclear[5][38][44]. **Closest Competing Studies:** Advisory restrictions—explainable AI and trust calibration[2][9]; binary gating—vision-language-action tasks[1][10]. **Benchmarking:** Standardized safety and advice retention metrics are needed for unified evaluation.

## Recommendations for Research and Practice

**Experimental Design:** Conduct head-to-head studies under controlled input degradation. **Benchmark Development:** Create standardized protocols for safety and advice retention. **Integrated Mechanisms:** Combine explainability, uncertainty quantification, and human-in-the-loop approaches. **Regulatory Translation:** Operationalize regulatory requirements into measurable controls. **Human-Centric Design:** Address socio-technical and psychological factors in trust calibration and advice retention.

## Conclusion:

Current peer-reviewed literature does not provide a direct comparison between intermediate AI advisory restrictions and calibrated binary gating regarding safety outcomes and advice retention under degraded input conditions. Individual studies highlight strengths and trade-offs, but unified evaluation frameworks are needed. Future research should bridge these strands, leveraging uncertainty communication, explainability, and standardized metrics to optimize AI safety and advice retention in real-world applications.

## References

1. ViLU: Learning Vision-Language Uncertainties for Failure Prediction Lafon, M., Karmim, Y., Silva- Rodríguez, J., (...), Thome, N. Proceedings of the IEEE International Conference on Computer Vision, 2025 https://www.scopus.com/pages/publications/105044230126?origin=scopusAI

2. Trusting the Middle in the TNO Trust Task: How Medium Risk and Reliability Shape AI-Assisted Advice-Taking Sun, Z., Ding, J. Human Behavior and Emerging Technologies, 2025 https://www.scopus.com/pages/publications/105022635760?origin=scopusAI

3. Calibrating Uncertainty in Generative Language Interfaces: A Behavioral Economics Framework for Engagement and Conversion Para, R., Krishnamoorthy, D. International Conference on Intelligent Communication Networks and Computational Techniques, ICICNCT 2025, 2025 https://www.scopus.com/pages/publications/105030474376?origin=scopusAI

4. Linguistic Uncertainty Markers for Trust Calibration in AI-Assisted Decision-Making Spillner, L., Rockstroh, J., Wenig, N., (...), Malaka, R. CUI 2026 - Proceedings of the 2026 Conference on Conversational User Interfaces, 2026 https://www.scopus.com/pages/publications/105046112431?origin=scopusAI

5. A Systematic Survey of the Optimal Strategy for Dealing With Missing Binary Outcomes in Simulation Studies of Randomized Controlled Trials Shen, Y., Sameer, P., Xia, X., (...), Gordon, G. Journal of Evidence- Based Medicine, 2025 https://www.scopus.com/pages/publications/105014122113?origin=scopusAI

6. Multiple Imputation via Generative Adversarial Network for High-dimensional Blockwise Missing Value Problems Dai, Z., Bu, Z., Long, Q. Proceedings - 20th IEEE International Conference on Machine Learning and Applications, ICMLA 2021, 2021 https://www.scopus.com/pages/publications/85125848302?origin=scopusAI

7. From Architecture to Compliance: A Model-Driven Assessment of AI Systems Ekeh, I.F., Matulevi č ius, R., Affia-Jomants, A.-A., Karagjaur, M. Lecture Notes in Business Information Processing, 2026 https://www.scopus.com/pages/publications/105041852166?origin=scopusAI

8. Risk, Reasonableness and Residual Harm under the EU AI Act: A Conceptual Framework for Proportional Ex-Ante Controls Teichmann, F. European Journal of Risk Regulation, 2026 https://www.scopus.com/pages/publications/105028035734?origin=scopusAI

9. Explainable artificial intelligence in air traffic control: effects of expertise on workload, acceptance, and usage intentions Cartocci, G., Veyrié, A., Cavagnetto, N., (...), Aricò, P. Brain Informatics, 2026 https://www.scopus.com/pages/publications/105033819242?origin=scopusAI

10. Uncertainty-Calibrated Safety Gating for Vision–Language– Action Manipulation Under Domain Shift: Reliability Gains and Intervention–Efficiency Trade-Offs Ghaleb, A.M., Allahloh, A.S., Mejjaouli, S., (...),

Al-Shayea, A. Sensors, 2026 https://www.scopus.com/pages/publications/105040252138?origin=scopusAI

11. Analysis of responses from artificial intelligence programs to medication-related questions derived from critical care guidelines Williams, B., Erstad, B.L. American Journal of Health-System Pharmacy, 2025 https://www.scopus.com/pages/publications/105016832580?origin=scopusAI

12. Performance and safety of a fine-tuned small language model for pediatric emergency triage: A benchmark study Lee, E.J., Jung, J.Y., Kim, D.K., (...), Kwak, Y.H. PLOS One, 2026 https://www.scopus.com/pages/publications/105041057156?origin=scopusAI

13. Examining reliance patterns on AI advice in medical imaging: a mixed-methods, randomised, crossover experiment Gaube, S., Jussupow, E., Kokje, E., (...), Colak, E. The Lancet Digital Health, 2026 https://www.scopus.com/pages/publications/105054111599?origin=scopusAI

14. Fool Me Once? Contrasting Textual and Visual Explanations in a Clinical Decision-Support Setting Kayser, M., Menzat, B., Emde, C., (...), Camburu, O.-M. EMNLP 2024 - 2024 Conference on Empirical Methods in Natural Language Processing, Proceedings of the Conference, 2024 https://www.scopus.com/pages/publications/85217771428?origin=scopusAI

15. AI SAFETY: PERFORMANCE METRICS AND FAILURE MODES Ranieri, C., Lecis, P.O., Castaldi, L. 51st European Rotorcraft Forum, ERF 2025, 2025 https://www.scopus.com/pages/publications/105038941986?origin=scopusAI

16. Seeing is believing: how (X)AI-augmented advice guides human evidence accumulation in perceptual decision-making Bershadskyy, D., Heinrich, K., Sachs, F.E. European Journal of Information Systems, 2026 https://www.scopus.com/pages/publications/105054503417?origin=scopusAI

17. Mitigating Algorithmic Bias Through Probability Calibration: A Case Study on Lead Generation Data Nikoli ć, M., Nikoli ć, D., Stefanovi ć, M., (...), Stefanovi ć, D. Mathematics, 2025 https://www.scopus.com/pages/publications/105010300714?origin=scopusAI

18. Evaluating Model-Free Reinforcement Learning toward Safety-Critical Tasks Zhang, L., Zhang, Q., Shen, L., (...), Tao, D. Proceedings of the 37th AAAI Conference on Artificial Intelligence, AAAI 2023, 2023 https://www.scopus.com/pages/publications/85167964284?origin=scopusAI

19. Preference-based probabilistic planning with partially-ordered temporal goals Rahmani, H., Kulkarni, A.N., Fu, J. Automatica, 2026 https://www.scopus.com/pages/publications/105030828167?origin=scopusAI

20. Enhancing Clinician Trust in AI Diagnostics: A Dynamic Framework for Confidence Calibration and Transparency Yu, Y., Gomez-Cabello, C.A., Haider, S.A., (...), Forte, A.J. Diagnostics, 2025 https://www.scopus.com/pages/publications/105015487559?origin=scopusAI

21. Evaluating the impact of explainable AI on clinicians’ decision-making: A study on ICU length of stay prediction Jung, J., Kang, S., Choi, J., (...), Kim, H. International Journal of Medical Informatics, 2025 https://www.scopus.com/pages/publications/105004061746?origin=scopusAI

22. Governing AI reasoning to mitigate assumption injection in assurance workflows Wen, S.-F. Discover Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105052045266?origin=scopusAI

23. Ontological Foundations for Deterministic Assurance Context Construction and Governed AI Reasoning Wen, S.-F. Applied Sciences (Switzerland), 2026 https://www.scopus.com/pages/publications/105031456507?origin=scopusAI

24. Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context Zhang, Z., Huang, L., Wu, G., (...), Naseem, U. Proceedings of the Annual Meeting of the Association for Computational Linguistics, 2026 https://www.scopus.com/pages/publications/105053542769?origin=scopusAI

25. Visual-Independent Affective Computing: A Hardware-Aware Statistical Circuit Breaker for Extreme Noise Resilience in Dual-Stream Acoustic Emotion Recognition Mahmud, M.D.Z. IEEE Access, 2026 https://www.scopus.com/pages/publications/105050172254?origin=scopusAI

26. Improving Trust in AI with Mitigating Confirmation Bias: Effects of Explanation Type and Debiasing Strategy for Decision-Making with Explainable AI Ha, T., Kim, S. International Journal of Human- Computer Interaction, 2024 https://www.scopus.com/pages/publications/85178011642?origin=scopusAI

27. Human-Aligned Calibration for AI-Assisted Decision Making Corvelo Benz, N.L., Rodriguez, M.G. Advances in Neural Information Processing Systems, 2023 https://www.scopus.com/pages/publications/85188262930?origin=scopusAI

28. Towards a Trust Reliance Paradox? Exploring the Gap Between Perceived Trust in and Reliance on Algorithmic Advice Schmitt, A., Wambsganss, T., Söllner, M., Janson, A. 42nd International Conference on Information Systems, ICIS 2021 TREOs: "Building Sustainability and Resilience with IS: A Call for Action", 2021 https://www.scopus.com/pages/publications/85144797229?origin=scopusAI

29. Too Much, Too Little, Just Right? Towards Dimensions of Trust Calibration in Human-AI Interaction Börsting, I., Hesenius, M. CUI 2026 - Proceedings of the 2026 Conference on Conversational User Interfaces, 2026 https://www.scopus.com/pages/publications/105046127514?origin=scopusAI

30. Confidence-Based Trust Calibration in Human-AI Teams Ibrahim, M. International Journal of Advanced Computer Science and Applications, 2025 https://www.scopus.com/pages/publications/105028653539?origin=scopusAI

31. The role of behavioral anthropomorphism in human-automation trust calibration Jensen, T., Khan, M.M.H., Albayram, Y. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2020 https://www.scopus.com/pages/publications/85088746569?origin=scopusAI

32. Building Appropriate Trust in Artificial Intelligence: Examining a Dynamic Trust Calibration Model and an Intervention Xu, S., Gong, Z., Li, Y., (...), Ahsan, A. International Journal of Human-Computer Interaction, 2026 https://www.scopus.com/pages/publications/105048822558?origin=scopusAI

33. Quality of data sets that feed AI and big data applications for law enforcement Kusak, M. ERA Forum, 2022 https://www.scopus.com/pages/publications/85139964414?origin=scopusAI

34. Not All Missing Data are Equal: Choosing the Right Imputation Method for Binary Datasets Delfino, M., Rapallo, F. Quality and Reliability Engineering International, 2026 https://www.scopus.com/pages/publications/105045494595?origin=scopusAI

35. Trust and reliance on AI — An experimental study on the extent and costs of overreliance on AI Klingbeil, A., Grützner, C., Schreck, P. Computers in Human Behavior, 2024 https://www.scopus.com/pages/publications/85199701123?origin=scopusAI

36. Explainability does not mitigate the negative impact of incorrect AI advice in a personnel selection task Cecil, J., Lermer, E., Hudecek, M.F.C., (...), Gaube, S. Scientific Reports, 2024

https://www.scopus.com/pages/publications/85191728904?origin=scopusAI

37. Exploring noise-induced techniques to strengthen deep learning model resilience Ganie, A.G., Dadvadipour, S. Pollack Periodica, 2024 https://www.scopus.com/pages/publications/85198914317?origin=scopusAI

38. A robust Bayesian and game-theoretic framework for certifying AI-enabled safety-critical systems under structural misspecification Anzum, K.M.T., Shahriar, A. Scientific Reports, 2026 https://www.scopus.com/pages/publications/105055268580?origin=scopusAI

39. Navigating Transparency: The Influence of On-demand Explanations on Non-expert User Interaction with AI Papenkordt, J. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2024 https://www.scopus.com/pages/publications/85196183119?origin=scopusAI

40. Operationalising AI Governance in Public Administration: An Integrated Regulatory and Risk Management Framework Levantis, N., Sgora, A., Tsipis, A., Polykalas, S. Information (Switzerland), 2026 https://www.scopus.com/pages/publications/105054997431?origin=scopusAI

41. Toward a Standards Framework for Hybrid Intelligence Governance: Integrating Human Judgment and AI Decision Support Aliba š i ć, H. Standards, 2026 https://www.scopus.com/pages/publications/105049868558?origin=scopusAI

42. A comprehensive approach to safety for highly automated off-road machinery under Regulation 2023/1230 de Koning, M., Machado, T., Ahonen, A., (...), Ghabcheloo, R. Safety Science, 2024 https://www.scopus.com/pages/publications/85189083993?origin=scopusAI

43. Towards an international regulatory framework for AI safety: lessons from the IAEA’s nuclear safety regulations Cha, S. Humanities and Social Sciences Communications, 2024 https://www.scopus.com/pages/publications/85190270476?origin=scopusAI

44. Multiple imputation for handling missing outcome data when estimating the relative risk Sullivan, T.R., Lee, K.J., Ryan, P., Salter, A.B. BMC Medical Research Methodology, 2017 https://www.scopus.com/pages/publications/85028939807?origin=scopusAI
