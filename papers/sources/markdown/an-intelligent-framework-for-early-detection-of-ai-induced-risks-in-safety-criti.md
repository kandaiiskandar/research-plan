# An Intelligent Framework for Early Detection of AI-Induced Risks in Safety-Critical Systems

> **Source PDF:** `An Intelligent Framework for Early Detection of AI-Induced Risks in Safety-Critical Systems.pdf` · **Pages:** 33 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Article An Intelligent Framework for Early Detection of AIInduced Risks in Safety-Critical Systems Thacha Lawanna International College of Digital Innovation, Chiang Mai University, Chiang Mai 50200, Thailand E-mail: thacha.l@icdi.cmu.ac.th (Corresponding author) Abstract. IRED-AI is an intelligent framework designed for the early detection of AIinduced risks in safety-critical systems, including healthcare, autonomous driving, aviation, industrial control, and cybersecurity. Unlike traditional detection models that optimize single metrics, IRED-AI unifies continuous monitoring, hybrid statistical–AI anomaly detection, explainable reasoning, and retrieval-guided adaptation into a cohesive, SLA-compliant architecture. A multi-view feature engineering pipeline captures contextual, signal, and semantic health indicators to construct risk embeddings that enable real-time anomaly scoring and efficient case retrieval. The framework’s adaptive alert escalation process provides operators with actionable insights at informational, cautionary, critical, and emergency levels, while integrated explainable AI modules ensure transparency and regulatory compliance. Best results across ten benchmark datasets confirm its superiority: accuracy of 95.20%, AUROC up to 0.960 (aviation), AUPRC gains of +3.37%, latency reduced to 90–150 ms (−20.83%), false alarms lowered to 7.20% (−22.22%), throughput reaching 1500 q/s, Top-1 retrieval accuracy of 92.40% (Top-5 = 97.20%), robustness of 0.920, interpretability of 0.900, and SLA compliance of 98.00%. Statistical analysis confirms these improvements as significant (p < 0.050), demonstrating that IRED-AI’s enhancements are not incidental but systematically robust. The framework also incorporates a knowledge retention loop, enabling continuous adaptation through operator feedback and periodic recalibration, ensuring resilience against data drift, adversarial manipulation, and emerging risks. By combining technical excellence with practical trustworthiness, IRED-AI provides a deployable, domain-general solution that advances safety assurance in missioncritical environments where failures carry unacceptable human and economic consequences. Keywords: AI-induced risk detection, safety-critical systems, anomaly detection, case-based retrieval, SLA-aware real-time monitoring

ENGINEERING JOURNAL Volume 30 Issue 7 Received 28 September 2025 Accepted 30 June 2026 Published 31 July 2026 Online at https://engj.org/ DOI:10.4186/ej.2026.30.7.1

<!-- page 2 -->

## 1. Introduction

responses rather than opaque alerts. By fulfilling these objectives, the framework will contribute to safer, more reliable, and more trustworthy deployment of AI in mission-critical applications.

Artificial Intelligence (AI) has become an indispensable component in safety-critical systems such as autonomous vehicles, medical devices, aviation control, and industrial automation [1]. These domains demand real-time decision-making, high precision, and unwavering reliability. While AI enables enhanced perception, prediction, and optimization, its integration introduces new forms of risks that traditional safety mechanisms cannot fully address [2]. AI models are often data-driven, adaptive, and non-deterministic, leading to vulnerabilities such as bias, adversarial manipulation, data drift, or unexpected emergent behaviors [3]. Failures in such environments can result in catastrophic outcomes, including loss of human lives or large-scale economic disruption [4]. Consequently, early detection of AIinduced risks is paramount to ensure resilience and trustworthiness in these systems [5]. A systematic framework that unites monitoring, anomaly detection, and explainability is essential to preempt failures before they escalate [6]. This research proposes an intelligent framework capable of identifying risks proactively, enabling rapid intervention in safety-critical contexts.

The significance of this research lies in its potential to bridge critical gaps between AI innovation and safety assurance in high-stakes environments. Safety-critical systems demand near-zero tolerance for failure, yet the inherent uncertainties of AI pose significant barriers to trust and adoption. By proposing an intelligent framework for early detection, this work contributes to enhancing operational resilience, ensuring risks are identified and mitigated before they compromise system safety. Moreover, the research advances the field of trustworthy AI by combining anomaly detection with explainability, offering not only accurate alerts but also transparent reasoning behind system behavior. Such capabilities are crucial for compliance with emerging regulatory standards and ethical guidelines. Beyond theoretical advancement, the framework has practical value, enabling organizations in healthcare, transportation, and industrial automation to deploy AI solutions with greater confidence, ultimately safeguarding human lives, assets, and societal infrastructure.

This research offers three major contributions. First, Framework Design: a novel intelligent architecture is developed that integrates real-time monitoring, AIenhanced anomaly detection, and explainable modules to address diverse risk scenarios in safety-critical systems. Second, Experimental Protocol: a rigorous evaluation methodology is proposed using multiple datasets and simulation environments across domains such as healthcare, autonomous driving, and industrial automation. The protocol benchmarks performance using metrics including detection accuracy, latency, false alarm rate, and interpretability. Third, Theoretical and Practical Insights: the study provides a taxonomy of AI-induced risks, formalizes detection challenges, and identifies tradeoffs between robustness and efficiency. These insights are complemented with practical recommendations for deploying the framework in real-world systems under stringent safety requirements. Collectively, these contributions advance both the academic understanding and practical implementation of AI safety, paving the way for more resilient and trustworthy integration of AI into mission-critical domains.

Despite progress in AI safety, current approaches for risk management in safety-critical systems remain insufficient [7]. Traditional verification and validation processes assume predictable system behavior, which conflicts with AI’s dynamic and probabilistic nature [8]. Runtime monitoring and anomaly detection techniques often face challenges such as high false positives, slow detection latency, and limited adaptability to evolving risks [9]. Moreover, explainability is frequently overlooked, leaving operators uncertain about why certain warnings are triggered [10]. This gap hinders trust and slows adoption of AI in critical environments [11]. Without an intelligent, holistic framework, the risks of AI-induced failures remain inadequately managed, creating vulnerabilities in high-stakes domains such as healthcare, autonomous driving, and industrial control [12]. Therefore, a new solution is required that not only improves detection accuracy and timeliness but also integrates interpretability and actionable insights to support decision-makers under real-world operational constraints.

The primary objective of this research is to design and evaluate an intelligent framework that can detect AIinduced risks in safety-critical systems at an early stage. Specifically, the framework aims to combine advanced anomaly detection, adaptive learning mechanisms, and explainable AI modules to identify deviations in system performance with minimal latency. It seeks to ensure that risks are flagged in time for corrective action, reducing the likelihood of catastrophic system failures. The framework also strives to maintain a balance between detection accuracy and operational efficiency, ensuring it can be deployed in real-time environments. Furthermore, the research intends to provide actionable insights to operators and decision-makers, enabling informed

Unlike existing AI risk detection approaches that focus on isolated capabilities such as anomaly detection, explainability, or monitoring, IRED-AI integrates realtime monitoring, hybrid statistical-AI anomaly detection, explainable reasoning, similarity-based risk retrieval, and adaptive learning within a unified architecture. This integration enables not only accurate risk detection but also transparent decision support and continuous adaptation across multiple safety-critical domains. To the best of our knowledge, no existing framework combines these capabilities into a single operational pipeline designed specifically for AI-induced risk detection.

<!-- page 3 -->

2. Literature Review 2.1. AI for High-Stakes Safety Systems Artificial Intelligence has transformed safety-critical systems by enabling intelligent decision-making, automation, and predictive analytics across domains such as healthcare, autonomous driving, aviation, and industrial control [13]. In healthcare, AI supports diagnostic imaging, patient monitoring, and clinical decision support, offering faster and more accurate detection of life-threatening conditions [14]. However, reliance on AI models can lead to misdiagnosis if biases or anomalies in data are not addressed [15]. In autonomous driving, AI enables perception, navigation, and collision avoidance, where real-time accuracy is essential to prevent accidents [16]. Failures in object recognition or environmental perception pose significant safety hazards. Similarly, in aviation, AI is applied to predictive maintenance, air traffic management, and pilot assistance, yet errors or adversarial inputs could disrupt flight safety [17]. In industrial control systems, AI optimizes resource management, predictive fault detection, and cyber-physical integration, but vulnerabilities may lead to downtime, equipment damage, or safety violations [18]. The integration of AI in these domains creates opportunities for efficiency and reliability, but the non-deterministic nature of AI also introduces risks that conventional safety assurance methods cannot fully mitigate [19]. These risks underscore the importance of frameworks capable of real-time risk detection, interpretability, and adaptation, ensuring that AI-driven systems meet the stringent safety requirements of missioncritical environments. 2.2. Risk and Fault Detection in AI-Driven Systems

specific and struggle to generalize across contexts [25]. The growing complexity of AI-enabled systems demands integrated detection mechanisms that can combine predictive modeling, adaptive learning, and explainable reasoning [26]. Such mechanisms must also satisfy operational constraints such as low latency, scalability, and resilience to adversarial manipulation, thereby ensuring dependable risk detection in critical systems [27]. 2.3. Anomaly Detection and Explainable AI in Risk Monitoring

Anomaly detection has emerged as a cornerstone for identifying early signs of AI-induced risks in safety-critical systems [28]. It focuses on detecting deviations from normal behavior that may indicate failures, adversarial manipulation, or unexpected conditions [29]. Classical techniques such as statistical hypothesis testing, clustering, and distance-based metrics are widely used for anomaly identification but often struggle with high-dimensional and dynamic data typical of AI applications [30]. Advanced methods, including autoencoders, generative adversarial networks (GANs), and ensemble learning, enhance detection accuracy by modeling complex patterns in data streams [31]. While these methods improve performance, they are often criticized for their black-box nature, making it difficult for human operators to trust alerts. Explainable AI (XAI) complements anomaly detection by providing interpretable reasoning behind anomalies, such as feature attribution, saliency maps, or counterfactual explanations [32]. For example, in autonomous driving, XAI can highlight which visual features led to misclassification of road signs, while in healthcare, it can clarify which patient parameters triggered an alert. The combination of anomaly detection and XAI strengthens trust, improves human oversight, and supports regulatory compliance in safety-critical systems [33]. By making alerts not only accurate but also interpretable, risk monitoring systems can ensure both timely detection and actionable insights, which are vital for preventing catastrophic failures in real-world operations [34]. 2.4. Hybrid Models for Risk Detection

Risk and fault detection in AI systems has traditionally relied on verification and validation (V&V) techniques, fault tolerance mechanisms, and safety assurance processes [20]. Traditional methods such as model testing, redundancy, and formal verification are effective for deterministic systems but often insufficient for dynamic and probabilistic AI models [21]. Runtime monitoring techniques have been introduced to observe system behavior during operation, enabling detection of deviations from expected outputs [22]. For instance, sensor fusion monitoring in autonomous driving can identify discrepancies between LIDAR and camera data, while in healthcare, patient monitoring systems can flag abnormal vital signs. Fault detection also involves statistical process control, signal analysis, and modelbased reasoning to anticipate system degradation [23]. More recently, AI-driven methods such as deep learning classifiers, Bayesian networks, and reinforcement learning agents have been applied to detect anomalies and risks in real-time environments [24]. However, these methods often lack transparency and generate high false-positive rates, limiting their trustworthiness in safety-critical applications. Furthermore, many approaches are domain-

Hybrid models that combine statistical and AI-based techniques have gained traction as promising solutions for risk detection in safety-critical systems [35]. Statistical methods, such as regression analysis, control charts, and hypothesis testing, are valued for their interpretability and mathematical rigor, offering reliable baseline detection of anomalies [36]. However, they are limited in handling complex, high-dimensional data or adapting to non-linear behaviors common in AI-driven environments. In contrast, AI-based methods, including deep learning, reinforcement learning, and probabilistic graphical models, excel in identifying intricate patterns and adaptive responses but often lack transparency and may overfit [37]. Hybrid frameworks aim to bridge these gaps by integrating

<!-- page 4 -->

the strengths of both approaches. For example, statistical preprocessing can filter noise and highlight candidate anomalies, while AI modules refine detection through pattern recognition and context awareness. In aviation, hybrid approaches are used for predictive maintenance by combining statistical wear analysis with machine learning models trained on sensor data. In autonomous driving, statistical anomaly scoring can be coupled with AI-based perception systems to reduce false positives [38]. These hybrid systems not only enhance accuracy and adaptability but also facilitate explainability by anchoring AI predictions within statistical evidence. Thus, hybrid risk detection models represent a balanced strategy for addressing the dual challenges of accuracy and transparency in mission-critical AI systems. 2.5. Research Gaps in Explainable AI

Hybrid AI

✗ Limite d IREDAI

✓ ✓ Limit ed

✓ ✓ ✓ ✓ ✓

As shown in Table 1, existing frameworks typically focus on one or two aspects of risk management. In contrast, IRED-AI provides a comprehensive architecture that integrates monitoring, explainability, retrieval, and adaptation within a single framework. 3. Research Methodology 3.1. Conceptual Framework for an Intelligent Risk Detection System

The proposed conceptual framework (Fig. 1) for early detection of AI-induced risks in safety-critical systems is designed as a layered and adaptive architecture that integrates monitoring, anomaly detection, explainability, and feedback mechanisms. At its foundation, a data acquisition layer continuously collects system inputs, model outputs, and contextual information from sensors, logs, and control modules. This information feeds into the risk monitoring loop, where statistical thresholds and AIbased anomaly detection methods operate in parallel to identify deviations from expected system behavior. To ensure transparency, an explainability module generates interpretable outputs, highlighting features or conditions responsible for risk alerts. Detected anomalies are then passed to the risk scoring and prioritization module, which assigns severity and likelihood values, enabling operators to focus on the most critical issues. A mitigation and feedback layer provides actionable recommendations, activates fallback mechanisms, and retains new cases in the knowledge base for continuous learning. This closed-loop design ensures that the framework adapts to evolving environments and adversarial threats. Unlike traditional static models, the intelligent framework emphasizes adaptability, low detection latency, and operational interpretability. By combining multiple detection strategies and embedding explainability, the system reduces false alarms, enhances trust, and supports regulatory compliance. The conceptual framework therefore balances technical performance with human oversight, ensuring that AI-driven safety-critical systems remain resilient under uncertainty and unexpected disruptions. ALGORITHM 1. REAL-TIME DATA INTEGRATION AND RISK MONITORING

Despite advancements in anomaly detection, explainability, and hybrid approaches, several research gaps remain in the early detection of AI-induced risks in safety-critical systems. First, existing methods often lack real-time capability, leading to delays in detecting fastevolving risks such as adversarial attacks or sudden system malfunctions. Second, the high false alarm rate of many AI-driven detectors reduces their usability in practice, as operators become desensitized to frequent alerts. Third, there is a shortage of generalizable frameworks that can operate across multiple safety-critical domains, with most solutions being tailored to specific applications such as healthcare or autonomous vehicles. Fourth, the integration of explainability into risk detection is still at an early stage, with limited mechanisms for providing actionable, human-understandable insights. Finally, there is insufficient work on aligning risk detection frameworks with regulatory standards and ethical considerations, which are essential for deployment in real-world systems. Addressing these gaps requires developing intelligent, adaptive frameworks that balance accuracy, interpretability, and scalability while meeting strict operational constraints. Such work would significantly advance the reliability and trustworthiness of AI in safetycritical applications. Table 1. Comparative Analysis of Existing Risk Management Frameworks and the Proposed IRED-AI Framework

Framew

Monitor

AI Detect

XAI Retrie

Adapti

ork

ing

val

ve Learni

ion

1: INPUT: SystemData S, Thresholds T, RiskKnowledgeBase K 2: INITIALIZE RiskScore = 0, AlertFlag = FALSE 3: WHILE system is operational DO 4: Acquire new data D from sensors and logs 5: Preprocess D (filter noise, normalize values) 6: Extract features F from D 7: Compute statistical deviations SD using T 8: Apply anomaly detection model M on F 9: IF SD > T OR M detects anomaly THEN 10: Generate preliminary RiskEvent R 11: Compute RiskScore = Severity(R) + Likelihood(R) 12: Store R in temporary buffer B 13: Apply ExplainabilityModule E on R 14: Present explanation to operator

