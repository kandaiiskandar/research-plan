# Implementing Artificial Intelligence in Safety-Critical Systems during Operation: Challenges and Extended Framework for a Quality Assurance Process

> **Source PDF:** `Implementing Artificial Intelligence in Safety-Critical Systems during Operation: Challenges and Extended Framework for a Quality Assurance Process.pdf` · **Pages:** 8 · Converted by `scripts/paper2md.py` from the original PDF.

<!-- page 1 -->

Implementing Artificial Intelligence in Safety-Critical Systems during Operation: Challenges and Extended Framework for a Quality

IECON 2024 - 50th Annual Conference of the IEEE Industrial Electronics Society | 978-1-6654-6454-3/24/$31.00 ©2024 IEEE | DOI: 10.1109/IECON55916.2024.10906021

Assurance Process

1st Niclas Flehmig NTNU, Norwegian University of Science and Technology

2nd Mary Ann Lundteigen NTNU, Norwegian University of Science and Technology

Trondheim, Norway niclas.flehmig@ntnu.no

Trondheim, Norway mary.a.lundteigen@ntnu.no

3rd Shen Yin NTNU, Norwegian University of Science and Technology

Trondheim, Norway

shen.yin@ntnu.no

data input and a continuous data stream, and to improve safety-related systems. This research area of implementing AI in safety-critical systems is still evolving, necessitating further research [2]. A major step forward for implementing AI in safety-critical systems was a recently published technical report by the International Standardization Organization (ISO) and the International Electrotechnical Commission (IEC) on the topic of AI and functional safety [3]. Moreover, the European Union introduced an AI act that classifies AI to its risk and assigns additional obligations to the developers and users of high-risk AI systems. Part of the obligations of developers is the monitoring of the performance of AI after deployment as well as including human oversight of the AI during operation. According to this AI act, most of the safetycritical systems would fall into the high-risk category of AI systems [4]. Much research in the past has focused on AI and machine learning without considering the safety-critical system aspect. However, this research can be used as a foundation for developing integrated AI in safety-critical systems that fulfill the requirements and safety regulations. The challenges for AI in safety-critical systems during operation in comparison to other applications are potentially the same but the requirements and obligations during implementation and deployment are stricter to ensure the safety of the AI and consequently the broader system. One issue for AI in safety-critical systems revolves around quality assurance during real-world AI deployment, ensuring that the model maintains its behavior which was observed and tested during training. Additionally, guaranteeing that the AI operates within an acceptable performance range throughout its deployment is crucial. Common challenges for AI during operation are outliers, concept drift, adversarial attacks and not sufficient training data [5], [6]. There are countermeasures for challenges like outlier detection [7], [8]

Abstract—Implementing artificial intelligence (AI) in safetycritical systems comes with challenges that are also common in the implementation of AI in other domains. However, the consequences are distinct due to the inherent nature of safetycritical systems, where failure can lead to potential harm to people and the environment. This necessitates special consideration in AI design. When deploying AI in safety-related systems, it is necessary to ensure that the AI’s performance aligns with its training results and remains within acceptable bounds during operation to uphold the system’s safety. This paper focuses on addressing the quality assurance of AI during operation within safety-critical systems. Through a literature review and analysis, we aim to provide a comprehensive overview of common challenges encountered during operation and propose an extended framework of the ISO/IEC TR 5469 for a quality assurance process of AI within safety-critical systems. The extension adds monitoring of the AI component and a component for updating the AI, as well as several adjustments that are connected to those additions. As part of the monitoring, we introduce an indexing framework for the degradation of AI, based on a traffic-light design. The results, together with a comprehensive road map for future work, provide a foundation for further research and developing a holistic quality assurance of AI during operation.

Index Terms—Artificial intelligence, safety-critical systems, quality assurance

## I. INTRODUCTION

Mistakes by AI technology such as large language models, as in [1], are potentially annoying or may require a second verification through a reliable source when we use them as an assistant for simple tasks. However, they are harmless in contrast to mistakes in other applications, e.g. safety-critical systems. A safety-critical system describes a system where a failure can cause potential harm to people or the environment. For AI in this field, the regulatory standards are high to ensure a safe operation and protect from potential harm through AI misbehavior. The purpose of AI in this field is to handle more complex safety-critical systems, e.g., with high-dimensional

<!-- page 2 -->

