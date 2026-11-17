---
source_pdf: "Search 4 Empirical Comparisons of Participation-Only and Intermediate Action-Scope Safety Gates- Measurement, Methodology, and Reporting Practices.pdf"
source_sha256: "bde6d3015663e6666c32c9bd1c525fe5a9079e2191ca8f9dc8a2031a3f0c5240"
source_pages: 11
scopus_ai_generated: "Wed Sep 23 2026"
query: "Empirical studies on safety gate designs"
report_title: "Empirical Comparisons of Participation-Only and Intermediate Action-Scope Safety Gates: Measurement, Methodology, and Reporting Practices"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Empirical studies on safety gate designs

## Quick Reference

## Key Findings Table

| Research Question | Closest Empirical Evidence Found | Direct Comparative Data? | Activation Frequency Measured? | Marginal Effect Isolated? | Key Limitations |
| --- | --- | --- | --- | --- | --- |
| Direct comparison of participation-only vs. intermediate action-scope safety gates | No direct empirical studies; related analyses in digital valve controllers, accelerator interlocks, and safety instrumented systems | No | Rarely, inconsistently | No | Lack of standardized protocols, indirect evidence, inconsistent reporting |
| Frequency of intermediate restriction changing permitted actions | Modeled in probabilistic safety analysis, Markov models, and human reliability analysis | Indirect | Sometimes (spurious trips) | Sometimes (via modeling) | Not systematically measured or reported; often inferred from system-level reliability analyses |
| Use of comparator/ablation to isolate marginal effect | Rare; some use of segmented regression, marginal structural models, and advanced analytics in related domains | Rare | N/A | Sometimes (indirect) | Not applied directly to safety gate design comparisons |
| Reporting of activation frequency | Inconsistent; some studies report spurious activation rates in SIS, but not standardized across domains | N/A | Sometimes | N/A | Measurement protocols and reporting vary widely, limiting comparability |

## Direct Answer

Empirical studies that directly compare participation-only or binary safety gates with intermediate action-scope restrictions—especially in systems where one design allows full actions at intermediate risk while another restricts the action set—are currently lacking. Existing literature provides analyses on related systems (e.g., digital valve controllers, accelerator safety interlocks), but these do not consistently measure how often intermediate restrictions change permitted actions, do not consistently use comparators or ablation designs to isolate marginal effects, and rarely report activation frequency in a standardized manner. The field is marked by methodological gaps and inconsistent reporting practices, impeding direct empirical comparison and quantification of marginal effects between these safety gate designs[1][2][3][4].

## Study Scope

**Time Period:** Most relevant studies and reviews span the last 10–20 years, with a focus on recent advances in digital safety systems and human reliability analysis.

**Disciplines:** Industrial control systems, safety instrumented systems, human factors engineering, reliability engineering, behavioral safety science.

**Methods:** Probabilistic safety analysis, Markov modeling, human reliability analysis (ATHEANA, MERMOS), segmented regression, marginal structural models, Bayesian kernel machine regression, fault tree analysis, FMEA, formal verification.

## Assumptions & Limitations

**Assumptions:** The review assumes that related studies in digital valve controllers, accelerator safety interlocks, and human reliability analysis provide the closest available empirical evidence, even if not direct comparisons.

**Limitations:** There is a lack of direct, side-by-side empirical studies; most evidence is indirect, model-based, or focused on related but not identical system designs. Reporting of activation frequency and marginal effect isolation is inconsistent and non-standardized, limiting comparability.

## Suggested Further Research

Design controlled experiments or quasi-experimental studies in industrial environments to directly compare participation-only and intermediate action-scope safety gates. Develop and standardize measurement protocols for activation frequency and marginal effect isolation. Integrate digital monitoring with advanced statistical models (e.g., Bayesian kernel machine regression) to improve quantification and comparability. Foster cross-disciplinary collaboration between safety engineers, human factors experts, and data scientists to address methodological gaps.

## 1. Introduction

## Background and Motivation

Safety gates—mechanisms that restrict or permit actions in safety-critical systems—are foundational to risk management in industrial, medical, and technological domains. Two principal designs are prevalent: **participation-only (binary) safety gates**, which allow or block all actions based on a threshold, and **intermediate action-scope restrictions**, which selectively restrict subsets of actions at intermediate risk levels. The distinction is crucial: while binary gates offer simplicity, intermediate restrictions promise nuanced risk mitigation by tailoring permitted actions to context.

