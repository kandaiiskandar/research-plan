---
source_pdf: "Scopus - Scopus AI - formal.pdf"
source_sha256: "d291554969727b9418e5964fd4e9f43aacef2314c1bb8f5ebd99602359710825"
source_pages: 16
scopus_ai_generated: "Thu Apr 16 2026"
query: "Formal architectural layers for AI decision support systems"
report_title: "Formal Architectural Layers and Deterministic Governance in AI Decision Support Systems: Specification, Properties, and Safety Assurance"
converted_tables: 1
converter: "scopus2md.py (pdfplumber)"
---
# Formal architectural layers for AI decision support systems

## Quick Reference

## Key Findings Table

| Theme | Summary | Supporting Citations |
| --- | --- | --- |
| Hierarchical Architectural Approaches | Multi-layer, hierarchical architectures are central to AI decision support systems, emphasizing composability, maintainability, and formal containment hierarchies. | 1 2 3 |
| Deterministic Governance of Probabilistic Outputs | Deterministic runtime layers govern probabilistic AI outputs via formal monitors, runtime assurance, and proof-carrying architectures, ensuring safety dominance and admissible output spaces. | 4 5 6 |
| Formal Specification and Verification | Formal methods (e.g., Z, B, TLA+, VerifAI) are used to define and verify architectural properties such as admissible output spaces, safety dominance, and containment hierarchies. | 7 8 9 |
| Integration of Probabilistic and Deterministic Components | Hybrid architectures combine probabilistic AI with deterministic safety controllers, enforcing runtime safety through formal verification and monitoring. | 10 11 12 |

## Direct Answer

Several lines of work address the need for formal architectural layering in AI decision support systems where deterministic components govern probabilistic outputs. For example, architectures integrating a deterministic verification layer—often implemented via runtime assurance frameworks or simplex structures—have been proposed to enforce formally specified admissible output spaces and containment hierarchies (e.g.,[4][13]). These approaches focus on delineating architectural specifications and formal properties rather than merely proposing algorithms or frameworks, suggesting that such formal specifications can guide the design of systems with provable safety and governance guarantees.

## Study Scope

**Time Period:** Primarily 2010–2024, with foundational works from earlier decades. **Disciplines:** Computer science, AI safety, formal methods, software engineering, cyber-physical systems.

**Methods:** Literature review, meta-analysis, synthesis of architectural models, formal specification languages, runtime assurance frameworks.

## Assumptions & Limitations

**Assumptions:** The report assumes that architectural specifications are distinct from algorithmic or framework proposals, focusing on formal properties and structural organization.

**Limitations:** Explicit formal frameworks linking epistemic uncertainty quantification to deterministic governance layers remain underexplored. Scalability and integration of formal verification with AI training are ongoing challenges.

## Suggested Further Research

Develop unified formal models coupling epistemic uncertainty quantification with deterministic governance. Explore hybrid verification methodologies leveraging machine learning for adaptive formal monitoring. Investigate symbiotic integration of large language models (LLMs) and formal methods for runtime specification and verification.

## 1. Introduction

AI decision support systems (DSS) increasingly underpin critical decision-making in domains ranging from healthcare to autonomous vehicles. The complexity and unpredictability of modern AI—especially probabilistic models—necessitate robust architectural layering, where deterministic components govern and constrain AI outputs at runtime. This report synthesizes literature on formal architectural layers, focusing on structural specifications, containment hierarchies, admissible output spaces, and safety dominance properties, emphasizing architectural design rather than algorithmic implementation.

## 1.1 Background and Motivation

The evolution of AI DSS has shifted from monolithic, rule-based systems to modular, multi-layered architectures integrating probabilistic AI with deterministic governance. The need for formal architectural specifications arises from challenges in ensuring safety, transparency, and accountability, especially as AI systems become more autonomous and complex. Integrating deterministic and probabilistic components is essential for maintainability, composability, and operational reliability in high-stakes environments[1][14][15] [16].

## 2. Theoretical Frameworks

**2.1 Formal Architectural Layers in AI Decision Support Systems**

## 2.1.1 Multi-Layer Architectural Patterns

**Three-layer architectures:** Adaptable, reusable across domains, emphasizing structural organization (e.g., private applications, mediating servers, infrastructure)[1][17].

**Seven-layer models:** Conceptually clear, supporting problem-solving and decision-making, focusing on modularity and adaptability[14].

**Two-layered architectures:** Integrate neural codification with normative reasoning, enhancing transparency and ethical accountability[18].

**Five-stage neurosymbolic frameworks:** Modular, scalable, combining data preprocessing, embedding, domain knowledge, logical reasoning, and postprocessing[19].

**Hierarchical knowledge representation:** Distributed program mechanisms, structurally analogous to biological intelligence[20]. **Synthesis:** Multi-layered architectural patterns provide a foundation for composability and maintainability, enabling modular integration of AI components and deterministic governance layers[1][14][18][19][20].

## 2.1.2 Containment Hierarchies and Modularization

**Mathematical frameworks:** Specify operations and data structures for hierarchical information, supporting containment criteria for data selection[21].

**Constrained Object Hierarchies (COH):** Model components, attributes, methods, and constraints in hierarchical structures for maintainability and verification[22].

**Cognitive models:** Layer data, information, knowledge, and wisdom, informing DSS design for effective human-AI interaction[23][24].

**Modularization strategies:** AI modules operate within hierarchies of ontologies and subtasks, facilitating maintainability and composability[25]. **Synthesis:** Formal containment hierarchies and modularization strategies are central to architectural specifications, supporting maintainability and composability in complex AI DSS[21][22][23][24][26][27][28].

## 2.1.3 Composability and Maintainability

