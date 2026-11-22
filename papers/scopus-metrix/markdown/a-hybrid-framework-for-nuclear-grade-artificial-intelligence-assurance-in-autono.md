# A Hybrid Framework for Nuclear-Grade Artificial Intelligence Assurance in Autonomous Nuclear Power Reactor Operations

> **Source PDF:** `A Hybrid Framework for Nuclear-Grade Artificial Intelligence Assurance in Autonomous Nuclear Power Reactor Operations.pdf` · **Pages:** 4 · Converted by `scripts/paper2md.py` from the original PDF.

<!-- page 1 -->

VI. International Conference on Electrical, Computer and Energy Technologies (ICECET 2026)

6-9 July 2026, Rome-Italy

A Hybrid Framework for Nuclear-grade Artificial

Intelligence Assurance in Autonomous Nuclear

Power Reactor Operations

2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET) | 979-8-3195-0598-9/26/$31.00 ©2026 IEEE | DOI: 10.1109/ICECET65726.2026.11632747

Jonghyeok KIM Growth Research Laboratory KHNP Central Research Institute

Yongsik KIM Growth Research Laboratory KHNP Central Research Institute

Daejeon, Republic of Korea

Daejeon, Republic of Korea

jofficer@khnp.co.kr

yongsik.kim@khnp.co.kr

existed for decades, they often rely on rigid setpoints that do not account for the non-linear, dynamic evolution of complex "beyond-design-basis" accidents. This creates a critical "Assurance Gap," where the need for flexible response during rare events conflicts with the deterministic reliability required for regulatory certification.

Abstract— Achieving full autonomy in next-generation Nuclear Power Plants (NPP) requires a fundamental change from simple automation to intelligent decision-making. While traditional Rule-based Algorithms (RbA) provide the deterministic reliability necessary for safety-critical operations, they lack the flexibility to handle unforeseen, complex transients.

Furthermore, the transition from legacy analog systems to fully digital architectures has enabled the application of advanced data analytics. Recent breakthroughs in Generative Artificial Intelligence (GenAI) and Large Language Models (LLM) have introduced tools capable of synthesizing technical documentation and generating initial hypotheses for system optimization. Despite these capabilities, frontier models achieve only 50-53% accuracy on basic quantitative physics tasks. These models prioritize semantic plausibility over physical correctness, acting as "approximate guessers" that may violate fundamental physical constraints.

This paper proposes a hybrid architecture designed to achieve "Nuclear-grade Artificial Intelligence Assurance." To overcome the unacceptable computational latency and hallucination risks of massive Large Language Models (LLMs) in real-time control, the framework utilizes a lightweight Multi-Layer Perceptron (MLP) as the reasoning agent, tightly constrained by a deterministic Rulebased "Safety Shield." Evaluated against 500 complex transient scenarios sampled from the NPPAD dataset, the hybrid framework demonstrated an average execution latency of 4.2 milliseconds. Furthermore, it successfully resolved beyond-designbasis transients with a 95.0 percent success rate—a 17.0 percent improvement over standalone rule-based systems—while maintaining 100 percent compliance with immutable thermal limits such as the 350 degrees Celsius core temperature boundary. This research provides a computationally feasible and mathematically verifiable methodology for integrating AI into safety-critical Instrumentation and Control (I&C) systems.

This paper addresses these limitations by proposing a hybrid framework that bridges the gap between AI flexibility and nuclear-grade determinism. By integrating a "Safety Shield" derived from symbolic logic and physical laws, we establish a hierarchy where GenAI-driven reasoning is strictly bound by immutable safety envelopes. This approach aligns with international regulatory roadmaps for reliable and transparent AI integration in safety-critical environments.

Keywords—Generative Artificial Intelligence (GenAI), Rulebased Algorithms (RbA), Nuclear-grade AI Assurance, Autonomous Operation, Instrumentation and Control (I&C), Safety Shielding.

## II. RELATED WORK

## I. INTRODUCTION

The research landscape for autonomous nuclear operations is evolving from simple control loops to complex, cognitivelyaware systems. This section reviews the technological foundations of Agentic AI, Digital Twin-based management, Explainable AI, and the rigorous standards governing digital safety software.