Scholar to access also more recently published papers since the field of AI in safety-critical systems is still evolving. During the review process, we also used publications on the application of AI in healthcare, distinct from the application discussed in [3], which handles safety-critical systems for electrical, electronic, and programmable electronic technologies. We assume that this is appropriate given that healthcare can be seen as a high-risk application for AI, as noted in [13] and [4]. Therefore, similar regulations apply to both. Moreover, typical challenges in the deployment of AI in healthcare, e.g. imbalanced data and non-stationary data environment, are also common for safety-critical systems [2], [3], [12]. The challenges connected to the degradation of AI during the operation were conducted with keywords such as degradation of AI, concept drift, and temporal generalization of AI. Data drift was excluded since depending on the literature, it can be used interchangeably with concept drift. Reference [14] was to our knowledge the only relevant publication stating not data as the main driver for AI degradation but the models. This phenomenon was included in the list of challenges. The possible techniques collected to address these challenges included also detectors and countermeasures for concept drift [9]–[11]. Concerning the countermeasures, model updating such as lifelong or continual learning methodologies and re-training were identified. The terms, lifelong learning and continual learning are regarded as interchangeable in [15], [16]. A limitation regarding lifelong learning is the phenomenon known as catastrophic forgetting [11], [14]–[18]. This is relevant for understanding the degradation of AI performance and was therefore a part of the literature review [19]. To get a perspective on the performance measures for AI during operation the topics of monitoring of machine learning and monitoring of AI were investigated [18], [20]–[23]. In [18], [22], [23], the authors mention also outlier or anomaly detection as a part of the monitoring process. This topic was covered by two comprehensive journal articles [7], [8]. Subsequently, through an analysis of the collected content and thorough discussions, we developed an extension to the existing framework of ISO/IEC TR 5469 in which we focus on the quality assurance process for AI in safety-critical systems during operation with an additional framework for the indexing of AI performance degradation. The potential implementation environment we are aiming for is non-stationary. Therefore, we focus on challenges like concept drift and outliers as well as other challenges connected to nonstationary environments as suggested in [5], [6]. By using the term model updating, we refer to online and offline training techniques that aim to update and improve the AI in response to a non-stationary environment.

or concept drift [9]–[11]. However, the framework of ISO/IEC TR 5469 does not cover the process of quality assurance of AI within safety-critical systems during operation. Therefore, we conduct challenges and related countermeasures of AI during operation and propose an extended framework to tackle this challenge holistically. Additionally, we developed a framework for indexing the degradation of AI to increase the understanding of the output of the AI monitoring. We want to develop an AI assistant that collaborates with the human operator to enhance the safety of the system and augment the operator’s capabilities. This work is organized as follows: in Section II, we provide the methods we used to conduct the literature review and to develop the extended framework for the quality assurance process of AI during operation and the framework for indexing the AI degradation. In Section III, we present the results of the review and our developed extended framework. In Section IV, we discuss the results, in Section V, we provide a conclusion and a road map for further research.

## II. METHODS

The motivation, as well as a foundation for the research of this paper, has been the recently published technical report ISO/IEC TR 5469 [3]. The technical report is a joint effort by working groups within functional safety and AI within the ISO and the IEC. ISO/IEC TR 5469 can be regarded as a first step towards a unified approach by the industry in how to apply AI for safety-critical systems. It is evident from their work that the incorporation of AI in safety-critical systems can be seen as a complex problem. Therefore, in this paper, we have selected one particular problem which we strongly believe will be among the more central ones:

How to perform quality assurance of AI that is incorporated in safety-critical systems during operation.

A first comprehensive review on the topic of AI in safetycritical systems was written in 2022 [2], followed by a second comprehensive review paper [12]. Relevant challenges for implementing AI have also been pointed out in [5] and [6]. These papers have identified that trained AI systems may experience performance degradation during the operation even with high performance demonstrated during the learning stage. Such a degradation will be of high importance to manage and mitigate as part of the qualification assurance of AI systems. The causes of performance degradation are typically inadequate training data, adversarial input, and concept and data drift. Since the focus is on the operation stage, only concept drift and data drift were selected for further literature review. This is appropriate because inadequate training data can be located in the data acquisition stage and adversarial input may be covered in the data acquisition and learning stage. Furthermore, we assume that the training data is adequate and that adversarial inputs are tracked down by cybersecurity during operation. The main sources for the literature review were Web of Science to ensure the quality of the publications combined with Google

## III. RESULTS

In this section, we present the key findings from our analysis of the literature and an extended framework for a quality assurance process of AI during operation. In general, this framework aims to provide a foundation for implementing a

<!-- page 3 -->

