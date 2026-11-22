---
source_pdf: "Search 1 - Research on AI action restrictions under changing conditions.pdf"
source_sha256: "25348bc9cd78e29a817c70d727e9abe95aaedbb598abc5b172d7d97eda4e693c"
source_pages: 19
scopus_ai_generated: "Wed Sep 23 2026"
query: "Research on AI action restrictions under changing conditions"
report_title: "Runtime Restriction and Governance Mechanisms for AI Decision-Support Systems: Empirical Evidence and Conceptual Frameworks"
converted_tables: 2
converter: "scopus2md.py (pdfplumber)"
---
# Research on AI action restrictions under changing conditions

## Quick Reference

## Key Findings Table

| Mechanism/Framework | Empirical Evidence | Conceptual Framework | Dynamic Adaptation | Human Oversight | Multi- Agent Support | Notable Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| Mandatory Results Automata (MRA) | Yes | Yes | Partial | No | Partial | Enforceability limits, deterministic focus |
| Controlled Agentic AI Systems (CAIS) | Yes | Yes | Yes | Yes | Yes | Complexity, integration overhead |
| Constitutional Autonomy | Partial | Yes | Yes | Yes | Yes | Early-stage empirical validation |
| Legitimacy Layer | Prototype | Yes | Yes | Yes | Yes | Adoption, interoperability |
| Safety Filters & Shielding | Yes | Yes | Yes | Partial | Yes | Adversarial bypass, language gaps |
| Runtime Assurance (RTA) | Yes | Yes | Yes | Yes | Yes | Certification, recovery rates |
| Centralized Runtime Control Layers | Yes | Yes | Yes | Yes | Yes | Verifier tax, scalability |
| Dynamic Consent Mechanisms | Yes | Yes | Yes | Yes | Yes | Conflict resolution, timing |
| Integrated Safety Architectures | Yes | Yes | Yes | Partial | Yes | Scalability, context sensitivity |

## Direct Answer

Research on runtime restrictions for AI actions under varying risk or environmental conditions has been explored through both empirical studies and conceptual frameworks. Key contributions include formal models such as Mandatory Results Automata, Controlled Agentic AI Systems, and Constitutional Autonomy for embedding deterministic governance, empirical validations of dynamic safety filters, and runtime assurance mechanisms like TiPEX, GREP, and RTAEval. Additionally, middleware architectures such as the Legitimacy Layer have been proposed to dynamically adjust admissible action sets based on real-time governance signals, while challenges like multi-agent coordination limits and the legitimacy gap highlight areas for further research [1][2][3][4][5][6].

## Study Scope

**Time Period:** 2000–2024, with emphasis on post-2018 advances in LLMs, agentic AI, and runtime assurance.

**Disciplines:** Computer science (AI, multi-agent systems, formal methods), safety engineering, regulatory science, human-computer interaction, and organizational governance.

**Methods:** Formal modeling, empirical validation (simulation, real-world deployment, case studies), prototype implementation, meta-analysis, and cross-domain comparative studies.

## Assumptions & Limitations

**Assumptions:** The surveyed literature assumes the feasibility of embedding runtime restriction mechanisms in AI pipelines and the necessity of human oversight for legitimacy.

**Limitations:** Empirical validation is often limited to simulation or prototype scale; multi-agent and non-deterministic settings expose fundamental enforcement limits; interoperability and HITL effectiveness remain underexplored[5][7].

## Suggested Further Research

Operationalizing continuous human oversight during runtime, especially in multi-agent and high-autonomy settings. Enhancing interoperability and standardization of runtime governance middleware. Developing AI-specific, dynamic, and explainable risk assessment frameworks. Addressing the legitimacy gap and HITL effectiveness through role-specific, context-aware governance models. Bridging technical and regulatory advances for AGI and critical infrastructure applications[8][9][10].

## 1. Introduction

## Scope and Motivation

As AI and automated decision-support systems are increasingly deployed in high-stakes and dynamic environments, the need for robust runtime restriction mechanisms has become paramount. These mechanisms— ranging from admissible action sets and advisory restrictions to runtime governance, safety filters, shielding, and runtime assurance—are essential for ensuring that AI systems act within safe, legitimate, and context-appropriate boundaries, especially as risk profiles and environmental conditions evolve in real time[5][11]. Dynamic adaptation and empirical validation of these mechanisms are critical to address the limitations of static, pre-deployment controls and to operationalize human oversight, contestability, and escalation during the brief but consequential intervals of AI decision execution.

**2. Formal Models and Conceptual Frameworks for Runtime Restriction**

## 2.1 Mandatory Results Automata and Extensions

Mandatory Results Automata (MRAs) provide a foundational formal model for runtime enforcement, capable of monitoring and transforming security-relevant actions and their results. MRAs offer simple operational semantics and expressive policy definitions, supporting both deterministic and non-deterministic policies[1]. Extensions to MRAs address: **Non-deterministic policies:** Handling stochastic and multi-agent behaviors, with enforceability characterized by the monitor's control over actions (suppress, insert, observe)[11].

**Multi-agent coordination:** Formalizing limits of local enforcement and the emergence of governance blind spots (e.g., the "routing gap")[7].

**Timed properties:** Incorporating timing constraints and uncontrollable events, with tools like TiPEX and GREP supporting enforcement[4]. **Synthesis:** MRAs and their extensions provide a rigorous basis for runtime restriction but face enforceability limits in non-deterministic and multi-agent settings, motivating the need for layered and adaptive governance architectures.