**Layered design:** Modularizes system functions (e.g., data, computing, analysis, application layers)[26]. **Hybrid models:** Combine AI techniques (e.g., LSTM, XGBoost) for feature integration and interpretability [26]. **Knowledge graphs:** Enhance interpretability and transparency[26]. **Agent-based systems:** Enable distributed collaborative decision support[29]. **Federated architectures:** Allow modular sharing and reuse, improving maintainability[27]. **Digital twin-based systems:** Incorporate layers for data acquisition, modeling, risk assessment, and intelligent decision modules[30][31]. **Synthesis:** Multi-layer architectures ensure composability and maintainability through modular design, hybrid integration, and distributed collaboration[26][27][29][30][31][32].

## 2.2 Deterministic Governance of Probabilistic AI Outputs

## 2.2.1 Governance-Oriented Architectures

**Deterministic governance layers:** Oversee and control probabilistic AI outputs, ensuring accountability and compliance[13][33]. **Policy enforcement and audit trails:** Integrated verification and governance layers enforce constraints and human oversight[13]. **Defense-in-Depth (DiD):** Layered governance approach controlling probabilistic risks[34][35]. **Epistemic Gain models:** Monitor and control scaling of probabilistic AI layers[36]. **Hierarchical multi-agent structures:** Secure role-based access controls and causality-augmented decision algorithms[37]. **Causally explainable AI:** Deterministic reasoning layers interpret and govern probabilistic recommendations [38]. **Synthesis:** Governance-oriented architectures integrate deterministic layers to enforce policy constraints, auditability, and operational reliability over probabilistic AI outputs[13][33][39][40].

## 2.2.2 Formal Models and Runtime Assurance

**Probabilistic circuits (PCs):** Balance representational power and computational efficiency, enabling tractable uncertainty handling with provable guarantees[41]. **Runtime monitors (e.g., VerifAI):** Provide runtime assurance for AI/ML-based systems, ensuring safety within operating environments[42]. **Simplex architecture:** Combines complex AI controller with safe deterministic controller, switching control upon safety risks[4]. **Runtime Assurance Architectures (RTAs):** Monitor risk levels and switch to deterministic safety controllers[10]. **RTA-IR framework:** Integrates AI controller with verifiable safety controllers and decision modules[43]. **Bayesian approaches:** Derive context-dependent probabilistic safety violation bounds at runtime[44]. **Markov logic networks:** Combine first-order logic with probabilistic graphical models for provable inference[45]. **Synthesis:** Formal models and runtime assurance architectures provide provable safety guarantees by bounding probabilistic AI outputs with deterministic controllers[4][10][34][35][41][42][43].

## 2.2.3 Formal Languages and Logics for Governance

**B notation:** Used for formal specification in medical DSS[7].

**Z specification language:** Applied to maintain deductive extensions of knowledge bases[46]. **Dynamic Bayesian Networks (DBNs):** Probabilistic formalism for online diagnosis[47]. **Maude:** Rewriting logic-based language for formal specification and model checking[48]. **Temporal Z:** Combines Z and temporal logic for RBAC policies[49]. **PROMELA and Spin:** Specify and verify safety properties under faults[50]. **CafeOBJ:** Algebraic specification for hybrid autonomous vehicle control[51]. **TLA+:** Used for fault-tolerant real-time communication protocols[52]. **PRISM:** Probabilistic model checking with continuous stochastic logic[53]. **Synthesis:** Formal specification languages and logics are essential for defining and verifying governance layers over probabilistic AI in DSS[7][46][47][48][49][50][51][52][53][54].

## 3. Methods & Data Transparency

This report is based on a meta-analytical synthesis of peer-reviewed literature, architectural models, and formal specification frameworks. Data sources include published papers, standards, and toolkits from computer science, AI safety, and formal methods domains. The findings are structured by topic, with iterative refinement and cross-validation of architectural patterns, formal properties, and runtime assurance mechanisms.

## 4. Critical Analysis of Findings

## 4.1 Formal Properties and Specifications in AI Architectures

## 4.1.1 Admissible Output Spaces

**Probabilistic models:** Structured spaces constrained by logical rules (e.g., probabilistic sentential decision diagrams)[55]. **Automata-based formalisms:** Deterministic finite-state automata define probabilistic specifications[56]. **Ontologies and causal reasoning:** Probabilistic ontologies and causal models enforce admissible output spaces[38][57][58]. **Output space mapping:** Multi-level and adaptive nonlinear projections constrain output spaces[59][60][61] [62]. **Set-theoretic frameworks:** Map input to output spaces with certainty measures[63]. **Synthesis:** Admissible output spaces are formally characterized and enforced using probabilistic models, automata, ontologies, and causal reasoning frameworks[2][15][38][41][55][56][57][58][64][65].

## 4.1.2 Containment Hierarchies and Safety Dominance

**Epistemic uncertainty metrics:** Frameworks integrate epistemic states and uncertainty metrics (e.g., M- Vector, Δ–η–ζ model)[36]. **Safety envelopes:** Intersections of predictability and confidence regions in state space[66]. **Probabilistic safety margins:** Combine deterministic and probabilistic models of system load and capacity [6][67][68][69]. **Bayesian approaches:** Bound probability of safety violations under uncertainty[44]. **Pluralistic safety architectures:** Multi-agent debate frameworks enforce safety dominance[70]. **Synthesis:** Containment hierarchies and safety dominance properties are formally specified and verified using epistemic uncertainty metrics, safety envelopes, and multi-agent frameworks[6][21][22][36][44][66][70][71].

## 4.1.3 Formal Specification and Verification Techniques

**Temporal logic:** LTL, PPTL, and dialects for safety property specification[8][72][73][74][75][76]. **Model checking tools:** SPIN, NuSMV, CadenceSMV, Maude for verification[50][77][78][79][80]. **Process algebras:** Model system behavior for verification[50][80][81]. **Specification patterns:** New dialects (e.g., ST-LTL) for domain-specific safety constraints[74][82]. **Advanced model checking:** On-the-fly unfolding, deterministic compilation for efficiency[83][84]. **Synthesis:** Formal specification and verification techniques are widely applied to ensure containment and safety properties in AI DSS, supporting rigorous architectural design[8][50][72][73][74][75][76][79][80].