Despite their theoretical importance, empirical evidence directly comparing these designs—especially regarding how often intermediate restrictions alter permitted actions, their marginal effects, and activation frequency—is sparse. This gap is significant, as the choice of safety gate design can profoundly affect operational reliability, human error rates, and overall system safety[1][2].

## 2. Theoretical Frameworks

**Participation-Only vs. Intermediate Action-Scope Safety Gates**

**Participation-Only (Binary) Safety Gates:** Permit or block all actions based on a binary risk assessment. Common in traditional safety instrumented systems (SIS) and many industrial applications.

**Intermediate Action-Scope Restrictions:** Allow a subset of actions at intermediate risk levels, restricting only those deemed unsafe while permitting others. Increasingly relevant in digital and programmable safety systems.

## Conceptual Distinctions

Feature Participation-Only (Binary) Intermediate Action-Scope Restriction Action Set at Intermediate Risk All actions permitted Subset of actions permitted Operator Flexibility High Moderate to low Risk Mitigation Granularity Coarse Fine-grained Implementation Complexity Low High

## Theoretical Rationale

**Binary gates** are easier to implement and verify but may be overly restrictive or insufficiently nuanced for complex, dynamic environments.

**Intermediate restrictions** can better balance safety and operational flexibility but require sophisticated modeling, monitoring, and human factors integration[5][6][7].

## 3. Methods & Data Transparency

## Review Methodology

**Scope:** Focused on empirical studies and systematic reviews in safety-critical domains (industrial control, digital valve controllers, accelerator safety interlocks, human reliability analysis).

**Data Sources:** Meta-analyses, systematic reviews, and primary studies identified through structured literature mapping.

**Key Metrics:** Frequency of intermediate restriction activation, use of comparators/ablations, marginal effect isolation, and reporting practices.

## Data Limitations

**Direct Empirical Comparisons:** None found; evidence is indirect or model-based. **Activation Frequency:** Sometimes reported as spurious trip rates or through probabilistic models, but not standardized. **Marginal Effect Isolation:** Rarely implemented; some use of advanced statistical models in related domains.

## 4. Critical Analysis of Findings

## 4.1 Empirical Evidence on Safety Gate Mechanisms

**Comparative Studies in Safety Instrumented and Control Systems** **No direct empirical studies** compare participation-only and intermediate action-scope restrictions in systems allowing full actions at intermediate risk[1][2]. **Related evidence**: **Digital valve controllers**: Improve reliability and diagnostics over traditional binary gates, but studies focus on operational outcomes rather than direct design comparisons[8][9]. **Accelerator safety interlocks**: Surveyed across international labs, but lack self-consistent comparative methods for gate design types[2]. **Multistate production systems**: Use probabilistic models (fault trees, Markov, Petri nets) to analyze safety, but do not isolate marginal effects of intermediate restrictions[5].

## Empirical Gaps and Methodological Challenges

**Marginal effect isolation**: Rarely achieved; most studies do not use comparators or ablation designs[10][11]. **Measurement of activation frequency**: Inconsistent; spurious activation rates sometimes reported in SIS, but not standardized[12][13]. **Behavioral and contextual factors**: Significantly influence safety engagement metrics, complicating direct comparison of gate designs[14][15].

## Synthesis

The empirical landscape is characterized by indirect evidence, with most studies focusing on system-level reliability or human factors without directly comparing safety gate designs. Methodological challenges— especially in isolating marginal effects and standardizing activation frequency measurement—persist across domains.

## 4.2 Measurement and Analysis of Intermediate Restrictions

## Frequency and Impact of Intermediate Restrictions

**Intermediate restrictions** can trigger complex risk abatement actions, sometimes creating new hazards or complicating operator response[16].

**Frequency of change in permitted actions**: Modeled probabilistically (e.g., spurious trip rates in SIS), but rarely measured directly in operational settings[12][13].

**Operational consequences**: Spurious activations can cause production interruptions, economic loss, and safety risks during restoration[12].

## Methodologies for Marginal Effect Isolation

**Probabilistic Safety Analysis (PSA)**: Screens risks and guides corrective actions, sometimes modeling the impact of intermediate restrictions[17][18].

**Segmented regression and marginal structural models**: Used in related domains to estimate intervention effects, but not directly applied to safety gate design comparisons[19][20].