**2.2 Controlled Agentic AI Systems (CAIS) and Deterministic Governance** The CAIS framework embeds governance as a deterministic operator within AI decision pipelines, ensuring constraint-aware, auditable, and reproducible decision-making. Empirical studies demonstrate that CAIS outperforms approval-only strategies in federated and multi-agent environments by reducing constraint violations and stabilizing system dynamics without degrading performance[12]. Key features include:

**Constraint projection:** Transforming proposed actions into compliant executed actions.

**Audit trace semantics:** Enabling replayability and regulatory compliance.

**Stabilizing transformation:** Reducing action-level variance and intervention costs. **Synthesis:** CAIS operationalizes deterministic governance, offering formal guarantees and empirical effectiveness, but introduces complexity and integration overhead in large-scale deployments.

## 2.3 Constitutional Autonomy and Normative Reasoning

Constitutional Autonomy frameworks extend runtime enforcement beyond training-phase alignment by embedding normative reasoning and constitutional attention mechanisms directly into AI architectures. This enables: **Continuous runtime enforcement:** Reducing harmful behaviors and enhancing adversarial robustness[2]. **Normative prior engineering:** Integrating ethical and legal norms as first-class architectural elements. **Principled conflict resolution:** Supporting interpretable and contestable decision-making. **Synthesis:** These frameworks bridge technical and normative domains, but empirical validation is at an early stage, and integration with legacy systems remains a challenge.

**2.4 Probabilistic Requirement Modeling and Outcome-Centric Governance** Probabilistic Requirement Modeling (PRM) offers an outcome-centric formalism for non-deterministic AI systems, redefining requirements in terms of use cases, user intent, and measurable outcomes. PRM supports: **Adaptive workflow orchestration:** Aligning with regulatory frameworks (e.g., EU AI Act)[13]. **Continuous validation:** Facilitating ongoing compliance and risk management. **Synthesis:** PRM addresses the probabilistic and adaptive nature of modern AI, but practical adoption depends on integration with runtime monitoring and assurance tools.

## 2.5 Legitimacy Layer and Model-Agnostic Middleware

The Legitimacy Layer is a model-agnostic middleware architecture that evaluates governance signals— uncertainty, impact, reversibility, and contestation—in real time. It routes AI decisions through a legitimacy controller, enforcing structural human oversight, contestation, and escalation during runtime[5][6]. Features include: **Four-state autonomy model:** Normal, Reduced, Human Oversight Required, Safe Halt. **Execution directives:** Execute, execute_async, escalate, halt. **Structural enforcement:** Embedding human inclusion as an architectural property. **Synthesis:** The Legitimacy Layer closes the legitimacy gap in runtime execution, but widespread adoption and interoperability with diverse AI systems are ongoing challenges.

**3. Empirical Studies of Safety Filters, Shielding, and Runtime Assurance**

## 3.1 Safety Filters and Shielding in LLM Agents

Empirical studies on safety filters and shielding in multi-step LLM agents reveal: **Multi-stage output filtering:** Reduces harmful outputs but faces diminishing returns and adversarial bypass (e.g., coordinated jailbreaks)[3][14].

**Language and context sensitivity:** Effectiveness varies across languages and harm categories, with higher vulnerabilities in non-English contexts[15].

**Advanced moderation frameworks:** Tools like Legilimens and SafeIntervention dynamically adjust internal representations to defend against jailbreaks while preserving utility[16][17].

**Function call vulnerabilities:** Over 90% success rate for jailbreaks via function calls, highlighting the need for specialized safety filters[18]. **Synthesis:** While safety filters and shielding are effective in reducing certain risks, they are not foolproof and require continuous adaptation to adversarial tactics and context-specific vulnerabilities.

## 3.2 Runtime Assurance Frameworks and Hybrid Controllers

Runtime Assurance (RTA) frameworks employ hybrid controllers that monitor system state and switch to simpler safety controllers to avoid hazards. Empirical validation includes: **Aerospace and vehicle safety:** RTA frameworks ensure hard safety constraints while allowing performance optimization[19][20].

**Certification challenges:** Alignment with standards (e.g., DO-178C) and traceability are critical for operational safety[21].

**Distributed frameworks:** M-DRTA and Black-Box Simplex architectures support multi-agent and complex controller scenarios[22][23].

**Recovery mechanisms:** Extending safety shields with recovery logic improves resilience in multi-agent systems[24]. **Synthesis:** RTA frameworks provide robust runtime assurance but face challenges in certification, recovery rates, and integration with learning-based controllers.

## 3.3 Integrated Safety Architectures and Empirical Validation

Integrated safety architectures validated in uncertain environments include: **Learning-based safety filters:** Robust optimization and online adaptation ensure high-probability safety in unknown or noisy systems[25][26]. **Control barrier functions (CBFs):** Applied as add-ons to LLMs and control systems for real-time intervention[27][28]. **Adaptive shielding:** Hamilton-Jacobi reachability and conformal prediction methods reduce safety violations during reinforcement learning[29][30]. **Domain-specific validation:** Medical, energy, and robotics applications demonstrate improved safety and performance[31][32].

**Synthesis:** Empirical validation confirms the effectiveness of integrated safety architectures, but scalability and context sensitivity remain open issues.

**4. Dynamic Adaptation to Changing Risk and Environmental Conditions** **4.1 Legitimacy Layer: Real-Time Adaptation and Governance Signals** The Legitimacy Layer dynamically adjusts AI action sets based on real-time governance signals: **Signal evaluation:** Uncertainty, impact, reversibility, and contestation are continuously assessed[5]. **Execution routing:** Decisions are routed to appropriate autonomy states and directives (e.g., escalate for high-impact, high-uncertainty actions). **Structural oversight:** Human inclusion, contestability, and escalation are enforced as architectural properties. **Synthesis:** This approach enables nuanced, context-sensitive adaptation of AI autonomy, balancing operational efficiency with safety and legitimacy.

