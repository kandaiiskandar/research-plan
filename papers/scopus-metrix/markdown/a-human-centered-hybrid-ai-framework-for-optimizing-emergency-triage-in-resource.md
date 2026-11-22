# A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings

> **Source PDF:** `A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings.pdf` · **Pages:** 15 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Intelligence-Based Medicine 12 (2025) 100311

Contents lists available at ScienceDirect

Intelligence-Based Medicine

journal homepage: www.sciencedirect.com/journal/intelligence-based-medicine

A human-centered hybrid AI framework for optimizing emergency triage in resource-constrained settings

E. Bhuvaneswari a,*, K.D.V. Prasad b,c, Mohd Ashraf d, Sachin Jadhav e, TK Rama Krishna Rao f, Tirukoti Sudha Rani g

a Department of Artificial Intelligence and Data Science, Panimalar Engineering College, Chennai, Tamil Nadu, India b Symbiosis Institute of Business Management, Hyderabad, India c Symbiosis International (Deemed University), Pune, India d Computer Science & Engineering, School of Technology, Maulana Azad National Urdu University, Hyderabad, TS, India e Department of Computer Engineering, Vishwakarma Institute of Technology, Pune, India f Department of Computer Science and Engineering, Koneru Lakshmaiah Education Foundation, Vaddeswaram, AP, India g Department of Computer Science & Engineering, Aditya University, Surampalem, India

### A R T I C L E I N F O

### A B S T R A C T

Keywords: Hybrid AI Emergency triage Human cognitive insights Resource-constrained healthcare Machine learning Cognitive biases Decision support systems Human-in-the-loop Clinical decision-making

The paper proposes a human-centred hybrid artificial intelligence system, capable of triaging emergencies in healthcare facilities that are resource-constrained. The system combines cognitive modelling, lightweight ma­ chine learning and resource-aware optimization to provide interpretable and actionable triage recommendations. The framework provides adaptive decision support by integrating patient vital signs, accessible clinical re­ sources, and clinician workload, allowing clinicians to override these inputs as needed.

The architecture is a hybrid of a cognitive module that probabilistically learns clinical heuristics and cognitive biases, a convolutional neural network-based predictive model with explainability provided by SHAP, and a resource-conscious optimizer, based on either integer programming or heuristic reinforcement learning. Two- way communication is supported by a human-in-the-loop interface, allowing the clinician to provide feedback and override suggestions, with the system recording the reasons behind ongoing learning and adaptation.

The 90 % accuracy and over 0.86 receiver operating characteristic area under the curve were confirmed through simulated and pilot implementations. Compared to baseline methods, the hybrid system decreased the false negatives by 12 to 5 %, thus significantly enhancing the detection of high-acuity cases. The AI-assisted decision-making lowered the time spent by clinicians in decision-making by 31 % and resource optimization strategies enhanced the critical resource use by 20 %, lowering the override rates significantly.

Significant results include better triage accuracy, faster and more confident clinician decisions, and more effective resource allocation. The flexibility of the framework to local constraints offers a viable avenue through which AI implementation in resource-constrained emergency care facilities can be done safely and effectively. The presented collaborative model suggests that a combination of human skills and AI capabilities can be used to improve the performance of emergency triage and support progress in the field of difficult healthcare settings without ethical and clinical supervision.

## 1. Introduction

patients is however questioning the validity and reliability of traditional triage systems. The conventional methods like the Manchester Triage System (MTS) and Emergency Severity Index (ESI) tend to be based on some judgment of the physician and some fixed scoring criteria that all are prone to human error and inconsistencies [1,2].

Good triage in an emergency is a third important aspect of deciding survival and survival of the patient and it continues to be a massive aspect in the prompt identification and treatment of patients who are in critical conditions. The emergence of more patients and complex

Among the possible channels to enhance the accuracy of the triage,

* Corresponding author. E-mail addresses: bhuvaname2008@gmail.com (E. Bhuvaneswari), Kdv.prasad@sibmhyd.edu.in (K.D.V. Prasad), ashraf.saifee@gmail.com (M. Ashraf), srjadhav02@gmail.com (S. Jadhav), ramakrishnatk@gmail.com (T.R.K. Rao), sudharani.tirukoti@adityauniversity.in (T. Sudha Rani).

https://doi.org/10.1016/j.ibmed.2025.100311 Received 6 September 2025; Received in revised form 18 October 2025; Accepted 29 October 2025

Available online 1 November 2025 2666-5212/© 2025 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by- nc/4.0/ ).

<!-- page 2 -->

the use of artificial intelligence (AI), allowing categorising risks on the basis of the information and distributing the medical resources more efficiently is one of the possible options [3–5]. The current study reveals that the accuracy of the classification systems in the triage systems based on the artificial intelligence is over 90 % and with the conventional systems, the accuracy is under 70 % [1,4,6].

significant surge in recent years, driven by the potential to enhance patient outcomes in high-pressure healthcare environments with limited resources, optimise resource allocation, and improve triage accuracy. Numerous studies have explored the application and usage of a plethora of AI techniques, from deep learning models to traditional machine learning algorithms, on various datasets, such as prehospital, clinical, and operational data. Despite promising results, there are still significant problems with real-time applications, ethical concerns and model transparency. The following assessment examines important recent contributions to this field, identifying methods, performance measures, and gaps in order to help point the way to further research and clinical adoption [11–14].

Although these were popular triage techniques, however, there is subjectivity in popular triage techniques, cognitive overload, and human biases such as anchoring bias and human availability. These biases might cause distortion of clinical judgment and result in unequal attention and late treatment. As a result, the rate of triage errors can be up to 32 % in certain systems [6,7]. Furthermore, rule based or rule-based triage strategies do not have the adaptability to match the changing workload, the rise and fall of patient acuity and alterations in the situation. Rigidity can make unequal priority allocation and resource misallocation more likely to happen [8]. These shortcomings show how difficult it is to identify decision support tools to ensure decisions are more reliable and at the same time acknowledge the cognitive pecu­ liarities of human beings.

Gao et al. [15] applied big data from the Emergency Medicine Department of Beijing Chao-Yang Hospital, which includes 276,164 patients from 2017 to 2020, to develop and validate an emergency triage model based on machine learning techniques. By applying the Extreme Gradient Boosting (XGBoost) technique to simulate the triage decisions of nurses, they were able to obtain a prediction accuracy of 82.57 %. The area under the curve (AUC) of the model was between 0.9120 and 0.9629 for cases of all triage severity. Challenges included the general­ izability of the models in different hospital settings and a variety of patient presentations.