The global nuclear industry is entering a significant digital transition to enhance the safety and economic viability of current and future reactor fleets. As existing facilities undergo digital modernization, the complexity of digital Instrumentation and Control (I&C) systems has increased, integrating thousands of interconnected sensors and actuators. The primary motivation for pursuing full autonomy in these systems is the mitigation of human error, which remains a contributing factor in approximately 70% to 80% of all operational incidents in Nuclear Power Plants (NPPs) [1].

A. Agentic AI and Domain-Specific Models

Recent research has successfully adapted compact language models for reactor control, demonstrating a phenomenon known as "variance collapse." When trained on vast synthetic reactor datasets, these domain-specific agents stabilize their executionlevel behavior, autonomously rejecting high-variance strategies and concentrating 95% of runtime execution on physically robust strategies. [2]

This increased complexity, however, presents a new challenge for reactor operators who must process an overwhelming volume of data during abnormal transients. The cognitive load required to identify fault origins and implement mitigation strategies in real-time can lead to decision-making fatigue or erroneous diagnoses. While automated systems have

979-8-3195-0598-9/26/$31.00 ©2026 IEEE

<!-- page 2 -->

B. Nearly Autonomous Management and Control (NAMAC)

specifically, Time (TIME), Reactor Average Temperature (TAVG), and Pressurizer Pressure (P)— extracted from the NPPAD dataset. This architecture ensures that the agent rapidly outputs deterministic control commands, such as targeted Emergency Core Cooling flow rates (WECS), entirely bypassing the semantic hallucinations and delays typical of standard LLMs .

The Nearly Autonomous Management and Control (NAMAC) framework utilizes digital twins for real-time diagnosis and prognosis in advanced reactors. A core component of NAMAC is the "discrepancy checker," which manages uncertainty by alerting operators when AI-driven recommendations deviate from expected physical states, providing a necessary layer of verification for regulatory acceptance. [3]

2. Safety Shield Layer and Baseline Rule-based Algorithm: The baseline Rule-based Algorithm (RbA) and the proposed Safety Shield share the same deterministic nature. They operate on standard proportional control logic and hard-wired Reactor Protection System (RPS) trip setpoints aligned with standard Emergency Operating Procedures (EOP). The Safety Shield strictly monitors immutable physical limits, specifically a maximum reactor core temperature limit of 350°C in this study. If the digital twin predicts that an AI-proposed action will violate this deterministic boundary, the shield overrides the command and immediately executes a predefined failsafe sequence (e.g., maximum emergency core cooling injection).

C. Explainable AI (XAI) for Diagnostic Reliability

A significant barrier to AI adoption in nuclear facilities is the "black-box" nature of deep learning. Techniques such as SHapley Additive exPlanations (SHAP) and Local Interpretable Model-agnostic Explanations (LIME) have emerged as essential tools for quantifying the contribution of specific physical variables to an AI's decision. This transparency enables operators to understand the phenomenological justification behind a diagnosis, enhancing trust in the decision-support system. [6]

D. Verification and Validation (V&V) of Digital Safety

Systems Nuclear-grade software must comply with rigorous standards such as IEEE Standard 603-2018 and IEEE Standard 7-4.3.2-2016. [4,5] Traditional Verification and Validation (V&V) processes for digital I&C systems ensure that software artifacts comply with requirement specifications through behavioral and post-layout simulations. The proposed hybrid framework leverages these standards by separating non-safetyrelated "Intelligent Agents" from safety-related "Safety Shields," allowing for advanced AI integration without compromising the V&V rigor of Class 1E components.

3. Validation Layer (Real-time Digital Twin Loop): To ensure computational feasibility within the strict latency margins of Nuclear I&C systems (< 100 ms), the validation layer avoids computationally exhaustive 3D fluid dynamics. Instead, it employs a fast-running, lumped-parameter dynamic simulator employs a datadriven mathematical surrogate model derived from NPPAD thermal-hydraulic data. This reduced-order Digital Twin rapidly calculates the -step future state ( ) of critical thermal-hydraulic parameters based on the AI's proposed action. As validated in our experimental setup, this highly optimized forwardsimulation loop executes in an average of 4.2 milliseconds on standard CPU hardware, guaranteeing real-time physical verification without computational bottlenecks.

## III. METHODOLOGY

This section delineates the proposed hierarchical assurance architecture and the mathematical logic governing runtime enforcement. The primary objective is to create a multi-layered defense-in-depth strategy for AI-driven decision processes, ensuring that every command is physically verified before actuation.