## 4.2 Runtime Certification and Dynamic Safety Management

Best practices for runtime certification and dynamic safety management include: **Continuous monitoring:** Dynamic risk management and runtime certification are essential for dependable autonomous systems[33]. **Formal verification:** Hybrid programs and theorem provers support design-time verification of safety properties[34]. **Distributed assurance:** Frameworks like M-DRTA balance safety and efficiency in multi-vehicle systems [22]. **Automated recovery:** Symbolic rewriting and SMT solvers enable formal verification of safety recovery[35]. **Synthesis:** Dynamic certification frameworks are critical for evolving AI systems but require structured research and cross-domain collaboration.

**4.3 Predictive Risk Modeling and Continuous Runtime Assessment** AI governance frameworks increasingly incorporate predictive risk modeling: **Machine learning integration:** Supervised and reinforcement learning forecast risk trajectories and adapt decisions[36][37]. **Dynamic risk scoring:** Algorithms continuously adjust to regulatory changes and security events[37]. **Lifecycle-based control:** Standards like ISO/IEC 42001:2023 and NIST AI RMF support continuous improvement and risk-driven governance[38].

**Synthesis:** Predictive risk modeling enhances real-time risk assessment and mitigation but depends on robust data integration and explainability. **4# Runtime Restriction and Governance Mechanisms for AI Decision-Support Systems: Empirical Evidence**

## and Conceptual Frameworks

## Quick Reference

## Key Findings Table

| Mechanism/Framework | Empirical Evidence | Conceptual Framework | Dynamic Adaptation | Human Oversight | Multi- Agent Support | Notable Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| Mandatory Results Automata (MRA) | Yes | Yes | Partial | No | Partial | Enforceability limits, deterministic focus |
| Controlled Agentic AI Systems (CAIS) | Yes | Yes | Yes | Yes | Yes | Complexity, integration overhead |
| Constitutional Autonomy | Partial | Yes | Yes | Yes | Yes | Early-stage empirical validation |
| Legitimacy Layer | Prototype | Yes | Yes | Yes | Yes | Adoption, interoperability |
| Safety Filters & Shielding | Yes | Yes | Yes | Partial | Yes | Adversarial bypass, language gaps |
| Runtime Assurance (RTA) | Yes | Yes | Yes | Yes | Yes | Certification, recovery rates |
| Centralized Runtime Control Layers | Yes | Yes | Yes | Yes | Yes | Verifier tax, scalability |
| Dynamic Consent Mechanisms | Yes | Yes | Yes | Yes | Yes | Conflict resolution, timing |
| Integrated Safety Architectures | Yes | Yes | Yes | Partial | Yes | Scalability, context sensitivity |

## Direct Answer

Research on runtime restrictions for AI actions under varying risk or environmental conditions has been explored through both empirical studies and conceptual frameworks. Key contributions include formal models such as Mandatory Results Automata, Controlled Agentic AI Systems, and Constitutional Autonomy for embedding deterministic governance, empirical validations of dynamic safety filters, and runtime assurance mechanisms like TiPEX, GREP, and RTAEval. Additionally, middleware architectures such as the Legitimacy Layer have been proposed to dynamically adjust admissible action sets based on real-time governance signals, while challenges like multi-agent coordination limits and the legitimacy gap highlight areas for further research [1][2][3][4][5][6].

## Study Scope

**Time Period:** 2000–2024, with emphasis on post-2018 advances in LLMs, agentic AI, and runtime assurance.

**Disciplines:** Computer science (AI, multi-agent systems, formal methods), safety engineering, regulatory science, human-computer interaction, and organizational governance.

**Methods:** Formal modeling, empirical validation (simulation, real-world deployment, case studies), prototype implementation, meta-analysis, and cross-domain comparative studies.

## Assumptions & Limitations

**Assumptions:** The surveyed literature assumes the feasibility of embedding runtime restriction mechanisms in AI pipelines and the necessity of human oversight for legitimacy.

**Limitations:** Empirical validation is often limited to simulation or prototype scale; multi-agent and non-deterministic settings expose fundamental enforcement limits; interoperability and HITL effectiveness remain underexplored[5][7].

## Suggested Further Research

Operationalizing continuous human oversight during runtime, especially in multi-agent and high-autonomy settings. Enhancing interoperability and standardization of runtime governance middleware. Developing AI-specific, dynamic, and explainable risk assessment frameworks. Addressing the legitimacy gap and HITL effectiveness through role-specific, context-aware governance models. Bridging technical and regulatory advances for AGI and critical infrastructure applications[8][9][10].

## 1. Introduction

## Scope and Motivation

As AI and automated decision-support systems are increasingly deployed in high-stakes and dynamic environments, the need for robust runtime restriction mechanisms has become paramount. These mechanisms— ranging from admissible action sets and advisory restrictions to runtime governance, safety filters, shielding, and runtime assurance—are essential for ensuring that AI systems act within safe, legitimate, and context-appropriate boundaries, especially as risk profiles and environmental conditions evolve in real time[5][11]. Dynamic adaptation and empirical validation of these mechanisms are critical to address the limitations of static, pre-deployment controls and to operationalize human oversight, contestability, and escalation during the brief but consequential intervals of AI decision execution.

**2. Formal Models and Conceptual Frameworks for Runtime Restriction**

## 2.1 Mandatory Results Automata and Extensions