Some of the other difficulties in the low-resource setting, including rural hospitals, small clinics, and disaster scenarios, include high patient to provider ratio, unstable infrastructure, shortage of critical care pro­ viders, and diagnostic capabilities [9–11]. Researchers indicate that over 80 percent of physicians in certain regions lack any formal training in pediatric emergency triage, a factor that increases the occurrence of triage mistakes and care delays [11]. Safety, flexible, and context-driven triage systems are therefore gaining more and more demand particularly in circumstances where resources are limited.

Chen et al. [16] studied the impact of ED congestion on admission decision and triage based on retrospective data from 65,065 patient encounters at a US university centre ED. They used cumulative logit regression and multivariate logistic regression models to investigate correlations between ED census data and evaluation of the patient acuity classification or disposition. According to statistical research, the probability of admission or classification of patients into high acuity rose significantly with the increase in occupancy in the ED. High acuity triage increased by about 50 % with a rise in census from 25 to 75. The study highlighted the issues that clinicians experience when trying to make decisions when facing the pressure of crowds.

Human-in-the-loop (HITL) systems, where the AI models and humans are run in a feedback loop, represent a possible solution to this issue. This model is characterized by doctors continuing to have over­ sight and power to confirm, revise or obstruct verdicts and AI provides interpretable triage proposals, which are grounded in data-driven inference. When the AI model is progressively enhanced with the contribution of the physicians, transparency, flexibility and trust are enhanced [12,13].

Kang et al. [17] created a deep learning artificial intelligence algo­ rithm for determining the need for critical care in prehospital emergency medical services (EMS) based on data from 8,981,181 patients in Korean EDs. A total of 2604 EMS run sheets were used for validating this model. Their model was sensitive compared with traditional triage techniques, with an area under the receiver operating characteristic curve (AUC) of 0.867 (95 % CI: 0.864–0.871). The aim of the study was to focus on clinical features and vital signs available in EMS to better identify high-risk patients at an early stage. Among the challenges were inte­ grating heterogeneous real-time EMS data and ensuring reliable per­ formance in various prehospital scenarios.

According to recent research, it is possible to create hybrid AI triage systems, which integrate workload and resources data, represent cognitive biases (probabilistically) and encode clinician heuristics and preserve human interpretability [4,12–14]. These systems are a com­ bination of machine learning, constrained optimisations and program cognitive modelling systems. Particularly in areas where the burden of patients is high and medical resources are limited, these hybrid solutions increase safety, flexibility and physician confidence.

A hybrid artificial intelligence triage system is developed specifically for urgent situations characterised by limited resources and is proposed and evaluated in this research. To generate adaptive triage recommen­ dations, the system uses a combination of cognitive task analysis, interpretable machine learning-based risk predictors, and a resource- aware optimization engine. In order to support continuous model development, a human-in-the-loop interface logs clinician reasons for overriding in addition to showing risk indications and triage recom­ mendations. Through pilot implementations and simulations, clinical accuracy, operational efficacy, and human factor operation of the sug­ gested system is estimated.

Chee et al. [18] conducted systematic scoping review of uses of AI in prehospital emergency care (PEC) field and found 106 relevant studies, with most of them internally validated and retrospective. Very few of the AI applications that they charted like triage, prognostication and CPR/AED optimization, employed multimodal data-inputs like text or audio. They discovered that AI defeated human or non-AI algorithm in 39 out of the 49 comparator studies. In order to apply AI beyond the proof-of-concept level, they also defined multiple potential barriers, such as the necessity of prospective validation and the issue of meth­ odological heterogeneity.

In one of the examples of a scoping study on the use of AI in the context of emergency care, Hosseini et al. [19] discovered that 47 papers found were relevant to the research topic, and that included ethical and legal concerns pertinent to AI. Their thematic analysis of the identified AI applications found seven areas, such as triage, prediction of illness and handling of the emergency department. They indicated that despite such a monumental move in the artificial intelligence research sector, questions regarding explainability and transparency in artificial intelli­ gence decision-making still persist and present a risk to the ethical use and use of clinicians. The assessment proposed to establish frameworks to enhance the visibility of AI integration into emergency medical practice, as it will result in safer implementation.

This paper’s other sections are organised as follows: Section 2 re­ views pertinent work on cognitive modelling, adoption of AI, and emergency triage. The architecture, the model training and the cognitive elicitation procedure are introduced in Section 3. Results obtained from evaluations and pilot tests are presented in Section 4. The principal contributions and potential therapeutic applications of the framework suggested are finally discussed in Section.

## 2. Literature survey

The integration of AI and ML into emergency care has led to a

<!-- page 3 -->

**Fig. 1. Overview of the proposed Hybrid AI Triage Framework Methodology.**

Recent extensive research by Agius et al. (2025) indicates the importance of machine learning based on the data in emergency triage and clinical decision-making. They use large volumes of real world emergency room data to create effective predictive models that integrate demographic, clinical and cognitive data. They demand a systematic and explicit strategy of healthcare predictive models development on the clinical relevance and interpretability basis. Moreover, their analysis shows the significance of human-centred digital technologies in the improvement of patient safety through preventing cognitive load and complexity in the workflow in acute care facilities [20–22].

This module is built on lightweight, explainable machine learning ap­ proaches, such as gradient boosted trees with SHAP-based interpret­ ability. Using integer programming or heuristic reinforcement learning, resource-aware optimization is accomplished, guaranteeing that sug­ gestions are workable even in constrained environments. By supporting two-way communication, a human-in-the-loop interface enables physi­ cians to record reasons, veto system suggestions, get bias/confidence signals, and continuously build trust. Because system thresholds and models are updated based on patient outcomes and physician input, this promotes adaptive learning. Through offline simulations, tabletop ex­ ercises, and pilot deployments, the entire system is iteratively verified. The results are assessed in terms of clinical accuracy, decision speed, resource use, override rates, and physician acceptability. Fig. 1 visually summarizes the proposed architecture.

Recent studies indicate that AI has made a significant development in the area of emergency care, and its models have achieved high levels of prediction and a significant level of triage classification. Majority of the studies are however retrospective in nature and have not been pro­ spectively validated and this limits their application in practice. Among the challenges, there are the need to introduce human cognitive factors, deal with ethical concerns, and the transparency of AI decision-making. Resource constraints and dynamic emergency department settings make deployment challenging. The proposed project will solve these gaps by creating a hybrid artificial intelligence (AI) triage system. The system integrates resource-sensitive optimization, explicit cognitive modelling and light-weight machine learning to maximise the safety, understand­ ability, and usefulness of resource-constrained responses to emergencies.