**Bayesian Kernel Machine Regression (BKMR)**: Quantifies joint, nonlinear effects of mixed exposures, offering potential for future application[21].

**Human reliability analysis (ATHEANA, MERMOS)**: Models context-specific error probabilities, capturing the impact of intermediate restrictions on operator behavior[22][23][24].

## Activation Frequency: Measurement and Reporting

**Spurious activation rates**: Quantified using analytical formulas and optimization algorithms (e.g., Particle Swarm Optimization), but reporting is inconsistent[12][25][26]. **Industry standards (IEC 61508, IEC 61511)**: Provide frameworks for defining and calculating spurious activation rates, but do not mandate specific reporting protocols[13]. **Comparative Strengths and Limitations of Quantification Methodologies** Methodology Strengths Limitations Simplified equations User-friendly, quick estimates Less detailed, may miss complex interactions

Methodology Strengths Limitations Fault tree analysis Visualizes fault causation, Can be complex for large systems (FTA) qualitative/quantitative Markov modeling Captures dynamic behavior, comprehensive Computationally intensive, complex FMEA Identifies failure modes, qualitative May miss system-level interactions PSA Probabilistic quantification, integrates multiple Data-intensive, requires expertise methods Formal verification Rigorous, efficient for discrete systems Requires formal modeling, expertise Human reliability Context-sensitive, models human error Data collection intensive, context-analysis dependent

## Synthesis

While a variety of methodologies exist to model and quantify the effects of intermediate restrictions, none are routinely used to directly compare safety gate designs. Reporting of activation frequency and marginal effect isolation is inconsistent, and methodological variability limits comparability.

**4.3 Characterization and Reporting Practices in Safety Gate Studies**

## System Types and Methodological Approaches

**Studied systems**: Accelerator safety interlocks, digital valve controllers, medical devices, industrial controls, and behavioral safety interventions[2][6][27][28][29][30].

**Methodologies**: RCTs, observational studies, probabilistic modeling, human reliability analysis, and advanced analytics[31][32].

## Gaps in Activation Frequency Measurement and Reporting

**Variability in protocols**: Differences in device characteristics, sampling rates, calibration, and data processing[3][4]. **Lack of standardization**: Limits comparability and reproducibility across studies[33][34]. **Pooling multicenter data**: Can improve reliability but requires harmonized protocols[4].

## Influence of Behavioral and Contextual Factors

**Psychological safety, leadership, work pressure, trust, and engagement**: All affect the reliability of participation and safety engagement metrics[14][15][35][36].

**Measurement tools**: Vary in conceptual focus and psychometric validity, requiring further development[37] [38][39].

## Best Practices for Activation Measurement and Reporting

**Standardization of protocols**: Improves comparability and reliability[33][40]. **Multicenter data pooling**: Enhances reproducibility[4]. **Advanced data processing**: Improves detection sensitivity and comparability[41][42].

## Synthesis

The field is marked by methodological diversity and inconsistent reporting, particularly regarding activation frequency and the influence of behavioral/contextual factors. Standardization and harmonization of measurement protocols are urgently needed.

## 5. Real-World Implications

**Operational Reliability:** The lack of direct empirical comparisons limits evidence-based decision-making in selecting safety gate designs for critical systems.

**Human Factors:** Intermediate restrictions may offer better alignment with human operator capabilities, but their impact is underexplored due to measurement and reporting gaps.

**System Safety:** Inconsistent quantification of activation frequency and marginal effects may obscure true risk profiles, potentially leading to suboptimal safety interventions.

**Regulatory Compliance:** Without standardized reporting, compliance with safety standards (e.g., IEC 61508/61511) may be uneven, affecting both safety and operational efficiency.

## 6. Future Research Directions

## Summary of Key Insights

There is a **notable absence of direct empirical studies** comparing participation-only and intermediate action-scope safety gates.

**Methodological advancements** (e.g., advanced analytics, human reliability analysis) offer promise but are not yet fully applied to this comparison.

**Measurement and reporting practices** are inconsistent, particularly regarding activation frequency and marginal effect isolation.

**Behavioral and contextual factors** significantly influence the reliability of safety engagement metrics, complicating direct comparisons.

## Research Gaps and Methodological Needs