Mandatory Results Automata (MRAs) provide a foundational formal model for runtime enforcement, capable of monitoring and transforming security-relevant actions and their results. MRAs offer simple operational semantics and expressive policy definitions, supporting both deterministic and non-deterministic policies[1]. Extensions to MRAs address: **Non-deterministic policies:** Handling stochastic and multi-agent behaviors, with enforceability characterized by the monitor's control over actions (suppress, insert, observe)[11].

**Multi-agent coordination:** Formalizing limits of local enforcement and the emergence of governance blind spots (e.g., the "routing gap")[7].

**Timed properties:** Incorporating timing constraints and uncontrollable events, with tools like TiPEX and GREP supporting enforcement[4]. **Synthesis:** MRAs and their extensions provide a rigorous basis for runtime restriction but face enforceability limits in non-deterministic and multi-agent settings, motivating the need for layered and adaptive governance architectures.

**2.2 Controlled Agentic AI Systems (CAIS) and Deterministic Governance** The CAIS framework embeds governance as a deterministic operator within AI decision pipelines, ensuring constraint-aware, auditable, and reproducible decision-making. Empirical studies demonstrate that CAIS outperforms approval-only strategies in federated and multi-agent environments by reducing constraint violations and stabilizing system dynamics without degrading performance[12]. Key features include:

**Constraint projection:** Transforming proposed actions into compliant executed actions.

**Audit trace semantics:** Enabling replayability and regulatory compliance.

**Stabilizing transformation:** Reducing action-level variance and intervention costs. **Synthesis:** CAIS operationalizes deterministic governance, offering formal guarantees and empirical effectiveness, but introduces complexity and integration overhead in large-scale deployments.

## 2.3 Constitutional Autonomy and Normative Reasoning

Constitutional Autonomy frameworks extend runtime enforcement beyond training-phase alignment by embedding normative reasoning and constitutional attention mechanisms directly into AI architectures. This enables: **Continuous runtime enforcement:** Reducing harmful behaviors and enhancing adversarial robustness[2]. **Normative prior engineering:** Integrating ethical and legal norms as first-class architectural elements. **Principled conflict resolution:** Supporting interpretable and contestable decision-making. **Synthesis:** These frameworks bridge technical and normative domains, but empirical validation is at an early stage, and integration with legacy systems remains a challenge.

**2.4 Probabilistic Requirement Modeling and Outcome-Centric Governance** Probabilistic Requirement Modeling (PRM) offers an outcome-centric formalism for non-deterministic AI systems, redefining requirements in terms of use cases, user intent, and measurable outcomes. PRM supports: **Adaptive workflow orchestration:** Aligning with regulatory frameworks (e.g., EU AI Act)[13]. **Continuous validation:** Facilitating ongoing compliance and risk management. **Synthesis:** PRM addresses the probabilistic and adaptive nature of modern AI, but practical adoption depends on integration with runtime monitoring and assurance tools.

## 2.5 Legitimacy Layer and Model-Agnostic Middleware

The Legitimacy Layer is a model-agnostic middleware architecture that evaluates governance signals— uncertainty, impact, reversibility, and contestation—in real time. It routes AI decisions through a legitimacy controller, enforcing structural human oversight, contestation, and escalation during runtime[5][6]. Features include: **Four-state autonomy model:** Normal, Reduced, Human Oversight Required, Safe Halt. **Execution directives:** Execute, execute_async, escalate, halt. **Structural enforcement:** Embedding human inclusion as an architectural property. **Synthesis:** The Legitimacy Layer closes the legitimacy gap in runtime execution, but widespread adoption and interoperability with diverse AI systems are ongoing challenges.

**3. Empirical Studies of Safety Filters, Shielding, and Runtime Assurance**

## 3.1 Safety Filters and Shielding in LLM Agents

Empirical studies on safety filters and shielding in multi-step LLM agents reveal: **Multi-stage output filtering:** Reduces harmful outputs but faces diminishing returns and adversarial bypass (e.g., coordinated jailbreaks)[3][14].

**Language and context sensitivity:** Effectiveness varies across languages and harm categories, with higher vulnerabilities in non-English contexts[15].

**Advanced moderation frameworks:** Tools like Legilimens and SafeIntervention dynamically adjust internal representations to defend against jailbreaks while preserving utility[16][17].

**Function call vulnerabilities:** Over 90% success rate for jailbreaks via function calls, highlighting the need for specialized safety filters[18]. **Synthesis:** While safety filters and shielding are effective in reducing certain risks, they are not foolproof and require continuous adaptation to adversarial tactics and context-specific vulnerabilities.

## 3.2 Runtime Assurance Frameworks and Hybrid Controllers

Runtime Assurance (RTA) frameworks employ hybrid controllers that monitor system state and switch to simpler safety controllers to avoid hazards. Empirical validation includes: **Aerospace and vehicle safety:** RTA frameworks ensure hard safety constraints while allowing performance optimization[19][20].

**Certification challenges:** Alignment with standards (e.g., DO-178C) and traceability are critical for operational safety[21].

**Distributed frameworks:** M-DRTA and Black-Box Simplex architectures support multi-agent and complex controller scenarios[22][23].

**Recovery mechanisms:** Extending safety shields with recovery logic improves resilience in multi-agent systems[24]. **Synthesis:** RTA frameworks provide robust runtime assurance but face challenges in certification, recovery rates, and integration with learning-based controllers.

## 3.3 Integrated Safety Architectures and Empirical Validation

Integrated safety architectures validated in uncertain environments include: **Learning-based safety filters:** Robust optimization and online adaptation ensure high-probability safety in unknown or noisy systems[25][26]. **Control barrier functions (CBFs):** Applied as add-ons to LLMs and control systems for real-time intervention[27][28]. **Adaptive shielding:** Hamilton-Jacobi reachability and conformal prediction methods reduce safety violations during reinforcement learning[29][30]. **Domain-specific validation:** Medical, energy, and robotics applications demonstrate improved safety and performance[31][32].