three stages: the general detection of the concept drift, the understanding to determine when the drift occurred, how severe the drift is and where it happened, and the last stage the adaption to decide on how to react to the drift [9], [10]. The most common challenge for this process relates to the complete absence of labels, scarce availability of labels, or delayed availability of labels [5], [9]–[11]. Additionally, many methods cannot predict drift, resulting in detection only after the drift has occurred. This delay in detection can potentially lead to degradation in the AI component’s performance until it is updated to the occurred drift [9]. [9]–[11] suggest concrete techniques for concept drift and evaluate some of them in terms of drawbacks and advantages. The authors of [14] introduce the phenomenon of temporal degradation of AI that cannot be fully explained by concept drift in the underlying data but within the models themselves. This degradation may occur gradually over time, escalate abruptly or emerge in other degradation patterns. Different models trained on the same training and test set showed completely different behavior at a certain point in time and after that which indicates ”[...] temporal model quality depends on the choice of the ML model, and the model stability on a certain set of data” [14]. However, a suggested solution for both phenomenons is model updating which implies re-training or lifelong learning [5], [6], [9]–[11], [14]. Re-training is considered an offline approach for model updating which means the model trains on either all or a part of historical data up to the point in time of re-training. This becomes a challenge when the data stream produces a lot of data that necessitates the storage of it for later re-training [15], [25]. Moreover, there are increased computational expenses due to large-scale models with big data [25]. However, [25] states that more data does not always guarantee better performance, as smaller models trained on less data can sometimes outperform larger models. So, there has to be found a good balance. Another problem is to determine a time to trigger the re-training, e.g. considering the downtime of the AI component or determining an appropriate threshold value for when re-training is needed [14]. Lifelong learning aims to overcome the aforementioned challenges of re-training and provides a way for models to adapt to a non-stationary environment. It is categorized as an online learning approach that learns to improve sequentially over a data stream [15]. However, an inherent challenge of lifelong learning is called stability-plasticity dilemma. Plasticity describes the ability to integrate new knowledge into the model while stability is about retaining previous knowledge. This is related to the effect of catastrophic forgetting that describes the effect of a model ”forgetting” its previously learned task when it learns a new task [19]. This leads potentially to poor generalization of the model. There are methods like cross-validation and dropout algorithms in neural networks to mitigate the effect [19] but it remains a challenge [15]–[17], [25]. Re-training usually overcomes catastrophic forgetting but at the price of inefficiency due to requirements of memory usage and computational expenses. Furthermore,

quality assurance process for AI in safety-critical systems during operation. This includes maintaining the AI performance during operation within an acceptable range and enabling operators to respond effectively by using adequate methods. Furthermore, we propose an indexing framework to evaluate the severity of AI performance degradation and the necessity for the supervisory component to interfere.

A. Results of the Literature Review

The analysis of ISO/IEC TR 5469 [3] identifies developers as well as future owners and users as the main target audience. The technical report recognizes that the objectives of developers and users may vary, ranging from full reliance on AI for executing safety functions to the use of AI as an integral part of an extended architecture with also supervisory and conventional backup safety system or as development tools incorporating AI e.g., code generation or testing. For this purpose, ISO/IEC TR 5469 has introduced a classification scheme for AI consisting of four levels (A, B, C, D) and three classes (Class I, II, III). Depending on the usage the AI gets classified within a certain level along the first axis of the scheme, e.g. Level A1 describes an AI ”[...] in a safety-relevant E/E/PE system [and] where automated decision-making of the system function using AI technologies is possible” [3]. Along the second axis, the AI is assigned to a class that represents the degree to which the AI was developed and reviewed within the existing International Standards for functional safety. An AI with usage level A1 and class III, for example, cannot be developed and implemented using existing functional safety standards [3]. Therefore, obtaining approval for industrial use can be challenging. This must kept in mind when incorporating AI in safety-critical systems. In Fig. 1, it is shown that the safety-related system consists of three main components: an AI component, a supervisory component, and a backup safety system. The AI component can consist of one or several AI models that can work in an ensemble strategy, e.g. majority vote on the output. The input for the safety-related system is a data stream that is generated by the controlled system and the environment. The output is an action to maintain the safe state of the safety-critical system. As mentioned in Section II, one focus is on the concept drift which is mentioned as a challenge not just in terms of AI in safety-critical systems [2], [3] but in general in the literature on deploying machine learning in real-world applications [5], [6]. Concept drift refers to an unpredictable change in the distribution of the data during operation [10]. According to [10], there are three different sources of concept drift:

• Virtual drift describes a drift in the input data with no effect on the decision boundary;

• Actual drift describes a drift in the conditional probability distribution which affects the decision boundary;

• A mixture of the first two types. Moreover, there are four ways concept drift may appear, i.e. sudden drift, gradual drift, incremental drift, and recurring drift. For a more detailed explanation of the different types, we refer to [24]. The concept drift problem is split into

<!-- page 4 -->