**Direct empirical research**: Needed to compare safety gate designs using controlled or quasi-experimental methods. **Standardized measurement protocols**: Essential for activation frequency and marginal effect isolation. **Integration of advanced analytics**: Application of models like BKMR and marginal structural models to safety gate comparisons. **Cross-disciplinary collaboration**: Safety engineers, human factors experts, and data scientists must work together to address methodological challenges.

## Recommendations for Future Research

**Design and implement controlled studies** in industrial settings to directly compare participation-only and intermediate action-scope safety gates. **Develop and validate standardized protocols** for measuring activation frequency and isolating marginal effects. **Leverage digital monitoring and advanced analytics** to improve quantification and comparability. **Address behavioral and contextual factors** by integrating human factors research into safety gate design and evaluation. **Promote multicenter collaborations** to harmonize protocols and pool data for greater reliability and generalizability.

## Conclusion

The empirical comparison of participation-only and intermediate action-scope safety gates remains an open challenge. While theoretical and methodological advances provide a foundation, the field urgently needs direct, standardized, and context-sensitive empirical research to inform best practices and optimize safety in critical systems. Bridging these gaps will require methodological innovation, cross-disciplinary collaboration, and a commitment to rigorous measurement and reporting standards[1][3][14][19].

## References

1. Struck-by fatalities in construction: A systematic review of regulatory roles, responsibilities, and research gaps Kudlinski, D., Ryu, J. Journal of Safety Research, 2026 https://www.scopus.com/pages/publications/105022620029?origin=scopusAI

2. Survey of electronic safety systems in accelerator applications Mahoney, K. Proceedings of the IEEE Particle Accelerator Conference, 1998 https://www.scopus.com/pages/publications/0032266055?origin=scopusAI

3. Frequency domain and time complex analyses manifest low correlation and temporal variability when calculating activation rates in atrial fibrillation patients Biviano, A.B., Coromilas, J., Ciaccio, E.J., (...), Garan, H. PACE - Pacing and Clinical Electrophysiology, 2011 https://www.scopus.com/pages/publications/79957538817?origin=scopusAI

4. Reproducibility of PET activation studies: Lessons from a multi-center European experiment. EU concerted action on functional imaging Poline, J.-B., Vandenberghe, R., Holmes, A.P., (...), Frackowiak, R.S.J. NeuroImage, 1996 https://www.scopus.com/pages/publications/0030220633?origin=scopusAI

5. Extensions to Production Availability and Functional Safety Analyses Signoret, J.-P., Leroy, A. Springer Series in Reliability Engineering, 2021 https://www.scopus.com/pages/publications/85103236065?origin=scopusAI

6. A functional safety methodology based on IEC 61508 for critical reliability FPGA-based designs Flesch, B.F., Tedeschi, I., De Figueiredo, R.M., (...), Da Silva, M.R. International Journal of Emerging Technology and Advanced Engineering, 2020 https://www.scopus.com/pages/publications/85099576911?origin=scopusAI

7. Case Studies for System Reliability and Risk AssessmentCase studies for system reliability and risk assessment Choi, J.G., Kang, H.G., Seong, P.H. Springer Series in Reliability Engineering, 2009 https://www.scopus.com/pages/publications/84951798158?origin=scopusAI

8. Digital approaches to safety instrumented systems provide faster ROI Fillion, E. Hydrocarbon Processing, 2006 https://www.scopus.com/pages/publications/33751012103?origin=scopusAI

9. Making valve controllers/positioners smarter is smart business Harrold, D. Control Engineering, 2003 https://www.scopus.com/pages/publications/3042550496?origin=scopusAI

10. Practice what you preach and be a control freak Thomas, M.K., Klopfenstein, K. Applied Economics, 2020 https://www.scopus.com/pages/publications/85081296815?origin=scopusAI

11. Chemical safety board investigation reports and the hierarchy of controls: Round 2 Amyotte, P., Irvine, Y., Khan, F. Process Safety Progress, 2018 https://www.scopus.com/pages/publications/85054593646?origin=scopusAI

12. Spurious activation and operational integrity evaluation of redundant safety instrumented systems Qi, M., Kan, Y., Li, X., (...), Moon, I. Reliability Engineering and System Safety, 2020 https://www.scopus.com/pages/publications/85078703615?origin=scopusAI

13. Spurious activation of safety instrumented systems in the oil and gas industry: Basic concepts and formulas Lundteigen, M.A., Rausand, M. Reliability Engineering and System Safety, 2008 https://www.scopus.com/pages/publications/40949092681?origin=scopusAI