**4.2 Formal Methods and Safety Assurance in AI Architectural Design**

## 4.2.1 Formal Methods for Specification and Verification

**Mathematically rigorous techniques:** Specification, development, and verification of AI systems[85][86][87]. **Hybrid approaches:** Combine formal methods with machine learning for expressing and verifying safety properties[88][89]. **Verification tools:** VerifAI, AVATAR for modeling, simulation, and runtime monitoring[42][90][91]. **Safety assurance:** Layered designs with extrinsic safeguarding mechanisms[11]. **Unified frameworks:** Characterize safety, robustness, hyper-safety, and explainability[92]. **Challenges:** Scalability, integration with training, continuous verification[93]. **Synthesis:** Formal methods contribute to error elimination, safety assurance, and verification of architectural layers in AI DSS, supporting certifiable safety dominance and output containment[11][42][85][86][87][88][89][90] [91][92][93][94][95].

## 4.2.2 Runtime Assurance Architectures

**ASSURE framework:** Formal verification for safety-critical aerospace systems[96]. **VerifAI toolkit:** Formal modeling, falsification, runtime monitor generation[42]. **SAFEXPLAIN project:** End-to-end design and validation for safety-critical AI systems[97][98]. **RADICS:** Extends Simplex architecture for ML-controlled cyber-physical systems[12]. **Extrinsic safeguarding:** Layered, independent runtime assurance with fallback paths[11]. **Synthesis:** Runtime assurance architectures enforce safety dominance and output containment, providing provable guarantees for AI DSS[11][12][42][96][97][98][99].

## 4.2.3 Runtime Verification of Layered AI Architectures

**Abstraction and compositional verification:** Handle probabilistic and nondeterministic behaviors[99][100]. **Runtime monitoring:** Anticipate violations, with LLMs assisting in specification capture[42][101]. **Extrinsic safeguarding:** Continuous verification against safety constraints[11]. **Probabilistic ontologies:** Support reasoning about uncertain knowledge[57]. **Symbiotic integration:** LLMs and formal methods enhance runtime verification[102]. **Synthesis:** Formal methods frameworks support runtime verification of layered AI architectures, combining probabilistic and deterministic components for scalable and sound safety assurance[11][42][99][100][101][102][103]. **4.2.4 Formal Specification Languages and Model Checking Tools** **OCL and temporal extensions:** Express behavioral properties for model checking[104]. **Probabilistic model checking (PMC):** Analyze systems with non-deterministic components[105][106]. **Estelle and LOTOS:** Structure hierarchical specifications[107]. **Cadp:** Model and verify GALS systems[108][109]. **Limit-deterministic Büchi automata:** Compact translation for LTL formulas[9]. **Synthesis:** Formal specification languages and model checking tools are best suited for verifying safety envelopes and containment hierarchies in AI DSS, supporting rigorous architectural verification[9][104][105][106] [107][108][109].

## 5. Real-world Implications

**Safety-critical domains:** Formal architectural layering and deterministic governance are essential in healthcare, autonomous vehicles, and industrial control systems, ensuring operational reliability and compliance[97][110][111].

**Auditability and accountability:** Governance-oriented architectures support regulatory compliance and traceability, critical for responsible AI deployment[13][112][113].

**Maintainability and scalability:** Modular, multi-layered architectures facilitate system maintenance, extensibility, and adaptation to evolving requirements[26][27][29].

**Runtime assurance:** Provable safety guarantees via runtime assurance architectures enable trustworthy integration of AI in real-world systems[4][10][12].

## 6. Future Research Directions

## 6.1 Research Gaps and Challenges

**Scalability of formal verification:** Current methods struggle with complex AI models; hybrid approaches and continuous verification are needed[93].

**Integration with AI training:** Formal verification must be tightly coupled with AI model training for effective safety assurance[114][115][116].

**Epistemic uncertainty frameworks:** Explicit formal models linking epistemic uncertainty quantification to deterministic governance layers are underdeveloped[114].

## 6.2 Emerging Trends and Opportunities

**Symbiotic integration:** Combining LLMs and formal methods for adaptive specification and runtime verification[102].

**Blockchain-based governance:** Decentralized consensus mechanisms and smart contracts for deterministic governance[115].

**Pluralistic safety architectures:** Multi-agent debate frameworks for robust safety dominance under uncertainty[70]. **Synthesis:** The literature reveals broad consensus on multi-layered, hierarchical architectures integrating probabilistic AI with deterministic governance. Formal specification languages and runtime assurance frameworks are central to safety and reliability. Future research should focus on unified formal models coupling epistemic uncertainty with deterministic governance, hybrid verification methodologies, and symbiotic integration of LLMs and formal methods.

## End of Report

## References

1. Proposition of a three layers architecture for adaptable artificial intelligence Benoît, V., Alexandre, D., Nakashima, T. 2014 Joint 7th International Conference on Soft Computing and Intelligent Systems, SCIS 2014 and 15th International Symposium on Advanced Intelligent Systems, ISIS 2014, 2014 https://www.scopus.com/pages/publications/84946530965?origin=scopusAI

2. PECOS: Prediction for Enormous and Correlated Output Spaces Yu, H.-F., Zhong, K., Zhang, J., (...), Dhillon, I.S. Journal of Machine Learning Research, 2022 https://www.scopus.com/pages/publications/85128313329?origin=scopusAI

3. Intelligent control architecture Insaurralde, C.C. Studies in Systems, Decision and Control, 2015 https://www.scopus.com/pages/publications/85028950034?origin=scopusAI