ng Rulebased

✓ ✗ ✓ ✗ ✗

Statistica l Monitori ng

✓ ✗ ✓ ✗ ✗

Deep Learning

✗ ✓ ✗ ✗ ✗

<!-- page 5 -->

15: IF RiskScore >= CriticalLevel THEN 16: Set AlertFlag = TRUE 17: Trigger MitigationAction A 18: Log R and A in RiskKnowledgeBase K 19: END IF 20: ELSE 21: Continue monitoring 22: END IF 23: END WHILE

Change-Point Detection using Bayesian Online Change Point Detection (BOCPD) to identify sudden distributional shifts associated with data drift or emerging failures.

The AI component operates in parallel and consists of three complementary models:

2

```math
2
ˆ
AE
E
x
x
=
−
 
(3)
```

where high reconstruction error indicates abnormal behavior.

LSTM-based Temporal Prediction Models for sequential sensor streams:

```math
2
ˆ
LSTM
t
t
E
y
y
=
−
 
(4)
```

capturing deviations from expected temporal dynamics.

**Fig. 1. The conceptual framework**

Bayesian Neural Networks (BNN) to estimate predictive uncertainty:

A distinguishing characteristic of IRED-AI is the interaction among its five core modules. Real-time monitoring continuously collects operational evidence, hybrid anomaly detection combines statistical and AIbased indicators to identify abnormal behaviors, explainable AI provides human-interpretable reasoning, similarity-based retrieval contextualizes detected risks through historical knowledge, and adaptive feedback continuously refines detection performance. The integration of these components forms a closed-loop risk intelligence system capable of proactive and selfimproving safety assurance. 3.1.1. Hybrid Statistical–AI Anomaly Detection Module

```math
( )
Var[ (
)]
U x
p y x
=
∣
 
(5)
```

where elevated uncertainty often precedes unsafe system behavior.

The outputs of the statistical and AI detectors are normalized and fused using adaptive confidence weighting:

```math
Hybrid
Stat
AI
s
a
S
w S
w S
=
+
 
(6)
```

subject to

```math
1
s
a
w
w
+
= 
(7)
```

where:

Stat S = aggregated statistical anomaly score,

The Hybrid Statistical–AI Anomaly Detection Module constitutes the core detection engine of IRED-AI. The objective of this module is to combine the interpretability and stability of statistical monitoring with the adaptability and pattern-recognition capabilities of modern AI models.

AI S = aggregated AI anomaly score,

s w and a w are dynamically adjusted according to detector reliability.

Detector reliability is computed from recent precision and false-alarm statistics:

The statistical component continuously evaluates operational variables using three complementary techniques:

i i

```math
(8)
```

R w R = 

Statistical Process Control (SPC) based on control charts (Shewhart, EWMA, and CUSUM) to identify abrupt deviations from expected operating ranges.

j j

where iR denotes the reliability score of detector i.

Z-score and Mahalanobis Distance Analysis to quantify multivariate deviations from historical normal behavior:

The final anomaly decision is generated as:

i i i

```math
−
=
 
(1)
```

x Z  

Hybrid 1, Alert 0, otherwise S    = 

```math
(9)
```



i

```math
1
( )
(
)
(
)
T
M
D
x
x
x


−
=
−

−
 
(2)
```

where τ is an adaptive threshold calibrated using validation data and continuously updated through operator feedback.

where μ and Σ denote the historical mean vector and covariance matrix.

<!-- page 6 -->

This hybrid design enables IRED-AI to detect both simple statistical abnormalities and complex nonlinear behavioral anomalies. Statistical detectors provide transparent evidence and low computational overhead, while AI detectors capture subtle patterns, temporal dependencies, and emerging risks that traditional monitoring techniques may overlook. The fusion mechanism therefore reduces false positives, improves robustness against data drift, and enhances detection accuracy across heterogeneous safety-critical environments. 3.2. Data Collection and Pre-processing

eliminate corrupted observations caused by communication failures or sensor malfunctions. Data quality is continuously evaluated using completeness, consistency, timeliness, and validity metrics. Records failing predefined quality thresholds are quarantined and excluded from downstream risk analysis.

After validation, heterogeneous inputs are transformed into modality-specific feature representations. Numerical telemetry data are normalized using robust scaling, categorical protocol events are encoded through embedding representations, textual user interactions are converted into semantic embeddings, and environmental variables are standardized using domain-specific normalization functions. The resulting feature vectors are subsequently fused using an attention-weighted latefusion strategy, where each modality receives a dynamic importance weight according to its reliability, relevance, and predictive contribution to risk detection. This approach prevents noisy or low-quality data sources from disproportionately influencing the final risk assessment.

Data collection and preprocessing form the foundation of the proposed intelligent framework for early detection of AI-induced risks. Safety-critical systems generate heterogeneous data from sensors, control logs, user interactions, and external environments, each requiring careful integration to ensure quality and consistency. For this study, we leverage ten representative datasets spanning healthcare, autonomous driving, aviation, and industrial control, ensuring broad coverage of domains where AI-induced risks are prominent. The selection criteria included relevance to risk scenarios, data availability, diversity of features, and potential for realtime analysis. Preprocessing involved several steps. First, data cleaning removed incomplete, noisy, or redundant records to reduce the probability of spurious risk signals. Second, normalization and standardization were applied to align heterogeneous feature scales, ensuring comparability across inputs. Third, feature extraction and engineering transformed raw inputs into risk-relevant representations, such as anomaly scores, temporal patterns, and contextual embeddings. Outlier detection techniques were applied during preprocessing to avoid contamination of the training process with corrupted data.

Furthermore, a confidence scoring mechanism is maintained for each data source. Sources exhibiting excessive missing values, communication instability, or abnormal variance receive reduced weighting during feature fusion. Consequently, the framework preserves robustness even when certain sensors or external data streams become unreliable. Through this combination of temporal synchronization, schema harmonization, quality validation, reliability assessment, and adaptive multimodal fusion, IRED-AI ensures that heterogeneous data are integrated into a consistent and trustworthy representation suitable for real-time AI risk monitoring and early warning generation.

For temporal datasets, such as industrial sensor readings and aviation flight logs, window-based segmentation was adopted to capture evolving system behaviors. In contrast, healthcare records were preprocessed using patient-level aggregation with mean ± standard deviation statistics to preserve interpretability. Autonomous driving data underwent multimodal synchronization to align camera, LiDAR, and telemetry signals. Finally, all datasets were split into training, validation, and test subsets using stratified sampling to maintain risk-event distribution balance. This systematic preprocessing ensures that the proposed framework operates on high-quality, risk-relevant data streams. The prepared datasets enable robust benchmarking across domains while supporting the evaluation of generalizability, scalability, and explainability of the risk detection framework. Table 2 presents the ten datasets selected for AI risk detection across healthcare, autonomous driving, aviation, industrial control, and cybersecurity domains. Each dataset is described with its symbol, domain, instances, and features, alongside data source and frequency. The inclusion of statistical measures such as mean ± standard deviation ensures that the raw data is quantitatively characterized.

To address the challenge of heterogeneous data integration, IRED-AI employs a multi-stage data fusion and quality assurance pipeline. First, all incoming data sources—including sensor streams, control protocol logs, user interaction records, and environmental monitoring data—are mapped into a unified schema consisting of timestamp, source identifier, context attributes, operational state variables, and risk-related indicators. Temporal synchronization is achieved using slidingwindow alignment and event-based timestamp normalization, ensuring that observations originating from different sampling frequencies can be analyzed within a common temporal context. Missing values are handled through domain-specific imputation techniques, including interpolation for time-series sensor data, forward filling for operational logs, and model-based estimation for sparse contextual variables.

To ensure data consistency, schema validation rules are applied during ingestion to detect malformed records, incompatible formats, and semantic conflicts among data sources. Duplicate events are removed through hashbased record matching, while anomaly filtering techniques

<!-- page 7 -->

**Table 2. Datasets for AI-Based Risk Detection**

Dataset Symbol Domain Instances Features /

Data Source &

Statistical

Analysis (Mean ± SD) MIMIC-III [39] H1 Healthcare 58,976 ICU records,

Notes

Frequency

PhysioNet,

### HR 85.2 ± 14.3

vitals, labs

hourly

PhysioNet

H2 Healthcare 20,000 ECG signals PhysioNet,

250Hz QRS 0.89 ±

### 0.12 BDD100K [40] A1 Autonomous

### ECG

100,000 Images, video Berkeley DeepDrive, 30fps

ObjCount 12.5

± 3.4 KITTI [41] A2 Autonomous

Driving

7,481 LiDAR +

KITTI Vision,

10Hz Dist 35.7 ± 7.2

Driving

camera

NASA Turbofan [42]

AV1 Aviation 21,000 Engine cycles CMAPSS, per

Temp 482.1 ±

### 35.8 FlightRadar24

cycle

AV2 Aviation 15,000 Flight telemetry

FR24, per min Alt 8,450 ±

## 1200 SWaT [44] I1 Industrial

Logs [43]

51,000 Water treatment

iTrust, per sec Flow 35.6 ± 5.8

Control

WADI [45] I2 Industrial

100,000 Water distribution

iTrust, per sec pH 7.1 ± 0.5

Control

### UNSW-NB15

C1 Cybersecurity 2,540,000 Network

UNSW, per

Bytes 425 ± 210

[46]

traffic

packet

MAAD-Faults

C2 Industrial

50,000 Machine logs Manufacturing AI

Vib 0.015 ±

### 0.006 Table 3. Benchmark Datasets for AI Risk Detection Across Domains

[47]

Sensors

Lab, daily

Symbol Type Features Label Types Risk Relevance Size (GB) H1 Tabular 45 Mortality / anomaly High 12 H2 Time-series 30 Arrhythmia detection High 8 A1 Image/Video 50 Object recognition failures Medium 40 A2 Multi-modal 25 Lane/obstacle misclassification High 15 AV1 Time-series 21 Engine degradation High 2 AV2 Time-series 18 Flight anomalies Medium 3 I1 Sensor 51 Water flow faults High 4 I2 Sensor 40 Water contamination High 6 C1 Network logs 49 Intrusion detection High 25 C2 Sensor 35 Mechanical failures Medium 5 Table 4. Representative Datasets for Intelligent Risk Detection

Symbol Mean Std. Dev. Min Max Missing (%) H1 85.200 14.300 40.000 180.000 2.100 H2 0.890 0.120 0.450 1.150 0.800 A1 12.500 3.400 2.000 22.000 0.500 A2 35.700 7.200 5.000 70.000 1.400 AV1 482.100 35.800 390.000 590.000 0.200 AV2 8,450 1200.000 1,500.000 11,500.000 1.800 I1 35.600 5.800 20.000 55.000 0.900 I2 7.100 0.500 5.500 8.800 1.200 C1 425.000 210.000 12.000 1600.000 0.100 C2 0.0150 0.006 0.005 0.032 0.400

<!-- page 8 -->

This table demonstrates the diversity of data modalities, including tabular records, time-series signals, multimodal driving data, and network logs, ensuring coverage of multiple safety-critical contexts. Table 3 summarizes the dataset characteristics, highlighting type, number of features, label categories, and associated risk relevance. For example, healthcare datasets contain mortality and anomaly labels, while aviation datasets focus on degradation and flight anomalies. The inclusion of dataset size reflects practical considerations for computational feasibility. This table ensures that the proposed framework is evaluated against datasets of varying scale, complexity, and criticality, strengthening its generalizability. Table 4 provides descriptive statistics, offering insight into central tendency, variability, and missing data percentages for each dataset. These values are critical for preprocessing, as they guide normalization strategies and anomaly thresholds. For instance, high variance in flight telemetry data or large missing values in healthcare datasets may significantly impact detection reliability. By presenting minimum and maximum values, the table also highlights potential outliers and operational extremes that must be managed by the risk detection system. Collectively, the three tables provide a holistic overview of the datasets, ensuring transparency in data selection, statistical readiness, and domain coverage for robust framework evaluation.

For autonomous driving datasets, risk labels were assigned to situations involving perception uncertainty, object misclassification, sensor disagreement, localization instability, delayed obstacle recognition, or unsafe driving decisions. Events associated with near-collision scenarios, emergency braking activation, or significant disagreement between sensing modalities were classified as high-risk observations.

For aviation datasets, AI-induced risks were defined as anomalies that could potentially influence predictive maintenance recommendations, flight-state estimation, trajectory prediction, or operational decision support systems. Large prediction residuals, abnormal uncertainty estimates, and deviations from certified operational envelopes were labeled as risk conditions.

For industrial control datasets, risk events corresponded to abnormal process control recommendations, unstable actuator behavior, sensor drift, communication failures, and prediction inconsistencies capable of affecting operational safety or equipment integrity.

For cybersecurity datasets, AI-induced risks included anomalous threat classification behavior, elevated uncertainty during intrusion detection, adversarially manipulated traffic patterns, and situations where model predictions significantly diverged from verified attack classifications.

The selected datasets were chosen to reflect diverse safety-critical scenarios where AI-induced risks carry severe consequences. Healthcare datasets ensure evaluation of patient monitoring and diagnostic reliability. Autonomous driving data addresses perception errors and environmental uncertainties. Aviation datasets capture predictive maintenance and flight anomalies essential for operational safety. Industrial control datasets represent cyber-physical vulnerabilities in critical infrastructure. Cybersecurity and manufacturing sensor data highlight adversarial threats and mechanical failures. By covering multiple domains, data modalities, and risk conditions, the selection ensures that the proposed framework is generalizable, adaptable, and robust, supporting evaluation under realistic and high-stakes conditions. 3.2.1. Dataset Labeling Strategy for AI-Induced Risks

To ensure consistency across domains, a common risk scoring function was applied:

```math
R
U
D
E



=
+
+
 
(10)
```

where: U represents model uncertainty, D represents distributional deviation or data drift, E represents prediction error or decision inconsistency, α,β,γ are weighting coefficients determined through validation.

Samples exceeding a predefined risk threshold were assigned positive AI-induced risk labels. This procedure enabled construction of a unified cross-domain benchmark while preserving domain-specific safety semantics.

To ensure consistent and domain-specific risk identification, the proposed IRED-AI framework employs a unified labeling strategy tailored to the operational characteristics of each application domain. In healthcare systems, AI-induced risks are defined as unsafe diagnoses, high predictive uncertainty, and out-ofdistribution (OOD) patient cases, with labels generated using entropy measures and calibration error analysis. In autonomous driving environments, risks are associated with perception failures and disagreements among heterogeneous sensors, where labels are derived from sensor-fusion inconsistency metrics. For aviation applications, AI-induced risks are identified through abnormal flight prediction behavior, with labeling based on prediction residuals and uncertainty estimates. Within

The benchmark datasets used in this study were not originally annotated with explicit "AI-induced risk" labels. Therefore, a domain-specific weak-supervision labeling strategy was developed to construct consistent risk annotations across heterogeneous safety-critical domains.

For healthcare datasets, AI-induced risks were defined as situations in which model predictions exhibited elevated uncertainty, calibration failure, inconsistent diagnostic recommendations, or significant divergence from clinically validated outcomes. Samples associated with high predictive entropy, out-of-distribution patient characteristics, or medically unsafe recommendations were labeled as risk events.

<!-- page 9 -->

17: y_risk ← weak_label(X_raw, rules_or_sim) 18: emit FeatureRecord{t, Z_embed, A_attr, y_risk} 19: END FOR 20: OUTPUT: FeatureStream F 1) Risk Taxonomy Model The proposed risk taxonomy framework categorizes AI-induced risks in safety-critical systems into data-related, model-related, and operational domains. Data-related risks include bias, noise, drift, and adversarial perturbations that compromise model reliability. Modelrelated risks capture uncertainties such as overfitting, calibration errors, black-box opacity, and adversarial vulnerability that can trigger unsafe outputs. Operational risks emerge during deployment, encompassing hardware failures, sensor degradation, network latency, and cascading faults in cyber-physical integration. Each risk class is further characterized by its severity, likelihood, and detectability, forming a structured matrix for prioritization. The taxonomy also supports cross-domain mapping, allowing risks identified in one domain (e.g., aviation engine degradation) to inform detection strategies in others (e.g., industrial sensor drift). By formalizing these categories, the framework provides a common vocabulary for risk assessment, enabling systematic representation, monitoring, and mitigation. This taxonomy underpins feature modeling, ensuring that the detection system targets diverse and contextually relevant risk factors.