it hinders updating the model as it relies predominantly on old, potentially outdated data [16], [25]. A lot of methods also assume an independent and identical distribution but a data stream will likely not provide such a distribution [15]. The data stream can be also imbalanced which necessitates techniques such as oversampling to handle this issue [11]. References [15]–[17], [25] address these challenges within lifelong learning, e.g. learning from the biological system as an inspiration [16], comparing different methods and suggesting desiderata for an ideal continual learning approach [15] or proposing new online learning approaches [25]. The technical report [3] from the ISO limits the use of online learning approaches to only AI that is not part of a safety function nor has an impact on it. Besides model updating, monitoring the AI component is also essential for the quality assurance of the performance of the AI [18], [20], [21], [23]. A monitoring process generates information about the overall performance of the component and the impact of the updating. When AI models are deployed in the real world, which naturally often differs from their training environment, a certain drop in model performance is expected. Additionally, in non-stationary environments, the performance of static AI models tends to deteriorate progressively, necessitating ongoing monitoring [18], [21]. Transparency and explainability are helpful for the output of the monitoring to make decisions understandable but the implementation can be complex and an improvement in terms of explainability is not guaranteed [20], [23]. For the monitoring, the high dimensionality of input data within a data stream can be challenging in terms of computation [20] and there may be latency between the prediction of the model and the target variable [18], [23], both leading to a delay in measuring performance degradation. Additional aspects to the aforementioned challenges are described in some of the studies, i.e. an organizational structure for monitoring AI [18], open source tools to handle the challenges in monitoring [23], and an additional challenge noted in [20] is the system dependency meaning external libraries and software, as well as potential dependencies on the output of other AI models or from data sources which can be part of an external or internal pipeline with limited control and transparency. A broader definition of monitoring can include more than evaluating the AI component’s performance and the impact of the updating, by incorporating concept drift detection and understanding [18], [20], [23]. A common challenge of concept drift and monitoring the AI’s performance is the limited availability of labels [18], [23]. This is also a challenge for outlier detection which is also part of the monitoring process [18], [22], [23]. An outlier or anomaly represents a data instance that is extremely off the underlying distribution [7]. A common phenomenon for datasets from safety-critical systems is the under-representation of a certain class, i.e., rare safetycritical events. This is usually solved by oversampling the underrepresented class during the learning stage. However, in data streams, this can interfere with the outlier detec-

tion if imbalanced data is not sufficiently considered in the model updating process. The monitoring could misinterpret an imbalanced class as an outlier [5]. Additionally, some detection methods suffer from limitations in handling data streams or they tend to be computationally expensive [7]. Various potential methods to detect outliers, as well as their pros and cons, are mentioned in [7], [8]. Reference [22] suggests to evaluate the monitors, i.e., algorithms implemented for performance monitoring, before their implementation. In their study, they benchmarked various monitoring methods for image classifiers and concluded that the overall accuracy of those monitors was inadequate. They predicted a high amount of false positives and false negatives which negatively affects the system by interfering with correct predictions of the model.

B. Extended Framework and Indexing of AI Degradation

A qualitative analysis of sociotechnical risks and resilience linked to the implementation of AI in healthcare provided helpful support for the development of the extended framework of the ISO/IEC TR 5469 [13]. This extended framework represents a quality assurance process for AI in safety-critical systems during operation. The extension adds two components:

• Monitoring of the AI component;

• updating of the AI component. Together with the two additions, further minor changes are introduced in the safety-related system. Fig. 1 shows the extended framework from [3] with all the new parts colored blue. Firstly, the extension affects the data stream by adding operational constraints that are provided to the supervisory component as well as the backup safety system. Secondly, the data stream is transformed into operational data for the backup safety system, if necessary. An adjusted simplex architecture based on [26] is added to the switch component to enable the human operator, who is part of the non-AI supervisory component, to seamlessly switch to the backup safety system, ensuring continuous oversight and intervention in case of an AI misbehavior or degradation in the performance. Once the AI performance is restored, the operator can transition back to the AI control, maintaining operational efficiency and safety protocols. Detection methods for outliers and concept drift are part of the monitoring of the AI. The concept drift detection includes also the understanding of the underlying concept drift. This means generating information about the time, cause, and location of the drift in the data. Moreover, general performance metrics are suggested to measure the confidence, accuracy, and robustness of the AI component as well as a relative error that measures the degradation after the implementation. This information is provided to the supervisory component that evaluates its content and makes a decision. The monitoring of AI is implemented without AI, using statistical methods or other non-AI technologies. The use of AI in this component, for instance for outlier detection, must be considered carefully. The second component is the updating of the AI. It consists of

<!-- page 5 -->

Ensemble strategy (e.g. voting

AI component (perform safety function)

Limiting

system)

logic

AI monitoring (non-AI) (detect outliers & concept

drift, measure performance, create index

Operational data for AI

of AI degradation)

enforce restrictions on outputs to prevent unsafe behavior

component

Output: Action to maintain safe state

Switch (adjusted

Supervisory component

(non-AI) (detect unsafe pattern in

simplex

Operational constraints

architecture)

fault detection/AI degradation; command to switch to backup system

input data, evaluate

monitoring)

Operational

trigger retraining & decide on strategy

data for

Backup safety system

back-up

(non-AI) (passive, deterministic logic or human task, focus

system

on transition to a safe

Data stream from controlled system and environment

(degraded) state only)

Online safety-related system

Output: Re-trained AI component to replace current component

AI updating (provide dynamic memory & various updating strategies)

Offline updating

**Fig. 1. Extended framework of the ISO/IEC TR 5469. Extensions are marked with blue color and represent the proposed quality assurance process during operation. Adopted from [3].**