**Synthesis:** Empirical validation confirms the effectiveness of integrated safety architectures, but scalability and context sensitivity remain open issues.

**4. Dynamic Adaptation to Changing Risk and Environmental Conditions** **4.1 Legitimacy Layer: Real-Time Adaptation and Governance Signals** The Legitimacy Layer dynamically adjusts AI action sets based on real-time governance signals: **Signal evaluation:** Uncertainty, impact, reversibility, and contestation are continuously assessed[5]. **Execution routing:** Decisions are routed to appropriate autonomy states and directives (e.g., escalate for high-impact, high-uncertainty actions). **Structural oversight:** Human inclusion, contestability, and escalation are enforced as architectural properties. **Synthesis:** This approach enables nuanced, context-sensitive adaptation of AI autonomy, balancing operational efficiency with safety and legitimacy.

## 4.2 Runtime Certification and Dynamic Safety Management

Best practices for runtime certification and dynamic safety management include: **Continuous monitoring:** Dynamic risk management and runtime certification are essential for dependable autonomous systems[33]. **Formal verification:** Hybrid programs and theorem provers support design-time verification of safety properties[34]. **Distributed assurance:** Frameworks like M-DRTA balance safety and efficiency in multi-vehicle systems [22]. **Automated recovery:** Symbolic rewriting and SMT solvers enable formal verification of safety recovery[35]. **Synthesis:** Dynamic certification frameworks are critical for evolving AI systems but require structured research and cross-domain collaboration.

**4.3 Predictive Risk Modeling and Continuous Runtime Assessment** AI governance frameworks increasingly incorporate predictive risk modeling: **Machine learning integration:** Supervised and reinforcement learning forecast risk trajectories and adapt decisions[36][37]. **Dynamic risk scoring:** Algorithms continuously adjust to regulatory changes and security events[37]. **Lifecycle-based control:** Standards like ISO/IEC 42001:2023 and NIST AI RMF support continuous improvement and risk-driven governance[38].

**Synthesis:** Predictive risk modeling enhances real-time risk assessment and mitigation but depends on robust data integration and explainability.

## 4.4 Empirical Validation of Integrated Safety Architectures

Empirical studies validate integrated safety architectures for managing irreducible uncertainty: **Robust optimization:** Ensures safety with high probability as more data is collected[25]. **Adaptive control:** Real-time adjustment of safety margins under distribution shifts[39][40]. **Domain-specific frameworks:** Healthcare, energy, and robotics applications demonstrate practical effectiveness[31][32]. **Synthesis:** Integrated safety architectures are effective in dynamic, uncertain environments, but require ongoing adaptation and validation.

**5. Empirical Studies vs Conceptual Frameworks: Comparative Analysis** **5.1 Empirical Evidence for Runtime Governance and Safety Mechanisms** Empirical studies highlight: **Fundamental limits:** Impossibility results for certain policy enforcement in multi-agent systems and governance blind spots (e.g., routing gap)[7]. **Centralized control layers:** Improve policy compliance and fault recovery but introduce overhead and scalability challenges[41]. **Dynamic consent mechanisms:** Enable sub-second enforcement and maintain persona coherence under governance constraints[42]. **Synthesis:** Empirical evidence supports the effectiveness of runtime governance mechanisms but underscores practical limitations in scalability, latency, and enforcement visibility.

## 5.2 Validation and Performance of Conceptual Frameworks

Conceptual frameworks such as the Legitimacy Layer, CAIS, and A4-Gov have been validated through: **Prototype implementations:** LLM-controlled UAVs with runtime assurance mechanisms[6]. **Case studies:** Nuclear power, healthcare, and multi-agent simulations[43][44]. **Auditability and reproducibility:** Formal guarantees and audit trace semantics[12]. **Synthesis:** Conceptual frameworks provide robust architectures for runtime governance, but real-world adoption and interoperability remain ongoing challenges.

## 5.3 Lessons from Safety-Critical Domains

Empirical case studies in nuclear power, healthcare, and other domains reveal: **Multi-dimensional evaluation:** Integration of social, economic, and technical criteria[45]. **Continuous monitoring:** Proactive maintenance and dynamic risk modeling[46][47]. **Organizational factors:** Market design, regulatory environment, and workforce capabilities influence governance outcomes[48]. **Synthesis:** Safety-critical domains underscore the importance of continuous monitoring, adaptive governance, and multi-stakeholder engagement.

## 6. Research Gaps and Future Directions

## 6.1 Legitimacy Gap and Human Oversight

Current methodologies exhibit a legitimacy gap during AI decision execution, where active human oversight, contestability, and escalation are lacking[5]. Frameworks like the Legitimacy Layer and the EU AI Act propose structural solutions, but empirical validation and adoption are limited.

## 6.2 Enhancing Information Security Risk Assessment for AI

Traditional risk assessment methods are inadequate for AI-specific threats (e.g., adversarial attacks, data poisoning). Enhancements include: **Dynamic, explainable models:** Bayesian networks, neural networks, and hybrid frameworks[49][50]. **Automated, real-time assessment:** Attack graphs, OSCAL, and domain-specific languages[51]. **Explainable AI integration:** Improves transparency and trust in risk evaluations[52].

## 6.3 Interoperability and Structural Failure Modes

Implementation of runtime restriction mechanisms is hindered by: **Fragmented standards:** Metadata formats and proprietary systems[53]. **Structural failures:** Timing, visibility, and abstraction failures in governance[54]. **Usability barriers:** Workflow and policy complexity[55].