4. Runtime safety assurance methods for cyber physical systems based on simplex architecture Wang, Q., Chen, Q., Cao, W., He, W. Shenzhen Daxue Xuebao (Ligong Ban)/Journal of Shenzhen University Science and Engineering, 2024 https://www.scopus.com/pages/publications/85194961789?origin=scopusAI

5. Toward Constitutional Autonomy in AI Systems: A Theoretical Framework for Aligned Agentic Intelligence Torgbi Agbemabiese, W. IEEE Access, 2026 https://www.scopus.com/pages/publications/105027519739?origin=scopusAI

6. Modeling uncertainties in safety-critical real-time systems: A probabilistic component-based analysis Khan, D.A., Santinelli, L., Cucu-Grosjean, L. 7th IEEE International Symposium on Industrial Embedded Systems, SIES 2012 - Conference Proceedings, 2012 https://www.scopus.com/pages/publications/84871596999?origin=scopusAI

7. A formal specification in B of a medical decision support system Poerschke, C., Lightfoot, D.E., Nealon, J.L. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2003 https://www.scopus.com/pages/publications/35248847901?origin=scopusAI

8. Automatic Generation of Specification from Natural Language Based on Temporal Logic Wang, X., Li, G., Li, C., (...), Shu, X. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2021 https://www.scopus.com/pages/publications/85111149251?origin=scopusAI

9. Limit-deterministic büchi automata for linear temporal logic Sickert, S., Esparza, J., Jaax, S., Křetínský, J. Lecture Notes in Computer Science, 2016 https://www.scopus.com/pages/publications/84978886870?origin=scopusAI

10. Automating Recoverability Proofs for Cyber-Physical Systems with Runtime Assurance Architectures Nigam, V., Talcott, C. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85164927589?origin=scopusAI

11. Extrinsic Safeguarding Mechanism Requirements for Trustworthy Physical AI Harris, M., Madden, D. Proceedings - 2025 IEEE 33rd International Requirements Engineering Conference Workshops, REW 2025, 2025 https://www.scopus.com/pages/publications/105020927532?origin=scopusAI

12. Runtime Assurance for Intelligent Cyber-Physical Systems Dementyeva, V., Hickert, C., Sarfaraz, N., (...), Sookoor, T. Proceedings - 13th ACM/IEEE International Conference on Cyber-Physical Systems, ICCPS 2022, 2022 https://www.scopus.com/pages/publications/85134207376?origin=scopusAI

13. LLM-Augmented Algorithmic Management: A Governance-Oriented Architecture for Explainable Organizational Decision Systems Hinov, N., Ivanova, M. AI (Switzerland), 2026 https://www.scopus.com/pages/publications/105034451608?origin=scopusAI

14. The Emerged Artificial Intelligence Protocol for Hierarchical Information Network Wu, C., Bouvry, P. International Conference on Information Networking, 2023 https://www.scopus.com/pages/publications/85149178175?origin=scopusAI

15. An XAI Framework for Automated Allocation and Exploitation of Resources Marcia, D. CEUR Workshop Proceedings, 2022 https://www.scopus.com/pages/publications/85137476481?origin=scopusAI

16. ANSI/IEEE 1471 and systems engineering Maier, M.W., Emery, D., Hilliard, R. Systems Engineering, 2004 https://www.scopus.com/pages/publications/24744448387?origin=scopusAI

17. The roles of artificial intelligence in information systems Wiederhold, G. Journal of Intelligent Information Systems, 1992 https://www.scopus.com/pages/publications/0011711627?origin=scopusAI

18. An exploration of a two-layered artificial intelligence: integrating neural codification with normative reasoning Bajaj, A. Discover Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105028267008?origin=scopusAI

19. A Roadmap Toward Neurosymbolic Approaches in AI Design Arachchige, P.J., Iancu, B., Lilius, J. IEEE Access, 2025 https://www.scopus.com/pages/publications/105018075222?origin=scopusAI

20. On a common structure of intelligence in biological and technical systems Rapoport, G.N., Hertz, A.G. Bioinformatics, 1992 https://www.scopus.com/pages/publications/0026605533?origin=scopusAI

21. Retrieval activities in a database consisting of heterogeneous collections of structured text Burkowski, Forbes J. SIGIR Forum (ACM Special Interest Group on Information Retrieval), 1992 https://www.scopus.com/pages/publications/0027020320?origin=scopusAI

22. Unified Modelling of Intelligent Robotic Systems: Applications of COH/GISMOL in Automation Engineering Wang, H. Proceedings - 2025 10th International Conference on Robotics and Automation Engineering, ICRAE 2025, 2025 https://www.scopus.com/pages/publications/105034395244?origin=scopusAI

23. Finding the Path Toward Design of Synergistic Human-Centric Complex Systems Fouad, H.Y., Raz, A.K., Llinas, J., (...), Mittu, R. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2021 https://www.scopus.com/pages/publications/85120713694?origin=scopusAI

24. Hierarchies of Understanding: Preparing for A.I. Carpenter, S.A., Liu, C., Cao, W., Yao, A. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2018 https://www.scopus.com/pages/publications/85050562883?origin=scopusAI

25. The roles of artificial intelligence in information systems Wiederhold, G. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 1991 https://www.scopus.com/pages/publications/0348065980?origin=scopusAI

26. Research on Business Decision Support System Based on Big Data and Artificial Intelligence Zhang, Y., Chen, N., Zhang, Y., Wu, W. 2025 International Conference on Data Science and Its Applications, ICoDSA 2025, 2025 https://www.scopus.com/pages/publications/105018110989?origin=scopusAI

27. Bridging challenges of clinical decision support systems with a semantic approach. A case study on breast cancer Sanchez, E., Toro, C., Artetxe, A., (...), Guijarro, F. Pattern Recognition Letters, 2013 https://www.scopus.com/pages/publications/84885677354?origin=scopusAI