a re-training method that provides an offline learning approach outside of the safety-related system. We suggest a re-training with small batches to save memory storage. A dynamic evaluation, as in [25], can be used as an appropriate approach to select an adequate re-training data set that does not need all the historical data and find the right distribution between old and recent data. This is important because the relevance of recent data varies depending on the nature of changes in the underlying data distribution. In some cases, recent data holds greater relevance, while in others, a balanced mix or a greater emphasis on older data may be better. Depending on the underlying data, methods for semi-supervised learning must be considered as well to handle scarce labeling. Furthermore, a structured plan for the re-training process ensures no unwanted behavior is learned through the training and it provides some documentation regarding regulations. The supervisory component decides on the timing of re-training and the strategy, as different root causes of performance degradation necessitate distinct updating approaches. The new re-trained AI component potentially replaces the current AI component in the safety-related system. The main idea of this extension is to handle the different challenges regarding the performance of AI during the operation and the potential shortcomings of some methods by a holistic approach. Holistic, because various challenges and countermeasures are included in a broader concept and are handled simultaneously. Moreover, the human operator is empowered as supervisor to ensure safe operation, leverage

also the acceptance of the end users and increase trust. The AI acts rather as an assistant than an autonomous tool.

To enhance the understanding of the output generated by the AI monitoring for the supervisory component, a preliminary indexing framework was developed. This framework, as seen in Fig. 2, adopts a traffic-light design consisting of three levels, each representing a different degree of severity of AI performance degradation or changes in the underlying data. Additionally, it provides actionable recommendations to each level. The input parameters for the indexing framework are derived from a set of performance metrics including confidence, accuracy, and robustness of the AI component, as well as data-driven indicators such as outlier and concept drift detection. These parameters are weighted based on their overall impact on AI degradation or misbehavior, taking into consideration both their general influence and the severity of the occurrence. For instance, a 5 % decrease in confidence is indexed with a lower weight than a 10 % decrease and the detection of a single outlier is also indexed with a lower weighting factor than a substantial concept drift. By implementing these weights, along with predefined rules and conditions, the system computes a total score resulting in one of the three severity levels. The goal of the implemented framework is to leave out AI technologies and fully rely on non-AI technologies to monitor the AI component. If those non-AI technologies do not provide adequate performance, the use of AI must be considered. Level 1 is represented by the color green, indicating that the

<!-- page 6 -->

AI monitoring (non-AI)

Level 3:

AI degradation surpassed safety threshold value

and/or significant change in underlying data

Performance

• Switch to conventional safety controller • Check and analyze of root cause of alarm • Re-training recommended

metrics (confidence, accuracy etc.)

Trained AI

component

Level 2:

AI shows sign of performance degradation and/or

Supervisory

Weighted

change in underlying data

Outlier detection

component

index

• Stay on AI as safety function • Check on AI model and data distribution • If necessary re-training or other adjustments

Data stream

Concept drift

Level 1:

detection

AI shows no sign of significance degradation

• Stay on AI as safety function • Regular checks on data distribution and AI model

**Fig. 2. Framework for an indexing of AI degradation in a traffic-light design. The indexing is part of the monitoring of the AI that gets input from the AI component and the data stream and generates an output for the supervisory component.**

AI component is functioning adequately as the safety function, and it is recommended to have it in control. Nevertheless, routine checkups of both the AI component and the data distribution are recommended to ensure continued reliability and safety. At the first sign of performance degradation, shifts in the underlying data distribution, or various anomalies within the data, the traffic light switches to orange, indicating Level 2. Despite this, it is still recommended to rely on the AI component as the safety function within the safety-related system. However, the supervisory component is mandated to conduct thorough checks on the AI component, analyze the data distribution, and investigate potential root causes for the alarm. If the necessity is given, a re-training or other adjustments must be introduced. At Level 3, the AI component’s performance exceeds the recommended safe range or there is a rapid and substantial change in the underlying distribution. In this scenario, control of the safety-related system should be transferred to the conventional non-AI safety controller. The supervisor is tasked with analyzing the root cause of the alarm and initiating appropriate countermeasures, i.e. re-training. The indexing of degradation alongside the traffic-light feedback aims to assist the human operator in managing the system and making informed decisions.

investigation to achieve more comprehensive development of their parts and to refine specific methodologies. We also need to determine the best approach for managing the AI component consisting of multiple models in an ensemble strategy. Should we monitor and update each model individually or treat them collectively as one AI component? While individual monitoring and updates provide detailed insights and precise fixes for specific models, this method can become complicated with a larger number of models. Moreover, it is important to note that this extension primarily focuses on quality assurance during operation, excluding considerations related to data acquisition, model training and selection, and the broader system integration. Nevertheless, these proposals serve as initial frameworks to open up further discussions and provide a basis for the development of more refined tools in the future. In general, there is a gap in the literature on frameworks and detailed real-world studies on monitoring and addressing the degradation or failure of AI during operation within safetycritical systems, particularly considering the regulations on the usage of AI. There is a need for further research in this specialized field, approached holistically. The explicit challenges must be identified and analyzed, along with appropriate countermeasures to address them effectively. This comprehensive understanding is essential for ensuring the safety, reliability, and regulatory compliance of AI technology within safety-critical systems. Moreover, insights into implemented AI in safety-critical systems in real-world settings are important to better understand its operations, limitations, and potential solutions. Relying solely on simulations or experimental data may not fully capture the complexities and nuances of real-world scenarios. One promising approach is the use of ”shadow” models, that operate alongside the traditional system without impacting