industrial control systems, unsafe control actions and deviations from expected operational processes are treated as risk events, and labels are generated using processdeviation measurements. In cybersecurity settings, risks include misclassified threats, adversarial traffic patterns, and inconsistent threat assessments, with labels assigned through prediction inconsistency analysis. This domainaware labeling methodology enables IRED-AI to establish reliable ground truth across diverse environments while ensuring that detected risks are aligned with practical operational concerns and safety requirements. 3.3. Evaluation Metrics

Risk representation follows a multi-view schema that encodes context, state, and behavioral deviation for safetycritical AI. Each observation is mapped to a tuple ⟨X_ctx, X_sig, X_sem, y_risk⟩. Context features (X_ctx) capture operating mode, environment, and asset metadata (e.g., vehicle speed regime, ICU ward, turbine load). Signal features (X_sig) summarize raw telemetry via temporal statistics (mean, variance, trend), spectral descriptors (bandpower, dominant frequency), and change-point indicators to expose nonstationarity. Semantic features (X_sem) derive from task-level AI outputs (class probabilities, logits, detection confidences) and internal health indicators (entropy, calibration error, OOD scores), enabling alignment between model uncertainty and system risk. To maintain interpretability, we learn lowdimensional risk embeddings using constrained autoencoders or PCA with feature-attribution sidechannels (e.g., SHAP values) that preserve traceability to original inputs. Robustness is improved via winsorization, robust scaling, and adversarially perturbed augmentations that stress detector invariances. For multimodal settings (vision–LiDAR–telemetry), synchronized windows are fused through late fusion (stacked meta-features) and attention-weighted pooling to preserve modality salience. Labels y_risk encode graded severity/likelihood or proxy anomalies from weak supervision (rules, simulators). The final feature vector balances detection power, latency, and explainability, supporting downstream modules for anomaly scoring, early warning generation, and SLA-aware prioritization. ALGORITHM 2. FEATURE EXTRACTION AND RISK EMBEDDING GENERATION

2) Illustrative Risk Representation Model An example risk representation model integrates contextual, statistical, and semantic features into a unified risk embedding vector. For instance, in an autonomous driving scenario, contextual features include road type, weather conditions, and vehicle speed; statistical features capture deviations in LiDAR depth distributions and sudden changes in acceleration profiles; semantic features derive from AI perception models, such as the confidence score of pedestrian detection or the entropy of object classification. These features are normalized, fused through attention-weighted aggregation, and transformed into a compact risk vector that quantifies both likelihood and severity. The model also embeds explainability metadata, linking each vector component back to its contributing feature, thereby enhancing interpretability. This structured representation supports both real-time anomaly detection and historical case retrieval, allowing the framework to not only flag current risks but also learn from past risk patterns. Such representations enable efficient monitoring, adaptive detection, and actionable insights for operators. 3.3.1. Explainability and Interpretable Risk Representation Module

1: INPUT: Stream S, Window w, Step s, Schema Σ, Calibrator C 2: FOR t = 0 TO |S| STEP s DO 3: X_raw ← slice(S, t, t+w) 4: X_ctx ← extract_context(X_raw, Σ.ctx) 5: X_sig.time ← stats(X_raw.signals) // mean, var, trend 6: X_sig.freq ← spectral(X_raw.signals) // bandpower, peak f 7: X_sig.cp ← changepoints(X_raw.signals) 8: P_logits, P_conf ← model_outputs(X_raw.inputs) 9: X_sem.unc ← calibrate(P_conf, C) // ECE, entropy 10: X_sem.ood ← ood_score(X_raw.inputs) // Mahalanobis/energy 11: X_sem.err ← residuals(P_logits, X_raw.labels_opt) 12: Z ← concat(X_ctx, X_sig.time, X_sig.freq, X_sig.cp, X_sem) 13: Z ← robust_scale(winsorize(Z)) 14: if multimodal(X_raw) then Z ← late_fuse(Z, X_raw.modalities) 15: A_attr ← explainability_sidechannel(Z) // SHAP/IG summary 16: Z_embed ← reduce_dim(Z, method=PCA_or_CAE, keep_attrs=A_attr)

The Explainability Module provides transparent reasoning for anomaly detection, risk retrieval, and alert generation. The module consists of three components: interpretable embedding generation, feature attribution analysis, and explanation synthesis.

<!-- page 10 -->

(1) Interpretable Embedding Generation For low-dimensional tabular datasets (d<100), dimensionality reduction is performed using Principal Component Analysis (PCA):

For real-time deployment, TreeSHAP is used for treebased components, while DeepSHAP is applied to neural models. (3) Explanation Synthesis Layer The proposed IRED-AI framework incorporates Explainable Artificial Intelligence (XAI) mechanisms to enhance transparency and user trust in automated risk detection. Specifically, the system utilizes SHAP (SHapley Additive exPlanations) to quantify the contribution of individual features to each prediction. Rather than presenting technical importance scores that may be difficult for operators to interpret, IRED-AI automatically converts these outputs into human-readable explanations. For example, an anomaly alert may be attributed primarily to abnormal sensor temperature, elevated prediction uncertainty, increasing data drift, and network latency issues. The generated explanation may state that the alert was triggered mainly by abnormal sensor temperature (34%), elevated model uncertainty (28%), and increasing data drift (19%), while also referencing similar historical cases that previously resulted in engine degradation events. This explanation mechanism enables users to understand the reasoning behind AI-generated decisions, facilitating more informed responses and faster root-cause analysis. By combining feature attribution with retrieval-based evidence from past cases, IRED-AI improves interpretability, accountability, and operational confidence, addressing one of the key limitations of traditional blackbox AI systems in risk management environments. (4) Retrieval-Aware Explainability When historical cases are retrieved, explanations are augmented with similar incidents:

```math
PCA
k
Z
XW
=
 
(11)
```

where

X denotes the normalized feature matrix,

k W represents the first k principal components.

PCA is selected because each principal component can be traced back to original operational variables through loading vectors.

For high-dimensional multimodal data (d ≥100), IRED-AI employs a Constrained Autoencoder (CAE):

```math
( )
z
f
x

=
 
(12)
```

```math
ˆ
( )
x
g
z

=
 
(13)
```

subject to

```math
rec
1
sparse
2
attr
L
L
L
L


=
+
+
 
(14)
```

where

```math
2
rec
ˆ
L
x
x
=
−
 
(15)
```

```math
sparse
1
L
z
=‖ ‖ 
(16)
```

```math
2
attr
SHAP
latent
L
A
A
=
−
 
(17)
```

The attribution-preservation constraint ensures that latent variables remain aligned with important input features, improving interpretability. (2) SHAP-Based Feature Attribution After anomaly scoring, feature importance is calculated using SHAP (Shapley Additive Explanations).

Sim( , ) n i n i

```math
R
C

= ‖
‖‖
‖ 
(19)
```

### R C R C

n i

The retrieved case provides:

• historical context, • previous mitigation actions, • expected outcomes.

For an anomaly prediction model f(x):

```math
=
=
+
 
(18)
```

n

i i f x  

## 0 1 ( )

This transforms explanations from purely local feature importance into actionable risk intelligence. 3.4. Risk Retrieval and Case Matching Risk retrieval and matching constitute the process of identifying the most relevant historical cases when a new risk signal is detected. The framework maintains a risk knowledge base, where past anomalies, faults, and system failures are represented as structured vectors encoding contextual, statistical, and semantic features. When a new observation arrives, its risk embedding is compared against stored cases using similarity measures such as cosine similarity, Mahalanobis distance, or learned

where

i is the Shapley contribution of feature i,

## 0  is the baseline prediction. SHAP explanations are generated for:

• Autoencoder reconstruction errors. • LSTM prediction residuals. • Bayesian uncertainty estimates. • Final hybrid anomaly score.

<!-- page 11 -->

embeddings from Siamese networks. Retrieval ensures that the system not only identifies anomalies but also contextualizes them by linking to prior occurrences, thereby enhancing interpretability and supporting rootcause analysis. Matching strategies are adaptive, weighting features based on domain relevance—for example, prioritizing telemetry signals in aviation or perception features in autonomous driving. Retrieved cases guide decision-making by offering evidence-based insights into potential outcomes and effective mitigation strategies. This retrieval process reduces uncertainty, facilitates explainable alerts, and accelerates operator trust in safetycritical environments. ALGORITHM 3. RETRIEVAL-GUIDED RISK ADAPTATION 1: INPUT: RiskEvent R, RiskKnowledgeBase K, ContextData X 2: Embedding ← GenerateRiskEmbedding(R) 3: RetrievedCases ← SearchSimilarCases(K, Embedding) 4: RankedCases ← RankBySimilarity(RetrievedCases) 5: TopCases ← SelectTopK(RankedCases) 6: Outcomes ← AnalyzeHistoricalOutcomes(TopCases) 7: Severity ← EstimateSeverity(R, Outcomes, X) 8: Likelihood ← EstimateLikelihood(R, Outcomes, X) 9: RiskScore ← AdjustRiskScore( Severity, Likelihood, Outcomes, X, ModelUncertainty, OperatorFeedbackHistory ) 10: RecommendedActions ← GenerateMitigationActions(R, TopCases) 11: Explanation ← GenerateExplanation(R, TopCases, X) 12: IF RiskScore < T.low THEN 13: AlertLevel ← "INFORMATIONAL" 14: ELSE IF RiskScore ≥ T.low AND RiskScore < T.med THEN 15: AlertLevel ← "CAUTIONARY" 16: ELSE IF RiskScore ≥ T.med AND RiskScore < T.high THEN 17: AlertLevel ← "CRITICAL" 18: ELSE 19: AlertLevel ← "EMERGENCY" 20: END IF 21: IF AlertLevel = "EMERGENCY" THEN 22: Trigger ImmediateMitigation(R) 23: ELSE IF AlertLevel = "CRITICAL" THEN 24: Recommend PreemptiveMitigation(R) 25: ELSE 26: Log Event for Monitoring 27: END IF 28: StoreCurrentEvent(R, RiskScore, AlertLevel) 29: UpdateKnowledgeBase(K, R) 30: NotifyOperator(AlertLevel, Explanation) 31: StoreAlertInAuditLog(R, RiskScore, AlertLevel) 32: OUTPUT: AdaptedRiskScore(RiskScore), AlertLevel, RecommendedActions, Explanation 3.4.1. Retrieval and Adaptation Strategy

scores. Each retrieved case contains information regarding the original anomaly, operational context, mitigation actions, and final outcomes.

The adaptation mechanism utilizes these retrieved cases to refine the initial risk assessment. If highly similar historical cases resulted in severe failures, the system increases the estimated severity of the current event. Conversely, if similar cases were previously classified as false alarms or low-impact events, the risk score may be reduced. Environmental conditions, model uncertainty estimates, and recent operator feedback are also incorporated during adaptation. The final output is an adjusted risk score together with recommended mitigation actions and an explanation describing why the alert was generated. 3.5. Evaluation Metrics

Once risks are retrieved and matched, the system proceeds with adaptation and early warning generation, transforming raw detections into actionable insights. Adaptation involves aligning current risk observations with contextual factors, operational constraints, and previously successful mitigation strategies. For example, a medium-severity anomaly in industrial sensors may be escalated if combined with adverse environmental conditions, while a low-confidence anomaly in healthcare data may be downgraded if vital parameters remain stable. The adaptation module refines severity and likelihood scores by incorporating both real-time context and historical outcomes. Following adaptation, the early warning generator issues alerts at varying escalation levels: informational, cautionary, critical, or emergency. Each alert is accompanied by explanations derived from retrieved cases and feature attributions, ensuring operator trust. Importantly, the system distinguishes between preemptive alerts (early indicators of possible risks) and critical alerts (confirmed imminent failures). This hierarchical warning process balances responsiveness with false alarm minimization, enabling operators to act swiftly while avoiding alert fatigue. Thus, risk adaptation and early warning generation create a bridge between detection and actionable decision-making.

ALGORITHM 4. ADAPTATION LOGIC FOR REAL-TIME ALERTS

1: INPUT: RiskEvent R, RetrievedCase C, ContextData X, Thresholds T 2: Severity ← compute_severity(R, C, X) 3: Likelihood ← compute_likelihood(R, C, X) 4: RiskScore ← weighted_sum(Severity, Likelihood) 5: IF RiskScore < T.low THEN 6: Level ← "INFORMATIONAL" 7: ELSE IF RiskScore ≥ T.low AND RiskScore < T.med THEN 8: Level ← "CAUTIONARY" 9: ELSE IF RiskScore ≥ T.med AND RiskScore < T.high THEN 10: Level ← "CRITICAL" 11: ELSE 12: Level ← "EMERGENCY" 13: END IF 14: Explanation ← generate_explanation(R, C, X) 15: IF Level = "EMERGENCY" THEN 16: Trigger ImmediateMitigation(R) 17: ELSE IF Level = "CRITICAL" THEN 18: Recommend PreemptiveMitigation(R) 19: ELSE 20: Log Event for Monitoring

When a new risk event is detected, IRED-AI generates a risk embedding containing contextual, statistical, and semantic features extracted from the monitoring pipeline. The embedding is compared against historical cases stored in the Risk Knowledge Base using similarity measures such as cosine similarity and learned embedding matching. The system retrieves the Top-K most similar cases and ranks them according to similarity

<!-- page 12 -->

21: END IF 22: Update KnowledgeBase with {R, RiskScore, Level} 23: Notify Operator with {Level, Explanation} 24: Store Alert in AuditLog 25: OUTPUT: Alert(Level, Explanation) 1) Alert Escalation Framework The alert escalation flow defines how detected risks progress through different levels of operator notification and system response. It begins with informational alerts, which document anomalies of low severity, often serving as indicators for monitoring trends. If anomalies persist or severity increases, the system issues cautionary alerts, notifying operators of potential risks without demanding immediate intervention. When likelihood and severity surpass medium thresholds, a critical alert is generated, recommending preemptive mitigation such as switching to redundant modules, adjusting control parameters, or initiating diagnostic checks. In extreme cases, where imminent system failure or safety hazards are predicted, the framework triggers an emergency alert, activating immediate mitigation actions such as emergency braking in autonomous vehicles, shutdown in industrial plants, or fail-safe mechanisms in aviation. Each escalation step incorporates context-aware reasoning and explanations drawn from historical cases to justify the decision. This hierarchical escalation minimizes operator fatigue by filtering noise while ensuring urgent risks are not overlooked. By dynamically adjusting alert levels, the system balances sensitivity and specificity, ensuring timely intervention without overwhelming decision-makers in safety-critical environments. 3.6. Risk Revision and Knowledge Retention Framework

making, thereby improving trust and performance in safety-critical applications. ALGORITHM 5. CONTINUOUS UPDATE AND FEEDBACK LOOP

1: INPUT: RiskEvent R, OperatorFeedback F, KnowledgeBase K 2: IF F = "FALSE POSITIVE" THEN 3: Adjust Thresholds T ← update_thresholds(T, R) 4: Update DetectionModel M ← penalize_false(R) 5: ELSE IF F = "TRUE POSITIVE" THEN 6: Enrich R with {Context, MitigationActions, Outcome} 7: Append R to KnowledgeBase K 8: END IF 9: Periodically Review K 10: FOR each Case Ci in K DO 11: IF age(Ci) > ExpiryLimit THEN 12: Remove Ci from K 13: ELSE IF relevance(Ci) < MinRelevance THEN 14: Archive Ci 15: END IF 16: END FOR 17: Re-train DetectionModel M with updated K 18: Validate performance on ValidationSet V 19: IF performance < AcceptableLevel THEN 20: Trigger ModelRecalibration(M, K) 21: END IF 22: Log Updates {R, F, Adjustments} 23: Notify Operator of KnowledgeBase Changes 24: Sync K across distributed nodes 25: OUTPUT: Updated KnowledgeBase K 4. Implementation of the Model 4.1. System Design and Architecture