28. A layered architecture for the exploration of heterogeneous information using coordinated views Cruz, I.F., Huang, Y.F. Proceedings - 2004 IEEE Symposium on Visual Languages and Human Centric Computing, 2004 https://www.scopus.com/pages/publications/16244384530?origin=scopusAI

29. An agent-based distributed collaborative decision support system Nachet, B., Adla, A. Intelligent Decision Technologies, 2014 https://www.scopus.com/pages/publications/84899033838?origin=scopusAI

30. Digital twin-based intelligent risk assessment and decision support system for university student entrepreneurial projects Qin, R., Zi, X., Ge, X. Scientific Reports, 2026 https://www.scopus.com/pages/publications/105029755534?origin=scopusAI

31. Digital Twins in Surgery as a Real-Time Decision Support System: A Multi-Layered Framework Ouarour, A., Hadid, M., Padmanabhan, R., (...), Al-Ansari, A. 2025 IEEE International Conference on Technology Management, Operations and Decisions, ICTMOD 2025, 2025 https://www.scopus.com/pages/publications/105034467471?origin=scopusAI

32. Multi-layered architecture of decision support system for monitoring of dangerous good transportation Dzemydiene, D., Dzindzalieta, R. CEUR Workshop Proceedings, 2012 https://www.scopus.com/pages/publications/84893299127?origin=scopusAI

33. Board-level governance and risk oversight framework for Artificial Intelligence systems Kumar, K., Jaya, J. EDPACS, 2026 https://www.scopus.com/pages/publications/105033549713?origin=scopusAI

34. Integrated use of defense-in-depth and probabilistic safety assessment for risk acceptance la Rovere, S., Fiorini, G.L., Vestrucci, P., Tenaglia, G. 30th European Safety and Reliability Conference, ESREL 2020 and 15th Probabilistic Safety Assessment and Management Conference, PSAM 2020, 2020 https://www.scopus.com/pages/publications/85110355542?origin=scopusAI

35. Integrated use of defense-in-depth and probabilistic safety assessment for risk acceptance La Rovere, S., Fiorini, G.L., Vestrucci, P., Tenaglia, G. Proceedings of the 30th European Safety and Reliability Conference and the 15th Probabilistic Safety Assessment and Management Conference, 2020 https://www.scopus.com/pages/publications/85107290200?origin=scopusAI

36. Epistemic Gain in M-Space: A Metric for AI Governance in Complex Systems Immediato, G. International Journal of Semantic Computing, 2026 https://www.scopus.com/pages/publications/105032463155?origin=scopusAI

37. Shadow Management: Leveraging Responsible Agentic AI to Revolutionize Safe Decision-Making in Complex Organizations Ghaemi, M.S. Lecture Notes in Networks and Systems, 2026 https://www.scopus.com/pages/publications/105021834192?origin=scopusAI

38. Causally Explainable Decision Recommendations Using Causal Artificial Intelligence Cox, L.A. International Series in Operations Research and Management Science, 2023 https://www.scopus.com/pages/publications/85164721903?origin=scopusAI

39. Enable Flexibilisation in FAIRWork’s Democratic AI-based Decision Support System by Applying Conceptual Models Using ADOxx Woitsch, R., Muck, C., Utz, W., Zeiner, H. Complex Systems Informatics and Modeling Quarterly, 2024 https://www.scopus.com/pages/publications/85192906319?origin=scopusAI

40. Towards a democratic AI-based decision support system to improve decision making in complex ecosystems Woitsch, R., Muck, C., Utz, W., Zeiner, H. CEUR Workshop Proceedings, 2023 https://www.scopus.com/pages/publications/85176113224?origin=scopusAI

41. Deep probabilistic circuits for efficient uncertainty handling in learning systems Ventola, F. At- Automatisierungstechnik, 2026 https://www.scopus.com/pages/publications/105032254534?origin=scopusAI

42. Formal Analysis of AI-Based Autonomy: From Modeling to Runtime Assurance Torfah, H., Junges, S., Fremont, D.J., Seshia, S.A. Lecture Notes in Computer Science, 2021 https://www.scopus.com/pages/publications/85117473078?origin=scopusAI

43. RTA-IR: A runtime assurance framework for behavior planning based on imitation learning and responsibility-sensitive safety model Peng, Y., Tan, G., Si, H. Expert Systems with Applications, 2023 https://www.scopus.com/pages/publications/85162857773?origin=scopusAI

44. Can a Bayesian Oracle Prevent Harm from an Agent? Bengio, Y., Cohen, M.K., Malkin, N., (...), Kaddar, Y. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105014742006?origin=scopusAI

45. Markov logic: An interface layer for artificial intelligence Domingos, P., Lowd, D. Synthesis Lectures on Artificial Intelligence and Machine Learning, 2009 https://www.scopus.com/pages/publications/68049142277?origin=scopusAI

46. Formal specification and decision support Krause, P.J., Byers, P.J., Hajnal, S. Decision Support Systems, 1994 https://www.scopus.com/pages/publications/0028529120?origin=scopusAI

47. Applied probabilistic AI for online diagnosis of a safety-critical system based on a quality assurance program Lauber, Johannes, Steger, Christian, Weiss, Reinhold Proceedings of the ACM Symposium on Applied Computing, 1999 https://www.scopus.com/pages/publications/0032674213?origin=scopusAI

48. Formal specification and model checking of a ride-sharing system in maude Muramoto, E., Ogata, K., Shinoda, Y. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2020 https://www.scopus.com/pages/publications/85081630154?origin=scopusAI

49. A holistic approach for access control policies: From formal specification to aspect-based enforcement Kallel, S., Charfi, A., Mezini, M., (...), Sewe, A. International Journal of Information and Computer Security, 2009 https://www.scopus.com/pages/publications/77149179360?origin=scopusAI