IV. DISCUSSION The traffic-light design for indexing AI degradation represents a first draft of the communication from the quality assurance process to the human operator. To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner. This approach offers a practical way of communicating the AI performance and providing actionable feedback to the operator to ensure a continued safe state of the system. The proposed extended framework for a quality assurance process and the indexing of AI degradation necessitate additional

<!-- page 7 -->

the broader system. This makes it possible for the AI to receive real input and produce real output, allowing for direct comparison and evaluation against the traditional system. This enables researchers to analyze AI in a safety-related system in a sandbox-like setup where the integrity of the operational system is maintained. By leveraging such methodologies, we can enhance our understanding of AI behavior in a practical context and develop more robust and reliable solutions. The availability of labeled data poses a challenge, as realworld data is often unlabelled, partially labeled, or subject to delays in labeling. Adopting a holistic approach to AI during operation amplifies the impact of challenges associated with unlabelled or delayed data on the different monitoring methods, i.e. concept drift detection, outlier detection, and model performance evaluation. The fields of unsupervised and semi-supervised learning are evolving to address these issues. However, there is still a gap and real-time labeling of high-dimensional data streams by a human operator represents an almost impossible challenge. This challenge is particularly crucial in safety-critical systems, where timely access to labeled data is necessary for effective AI monitoring. Delays in labeling can result in a lag in the detection of unsafe behavior of AI or AI degradation, potentially leading to adverse consequences. For monitoring the AI in safety-related systems, we aim for non-AI technologies. This preference stems from the technical report ISO/IEC TR 5469 [3], where introducing an additional AI can lead to more regulations and monitoring. Instead, nonAI technologies are favored for the monitoring task. However, the advantage of AI lies in its capabilities that surpass those of non-AI technologies. Thus, a balance between leveraging AI’s advantages and minimizing its limitations through monitoring by non-AI technologies must be investigated. There is a gap in the research to analyze the trade-off between using AI in safety-critical systems and implementing non-AI methods to monitor and constrain it. An additional part of the monitoring component can be explainable AI (XAI). This method seeks to make the outputs of AI systems more understandable for humans and therefore increases trust but also helps to improve the AI systems. Integrating XAI into the proposed monitoring, as a separate part or part of the indexing framework, has the potential to further empower the human operator by providing them with deeper insights and a better understanding of the AI’s output. This can lead to better decision-making and can give the operator valuable knowledge to identify potential improvements to the AI component.

sive analysis of relevant literature on the topics of AI in safetycritical systems, deploying AI, and the related challenges and countermeasures, i.e. monitoring of AI, concept drift, outlier detection, model updating, and catastrophic forgetting. This emphasized the necessity for a holistic approach to ensure the performance of AI during operation. Therefore, we proposed an extended framework for a quality assurance process that integrates detecting techniques as well as countermeasures that are mentioned in the literature. We added two components to the framework, namely AI component monitoring and AI component updating. Alongside those components, we made some minor adjustments in the framework, i.e. adjusted simplex architecture, operational constraints and transformation of the data stream. Overall, we provide a holistic approach to quality assurance of AI during operation. Moreover, we developed a new framework for indexing the degradation of AI that makes the output of the monitoring more understandable for the operator. Using a traffic-light design to communicate with the human operator aims to increase the interpretability of the AI monitoring decision and to enhance acceptance by providing a user-friendly interface. Recommended actions included in this are also helpful for the operator. With these frameworks, we aim to provide the first input to develop a quality assurance process for AI in safety-critical systems during operation. The extended framework and the underlying process stand out in the conducted literature that either reviewed the general implementation of AI in safetycritical systems with its challenges and potential solutions [2], [3], [12] or focuses on the deployment of AI excluding issues related to safety-critical systems [5], [6] without any comprehensive idea on the quality assurance during operation. The remaining literature predominantly addresses specific challenges, such as concept drift, rather than tackling the quality assurance during operation in a holistic manner including a supervisory component and an adapted simplex architecture. There is a necessity to conduct further research in the realm of AI within safety-critical systems. This includes investigating how to develop and implement AI technologies in compliance with regulations while enhancing the safety-related system. For instance, there is a need to investigate effective offline learning approaches to update the AI models, especially in cases where online learning is difficult to implement within certain usage levels. Furthermore, prioritizing the development and implementation of AI assistants over fully autonomous systems can facilitate easier compliance with regulatory requirements and increase the acceptance of AI technologies in safety-critical systems. By focusing on AI assistants, that work together with human operators, the regulatory burden can be managed more effectively, while fostering trust and confidence in AI as part of safety-related systems. Our future work seeks to evaluate and further improve the quality assurance process based on the proposed framework and to integrate the indexing of AI degradation. Therefore, both frameworks must be analyzed, and adequate methods must be chosen. Moreover, we want to deploy an AI alongside