14. Safety behaviors and positive emotions in social anxiety disorder Oren-Yagoda, R., Oren, B., Aderka, I.M. Journal of Anxiety Disorders, 2024 https://www.scopus.com/pages/publications/85202075183?origin=scopusAI

15. Analyzing behaviour of safety technologies in construction: An empirical study using the UTAUT Model in Guangdong Province, China Chungang, L., Zhuolin, Z., Yee, C.M., Kharuddin, A.F. Multidisciplinary Science Journal, 2026 https://www.scopus.com/pages/publications/105025955223?origin=scopusAI

16. Risk abatement provided by safety instrumented systems may cause remote hazards with higher risks Sepeda, A.L. AIChE Annual Meeting, Conference Proceedings, 2006 https://www.scopus.com/pages/publications/77953025754?origin=scopusAI

17. Resolution of the pressure locking issue of safety related MOVs at NPP Krško Bajs, T., Balić, M., Sember, B. International Conference on Nuclear Engineering, Proceedings, ICONE, 2012 https://www.scopus.com/pages/publications/84890110604?origin=scopusAI

18. Resolution of the Thermal Binding issue of safety related MOVs at NPP Krško Balić, M., Bajs, T., Sember, B. American Society of Mechanical Engineers, Power Division (Publication) POWER, 2013 https://www.scopus.com/pages/publications/84896301787?origin=scopusAI

19. Evaluation of two Japanese regulatory actions using medical information databases: A 'Dear Doctor' letter to restrict oseltamivir use in teenagers, and label change caution against co-administration of omeprazole with clopidogrel Hanatani, T., Sai, K., Tohkin, M., (...), Saito, Y. Journal of Clinical Pharmacy and Therapeutics, 2014 https://www.scopus.com/pages/publications/84904152505?origin=scopusAI

20. How to use marginal structural models in randomized trials to estimate the natural direct and indirect effects of therapies mediated by causal intermediates Oba, K., Sato, T., Ogihara, T., (...), Nakao, K. Clinical Trials,

2011 https://www.scopus.com/pages/publications/79960261022?origin=scopusAI

21. Mixture effects of multiple exposures on driving safety at tunnel entrances and exits: A Bayesian kernel machine regression (BKMR) method Bai, C., Luo, Y., Wang, W., (...), Song, X. Accident Analysis and Prevention, 2026 https://www.scopus.com/pages/publications/105043990421?origin=scopusAI

22. MERMOS catalogue: Use of generic analyses to improve the HRA method Le Bot, P., Pesme, H. 11th International Probabilistic Safety Assessment and Management Conference and the Annual European Safety and Reliability Conference 2012, PSAM11 ESREL 2012, 2012 https://www.scopus.com/pages/publications/84873159069?origin=scopusAI

23. Application of ATHEANA in human failure events analysis He, X.-H., Wang, Y., Huang, X.-R. Hedongli Gongcheng/Nuclear Power Engineering, 2005 https://www.scopus.com/pages/publications/33644960502?origin=scopusAI

24. Human-Machine interface (HMI) scenario quantification performed by ATHEANA, A Technique for Human Error Analysis Pinto, J.M.O., Frutuoso E Melo, P.F., Saldanha, P.L.C. Safety and Reliability of Complex Engineered Systems - Proceedings of the 25th European Safety and Reliability Conference, ESREL 2015, 2015 https://www.scopus.com/pages/publications/84959036512?origin=scopusAI

25. Spurious Trip Rate Optimization Using Particle Swarm Optimization Algorithm Eddine, B.H., Riad, B., Youcef, Z. International Journal of Safety and Security Engineering, 2024 https://www.scopus.com/pages/publications/85187929268?origin=scopusAI

26. Cost Effective Analysis of the Design of Safety Instrumented Systems Using Manta-Ray Foraging Optimization Algorithm Berrah, F., Chebila, M., Innal, F., Got, A. International Journal of Safety and Security Engineering, 2023 https://www.scopus.com/pages/publications/85183095305?origin=scopusAI

27. Building Australia’s non-animal technologies ecosystem: a national cross-sector mapping and strategic insights from the non-animal technologies network (NAT-Net) Waters, S.A., Hill, A.P., Pronker, E.S., (...), Gonzalez-Cordero, A. Frontiers in Toxicology, 2026 https://www.scopus.com/pages/publications/105041479598?origin=scopusAI