The system architecture (Figure 2) of the proposed intelligent framework is designed as a modular, layered structure that balances real-time performance with explainability and adaptability. At its foundation, the data acquisition layer interfaces with diverse sources, including sensors, control logs, telemetry streams, and external environments. The acquired data flows into the preprocessing and feature extraction layer, which standardizes formats, filters noise, and generates structured risk representations. Next, the risk monitoring layer operates in a continuous loop, combining statistical deviation analysis with AI-based anomaly detection to identify early indicators of risks. An integrated retrieval and adaptation module connects detected anomalies with historical cases stored in the risk knowledge base, ensuring context-aware interpretations and evidence-driven mitigation recommendations. Above this, the risk scoring and prioritization module quantifies severity and likelihood, enabling systematic alert escalation. The explainability and operator interface layer provides interpretable visualizations and justifications for detected risks, enhancing operator trust. Finally, the feedback and retention layer closes the loop, integrating operator feedback and revising the knowledge base for future adaptation. The architecture is designed for scalability and interoperability, supporting distributed deployment across healthcare systems, autonomous vehicles, aviation platforms, and industrial plants. Through its modular design, the framework ensures robustness, adaptability, and compliance with domain-specific safety requirements.

Risk revision and knowledge retention are crucial to maintaining the adaptability of the intelligent framework. Risk revision involves validating, refining, and correcting detected anomalies after operator feedback or post-event analysis. For example, if an alert is deemed a false positive, the system adjusts its thresholds or feature weights to prevent repeated misclassifications. Conversely, confirmed risks are enriched with contextual metadata and mitigation outcomes, enhancing case fidelity. This revision process ensures that the framework evolves continuously, reducing bias and error accumulation.

Knowledge retention focuses on systematically updating the risk knowledge base. Newly validated cases are encoded into structured risk representations and indexed for efficient retrieval in future monitoring cycles. Historical cases are periodically reviewed to remove outdated or irrelevant entries, ensuring the knowledge base remains concise and contextually relevant. A feedback loop involving anomaly detection, operator input, and case retention strengthens the long-term resilience of the system. Ultimately, this mechanism allows the framework to learn from past experiences, adapt to emerging risk profiles, and support explainable decision-

<!-- page 13 -->

### 4.1.1. Domain-Specific Risk Profiles and Regulatory Adaptation

according to domain conditions and operator-defined thresholds. If the adjusted risk score surpasses critical thresholds, the workflow triggers early warning generation, escalating alerts across hierarchical levels (informational, cautionary, critical, emergency). Each alert is accompanied by explanations, derived from attribution techniques and past case outcomes, ensuring transparency. Simultaneously, the event and its mitigation actions are logged into the knowledge base. The workflow ends with a feedback loop, where operator responses refine the system, and periodic retraining ensures resilience against emerging risks. This sequential yet adaptive workflow ensures that the framework not only detects anomalies but also contextualizes, adapts, and escalates them into meaningful, actionable insights for operators in safetycritical systems.

Although IRED-AI employs a common architecture across safety-critical domains, domain-specific differences are handled through configurable risk profiles and regulatory policy modules. The core monitoring, anomaly detection, retrieval, explainability, and adaptation components remain unchanged; however, each deployment environment defines its own risk taxonomy, severity thresholds, operational constraints, and compliance requirements.

For example, healthcare deployments prioritize patient safety, diagnostic reliability, and compliance with healthcare regulations. Aviation environments emphasize flight safety, maintenance integrity, and certification requirements. Autonomous driving systems focus on perception reliability, collision avoidance, and real-time decision constraints, while industrial control systems prioritize equipment integrity, process continuity, and operational safety. Cybersecurity deployments emphasize threat detection, resilience, and incident response. These domain-specific requirements are represented through configurable risk profiles that determine which features receive higher priority, how risk scores are interpreted, and when alert escalation should occur.

To support regulatory compliance, IRED-AI incorporates a policy layer that maps detected risks to domain-specific operational rules. Before alerts are issued, the framework evaluates whether the detected event violates predefined safety, operational, or compliance constraints associated with the target domain. Consequently, the same anomaly may receive different severity classifications depending on the deployment context. For instance, a prediction uncertainty level that generates a cautionary alert in industrial monitoring may trigger a critical alert in healthcare or aviation environments where tolerance for failure is substantially lower. This separation between the domain-independent detection engine and domain-specific policy configuration enables IRED-AI to maintain generality while remaining compliant with sector-specific requirements. 4.2. Algorithmic Framework

**Fig. 2. System Architecture 4.3. Integration of AI Modules**

The framework integrates multiple AI modules to achieve high accuracy, adaptability, and interpretability in risk detection. At its core, the anomaly detection module employs ensemble methods that combine autoencoders, Bayesian networks, and recurrent neural networks, enabling robust detection of deviations in both time-series and multimodal data. To address the opacity of these models, an explainable AI (XAI) module provides feature attributions, saliency maps, and counterfactual explanations, ensuring that operators understand why an alert is generated. The retrieval module leverages similarity-based learning with Siamese and metric-learning networks to align new risks with historical cases, offering evidence-driven insights into potential outcomes and mitigations. Complementing this, the adaptation module integrates reinforcement learning strategies to refine alert severity and timing based on dynamic contexts, thereby reducing false positives and enhancing reliability.

The algorithmic workflow orchestrates the dynamic processes underlying the intelligent risk detection framework (Fig. 2.). The workflow begins with data ingestion, where multimodal inputs are synchronized and validated. After preprocessing, the feature extraction pipeline produces enriched vectors containing contextual, statistical, and semantic indicators of potential risks. These features are analyzed in the risk monitoring loop, which applies hybrid statistical-AI techniques for anomaly detection. Detected anomalies are immediately compared against the risk knowledge base through similarity-based retrieval, enabling contextual alignment with historical risk cases. The retrieval results are passed to the adaptation logic, which adjusts severity and likelihood scores

Integration occurs through a modular API layer, enabling seamless data flow and communication between modules. The architecture supports containerization and

<!-- page 14 -->

microservices deployment, allowing scalability across distributed environments such as hospitals, aircraft systems, or industrial IoT networks. Furthermore, the integration emphasizes low-latency execution, with lightweight models optimized for real-time inference. Hence, these modules form a cohesive ecosystem where detection, explanation, retrieval, and adaptation operate synergistically. By combining advanced AI with interpretability and domain-specific adaptation, the integrated framework achieves both technical excellence and operational trustworthiness, meeting the stringent demands of safety-critical applications. 4.3.1. Model Architectures and Training Configuration

prevent overfitting and ensure stable generalization across heterogeneous safety-critical datasets. 4.3.2. Hyperparameter Configuration

To ensure reproducibility and stable performance across heterogeneous safety-critical datasets, the components of IRED-AI were configured using a common set of hyperparameters selected through validation-based tuning. The autoencoder module employed latent representations of moderate dimensionality to balance reconstruction accuracy and interpretability, while training was performed using the Adam optimizer with a learning rate of 0.001. Mini-batch training was adopted with batch sizes between 64 and 128 depending on dataset size, and training proceeded for up to 100 epochs with early stopping activated when validation performance failed to improve for ten consecutive epochs. For temporal anomaly detection, the LSTM models utilized sequence windows ranging from 30 to 50 time steps and incorporated dropout regularization to reduce overfitting. Bayesian Neural Networks used variational inference with multiple posterior samples during prediction to estimate uncertainty while maintaining computational efficiency.

To ensure reproducibility, the AI components within IRED-AI were implemented using standardized architectures tailored to the characteristics of safetycritical data streams. The anomaly detection module combines autoencoder networks, Long Short-Term Memory (LSTM) models, and Bayesian Neural Networks (BNNs). The autoencoder employs a symmetric encoder– decoder structure with progressively compressed latent representations, enabling reconstruction-based anomaly detection by measuring deviations between original and reconstructed inputs. For temporal data such as industrial telemetry, aviation flight logs, and physiological monitoring signals, a two-layer LSTM architecture is utilized to capture sequential dependencies and identify abnormal temporal patterns. To estimate predictive uncertainty, Bayesian Neural Networks are incorporated using variational inference, allowing the framework to quantify confidence levels associated with anomaly predictions. This uncertainty information is subsequently integrated into the overall risk assessment process, improving robustness in environments characterized by noisy, incomplete, or evolving data distributions.

For retrieval operations, the framework employed Top-K similarity search with K=5, which provided an effective balance between retrieval accuracy and computational cost. Similarity thresholds were calibrated on the validation set and dynamically adjusted through operator feedback and periodic recalibration. Risk scoring thresholds were configured to support four escalation levels—informational, cautionary, critical, and emergency—with boundaries determined using historical incident distributions and domain-specific safety requirements. During adaptation, learning-rate parameters governing threshold updates and feedback incorporation were intentionally constrained to prevent excessive sensitivity to isolated events. Hyperparameter tuning was performed using validation datasets from multiple domains, with final values selected according to a balance of accuracy, false-alarm reduction, latency, interpretability, and robustness. This strategy ensured that the framework remained stable and generalizable while avoiding overoptimization for any single dataset or application domain. 4.3.3. Training Procedures

The explainability component is implemented using SHAP-based feature attribution techniques. DeepSHAP is applied to neural-network-based models, while modelspecific variants are employed where appropriate to reduce computational overhead during real-time operation. Explanations are generated for anomaly scores, uncertainty estimates, and final risk assessments, allowing operators to identify the factors most responsible for triggering alerts. For retrieval operations, IRED-AI employs embedding-based similarity matching, where contextual, statistical, and semantic features are transformed into compact risk representations and indexed within the Risk Knowledge Base. Similarity search is performed using approximate nearest-neighbor retrieval to maintain low latency while preserving retrieval accuracy. The adaptive learning component continuously incorporates validated incidents and operator feedback to recalibrate thresholds, update retrieval priorities, and refine detector sensitivity, thereby improving performance over time and reducing recurring false alarms. All models were trained using the Adam optimization algorithm with early stopping and validation-based model selection to

The AI components within IRED-AI were trained using a standardized multi-stage training pipeline designed to ensure robustness, generalizability, and reproducibility across heterogeneous safety-critical datasets. Following preprocessing and feature engineering, each dataset was partitioned into training (70%), validation (15%), and testing (15%) subsets using stratified sampling to preserve the distribution of risk events and normal observations. For temporal datasets, chronological splitting was applied to prevent information leakage between training and evaluation periods.

<!-- page 15 -->

The autoencoder models were first trained in an unsupervised manner using predominantly normal operational samples to learn compact representations of expected system behavior. Reconstruction loss was minimized using the Mean Squared Error (MSE) objective, enabling the detection of anomalies through elevated reconstruction errors during inference. LSTM models were subsequently trained on sequential sensor streams and temporal operational records using backpropagation through time (BPTT). The objective was to minimize prediction errors associated with future observations while capturing temporal dependencies that may indicate emerging risks. Bayesian Neural Networks were trained using variational inference, where posterior parameter distributions were approximated through optimization of the evidence lower bound (ELBO), allowing uncertainty estimates to be incorporated into downstream risk assessment.

ICU records to UNSW-NB15 network traffic) cover heterogeneous data modalities such as tabular vitals, highfrequency ECG signals, LiDAR streams, engine telemetry, and packet-level logs. The statistical descriptors (e.g., HR 85.20 ± 14.30, Alt 8,450 ± 1,200) indicate realistic operational ranges, ensuring that evaluation is grounded in domain-specific variability rather than artificial benchmarks. This wide coverage provides robustness, stress-testing models against diverse, high-stakes conditions. Table 6 presents the domain-wise performance of IRED-AI. Healthcare, aviation, and cybersecurity domains achieve the strongest gains, with accuracy above 95.00% and AUROC values nearing or exceeding 0.950. In particular, aviation demonstrates 95.10% accuracy and 0.960 AUROC with low latency (90 ms), critical for real-time flight anomaly detection. Cybersecurity exhibits the highest robustness (0.960), reflecting IRED-AI’s adaptability in adversarial environments where packet patterns change rapidly. Even in industrial control performance remains above 92.00% across most metrics, underscoring broad generalizability. Importantly, interpretability scores remain high (≥0.87), addressing regulator and operator demands for explainable risk alerts rather than opaque anomaly flags.

To address class imbalance commonly observed in safety-critical datasets, minority risk events were oversampled using balanced mini-batch construction, while weighted loss functions assigned greater importance to rare but high-impact risk cases. During training, model performance was continuously monitored on the validation set using accuracy, AUROC, AUPRC, and false alarm rate. Early stopping was activated whenever validation performance failed to improve over ten consecutive epochs, and the best-performing model checkpoint was retained for deployment. Retrieval embeddings were generated from the final trained feature representations and indexed within the Risk Knowledge Base using approximate nearest-neighbor structures to support low-latency similarity search.

Table 7 contextualizes these results against a spectrum of baselines. Early frameworks like Rule-Based Detection and Statistical Control Charts lag significantly, with accuracies below 80.00% and high false alarm rates (0.190–0.220). Even modern machine learning baselines such as Random Forests, Autoencoders, and Deep Neural Nets plateau around 85–88% accuracy and 0.120–0.140 false alarm rates. The strongest conventional competitor, the ML Baseline (non-adaptive), achieves 92% accuracy and 0.920 recall, but lacks adaptability and interpretability. By contrast, IRED-AI raises performance by several percentage points across all core metrics while simultaneously reducing latency to 95 ms and cutting false alarm rates to 0.070. The combination of high detection accuracy and low false positives is particularly important in safety-critical contexts, where excessive false alarms can overwhelm operators and desensitize them to true risks.

Following initial deployment, IRED-AI supports periodic retraining and recalibration using newly validated incidents and operator feedback collected through the continuous learning loop. Confirmed risk events are incorporated into the training repository, while falsepositive cases contribute to threshold adjustment and detector refinement. Retraining is performed offline at scheduled intervals to maintain operational stability, after which updated models undergo validation before replacing production versions. This training strategy ensures that the framework remains adaptive to evolving operational environments, emerging threats, and distributional shifts while maintaining consistent detection performance and regulatory reliability across safety-critical domains. 5. Experimental Results 5.1. Dataset-Based Performance Evaluation

Table 8 quantifies these differences as relative gains. Accuracy rises by +3.48%, AUROC by +2.17%, and AUPRC by +3.37%. While these may appear modest, in real-world deployments such margins equate to thousands of avoided false negatives or earlier detections. Precision and recall both improve by over 2–3%, balancing the trade-off between catching more true events and avoiding spurious triggers. Latency is reduced by 20.83%, ensuring faster responses in domains such as autonomous driving, where milliseconds determine safety outcomes. False alarm rates decrease by 22.22%, arguably one of the most operationally significant improvements. Beyond raw performance, interpretability shows a dramatic +20% relative gain, enabling transparent decision support rather than black-box outputs. Robustness also improves by +11.76%, highlighting resilience to dataset drift, adversarial manipulation, and noise.