## V. CONCLUSION AND FURTHER WORK

The recently published technical report ISO/IEC TR 5469 [3] from the ISO marked the first step of the industry to propose a unified approach for the way of applying AI to safety-critical systems. However, it also underlines the several challenges that come along with the incorporation of AI in such systems. This work focused on the quality assurance of AI during operation. Therefore, we conducted a comprehen-

<!-- page 8 -->

the quality assurance process in a safety-related system as the next phase of our research. Another area of interest for our research involves addressing the challenge of delayed or partially labeled data, necessitating the use of semi-supervised learning techniques. These represent real-world scenarios for data streams in safetycritical systems, making them crucial to investigate within this context. Furthermore, investigating the use of non-AI technologies as safety measures for AI technologies and assessing the extent to which they constrain AI capabilities without compromising its inherent advantages.

[13] Macrae, Carl. “Managing Risk and Resilience in Autonomous and

Intelligent Systems: Exploring Safety in the Development, Deployment, and Use of Artificial Intelligence in Healthcare.” Risk Analysis, January 21, 2024, risa.14273. https://doi.org/10.1111/risa.14273. [14] Vela, Daniel, Andrew Sharp, Richard Zhang, Trang Nguyen, An

Hoang, and Oleg S. Pianykh. “Temporal Quality Degradation in AI Models.” Scientific Reports 12, no. 1 (July 8, 2022): 11654. https://doi.org/10.1038/s41598-022-15245-z. [15] Delange, Matthias, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia,

Ales Leonardis, Greg Slabaugh, and Tinne Tuytelaars. “A Continual Learning Survey: Defying Forgetting in Classification Tasks.” IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021, 1–1. https://doi.org/10.1109/TPAMI.2021.3057446. [16] Parisi, German I., Ronald Kemker, Jose L. Part, Christopher Kanan,

and Stefan Wermter. “Continual Lifelong Learning with Neural Networks: A Review.” Neural Networks 113 (May 2019): 54–71. https://doi.org/10.1016/j.neunet.2019.01.012. [17] Pianykh, Oleg S., Georg Langs, Marc Dewey, Dieter R. Enzmann,

ACKNOWLEDGMENT

Christian J. Herold, Stefan O. Schoenberg, and James A. Brink. “Continuous Learning AI in Radiology: Implementation Principles and Early Applications.” Radiology 297, no. 1 (October 2020): 6–14. https://doi.org/10.1148/radiol.2020200038. [18] Feng, Jean, Rachael V. Phillips, Ivana Malenica, Andrew Bishara, Alan

This work was carried out as a part of SUBPRO-Zero, a Research Centre at the Norwegian University of Science and Technology. The authors gratefully acknowledge the project support from SUBPRO-Zero, which is financed by major industry partners and NTNU.

E. Hubbard, Leo A. Celi, and Romain Pirracchio. “Clinical Artificial Intelligence Quality Improvement: Towards Continual Monitoring and Updating of AI Algorithms in Healthcare.” Npj Digital Medicine 5, no. 1 (May 31, 2022): 66. https://doi.org/10.1038/s41746-022-00611-y. [19] Goodfellow, Ian J., Mehdi Mirza, Da Xiao, Aaron Courville, and

## References

Yoshua Bengio. “An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks.” arXiv, March 3, 2015. http://arxiv.org/abs/1312.6211.

[20] Schr¨oder, Tim, and Michael Schulz. “Monitoring Machine Learn-

[1] Berglund, Lukas, Meg Tong, Max Kaufmann, Mikita Balesni, Asa Cooper Stickland, Tomasz Korbak, and Owain Evans. “The Reversal Curse: LLMs Trained on ‘A Is B’ Fail to Learn ‘B Is A.’” arXiv, September 22, 2023. http://arxiv.org/abs/2309.12288.

[2] Ashmore, Rob, Radu Calinescu, and Colin Paterson. “Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges.” ACM Computing Surveys 54, no. 5 (June 30, 2022): 1–39. https://doi.org/10.1145/3453444.

[3] ISO/IEC TR 5469:2024. “Artificial Intelligence — Functional Safety ing Models: A Categorization of Challenges and Methods.” Data Science and Management 5, no. 3 (September 2022): 105–16. https://doi.org/10.1016/j.dsm.2022.07.004.