28. Efficacy and Safety of Different Hybrid Closed Loop Systems for Automated Insulin Delivery in People With Type 1 Diabetes: A Systematic Review and Network Meta-Analysis Di Molfetta, S., Di Gioia, L., Caruso, I., (...), Giorgino, F. Diabetes/Metabolism Research and Reviews, 2024 https://www.scopus.com/pages/publications/85204512295?origin=scopusAI

29. Evaluating automatic hand hygiene monitoring systems: A scoping review Tseng, C., He, X., Chen, W., Tseng, C.-L. Public Health in Practice, 2022 https://www.scopus.com/pages/publications/85133564008?origin=scopusAI

30. Requirements for testing pedestrian aeb systems – Results from the aspecss FP7 project Seiniger, P., Bartels, O., Wisch, M., (...), Rigling, A. FISITA 2014 World Automotive Congress - Proceedings, 2014 https://www.scopus.com/pages/publications/85060432836?origin=scopusAI

31. The role of randomized controlled trials, registries, observational databases in evaluating new interventions Gale, R.P., Zhang, M.-J., Lazarus, H.M. Best Practice and Research: Clinical Haematology, 2023 https://www.scopus.com/pages/publications/85175540912?origin=scopusAI

32. Variation in research designs used to test the effectiveness of dissemination and implementation strategies: A review Mazzucca, S., Tabak, R.G., Pilar, M., (...), Brownson, R.C. Frontiers in Public Health, 2018 https://www.scopus.com/pages/publications/85045252947?origin=scopusAI

33. Muscle activation assessment: Effects of method, stimulus number, and joint angle Bampouras, T.M., Reeves, N.D., Baltzopoulos, V., Maganaris, C.N. Muscle and Nerve, 2006 https://www.scopus.com/pages/publications/33845285526?origin=scopusAI

34. Influence of ANOVA design and anatomical standardization on statistical mapping for PET activation Senda, M., Ishii, K., Oda, K., (...), Tatsumi, I. NeuroImage, 1998 https://www.scopus.com/pages/publications/0032190316?origin=scopusAI

35. Assessing the effects of safety leadership, employee engagement, and psychological safety on safety performance Quansah, P.E., Zhu, Y., Guo, M. Journal of Safety Research, 2023 https://www.scopus.com/pages/publications/85169839745?origin=scopusAI

36. Safety Leadership, Covid-19 Risk Perception, and Safety Behavior: The Moderator Role of Work Pressure Hiep, H.Y., Hien, N.N. International Journal of Safety and Security Engineering, 2023 https://www.scopus.com/pages/publications/85164360247?origin=scopusAI

37. Safety leadership, safety attitudes, safety knowledge and motivation toward safety-related behaviors in electrical substation construction projects Basahel, A.M. International Journal of Environmental Research and Public Health, 2021 https://www.scopus.com/pages/publications/85104116749?origin=scopusAI

38. Design and validation of an instrument to measure the level of worker participation in an Occupational Health and Safety Management System Alegre-Quintana, J., Gutiérrez-Falcón, P., Agustini-Paredes, L. Archivos de Prevencion Riesgos Laborales, 2024 https://www.scopus.com/pages/publications/85199994828?origin=scopusAI

39. Implementing the theoretical domains framework in occupational safety: Development of the safety behaviour change questionnaire Morgan, J.I., Curcuruto, M., Steer, M., Bazzoli, A. Safety Science, 2021 https://www.scopus.com/pages/publications/85098947643?origin=scopusAI

40. Identification of key upper-limb muscles during a standardized reach-to-grasp task toward simplified clinical protocols Cabezaolias, C., Garcia, S., Sanchez, C., (...), Urendes, E. Frontiers in Bioengineering and Biotechnology, 2026 https://www.scopus.com/pages/publications/105039885819?origin=scopusAI

41. Improved signal-to-noise in PET activation studies using switched paradigms Cherry, S.R., Woods, R.P., Doshi, N.K., (...), Mazziotta, J.C. Journal of Nuclear Medicine, 1995 https://www.scopus.com/pages/publications/0028847571?origin=scopusAI

42. ROC analysis of statistical methods used in functional MRI: Individual subjects Skudlarski, P., Constable, R.T., Gore, J.C. NeuroImage, 1999 https://www.scopus.com/pages/publications/0032807513?origin=scopusAI