## 6.4 Human-in-the-Loop Effectiveness and Contextual Factors

HITL effectiveness is affected by complacency, workload, and organizational norms. Minimum governance requirements and adaptive oversight frameworks are needed to mitigate these factors[56].

## 6.5 Future Research Directions

**Continuous human oversight:** Operationalizing oversight during runtime, especially in multi-agent and high-autonomy settings. **Interoperability:** Standardizing middleware and governance signals across AI systems. **Dynamic risk assessment:** Developing AI-specific, explainable, and automated frameworks. **Legitimacy and HITL:** Embedding role-specific, context-aware governance models. **AGI and critical infrastructure:** Bridging technical and regulatory advances for safe deployment[8][9] [10][57].

## Synthesis and Conclusion

The research landscape on runtime restriction mechanisms for AI decision-support systems is characterized by a rich interplay between formal modeling, empirical validation, and adaptive governance. Formal frameworks such as MRAs, CAIS, and Constitutional Autonomy provide the theoretical foundation for deterministic and normative enforcement, while adaptive architectures like the Legitimacy Layer address the need for real-time, context-sensitive oversight. Empirical studies validate these approaches in diverse domains but reveal persistent gaps in scalability, interoperability, and human-in-the-loop effectiveness. Bridging these gaps through interdisciplinary research, standardization, and dynamic regulatory frameworks is essential for the safe and legitimate deployment of AI in critical and evolving environments[1][2][5][6].

## References

1. Modeling runtime enforcement with mandatory results automata Dolzhenko, E., Ligatti, J., Reddy, S. International Journal of Information Security, 2015 https://www.scopus.com/pages/publications/84921069010?origin=scopusAI

2. Toward Constitutional Autonomy in AI Systems: A Theoretical Framework for Aligned Agentic Intelligence Torgbi Agbemabiese, W. IEEE Access, 2026 https://www.scopus.com/pages/publications/105027519739?origin=scopusAI

3. A Theoretical Framework for the Security of Multi-stage LLM Output Filtering Pipelines Shang, Z., Liu, H. Lecture Notes in Computer Science, 2027 https://www.scopus.com/pages/publications/105047010679?origin=scopusAI

4. On the Runtime Enforcement of Timed Properties Falcone, Y., Pinisetty, S. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2019 https://www.scopus.com/pages/publications/85075729576?origin=scopusAI

5. The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems Aarab, H. International Conference on Human Centric Artificial Intelligence, ICHCAI 2026 - 1st International Conference, 2026 https://www.scopus.com/pages/publications/105046217618?origin=scopusAI

6. Safe Experimentation with LLM-Controlled UAVs: An Agile Systems Engineering Approach to Requirements Development for Autonomous Systems Harris, M., Madden, D., Thomas, K. Proceedings - 2025 IEEE 33rd International Requirements Engineering Conference Workshops, REW 2025, 2025 https://www.scopus.com/pages/publications/105020970136?origin=scopusAI

7. Fundamental Limits of Runtime Policy Enforcement in Multi-agent AGI Systems Shukla, S., Joshi, H. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105047047250?origin=scopusAI

8. Emerging Standards Best Practices and Future Research Directions in Artificial Intelligence Security Systems Abdulla, H.Y., Al-Omari, F. Global Risk Management and Governance in AI Security Operations, 2026 https://www.scopus.com/pages/publications/105047645749?origin=scopusAI

9. The Yellow Brick Road to AGI: Governance Infrastructure as a Constitutive Requirement for General Intelligence Spehar, G.D., Mittal, A. 2026 International Conference on Artificial Intelligence, Systems, and Emerging Technologies, ICAISET 2026, 2026 https://www.scopus.com/pages/publications/105042178957?origin=scopusAI

10. Safeguarding Artificial Intelligence in Autonomous Vehicles: Industry Perspectives and Research Challenges Hamad, M., Knoop, S., Assaf, C., Steinhorst, S. Proceedings - 17th ACM/IEEE International Conference on Cyber-Physical Systems, ICCPS 2026, 2026 https://www.scopus.com/pages/publications/105044204447?origin=scopusAI

11. A theory of runtime enforcement, with results Ligatti, J., Reddy, S. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2010 https://www.scopus.com/pages/publications/78049404569?origin=scopusAI

12. Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines Miller, T. Machine Learning and Knowledge Extraction, 2026 https://www.scopus.com/pages/publications/105040121699?origin=scopusAI

13. Probabilistic Requirement Modeling For Enterprise AI Workflow Orchestration: An Outcome-Centric Framework For Non-Deterministic Systems Narasimhan, V. International Journal of Artificial Intelligence and Machine Learning, 2026 https://www.scopus.com/pages/publications/105046158647?origin=scopusAI

14. On Targeted Output Generation via Adversarial Reframing in Language Models Sakib, S.K., Kar, S., Das, A.B. Lecture Notes in Computer Science, 2026 https://www.scopus.com/pages/publications/105047003609?origin=scopusAI

15. Differences in Safety Risks Across Languages in Health-Relevant Queries: Vulnerability Analysis of Large Language Model Responses Joshi, S., Mehta, M.A., Mendoza, M., (...), Singh, V.K. JMIR Formative Research, 2026 https://www.scopus.com/pages/publications/105042291746?origin=scopusAI

16. Legilimens: Practical and Unified Content Moderation for Large Language Model Services Wu, J., Deng, J., Pang, S., (...), Xu, W. CCS 2024 - Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security, 2024 https://www.scopus.com/pages/publications/85208151256?origin=scopusAI