50. A Formal Specification and Validation of a Critical System in Presence of Byzantine Errors Gnesi, S., Latella, D., Lenzini, G., (...), Marmo, P. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2000 https://www.scopus.com/pages/publications/23044518364?origin=scopusAI

51. Formal Specification and Verification of an Autonomous Vehicle Control System by the OTS/CafeOBJ method Wang, Y., Nakamura, M., Sakakibara, K., Okura, Y. Proceedings of the International Conference on Software Engineering and Knowledge Engineering, SEKE, 2023 https://www.scopus.com/pages/publications/85170103214?origin=scopusAI

52. A TLA+ Formal Specification and Verification of a New Real-Time Communication Protocol Regnier, P., Lima, G., Andrade, A. Electronic Notes in Theoretical Computer Science, 2009 https://www.scopus.com/pages/publications/67649404680?origin=scopusAI

53. Dynamic Reliability Evaluation Approach for Electromechanical Systems Based on Probabilistic Model Checking Hou, Y., Yang, P., Xu, K., (...), Fan, J. Zhongguo Jixie Gongcheng/China Mechanical Engineering, 2019 https://www.scopus.com/pages/publications/85064601912?origin=scopusAI

54. Formal specification and validation of selective acknowledgement protocol using Z/EVES theorem prover Shukur, Z., Alias, N., Halip, M.H.M., Idrus, B. Journal of Applied Sciences, 2006 https://www.scopus.com/pages/publications/33749647733?origin=scopusAI

55. Probability distributions over structured spaces Choi, A., Van Den Broeck, G., Darwiche, A. AAAI Spring Symposium - Technical Report, 2015 https://www.scopus.com/pages/publications/84987617446?origin=scopusAI

56. Quantitative automata-based controller synthesis for non-autonomous stochastic hybrid systems Tkachev, I., Mereacre, A., Katoen, J.-P., Abate, A. HSCC 2013 - Proceedings of the 16th International Conference on Hybrid Systems: Computation and Control, Part of CPSWeek 2013, 2012 https://www.scopus.com/pages/publications/84876757058?origin=scopusAI

57. Project Presentation: Recursive Functions and Engineering Probabilistic Ontologies Chitaia, I., Omanadze, R., Rukhaia, M. Proceedings 2023 IEEE 19th International Conference on e-Science, e-Science 2023, 2023 https://www.scopus.com/pages/publications/85174225685?origin=scopusAI

58. ARTI reference architecture – PROSA revisited Valckenaers, P. Studies in Computational Intelligence, 2019 https://www.scopus.com/pages/publications/85059073014?origin=scopusAI

59. Three-level adapted output space mapping technique for two-objective optimization Gong, J., Ben-Ayed, R., Gillon, F., (...), Brochet, P. Przeglad Elektrotechniczny, 2012 https://www.scopus.com/pages/publications/84863806183?origin=scopusAI

60. Three-level output space mapping strategy for electromagnetic design optimization Ayed, R.B., Gong, J., Brisset, S., (...), Brochet, P. IEEE Transactions on Magnetics, 2012 https://www.scopus.com/pages/publications/84856404528?origin=scopusAI

61. Proposal of a bi-objective kriging adapted output space mapping technique for electromagnetic design optimization Gong, J., Zhang, H., Zhao, B., (...), Gillon, F. IEEE Transactions on Magnetics, 2019 https://www.scopus.com/pages/publications/85065917980?origin=scopusAI

62. Proposal of a kriging output space mapping technique for electromagnetic design optimization Gong, J., Gillon, F., Canh, J.T., Xu, Y. IEEE CEFC 2016 - 17th Biennial Conference on Electromagnetic Field Computation, 2016 https://www.scopus.com/pages/publications/85011954135?origin=scopusAI

63. SET-THEORETIC FRAMEWORK FOR THE PROCESSING OF UNCERTAIN KNOWLEDGE. Lu, S.Y., Stephanou, H.E. null, 1983 https://www.scopus.com/pages/publications/0021002869?origin=scopusAI

64. PECOS: Prediction for Enormous and Correlated Output Spaces Yu, H.-F., Zhang, J., Chang, W.-C., (...), Hsieh, C.-J. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2022 https://www.scopus.com/pages/publications/85137150919?origin=scopusAI

65. Multi-output regression on the output manifold Liu, G., Lin, Z., Yu, Y. Pattern Recognition, 2009 https://www.scopus.com/pages/publications/67649387956?origin=scopusAI

66. Towards Provably Correct Probabilistic Flight Systems Cruz-Camacho, E., Paul, S., Kopsaftopoulos, F., Varela, C.A. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2020 https://www.scopus.com/pages/publications/85097426521?origin=scopusAI

67. Risk Informed Safety Margins Characterization via failure domain quantification. Loss of main feed water example Rychkov, V. International Topical Meeting on Probabilistic Safety Assessment and Analysis 2013, PSA 2013, 2013 https://www.scopus.com/pages/publications/84899117307?origin=scopusAI

68. Robustness of decision insights under alternative aleatory/epistemic uncertainty classifications Unwin, S.D., Eslinger, P.W., Johnson, K.I. International Topical Meeting on Probabilistic Safety Assessment and Analysis 2013, PSA 2013, 2013 https://www.scopus.com/pages/publications/84899106927?origin=scopusAI

69. Risk-informed safety margin characterization methods Smith, C.L., Youngblood, R. 11th International Probabilistic Safety Assessment and Management Conference and the Annual European Safety and Reliability Conference 2012, PSAM11 ESREL 2012, 2012 https://www.scopus.com/pages/publications/84873194090?origin=scopusAI

70. Building Robust Artificial Intelligence Through Multi-Agent Debate Bauschard, S. AI Pluralism: Fostering Diversity and Dialogue in Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105032894204?origin=scopusAI