The results across Tables 5–8 collectively demonstrate how IRED-AI outperforms both traditional and modern frameworks in safety-critical domains. Table 5 establishes the foundation by standardizing datasets across healthcare, autonomous driving, aviation, industrial control, and cybersecurity. These datasets (ranging from MIMIC-III

<!-- page 16 -->

**Table 5. Standardized Datasets for AI Risk Evaluation**

Dataset Symbol Domain Instances Features /

MIMIC-III H1 Healthcare 58,976 ICU records, vitals, labs

PhysioNet ECG H2 Healthcare 20,000 ECG signals PhysioNet, 250Hz QRS 0.890 ± 0.120 BDD100K A1 Autonomous Driving

100,000 Images, video Berkeley DeepDrive, 30fps ObjCount 12.500 ± 3.400 KITTI A2 Autonomous Driving

NASA Turbofan AV1 Aviation 21,000 Engine cycles CMAPSS, per cycle Temp 482.100 ± 35.800 FlightRadar24 Logs AV2 Aviation 15,000 Flight telemetry FR24, per min Alt 8,450.000 ± 1,200.000 SWaT I1 Industrial Control 51,000 Water treatment iTrust, per sec Flow 35.600 ± 5.800 WADI I2 Industrial Control 100,000 Water distribution iTrust, per sec pH 7.100 ± 0.500 UNSW-NB15 C1 Cybersecurity 2,540,000 Network traffic UNSW, per packet Bytes 425.000 ± 210.000 MAAD-Faults C2 Industrial Sensors 50,000 Machine logs Manufacturing AI Lab, daily

**Table 6. Enhanced Performance of IRED-AI in Safety-Critical Domains**

Domain ACC

AUROC AUPRC Precision Recall F1score

(%)

Healthcare 94.700 0.950 0.930 0.920 0.960 0.940 95.000 0.070 0.920 0.930

Autonomous Driving 93.500 0.940 0.910 0.900 0.950 0.920 100.000 0.080 0.910 0.920

Aviation 95.100 0.960 0.940 0.930 0.970 0.950 90.000 0.060 0.940 0.950

Industrial Control 92.800 0.920 0.900 0.910 0.940 0.920 110.000 0.090 0.870 0.910

Cybersecurity 95.400 0.970 0.950 0.940 0.960 0.950 85.000 0.050 0.950 0.960

**Table 7. Comparative Analysis of Frameworks**

Framework ACC

AUROC AUPRC Precision Recall F1score

(%)

Rule-Based Detection

Statistical Control Charts

SVM Classifier 83.60 0.800 0.770 0.810 0.820 0.810 210 0.150 0.650 0.650 Random Forest 85.90 0.820 0.790 0.830 0.840 0.830 190 0.140 0.700 0.700 Deep Neural Net (DNN)

Autoencoder (AE)

Bayesian Network

Recurrent Neural Net (RNN)

Hybrid Statistical + AI

ML Baseline (non-adaptive)

IRED-AI (Proposed)

**Table 8. Relative Performance Gain of IRED-AI Against the Strongest Baseline**

Metric Best Baseline Score IRED-AI Score Relative Gain (%) Accuracy (ACC) 92.000 95.200 +3.480 AUROC 0.920 0.940 +2.174 AUPRC 0.890 0.920 +3.371 Precision 0.910 0.930 +2.198 Recall 0.920 0.950 +3.261 F1-score 0.910 0.940 +3.297 Latency (ms) ↓ 120.000 95.000 −20.833 False Alarm Rate ↓ 0.090 0.070 −22.222 Interpretability ↑ 0.750 0.900 +20.000 Robustness ↑ 0.850 0.950 +11.7650

Data Source &

Statistical Analysis

Notes

Frequency

(Mean ± SD)

PhysioNet, hourly HR 85.200 ± 14.300

7,481 LiDAR + camera KITTI Vision, 10Hz Dist 35.700 ± 7.200

Vib 0.015 ± 0.006

Latency

False Alarm

Interpretability

Robustness

(ms) ↓

↑

↑

Rate

↓

Latency

False Alarm Rate ↓

Interpretability

Robustness

(ms) ↓

↑

↑

75.20 0.700 0.650 0.710 0.680 0.690 280 0.220 0.400 0.450

78.40 0.730 0.690 0.720 0.740 0.730 250 0.190 0.550 0.600

87.20 0.840 0.800 0.850 0.830 0.840 170 0.130 0.500 0.700

88.60 0.860 0.830 0.860 0.850 0.850 160 0.120 0.550 0.700

89.10 0.870 0.840 0.870 0.860 0.860 150 0.110 0.700 0.750

90.40 0.890 0.860 0.890 0.880 0.880 140 0.100 0.600 0.850

91.40 0.910 0.880 0.900 0.910 0.910 130 0.090 0.750 0.850

92.00 0.920 0.890 0.910 0.920 0.910 120 0.090 0.750 0.850

95.20 0.940 0.920 0.930 0.950 0.940 95 0.070 0.900 0.950

<!-- page 17 -->

Taken together, these results emphasize that IREDAI does not simply push accuracy upward but balances accuracy, efficiency, trust, and resilience. Its advantages emerge not from incremental statistical tuning, but from architectural design that unifies adaptive detection with interpretability modules. This positions IRED-AI as a viable framework for deployment in high-stakes, regulated environments where both technical precision and human trust are indispensable.

Figures 3 through 5 provide a visual analysis of IREDAI’s performance compared to the best-performing baseline across eight core evaluation metrics. Figure 3 presents a bar chart comparison, clearly showing that IRED-AI consistently achieves higher values in accuracy, AUROC, AUPRC, precision, recall, and F1-score, while simultaneously lowering latency and false alarm rate. This highlights the framework’s dual ability to maximize detection reliability while minimizing operational inefficiencies.

**Fig. 4. Multi-Metric Performance Comparison of IREDAI vs. Best Baseline**

Figure 4 further emphasizes these findings using a radar chart, where the IRED-AI curve extends beyond the baseline across nearly all axes. The chart demonstrates IRED-AI’s balanced improvements, ensuring that no single metric dominates at the expense of others. By simultaneously strengthening interpretability, robustness, and error reduction, the framework achieves holistic risk detection suitable for safety-critical environments.

Finally, Figure 5 illustrates relative gains of IRED-AI over the strongest baseline. Improvements are quantified, including +3.48% in accuracy, +3.37% in AUPRC, and −22.22% in false alarm rates. Importantly, latency is reduced by −20.83%, confirming the framework’s efficiency in real-time contexts. Thus, these figures validate IRED-AI’s superiority, confirming it as a resilient and explainable solution for proactive AI risk detection across diverse domains.

**Fig. 5. Relative Gain Analysis of IRED-AI vs. Strongest Baseline 5.1.1. Statistical Validation**

Table 9 presents the results of paired t-tests conducted to evaluate whether the performance improvements achieved by the proposed IRED-AI framework were statistically significant when compared with the strongest baseline model. The analysis was performed across multiple experimental runs using key evaluation metrics, including Accuracy, AUROC, AUPRC, F1-score, and Latency. The obtained p-values ranged from 0.001 to 0.007, all of which are substantially below the conventional significance threshold of 0.05. These findings indicate that the observed improvements are unlikely to have occurred due to random variation or sampling fluctuations. In particular, the significant gains in predictive performance metrics such as Accuracy, AUROC, AUPRC, and F1-score demonstrate the effectiveness of integrating retrieval mechanisms, explainable AI components, and adaptive learning capabilities within the IRED-AI architecture. Furthermore, the statistically significant reduction in latency confirms that the proposed framework achieves enhanced efficiency without sacrificing detection quality. Overall, the paired t-test results provide strong empirical

**Fig. 3. Evaluation of IRED-AI Across Eight Metrics**

<!-- page 18 -->

evidence supporting the superiority and robustness of IRED-AI over existing approaches, thereby validating the effectiveness of the proposed framework for intelligent and adaptive risk management applications. Table 9. Statistical Significance Analysis of IRED-AI Performance Improvements over the Strongest Baseline

healthcare and aviation showing the strongest increases. AUROC and AUPRC scores also rise, confirming that IRED-AI is better at distinguishing between normal and abnormal conditions. Importantly, precision and recall are both enhanced, resulting in higher F1-scores and reducing the likelihood of missed detections or false positives. Efficiency is also improved, as shown by reductions in latency ranging from 15–25 ms, while false alarm rates drop by more than 20.00%, strengthening system reliability. These results are further illustrated in Figures 6–10. Figure 6 demonstrates clear accuracy gains across domains, validating the framework’s stronger predictive capability. Figure 7 highlights improvements in AUROC and AUPRC, with feature engineering enabling more stable and reliable detection. Figure 8 shows balanced gains in precision, recall, and F1-score, emphasizing the framework’s ability to reduce false alarms without sacrificing sensitivity. Figures 9a and 9b highlight reductions in latency and false alarm rates, proving that efficiency and robustness improve simultaneously. Finally, Figure 10 consolidates these benefits in a relative gain analysis, where reductions in latency and false alarm rates represent the largest improvements, alongside notable enhancements in predictive metrics. Collectively, Table 8 and Figures 6–10 confirm that intelligent risk feature engineering is a key driver of IRED-AI’s performance. It strengthens accuracy, improves robustness, and reduces inefficiencies, enabling the framework to deliver trustworthy and efficient risk detection in real-time, safetycritical contexts.

Metric p-value Accuracy 0.003 AUROC 0.007 AUPRC 0.005 F1-score 0.004 Latency 0.001 5.2. Impact of Intelligent Risk Feature Engineering

This section evaluates the role of intelligent risk feature engineering in enhancing IRED-AI’s performance. It examines how engineered features improve accuracy, efficiency, and robustness across domains, explores risks and mitigation strategies, and presents additional results, supported by comprehensive tables and figures to validate practical and theoretical contributions.

1) Accuracy, Efficiency, and Robustness Evaluation in Multiple Domains

Table 10 presents the quantitative results of feature engineering on accuracy, efficiency, and robustness across five safety-critical domains. The findings reveal consistent gains when intelligent feature engineering is applied. Accuracy improves by 3–5% in every domain, with

**Table 10. Comparison of Model Performance With and Without Feature Engineering**

Domain Model Variant

ACC (%)

AUROC AUPRC Precision Recall F1score

Latency (ms) ↓

False Alarm Rate ↓

Robustness ↑

|  | Without |  | 90.12 | 0.910 | 0.880 | 0.890 | 0.900 | 0.895 | 120 | 0.110 | 0.750 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FE |  |  |  |  |  |  |  |  |  |  |

|  | Without |  | 89.80 | 0.905 | 0.875 | 0.885 | 0.895 | 0.890 | 125 | 0.120 | 0.750 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FE |  |  |  |  |  |  |  |  |  |  |

|  | Without |  | 91.20 | 0.920 | 0.890 | 0.900 | 0.920 | 0.910 | 115 | 0.100 | 0.750 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FE |  |  |  |  |  |  |  |  |  |  |

|  | Without |  | 88.90 | 0.890 | 0.860 | 0.870 | 0.880 | 0.875 | 130 | 0.130 | 0.750 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FE |  |  |  |  |  |  |  |  |  |  |

|  | Without |  | 91.70 | 0.930 | 0.900 | 0.910 | 0.920 | 0.915 | 118 | 0.105 | 0.750 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | FE |  |  |  |  |  |  |  |  |  |  |

<!-- page 19 -->

**Fig. 6. Feature Engineering Impact on Accuracy Across Domains**

**Fig. 9(a). Latency Reduction and False Alarm Mitigation via Feature Engineering**

**Fig. 7. Enhanced Discrimination Power via Feature Engineering**

**Fig. 9(b). False Alarm Mitigation Enhancements Achieved by Feature Engineering**

**Fig. 10. Impact of Intelligent Risk Feature Engineering on Multi-Metric Performance**

2) Risks and Mitigation Strategies Although intelligent risk feature engineering strengthens IRED-AI, challenges remain. Limitations such as domain transferability, adversarial vulnerability, and operator overload can affect deployment. Addressing these risks requires proactive mitigation strategies combining technical solutions, human oversight, and regulatory alignment to ensure safe, reliable, and trustworthy system performance.

**Fig. 8. Feature Engineering Impact on Precision, Recall, and F1-score**

<!-- page 20 -->

**Fig. 11. Risk Landscape Heatmap: Severity vs. Likelihood**

**Fig. 12. Mitigation Strategy Effectiveness in Risk Reduction**

**Table 11. Performance Comparison with and Without Feature Engineering Limitation Impact Severity (0–1)**

Likelihood (0–1)

Performance Degradation (%)

Mitigation Effectiveness (%)

Mitigation Strategy

Domain-Specific Overfitting

0.800 0.700 12.50 85.00 Cross-domain training, domain adaptation Adversarial Vulnerability

0.900 0.650 15.20 82.30 Adversarial training, anomaly scoring Data Drift & Concept Shift

0.750 0.800 10.70 87.40 Online learning, adaptive recalibration High False Positives 0.700 0.750 9.80 84.60 Context-aware fusion, hierarchical alerts Limited Interpretability

0.850 0.600 11.30 88.20 XAI modules (SHAP, saliency, counterfactuals) Scalability Challenges 0.650 0.700 8.90 83.50 Distributed architecture, microservices Latency Constraints 0.780 0.680 12.00 86.70 Lightweight models, hardware accelerators Knowledge Base Saturation

0.600 0.720 7.50 81.90 Relevance scoring, case pruning Regulatory NonCompliance

0.950 0.550 13.80 90.00 GDPR/HIPAA alignment, safety standards Human-Machine Misalignment

0.820 0.650 11.60 85.80 Human-in-the-loop, adaptive visualization Table 12 Evaluation of Model Robustness Under Diverse Conditions

Condition Accuracy (%) AUROC Latency (ms) ↓ False Alarm Rate ↓ Robustness ↑ Balanced Dataset 95.20 0.940 95 0.070 0.950 Imbalanced Dataset 92.60 0.910 100 0.090 0.850 Adversarial Perturbations 91.80 0.905 105 0.095 0.750 Real-Time Streaming 94.10 0.930 90 0.075 0.950 Cross-Domain Transfer 93.70 0.925 98 0.085 0.850

<!-- page 21 -->

Table 11 quantifies the limitations, impacts, and mitigation strategies associated with intelligent risk feature engineering in IRED-AI. Results demonstrate that several risks pose substantial challenges. Regulatory noncompliance recorded the highest severity (0.950) and notable performance degradation (13.80%), while adversarial vulnerability followed closely with high severity (0.900) and degradation of 15.20%. Data drift and high false positives presented frequent risks, with likelihood scores of 0.800 and 0.750 respectively, highlighting their persistent operational impact. Scalability and knowledge base saturation were less severe but still introduced measurable degradation of 8.90% and 7.50%. Despite these challenges, mitigation strategies proved effective, achieving 81.90–90.00% reduction in impact across all categories. Figure 11 provides a heatmap of severity and likelihood, making it clear that regulatory non-compliance, adversarial vulnerability, and data drift cluster in the highrisk zone, requiring priority intervention. Risks such as scalability and knowledge base saturation appear less severe yet remain non-negligible for long-term stability. Figure 12 depicts mitigation effectiveness using a radar chart. The chart demonstrates that regulatory alignment and explainability strategies yield the greatest gains (≈ 90%), while all other mitigation strategies achieve consistently high effectiveness above 80%, underscoring the resilience of IRED-AI against diverse risks. Additional Experimental Results

when exposed to imbalanced data, adversarial risks, or cross-domain deployment challenges.

**Fig. 13. Accuracy and AUROC Across Varying Conditions**

**Fig. 14. Latency Comparison Across Operational Modes**

Table 12 summarizes IRED-AI’s performance under varying operational conditions, including balanced datasets, imbalanced distributions, adversarial perturbations, realtime streaming, and cross-domain transfer. The results demonstrate that IRED-AI consistently maintains high accuracy and AUROC, with values above 91.800% and 0.905 even under the most challenging adversarial scenarios. Balanced datasets yield the strongest performance, with accuracy at 95.200% and AUROC at 0.940, while imbalanced and adversarial conditions show moderate degradation, reflecting expected challenges in risk-sensitive contexts. Latency remains below 105 ms across all settings, with real-time streaming achieving the fastest response at 90 ms. False alarm rates are consistently low, ranging from 0.070 to 0.095, ensuring trustworthiness in diverse environments.

Figure 13 illustrates the impact of dataset conditions on accuracy and AUROC. Although performance dips in adversarial and imbalanced cases, the margins remain small, confirming IRED-AI’s resilience. Figure 14 compares latency across conditions, showing that streaming enhances efficiency, whereas adversarial manipulation introduces additional processing delays. Figure 15 integrates all metrics into a radar chart, visualizing IRED-AI’s balanced strength. The framework demonstrates robustness above 0.70 in all scenarios, with consistent advantages in accuracy, interpretability, and error reduction. Collectively, these results confirm that IRED-AI adapts effectively across domains and operational contexts, sustaining accuracy, minimizing false alarms, and preserving efficiency even

**Fig. 15. Multi-Metric Robustness Across Experimental Conditions 5.3. Effectiveness of AI-Accelerated Risk Retrieval**

1) Effectiveness of Intelligent Similarity Detection The effectiveness of IRED-AI’s intelligent similarity detection is demonstrated through retrieval accuracy, latency, and error analysis. Figure 16 presents a comparative analysis of retrieval accuracy across three ranking levels: Top-1, Top-3, and Top-5. IRED-AI achieves the highest accuracy, with Top-1 reaching

<!-- page 22 -->