17. SafeInt: Shielding Large Language Models from Jailbreak Attacks via Safety-Aware Representation Intervention Wu, J., Chen, C., Hou, C., Yuan, X. EMNLP 2025 - 2025 Conference on Empirical Methods in Natural Language Processing, Findings of EMNLP 2025, 2025 https://www.scopus.com/pages/publications/105028960954?origin=scopusAI

18. The Dark Side of Function Calling: Pathways to Jailbreaking Large Language Models Wu, Z., Gao, H., He, J., Wang, P. Proceedings - International Conference on Computational Linguistics, COLING, 2025 https://www.scopus.com/pages/publications/85218487775?origin=scopusAI

19. Accounting for helpful and harmful human reactions in run-time assurance frameworks Fuller, J.G., Hook, L., Hutchins, N. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2017 https://www.scopus.com/pages/publications/85040977584?origin=scopusAI

20. Optimal Runtime Assurance via Reinforcement Learning Miller, K., Zeitler, C.K., Shen, W., (...), Mitra, S. Proceedings - 15th ACM/IEEE International Conference on Cyber-Physical Systems, ICCPS 2024, 2024 https://www.scopus.com/pages/publications/85198538372?origin=scopusAI

21. Certification Aspects of Runtime Assurance for Urban Air Mobility Torens, C., Nagarajan, P., Schirmer, S., (...), Manfredi, G. AIAA SciTech Forum and Exposition, 2024, 2024 https://www.scopus.com/pages/publications/85194078073?origin=scopusAI

22. M-DRTA: A Distributed Runtime Monitoring and Assurance Framework for Multi-vehicle Behavior Planning Peng, Y., Tan, G., Wang, X. Proceedings - 2024 IEEE 30th International Conference on Embedded and Real-Time Computing Systems and Applications, RTCSA 2024, 2024 https://www.scopus.com/pages/publications/85207099424?origin=scopusAI

23. The black-box simplex architecture for runtime assurance of multi-agent CPS Sheikhi, S., Mehmood, U., Bak, S., (...), Stoller, S.D. Innovations in Systems and Software Engineering, 2025 https://www.scopus.com/pages/publications/85188254218?origin=scopusAI

24. Reliable Intention Selection in BDI Agents with Recovery Shields Ferrando, A., Cardoso, R.C. Frontiers in Artificial Intelligence and Applications, 2025 https://www.scopus.com/pages/publications/105024435457?origin=scopusAI

25. Learning Safety Filters for Unknown Discrete-Time Linear Systems Farokhi, F., Leong, A.S., Zamani, M., Shames, I. IEEE Control Systems Letters, 2023 https://www.scopus.com/pages/publications/85161551510?origin=scopusAI

26. Safety-Aware Residual Reinforcement Learning for Spacecraft Formation with Coupled Relative Translation and Attitude Dynamics Sun, Y., Huang, D., Li, Z. Guidance, Navigation and Control, 2026 https://www.scopus.com/pages/publications/105046114169?origin=scopusAI

27. Learning Safe Control via On-the-Fly Bandit Exploration Capone, A., Cosner, R., Ames, A., Hirche, S. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105023562085?origin=scopusAI

28. Safety-Enhanced COLREGs-Compliant Path Planning for USVs with a CBF-Based Safety Shield Yun, S.- J., Kim, H., Kwon, J.-W., (...), Choi, J.-H. Journal of Marine Science and Engineering, 2026 https://www.scopus.com/pages/publications/105048465787?origin=scopusAI

29. Safe Learning in the Real World via Adaptive Shielding with Hamilton-Jacobi Reachability Lu, M., Gosain, J.S., Sang, L., Chen, M. Proceedings of Machine Learning Research, 2025 https://www.scopus.com/pages/publications/105013956118?origin=scopusAI

30. Probabilistic Safety for Hard-to-Formalize Constraints via Conformal Neural CBFs Hirano, K., Takeishi, N., Yairi, T. Proceedings of the IEEE Conference on Decision and Control, 2025 https://www.scopus.com/pages/publications/105031882476?origin=scopusAI

31. Safety filters as a means for ensuring functional safety in data-driven control: an overview Hess, M., Piscol, B.-M., Bohn, C., Hohmann, S. At-Automatisierungstechnik, 2026 https://www.scopus.com/pages/publications/105040974990?origin=scopusAI

32. Deep reinforcement learning-based predictive control for uncertain mechanical leg trajectory tracking Chen, M., Hu, L., Huang, X. Applied Mathematical Modelling, 2027 https://www.scopus.com/pages/publications/105042642918?origin=scopusAI

33. Structuring Research Related to Dynamic Risk Management for Autonomous Systems Adler, R., Reich, J., Hawkins, R. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85172415041?origin=scopusAI

34. A Verification Framework for Runtime Assurance of Autonomous UAS Slagel, J.T., White, L.M., Dutle, A., (...), Crespo, N. AIAA/IEEE Digital Avionics Systems Conference - Proceedings, 2024 https://www.scopus.com/pages/publications/85211229878?origin=scopusAI

35. Automating Recoverability Proofs for Cyber-Physical Systems with Runtime Assurance Architectures Nigam, V., Talcott, C. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2023 https://www.scopus.com/pages/publications/85164927589?origin=scopusAI

36. The contribution of AI-based stakeholder network modeling to risk governance in housing development Gharehgozli, M.A. International Journal of Housing Markets and Analysis, 2025 https://www.scopus.com/pages/publications/105016732079?origin=scopusAI

37. The Role of AI and Machine Learning in Next-Generation Governance, Risk, and Compliance (GRC) Platforms Tarakampet, S., Tatavarthi, S., Puvvula, G. International Conference on Ubiquitous and Future Networks, ICUFN, 2026 https://www.scopus.com/pages/publications/105047280674?origin=scopusAI