71. LUCID: Learning-Enabled Uncertainty-Aware Certification of Stochastic Dynamical Systems Casablanca, E., Schön, O., Zuliani, P., Soudjani, S. Proceedings of the AAAI Conference on Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105034734140?origin=scopusAI

72. Linear Temporal Logic Symbolic Model Checking Rozier, K.Y. Computer Science Review, 2011 https://www.scopus.com/pages/publications/79955035042?origin=scopusAI

73. Formal verification of safety properties for a cache coherence protocol Ramirez, S., Rocha, C. 2015 10th Colombian Computing Conference, 10CCC 2015, 2015 https://www.scopus.com/pages/publications/84963799316?origin=scopusAI

74. A formal specification language for PLC-based control logic Ljungkrantz, O., Akesson, K., Fabian, M., Yuan, C. IEEE International Conference on Industrial Informatics (INDIN), 2010 https://www.scopus.com/pages/publications/77956580760?origin=scopusAI

75. Formal verification of eBPF program security based on PTL Chen, Y., Shu, X. ACM International Conference Proceeding Series, 2023 https://www.scopus.com/pages/publications/85197336362?origin=scopusAI

76. Designing a Safe Intersection Management Algorithm using Formal Methods Saraoglu, M., Pintscher, J., Janschek, K. IFAC-PapersOnLine, 2022 https://www.scopus.com/pages/publications/85138480621?origin=scopusAI

77. Supporting formal verification of dima multi-agents models: Towards a framework based on maude model checking Boudiaf, N., Mokhati, F., Badri, M. International Journal of Software Engineering and Knowledge Engineering, 2008 https://www.scopus.com/pages/publications/60849111395?origin=scopusAI

78. Descartes-Agent: Verifying Formal Specifications Using the Model Checking Technique Subburaj, V.H., Urban, J.E. Proceedings - 2nd IEEE International Conference on Robotic Computing, IRC 2018, 2018 https://www.scopus.com/pages/publications/85049645115?origin=scopusAI

79. Formal specification and verification of a coordination protocol for an automated air traffic control system Zhao, Y., Rozier, K.Y. Science of Computer Programming, 2014 https://www.scopus.com/pages/publications/84908352492?origin=scopusAI

80. Formal Verification and Validation of IoT-based Railway Gate Controlling System at Level Crossing Rashid, M., Qadeer, M., Raza, H., (...), Zafar, N.A. 2024 IEEE 1st Karachi Section Humanitarian Technology Conference, Khi-HTC 2024, 2024 https://www.scopus.com/pages/publications/85190663098?origin=scopusAI

81. Formal specification and verification of properties of lactose operon regulation by using the EST toolbox Vogrin, R., Meolic, R., Kapus, T. Elektrotehniski Vestnik/Electrotechnical Review, 2017 https://www.scopus.com/pages/publications/85039455672?origin=scopusAI

82. Novel Patterns for Formal Verification of System Safety Properties Nallamalli, R., Chauhan, D.S. Journal of The Institution of Engineers (India): Series B, 2022 https://www.scopus.com/pages/publications/85136483628?origin=scopusAI

83. Deterministic compilation of temporal safety properties in explicit state model checking Rozier, K.Y., Vardi, M.Y. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2013 https://www.scopus.com/pages/publications/84880747508?origin=scopusAI

84. On-the-fly unfolding with optimal exploration for linear temporal logic model checking of concurrent software and systems Li, S., Zheng, L., Yang, R., Ding, Z. Automated Software Engineering, 2025 https://www.scopus.com/pages/publications/105007776171?origin=scopusAI

85. Formal and conventional development methods-complementary techniques for error elimination Hamilton, V. Atomic Energy of Canada Limited, AECL (Report), 1993 https://www.scopus.com/pages/publications/0027541630?origin=scopusAI

86. The industrial use of formal methods Thomas, M. Microprocessors and Microsystems, 1993 https://www.scopus.com/pages/publications/3142649409?origin=scopusAI

87. Formal verification, testing, and inspection for intelligent services Xu, M., Wang, L. EAI/Springer Innovations in Communication and Computing, 2021 https://www.scopus.com/pages/publications/85091707181?origin=scopusAI

88. Bridging formal methods and machine learning with model checking and global optimisation Bensalem, S., Huang, X., Ruan, W., (...), Zhao, X. Journal of Logical and Algebraic Methods in Programming, 2024 https://www.scopus.com/pages/publications/85182811648?origin=scopusAI

89. Bridging Formal Methods and Machine Learning with Global Optimisation Huang, X., Ruan, W., Tang, Q., Zhao, X. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2022 https://www.scopus.com/pages/publications/85141654974?origin=scopusAI

90. Formal Verification of Safety and Security Properties in Industry 4.0 Applications Hosseini, A.M., Sauter, T., Kastner, W. IEEE International Conference on Emerging Technologies and Factory Automation, ETFA,

2023 https://www.scopus.com/pages/publications/85175428921?origin=scopusAI

91. Formal Analysis of Neural Network-Based Systems in the Aircraft Domain Kouvaros, P., Kyono, T., Leofante, F., (...), Zheng, Y. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2021 https://www.scopus.com/pages/publications/85119873349?origin=scopusAI

92. A Uniform Language for Safety, Robustness and Explainability Belle, V., Barcelo, P. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105023401114?origin=scopusAI

93. Formal methods for safety-critical machine learning: a systematic literature review Newcomb, A., Ochoa, O. Frontiers in Artificial Intelligence, 2026 https://www.scopus.com/pages/publications/105031810112?origin=scopusAI

94. Development of an Effective Safety Assessment Capable of Measuring the Safety of AI-Based Systems. Nyakundi, N.B.N., Reza, H. IEEE International Conference on Electro Information Technology, 2024 https://www.scopus.com/pages/publications/85201262799?origin=scopusAI