• Patient, context, and human factors input data are processed through the cognitive module and a CNN-based predictive model. • Explainable outputs and risk predictors feed into a resource-aware optimizer, which applies heuristic reinforcement learning. • The human-in-the-loop interface enables feedback and overrides, driving ongoing learning and adaptation. • Continuous evaluation and iteration update the system for improved accuracy and reliability in emergency triage processes.

## 3. Methodology

### 3.1. Input data and context

In order to design, create, and assess a hybrid AI triage system that is suited for emergency situations with limited resources, this study uses an organized methodology. In order to methodically record expert heuristics, triage decision limits, and common cognitive biases influ­ encing emergency treatment, the method starts with thorough cognitive task analysis and facilitated clinician interviews. The development of a cognitive module that probabilistically predicts bias and encodes physician knowledge is guided by these results.

A wide range of input variables, including clinical, contextual, and human elements that are essential for precise emergency triage decision- making, are included in the first stage of the hybrid AI triage architec­ ture. A patient’s vital signs (heart rate, respiration rate, oxygen satura­ tion, blood pressure, temperature), Glasgow Coma Scale scores, Glasgow Coma Scale scores, comorbidity counts, and point-of-care test findings (lactate levels) are examples of clinical variables. These characteristics record the patient’s present physiological condition as well as clinical risk factors that are important for prioritizing triage.

In addition, a predictive module is created to use real-time clinical and contextual data to estimate patient risk and resource requirements.

The operating environment and resource availability of the

<!-- page 4 -->

**Fig. 2. The proposed Predictive Module CNN Architecture.**

emergency scenario at the time of evaluation are represented by contextual characteristics. This includes real-time information on oxy­ gen cylinders, hospital beds, staffing levels (number of clinicians on duty), patient wait times, transportation availability, and the time of day. These factors show how local resource limitations impact triage choices. Workload indices that reflect the current patient load per clinician, self-confidence scores that indicate subjective clinician assurance, adherence to local triage guidelines or protocols, and healthcare provider experience (years of practice) are examples of human factors that capture clinician-related influences on triage. These elements recognize how human cognitive and operational dynamics affect the results of triage.

```math
bk = P(biask|X, c)
eq(3)
```

where bk is the probability of cognitive bias k (such as anchoring or availability) given patient data X and clinician context c (workload, experience). The combined cognitive output C(X, c) fuses heuristic de­ cisions and bias probabilities to adjust recommendations or trigger alerts:

### ∑ M

### ∑ N

C(X, c) =

wjhj(X) −

```math
λkbk
eq(4)
```

j=1

k=1

where wj and λk are weighting parameters balancing heuristic contri­ butions and bias influences.

The basic dataset for later cognitive modeling and predictive ana­ lytics that are adapted to the limitations and dynamics of emergency care situations is provided by these multi-dimensional inputs. The following may be used to describe the input feature vector for each patient instance at time t:

### 3.3. Predictive module

The predictive module is a lightweight convolutional neural network (CNN) designed to predict risk during emergency triage processing of multi-dimensional clinical data in context. This CNN model consists of two convolutional layers with ReLU activation functions, two fully connected layers, and allows the model to reveal complex non-linear interaction effects among human variables, vital signs, and environ­ mental data. The model produces patient-specific risk scores that indi­ cate the likelihood of clinical deterioration or resource requirements. To further increase interpretability, Shapley Additive exPlanations (SHAP) is applied to the outputs of the CNN, providing a feature-level contri­ bution for each prediction made by the model. This transparency pro­ motes confidence and enables doctors to understand the reasoning behind AI-driven risk assessments, leading to informed and secure triage decisions. The proposed CNN architecture of the Predictive Module is shown in Fig. 2.

⎡

⎤

Pt Ct Ht

Xt =

```math
⎦
eq(1)
```

⎣

Where, Pt = [p1, p2, …, pm] represents the patient features, pi ∈ {heart rate,respiratory rate,SpO2,blood pressure,temperature,…}, Ct = [c1, c2, …, cn] denotes the context features, such as: cj ∈{available beds, oxygen cylinders, staff count, transport availability, time of day, …}, Ht = [h1, h2, …, hk] captures the human factors, including: hl ∈ {clinician experience, workload index, local triage rules, …}. Thus, the complete feature set Xt integrates diverse dimensions necessary to model nuanced triage decisions in resource-constrained settings.

### 3.2. Cognitive module

Let the input feature tensor for patient t be Xt ∈Rm×n×c, where m and n denote spatial or temporal dimensions (e.g., vital sign sequences) and c represents input channels (features). The CNN model fθ with parameters θ maps the input to a risk prediction: ̂

Clinical heuristics and decision rules are explicitly stored in the cognitive module based on structured interviews and analysis of cognitive tasks. These heuristics will reflect predefined clinical trends and rule-of-thumb cutoffs that doctors tend to apply when triaging in an emergency. The program also includes models of cognitive biases, such as availability and anchoring biases, that can affect decision-making under stressful and uncertain situations. Incorporated (through a prob­ abilistic model), the system can use biases to reduce the risks of error generation by creating warnings or modifying the recommendations. Combining expert knowledge and bias awareness makes triage decisions safer and more understandable, as well as closer to the clinical reasoning of a real-world patient. Suppose that the set of clinical heuristics and decision rules can be expressed as follows:

```math
yt = fθ(Xt)
eq(5)
```

where ̂ yt represents the estimated risk probability. SHAP values ϕi quantify the contribution of each feature/input channel i to the model output: ̂

∑ d

yt = ϕ0 +

```math
ϕi
eq(6)
```

i=1

where ϕ0 is the expected output over the dataset, and d is the total number of input features. This decomposition enhances clinical decision support and promotes local interpretability by highlighting key features that influence the CNN’s risk prediction for each patient.

{

}

hj : X →{0, 1}⃒⃒j = 1, …, M

```math
eq(2)
```

### H =

where each heuristic hj is a binary function mapping input features X to a decision indicator. A probabilistic function represents the cognitive bias model:

The CNN architecture was chosen over conventional machine learning approaches because it excelled in an emergency triage predic­ tion challenge and has been shown to effectively model complex