92.40%, significantly surpassing cosine similarity (78.00%), Euclidean distance (75.50%), and Mahalanobis distance (80.2%). The margin widens further at Top-3 and Top-5 levels, where IRED-AI achieves 95.10% and 97.20% respectively. This consistency illustrates the model’s ability to retrieve relevant cases across varying degrees of tolerance, demonstrating superior effectiveness in matching complex patterns. Figure 17 analyzes latency under increasing dataset sizes ranging from 10,000 to 250,000 cases. Traditional baselines show steep increases in latency, with Mahalanobis exceeding 1,100 ms at the largest dataset size, while cosine and Euclidean retrieval also surpass 900 ms. By contrast, IRED-AI maintains significantly lower latency, registering 550 ms at 250,000 cases. This scalability advantage confirms that the framework can be deployed in real-time risk monitoring environments without compromising responsiveness. Figure 18 provides further insight through a confusion matrix of retrieval results. IRED-AI shows a dominant proportion of correct matches (920) compared to incorrect (80), outperforming traditional methods that frequently misclassify similar but non-critical cases. The reduced mismatch rate directly contributes to higher trustworthiness and actionable insights for operators. Collectively, these results confirm that IRED-AI’s similarity detection is both accurate and efficient, achieving superior retrieval precision while maintaining low latency and reducing errors, making it suitable for safety-critical risk retrieval applications.

**Fig. 18. Confusion Matrix of Retrieval Accuracy**

Moreover, Table 13 evaluates retrieval quality using ranking-based metrics. The proposed IRED-AI framework consistently outperforms traditional similarity methods across Precision@K, Recall@K, MRR, and nDCG. At Precision@1, IRED-AI achieves 0.924, exceeding cosine (0.780) and Mahalanobis (0.802). Similar improvements are observed at higher ranks, with Precision@5 reaching 0.972 and Recall@5 at 0.865. MRR (0.935) and nDCG (0.948) confirm that IRED-AI produces highly ranked, relevant matches with minimal ranking errors. These results highlight the framework’s ability to retrieve not only accurate but also well-ranked cases, ensuring efficiency and reliability in safety-critical risk retrieval tasks.

2) Retrieval Architectures Table 14 compares a range of retrieval architectures, evaluating accuracy, latency, scalability, interpretability, and robustness. Traditional approaches such as flat indexing and KD-trees provide moderate accuracy (≈ 88–89%) but suffer from high latency (620–950 ms) and limited scalability, restricting their suitability for real-time risk detection. Locality Sensitive Hashing (LSH) and inverted indexes deliver strong scalability scores (0.850– 0.900) and reduced latency (350–400 ms), but their interpretability values remain low (≤0.400), limiting their transparency in safety-critical applications.

**Fig. 16. Comparison of Retrieval Accuracy: IRED-AI vs. Traditional Similarity Methods**

More advanced methods demonstrate improved balance. Approximate Nearest Neighbor (ANN) retrieval achieves accuracy of 91.000% and better robustness (0.700), while graph-based retrieval raises accuracy to 92.300% and robustness to 0.780. Neural embedding retrieval further strengthens accuracy (93.100%) and interpretability (0.700), offering enhanced semantic understanding. Hybrid statistical–AI models improve interpretability to 0.750 and robustness to 0.820, reflecting their adaptability across domains. Reinforcement learning–based retrieval yields accuracy of 93.800%, robustness of 0.850, and interpretability of 0.800, highlighting its adaptive potential.

**Fig. 17. Efficiency and Scalability of IRED-AI in Retrieval Latency**

<!-- page 23 -->

**Table 13. Retrieval Quality Metrics for Similarity Detection**

Method Precision@1 Precision@3 Precision@5 Recall@3 Recall@5 MRR nDCG Cosine Similarity 0.780 0.850 0.887 0.690 0.720 0.792 0.805 Euclidean Distance 0.755 0.831 0.875 0.672 0.710 0.781 0.796 Mahalanobis Distance 0.802 0.876 0.900 0.710 0.735 0.812 0.823 IRED-AI (Proposed) 0.924 0.951 0.972 0.830 0.865 0.935 0.948 Table 14. Performance Evaluation of Retrieval Architectures

Architecture Core Approach Accuracy (%)

Robustness (0–1) Flat Index (Brute Force) Linear search with distance metrics

Latency (ms) ↓

Scalability (0–1)

Interpretability (0–1)

88.20 95 0.400 0.600 0.550

KD-Tree Partitioned space search 89.50 620 0.600 0.600 0.600 Locality Sensitive Hashing Hash-based nearest neighbor 87.90 400 0.850 0.400 0.580 Inverted Index Sparse vector retrieval 86.70 350 0.900 0.350 0.500 ANN (Approx. NN) Vector quantization & pruning 91.00 300 0.880 0.450 0.700 Graph-Based Retrieval Proximity graph navigation 92.30 280 0.870 0.600 0.780 Neural Embedding Retrieval

Deep learning semantic embeddings

93.10 240 0.900 0.700 0.800

Hybrid Statistical + AI Combined rule/statistical + ML 92.60 210 0.750 0.750 0.820 RL-Based Retrieval Policy-driven adaptive retrieval 93.80 190 0.880 0.800 0.850 IRED-AI (Proposed) Similarity learning + XAI + adaptation

95.20 150 0.950 0.900 0.920

**Table 15. Efficiency Evaluation of Retrieval Architectures**

Architecture Memory Usage (MB) ↓

Overall Efficiency (0–1) ↑ Flat Index (Brute Force)

Training Cost (GPU hours) ↓

Energy Efficiency (ops/W) ↑

Deployment Complexity (0–1) ↓

420 0.000 0.450 0.200 0.500

KD-Tree 350 1.200 0.520 0.400 0.550 Locality Sensitive Hashing

280 2.500 0.700 0.450 0.650

Inverted Index 260 1.000 0.680 0.300 0.620 ANN (Approx. NN) 500 5.000 0.600 0.600 0.580 Graph-Based Retrieval

600 6.500 0.570 0.650 0.560

Neural Embedding Retrieval

800 10.000 0.620 0.700 0.600

Hybrid Statistical + AI

550 4.200 0.650 0.500 0.670

RL-Based Retrieval 700 8.000 0.640 0.750 0.620 IRED-AI (Proposed)

480 5.800 0.780 0.400 0.820

**Table 16. Evaluation of Retrieval Architectures: Reliability and Adaptability**

Overall Reliability (0–1) ↑ Flat Index (Brute Force) 0.550 0.400 0.350 0.500 0.450 KD-Tree 0.600 0.420 0.380 0.520 0.480 Locality Sensitive Hashing 0.580 0.500 0.420 0.540 0.510 Inverted Index 0.520 0.480 0.390 0.530 0.480 ANN (Approx. NN) 0.700 0.620 0.550 0.680 0.640 Graph-Based Retrieval 0.720 0.640 0.600 0.710 0.670 Neural Embedding Retrieval 0.750 0.680 0.650 0.740 0.710 Hybrid Statistical + AI 0.780 0.700 0.680 0.760 0.730 RL-Based Retrieval 0.800 0.750 0.720 0.780 0.760 IRED-AI (Proposed) 0.880 0.820 0.780 0.850 0.830

Architecture Fault Tolerance (0–1) ↑

Adaptability to Drift (0–1) ↑

Adversarial Resilience (0–1) ↑

Consistency Across Domains (0–1) ↑

The proposed IRED-AI architecture surpasses all baselines with accuracy of 95.200%, lowest latency at 150 ms, scalability of 0.950, interpretability of 0.900, and robustness of 0.920. These results confirm IRED-AI’s superiority in combining precision, efficiency, and

transparency, making it the most effective architecture for intelligent risk retrieval in safety-critical environments.

Tables 15 and 16 provide a comprehensive comparison of retrieval architectures, focusing on both performance and efficiency trade-offs. Traditional

<!-- page 24 -->

methods such as brute force and KD-trees exhibit moderate accuracy (≈88–89%) but incur high latency (620 – 950 ms) and limited scalability, making them impractical for large-scale, real-time risk detection. Hashbased and inverted index approaches improve efficiency and memory usage but sacrifice interpretability and robustness, which are critical in safety-critical applications. Neural and graph-based retrieval architectures achieve higher accuracy (92–93%) yet require substantial memory (600–800 MB) and training costs, creating deployment challenges. Hybrid statistical–AI and RL-based retrieval strike a better balance, with improved robustness and interpretability but still limited by energy efficiency. In contrast, the proposed IRED-AI demonstrates the highest accuracy (95.200%), lowest latency (150 ms), strong scalability (0.950), and high interpretability (0.900), while maintaining efficient resource use (480 MB memory, 0.780 ops/W). This combination establishes IRED-AI as the most effective and practical solution.

optimizes system performance, making it both scalable and resource-efficient. Such improvements are essential for safety-critical systems where rapid, reliable retrieval under heavy loads is required.

**Fig. 19. Indexing Time Comparison Across Dataset Sizes**

Lastly, Table XIV evaluates retrieval architectures on reliability and adaptability factors, including fault tolerance, resilience to adversarial inputs, adaptability to data drift, and consistency across domains. Traditional methods such as brute force, KD-tree, and inverted index score below 0.50 overall, reflecting their vulnerability in dynamic environments. Advanced methods like ANN, graph-based, and neural embeddings achieve moderate improvements, with overall reliability between 0.64 and 0.71. Hybrid and RL-based retrievals further strengthen adaptability, reaching 0.73 and 0.76 respectively. The proposed IREDAI achieves the highest reliability score (0.830), demonstrating superior adaptability to drift, adversarial resilience, and cross-domain consistency.

**Fig. 20.**

3) Indexing and Optimization Indexing and optimization play a critical role in ensuring that retrieval systems can scale effectively while maintaining speed and accuracy. Figure 19 compares indexing time across datasets of increasing size. Traditional approaches such as KD-Tree, LSH, and ANN show progressively higher costs as data scales, with indexing times exceeding 800–1100 ms at 250,000 cases. In contrast, IRED-AI achieves substantially lower times, completing indexing at just 500 ms, underscoring its efficiency in handling large datasets. Figure 20 highlights query throughput, measured in queries per second. While KD-Tree and LSH performance deteriorates significantly at scale, IRED-AI consistently maintains the highest throughput, achieving 900 queries per second at 250,000 cases compared to 250 for KD-Tree. This advantage demonstrates IRED-AI’s superior scalability and capacity to support real-time applications. Figure 21 presents a radar chart capturing multiple optimization metrics, including indexing time, query latency, memory usage, scalability, and accuracy. IRED-AI displays balanced superiority across all categories, scoring higher in efficiency without compromising robustness or interpretability. Together, these results confirm that IRED-AI not only enhances retrieval accuracy but also

**Fig. 21. Query Throughput Analysis Across Dataset Scales**

**Figure 21. Radar chart illustrates optimization tradeoffs. IRED-AI demonstrates balanced superiority in indexing time, query latency, memory efficiency, scalability, confirming its effectiveness as the most optimized retrieval architecture for safety-critical environments.**

<!-- page 25 -->

4) Evaluation and Service-Level Agreements (SLAs) Table 17 presents evaluation metrics aligned with SLA requirements across retrieval architectures. KD-Tree and LSH struggle to meet latency and accuracy targets, with accuracy below 90% and latency exceeding 400–600 ms, resulting in partial SLA compliance of 60–65%. ANN improves performance, achieving 91.000% accuracy and 300 ms latency, but still falls short of full compliance. RLbased retrieval further enhances results, delivering 93.800% accuracy and 190 ms latency with 90% SLA compliance. In contrast, the proposed IRED-AI exceeds all targets, achieving 95.200% accuracy, 150 ms latency, and the highest throughput (1500 q/s), alongside superior interpretability (0.900) and robustness (0.920). Its overall SLA compliance reaches 98%, making it the most reliable architecture.

significant. For example, accuracy showed consistent improvements with a mean of 95.200% ± 1.200, outperforming KD-Tree (p = 0.004), LSH (p = 0.003), and even strong baselines such as ANN (p = 0.018) and RL-based retrieval (p = 0.041). Latency analysis using ANOVA revealed that IRED-AI’s average 150 ms response was significantly faster, while Welch’s t-test for throughput validated its superior scalability with 1500 queries per second ± 45. Similarly, Chi-square tests for false alarms confirmed IRED-AI’s lowest error rate (7.200% ± 0.800). Figure 22, the radar chart, visualizes normalized performance across all metrics. After adjusting inverse measures such as latency and false alarms, IRED-AI demonstrates balanced superiority, consistently expanding its coverage across all axes relative to baseline averages. This balanced dominance highlights that improvements are holistic rather than metric-specific, reinforcing IREDAI’s adaptability to diverse operational demands. Figure 23, the heatmap of p-values, further confirms statistical robustness. All cells remain under the 0.050 threshold, with the strongest significance observed in latency (p = 0.001–0.030) and robustness (p = 0.002–0.027). The dense concentration of low p-values indicates consistent and replicable improvements across multiple baselines. Collectively, the integration of statistical tests, radar-based visualization, and p-value heatmaps substantiates that IRED-AI significantly outperforms traditional and advanced retrieval models in accuracy, speed, reliability, and interpretability. These results validate the framework’s readiness for deployment in safety-critical environments where statistical reliability is as important as raw performance.

Table 18 analyzes SLA violations across key dimensions. KD-Tree and LSH record high violation rates, with 40–65% of queries breaching latency or accuracy requirements. ANN significantly reduces violations to 19%, while RL-based retrieval lowers the rate to 7%. IRED-AI achieves near-perfect compliance, with only 1% overall violations, including minimal breaches in latency and robustness.

Therefore, these results confirm that IRED-AI not only meets but consistently exceeds SLA expectations, offering the highest reliability, efficiency, and compliance for deployment in safety-critical environments.

2) Effectiveness Across Scenarios The performance of IRED-AI was further evaluated across five safety-critical scenarios: healthcare, autonomous driving, aviation, industrial control, and cybersecurity. These environments represent diverse operational constraints, requiring both adaptability and robustness. Figure 24 provides a radar comparison of composite performance scores, normalized across multiple metrics. IRED-AI consistently outperforms ANN and RL-based retrieval in all scenarios, showing particularly strong advantages in healthcare and cybersecurity, where accurate detection and low false alarms are paramount. This balanced superiority confirms that the framework generalizes effectively, without sacrificing performance in domain-specific contexts. Figure 25 presents histogram distributions of accuracy across scenarios. While ANN and RL-based retrieval show broader spreads and occasional dips below 92%, IREDAI achieves higher mean accuracy with reduced variance, clustering around 95%. This demonstrates not only superior accuracy but also greater stability, which is critical in mission-critical environments where reliability cannot fluctuate with domain changes. Figure 26 employs a GAM-like heatmap to visualize IRED-AI’s performance as a function of scenario type and stress factor.

**Fig. 22. Normalized Comparison of IRED-AI vs. Baseline Across Six Metrics 5.4. Statistical Analysis**

1) Extended Performance Statistical Analysis The extended statistical analysis provides a rigorous evaluation of IRED-AI’s improvements over established retrieval architectures. Table 19 presents results of multiple hypothesis tests conducted across six key performance dimensions. In each case, the p-values were well below the α = 0.05 threshold, confirming that performance gains are not coincidental but statistically

<!-- page 26 -->

**Table 17. Evaluation Metrics and SLA Compliance**

Metric / SLA Requirement SLA Target KD-Tree LSH ANN RL-Based IRED-AI (Proposed) Accuracy (%) ≥ 92.00 89.50 87.90 91.00 93.80 95.20 Latency (ms) ↓ ≤ 200 620.00 400.00 300.00 190.00 150.00 Query Throughput (q/s) ↑ ≥ 800 600.00 850.00 1000.00 1200.00 1500.00 False Alarm Rate (%) ↓ ≤ 10.0 12.50 11.20 9.50 8.700 7.20 Robustness (0–1) ↑ ≥ 0.75 0.600 0.580 0.700 0.850 0.920 Interpretability (0–1) ↑ ≥ 0.70 0.600 0.400 0.450 0.800 0.900 SLA Compliance (%) ↑ 100.00 60.00 65.00 80.00 90.00 98.00 Table 18. Comparison of SLA Compliance Across Retrieval Architectures

Architecture Latency Violations (%)

Accuracy Violations (%)

Throughput Violations (%) ↓

Robustness Violations (%) ↓

Overall SLA Violations (%) ↓

↓

↓

KD-Tree 65.00 40.00 25.00 30.00 40.00 LSH 40.00 45.00 15.00 35.00 34.00 ANN 25.00 20.00 10.00 20.00 19.00 RL-Based