95. Systems Engineering With Architecture Modeling, Formal Verification, and Human Interactions for Learning-Enabled Autonomous Agent Ganeriwala, P., Narayan, N., Jones, R.M., (...), Neogi, N. Systems Engineering, 2025 https://www.scopus.com/pages/publications/105002154781?origin=scopusAI

96. Formal Verification of Safety-Critical Aerospace Systems Paul, S., Cruz, E., Dutta, A., (...), Varela, C. IEEE Aerospace and Electronic Systems Magazine, 2023 https://www.scopus.com/pages/publications/85147265739?origin=scopusAI

97. SAFEXPLAIN: a Complete Approach Towards Trustworthy AI-Based Safety-Critical Systems Abella, J., Agirre, I., Bui, T., (...), Dallara, V. Proceedings - 2025 28th Euromicro Conference on Digital System Design, DSD 2025, 2025 https://www.scopus.com/pages/publications/105030537985?origin=scopusAI

98. SAFEXPLAIN: Safe and Explainable Critical Embedded Systems Based on AI Abella, J., Perez, J., Englund, C., (...), Cunial, D. Proceedings -Design, Automation and Test in Europe, DATE, 2023 https://www.scopus.com/pages/publications/85162662708?origin=scopusAI

99. Harmonizing Parameterized Verification and Invariant Synthesis for Safety Envelopes in Black-Box Autonomy Lu, Y., Xiong, Z., Huang, H., (...), Kuang, J. Concurrency and Computation: Practice and Experience, 2025 https://www.scopus.com/pages/publications/105020449484?origin=scopusAI

100. An Enhanced Interface-Based Probabilistic Compositional Verification Approach Ouchani, S., Ait Mohamed, O., Debbabi, M. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2024 https://www.scopus.com/pages/publications/85180770313?origin=scopusAI

101. Watchdogs and Oracles: Runtime Verification Meets Large Language Models for Autonomous Systems Ferrando, A. Electronic Proceedings in Theoretical Computer Science, EPTCS, 2025 https://www.scopus.com/pages/publications/105023156059?origin=scopusAI

102. Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods Zhang, Y., Cai, Y., Zuo, X., (...), Dong, J.S. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105023637086?origin=scopusAI

103. Leveraging AI-Driven Methods for Optimized Formal Verification of Generated Properties in SoC Components Eljadiri, L., Assayad, I., Nahhal, T. 2025 International Conference on Circuit, Systems and Communication, ICCSC 2025, 2025 https://www.scopus.com/pages/publications/105016883796?origin=scopusAI

104. Leveraging formal verification tools for DSML users: A process modeling case study Zalila, F., Crégut, X., Pantel, M. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and

Lecture Notes in Bioinformatics), 2012 https://www.scopus.com/pages/publications/84868277184?origin=scopusAI

105. Dependability analysis of networked automation systems by probabilistic delay time analysis Greifeneder, J., Frey, G. IFAC Proceedings Volumes (IFAC-PapersOnline), 2006 https://www.scopus.com/pages/publications/79961189160?origin=scopusAI

106. Dependability Analysis of Networked Automation Systems by Probabilistic Delay Time Analysis Greifeneder, J., Frey, G. Information Control Problems in Manufacturing 2006, 2006 https://www.scopus.com/pages/publications/84884093790?origin=scopusAI

107. Formal specification in OSI Vissers, C.A., Scollo, G. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 1987 https://www.scopus.com/pages/publications/84915385167?origin=scopusAI

108. Vérification de systèmes gals en combinant langages synchrones et algèbres de processus Thivolle, D. UPB Scientific Bulletin, Series C: Electrical Engineering, 2011 https://www.scopus.com/pages/publications/80052182448?origin=scopusAI

109. Verification of Gals systems by combining synchronous languages and process calculi Garavel, H., Thivolle, D. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2009 https://www.scopus.com/pages/publications/70350637206?origin=scopusAI

110. Architecting safety-critical decision-support systems for nuclear emergency management Ionescu, T.B., Scheuermann, W. IT - Information Technology, 2016 https://www.scopus.com/pages/publications/85041748457?origin=scopusAI

111. Architectural Patterns for Integrating AI Technology into Safety-Critical Systems MacHer, G., Seidl, M., Dzambic, M., Dobaj, J. ACM International Conference Proceeding Series, 2021 https://www.scopus.com/pages/publications/85123803765?origin=scopusAI

112. Responsible Artificial Intelligence Systems: From Trustworthiness to Governance Herrera, F. Proceedings - Design, Automation and Test in Europe, DATE, 2024 https://www.scopus.com/pages/publications/85210066367?origin=scopusAI

113. IntelliLung AI-DSS Trustworthiness Evaluation Framework Janev, V., Nenadovic, M., Paunovic, D., (...), Huhle, R. 2024 32nd Telecommunications Forum, TELFOR 2024 - Proceedings of Papers, 2024 https://www.scopus.com/pages/publications/85216887228?origin=scopusAI

114. The Epistemic Role of AI Decision Support Systems: Neither Superiors, Nor Inferiors, Nor Peers Hirmiz, R. Philosophy and Technology, 2024 https://www.scopus.com/pages/publications/85208608250?origin=scopusAI

115. Integrating Blockchain Technology with Artificial Intelligence to Create Scalable, Reliable, and Open Decision Support Systems Khan, S.A., Balusamy, S., Saviour, M.P.A., (...), Sofia, D.S. 2025 Global Conference in Emerging Technology, GINOTECH 2025, 2025 https://www.scopus.com/pages/publications/105013619394?origin=scopusAI

116. Ontology-Based Explanations of Neural Networks for Collaborative Human-AI Decision Support Systems Smirnov, A., Ponomarev, A. Lecture Notes in Networks and Systems, 2023 https://www.scopus.com/pages/publications/85174506375?origin=scopusAI