[21] Allen, Bibb, Keith Dreyer, Robert Stibolt, Sheela Agarwal, Laura Coombs, Chris Treml, Mona Elkholy, Laura Brink, and Christoph Wald. “Evaluation and Real-World Performance Monitoring of Artificial Intelligence Models in Clinical Practice: Try It, Buy It, Check It.” Journal of the American College of Radiology 18, no. 11 (November 2021): 1489–96. https://doi.org/10.1016/j.jacr.2021.08.022.

[22] Ferreira, Raul Sena, Jean Arlat, Jeremie Guiochet, and Helene Wae- and AI Systems.” International Organization of Standardization, 2024. https://www.iso.org/standard/81283.html.

[4] EU AI Act. “European Union Artificial Intelligence Act.” European Union, 2024. https://artificialintelligenceact.eu/ai-act-explorer/.

[5] Gomes, Heitor Murilo, Jesse Read, Albert Bifet, Jean Paul Bard- selynck. “Benchmarking Safety Monitors for Image Classifiers with Machine Learning.” In 2021 IEEE 26th Pacific Rim International Symposium on Dependable Computing (PRDC), 7–16. Perth, Australia: IEEE, 2021. https://doi.org/10.1109/PRDC53464.2021.00012.

[23] Klaise, Janis, Arnaud Van Looveren, Clive Cox, Giovanni Vacanti, dal, and Jo˜ao Gama. “Machine Learning for Streaming Data: State of the Art, Challenges, and Opportunities.” ACM SIGKDD Explorations Newsletter 21, no. 2 (November 26, 2019): 6–22. https://doi.org/10.1145/3373464.3373470.

[6] Paleyes, Andrei, Raoul-Gabriel Urma, and Neil D. Lawrence. “Chal- and Alexandru Coca. “Monitoring and Explainability of Models in Production,” 2020. https://doi.org/10.48550/ARXIV.2007.06299.

[24] Gama, Jo˜ao, Indr˙e ˇZliobait˙e, Albert Bifet, Mykola Pechenizkiy, and Abdelhamid Bouchachia. “A Survey on Concept Drift Adaptation.” ACM Computing Surveys 46, no. 4 (April 2014): 1–37. https://doi.org/10.1145/2523813.

[25] Lazaridou, Angeliki, Adhiguna Kuncoro, Elena Gribovskaya, Devang lenges in Deploying Machine Learning: A Survey of Case Studies.” ACM Computing Surveys 55, no. 6 (July 31, 2023): 1–29. https://doi.org/10.1145/3533378.

[7] Smiti, Abir. “A Critical Overview of Outlier Detection Methods.” Computer Science Review 38 (November 2020): 100306. https://doi.org/10.1016/j.cosrev.2020.100306.

[8] Bl´azquez-Garc´ıa, Ane, Angel Conde, Usue Mori, and Jose A. Lozano. “A Review on Outlier/Anomaly Detection in Time Series Data.” ACM Computing Surveys 54, no. 3 (April 30, 2022): 1–33. https://doi.org/10.1145/3444690.

[9] Lima, Marilia, Manoel Neto, Telmo Silva Filho, and Roberta A. Agrawal, Adam Liska, Tayfun Terzi, Mai Gimenez, et al. “Mind the Gap: Assessing Temporal Generalization in Neural Language Models.” arXiv, October 26, 2021. http://arxiv.org/abs/2102.01951.

[26] Phan, Dung T., Radu Grosu, Nils Jansen, Nicola Paoletti, Scott A. Smolka, and Scott D. Stoller. “Neural Simplex Architecture.” In NASA Formal Methods, edited by Ritchie Lee, Susmit Jha, Anastasia Mavridou, and Dimitra Giannakopoulou, 12229:97–114. Lecture Notes in Computer Science. Cham: Springer International Publishing, 2020. https://doi.org/10.1007/978-3-030-55754-6 6. De A. Fagundes. “Learning Under Concept Drift for Regression—A Systematic Literature Review.” IEEE Access 10 (2022): 45410–29. https://doi.org/10.1109/ACCESS.2022.3169785.

[10] Lu, Jie, Anjin Liu, Fan Dong, Feng Gu, Joao Gama, and Guangquan Zhang. “Learning under Concept Drift: A Review.” IEEE Transactions on Knowledge and Data Engineering, 2018, 1–1. https://doi.org/10.1109/TKDE.2018.2876857.

[11] Su´arez-Cetrulo, Andr´es L., David Quintana, and Alejandro Cervantes. “A Survey on Machine Learning for Recurring Concept Drifting Data Streams.” Expert Systems with Applications 213 (March 2023): 118934. https://doi.org/10.1016/j.eswa.2022.118934.

[12] Wang, Yue, and Sai Ho Chung. “Artificial Intelligence in Safety-Critical Systems: A Systematic Review.” Industrial Management & Data Systems 122, no. 2 (February 1, 2022): 442–70. https://doi.org/10.1108/IMDS07-2021-0419.