12.00 5.00 5.00 8.00 7.00

Retrieval

IRED-AI (Proposed)

### 2.00 1.00 0.00 1.00 1.00

**Table 19. Comprehensive Evaluation of Metrics and SLA Compliance**

Metric Test Applied

KD-Tree (p-value)

LSH (p-

ANN (p-

RL-Based

IRED-AI Mean ± SD

Significance

```math
(α=0.05) 
Accuracy (%) 
Paired t-test 
0.004 
0.003 
0.018 
0.041 
95.20 ± 1.20 
Significant 
Latency (ms) ↓ 
ANOVA (F-
```

value)

value)

(p-value)

### 0.001 0.002 0.009 0.030 150.00 ± 12.00 Significant

test)

Query Throughput (q/s)

Welch’s t-test 0.005 0.004 0.021 0.038 1500.00 ± 45.00 Significant

↑

False Alarm Rate

Chi-square

### 0.006 0.007 0.025 0.042 7.200 ± 0.800 Significant

(%) ↓

test

Robustness (0–1)

Kruskal– Wallis test

### 0.002 0.003 0.014 0.027 0.920 ± 0.020 Significant

↑

Interpretability (0–

1) ↑ Mann– Whitney U-

### 0.004 0.006 0.020 0.035 0.900 ± 0.030 Significant

test

**Fig. 23. Statistical Significance of Performance Differences Across Metrics**

<!-- page 27 -->

**Fig. 24. Composite Scenario Scores Across Domains**

**Fig. 27. Correlation–Standard Deviation Comparison of Methods 6. Discussion**

The evaluation of IRED-AI across multiple benchmarks confirms its superiority as a scalable, accurate, and interpretable framework for AI-induced risk detection in safety-critical domains. 6.1. AIImpact of Intelligent Enhancements

Intelligent enhancements embedded in IRED-AI (advanced risk feature engineering, optimized retrieval architectures, and integrated explainability) directly contribute to its balanced performance [48]. Feature engineering improves predictive power and efficiency across healthcare, aviation, and cybersecurity, reducing false alarms while maintaining sensitivity [49]. Retrieval enhancements, supported by indexing optimization and hybrid statistical–AI mechanisms, demonstrate that scalability and latency can be addressed simultaneously without sacrificing interpretability [50]. The integration of explainability modules ensures that improved performance is not achieved at the expense of transparency, a critical aspect for real-world adoption in safety-critical environments [51]. Collectively, these enhancements reinforce each other, producing consistent accuracy improvements above 95%, reductions in false alarm rates exceeding 20%, and robust resilience under adversarial and imbalanced conditions. The results highlight that IRED-AI’s gains are not marginal but systemic, reflecting a holistic design philosophy that integrates detection reliability, operational efficiency, and transparency into a single unified framework [52]. 6.1.1. Conceptual Novelty and Adaptive Risk Intelligence

**Fig. 25. Accuracy Distributions Across Scenarios**

**Fig. 26. Surface Visualization of Scenario-Stress Interactions**

The conceptual novelty of IRED-AI lies in its ability to unify multiple risk management capabilities within a single adaptive architecture. Existing approaches typically

<!-- page 28 -->

focus on isolated functions such as anomaly detection, statistical monitoring, or explainable decision support. In contrast, IRED-AI integrates real-time monitoring, hybrid statistical–AI anomaly detection, explainable reasoning, similarity-based risk retrieval, adaptive alert generation, and continuous knowledge retention into a cohesive operational framework. This integration enables the framework to move beyond passive detection by supporting proactive risk intelligence, where emerging threats are identified, contextualized, explained, and continuously refined through feedback-driven learning. As a result, the framework addresses several persistent challenges in safety-critical systems, including high false alarm rates, limited transparency, and insufficient adaptability to dynamic operating conditions.

essential for future refinement and broader deployment in heterogeneous operational environments.

6.3. Application Potential in Safety-Critical Systems The demonstrated robustness, efficiency, and transparency of IRED-AI highlight its significant application potential in safety-critical systems [58]. In healthcare, its high recall ensures sensitivity to lifethreatening anomalies, while reduced false alarm rates mitigate clinician fatigue. In aviation and autonomous driving, latency reductions and robust retrieval allow realtime decision support without compromising reliability. Industrial control systems benefit from interpretability, enabling operators to understand why anomalies are flagged and facilitating corrective action [59]. Cybersecurity applications leverage IRED-AI’s ability to handle adversarial conditions, ensuring resilience against evolving threats while preserving low false positive rates [60]. Importantly, compliance with SLA requirements across latency, throughput, and interpretability makes the framework ready for integration into operational pipelines where downtime and errors have significant societal costs [61]. The adaptability demonstrated in cross-domain scenarios further underscores its generalizability, establishing IRED-AI as a versatile solution capable of addressing varied challenges across multiple missioncritical sectors [62].

A particularly important contribution is the closedloop design supported by the knowledge retention mechanism. Unlike static risk detection systems that operate using fixed rules or periodically retrained models, IRED-AI continuously incorporates operator feedback, validated incidents, and mitigation outcomes into its risk knowledge base. This process enables ongoing refinement of detection thresholds, retrieval accuracy, and adaptation strategies, allowing the framework to evolve alongside changing environments, data distributions, and threat landscapes. By combining real-time monitoring with continuous learning and explainable decision support, IRED-AI establishes a foundation for adaptive and trustworthy AI safety management. This capability is especially valuable in safety-critical domains where emerging risks, concept drift, and operational uncertainties require detection systems that can learn from experience while maintaining transparency and accountability.

6.4. Role of Explainable AI and Graph Neural Networks in Risk Detection and Deployment Explainable AI (XAI) plays a pivotal role in bridging the gap between high-performance detection and operational trust [63]. By incorporating interpretability modules, IRED-AI ensures that users can validate decisions, understand root causes, and comply with regulatory standards in sensitive domains such as healthcare and aviation [64]. Graph Neural Networks (GNNs) further extend this capability by modeling complex dependencies and interactions among system components, enabling contextualized risk detection that surpasses traditional feature-based approaches [65]. When combined, XAI and GNNs support multi-level explanations, from local feature attribution to global system insights, enhancing transparency without compromising accuracy [66]. This synergy empowers operators to act confidently on alerts, strengthens resilience against adversarial manipulation, and facilitates real-world deployment by aligning technical outputs with human decision-making processes [67]. As safety-critical systems increasingly demand both predictive strength and interpretability, the integration of XAI and GNNs within IRED-AI ensures scalability, compliance, and long-term trustworthiness in operational environments [68].

6.2. Trade-offs and Limitations Despite its strong performance, IRED-AI presents trade-offs and limitations that warrant attention. Intelligent feature engineering enhances accuracy but increases model complexity, requiring careful design to avoid overfitting and domain over-dependence [53]. While latency is significantly reduced compared to baselines, optimization overhead introduces higher computational costs during training and indexing phases [54]. Crossdomain transfer, though promising, reveals moderate degradation under adversarial and imbalanced conditions, highlighting the challenge of ensuring universal robustness [55]. Additionally, while explainability modules improve transparency, their integration adds computational layers that could marginally affect throughput in resourceconstrained systems. Risks such as regulatory noncompliance, adversarial vulnerability, and data drift remain persistent, even with effective mitigation strategies [56]. These trade-offs reflect the practical reality that achieving state-of-the-art performance requires balancing accuracy, interpretability, and efficiency, with no single metric dominating [57]. Addressing these limitations will be

<!-- page 29 -->

### 6.5. Limitations of the Proposed Framework

detection models without sharing sensitive data, thereby preserving privacy while benefiting from distributed knowledge. At the same time, digital twins can provide virtual representations of physical systems, allowing risk scenarios, system degradations, and failure conditions to be simulated before they occur in operational environments. The combination of federated intelligence and digital twin simulation would enable proactive risk assessment, continuous model validation, and safer deployment of AI-driven systems under evolving operational conditions.

Despite the promising performance achieved by IRED-AI across multiple safety-critical domains, several limitations should be acknowledged. First, the framework relies heavily on the availability and quality of historical risk cases stored within the knowledge base. In environments where limited prior incidents are available, the effectiveness of similarity-based retrieval and adaptation may be reduced. Furthermore, although the framework demonstrated strong generalizability across healthcare, autonomous driving, aviation, industrial control, and cybersecurity datasets, domain-specific characteristics may still require customized feature engineering, threshold calibration, and model tuning to achieve optimal performance. Another limitation is that the experimental evaluation was primarily conducted using benchmark datasets and simulated risk scenarios. While these datasets are widely recognized and representative of real-world conditions, they may not fully capture the complexity, unpredictability, and operational constraints encountered in live deployments. Consequently, additional validation in large-scale industrial and missioncritical environments is necessary to further establish the framework’s practical reliability and robustness.

Another promising direction involves the incorporation of Generative AI-assisted risk reasoning to strengthen explainability and decision support. While the current framework provides explanations through feature attribution and historical case retrieval, future systems could employ large language models and generative reasoning engines to produce more comprehensive, human-readable interpretations of detected risks. Such capabilities could automatically summarize anomaly causes, predict potential consequences, recommend mitigation strategies, and generate incident reports for operators and regulators. By combining statistical evidence, retrieved historical cases, and generative reasoning, future versions of IRED-AI may provide more intelligent and context-aware support for decision-makers operating in complex and time-sensitive environments.

A second limitation concerns computational and operational considerations associated with real-time deployment. The integration of multiple components— including anomaly detection, explainable AI modules, similarity-based retrieval mechanisms, and adaptive feedback processes—introduces additional computational overhead compared with simpler detection approaches. Although the proposed framework maintains low latency and high throughput under experimental conditions, deployment in resource-constrained environments such as embedded systems, edge devices, or low-power industrial controllers may require further optimization. Moreover, while the framework incorporates explainability mechanisms to enhance transparency, the interpretation of generated explanations may still depend on the expertise of human operators and domain specialists. Finally, emerging challenges such as adversarial attacks, concept drift, evolving regulatory requirements, and novel AI failure modes remain active research areas that may affect long-term system performance. Future work should therefore focus on lightweight deployment strategies, federated and distributed learning architectures, enhanced adversarial resilience, and continuous validation under real-world operational conditions to further strengthen the trustworthiness and scalability of IRED-AI. 6.6. Future Research Directions

Finally, future studies should investigate multi-agent risk detection architectures and Edge AI deployment strategies to support increasingly distributed safety-critical ecosystems. In many real-world applications, risks emerge from interactions among multiple intelligent agents, sensors, autonomous vehicles, industrial robots, or interconnected cyber-physical systems. A multi-agent framework could enable cooperative risk detection, information sharing, and coordinated mitigation across distributed entities. Furthermore, deploying IRED-AI directly on edge devices would reduce communication latency, improve resilience against network disruptions, and enable faster responses to emerging threats. Advances in lightweight AI models, hardware acceleration, and distributed learning mechanisms will be essential for enabling real-time, scalable, and trustworthy risk detection in next-generation intelligent infrastructures. 7. Conclusion

IRED-AI establishes itself as a resilient, interpretable, and scalable solution for AI-induced risk detection. Through intelligent feature engineering, optimized retrieval, and explainability, it consistently outperforms baselines across safety-critical domains, balancing accuracy, latency, and robustness while addressing realworld challenges such as false alarms, adversarial conditions, and regulatory compliance.

Future research should focus on extending IRED-AI through the integration of federated learning and digital twin technologies to enhance scalability and real-world applicability. Federated learning would enable safetycritical organizations such as hospitals, aviation operators, and industrial facilities to collaboratively improve risk

1) Key Contributions and Innovations This work introduces IRED-AI, a comprehensive framework that integrates intelligent risk feature

<!-- page 30 -->

engineering, AI-accelerated retrieval, and explainability to address the limitations of traditional detection models. Unlike baselines that optimize single metrics, IRED-AI delivers holistic improvements across accuracy, latency, interpretability, and robustness. Key novel contributions include: (i) advanced feature engineering methods that enhance predictive accuracy while lowering false alarm rates; (ii) optimized retrieval architectures that scale efficiently to large datasets with minimal latency; and (iii) the integration of explainable AI and graph neural networks to ensure transparency in safety-critical operations. The framework also contributes a rigorous benchmarking pipeline across five domains, extending evaluation beyond static measures to include SLA compliance, adversarial resilience, and statistical significance testing. Together, these innovations create a unified, deployable solution for detecting AI-induced risks in real time while providing actionable, trustworthy insights, representing a substantial advancement over current state-of-the-art approaches.

increases computational cost and may reduce throughput in certain real-time scenarios. Risks such as data drift, adversarial manipulation, and operator overload persist, requiring continuous mitigation strategies. The framework’s scope is therefore best suited for safetycritical domains where accuracy, robustness, and transparency outweigh minimal efficiency costs. Future refinement should focus on reducing overhead, enhancing generalization across unseen domains, and further automating mitigation strategies to ensure seamless integration into dynamic operational environments.

4) Research Implications and Next Steps The implications of IRED-AI extend across technical, operational, and societal dimensions. Technically, it demonstrates that accuracy, interpretability, and scalability can be jointly optimized through intelligent enhancements. Operationally, its ability to meet SLA compliance and sustain performance under stress factors makes it suitable for direct deployment in healthcare monitoring, aviation safety, autonomous vehicles, and industrial control. Societally, the integration of explainable AI addresses regulatory compliance and fosters trust among human operators, paving the way for responsible AI adoption in sensitive sectors. The next steps involve expanding the framework’s adaptability by testing in large-scale realworld pilots and incorporating continuous learning mechanisms to handle evolving threats and data drift. Integration with edge and cloud infrastructures will also ensure broader accessibility and efficiency. These directions will ensure that IRED-AI not only remains academically significant but also transitions into a practically impactful solution with tangible benefits for critical industries.

2) Evidence of Effectiveness Extensive experiments across healthcare, aviation, autonomous driving, industrial control, and cybersecurity demonstrate IRED-AI’s consistent superiority. Dataset benchmarking confirms accuracy improvements above 95% and AUROC/AUPRC gains exceeding 3% over the strongest baselines. Latency reductions of 20–25% and false alarm rate decreases above 20% highlight its efficiency and reliability. Statistical tests reinforce significance, with p-values consistently <0.05 across all metrics, validating that performance gains are not incidental. Scenario-based evaluations show robustness under imbalanced distributions, adversarial perturbations, and cross-domain transfers, confirming adaptability to diverse operational environments. SLA analyses further establish IRED-AI’s compliance, with near-perfect adherence to latency, throughput, and interpretability targets. Visualization methods, including radar charts, heatmaps, and Taylor diagrams, confirm its balanced performance without trade-offs between accuracy and robustness. Collectively, the evidence confirms that IRED-AI is not only effective but also resilient, interpretable, and scalable, making it a reliable solution for risk detection in real-world safety-critical systems.

5) Directions for Future Research Future research on IRED-AI can focus on three key areas: scalability, resilience, and integration. Scalability improvements could leverage distributed architectures, federated learning, and cloud–edge synergy to enable deployment across massive datasets and geographically distributed environments. Resilience research should explore adversarially robust feature engineering and continual learning to ensure adaptability against evolving threats and unseen conditions. Deeper integration of graph neural networks and multimodal data streams will expand the framework’s applicability to complex, heterogeneous safety-critical systems. Additionally, embedding reinforcement learning for adaptive SLA optimization could further automate responsiveness to dynamic operational demands. From a societal perspective, aligning with emerging global regulatory frameworks and developing user-friendly interfaces for non-experts will increase adoption. These future directions position IREDAI not only as a next-generation research prototype but also as a sustainable, industry-ready platform for safe, reliable, and transparent AI deployment across diverse domains.

3) Research Limitations and Scope of Applicability Despite its strong results, IRED-AI faces limitations that define its scope of applicability. While feature engineering enhances accuracy and robustness, it introduces complexity and potential overfitting, particularly in domains with limited or noisy datasets. Cross-domain transfer shows moderate degradation, underscoring challenges in universal generalization. Computational overhead during training and indexing remains higher than lightweight baselines, potentially limiting deployment in extremely resource-constrained environments. Additionally, while explainability modules enhance trust and regulatory compliance, their integration

<!-- page 31 -->

[15] V. Thorstensen, On the use of artificial intelligence in safety-