<!-- page 5 -->

nonlinear interactions in multimodal clinical data. This balance of per­ formance and resource usage is supported in the literature and ablation studies showing light CNNs that can extract hierarchical features in time series, structured inputs, and achieve high accuracy, robustness, and interpretability with computational lightness.

associated confidence score and bias alert indicator bt ∈{0,1}, where 1 denotes a significant cognitive bias warning.

The clinician’s final decision yt is defined as:

{̂

```math
yt
if no override
ot
if override
eq(12)
```

yt =

### 3.4. Resource-aware optimizer

where ot is the clinician’s override decision at time t.

Additionally, the interface captures the clinician’s rationale rt, which can be represented as a vector of qualitative or quantitative annotations:

A resource-aware optimizer is also a major component that maps the resource estimates with actual resource constraints to produce feasible triage decisions. It optimally distributes scarce resources, namely, hos­ pital beds, oxygen supply and clinical staff, subject to the predicted patient demands using an integer programming algorithm or by a heu­ ristic reinforcement learning algorithm. By incorporating explicit con­ straints that represent the actual availability and capacity of resources, the optimizer ensures the feasibility and practicality of the triage labels and transfer recommendations. By balancing patient outcomes and resource use, the risk of inappropriate patient assignment due to over­ allocation or resource constraints is reduced, which in turn is likely to decrease the number of patients assigned to risky triage placements.

[

]

rt =

rt,1, rt,2, …, rt,m

```math
eq(13)
```

(

)

is then fed back into the system’s learning and adaptation module to refine model parameters and thresholds dynamically, enhancing future recommendation accuracy and clinician satisfaction.

The combined tuple

yt, ct, bt, rt

### 3.6. Learning and adaptation

The learning and adaptation module is the one that provides the hybrid AI triage system with a chance to continuously ameliorate, owing to the real-world patient outcomes and clinician override response. Exempts cases of the documents in which the medical professionals are relying on advice of the AI that provides imperative information that covers the context-specific details and progressing heuristics. Previously established conclusions can be compared to the data of the patient outcomes, and the model can be re-calibrated to minimize the error count and make the forecasts more precise. It is through this feedback mechanism that it is possible to make online learning possible by adaptively adjusting the decision thresholds and retraining the predic­ tion models associated with the decision thresholds, to reflect clinical reality and resource constraints. With a planned cycle of adjusting to the emerging information, the system can remain pertinent, reliable, and secure not only in a range of diverse emergency care settings but also dynamic. In order to capture the data of the above-mentioned decisions, we will have the following representation:

Let there be N patients, each with a predicted resource requirement ri and a binary decision variable xi indicating admission or transfer where:

{

```math
1
if patient i is allocated resources (e.g., admitted)
0
otherwise
eq(7)
```

xi =

Given resource availability constraints, such as total available beds B and oxygen units O, the optimizer solves:

### ∑ N

max

```math
vixi
eq(8)
```

x

i=1

subject to

### ∑ N

r(bed)

```math
i
xi ≤B
eq(9)
```

i=1

### ∑ N

D = {Xi, yi, oi, ri, zi}N

```math
i=1
eq(14)
```

r(oxygen)

```math
i
xi ≤O e
eq(10)
```

i=1

where for each case i, Xi is the input feature vector, yi is the AI recom­ mendation, oi is the clinician override decision (if any), ri is the captured rationale for overrides, zi is the observed patient outcome (e.g., deteri­ oration or stability). The model parameters θ and thresholds τ are adaptively updated by minimizing a loss function L over D that in­ corporates prediction accuracy and override agreement:

```math
xi ∈{0, 1} ∀i = 1, …, N
eq(11)
```

where vi is the prioritization value reflecting patient acuity or predicted benefit from resource allocation. Alternatively, heuristic reinforcement learning (RL) approaches learn allocation policies π(s) mapping system states s including patient risks and resource status to triage actions optimized for long-term outcomes under constraints. The optimizer produces workable triage labels and transfer recommendations that consider the risk of each patient as well as the capabilities of the system at the moment.

### ∑ N

θ*, τ* = arg min

```math
L(fθ(Xi; τ), zi, oi)
eq(15)
```

θ,τ

i=1

where fθ(Xi; τ) is the model output with current parameters and thresholds. This optimization is performed periodically or online to refine the system’s decision boundaries and predictive accuracy, ensuring continual alignment with clinician expertise and patient safety.

### 3.5. Human-in-the-loop interface

Human-in-the-loop interface: A human-in-the-loop interface is necessary for the smooth collaboration between medical professionals and the AI system, which is precisely what this interface provides. It provides short-term triage advice, gives ratings of confidence, and points out potential cognitive biases that may influence decision-making. The interface should enable physicians to override AI recommendations when necessary and provide justification for their choices. This two-way communication encourages transparency and creates confidence among clinicians, and adds feedback to the decision-making process, resulting in improved learning outcomes. This design acknowledges the need for human expertise in complicated healthcare scenarios, recognising that AI complements, rather than replaces, critical decision-making.

### 3.7. Evaluation and iteration

The evaluation and refinement phase takes a complex approach to critically analyze the functionality of the hybrid AI triage system by refining its components. In the first stage of the validation, emergency scenarios are simulated using both tabletop simulation and offline simulation based on the resource needs. This allows faults and strengths in the system to be diagnosed at an early stage in a controlled envi­ ronment. This theoretical framework is then translated to concrete emergency situations with limited resources in field pilot studies in order to investigate its impact on clinical practice and patient outcomes. Just some of the myriad of data points that are routinely collected and

Let the AI system produces a recommendation ̂yt for patient t with an

<!-- page 6 -->

analysed include clinical accuracy (ROC, precision), decision-making rate, resource utilization (bed and oxygen consumption) and human factors such as clinician trust, override rate and perceived utility. With this form of iterative review, the system can be modified continuously until it is acceptable, safe and effective before it is adopted more widely.

**Table 1 Simulation parameter specifications for the hybrid AI triage framework.**

Simulation Parameter Specification Value

Patient Heart Rate Range 50–150 bpm Patient Respiratory Rate Range 9–39 breaths per minute Patient Oxygen Saturation Range

72 %–99 %

### 3.8. About the dataset

(SpO2)

Blood Pressure (Systolic) Range 81–182 mmHg Body Temperature Range 35.3 ◦C–38.8 ◦C Glasgow Coma Scale Range 6–13 Comorbidity Count Range 0–3 Point-of-Care Lactate Range 0.5–2.9 mmol/L Time Since Arrival Range 23–173 min Beds Free Range 0–7 Oxygen Cylinders Free Range 0–8 Staff on Shift Range 1–5 Patients Waiting Range 2–24 Clinician Experience Range 0–23 years Clinician Workload Index Range 1–24 Self Confidence Score Range 1–4 NEWS-like Score Range 1–14 Risk Deterioration Probability

In order to create and assess the hybrid AI triage system, this study used a mixed dataset that included both artificially created data and actual patient cases. Fifteen patient examples with diverse clinical, de­ mographic, and contextual characteristics gathered from emergency healthcare settings with limited resources comprise the real-world sec­ tion. In order to improve model training and generalizability, adaptive oversampling techniques were used to produce synthetic data that supplemented underrepresented examples.

The dataset includes human aspects (clinician experience, workload, and confidence scores), contextual characteristics (staff count, oxygen and bed availability), and clinical variables (vital signs, symptoms, and laboratory markers such point-of-care lactate and comorbidity counts). Data sets containing a balance of genuine and synthetic instances were divided into training (60 %), validation (20 %), and test (20 %) sets. For research purposes, a sample of this combined actual and synthetic dataset is made publicly available at [23]. Subject to ethical approval, requests for access to the entire dataset can be sent to the authors.

0.89–0.99

Range

Resource Need Score Range 0.89–1.00 CNN Input Channels 7 (hr, spo2, rr, sbp, lactate, clinician exp, workload index) CNN Convolutional Layers 2 CNN Filters per Conv Layer 32, 64 CNN Kernel Size 3x3 CNN Activation Function ReLU CNN Fully Connected Layers 2 (units: 128, 64) CNN Output Layer Sigmoid (1 unit) CNN Dropout Rate 0.25 CNN Optimizer Adam CNN Training Epochs 5 CNN Batch Size 32 CNN Loss Function Binary Cross-Entropy

### 3.9. Clinical integration, safety, and conclusion

The proposed hybrid AI triage solution aims to integrate seamlessly into the existing clinical process of the emergency department, partic­ ularly a small-capacity one, to meet the needs. The system respects the clinical knowledge of physicians, while also helping to improve the accuracy of decisions and resource allocation by providing physician override options and interpretable, actionable triage suggestions. In accordance with existing frameworks for the safe deployment of digital health technologies, patient safety is given first priority through the continued monitoring of model performances, the identification of cognitive biases and the open communication of confidence levels and potential risks. Clinical confidence and regulatory compliance are further ensured through stringent validation procedures and adherence to ethical standards [1,24].

emergency contexts. Table 1 shows the Simulation Parameter Specifi­ cations. The experimental design was employed to examine the pre­ dictive accuracy, resource-aware optimization, human-in-the-loop interactions, and adaptive learning components in realistic clinical conditions, thereby confirming the usability and safety of the framework in settings such as those characteristic of emergency departments with limited resources.

A balance between model complexity and computational efficiency appropriate for emergency situations with limited resources served as the basis for the convolutional neural network’s (CNN) parameter se­ lection. In order to successfully capture pertinent temporal and spatial patterns within the multichannel input data without overfitting, the number of convolutional layers (2) and filters per layer (32, 64) were chosen based on preliminary tests. For such sensor data, a 3x3 kernel size is typical as it provides a good balance between computational burden and local feature extraction. ReLU activation functions were used since they have been shown to be effective in avoiding vanishing gradient issues, and dropout rate (0.25) was used to improve general­ ization by reducing the danger of overfitting in light of the small dataset size.

One of the limitations of the study is that the actual patient data is very limited and may not fully represent the diversity of emergency situations, even with the injection of synthetic data. Additionally, physician acceptance, as well as feedback quality (which may vary by setting) is key to the system’s effectiveness. Expanding in real-world data collection, enhancing human-in-the-loop interfaces to optimise participation by clinicians, and conducting large-scale, multi-centre clinical studies to validate safety and efficacy in various healthcare settings will be the primary objectives for future research. Sustained improvements in patient-centred treatment will be guaranteed by model upgrades and integration of novel AI fairness and transparency strate­ gies delivered frequently [25–27].

Because of its flexible learning rate characteristics, which provide steady and effective training convergence even with tiny batch sizes, the Adam optimizer was used. The five training epochs were empirically shown to produce steady validation accuracy without overfitting in pilot trials, and the batch size of 32 complies with hardware limitations and offers a realistic approximation of gradient updates. To fit the binary classification problem of triage risk prediction, the binary cross-entropy loss function was used.

## 4. Experimental setup and results

The hybrid AI triage model was tested in a controlled environment with a large dataset of 15 patient cases (varied clinical and demographic characteristics, such as lab results including point-of-care lactate, comorbidities, symptom profile, and vital signs [heart rate, respiratory rate, oxygen saturation]). Along with features related to resource availability (number of beds, oxygen cylinders, and staffing amount), contextual data also included variables related to the clinicians, such as experience, workload, and confidence rating. As a result of the diverse data, which reflected human nature and realistic constraints, the decision-making of the AI system was widely tested in various

Using box plots, in Fig. 3, the distribution of 15 main numerical parameters categorized by triage label as human factors (workload, clinical experience), background variables (available beds, oxygen cyl­ inders), and vital indicators (heart rate, respiratory rate) are shown. The

<!-- page 7 -->

**Fig. 3. Boxplots of patient, context, and human factor features by triage label.**

**Fig. 4. Histograms of select features stratified by triage label.**

wide spread of triage groups with workload indices varying from 1 to 24 and heart rates from roughly 50 to 150 bpm emphasises important factors that may impact upon triage decisions.

correlations (−0.65) between SpO2 and respiratory rate, as well as strong positive correlations (up to 0.85) between heart rate and respi­ ratory rate. These connections provide information for the interpreta­ tion of the model and feature selection for the triage framework.

Heart rate, oxygen saturation and available bed feature distributions are presented per triage category in Fig. 4 Histograms. For lesser acuity, heart rate peaks between 50 and 100 beats a minute, but in high-risk groups, the heart rate can reach 150 beats a minute. The average amount of oxygen saturation is between 75 and 99 %, with lower oxygen saturation more common in RED label instances. There are zero to seven bed places to be occupied, emphasising the impact of shortage of re­ sources on the triage result.

Fig. 6 shows the frequency of cognitive bias warnings given during triage. 13 of these instances have a value of “None”, meaning that there is typically no discernible bias. The “Other” category was used twice; conventional biases, such as “Availability” and “Anchoring” were not in any way triggered. These data suggest that most triage actions were free from any detectable cognitive bias since only a small percent of triage activities in this cohort were found to have non-anchoring, non-avail­ ability bias patterns.

The heatmap in Fig. 5, which displays Pearson correlation co­ efficients among 15 numerical characteristics, reveals strong negative

Fig. 7 illustrates the frequency of application of clinician-derived

<!-- page 8 -->

**Fig. 5. Correlation matrix of numerical features.**

**Fig. 6. Distribution of cognitive bias alerts.**

<!-- page 9 -->

**Fig. 7. Frequency of extracted clinician heuristics triggered.**

**Fig. 8. Training and validation accuracy and loss curves.**

heuristic criteria in different triage scenarios: “heuristic_low_spo2”, the most commonly applied rule, was applied nine times; “heuri­ stic_high_lactate” was interpolated in seven cases and “heuri­ stic_high_hr” in five cases. Using statistical tests, the rule-based architecture of the cognitive module is supported by the emphasis on the clinical relevance of the elevated lactate and hypoxia as common deci­ sion triggers rather than tachycardia.

trade-off between accuracy and recall for high acuity categorization. Precision is almost 100 % on low recall and falls to about 45 % on recall, going up to 100 %. The curve demonstrates the model’s ability to accurately identify all high-risk patients, which is critical for urgent emergency triage.

Fig. 11’s confusion matrix is a summary of the outcomes of this classification on 100 validation cases. Four false negatives, three false positives, forty-two true negatives and fifty-one true positives. This performance is restricted in regards to false non-high forecasts but provides high detection rate for the emergence of critical patients in emergency situations and with low resources. Fig. 12 plots mean ex­ pected probabilities against actual observed events in 11 probability bins. The close following of the calibration curve to the best diagonal line indicates the good calibration of risk assessments for the AI triage model. When correctly calibrated, probabilities that are anticipated can be trusted by physicians when making decisions in the face of uncertainty.

Fig. 8 shows the progress of the model’s training in 5 epochs. Training accuracy increases from 65 % to 95 % while validation accu­ racy increases from 60 % to 90 %. As a result, training loss is reduced from 0.9 to 0.25 and validation loss is reduced from 1.0 to 0.35. These trends show how well the AI triage model learns and generalizes in emergency situations and has shown steady performance gains and minimal overfitting.

The ability of the model to distinguish between high acuity situations during validation (100 samples) is shown by the receiver operating characteristic curve in Fig. 9. The curve indicates that it has a good balance between specificity and sensitivity with an estimated area under the curve (AUC) of 0.86. The method enables reliable triage prioritiza­ tion by precisely identifying patients in danger. Fig. 10 displays the

Fig. 13 shows the information about the bed, oxygen cylinder, and staff utilization rates before and during the resource-aware optimiza­ tion. Utilization was significantly increased with increased oxygen

<!-- page 10 -->

**Fig. 9. ROC curve for high-acuity detection.**

**Fig. 12. Calibration curve for prediction reliability.**

**Fig. 13. Resource utilization before and after optimization.**

**Fig. 10. Precision-recall curve.**

**Fig. 14. Changes in triage labels and transfer suggestions due to resource constraints.**

**Fig. 11. Confusion matrix demonstrating classification performance.**

<!-- page 11 -->

collaboration for emergency triage decision-making. The different con­ siderations that clinicians have when making overrides are shown in the pie chart in Fig. 18. Of these, 55 % of override reasons were for safety reasons, 20 % were related to patient preferences, 15 % were related to ancillary clinical information, and the other 10 % were for other

**Fig. 15. Computation time versus patient count for optimization algorithms.**

cylinders (60 %–85 %), beds (75 %–90 %) and staff (70 %–88 %). These improvements are good examples of how the optimization framework can be used to optimise scarce emergency resources. Fig. 14 shows how resource limitations affect the triage decisions for more than 100 pa­ tients. Of the 31 cases, 70 remained labelled, suggesting that adaptive decisions were made in resource-constrained environments, although 15 resulted in transfer recommendations, and 15 resulted in triage label downgrades.

**Fig. 17. Clinician override reasons for AI triage suggestions.**

Fig. 15 demonstrates the scaling of calculation time for integer programming and heuristic reinforcement learning optimizers as the load of patients increases. Because heuristic RL continues to work well and takes less than 3 s, it is possible to use it in large emergency rooms in real time. On the other hand, the time of integer programming increases strongly from 0.1 s for 10 patients to 25 s for 500 patients. Fig. 16 is a scatter plot of normalized demands for patient resources with respect to an availability criterion of 0.7. Green dots (60 % or so) indicate feasible allocations within capacity; red dots (40 % or so) indicate infeasible instances that cannot be managed without changes in management - it’s clear how optimization is important in supporting safe triage judgments within constraint.

Fig. 17 explains why doctors do not follow AI triage recommenda­ tions. Overrides were attributed to clinical judgment 45 %, contraindi­ cations 25 %, system issues 15 % and resource constraints 15 %. The results point to relevant considerations that affect human-AI

**Fig. 18. Distribution of clinician override rationales.**

**Fig. 16. Feasibility of resource allocation for emergency patients.**

<!-- page 12 -->

**Fig. 22. Effect of clinician feedback on system recommendations.**

**Fig. 19. Decision time comparison with and without AI support.**

**Fig. 20. Clinician survey feedback on AI triage system.**

**Fig. 23. False negative rate comparison between baseline and AI triage.**

**Fig. 21. Predictive accuracy and override reduction over pilot phases.**

reasons.

**Fig. 24. Reduction in delayed and inappropriate triage decisions.**

The bar chart in Fig. 19 shows how the use of AI-assisted triage makes the workflow more efficient by reducing the mean decision du­ rations from 180 s without AI assistance to 125 s with AI, an improve­ ment of 31 %. Fig. 20 shows In addition to high clinician trust (4.2/5) and usability (4.0/5), the moderate cognitive burden score of 2.3 in the survey meant acceptable acceptance and easy to manage mental stress when using the AI system in emergency situations.

suggestion changes decreases with each iteration of feedback, from 30 at the start until it is only 7 by the fifth cycle. This demonstrates how continuous adaptation is leading to the convergence of AI guidance and clinical competence.

Fig. 23 is a bar chart comparing the false negative rates (FNR) of significant patients under AI-assist triage with the conventional baseline triage. The AI system has shown a relative improvement of 58 % in FNR by reducing it from 12 % to 5 %. This is essential to improving patient safety and reducing the number of high acuity patients that are missed during an emergency. Fig. 24 below illustrates the dramatic reduction in delays and mis-triage through the use of AI. The proportion of delayed

The graph in Fig. 21 is a dual-axis line chart that depicts the enhancement of the system through input from clinicians and iterative learning showing the reduction of the rate of system overrides from 28 % to 10 % and the increase of predicted accuracy from 78 % in Phase 1–91 % in Phase 4. The line plot in Fig. 22 illustrates how the number of

<!-- page 13 -->

optimization was performed for low, moderate and high risk patients. High-risk patient bed utilization increased from 3.0 to 3.5 days, which is indicative of critical care priority, and low-risk bed utilization decreased, which is indicative of a more appropriate allocation of re­ sources to patient acuity. The bar chart in Fig. 26 shows the time saved on each of triage (5 min), decision-making (8 min), and transfer pro­ cesses (7 min) due to the integration of the AI system, which is important in terms of efficiency to promote ED throughput. This translates into a time saving of an average of 20 min.

Accuracy, Precision, Recall, and F1 Score and ROC AUC scores of the models of CNN, Logistic regression, and Random forest, each repre­ sented by different colors and hatch marks for better readability are shown in Fig. 27. Numerical labels are provided for comparison of scores. The CNN model performs better than other models in all metrics, showing better skill for triage decision making. These results are in agreement with the data in Table 2, which gives statistical values with 95 % confidence intervals and p-values for model comparison.

**Fig. 25. Resource utilization aligned with patient risk.**

### 4.1. Ablation study

To evaluate the contribution of each system component, we tested five model variants: (1) Baseline CNN with only clinical features, (2) Baseline + Clinician Features, (3) Baseline + Cognitive Module, (4) Baseline + Resource Optimizer, and (5) Full Hybrid System. All com­ ponents are shown in Table 3.

Cognitive module showed the greatest single improvement (5 % accuracy, p = 0.008), whereas clinician features contributed +3 % (p = 0.042). The main operational advantage of the resource optimizer was that the percentage of infeasible resource allocations was reduced from 18 % to 4 %. The whole system achieved an accuracy of 0.91, which confirmed synergistic effects above the components.

## 5. Conclusion

**Fig. 26. Workflow efficiency gains with AI triage support.**

This paper proposes an extensive hybrid AI triage architecture with a lightweight CNN-based prediction module, resource-aware optimiza­ tion, and human-in-the-loop cognitive modelling for low-resource emergency scenarios. With a ROC AUC of 0.94 (0.91–0.96) and a vali­ dation accuracy of 91 % (95 % CI: 88–94 %), the CNN was superior to random forest (accuracy 87 %, ROC AUC 0.88) and logistic regression (accuracy 83 %, ROC AUC 0.85). Strong predictive power with well- calibrated risk assessments is revealed by such key performance

decisions decreased from 18 % to 7 % and the proportion of inappro­ priate triage decreased from 15 % to 4 %, which indicates increased decision timeliness and correctness - two determinants required for efficient use of emergency resources.

Fig. 25 shows the average number of bed days before and after

**Fig. 27. Performance Metrics Comparison of Machine Learning Models in Emergency Triage Prediction.**

<!-- page 14 -->

**Table 2 Performance comparison metrics with confidence intervals and statistical significance for CNN, logistic regression, and random forest models in emergency triage prediction.**

Model Accuracy (95 % CI) Precision (95 % CI) Recall (95 % CI) F1-Score (95 % CI) ROC AUC (95 % CI) Brier Score (95 % CI) p-value (vs CNN)

CNN 0.91 (0.88–0.94) 0.89 (0.85–0.92) 0.90 (0.87–0.93) 0.90 (0.87–0.92) 0.94 (0.91–0.96) 0.07 (0.05–0.09) – Logistic Regression 0.83 (0.79–0.87) 0.81 (0.76–0.85) 0.82 (0.77–0.86) 0.81 (0.78–0.85) 0.85 (0.81–0.89) 0.12 (0.10–0.15) <0.001 Random Forest 0.87 (0.84–0.90) 0.86 (0.82–0.89) 0.85 (0.81–0.88) 0.85 (0.83–0.87) 0.88 (0.85–0.91) 0.10 (0.08–0.13) 0.002

interests or personal relationships that could have appeared to influence the work reported in this paper.

**Table 3 Ablation study results.**

## References

Model Variant Accuracy ROC AUC False Negative Rate p-value vs Baseline

[1] Da’Costa A, Teke J, Origbo JE, Osonuga A, Egbon E, Olawade DB. AI-driven triage Baseline CNN 0.83 0.87 9.5 % – Clinician Features 0.86 0.89 7.8 % 0.042 Cognitive Module 0.88 0.91 6.2 % 0.008 Resource in emergency departments: a review of benefits, challenges, and future directions. Int J Med Inf 2025:105838.

[2] Suamchaiyaphum K, Jones AR, Markaki A. Triage accuracy of emergency nurses: 0.85 0.88 8.1 % 0.126 an evidence-based review. J Emerg Nurs 2024;50(1):44–54.

[3] Butler K, Anderson N, Jull A. Evaluating the effects of triage education on triage Optimizer Full Hybrid 0.91 0.94 5.0 % <0.001 accuracy within the emergency department: an integrative review. Int Emerg Nurs 2023;70:101322.

[4] Abubshait L, Rizek J. Culturally Responsive Emergency Nursing: From Triage to System Discharge. J Emerg Nurs. 2025. https://doi.org/10.1016/j.jen.2025.04.017. S0099-1767(25)00161-8.

[5] El Arab RA, Al Moosa OA. The role of AI in emergency department triage: an parameters as accuracy (0.89), recall (0.90), and F1-score (0.90) (Brier score 0.07). Critical resource consumption was improved by up to 20 % using resource-aware optimization. Human-in-the-loop clinician inte­ gration led to better workflow efficiencies and trust through a reduction in rate of overrides and decision delay by 31 %. The reduction in false negative rates from 12 % to 5 % improved patient safety. The framework offers a scalable, interpretable, and clinically acceptable decision sup­ port system; however, the dataset’s size limits the model’s generaliz­ ability. Expanded multi-centre validation, as well as continuous model improvement, will be the focus of future research. integrative systematic review. Intensive Crit Care Nurs 2025;89:104058.

[6] Kingswell CJ, Calleja P, Sahay A. The Impact of Emergency Triage Practices on Patient Safety: A Scoping Review Protocol. J Emerg Nurs. 2025;51(3):498–503. https://doi.org/10.1016/j.jen.2024.12.002. Epub 2025 Feb 14. PMID: 39955670.

[7] Ilicki J. Challenges in evaluating the accuracy of AI-containing digital triage systems: a systematic review. PLoS One 2022;17(12):e0279636.

[8] Abbasi Dolatabadi Z, Zakerimoghadam M, Bahrampouri S, Jazini A, Nabi Foodani M. Challenges of implementing correct triage: a systematic review study. J Military Med 2022;24(2):1096–105.

[9] Mitchell R, O’Reilly G, Banks C, Nou G, McKup JJ, Kingston C, Cameron P. Triage systems in low-resource emergency care settings. Bull World Health Organ 2025; 103(3):204.

[10] Alsabri M, Oboli VN, Rath S, Tsoi V, Del Castillo Miranda JC, Alagarswamy K, CRediT authorship contribution statement Shehada W. Bridging the gap: lessons from low-resource pediatric emergency medicine for high-resource settings. Current Emerg Hospital Med Rep 2025;13(1): 10.

[11] Ahmed MM, Oweidat M, Okesanya OJ, Alaswad M, Abdelbar SMM, Gill P, E. Bhuvaneswari: Writing – review & editing, Writing – original draft, Data curation, Conceptualization. K.D.V. Prasad: Writing – original draft, Validation, Data curation, Conceptualization. Mohd Ashraf: Writing – original draft, Resources, Investigation, Conceptual­ ization. Sachin Jadhav: Writing – review & editing, Writing – original draft, Data curation, Conceptualization. TK Rama Krishna Rao: Writing – review & editing, Writing – original draft, Data curation, Conceptualization. Tirukoti Sudha Rani: Writing – review & editing, Writing – original draft, Validation, Formal analysis. Alsabri M. Barriers to pediatric emergency care in low-resource settings: a narrative review. Sage Open Pediatrics 2025;12. 30502225251336861.

[12] Margetis G, Ntoa S, Antona M, Stephanidis C. Human-centered design of artificial intelligence. In: Handbook of human factors and ergonomics; 2021. p. 1085–106.

[13] Xu W, Gao Z, Dainoff M. An HCAI methodological framework: putting it into action to enable human-centered AI. arXiv preprint arXiv:2311 16027 2023.

[14] Torkamaan H, Tahaei M, Buijsman S, Xiao Z, Wilkinson D, Knijnenburg BP. The role of human-centered ai in user modeling, adaptation, and personalization—models, frameworks, and paradigms. In: A human-centered perspective of intelligent personalized environments and systems. Cham: Springer Nature Switzerland; 2024. p. 43–84.

[15] Gao Z, Qi X, Zhang X, Gao X, He X, Guo S, Li P. Developing and validating an Ethics statement emergency triage model using machine learning algorithms with medical big data. Risk Manag Healthc Policy 2022:1545–51.

[16] Chen W, Linthicum B, Argon NT, Bohrmann T, Lopiano K, Mehrotra A, Ziya S. The This study was conducted in accordance with the Declaration of Helsinki and received ethical approval from Panimalar Engineering College. All procedures were performed in compliance with relevant laws and institutional guidelines of Panimalar Engineering College. effects of emergency department crowding on triage and hospital admission decisions. Am J Emerg Med 2020;38(4):774–9.

[17] Kang DY, Cho KJ, Kwon O, Kwon JM, Jeon KH, Park H, Oh BH. Artificial intelligence algorithm to predict the need for critical care in prehospital emergency medical services. Scand J Trauma Resuscitation Emerg Med 2020;28(1):17.

[18] Chee ML, Chee ML, Huang H, Mazzochi K, Taylor K, Wang H, Liu N. Artificial Written informed consent was obtained from all clinician partici­ pants prior to their involvement in cognitive task analysis interviews and pilot studies. All participants were informed of their right to with­ draw from the study at any time without consequence. The privacy rights of all human subjects were observed, and all data was anonymized to protect participant confidentiality. intelligence and machine learning in prehospital emergency care: a systematic scoping review. medRxiv 2023. 2023-04.

[19] Hosseini MM, Hosseini STM, Qayumi K, Ahmady S, Koohestani HR. The aspects of running artificial intelligence in emergency care; a scoping review. Archiv Academic Emerg Med 2023;11(1):e38.

[20] Agius S, Cassar V, Magri C, Khan W, Obe DAJ, Caruana G, Topham L. Predicting Emergency Severity Index (ESI) level, hospital admission, and admitting ward in an emergency department using data-driven machine learning. BMC Med Inf Decis Making 2025;25(1):281.

[21] Agius S, Cassar V, Magri C, Khan W, Topham L. Position paper: advocating for a Funding structured methodology in developing data-driven predictive models for healthcare–evidence from a large-scale national study. Health Technol 2025:1–7.

[22] Agius S, Cassar V, Bezzina F, Topham L. Leveraging digital technologies to enhance This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. patient safety. Health Technol 2025:1–11.

[23] Kadhiravan. Hybrid AI triage dataset for resource-constrained emergency care. Kaggle; 2025. https://www.kaggle.com/datasets/kadhiravanucet/hybrid-ai-triag e-dataset-resource-emergency-care. Declaration of competing interest The authors declare that they have no known competing financial

<!-- page 15 -->

[24] Abdalhalim AZA, Ahmed SNN, Ezzelarab AMD, Mustafa M, Albasheer MGA,

[26] Yi N, Baik D, Baek G. The effects of applying artificial intelligence to triage in the Ahmed REA, Albasheer Sr MGA. Clinical impact of artificial intelligence-based triage systems in emergency departments: a systematic review. Cureus 2025;17(6).

[25] Flott K, Maguire J, Phillips N. Digital safety: the next frontier for patient safety. emergency department: a systematic review of prospective studies. J Nurs Scholarsh 2025;57(1):105–18.

[27] Singhal A, Neveditsin N, Tanveer H, Mago V. Toward fairness, accountability, Future Healthcare J 2021;8(3):e598–601. transparency, and ethics in AI for social media and health care: scoping review. JMIR Med Inform 2024;12:e50048.