B. Mathematical Modeling of Runtime Decision Enforcement

To guarantee deterministic safety, the final Executed Action A is governed by a verification function . The decision logic is mathematically defined as:

A. Hierarchical Assurance Architecture

The proposed framework ensures Nuclear-grade AI Assurance through three distinct hierarchical layers:

= , , = 1

1. AI Reasoning Agent (MLP-based Real-time Execution): To address the computational feasibility and strict latency requirements of nuclear operations, the framework adapts the concept of a "domainspecific LLM" into a highly optimized execution layer. While massive language models are suitable for offline analysis of Natural Language Operating Procedures (NLOP), deploying them directly within a real-time control loop introduces unacceptable computational latency. Therefore, the execution-level GenAI Reasoning Agent is instantiated as a localized MultiLayer Perceptron (MLP) neural network. This lightweight model is trained directly on historical transient data and numerical physics parameters—

_	, , = 0

The verification function V returns 1 (Pass) only if the physics-informed confidence score (S#$%) for the AI's proposal exceeds a critical threshold (τ):

| −+,|

'( = 1 −

> .

where /01 is the future reactor state predicted by the fastloop digital twin loop and P34 is the goal state expected by the reasoning layer. If the condition fails('( ≤τ), indicating a potential safety limit violation (e.g., predicting a core

<!-- page 3 -->

computational latency well within the real-time operational margins for Nuclear I&C systems.

temperature exceeding 350°C), the Safety Shield instantly overrides the AI and reverts to the predefined rule-based failsafe sequence(A%607_/6%).

As detailed in Table I, the standalone RbA baseline operated with strict deterministic setpoints. While it successfully mitigated standard, single-fault transients, it failed to stabilize the reactor in 22.0% of the complex, beyond-design-basis scenarios due to logic branching exhaustion. In these multifault conditions, the predefined rules lacked the flexibility to adapt to non-linear physical changes.

C. Experimental Setup and Computational Feasibility

To rigorously evaluate the proposed hybrid framework and address the computational feasibility of the real-time Digital Twin validation loop, the experimental environment was established on a standard computational hardware setup (e.g., Intel Core i7 CPU, 16GB RAM). The evaluation utilized the Nuclear Power Plant Accident Data (NPPAD), an open timeseries dataset covering various accidents simulated via PCTRAN. The dataset encompasses 18 types of operating conditions, including Loss of Coolant Accidents (LOCA) and Steam Generator Tube Ruptures (SGTR).

Conversely, the proposed Hybrid Framework maintained a 95.0% average success rate across all complexity levels. The AI agent generated adaptive mitigation strategies that resolved complex transients where the standalone RbA failed. Crucially, all AI-proposed actions that violated the predefined deterministic safety limits within the validation loop were successfully intercepted by the Rule-based Safety Shield, maintaining 100% compliance with safety setpoints. This confirms that the integration of AI enhances diagnostic flexibility while the Safety Shield mathematically guarantees adherence to the reactor's Safe Operating Envelope.

For this study, 500 transient scenarios were randomly sampled across the dataset. The AI reasoning agent was trained using specific physical parameters, including Time (TIME), Reactor Coolant System Average Temperature ( T69 ), and Pressurizer Pressure (P), to predict the optimal Total Emergency Core Cooling System Flow. The Safety Shield was hard-coded with deterministic safety limits, such as a maximum core temperature of 350°C. During the real-time inference loop, if the Digital Twin predicted that the AI's proposed flow rate would violate these thermal limits ( '( ≤. ), the Safety Shield instantly intercepted the action and executed the baseline Rulebased Algorithm (RbA) fail-safe sequence.

**TABLE I. PERFORMANCE BENCHMARKING OF STANDALONE RBA**

### VS. THE HYBRID FRAMEWORK ON NPPAD DATASET

| Scenario Category | Standalone RbA Success | Proposed Hybrid Success | Delta (%) |
|---|---|---|---|
| Single Fault (Design Basis) | 100.0% | 100.0% | 0.0 |
| Dual Fault (Beyond Design) | 78.0% | 94.2% | +16.2 |
| Complex/Novel Transients | 64.5% | 91.8% | +27.3 |
| Total Weighted Average | 78.0% | 95.0% | +17.0 |

B. Definition of Success and Testing Methodology

In this evaluation, a "success" (Assurance Fidelity, F6//;<) is strictly defined as the framework's ability to mitigate a transient event and stabilize the reactor without the core temperature (T69) exceeding the deterministic safety limit of

350°C. To evaluate this, 500 transient scenarios were sequentially simulated using the sampled NPPAD dataset. To rigorously test the systems under beyond-design-basis conditions, simultaneous mechanical valve constraints were deliberately injected into the data stream, artificially capping the maximum allowable Emergency Core Cooling flow rate.

C. Analysis of 22.0% Failure Rate in Standalone RbA

Under these multi-fault conditions, the standalone Rulebased Algorithm exhibited a 22.0% failure rate. This failure originates from "logic branching exhaustion." Because the conventional proportional control logic reacts only after predetermined temperature thresholds are crossed, its delayed response under restricted valve capacities led to thermal accumulation, ultimately failing to prevent the temperature from exceeding 350°C.

**Fig. 1. Comparison of Assurance Fidelity ( F6//;< ) across varying scenario complexity levels.**

A. Real-time Implementation and Performance Benchmarking

The hybrid framework successfully processed all 500 sampled NPPAD scenarios locally, demonstrating minimal

<!-- page 4 -->

D. Analysis of 95.0% Success Rate in Hybrid Framework

viable actions. Ultimately, the proposed framework achieved a 95.0% mitigation success rate across complex transients, proving that it is possible to bridge the gap between AI diagnostic flexibility and nuclear-grade safety determinism. Future work will focus on expanding the validation loop to encompass full-scope 3D core simulators and hardware-in-theloop (HIL) testing.

Conversely, the 95.0% success rate of the proposed hybrid framework is achieved through the integration of the MLPbased reasoning agent with deterministic outcome-space guarantees. The theoretical reliance on macro-level behavioral phenomena, such as "variance collapse" typically associated with frontier LLMs, is entirely avoided in this framework. Instead, empirical results demonstrate that the localized MLP agent captured the non-linear operational dynamics between system pressure (P) and temperature (T69) early in the transient progression. This allowed the agent to compute and preemptively output non-intuitive cooling rates before the mechanical valve limits became a critical bottleneck. Simultaneously, the Safety Shield mathematically ensured that none of these preemptive strategies violated the Safe Operating Envelope, yielding high-fidelity, closed-loop mitigation without hallucination risks.

## References

[1] J. Qi et al., “Nuclear Power Plant Accident Data (NPPAD) for diagnostic benchmark,” Tsinghua Univ., 2022.

[2] Y. Lee et al., “Agentic physical AI toward a domain-specific foundation model for nuclear reactor control,” arXiv preprint arXiv:2512.23292, 2025.

[3] Lin et al., “Development and assessment of a nearly autonomous management and control system for advanced reactors,” Annals of Nuclear Energy, 2021.

[4] IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations, IEEE Standard 603-2018, 2018.

[5] IEEE Standard Criteria for Programmable Digital Computers in Safety V. CONCLUSION Systems of Nuclear Power Generating Stations, IEEE Standard 7-4.3.22016, 2016.

[6] S. Joo et al., “Leveraging explainable AI for reliable prediction of nuclear This study presented and rigorously validated a hybrid AI assurance framework for autonomous nuclear operations. By replacing computationally heavy LLMs with a highly optimized MLP reasoning agent, the system achieved a real-time inference latency of 4.2 milliseconds, well within the strict margins required for nuclear I&C systems. Through testing against 500 dynamic scenarios from the NPPAD benchmark, the framework demonstrated that it can overcome the logic branching exhaustion typical of traditional Rule-based Algorithms during multi-fault transients. The integration of a deterministic Safety Shield mathematically guaranteed 100% compliance with critical physical boundaries, successfully intercepting any non- power plant severe accident progression,” Reliability Engineering & System Safety, vol. 264, 2025.

[7] B. Qi, X. Xiao, J. Liang, et al., “An open time-series simulated dataset covering various accidents for nuclear power plants,” Scientific Data, vol. 9, no. 766, 2022.

[8] Considerations for Deploying Artificial Intelligence Applications in the Nuclear Power Industry, International Atomic Energy Agency (IAEA), Nuclear Energy Series, 2025.

[9] Fiscal Years 2023–2027 Artificial Intelligence Strategic Plan, United States Nuclear Regulatory Commission, 2023. .