References [1] I. Habli, R. Hawkins, C. Paterson, P. Ryan, Y. Jia, M.

critical systems, M.S. thesis, Norwegian University of Science and Technology (NTNU), 2024. [16] C. Thames and Y. Sun, “A survey of artificial

Sujan, and J. McDermid, “The big argument for AI safety cases,” arXiv preprint arXiv:2503.11705, 2025. [2] Z. Lin, H. Sun, and N. Shroff, “AI Safety vs. AI

intelligence approaches to safety and mission-critical systems,” in Proc. 2024 Integrated Communications, Navigation and Surveillance Conf. (ICNS), 2024. [17] I. F. Ramos, G. Gianini, M. C. Leva, and E. Damiani,

Security: Demystifying the Distinction and Boundaries,” arXiv preprint arXiv:2506.18932, 2025. [3] K. A. Kilian, “Beyond accidents and misuse:

“Collaborative intelligence for safety-critical industries: A literature review,” Information, vol. 15, no. 11, p. 728, 2024. [18] J. Fernández, I. Agirre, J. Perez-Cerrolaza, L.

Decoding the structural risk dynamics of artificial intelligence,” arXiv preprint arXiv:2406.14873, 2025. [4] Y. Bengio, S. Mindermann, D. Privitera, T. Besiroglu,

R. Bommasani, S. Casper, Y. Choi, et al., “International AI safety report,” arXiv preprint arXiv:2501.17805, 2025. [5] H. Abedsoltan, A. Abedsoltan, and Z. Zoghi,

Belategi, A. Adell, C. Donzella, and J. Abella, “AIFSM: Towards functional safety management for artificial intelligence-based critical systems,” in Proc. CARS@EDCC 2024 Workshop–Critical Automotive Applications: Robustness & Safety, 2024. [19] R. Blazevic, O. Veledar, M. Stolz, and G. Macher,

“RETRACTED: Future of process safety: Insights, approaches, and potential developments,” Process Safety and Environmental Protection, pp. 684–707, 2024. [6] M. Volk, “A safer future: Leveraging the AI power to

“Toward safety-critical artificial intelligence (AI)- based embedded automotive systems,” SAE Int. J. Connected and Automated Vehicles, vol. 8, no. 1, 2024. [20] S. Rana, “AI-driven fault detection and predictive

improve the cybersecurity in critical infrastructures,” Electrotechnical Review/Elektrotehniski Vestnik, vol. 91, no. 3, pp. 73-94, 2024. [7] H. Peter, “Cybersecurity implications of deploying

maintenance in electrical power systems: A systematic review of data-driven approaches, digital twins, and self-healing grids,” Amer. J. Adv. Technol. Eng. Solutions, vol. 1, no. 01, pp. 258–289, 2025. [21] J. Zhao, X. Feng, M.-K. Tran, M. Fowler, M. Ouyang,

autonomous AI agents in industrial control systems,” 2025. [8] I. Habli and J. A. McDermid, “AI safety: Navigating

the expanding landscape of potential harms,” 2024. [9] B. Kirwan, “Human factors requirements for human-

and A. F. Burke, “Battery safety: Fault diagnosis from laboratory to real world,” J. Power Sources, vol. 598, Art. no. 234111, 2024. [22] L. K. Vandrangi, “AI-driven fault detection and

AI teaming in aviation,” Future Transportation, vol. 5, no. 2, p. 42, 2025. [10] A. E. Muhammad, K. C. Yow, J. Baili, Y. Cho, and

isolation in smart grids: A review and lightweight framework proposal,” J. Appl. Sci. Multidiscip. Eng., 2025. [23] J. A. Martinez-Velasco, A. Serrano-Fontova, R.

Y. Nam, “CORTEX: Composite overlay for risk tiering and exposure in operational AI systems,” arXiv preprint arXiv:2508.19281, 2025. [11] S. Paleti, “Neural compliance: Designing AI-driven

Bosch-Tous, and P. Casals-Torrens, “Survey on methods for detection, classification and location of faults in power systems using artificial intelligence,” arXiv preprint arXiv:2507.10011, 2025. [24] J. Feng, T. Yu, K. Zhang, and L. Cheng, “Integration

risk protocols for real-time governance in digital banking systems,” SSRN, SSRN 5233099, 2024. [12] D. Onitiu, V. Yazdanpanah, A. Chapman, E.

Gerding, S. E. Middleton, and J. Williams, “On the Legal Aspects of Responsible AI: Adaptive Change, Human Oversight, and Societal Outcomes,” in AI for People, Democratizing AI: Second EAI International Conference, CAIP 2023, Bologna, Italy, Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering, vol. 591. Cham, Switzerland: Springer, 2024, pp. 73–85. [13] J. Perez-Cerrolaza, J. Abella, M. Borg, C. Donzella, J.

of multi-agent systems and artificial intelligence in self-healing subway power supply systems: Advancements in fault diagnosis, isolation, and recovery,” Processes, vol. 13, no. 4, p. 1144, 2025. [25] D. Simion, F. Postolache, B. Fleacă, and E. Fleacă,

“AI-driven predictive maintenance in modern maritime transport—Enhancing operational efficiency and reliability,” Applied Sciences, vol. 14, no. 20, p. 9439, 2024. [26] P. Giudici, M. Centurelli, and S. Turchetta, “Artificial

Cerquides, F. J. Cazorla, C. Englund, M. Tauber, G. Nikolakopoulos, and J. L. Flores, “Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey,” ACM Computing Surveys, vol. 56, no. 7, pp. 1–40, 2024. [14] N. Flehmig, M. A. Lundteigen, and S. Yin,

intelligence risk measurement,” Expert Syst. Appl., vol. 235, p. 121220, 2024. [27] M. Emmanuel, “Real-time fault detection in

predictive energy finance AI systems,” 2025. [28] S. Nazat, O. Arreche, and M. Abdallah, “On

“Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process,” in Proc. IECON 2024–50th Annu. Conf. IEEE Industrial Electronics Society, 2024, pp. 1–8.

evaluating black-box explainable AI methods for enhancing anomaly detection in autonomous driving systems,” Sensors, vol. 24, no. 11, p. 3515, 2024.

<!-- page 32 -->

[29] S. Nazat, L. Li, and M. Abdallah, “XAI-ADS: An

EURASIP J. Image Video Process., vol. 2024, no. 1, p. 15, 2024. [42] J.-S. Jung, C. Son, A. Rimell, and R. J. Clarkson, “A

explainable artificial intelligence framework for enhancing anomaly detection in autonomous driving systems,” IEEE Access, vol. 12, pp. 48583–48607, 2024. [30] A. N. Gummadi, J. C. Napier, and M. Abdallah,

framework for an ML-based predictive turbofan engine health model,” Aerospace, vol. 12, no. 8, p. 725, 2025. [43] Z. Cao, A Framework for Data Collection and Airside

“XAI-IoT: An explainable AI framework for enhancing anomaly detection in IoT systems,” IEEE Access, vol. 12, pp. 71024–71054, 2024. [31] D. G. Bhatt, P. U. Kyada, R. S. Rathore, M. K.

Operation Metrics Analysis at Small Airports, Ph.D. dissertation, University of Maryland, College Park, MD, USA, 2025. [44] F. Dadaser-Celik, “Modelling climate change impacts

Nallakaruppan, and R. H. Jhaveri, “Enhancing anomaly detection in industrial control systems through supervised learning and explainable artificial intelligence,” J. Cybersecurity & Inf. Manag., vol. 15, no. 1, 2025. [32] T. J. Chengula, J. Mwakalonge, G. Comert, M. Sulle,

on watershed hydrology using SWAT,” in Hydrology and Urban Water Supply, Cham, Switzerland: Springer Nature, 2024, pp. 43–54. [45] M. N. El-Tawapty, Z. Hamimi, H. Khamis, and M.

Khalil, “Landsat-based lithological mapping of the Neoproterozoic rocks in the Egyptian Nubian Shield: Case study from Wadi Zeidun area, Central Tectonic Province,” Sci. J. Damietta Fac. Sci., vol. 15, no. 1, pp. 82–89, 2025. [46] A. D. Vibhute, M. Khan, C. H. Patil, S. V. Gaikwad,

S. Siuhi, and E. Osei, “Enhancing advanced driver assistance systems through explainable artificial intelligence for driver anomaly detection,” Mach. Learn. Appl., vol. 17, p. 100580, 2024. [33] C. Nwachukwu, K. Durodola-Tunde, and C.

Akwiwu-Uzoma, “AI-driven anomaly detection in cloud computing environments,” Int. J. Sci. Res. Arch., vol. 13, no. 2, pp. 692–710, 2024. [34] K. Mathuros, S. Venugopalan, and S. Adepu, “Waxai:

A. V. Mane, and K. K. Patel, “Network anomaly detection and performance evaluation of convolutional neural networks on UNSW-NB15 dataset,” Procedia Comput. Sci., vol. 235, pp. 2227– 2236, 2024. [47] X. Qi, H. Gu, J. Yi, J. Tao, Y. Ren, J. He, and S. Zeng,

Explainable anomaly detection in industrial control systems and water systems,” in Proc. 10th ACM CyberPhysical System Security Workshop, 2024, pp. 3–15. [35] F. M. Talaat, A. R. Elnaggar, W. M. Shaban, M.

“MADD: A multi-lingual multi-speaker audio deepfake detection dataset,” in Proc. 2024 IEEE 14th Int. Symp. Chinese Spoken Language Processing (ISCSLP), 2024, pp. 466–470. [48] S. Paleti, “Neural compliance: Designing AI-driven

Shehata, and M. Elhosseini, “CardioRiskNet: A hybrid AI-based model for explainable risk prediction and prognosis in cardiovascular disease,” Bioengineering, vol. 11, no. 8, p. 822, 2024. [36] N. T. Hosseinkhani, “Comparative Analysis of

risk protocols for real-time governance in digital banking systems,” SSRN, SSRN 5233099, 2024. [49] J. Nolan and M. Steven, “AI-driven approaches for

Financial Performance Among Traditional Quantitative, AI-Based, and Hybrid Modeling Approaches,” SSRN, SSRN 5403534, 2025. [37] M. Alsaadi, M. T. Almashhadany, A. S. Obaed, H. B.

optimizing semiconductor design verification using UVM,” ResearchGate, Oct. 2024. [50] C. Park, “Addressing challenges for the effective

Furaijl, S. Kamil, and S. R. Ahmed, “AI-based predictive analytics for financial risk management,” in Proc. 2024 8th Int. Symp. Multidisciplinary Studies and Innovative Technologies (ISMSIT), 2024, pp. 1–7. [38] U. Ahmed, Z. Jiangbin, A. Almogren, S. Khan, M. T.

adoption of artificial intelligence in the energy sector,” Sustainability, vol. 17, no. 13, p. 5764, 2025. [51] A. Narayanan and S. Kapoor, “AI as normal

technology,” Knight First Amend. Inst., 2025. [52] D. Kutá and M. Faltejsek, “The role of artificial

Sadiq, A. Altameem, and A. U. Rehman, “Explainable AI-based innovative hybrid ensemble model for intrusion detection,” J. Cloud Comput., vol. 13, no. 1, p. 150, 2024. [39] O. J. Bear Don’t Walk IV, A. Pichon, H. R. Nieva, T.

intelligence in the transformation of the BIM environment: Current state and future trends,” Applied Sciences, vol. 15, no. 18, p. 9956, 2025. [53] A. Mohanty, A. G. Mohapatra, S. K. Mohanty, B.

Keswani, and S. Nayak, “Computational intelligent techniques in mechatronics: Emerging trends and case studies,” Comput. Intell. Tech. Mechatronics, pp. 401–444, 2024. [54] D. Onitiu, V. Yazdanpanah, A. Chapman, E.

Sun, J. Li, J. Joseph, S. Kinberg et al., “Contextualized race and ethnicity annotations for clinical text from MIMIC-III,” Sci. Data, vol. 11, no. 1, p. 1332, 2024. [40] T. D. Tran, N. Q. Tran, T. T. K. Dang, H. L. Pham,

and Y. Nakashima, “ECG captioning with priorknowledge transformer and diffusion probabilistic model,” J. Healthc. Inf. Res., pp. 1–26, 2024. [41] N. A. B. Martins, L. A. da Silva Cruz, and F. Lopes,

Gerding, S. E. Middleton, and J. Williams, “On the Legal Aspects of Responsible AI: Adaptive Change, Human Oversight, and Societal Outcomes,” in AI for People, Democratizing AI: Second EAI International Conference, CAIP 2023, Cham, Switzerland: Springer, 2024, pp. 73–85.

“Impact of LiDAR point cloud compression on 3D object detection evaluated on the KITTI dataset,”

<!-- page 33 -->

[55] M. Trigka and E. Dritsas, “The evolution of

[62] U. Tariq and I. Ahmed, “Reasoning about

generative AI: Trends and applications,” IEEE Access, vol. 13, 2025. [56] S. M. Hashemi and P. C. K. Hung, “Comprehensive

responsibility in autonomous systems: Navigating the challenges and charting future directions,” Ubiquitous Technol. J., vol. 1, no. 2, pp. 46–60, 2025. [63] S. U. Hamida, M. J. M. Chowdhury, N. R.

guide to home robot security: From system analysis to solution recommendation,” J. Inf. Assur. Secur., vol. 20, no. 1, 2025. [57] M. Ngcobo, “The ethics and law of medical AI in

Chakraborty, K. Biswas, and S. K. Sami, “Exploring the landscape of explainable artificial intelligence (XAI): A systematic review of techniques and applications,” Big Data Cogn. Comput., vol. 8, no. 11, p. 149, 2024. [64] R. Al-Dahdooh, A. Marouf, M. J. Abu Ghali, A. O.

South Africa: Balancing innovation with responsibility,” SAMJ: S. Afr. Med. J., vol. 115, no. 5B, pp. 75–79, 2025. [58] N. Bienefeld, E. Keller, and G. Grote, “AI

Mahdi, B. S. Abu-Nasser, and S. S. Abu-Naser, “Explainable AI (XAI),” IJAER, vol. 8, no. 10, 2025. [65] F. Herrera, “Reflections and attentiveness on

interventions to alleviate healthcare shortages and enhance work conditions in critical care: qualitative analysis,” J. Med. Internet Res., vol. 27, p. e50852, 2025. [59] R. Hunter, R. Moulange, J. Bernardi, and M. Stein,

eXplainable Artificial Intelligence (XAI). The journey ahead from criticisms to human–AI collaboration,” Inf. Fusion, vol. 121, p. 103133, 2025. [66] D. Tchuente, J. Lonlac, and B. Kamsu-Foguem, “A

“Monitoring human dependence on AI systems with reliance drills,” arXiv preprint arXiv:2409.14055, 2024. [60] J. Sun and B. Xin, “Special issue on new frontiers of

methodological and theoretical framework for implementing explainable artificial intelligence (XAI) in business applications,” Comput. Ind., vol. 155, p. 104044, 2024. [67] P.-D. Arsenault, S. Wang, and J.-M. Patenaude, “A

autonomous intelligent unmanned systems, dedicated to the 85th anniversary of the Beijing Institute of Technology,” Unmanned Syst., vol. 13, no. 5, 2025. [61] A. K. Musaffar, A. Gokhale, S. Zeng, R. Tadayon, X.

survey of explainable artificial intelligence (XAI) in financial time series forecasting,” ACM Comput. Surv., vol. 57, no. 10, pp. 1–37, 2025. [68] D. J. Yeong, K. Panduru, and J. Walsh, “Exploring

Yan, A. Singh, and F. Bullo, “Learning to lie: Reinforcement learning attacks damage human-AI teams and teams of LLMs,” arXiv preprint arXiv:2503.21983, 2025.

the unseen: A survey of multi-sensor fusion and the role of explainable AI (XAI) in autonomous vehicles,” Sensors, vol. 25, no. 3, p. 856, 2025.

Assoc. Prof. Dr. Thacha Lawanna is a dedicated academic currently serving as a lecturer at the International College of Digital Innovation, Chiang Mai University, Thailand. She earned her Ph.D. in Information Technology from Assumption University, where she cultivated a strong foundation in advanced computing and intelligent systems. Her areas of expertise include Artificial Intelligence (AI), Software Engineering, Machine Learning, and Data Mining.