38. Conceptual Model of Risk Based Artificial Intelligence Management System in Financial Technology Lestari, M., Sitokdana, M.N.N., Sari, M.K., (...), Gunawan, R.P. Proceedings - 2026 International Conference on Current Research in Artificial Intelligence and Data Science, ICCRAIDS 2026, 2026 https://www.scopus.com/pages/publications/105041647774?origin=scopusAI

39. ATOM-CBF: Adaptive Safe Perception-Based Control under Out-of-Distribution Measurements Yun, K.S., Azizan, N. Proceedings of Machine Learning Research, 2026 https://www.scopus.com/pages/publications/105046072397?origin=scopusAI

40. Safe Control using Learned Safety Filters and Adaptive Conformal Inference Huriot, S., Tabbara, I., Sibai, H. Proceedings of Machine Learning Research, 2026 https://www.scopus.com/pages/publications/105046061744?origin=scopusAI

41. An Agent Execution Control Layer for Organizational Multi-Agent Systems Dalal, S., Rambola, R.K. 2026 International Conference on Innovations in Emerging Technologies for Sustainable Development: Empowering Innovation for a Sustainable Future, ICIETSD 2026 - Conference Proceedings, 2026 https://www.scopus.com/pages/publications/105045456666?origin=scopusAI

42. Conflict resolution within multi-agent system in collaborative design Liu, Q., Cui, X., Hu, X. Proceedings - International Conference on Computer Science and Software Engineering, CSSE 2008, 2008 https://www.scopus.com/pages/publications/61849185636?origin=scopusAI

43. Resilience Governance in Nuclear Safety: Insights from China’s AI-Driven Innovative Practices Peng, R., Guo, D. Nuclear Technology, 2026 https://www.scopus.com/pages/publications/105033643463?origin=scopusAI

44. Evidence-Driven AI Governance for Healthcare: A PEARL-PATHWAY Analysis of Madinah Alsaigh, R., Mehmood, R., Katib, I., (...), Alshmrany, S. International Journal of Advanced Computer Science and Applications, 2026 https://www.scopus.com/pages/publications/105039664592?origin=scopusAI

45. Multi-criteria decision making for nuclear power plant selection using fuzzy AHP: Evidence from Indonesia Abdullah, A.G., Shafii, M.A., Pramuditya, S., (...), Anzhar, K. Energy and AI, 2023 https://www.scopus.com/pages/publications/85152116420?origin=scopusAI

46. CONCEPTUAL FRAMEWORK TO ANALYZE AND MITIGATE AGING EFFECTS OF A SYSTEM IN NUCLEAR POWER PLANTS. Ahmed, Shahid null, 1985 https://www.scopus.com/pages/publications/0022193958?origin=scopusAI

47. Conceptual framework for formulating a focused and cost-effective fire protection program based on analyses of risk and the dynamics of fire effects Dey, M.K. Nuclear Engineering and Design, 1999 https://www.scopus.com/pages/publications/0033355843?origin=scopusAI

48. Retirement or Renewal? Decision-making processes for long-term operations of nuclear power plants Dei, G., Rizzetto, M., Missaglia, L., (...), Mignacca, B. Progress in Nuclear Energy, 2026 https://www.scopus.com/pages/publications/105044408028?origin=scopusAI

49. Methodologies for information security risk assessment: shortcomings for analysing artificial intelligence systems Agathangelos-Ioannou, G., Tsohou, A. International Journal of Information Security, 2026 https://www.scopus.com/pages/publications/105039706444?origin=scopusAI

50. A systematic mapping study on approaches for AI-supported security risk assessment Erdogan, G., Garcia- Ceja, E., Hugo, A., (...), Sen, S. Proceedings - 2021 IEEE 45th Annual Computers, Software, and Applications Conference, COMPSAC 2021, 2021 https://www.scopus.com/pages/publications/85115837460?origin=scopusAI

51. Towards the Automation of Attack Graph-Based Risk Assessment with OSCAL Koufos, I., Christopoulou, M., Xilouris, G., (...), Trakadas, P. Lecture Notes in Networks and Systems, 2025 https://www.scopus.com/pages/publications/105005932847?origin=scopusAI

52. Integrating Explainable AI to Enhance Dynamic Risk Assessment in Automated Driving Systems Patel, A.R., Gohler, T., Liggesmeyer, P. 2024 IEEE International Conference on Vehicular Electronics and Safety, ICVES 2024, 2024 https://www.scopus.com/pages/publications/105002127575?origin=scopusAI

53. Dual - track labeling regulation and institutional refinement for generative artificial intelligence Zhang, B., Li, M.-Q. Studies in Science of Science, 2026 https://www.scopus.com/pages/publications/105045419296?origin=scopusAI

54. From Policy to Pipelines: Closing the AI Governance Execution Gap Vasireddy, R. IEEE Access, 2026 https://www.scopus.com/pages/publications/105050162324?origin=scopusAI

55. The state of the art of application restrictions and sandboxes: A survey of application-oriented access controls and their shortfalls Schreuders, Z.C., McGill, T., Payne, C. Computers and Security, 2013 https://www.scopus.com/pages/publications/84876667819?origin=scopusAI

56. Realizing the Promise of AI Governance Involving Humans-in-the-Loop McKay, M.H. Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 2024 https://www.scopus.com/pages/publications/85215671189?origin=scopusAI

57. Towards an international regulatory framework for AI safety: lessons from the IAEA’s nuclear safety regulations Cha, S. Humanities and Social Sciences Communications, 2024 https://www.scopus.com/pages/publications/85190270476?origin=scopusAI
