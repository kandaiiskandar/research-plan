# Situation-aware recommender systems- a systematic review and framework for trustworthy recommendations

> **Source PDF:** `Situation-aware recommender systems- a systematic review and framework for trustworthy recommendations.pdf` · **Pages:** 38 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Artificial Intelligence Review (2026) 59:101 https://doi.org/10.1007/s10462-026-11503-y

## Situation-aware recommender systems: a systematic review and framework for trustworthy recommendations

Luca Aliberti1 · Giuseppe D’Aniello1 · Matteo Gaeta1

Received: 19 August 2025 / Accepted: 17 January 2026 / Published online: 29 January 2026 © The Author(s) 2026

Abstract Over the past decade, recommender systems have become pivotal across digital platforms, supporting tasks such as media choice, e-commerce navigation, industrial decision sup­ port, and personalized learning. By analyzing user behaviors and preferences, modern engines enable filtering, ranking, and adaptive interaction at scale. A recent research trend concerns situation-aware recommenders, that are systems able to perceive and interpret surrounding conditions to adapt their output and anticipate user goals. These systems are increasingly shaped by the need for transparency, reliability, and alignment with trust­ worthy AI principles. Despite growing interest, the literature lacks a clear conceptual definition of “situation”, a distinction from “context”, and unified models, design guide­ lines, and evaluation frameworks for truly situation-aware recommenders. Consequently, only a limited subset of deployed solutions integrates situation awareness in an explicit and systematic way. This work presents a systematic review and classification of modern situation-aware recommender systems, highlighting the most used techniques, domains of application, open issues, and research challenges. The review follows the PRISMA meth­ odology for systematic literature studies. The analysis is completed with the proposal of a reference framework grounded in Endsley’s three-level Situation Awareness model and aligned with emerging principles of trustworthy AI. The architecture is used to identify key challenges and outline research directions in the field. It also serves as a comparative lens for existing work and as a blueprint intended to guide the development of the next generation of transparent, reliable, and human-centered recommender systems.

Keywords Situation awareness · Recommender systems · Context awareness · Systematic review · Trustworthy AI

Luca Aliberti, Giuseppe D’Aniello and Matteo Gaeta have contributed equally to this work.

Extended author information available on the last page of the article

<!-- page 2 -->

## 101 Page 2 of 38

L. Aliberti et al.

## 1 Introduction

Recommender Systems (RSs) have become fundamental to the operation of modern digi­ tal platforms, substantially influencing user attention and revenue generation. For instance, Netflix reports that approximately 80% of viewing hours are shaped by its personalised recommendation pipeline (Gomez-Uribe and Hunt 2015), while large-scale systems used by Google, across services such as YouTube and Google Play, integrate contextual factors such as device, time, and location to provide personalised and context-aware content to billions of users (Covington et al. 2016; Cheng et al. 2016).

Independent market analyses further show that RSs substantially impact user engage­ ment, decision-making processes, and business value across multiple industries (Jannach and Jugovac 2019). In addition to improving conversion rates and long-term retention, RSdriven personalisation shapes how users navigate information-rich environments, influenc­ ing exposure to content, products, and services.

Given this economic and societal relevance, RSs increasingly need to move beyond static preference estimation and adapt to users’ evolving objectives, constraints, and situational demands. This shift calls for more adaptive, situation-aware approaches, where recommen­ dations are sensitive not only to long-term preferences but also to the user’s immediate goals and environment.

Enhancing relevance, acceptability, and explainability requires systems that can adjust their behaviour to the user’s current situation and anticipated needs. Such goal-oriented, sit­ uation-aware models can respond proactively to changes in context, thereby strengthening user trust and engagement. At the same time, advances in artificial intelligence, particularly in deep learning, have greatly expanded the modelling capacity of RSs and, over nearly a decade, have enabled increasingly refined representations of latent preferences and behav­ ioural patterns. However, these gains come with growing opacity: the internal reasoning of large neural architectures often remains inaccessible to users, regulators, and even system designers.

To mitigate this opacity, Situation Awareness (SA), originally introduced by Endsley (1995), offers a theoretical lens that organises the decision process into perception, compre­ hension, and projection. When embedded into RS workflows, this structure can provide an interpretable scaffold that facilitates the tracing, explanation, and partial auditing of system behaviour, thereby helping to temper the black-box nature of modern neural architectures.

To preserve long-term trust, future RSs must also incorporate humans in the loop not only as passive recipients but as supervisory agents capable of interpreting, questioning, and influencing system behaviour. Here, “human in the loop” refers to mechanisms that enhance interpretability, enable informed oversight, and allow user feedback to refine or contest automated inferences, supporting operators and consumers within the system interaction.

Within the RS literature, different approaches incorporate environmental and contex­ tual factors. Context-Aware Recommender Systems (CARS) enrich classical methods with observable cues such as time, location, device, or social setting. Situation-Aware Recom­ mender Systems (SARS), instead, aim to infer a coherent situational state that captures the user’s goals, constraints, and environmental conditions, grounding the recommendation logic in this higher-level synthesis.

In such systems, trustworthiness becomes a critical requirement. As SARS often oper­ ate in time-sensitive, goal-critical, or high-stakes contexts, their situational reasoning must

<!-- page 3 -->

Page 3 of 38 101

Situation-aware recommender systems: a systematic review and…

be transparent, reliable, and aligned with user values. Trustworthy Recommender Systems (TRSs) extend beyond accuracy, encompassing explainability, fairness, privacy, robust­ ness, and controllability (Wang et al. 2024; Ge et al. 2024). These dimensions are essen­ tial to ensure that situational recommendations remain effective, accountable, and socially responsible.

The boundary between context and situation, however, is often unclear in RS research; many systems labelled situation-aware perform little more than contextual filtering, while others implement complex situation inference without reference to SA theory.

To clarify this grey zone, a systematic survey is conducted to disentangle context from situation in RS research, map current SARS works onto Endsley’s SA framework, and anal­ yse how situational information is gathered, represented, and exploited across domains. Building on this analysis, a reference framework is proposed that integrates SA with the principles of trustworthy recommender systems outlined by Wang et al. (2024). SA prin­ ciples are used to guide the modelling and exploitation of situational information, while trustworthiness dimensions serve as safeguards to ensure that recommendations remain interpretable, reliable, and ethically aligned.

The remainder of the article is organised as follows. Section 2 introduces the theoretical foundations of SA and the RS paradigms of CARS and SARS. Section 3 reviews existing surveys and highlights the lack of a comprehensive treatment of situation awareness. Sec­ tion 4 describes the PRISMA-based research methodology. Sections 5, 6 and 7 synthesise current SARS research, covering information types, integration strategies, algorithms, and application domains. Section 8 analyses the reviewed literature, identifying converging themes, research gaps, and emerging directions. Section 9 presents the SA-inspired, trustoriented framework. Finally, Sect. 10 discusses open challenges and Sect. 11 summarises the main findings.

## 2 Background

In this section, an overview is provided on two fundamental concepts for this survey: Situ­ ation Awareness and Recommender Systems, particularly Context-Aware Recommender Systems (CARS) and Situation-Aware Recommender Systems (SARS).

### 2.1 Situation awareness

Situation Awareness (SA) has been defined by Endsley as “the perception of the elements of the environment within a volume of time and space, the comprehension of their meaning, and the projection of their status in the near future” Endsley (1995).

This definition of SA is structured on three levels:

1. Perception perceiving the status of the environment, such as attributes and dynamics of the relevant elements, usually through sensors. 2. Comprehension understanding what perceived data means in relation to goals. 3. Projection predicting how the current situation will evolve and identifying the poten­ tial future states of the system.

<!-- page 4 -->

## 101 Page 4 of 38

L. Aliberti et al.

These three levels should not be interpreted as separate or strictly sequential steps, because each level influences the others during the situation awareness process. In this context, “good” SA does not simply mean having high values along these three levels, but rather achieving an adequate quality of each cognitive function: good Perception implies correctly detecting the relevant elements without omissions or noise; good Comprehension implies accurately integrating those elements into a meaningful assessment aligned with current goals; and good Projection implies being able to anticipate plausible future states of the environment. Maintaining adequate SA across these levels is essential for making informed decisions and interacting effectively with systems. Furthermore, as discussed in Sect. 7.4, several works explicitly investigate how SA (both Human Situation Awareness and Com­ puter Situation Awareness) can be measured through dedicated evaluation strategies, pro­ viding concrete operational tools for assessing the quality of SA in practical systems.

In fact, as also discussed in the work of D’Aniello et al. (2022), it is important to dif­ ferentiate the concept of Human Situation Awareness (HSA) from the concept of Computer Situation Awareness (CSA).

Kokar et al. (2009) provided a differentiation between these two ideas, which separates the two categories of SA. In particular, they recognize:

● The process by which a human operator becomes aware of a situation is known as Hu­ man Situation Awareness (HSA). The well-known model proposed by Endsley (1995), which describes the cognitive processes by which a human perceives, comprehends, and projects the state of the environment, is usually used to describe this. ● Computer Situation Awareness (CSA), which instead describes the capacity of auton­ omous agents or computer systems to comprehend the current situation. In this case, the subject executing the SA procedure is an artificial agent or machine rather than a human.

From the perspective of this survey, and in alignment with the framework introduced later, greater emphasis is placed on CSA. As discussed in Sect. 9, the proposed framework is designed to enhance both user and system awareness by adapting its behavior to each user’s characteristics and goals, recognizing that these goals shape and are shaped by specific situ­ ations perceived and interpreted differently across individuals.

### 2.2 Context-aware and situation-aware recommender systems

Recommender Systems (RSs) are tools and algorithms intended to predict user preferences and suggest relevant items, such as products, services, or content, based on historical inter­ action data. Traditional approaches, as discussed by Mateos and Bellogín (2024), include:

● Collaborative Filtering, which leverages similarities among users or items to generate recommendations. ● Content-Based Filtering, which models item attributes and matches them to user pro­ files. ● Hybrid Methods, which combine data from both collaborative and content-based mod­ els.

<!-- page 5 -->

Page 5 of 38 101

Situation-aware recommender systems: a systematic review and…

Context-Aware Recommender Systems (CARS) extend traditional RSs by incorporating additional information about the user’s environment, such as time, location, device, or social context, into the recommendation process (Adomavicius and Tuzhilin 2011). Context can be injected at various stages:

1. Pre-filtering, where the candidate item set is pruned according to contextual constraints. 2. Post-filtering, where an initial ranking is reordered using context signals. 3. Contextual Modeling, where context variables are included directly in the predictive model.

Empirical studies have demonstrated that conditioning recommendations on contextual fac­ tors reduces ambiguity in user preferences and improves overall accuracy (Villegas et al. 2018; Mateos and Bellogín 2024). On the other hand, Situation-Aware Recommender Systems (SARS) seek to advance beyond context aggregation by inferring high-level situations, which are semantic con­ structs capable of capturing the user’s current goals or anticipated needs, starting from multiple context features and sensor streams (Dötterl et al. 2017; Richthammer and Pernul 2020). In a typical SARS, raw context signals (e.g., time, location, physiological data) are fused into a situation (e.g., “commuting,” “in a meeting,” “on a lunch break”). The inferred situation drives both candidate selection and ranking, ensuring that recommendations align with the user’s immediate objectives while remaining tailored to their personal profile.

However, in the current literature, the distinction between CARS and SARS remains blurred: many systems termed “situation-aware” rely on simple context combinations, while others perform situational inference without explicit separation from context model­ ing. Clarifying this boundary is one of the primary goals of this survey and may provide a stronger conceptual foundation for SARS research, stimulating the design of more adaptive, goal-oriented, and trustworthy recommendation strategies.

## 3 Related works

The field of recommender systems has made great progress since the introduction of contex­ tual information, which has been used to improve recommendations and has led to the defi­ nition of a new type of recommender system, also known as context-aware recommender systems (CARS).

Different studies have highlighted the potential of adding contextual aspects, such as time, place, and social context, to improve suggestion relevance and accuracy (Villegas et al. 2018; Mateos and Bellogín 2024; Kulkarni and Rodd 2020).

Interest in CARS has gradually increased over time. Numerous studies have been con­ ducted to provide systematic reviews of CARS applications. For example, Villegas et al. (2018) defined context-aware recommendation processes based on recommendation strate­ gies, context integration methodologies, and the stages at which context is introduced within recommender systems. Similarly, the survey carried out by Mateos and Bellogín (2024) examined evaluation methodologies, incorporation methods, and context representation in CARS. Other surveys, such as the one conducted by Kulkarni and Rodd (2020), focused on

<!-- page 6 -->

## 101 Page 6 of 38

L. Aliberti et al.

specific techniques, including bio-inspired computing and statistical computing approaches used in recent CARS research.

Although several surveys on CARS exist, to the best of current knowledge, there are no surveys that specifically address Situation-Aware Recommender Systems (SARSs). This is mainly due to the lack of a clear distinction between the concepts of context and situation within recommender systems, an issue explored further in Sect. 5. The idea behind situation awareness in recommender systems is that CARS enhance recommendations by incorporat­ ing contextual factors, while SARS go one step further by comprehending the user’s overall situation.

This perspective considers the broader context in which a user interacts with a system, extending beyond isolated contextual elements. For example, the work proposed by Feng et al. (2009) was one of the first to underline the need for software adaptability in response to various contextual cues, introducing the concept of situation awareness for context-aware decision support systems. Dötterl et al. (2017) instead focused on integrating situation awareness into recommender systems and proposed an approach to make conventional rec­ ommendation methods situation-aware, arguing that selecting relevant scenarios is crucial to the effectiveness of recommendation computation. Richthammer and Pernul (2020) fur­ ther clarified the distinction between situation awareness and context awareness by defining situation awareness as the system’s ability to comprehend the user’s present personal situ­ ations through the integration of different kinds of contextual input. They proposed a situa­ tion awareness model for recommender systems and outlined general design procedures for developing situation-aware recommender systems.

This survey is proposed to fill the current gap in the literature regarding comprehen­ sive reviews of SARS. In doing so, the distinction between Context-Aware Recommender Systems (CARS) and SARS is clarified, providing precise definitions of both concepts and examining how they are incorporated into recommendation strategies. A reference frame­ work is also proposed to organize and support the development of SARSs.

## 4 Research methodology

This section details the methodological approach adopted for this survey on SARS. In par­ ticular, the survey focuses on articles published between 2009 and 2025, and was conducted following the guidelines of the PRISMA statement Page et al. (2021).

### 4.1 Rationale

The rationale behind this study stems from the growing interest in using SA principles, and in general situational information, within recommender systems. While numerous sur­ veys have been conducted on traditional context-aware recommender systems, fewer works explicitly address the integration of situational information or fully embrace SA. By adopt­ ing the PRISMA methodology, this survey aims to ensure a systematic review that:

● Captures how SA has been framed and used within recommender systems. ● Identifies the shift from context-awareness to situation awareness, analyzing whether existing works follow recognized SA models.

<!-- page 7 -->

Page 7 of 38 101

Situation-aware recommender systems: a systematic review and…

● Maps and categorizes existing SARS in terms of the techniques used, domains of ap­ plication, and outcomes achieved.

### 4.2 Research questions

This review examines how context and situation are conceptualised in recommender sys­ tems, how situational information and SA principles are integrated into recommendation processes, and which types of information, techniques, and application domains character­ ise SARS research. In addition, it investigates which datasets are commonly adopted and which evaluation metrics, both for Computer SA and Human SA, are used to assess these systems. Specifically, the Research Questions (RQs) in this survey are:

● RQ1 What differentiates context from situation within RS? ● RQ2 What is the most used contextual and situational information in RS? ● RQ3 How is situational information integrated within SARS to influence or guide the recommendation process? ● RQ4 Which are the most used techniques to generate recommendations in SARS? ● RQ5 What are the most common application domains in which SARS are used? ● RQ6 Which datasets are used in SARS, and what types of data characteristics enable the modelling of situations? ● RQ7 Which evaluation protocols and metrics are used in SARS, and to what extent do they assess Computer SA (algorithmic performance) versus Human SA (users’ situ­ ational understanding and decision quality)?

### 4.3 Search strategy

In accordance with PRISMA guidelines, a systematic search strategy was developed to identify all relevant studies. Peer-reviewed journal articles and conference proceedings from 2009 to 2025 were targeted. The following databases were consulted: Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and ScienceDirect.

A search query was designed to reflect the interest in both SA and recommender systems:

(“situation awareness” OR “situational awareness” OR “sit­ uation-aware”) AND

(“recommendation system*” OR “recommender system*”)

The query was slightly adjusted per database requirements (e.g., searching in titles, abstracts, and keywords). An initial set of potentially relevant publications was collected from each source and merged into a single repository after removing duplicates using the criteria below.

### 4.4 Eligibility criteria

Inclusion and exclusion criteria were established to systematically filter the literature and retain only contributions directly relevant to SARS. These criteria were designed to ensure

<!-- page 8 -->

## 101 Page 8 of 38

L. Aliberti et al.

conceptual relevance, by focusing on studies addressing situation awareness beyond basic contextual adaptation, and methodological robustness, by including only peer-reviewed works within the target time frame.

Inclusion Criteria

● Studies focusing on a recommender system that explicitly reference or integrate SA or situational information into the recommendation process. ● Studies providing a definition of or distinction between context and situation from a recommender systems perspective. ● Studies featuring actual SA constructs (e.g., references to Endsley’s model or demon­ strable use of situation beyond basic context).Exclusion Criteria

● Language different from English. ● Duplicate entries across databases. ● Non-peer-reviewed studies (e.g., extended abstracts, preprints without formal review). ● Full text not available. ● Studies not published between 2009 and 2025. ● Studies that do not propose any kind of recommender system. ● Studies that do not use or discuss situational information within the recommendation process. ● Studies mentioning SA only superficially (e.g., only in title or abstract) without demon­ strating actual integration into the recommendation methodology.

### 4.5 Study selection

Figure 1 shows the flow diagram used to select studies in accordance with PRISMA guide­ lines. The initial search across the five selected digital libraries yielded a total of 159 records: 82 from Scopus, 50 from Web of Science, 19 from IEEE Xplore, 4 from ACM Digital Library, and 4 from ScienceDirect.

In the first step, 99 records were removed before screening due to duplication (n = 87) or other reasons (e.g., inaccessible full text, dataset papers, slides; n = 12). This left 60 records for the initial screening phase.

During the first screening, titles, abstracts, and keywords were independently analyzed. The inclusion decision was based on whether the article proposed or discussed a recom­ mender system that explicitly incorporated situational information or SA principles. Follow­ ing the inclusion and exclusion criteria, articles selected by at least one reviewer proceeded to the next stage, resulting in 42 articles.

In the final screening, full texts of the 42 articles were assessed for eligibility. Nine articles were excluded because they either: (i) did not include a recommender system, (ii) used situational information in a superficial way, or (iii) mentioned SA without integrating it into the core methodology.

Ultimately, a total of 34 studies were deemed eligible and included in this survey. These studies form the basis for the analysis presented in the subsequent sections with respect to the aforementioned research questions.

<!-- page 9 -->

Page 9 of 38 101

Situation-aware recommender systems: a systematic review and…

**Fig. 1 Diagram of the literature review selection process according to the PRISMA guidelines**

## 5 What is the difference between context and situation?

To frame the academic debate on context and situation, it is useful to start from commonlanguage definitions. The Cambridge Dictionary provides the following:

● Context: “The situation within which something exists or happens, and that can help explain it.”1

● Situation: “A condition or combination of conditions that exist at a particular time.”2

These definitions already hint at a potential overlap: the word “situation” appears in the definition of “context,” underscoring how these two notions can be intertwined. Over the years, many researchers have attempted to clarify or disambiguate them, as shown below.

1 ​h​t​t​p​s​:​/​/​d​i​c​t​i​o​n​a​r​y​.​c​a​m​b​r​i​d​g​e​.​o​r​g​/​d​i​c​t​i​o​n​a​r​y​/​e​n​g​l​i​s​h​/​c​o​n​t​e​x​t.

2 ​h​t​t​p​s​:​/​/​d​i​c​t​i​o​n​a​r​y​.​c​a​m​b​r​i​d​g​e​.​o​r​g​/​d​i​c​t​i​o​n​a​r​y​/​e​n​g​l​i​s​h​/​s​i​t​u​a​t​i​o​n.

<!-- page 10 -->

## 101 Page 10 of 38

L. Aliberti et al.

### 5.1 Context versus situation

As noticeable from the dictionary definitions themselves, providing accurate definitions for the concepts of context and situation is challenging.

Context One of the earliest definitions dates back to 1999, provided by Abowd et al. (1999), and later refined by Dey (2001), where context is defined as: “any information that can be used to characterize the situation of an entity, where an entity can be a person, place, or physical or computational object.”

This definition has been widely recognized and reused by the scientific community. In 2007, Zimmermann et al. (2007), starting from the aforementioned definition of context, provided two extensions:

● Formal Extension: introducing a formal structure for context information, grouping it into five categories (Individuality, Activity, Location, Time, Relationships) to facilitate the modeling of a context model. ● Operational Extension: focusing on the dynamic nature of context and its use in in­ teraction with context-aware systems, including transitions between contexts, sharing contexts among multiple entities, and shifting attention.

As evidenced by the literature, the concept of context has been extensively studied and uti­ lized in numerous context-aware systems.

Nevertheless, given the subtle semantic line between the words context and situation, inconsistencies and confusion about the use of the term “situation” emerged. Many works use the terms interchangeably, making a clear definition essential.

Situation One of the first works addressing the concept of situation was conducted by Dey (2001), where the author acknowledged that contextual information facilitated the development of many applications, yet introducing the concept of situation could be beneficial. The author defined situation as “a description of the states of relevant entities.”

Subsequently, many works delved deeper into this concept. For instance, Baumgartner and Retschitzegger (2006), following Dey’s work, stated that context information character­ izes the situations of objects relevant for an agent. The aggregation of all context informa­ tion, the complete context of an agent, can be regarded as the single situation the agent is involved with.

They argued that situations exist at a higher abstraction level compared to individual contextual information.

Difference As highlighted in the analyzed literature, context and situation differ significantly in their abstraction and usage within context-aware and situation-aware systems.

According to Ye et al. (2012), context is structured information derived from sensor data, describing specific properties of the environment or user. Contextual data is typically lowlevel, specific, and directly measurable.

In contrast, a situation represents a more abstract, goal-oriented interpretation of con­ textual data. Ye et al. (2012) defined a situation as “the external semantic interpretation of sensor data,” assigning meanings to data from the application’s or user’s perspective.

<!-- page 11 -->

Page 11 of 38 101

Situation-aware recommender systems: a systematic review and…

Kim and Kim (2009) emphasized that situations imply understanding both phenomena and associated actions.

Thus, while context refers to immediate, low-level environmental or user-specific data, situations provide higher-level cognitive constructs aimed at meaningful interpretations guiding decision-making in dynamic environments (D’Aniello et al. 2022).

### 5.2 Context awareness versus situation awareness

To further clarify the distinction between context and situation, the related concepts of con­ text awareness and situation awareness are examined, which have been debated and often used interchangeably.

Context Awareness The concept of context awareness was first introduced by Schilit and Theimer (1994) to develop applications capable of adapting dynamically to their environments. According to Nwiabu et al. (2011), a system is considered context-aware when it exploits contextual information to deliver relevant and adaptive services. This idea gained importance with the diffusion of mobile computing.

Situation Awareness The most recognized definition of Situation Awareness (SA) is provided by Endsley (1995). According to Nwiabu et al. (2011), SA involves cognitive processes used by opera­ tors to understand their current state and anticipate future changes. Baumgartner and Retsch­ itzegger (2006) describe SA as offering a “bird’s eye view” of multiple relevant situations.

Alcaraz and Lopez (2013) emphasized that SA concerns the interpretation of seman­ tic knowledge about broader conditions experienced by an application domain at a given moment.

Difference A clear distinction exists between context awareness and situation awareness. Context awareness is typically lower-level, focusing on adaptations to specific environmental fea­ tures. Situation awareness provides a higher-level semantic interpretation of broader states Nwiabu et al. (2011), Alcaraz and Lopez (2013). Baumgartner and Retschitzegger (2006) suggest that context awareness can be seen as a subset within the broader framework of situation awareness.

### 5.3 A recommender system perspective

The previous sections clarified the distinction between the concepts of context and situa­ tion and examined the difference between context awareness and situation awareness. The analysis now shifts to the literature selected through the PRISMA methodology, examining how these works address situation awareness in recommender systems.

Many studies use the concepts of context and situation interchangeably, while only a limited number provide explicit distinctions.

As shown in Table 1, a common theme across the selected studies is that context aware­ ness deals with elementary data (e.g., time, location, environmental conditions), while situ­ ation awareness involves the higher-level interpretation of this data to infer the user’s actual condition. For example, Dötterl et al. (2017) regard context as a collection of punctual data (e.g., “12:00 PM”, “location X”), while the situation is seen as an understanding of

<!-- page 12 -->

## 101 Page 12 of 38

L. Aliberti et al.

**Table 1 Works on recommender systems providing an explicit distinction between context and situation**

References Main approach Context definition

```math
Situation 
definition
Dötterl et al. 
(2017)
```

Architec­ tural model differentiating contextual data and situational understanding

Individual environmental factors (e.g., time, location)

Capability to perceive and predict the impact of these factors on preferences

```math
Richtham­
mer and 
Pernul 
(2020)
```

```math
Fusion of such 
variables into 
a complex 
state affecting 
recommendations
Casillo et al. 
(2025)
```

Model introduc­ ing situation awareness as a “semantic scenario”

List of contex­ tual variables

Cultural recom­ mendation system based on IoT data and probabilistic models

Environmental data (location, time, etc.)

Interpretative and predictive exten­ sion of such data to personalize the experience

```math
Bouzeghoub 
et al. (2009)
```

```math
Inferred state 
(e.g., “at the of­
fice, lunch break”) 
used to drive 
recommendations
Li et al. 
(2025)
```

Mobile recom­ mendation approach in a campus setting

Any informa­ tion character­ izing the user at a given moment

Pluggable situation-aware recommendation module

Static attribute representation of users/items

“Precondition” for user-item interac­ tion, managing dynamic impact on preferences

how such information affects user preferences. Similarly, Richthammer and Pernul (2020) emphasize that “situation” should not be treated as a mere collection of attributes, but rather as a semantic fusion of these into meaningful scenarios. Casillo et al. (2025) differentiate between environmental data (context) and the predictive, interpretative phase (situation), while Bouzeghoub et al. (2009) define context as any basic information and the situation as a derived state. Finally, Li et al. (2025) propose treating the situation as a “precondition” for interactions in recommendation modules, thus separating it from the static modeling of users and items.

From this analysis, it can be observed that in a Situation-Aware Recommender Sys­ tem, context is the set of raw, immediately observable descriptors surrounding a user at a given moment. It includes sensor readings (heart rate, ambient light), device logs (running app, network strength), static attributes (age, language), and environmental facts (location, weather). Context is low-level, fleeting, and irrespective of any particular goal; it states what is happening around the user without yet indicating why it matters.

A situation, instead, is the high-level, goal-oriented interpretation of contextual snap­ shots. By selecting the most relevant cues, interpreting them with respect to the user’s current goals, and adding a qualitative assessment (e.g., “commuting and short of time”, “relaxing after work”), the system turns raw context into an actionable concept. Situations are semantic and purposeful: they explain why the current context is important, predict nearfuture constraints, and steer both data-driven and goal-driven recommendation strategies.

For example, the same context—“11:00 AM, at home”—may correspond to entirely dif­ ferent situations: for a night-shift worker it could mean “still sleeping” or “about to have

<!-- page 13 -->

Page 13 of 38 101

Situation-aware recommender systems: a systematic review and…

breakfast”, while for a day-shift worker it might imply “preparing lunch” or “taking a midmorning break”.

## 6 How situational information is used within SARS

Over the last 15 years the CARS community has converged on a reasonably shared vocabu­ lary and definitions that specify (i) which elements count as contextual, and (ii) how those elements can be used in the recommendation workflow.

What contextual information is used? Early works focused almost exclusively on spatio-temporal cues, but successive surveys broadened the lens. For example, Villegas et al. (2018) identify five recurrent dimensions: Individuality, Location, Time, Activity, and Relationships. The authors showed that these five facets cover the vast majority of variables reported in empirical studies. On the other hand, Casillo et al. (2025), working in the cultural-heritage domain, reinterpret the same facets through the well-known 5W+1 H schema (Who, What, Where, When, Why, How), thereby highlighting the role of user intentions (Why) and interaction modalities (How) alongside the more classical “where/when” signals.

Mateos and Bellogín (2024) introduce three orthogonal properties: acquisition mode, observability, and dynamism. These help developers reason about the practical cost of col­ lecting and maintaining each factor.

Where context is injected Once identified, contextual factors must be incorporated into the recommendation pipe­ line. For example, Kulkarni and Rodd (2020) describe the triad of pre-filtering, post-filter­ ing and contextual modelling: the first two strategies treat context as an external constraint applied before or after the core algorithm, whereas the third embeds contextual variables directly in the predictive model. Most large-scale systems adopt a hybrid approach, combin­ ing a cheap pre-filter with a lighter contextual model that can be retrained incrementally, as documented by recent benchmarks surveyed by Mateos and Bellogín (2024).

A first look beyond context The literature that labels itself “situation-aware” builds on the same raw information but pursues a qualitatively different goal: rather than exploiting each variable in isolation, SARS aim to interpret sets of variables as coherent situations and to drive the recommenda­ tion process from that higher-level construct.

Design choices diverge widely. Richthammer and Pernul (2020), for example, pre-define a set of everyday situations (e.g., relaxing at home on a rainy Sunday) and perform a strict pre-filter based on the situation that best matches the current sensor readings.

Dötterl et al. (2017) adopt a more flexible pipeline in which low-level events are fused on-the-fly, through complex-event processing, into short-lived situations that subsequently constrain and bias the recommender. An earlier contribution by Feng et al. (2009) embeds situation identification inside a decision-support loop, demonstrating that the same situ­ ational model can both filter options and anticipate future needs.

In the remainder of this section, these observations are leveraged to examine how current SARS select situational information and where they inject it.

<!-- page 14 -->

## 101 Page 14 of 38

### 6.1 What kinds of situational information are most frequently exploited?

A few trends emerge:

**Table 2 Macro-categories of situational information exploited in SARS**

L. Aliberti et al.

When moving to SARS, the picture becomes more variegated with respect to CARS: besides the “traditional” context cues (time, location, weather, company), researchers also inject higher-level evidence that mirrors the user’s goals, the system state, or even the opera­ tor’s physiological/cognitive condition. Table 2 groups the situational dimensions recurring across the literature into six macro-categories and lists representative works for each group.

● Temporal and spatial cues remain the most used information for SARS, inherited from CARS, and appear in almost every domain. ● Environmental signals such as weather or crowding are salient when the physical expe­ rience can be altered (e.g., outdoor tourism).

Category Typical situations’ attributes

SARS studies

Temporal Time-of-day, dayof-week, season, calendar events, remaining time

(Richthammer and Pernul 2020; Li et al. 2025; Dridi et al. 2016; Bedi and Agar­ wal 2012; Lv et al. 2023; Zhang et al. 2018; Bouzeghoub et al. 2009) Spatial/location GPS coordinates, indoor beacons, geographical region, distance to POI, map viewport

(Dötterl et al. 2017; Casillo et al. 2025; Liang et al. 2024; Zhao 2022; Viswa­ nathan et al. 2022; Iwasaki et al. 2010) Environmental Weather, traffic load, crowd density, network conditions, pollution

(Casillo et al. 2025; Dridi et al. 2016; Lim 2012; Hu et al. 2015; Zhang et al. 2020; Karlsen and Andersen 2019) User state & profile Physiological signals, mood/ emotions, exper­ tise level, current activity

(Hu et al. 2015; Richthammer and Pernul 2020; Abbas et al. 2024; Srivas­ tava et al. 2024b; Dridi et al. 2016; Li et al. 2025) Operational/system Task at hand, process vari­ ables, alarms, network topology, vulnerabilities

(Zhou et al. 2021; Abbas et al. 2024; Husák et al. 2022; Husak 2021; Sriv­ astava et al. 2024a; Kacprzyk et al. 2021) Social & relational Companions, user relation­ ships, collabora­ tively important situations

(Szczerbak et al. 2014; Viswanathan et al. 2022; Lim 2012; Dötterl et al. 2017)

<!-- page 15 -->

Page 15 of 38 101

Situation-aware recommender systems: a systematic review and…

● Capturing the user’s internal state (fatigue, mood, cognitive workload) is instrumental in safety-critical or wellbeing scenarios. ● In industrial, military, and cybersecurity settings the decisive factor is the operational/ system context. ● Several systems enrich recommendations with social signals, learning which composite situations are considered “important” by peers.

This spectrum of situational evidence underlines how SARS move beyond static user and item descriptors, dynamically blending multiple data streams so that recommendations remain aligned with the user’s immediate situation, a prerequisite for the architecture in Sect. 9.

### 6.2 When is the situation injected into the recommendation pipeline?

Following mainstream surveys on context-aware RS Villegas et al. (2018); Adomavicius and Tuzhilin (2011), Table 3 distinguishes three integration points of situational information:

(i) pre-filtering/triggering, (ii) post-filtering/re-ranking, (iii) model-level integration. Pre-filtering/triggering Early SARS prototypes rely on hard contextual constraints. Later works refine this by personalizing fuzzy boundaries or filtering sensor streams.

Post-filtering/re-ranking Some systems re-rank an initial recommendation list using situational hints. Model-level integration Most SARS embed situational variables directly within predictive models, ranging from Bayesian networks to deep neural architectures.

Overall, these findings indicate that pre- and post-filtering remain useful for mobile and push-style scenarios, while the mainstream trend involves weaving situational vari­ ables directly into the learning mechanisms for fine-grained personalization and continuous adaptation.

## 7 Techniques employed and domain of application of SARS

This section provides an overview of the most common state-of-the-art techniques and domains of application of SARS.

### 7.1 Techniques employed by SARS

Based on the selected works, SARS have been implemented using a variety of state-of-theart methods. A summary of the primary approaches, arranged into general categories, is provided in Fig. 2, and in Table 4 references to the representative works at the state of the art are also included.

Machine Learning Different works use machine learning techniques to make recommendations. Among the most commonly used techniques are collaborative filtering methods, such as the work proposed by Guo (2024), which suggests a collaborative filtering approach using a

<!-- page 16 -->

## 101 Page 16 of 38

**Table 3 Injection stage of situ­ ational information in SARS**

Works are listed in chronological order

L. Aliberti et al.

Stage Role of situ­ ational data

Representative studies

Pre-filtering/triggering Detect suitable moments for producing recom­ mendations or prune options conflicting with the in­ stantaneous situation

(Bouzeghoub et al. 2009; Bedi and Agar­ wal 2012; Ciaramella et al. 2010; Bedi et al. 2014; Dötterl et al. 2017; Richthammer and Pernul 2020)

Post-filtering/re-ranking Adjust an already com­ puted list by boosting items that comply with situational constraints

(Dötterl et al. 2017; Karlsen and Andersen 2019; Viswanathan et al. 2022; Jiang 2024)

Model-level integration Encode the situation directly in the learning or inference procedure

(Iwasaki et al. 2010; Cho et al. 2012; Szc­ zerbak et al. 2014; Hu et al. 2015; Dridi et al. 2016; Zheng 2017; Zhang et al. 2018; Chunhua et al. 2019; Zhou et al. 2020; Zhang et al. 2020; Husak 2021; Zhou et al. 2021; Kacprzyk et al. 2021; Husák et al. 2022; Zhao 2022; Chen 2022; Lv et al. 2023; Viswana­ than et al. 2022; Abbas et al. 2024; Liang et al. 2024; Srivastava et al. 2024b, a; Richtham­ mer and Pernul 2020; Li et al. 2025; Casillo et al. 2025)

context-resource matrix to recommend Chinese literature resources for study. From the per­ spective of content-based filtering, another example is the work proposed by Zhao (2022), which proposes a context-aware recommendation algorithm based on RFID applications, and Richthammer and Pernul (2020), who propose a situation-aware recommender based on content-based filtering that uses item seeds for music recommendations.

Another example is the work proposed by Cho et al. (2012), where the authors propose an approach based on co-clustering algorithms for extracting application usage patterns based on context for recommending applications on mobile phones according to the user’s current situation.

<!-- page 17 -->

Page 17 of 38 101

Situation-aware recommender systems: a systematic review and…

**Fig. 2 Distribution of techniques employed in SARS**

Tensor methods are also used at the state of the art, such as in the work proposed by Jiang (2024), where a tensor decomposition method called Context Aware Matrix Factorization (CAMF) is used for the recommendation of financial products, but also in the case of the work proposed by Zheng (2017), where both the CAMF technique and Biased Matrix Fac­ torization are used for the recommendation of online content, such as hotels, movies, etc.

Deep Learning Increasingly popular in recent years are the approaches based on deep learning. In par­ ticular, Li et al. (2025) propose a pluggable module called Situation-Aware Recommender Enhancer (SARE) that uses a Conditioning Neural Network, and an attention mechanism for the recommendation of multimedia content, such as news and short videos. Liang et al. (2024) use instead Spatiotemporal Graph Convolutional Neural Networks for text recom­ mendation. Other works, on the other hand, propose deep models, such as Lv et al. (2023), which proposes a deep model called Deep Situation-Aware Interaction Network (DSAIN), which uses deep learning techniques for predicting the Click-Through Rate. Zhou et al. (2021) and Chunhua et al. (2019) instead propose a recommendation model based on deep neural networks for recommending situational information in battle scenarios in order to provide the most relevant information to decision-makers and limit demons of situation awareness such as information overload (Endsley 1995).

Fuzzy Logic Fuzzy logic is useful for the management of imprecise and approximate information. In fact, Dridi et al. (2016) propose an approach for rating prediction based on the use of fuzzy rules to infer the user’s current situation, applying it to various contexts such as evaluating a menu based on different degrees of hunger, as well as musical or cinematic preferences.

Still regarding restaurant recommendations, there is the work of Bedi et al. (2014) and Bedi and Agarwal (2012), who use fuzzy logic for the situation assessment phase, where the system will determine the appropriate situation and the appropriate recommendation. Another work that used fuzzy logic to determine the most likely situation for the purpose of recommendation was proposed by Ciaramella et al. (2010), where the system leverages

<!-- page 18 -->

## 101 Page 18 of 38

**Table 4 Main techniques em­ ployed in SARS**

L. Aliberti et al.

Technique Key characteristics Representa­ tive works Machine learning Traditional methods such as collaborative filtering, content-based filtering, coclustering, and tensor decom­ position methods are used to recommend resources based on user-context interactions or context-aware preferences

(Cho et al. 2012; Zheng 2017; Guo 2024; Rich­ thammer and Pernul 2020; Zhao 2022; Jiang 2024) Deep learning Neural network architectures such as attention mecha­ nisms, conditioning neural networks, graph convolu­ tional networks, and interac­ tion networks for enhanced situational understanding and recommendation in multimedia, text, and critical decision-making scenarios

(Li et al. 2025; Liang et al. 2024; Lv et al. 2023; Zhou et al. 2021; Chunhua et al. 2019)

Fuzzy logic Fuzzy rules to manage uncertainty, approximate reasoning, and imprecise contextual data in various recommendation scenarios, including food, entertain­ ment, and semantic situation assessment

(Dridi et al. 2016; Bedi and Agarwal 2012; Bedi et al. 2014; Ciaramella et al. 2010)

Hybrid approaches Combines different tech­ niques such as semantic technologies, ontologies, Bayesian networks, tensor methods, machine learn­ ing, and deep learning approaches to derive and interpret complex situations and enhance recommenda­ tion capabilities in diverse domains, including smart farming, military, music, and industrial settings

(Dötterl et al. 2017; Szczerbak et al. 2014; Casillo et al. 2025; Chen 2022; Zhou et al. 2020; Abbas et al. 2024; Hu et al. 2015; Iwasaki et al. 2010; Zhang et al. 2018, 2020) Knowledge-based Employs explicit domain knowledge structured via ontologies, rules, and context behavior patterns to provide adaptive and precise recommendations tailored to specific contexts, espe­ cially in academic or spatial decision-making scenarios

(Bouze­ ghoub et al. 2009; Kacprzyk et al. 2021)

<!-- page 19 -->

Page 19 of 38 101

Situation-aware recommender systems: a systematic review and…

a semantic level with ontologies and fuzzy rules for situation recognition, supporting a rec­ ommender system based on genetic algorithms.

Hybrid Approaches Hybrid SARS approaches often combine semantic technologies and ontologies with machine learning, as in Dötterl et al. (2017), which integrates semantic web technologies and complex event processing for real-time context interpretation, and Szczerbak et al. (2014), which merges ontologies with collaborative filtering and rule-based methods. Ontologies are also paired with Bayesian networks, e.g., Casillo et al. (2025), where semantic pre-fil­ tering and context dimension trees constrain Bayesian network learning. Some works inte­ grate tensor methods with deep learning, such as Chen (2022), combining probability matrix decomposition with a Recurrent Neural Network for musical style recognition, and Zhou et al. (2020), which merges Tensor Factorization with Deep Neural Networks for military recommendations. Other studies couple probabilistic and statistical models: Abbas et al. (2024) integrates Hidden Markov Models with Deep Reinforcement Learning for industrial decision support, Hu et al. (2015) blends statistical methods and clustering for music mood labeling, and Iwasaki et al. (2010) combines Bayesian networks with machine learning for mobile content recommendations. In smart farming, Zhang et al. (2018) uses collaborative filtering with NLP and user portrait technology to build a three-dimensional rating matrix, while Zhang et al. (2020) merges situational matching with Bayesian learning.

Knowledge-Based Approaches in this category rely on explicit domain knowledge, typically structured through ontologies and rules, to deliver tailored and contextually relevant recommendations. For example, Bouzeghoub et al. (2009) employ an ontology- and rule-based framework to provide mobile users in a university setting with adaptive situation-aware recommenda­ tions, suggesting pertinent information about nearby people and resources according to their current context. In a different domain, Kacprzyk et al. (2021) focuses on spatial analysis using GIS, introducing a model based on context chains and behavior patterns. This model supports the selection of the most appropriate context for analysis, with the dual goal of improving the quality of the results and mitigating cognitive overload for decision-makers.

### 7.2 Domains of application in SARS

SARS have been applied in a wide range of contexts, as can be seen from Table 5, reflecting the flexibility and cross-cutting nature of these systems.

To complement, Tables 5 and 6 summarize, for each application domain, the main situ­ ational attributes used in the reviewed works to model or infer the user’s situation. This additional overview helps clarify which types of data contribute to situation formation across different domains.

Agriculture and Smart Farming SARS have proven highly valuable in agriculture, offering farmers precise and timely information to support decision-making. They help address challenges such as the “last mile” issue, integrating environmental and crop-monitoring data to improve logistics and resource management (Zhang et al. 2018, 2020).

Cultural Tourism and Museums In cultural tourism and museum contexts, SARS can enhance both physical and virtual experiences by enriching user engagement and personalizing content delivery. Examples

<!-- page 20 -->

## 101 Page 20 of 38

**Table 5 Key application domains of SARS and corresponding objectives Domain Use/main objectives Representative works Agriculture and smart farming**

Provide accurate and supportive information to farmers (e.g., logistics, “last mile” issue), integrating environmen­ tal data and crop monitoring

Cultural tourism and museums

(Casillo et al. 2025; Dötterl et al. 2017; Lim 2012) Cybersecurity and incident handling

Enrich the visiting experience (both physical and virtual) in cultural sites and museums, improving user engagement

(Husak 2021; Husák et al. 2022) E-commerce and financial

Support analysts in managing and responding to cyber in­ cidents (prioritizing at-risk devices and defense strategies)

Predict Click-Through Rate (CTR) and recommend prod­ ucts (including financial products), adapting the offering to the user’s preferences in the specific situation

Industrial and safety-critical

Support human–machine interactions (alarms, process anomalies) and manage spatial data in industrial contexts, reducing errors and cognitive load

Media and social Provide personalized recommendations in social plat­ forms or for multimedia content (news, short videos, feeds) by integrating contextual aspects (e.g., time, location)

(Li et al. 2025; Liang et al. 2024; Szczerbak et al. 2014; Zheng 2017) Music recommendation

(Dridi et al. 2016; Hu et al. 2015; Richtham­ mer and Pernul 2020) Military and safety-critical

Adapt playlists and tracks to the user’s mood, usage context (e.g., driving), or occasion, also for road safety or comfort

(Chunhua et al. 2019; Zhou et al. 2021, 2020; Srivastava et al. 2024b, a) Mobility and travel Recommend points of interest (POIs), resources, or routes to users on the move, taking into account location, sched­ ules, travel purpose, and providing proactive suggestions (e.g., restaurants)

Filter and prioritize operational information (battlefield situations), support high-risk missions, reduce informa­ tion overload, and improve decision-making

(Bedi and Agarwal 2012; Bedi et al. 2014; Iwasaki et al. 2010; Bouzeghoub et al. 2009; Cho et al. 2012; Ciaramella et al. 2010; Viswanathan et al. 2022; Zhao 2022) Personalized learning and education

Tailor educational materials to the student’s needs and context (e.g., musical learning, literary texts), optimizing the learning experience

L. Aliberti et al.

(Zhang et al. 2018, 2020)

(Lv et al. 2023; Jiang 2024)

(Abbas et al. 2024; Kacprzyk et al. 2021)

(Chen 2022; Guo 2024)

include systems that integrate semantic and situational data to guide visitors in archaeologi­ cal or cultural sites (Casillo et al. 2025; Dötterl et al. 2017). A complementary theoretical framework for designing mobile applications in tourism, grounded in situation awareness principles, is described in (Lim 2012).

Cybersecurity and Incident Handling In critical domains such as cybersecurity, SARS assists analysts in managing and responding to incidents by leveraging situation awareness models. For instance, the OODA loop (Richards 2020) is applied to prioritize devices at risk of infection and guide defense strategies in real time (Husak 2021; Husák et al. 2022). These approaches aim to reduce analyst workload while improving responsiveness in high-pressure environments.

E-commerce and Financial In the economic and marketing domain, SARS can adapt recommendations to a user’s immediate situation and preferences. In e-commerce, they have been applied to ClickThrough Rate prediction to improve product targeting (Lv et al. 2023). In the financial sec­

<!-- page 21 -->

Page 21 of 38 101

Situation-aware recommender systems: a systematic review and…

**Table 6 Examples of situational attributes used in each applica­ tion domain**

Domain Situational attributes (macro-categories) Agriculture and smart farming

Temporal attributes; spatial location; environmental and weather conditions; crop/soil state; equipment status; browsing or task topic Cultural tourism and museums

User location; time and availability; envi­ ronmental conditions; POI status/crowd­ ing; user intent and schedule; movement patterns; social proximity Cybersecurity and incident handling

Network location (physical/logical); device fingerprints; vulnerability state; update his­ tory; incident history; critical dependencies E-commerce and financial

Temporal attributes; user behavior type; physical/virtual location; scenario-specific contextual elements Industrial and safety-critical

Process variables and alarms; operator interaction logs; physiological signals; spatiotemporal navigation patterns Media and social Time; location; environment; emotional state; ongoing activities; behavioral prefer­ ences; device usage; social context Music recommendation Time and season; location; weather; driv­

ing dynamics; road/traffic conditions; mood and physiological cues; social context Military and safety-critical

Entity location and movement; threat at­ tributes; task assignment; environmental hazards; temporal discovery events Mobility and travel Location; temporal attributes; user activity; mobility speed; user intent; mood/emo­ tions; ambient conditions; device status; POI availability Personalized learning and education

Temporal attributes; learner location; en­ vironment; ongoing learning activity; user task; scenario/context elements

tor, similar techniques are used to recommend personalized investment or banking products (Jiang 2024), aligning offerings with the user’s situational profile.

Industrial and Safety-Critical Industrial applications of SARS include supporting human operators in managing alarms and process anomalies, as in formaldehyde production plant simulations (Abbas et al. 2024). In parallel, they assist analysts in the spatial exploration of industrial or business environ­ ments, using context chains and behavioral patterns to reduce cognitive load and enhance decision-making (Kacprzyk et al. 2021).

Media and Social In social media and multimedia domains, SARS aims to provide highly relevant and personalized content by integrating situational and contextual factors. For instance, they can tailor recommendations for news and short videos according to the user’s current cir­ cumstances (Li et al. 2025), incorporate spatiotemporal data to enhance social text recom­ mendations (Liang et al. 2024), or create collaborative environments where users share and validate situational contexts (Szczerbak et al. 2014). Multi-criteria methods also exploit situational context to refine user-item matching and optimize suggestion relevance (Zheng 2017).

<!-- page 22 -->

## 101 Page 22 of 38

L. Aliberti et al.

Music Recommendation In the music domain, SARS adapt playlists to specific moods, contexts, or activities (Richthammer and Pernul 2020). They can integrate mood and weather information to improve rating predictions (Dridi et al. 2016) or focus on safety-related applications, such as providing context-aware music suitable for driving conditions through crowd-cloud approaches (Hu et al. 2015).

Military and Safety-Critical In military and high-risk environments, SARS filter and prioritize operational informa­ tion to support decision-making in rapidly evolving scenarios. Battlefield-oriented systems employ neural networks and attention mechanisms to highlight the most relevant data for commanders (Chunhua et al. 2019; Zhou et al. 2021, 2020), while aerospace-focused studies explore how situational information improves human operator decision processes through collaborative AI-human frameworks (Srivastava et al. 2024b, a).

Mobility and Travel In mobility, SARS provide location- and situation-based recommendations to people on the move, anticipating needs without requiring explicit queries. Examples include proactive restaurant suggestions when a user’s location changes (Bedi and Agarwal 2012; Bedi et al. 2014), adaptive content delivery for in-car devices (Iwasaki et al. 2010), and campus guid­ ance systems indicating relevant buildings, people, and events (Bouzeghoub et al. 2009). Other works focus on recommending mobile applications depending on the scenario (Cho et al. 2012), optimizing travel consultant suggestions using context history (Ciaramella et al. 2010), analyzing mood-based variations in Points of Interest discovery (Viswanathan et al. 2022), or integrating RFID to personalize access to resources in mobile contexts (Zhao 2022). Personalized Learning and Education SARS in education adapts learning materials to the student’s context and needs, aiming to improve engagement and outcomes. Applications include music learning systems capable of recognizing and generating styles for targeted practice (Chen 2022), and personalized literary text recommendations that merge situation awareness with individual learning inter­ ests, particularly in the study of Chinese literature (Guo 2024).

### 7.3 Common datasets utilized by SARS

Among the works analyzed in the state of the art, many do not make available or mention the datasets used in their experiments. However, some studies employ publicly available datasets to train, test, and evaluate SARS models. These datasets, containing different con­ textual information, vary by domain and data type and can be grouped into a few relevant categories.

In the domain of multimedia and entertainment, different datasets have been employed, such as the InCarMusic dataset (Baltrunas et al. 2011), which collects user music prefer­ ences under various driving-related contextual conditions. This dataset was used in Dridi et al. (2016) to model music preferences based on dimensions such as time and mood. Similarly, the GTZAN dataset (Tzanetakis and Cook 2002) provides labeled audio tracks for genre classification and was used in the study by Chen (2022) for musical style learning and recommendation. The IMDb dataset, as used in Liang et al. (2024), was instead employed in Liang et al. (2024) to evaluate situation-aware text recommendation models, particularly

<!-- page 23 -->

Page 23 of 38 101

Situation-aware recommender systems: a systematic review and…

in the context of film reviews. The MovieLens dataset (Harper and Konstan 2015) is one of the most widely adopted datasets in recommender systems research. Zhao (2022) employed it in a context-aware setup, modeling user preferences based on inferred situational vari­ ables for mobile reading recommendations.

In the field of news and short videos recommendation, two large-scale datasets are espe­ cially relevant. The MIND dataset (Wu et al. 2020) was collected from Microsoft News and contains rich interaction logs and was used in the work proposed by Li et al. (2025) to build and evaluate a news recommendation model incorporating temporal situation features. Similarly, the KuaiRand (Gao et al. 2022) dataset was collected from the Kuaishou app and provides unbiased user interaction data with short-form videos, and was also used in the same work (Li et al. 2025) to train and test their proposed SARS framework.

For e-commerce and behavioral analysis, three large industrial datasets are often cited. The Taobao dataset (Zhu et al. 2018) and the Meituan dataset offer extensive logs of useritem interactions enriched with behavioral and temporal metadata. Along with Eleme, these datasets were used in Lv et al. (2023) to develop a deep learning model for click-through rate prediction in situation-aware e-commerce recommendation.

In the domain of tourism and multi-criteria feedback, the TripAdvisor and YahooMovie datasets (Jannach et al. 2014) are used as benchmarks. These datasets contain fine-grained user ratings over multiple criteria (e.g., cleanliness, service, story, acting) and were used by Zheng (2017) to investigate how multi-aspect preferences can be leveraged as situational information in SARS.

To complement this overview, Table 7 summarises the datasets explicitly used in the reviewed works, including their domain, approximate scale (when available), and the situ­ ational or contextual attributes they enable.

### 7.4 Evaluation protocols and metrics in SARS

Evaluation practices in SARS reveal a strong imbalance between computer-centric perfor­ mance metrics and human-centred assessments of Situation Awareness (SA). Most works adopt standard offline evaluation protocols inherited from traditional recommender systems, whereas only a small subset, typically in safety-critical domains, directly measure Human SA or cognitive outcomes. To clarify this distinction, we organise the evaluation landscape into two complementary dimensions: (i) metrics targeting Computer SA (algorithmic per­ formance and system-level behaviour), and (ii) metrics explicitly targeting Human SA (user cognition, workload, trust, and situational understanding).

### 7.4.1 Metrics for computer situation awareness (computer SA)

Computer SA is predominantly evaluated through offline accuracy metrics, often identical to those used in classical RS and CARS. Ranking-focused SARS employ Hit Ratio, MAP, and NDCG@K (Hariri et al. 2013; Li et al. 2025), whereas rating or prediction tasks rely on MAE and RMSE (Dridi et al. 2016; Tavakolifard 2009; Zheng 2017; Zhao 2022). Some domains introduce additional performance indicators tailored to operational constraints, such as response time, matching ratio, computational complexity, or business metrics like CTR, CPM, and GMV (Lv et al. 2023). Dataset splitting strategies are often conventional

<!-- page 24 -->

## 101 Page 24 of 38

**Table 7 Summary of datasets used in the reviewed SARS works**

a​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​m​e​i​t​u​a​n​/​M​e​ i​t​u​a​n​-​I​N​F​O​R​M​S​-​T​S​L​-​R​e​s​e​a​r​c​ h​-​C​h​a​l​l​e​n​g​e

L. Aliberti et al.

Dataset Domain Users Items Situational attributes InCarMu­ sic (Baltrunas et al. 2011)

Music/Mobility 42 139 tracks Driving context, mood, weather, time, traffic GTZAN (Tzane­ takis and Cook 2002)

Audio genre, mu­ sical style features IMDb Re­ views (Liang et al. 2024)

Music N/A 1000 tracks

Review text, timestamps, sentiment MovieLens (Small) (Harper and Konstan 2015)

Media/Text N/A 50k reviews

Time­ stamps, implicit temporal context MIND (Wu et al. 2020)

Movies 610 9,742 movies

Time, session structure, impression logs KuaiRand (Gao et al. 2022)

News 1 M 161k news

User behavior, time, device, session context Taobao (Zhu et al. 2018)

Short videos 27k 32 M videos

Time, be­ havior type, session context Meituana Food/E-comm 40k 1 M items Temporal features, activity pattern Eleme (Qin et al. 2020)

E-commerce 1 M 4 M products

Time, user actions, scenario context TripAdvi­ sor (Wang et al. 2011)

Food delivery 14.4M 7.4M items

Multi-crite­ ria ratings (service, value, etc.) YahooMov­ ie (Wang et al. 2011)

Tourism 1,725 3,347 hotels

Movies 6,078 976 movies

Multi-crite­ ria ratings (story, acting, visuals)

<!-- page 25 -->

Page 25 of 38 101

Situation-aware recommender systems: a systematic review and…

(hold-out, cross-validation), with a minority adopting session-based or temporal splits aligned with the dynamics of situational data (Li et al. 2025).

### 7.4.2 Metrics for human situation awareness (human SA)

Only a small number of SARS explicitly evaluate Human SA. In safety-critical domains, SA is measured using validated psychometric instruments, such as SART, SPAM, NASA-TLX, and trust questionnaires, often complemented by physiological signals (heart rate, EDA, eye-tracking) and task performance (Abbas et al. 2024). Studies in human–AI teaming adopt SA and Shared Situation Awareness (SSA) as primary outcomes, examining trust calibration and reduction of overreliance (Srivastava et al. 2024b, a). Mobility and consumer-oriented works tend instead to rely on lightweight user studies (e.g., satisfaction ratings, interviews, Wizard-of-Oz validation) that capture perceived usefulness but rarely measure SA directly (Richthammer and Pernul 2020; Viswanathan et al. 2022). Overall, explicit Human SA eval­ uation remains the exception rather than the rule.

Table 8 highlights that domains involving high-risk or high-stakes decision-making (industrial control, military operations, human–AI teaming) are the only ones where Human SA is systematically evaluated. By contrast, the majority of SARS, especially in com­ mercial, media, tourism, and entertainment contexts, restrict evaluation to Computer SA, relying primarily on algorithmic accuracy metrics. This imbalance reveals a substantial methodological gap: although SARS are motivated by SA theory, most contributions do not assess whether recommendations actually improve users’ awareness or decision quality.

## 8 Discussion

The analysis reveals a dynamic yet fragmented research landscape. Regarding RQ1 and RQ2, many research works still conflate raw, low-level context with the more complex notion of situation; others implicitly introduce situations but fail to explain how they emerge from context. Because each researcher employs an individual operational definition, direct comparisons remain difficult, which in turn slows the overall progress of the field. The aim of this survey is to contribute a common definition of SARS grounded in Situation Aware­ ness (SA) theory (Endsley 1995).

With respect to RQ3, most systems incorporate situational information during the model­ ling phase, for instance as additional features, latent factors, or graph nodes. Only a minority adopt SA in a more holistic way or attempt to evaluate whether either the user or the system genuinely attains greater awareness. Research explicitly addressing Human SA is still rare, largely due to the high costs and methodological challenges associated with collecting valid SA measures from end-users at scale. By contrast, the majority of works focus on Computer SA, often assuming that improved predictive accuracy is a sufficient proxy for enhanced awareness.

These findings highlight the importance of adopting design principles and guidelines inspired by SA and human factors, such as Endsley’s Situation Awareness Oriented Design (SAOD) (Endsley and Jones 2024), to ensure that data acquisition, reasoning, and interface design are aligned with SA objectives from the outset. While explicit adoption of SAOD is uncommon in the reviewed literature, such principles can provide a cohesive foundation

<!-- page 26 -->

## 101 Page 26 of 38

**Table 8 Evaluation metrics used across SARS domains, distinguishing computer SA and human SA**

Domain (representative works)

Cultural tourism and museums (Casillo et al. 2025; Dötterl et al. 2017; Lim 2012)

Cybersecurity and incident handling (Husak 2021; Husák et al. 2022)

Industrial/safety-critical (Abbas et al. 2024; Kacprzyk et al. 2021)

Music recommendation (Dridi et al. 2016; Hu et al. 2015; Richthammer and Pernul 2020)

L. Aliberti et al.

Computer SA metrics Human SA metrics Agriculture and smart farming (Zhang et al. 2018, 2020)

### N/A N/A

Precision; Recall; Fscore; Accuracy (clas­ sifier evaluation)

N/A

User interviews; perceived understand­ ing; trust in explanations E-commerce and financial (Lv et al. 2023; Jiang 2024)

Expert-based ranking quality; matching rate (case-study compari­ son with ground truth)

AUC; Logloss; CTR; CPM; GMV; offline + online A/B tests; recommendation accuracy

N/A

SART; SPAM; NASA-TLX; trust question­ naires; EDA; heart rate; eye-tracking Media/news/short video (Li et al. 2025; Liang et al. 2024; Zheng 2017)

Prediction accuracy; response time; com­ plexity; error rates

HR@K; MAP@K; NDCG@K; F1; RMSE; recommenda­ tion efficiency

N/A

User satisfac­ tion; perceived meaningful­ ness; fatigue reduction (self-report) Military and safety-critical (Chunhua et al. 2019; Zhou et al. 2021; Srivas­ tava et al. 2024b)

MAE; RMSE; Precision/Recall; classification accu­ racy; mood-mapping accuracy

SA/SSA (human–AI teaming); task perfor­ mance; trust calibration Mobility and travel (Bedi and Agarwal 2012; Iwa­ saki et al. 2010; Viswana­ than et al. 2022)

Accuracy; sce­ nario simulation indexes; task-specific performance

Wizard-ofOz evalua­ tions; user satisfaction; interviews Personalized learning/ education (Chen 2022; Guo 2024)

Precision; Recall; F1; MAE/RMSE; accep­ tance rate; prediction accuracy

Accuracy; outcomebased metrics (final student grade)

Perceived learning sup­ port (implicit SA proxy)

for developing SARS that are both effective and usable. In this perspective, the remaining research questions (RQ4–RQ7) investigate how SARS are technically realised and empiri­ cally assessed, from the underlying learning pipelines and application domains to the data­ sets and evaluation protocols used in practice.

<!-- page 27 -->

Page 27 of 38 101

Situation-aware recommender systems: a systematic review and…

From a methodological perspective, our analysis of techniques (RQ4) shows a strong predominance of supervised learning pipelines across the reviewed works. Situations are typically injected as predefined labels or engineered context features rather than discov­ ered autonomously from raw streams of contextual data. Unsupervised and self-supervised approaches, such as clustering, contrastive learning, or latent situation discovery, remain underexplored, despite their natural suitability for identifying recurrent or emerging situ­ ational patterns without requiring large volumes of annotated data. This imbalance is partly explained by the fact that many SARS operate in safety-critical or decision-critical domains (e.g., industrial process monitoring, military operations, cybersecurity, mobility). In such settings, supervised models are traditionally preferred because they provide higher predict­ ability, auditability, and certifiability. These properties make them easier to validate and govern compared to fully unsupervised methods, whose emergent structures may introduce uncertainty or reduce system controllability. While this does not fully justify the lack of unsupervised approaches, it contextualises why latent situation discovery remains a rela­ tively unexplored research direction.

A second methodological pattern emerges when examining domains of application (RQ5): none of the reviewed works adopt a true multi-domain design. This absence is not coincidental. Defining a “situation” in a domain-agnostic manner is intrinsically chal­ lenging, as the semantics, granularity, and relevant signals of a situation vary significantly across domains such as mobility, cultural heritage, industrial environments, and defence operations. Consequently, situation models tend to be tightly coupled to domain-specific ontologies, sensor modalities, and operational goals. Moreover, situation awareness is pri­ marily employed in safety-critical scenarios, discouraging cross-domain architectures, since general-purpose models introduce additional uncertainty and complicate validation, certifi­ cation, and risk management. Finally, most works intentionally limit their focus to a single domain due to the lack of shared datasets, evaluation protocols, and transferable situational representations. As a result, the current SARS landscape remains strongly domain-specific, highlighting an important open challenge for future research in cross-domain situation mod­ elling and generalizable situational embeddings.

Regarding RQ6, we observe that only a subset of SARS works rely on publicly available datasets, while many others use custom or undisclosed data sources. Available datasets vary greatly in scale, modality, and granularity of contextual signals, which limits comparabil­ ity across studies and highlights the need for standardized benchmarks for situation mod­ elling. Regarding RQ7, our analysis of evaluation protocols confirms that SARS largely inherit offline assessment practices from traditional RS and CARS. Most contributions focus on Computer SA, using standard accuracy and ranking metrics (e.g., MAE/RMSE, Precision/Recall, HR@K, MAP@K, NDCG@K) and, in industrial or commercial settings, business-oriented indicators such as CTR, CPM, or GMV. Only a minority of works, mainly in safety-critical domains (e.g., control rooms, military operations, human–AI teaming), explicitly measure Human SA through validated instruments such as SART, SPAM, NASATLX, trust questionnaires, or task performance combined with physiological signals. As summarised in Table 8, evaluations in media, tourism, mobility, and entertainment scenarios are almost exclusively computer-centric, occasionally complemented by user satisfaction or interview studies but rarely by direct SA measures. This reveals a methodological misalign­ ment: although SARS are motivated by Situation Awareness theory, most studies do not

<!-- page 28 -->

## 101 Page 28 of 38

L. Aliberti et al.

rigorously assess whether recommendations actually enhance users’ situational understand­ ing or decision-making quality.

Taken together, the methodological patterns emerging from RQ4–RQ7 intersect with broader concerns about the trustworthiness of SARS. Recent years have seen a clear shift toward deep learning-based approaches, often deployed in safety-critical domains. While these methods typically achieve strong predictive performance, Endsley warns of recur­ ring “ironies” in AI systems: as capabilities grow and interaction becomes more natural, internal reasoning processes remain opaque and users may overestimate system reliability and impartiality (Endsley 2023). These risks are amplified when evaluation focuses almost exclusively on algorithmic accuracy while neglecting Human SA and decision quality. To mitigate such issues, SARS development should integrate the foundational principles of trustworthy recommender systems, transparency, fairness, robustness, and privacy, recently outlined by Wang et al. (2024). Embedding these pillars within the SA loop can help balance predictive performance with interpretability and reliability. The framework proposed in Sect. 9 reflects this integration: it formalizes the fusion of raw context into situations, shows how SA principles inform each stage of processing, and incorporates continuous monitoring of trustworthiness requirements. In doing so, it aims to provide a unified reference model for designing SARS that are accurate, interpretable, and genuinely human-centered.

## 9 Proposed framework

The results of the systematic review highlight a fragmented landscape: existing SARS implementations differ substantially in how they gather contextual information, infer situ­ ational states, and incorporate such states into the recommendation process. Most works operationalise “situation” through ad-hoc heuristics or simplified feature engineering, while only a minority adopt explicit reasoning procedures grounded in SA theory. Moreover, no existing approach provides a unified view of how perception, comprehension, and projec­ tion should interact with the stages of a modern RS pipeline. As a consequence, situational reasoning is often treated as an isolated component, useful in specific tasks, but discon­ nected from data preparation, representation learning, or evaluation. Building on these find­ ings, this section proposes a reference framework designed to address these shortcomings. Its purpose is not merely to introduce another architectural template, but to systematise the insights emerging from the review: (i) SA offers a principled structure for modelling how situational information is exploited; (ii) trustworthy RS principles provide the safeguards needed to ensure that such reasoning remains transparent, robust, and ethically aligned; and (iii) their integration clarifies where situational cues should be processed and how their influence should propagate throughout the RS lifecycle.

The proposed framework is designed to be domain-independent, meaning that it can be instantiated in a variety of application areas while preserving its core structure and prin­ ciples. Figure 3 illustrates the proposed architecture for a Situation-Aware Recommender System (SARS) based on trustworthy principles. Its aim is to embed the loop of Endsley’s Situation Awareness (SA) model (Endsley 1995) into the life cycle of a recommender sys­ tem, while threading through every stage the four trust stages for trustworthy recommender systems identified by Wang et al. (2024).

According to Wang et al. (2024), these four stages are:

<!-- page 29 -->

Page 29 of 38 101

Situation-aware recommender systems: a systematic review and…

Fig. 3 Overview of the proposed domain-independent framework. Inspired by Endsley’s three-level SA model (Perception, Comprehension and Projection) the architecture aligns each level with the four trust­ worthiness stages defined by Wang et al. (2024). This mapping embeds robustness, privacy, fairness, and explainability directly inside the SA loop

● Data Preparation—ensuring robustness and privacy from the moment data is ingested; ● Data Representation—designing transparent, interpretable, and robust feature spaces; ● Recommendation Generation—producing fair, responsible, and goal-aware recom­ mendations; ● Recommendation Evaluation—assessing recommendations using both technical and socio-ethical metrics, enabling continuous adaptation.

These stages are depicted in the lower part of Fig. 3, aligned with the SA levels in the upper part.

It is important to clarify that, as can be seen in Fig. 3 the three levels of SA are not sequential. In Endsley’s formulation, Perception, Comprehension, and Projection oper­ ate as mutually dependent processes that continuously influence one another rather than forming a linear pipeline or explicit feedback loop. The proposed framework preserves this interpretation: the blocks are drawn separately for clarity, but situational reasoning unfolds as an ongoing, interconnected cycle in which updates at any level may propagate to the others. For the same reason, trustworthy AI principles are not mapped rigidly to a single SA level, in contrast, they are applied across multiple stages of the SA process, reflecting the inherently intertwined nature of situational inference and trustworthy recommendation generation. This interdependence explains why the figure does not adopt a circular loop rep­ resentation and why trustworthiness safeguards permeate the entire framework rather than appearing as fixed, one-to-one correspondences.

The proposed framework is introduced as a design guideline intended to support the development of SARS, providing practical guidance on how to embed Endsley’s percep­

<!-- page 30 -->

## 101 Page 30 of 38

L. Aliberti et al.

tion–comprehension–projection loop into the RS lifecycle, while aligning each phase with trustworthy AI requirements.

### 9.1 From raw signals to high-level context

The architecture begins in smart environments, which include mobile phones, IoT devices, and other sources that continuously emit raw signals. A first phase ingests those signals and applies noise removal, integrity checks, and privacy shielding. Because robustness and privacy are the prime concerns at this entrance point, this block addresses the Data Prepara­ tion stage of the TRS pipeline.

The low-level perception module φ0 converts each signal into punctual observations (heart rate, ambient light, GPS fix) and anonymises, corrects, and debiases all the gathered information. Formally:

```math
φ0 : raw −→C0 ∈C,
(1)
```

where C denotes the space of all contextual tuples.

A second stage of the perception phase is the high-level perception φ1, which trans­ forms heterogeneous observations into richer constructs, discarding variables that offer no explanatory power and re-weighting features according to user preferences. To preserve transparency, feature selection and fusion must remain explainable:

```math
φ1 : (C0, u) −→C1 ∈C′ ⊆C.
(2)
```

As stated before, the dependence on u ensures that for every user u the system maintains a latent profile u ∈Rd (chronotype, routine stability, risk tolerance, etc.). This vector does not directly produce recommendations; instead, it parametrises each transformation, allowing the same cue to be interpreted and weighted differently for different users.

### 9.2 Comprehension: promoting context to situation

In this stage, the mapping function f is formally defined as the mechanism that transforms high-level context into one or more possible situations, each with an associated probability. It leverages contextual features, active goals, and a hybrid knowledge base to bridge the gap between what is observed (context) and what it means (situation).

```math
f : (C1, G, Σ, u) −→{
```

(S1, p1), . . . , (Sk, pk)}

```math
,
(3)
```

where G = {g1, . . . , gm} is the (possibly concurrent) set of active goals. Identifying the active goals requires cognitive task analysis techniques, such as Goal-Directed Task Analy­ sis (GDTA) (Endsley 1995), to elicit and model the objectives driving the user’s current activity. Σ is a hybrid knowledge base composed of declarative rules and patterns learned from data and expert knowledge. The pairs

{

(S1, p1), . . . , (Sk, pk)}

are the inferred situa­ tions and the associated confidences.

For example, a person working night shifts may be in a “having breakfast” situation at 11:00 a.m., whereas an early riser could be in a “having lunch” situation. This divergence

<!-- page 31 -->

Page 31 of 38 101

Situation-aware recommender systems: a systematic review and…

occurs because the same contextual cues (e.g., time of day, activity level) are interpreted differently depending on the chronotype and daily routine embedded in u.

Over time, both u and fragments of Σ may drift. Accordingly, f has to be implemented so that either component can be updated without breaking determinism or auditability.

### 9.3 Projection and recommendation

The projection phase makes use not only of the inferred situation but also of the high-level context. This enables a hybrid approach that supports data-driven operation in cases where situational inference is uncertain, by falling back on contextual embeddings. Given the cur­ rent high-level context C1, the inferred situations with confidences

{

(S1, p1), . . . , (Sk, pk)}

, and the user profile u, the projection module π performs a dual task: (i) it produces a ranked list of items that respect both the current and the anticipated constraints and (ii) it forecasts how the situation may evolve in the near future. Formally:

π : (C1, (Sj, pj), p, u) −→(

j ))

### L, (S+

j , p+

```math
,
L = ⟨i1, . . . , iℓ⟩⊆I,
(4)
```

where (S+

j , p+

j ) is the short-term projection of the future situations and associated confi­ dences, while L is the recommendation list of items. The profile u modulates soft constraints (e.g., cognitive-load limits, preferred interaction modality), while C1 supplies the contex­ tual embeddings needed by data-driven rankers. This ensures adaptability: when the most probable situation is clear, the recommendation is goal-driven; when uncertainty is high, the system relies on contextual embeddings to preserve reliability.

Both outputs are logged together so that subsequent evaluation can trace every recom­ mendation back to the situational forecast, preserving transparency and accountability.

### 9.4 Endsley and TRS correspondence

The framework in Sect. 9 aligns the three levels of Endsley’s Situation Awareness (SA) model (Endsley 1995) with the four stages for trustworthy recommender systems (TRS) defined by Wang et al. (2024). This mapping is not merely structural: each SA layer benefits from safeguards typical of its corresponding TRS stage, ensuring that trustworthiness prin­ ciples are embedded directly in the SA loop.

For example, perception stages are reinforced by the TRS focus on robust and privacypreserving data preparation, while comprehension gains from transparency and fairness mechanisms during representation and reasoning. Projection is directly linked to the recom­ mendation generation stage, where contextual relevance is balanced with ethical constraints. Finally, the evaluation loop mirrors the TRS evaluation stage, integrating both technical and socio-ethical metrics to sustain user trust over time.

This correspondence clarifies where trust properties are applied and how they contribute to maintaining accurate situational reasoning and reliable recommendations. A concise sum­ mary of these mappings and safeguards is provided in Table 9.

<!-- page 32 -->

## 101 Page 32 of 38

L. Aliberti et al.

**Table 9 Where each TRS property is enforced inside the SA loop**

Endsley layer TRS stage Principal safeguards Perception-low Data preparation Robustness, privacy Perception-high Representation Explainability, robustness Comprehension Rep. → Gen Fairness, uncertainty bounds Projection Generation Transparency, responsibility Evaluation loop Evaluation Composite trust metrics and adaptation triggers

### 9.5 Illustrative example: adaptive micro-learning recommender

To demonstrate how the framework in Fig. 3 can be concretely instantiated, this subsection outlines a Situation-Aware Recommender that delivers short “micro-learning” nuggets to knowledge workers during their day (Aliberti et al. 2025). The system exploits off-the-shelf sensors already present on a smartphone and a smartwatch, plus privacy-preserving logs from the corporate Learning Management System (LMS).

● Sensing Level The client app continually gathers raw signals: GPS fixes, accelerometer streams, ambient noise, Bluetooth status (car kit/headphones), calendar events and a thin LMS log containing the IDs of the last resources studied. No personal content leaves the device; logs are anonymized. ● Low-Level Perception φ0. Raw samples are converted into atomic observations such as speed = 18 km/h, audio SNR = low, weekday = Mon, time = 07:45. A noise filter discards GPS jumps and corrects clock drift; debiasing routines down-sample overrepresented office hours to avoid class imbalance. ● High-Level Perception φ1. Contextual embeddings are derived by fusing the observa­ tions with the user profile u = (chronotype, preferred modality, . . . ).

– For an early-bird employee (uEB) the couple {time = 07:45, speed = 18 km/h} yields the high-level context commuting_to_work. – For a night-shift developer (uNS) the same cues are mapped to returning_ from_shift, because the embedding weights the sleep window feature more strongly.

● Comprehension f. The reasoning engine combines the embedding C1 with: (i) the ac­ tive goal set G={“finish Scrum guide”}, (ii) an expert rule base saying, e.g. “If driving then penalise video content”, and (iii) usage patterns mined from the LMS. It outputs ranked situations with confidence:

f {(driving_car, 0.72), (crowded_train, 0.18), (walking, 0.10)}.

Trustworthy safeguards propagate the confidence values, for example, if GPS accuracy drops, the weight of driving_car is lowered automatically.

● Projection & Recommendation π. The projection module forecasts that driving_

<!-- page 33 -->

Page 33 of 38 101

Situation-aware recommender systems: a systematic review and…

car will last ≈ 20 min until the next calendar appointment. It therefore selects an audio micro-podcast “Scrum Roles in a Nutshell” (5 min) and queues two spaced-repetition flash-cards that can be consumed hands-free via a voice interface. For a user detected as crowded_train, the same goal would instead trigger a short text summary plus a 1-min quiz optimised for thumb interaction.

The example shows how identical low-level cues (time, speed, noise) are translated, through user-conditioned embeddings, probabilistic situation inference and situation-aware projec­ tion, into radically different recommendation strategies, all while preserving the robustness, privacy and fairness guarantees mandated by the trustworthy pipeline.

## 10 Open challenges and future directions

The results of this survey reveal a field that is conceptually promising yet methodologi­ cally fragmented. While Situation Awareness (SA) offers a coherent theoretical lens for modelling dynamic, goal-driven interactions, current SARS implementations vary widely in how they define situations, infer them, and integrate them into recommendation processes. Building on the findings of RQ1–RQ7 and on the proposed framework in Sect. 9, several open challenges emerge that cut across modelling, data, evaluation, and system design.

Toward Shared and Operational Definitions of Situations A persistent problem is the absence of a shared operational definition of “situation.” Con­ text and situation are often conflated, while SA-inspired representations rarely specify how Perception, Comprehension, and Projection should interact. Establishing unified ontologies, taxonomies, and computational templates for situations remains a foundational research direction.

Unsupervised and Self-Supervised Situation Modelling Most SARS rely on supervised pipelines where situational states are predefined rather than discovered. Yet many situational patterns naturally emerge from sensor data, behav­ iour traces, and temporal dynamics. Unsupervised clustering, contrastive learning, latent situation discovery, and representation learning remain largely underexplored, despite their potential to generalise across domains and reduce annotation costs.

Goal Modelling and Truly Proactive Recommendations Few systems explicitly model user goals, although goals are central to SA. Without goal elicitation or goal inference, SARS remain reactive. Integrating lightweight cognitive task analysis, implicit goal recognition, and temporal goal modelling is essential for enabling genuinely proactive, SA-consistent recommendations.

Evaluation of Human and Computer SA Evaluation practices remain dominated by accuracy-based offline metrics inherited from traditional RS and CARS. Only a minority of works assess Human SA using instruments such as SART, SPAM, NASA-TLX, or trust calibration measures. Developing scalable pro­ tocols for jointly assessing Computer SA and Human SA, especially in safety-critical or decision-critical scenarios,nremains an essential but unresolved challenge.

Fragmented Datasets and Lack of Benchmarks Current SARS evaluations rely on heterogeneous, often private datasets with varying con­ textual granularity, making cross-study comparison difficult. The community lacks bench­

<!-- page 34 -->

## 101 Page 34 of 38

L. Aliberti et al.

mark datasets tailored to situation modelling, multimodal context fusion, and SA-informed evaluation. Creating such benchmarks is crucial for advancing reproducible research.

Trustworthy, Transparent, and Explainable SARS Deep learning-based SARS often achieve high predictive performance but introduce opacity, reduced controllability, and fairness risks. Integrating transparency, uncertainty estimation, causal reasoning, and privacy-preserving methods throughout the SA loop is still at an early stage. Closing the gap between algorithmic performance (Computer SA) and user-centred outcomes (Human SA) is critical for building trustworthy SARS aligned with SA theory.

Integration of LLMs into SA-Aware Recommendation Pipelines The emergence of Large Language Models (LLMs) opens new possibilities for SARS, including semantic orchestration of context signals, natural-language reasoning about situ­ ations, and simulation of future states. Approaches such as OpenAGI, Generative Agents, and language-driven recommendation (e.g., P5) highlight the potential of LLMs as SA inter­ mediaries. However, integrating them safely requires careful consideration of transparency, controllability, and reliability.

## 11 Conclusions

Recommender Systems have become central infrastructures of digital platforms, and the move from pure preference modelling to situation-aware paradigms reflects the need to anticipate user needs in dynamically changing environments. Building on Situation Aware­ ness (SA) theory, this survey examined how current Situation-Aware Recommender Sys­ tems (SARS) exploit contextual and situational information, and to what extent they embed principles of trustworthy AI. A key objective was to clarify the conceptual boundary between context and situation and to assess how SA is operationalised in practice.

Adopting a PRISMA-based methodology across Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and ScienceDirect, we identified 34 relevant works published between 2009 and 2025. The analysis reveals that, despite frequent references to SA, a clear and shared definition of “situation” is still lacking from a recommender-system perspec­ tive. Most contributions emphasise Computer SA and implicitly equate higher predictive accuracy with better awareness, whereas rigorous measurements of Human SA remain rare due to their methodological and logistical complexity. We also observed a strong preva­ lence of supervised learning pipelines, limited use of unsupervised or self-supervised situ­ ation discovery, and a fragmented ecosystem of datasets that hinders comparability and reproducibility.

To address these gaps, we introduced a reference framework that formalises the progres­ sion from raw contextual data to high-level situations, aligns this progression with End­ sley’s perception–comprehension–projection structure, and integrates the four stages of trustworthy recommender systems throughout the RS lifecycle. Rather than proposing yet another isolated architecture, the framework is intended as a design guideline: it indicates where situational cues should be ingested, how they can be fused with user goals and knowl­ edge bases, and at which stages robustness, fairness, transparency, and privacy safeguards should be enforced. The illustrative micro-learning use case shows how identical low-level

<!-- page 35 -->

Page 35 of 38 101

Situation-aware recommender systems: a systematic review and…

cues can lead to different recommendation strategies once situational reasoning and trust constraints are explicitly modelled.

Overall, our findings point to a field that is conceptually rich but methodologically frag­ mented. Open issues include the absence of shared situational representations, the limited assessment of Human SA, the lack of SARS-specific benchmarks, and the still partial inte­ gration of trustworthy-AI requirements into real-world pipelines. These challenges translate into a concrete research agenda for next-generation SARS that are not only accurate, but also interpretable, robust, and genuinely human-centred.

As future work, we plan to instantiate and evaluate the proposed framework in mul­ tiple domains, including academic and corporate learning environments and content-based advertising scenarios. Particular attention will be devoted to (i) designing situation-aware evaluation protocols that jointly consider Computer SA and Human SA, and (ii) exploring architectural choices, such as edge computing for on-device situation inference and privacy preservation, that can operationalise the trustworthiness pillars without sacrificing recom­ mendation quality.

Author contributions Luca Aliberti: Methodology, Validation, Investigation, Data Curation, Writing—Origi­ nal Draft, Visualization. Giuseppe D’Aniello: Conceptualization, Methodology, Validation, Investigation, Project administration, Writing—Original Draft, Writing - Review & Editing, Supervision, Visualization. Matteo Gaeta: Conceptualization, Methodology, Validation, Investigation, Writing—Original Draft, Writing - Review & Editing, Supervision, Visualization.

Funding Open access funding provided by Università degli Studi di Salerno within the CRUI-CARE Agree­ ment. This work was partially supported by the MIMIT—PN RIC 2021–2027 “Scoperta Imprenditoriale”— under the research project HAGRID—CUP B89J24000480005.

Data availability No datasets were generated or analysed during the current study.

Declarations

Conflict of interest The authors declare no conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

## References

Abbas A, Amazu C, Mietkiewicz J et al (2024) Analyzing operator states and the impact of AI-enhanced decision support in control rooms: a human-in-the-loop specialized reinforcement learning framework for intervention strategies. Int J Hum Comput Interact Abowd GD, Dey AK, Brown PJ et al (1999) Towards a better understanding of context and context-aware­ ness. In: Handheld and ubiquitous computing: first international symposium, HUC’99 Karlsruhe, Ger­ many, September 27–29, 1999 Proceedings. Springer, pp 304–307 Adomavicius G, Tuzhilin A (2011) Context-aware recommender systems. In: Recommender systems hand­ book. Springer, Boston, pp 217–253

<!-- page 36 -->

101 Page 36 of 38 L. Aliberti et al. Alcaraz C, Lopez J (2013) Wide-area situational awareness for critical infrastructure protection. Computer 46(4):30–37 Aliberti L, D’Aniello G, Gaeta M et al (2025) CONSALE: constructing situation awareness in microlearning environments. In: Proceedings of the 2025 IEEE conference on cognitive and computational aspects of situation management (CogSIMA), pp 200–204 Baltrunas L, Kaminskas M, Ludwig B et al (2011) InCarMusic: context-aware music recommendations in a car. In: E-commerce and web technologies. Springer, p 89–100 Baumgartner N, Retschitzegger W (2006) A survey of upper ontologies for situation awareness. In: Proceed­ ings of the 4th IASTED international conference on knowledge sharing and collaborative engineering, pp 1–9 Bedi P, Agarwal S (2012) A situation-aware proactive recommender system. In: Proceedings of the 2012 high performance computing and communications, pp 85–89 Bedi P, Agarwal S, Sharma S et al (2014) SAPRS: situation-aware proactive recommender system with explanations. In: Proceedings of the 2014 international conference on advances in computing, com­ munications and informatics (ICACCI), pp 277–283 Bouzeghoub A, Do K, Wives L (2009) Situation-aware adaptive recommendation to assist mobile users in a campus environment. In: Proceedings of the 23rd IEEE international conference on advanced informa­ tion networking and applications, pp 503–509 Casillo M, Colace F, Lorusso A et al (2025) Integrating physical and virtual experiences in cultural tourism: an adaptive multimodal recommender system. IEEE Access 13:28353–28368 Chen Y (2022) Construction and application of music style intelligent learning system based on situational awareness. Math Probl Eng 2022:2689233 Cheng HT, Koc L, Harmsen J et al (2016) Wide & deep learning for recommender systems. In: Proceedings of the 1st workshop on deep learning for recommender systems, pp 7–10 Cho H, Mandava D, Liu Q et al (2012) Situation-aware on mobile phone using co-clustering: algorithms and extensions. In: Proceedings of the 7th international conference on ubiquitous intelligence and comput­ ing. Springer, pp 272–282 Chunhua Z, Xiaofeng G, Yue S et al (2019) An attention-based deep learning situation information recom­ mendation model. In: Proceedings of the 2019 international conference on information science and control engineering (ICISCE), pp 174–178 Ciaramella A, Cimino MG, Lazzerini B et al (2010) Using context history to personalize a resource recom­ mender via a genetic algorithm. In: 2010 10th international conference on intelligent systems design and applications. IEEE, pp 965–970 Covington P, Adams J, Sargin E (2016) Deep neural networks for Youtube recommendations. In: Proceedings of the 10th ACM conference on recommender systems. ACM, RecSys ’16, pp 191–198 D’Aniello G, Gravina R, Gaeta M et al (2022) Situation-aware sensor-based wearable computing systems: a reference architecture-driven review. IEEE Sens J 22(14):13853–13863 Dey AK (2001) Understanding and using context. Pers Ubiq Comput 5:4–7 Dötterl J, Bruns R, Dunkel J (2017) Incorporating situation awareness into recommender systems. In: Inter­ national conference on enterprise information systems, SCITEPRESS, pp 676–683 Dridi R, Zammali S, Arour K (2016) Situation-aware rating prediction using fuzzy rules. In: Proceedings of the international conference on advanced data mining and applications, pp 209–221 Endsley MR (1995) Toward a theory of situation awareness in dynamic systems. Hum Factors 37(1):32–64 Endsley MR (2023) Ironies of artificial intelligence. Ergonomics 66(11):1656–1668 Endsley MR, Jones DG (2024) Situation awareness oriented design: review and future directions. Int J Hum Comput Interact 40(7):1487–1504 Feng YH, Teng TH, Tan AH (2009) Modelling situation awareness for context-aware decision support. Expert Syst Appl 36(1):455–463 Gao C, Li S, Zhang Y et al (2022) KuaiRand: an unbiased sequential recommendation dataset with randomly exposed videos. In: Proceedings of the 31st ACM international conference on information and knowl­ edge management, pp 3953–3957 Ge Y, Liu S, Fu Z et al (2024) A survey on trustworthy recommender systems. ACM Trans Recommend Syst 3(2):1–68 Gomez-Uribe CA, Hunt N (2015) The Netflix recommender system: algorithms, business value, and innova­ tion. ACM Trans Manag Inf Syst 6(4):1–19 Guo M (2024) Personalised recommendation of literary learning resources based on a mixed recommenda­ tion of learning interest and contextual awareness. J Inf Knowl Manag 23(4):2450055 Hariri N, Mobasher B, Burke R (2013) Query-driven context aware recommendation. In: Proceedings of the 7th ACM conference on recommender systems, pp 9–16 Harper FM, Konstan JA (2015) The MovieLens datasets: history and context. ACM Trans Interact Intell Syst 5(4):1–19

<!-- page 37 -->

Page 37 of 38 101 Situation-aware recommender systems: a systematic review and… Hu X, Deng J, Zhao J et al (2015) SAfeDJ: a crowd-cloud codesign approach to situation-aware music deliv­ ery for drivers. ACM Trans Multimedia Comput Commun Appl 12:1–24 Husak M (2021) Towards a data-driven recommender system for handling ransomware and similar incidents. In: Proceedings of the 2021 IEEE international conference on intelligence and security informatics (ISI) Husák M, Sadlek L, Špaček S et al (2022) CRUSOE: a toolset for cyber situational awareness and decision support in incident handling. Comput Secur 115:102609 Iwasaki H, Mizuno N, Hara K et al (2010) User-adapted recommendation of content on mobile devices using Bayesian networks. IEICE Trans Inf Syst 93(5):1186–1196 Jannach D, Jugovac M (2019) Measuring the business value of recommender systems. ACM Trans Manag Inf Syst TMIS 10(4):1–23 Jannach D, Zanker M, Fuchs M (2014) Leveraging multi-criteria customer feedback for satisfaction analysis and improved recommendations. Inf Technol Tour 14(2):119–149 Jiang Y (2024) Research on new economic marketing model system based on computer intelligent recom­ mendation algorithm. In: Proceedings of the 2024 IEEE 3rd international conference on electrical engi­ neering, big data and algorithms (EEBDA), pp 1290–1294 Kacprzyk J, Belyakov S, Bozhenyuk A et al (2021) Knowledge representations for constructing chains of contexts in geographic information systems. Int J Comput Intell Syst 14(1):1388–1395 Karlsen R, Andersen A (2019) Recommendations with a nudge. Technologies 7(2):45 Kim M, Kim M (2009) A formal definition of situation towards situation-aware computing. In: World summit on knowledge society. Springer, pp 553–563 Kokar MM, Matheus CJ, Baclawski K (2009) Ontology-based situation awareness. Inf Fusion 10(1):83–98 Kulkarni S, Rodd SF (2020) Context aware recommendation systems: a review of the state of the art tech­ niques. Comput Sci Rev 37:100255 Liang S, Liu M, Dong Z et al (2024) Spatiotemporal graph convolutional neural network-based text recom­ mendation by considering situational awareness. IEEE Access 12:134427–134438 Lim T (2012) Designing the next generation of mobile tourism application based on situation awareness. In: Proceedings of the 3rd Southeast Asian network of ergonomics societies conference (SEANES) Li J, Sun P, Jiang C et al (2025) A situation-aware enhancer for personalized recommendation. In: Proceed­ ings of the 2025 international conference on database systems for advanced applications, pp 99–114 Lv Y, Wang S, Jin B et al (2023) Deep situation-aware interaction network for click-through rate prediction. In: Proceedings of the 17th ACM conference on recommender systems, pp 171–182 Mateos P, Bellogín A (2024) A systematic literature review of recent advances on context-aware recom­ mender systems. Artif Intell Rev 58:20 Nwiabu N, Allison I, Holt P et al (2011) Situation awareness in context-aware case-based decision support. In: 2011 IEEE international multi-disciplinary conference on cognitive methods in situation awareness and decision support (CogSIMA). IEEE, pp 9–16 Page MJ, McKenzie JE, Bossuyt PM et al (2021) The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ 372 Qin J, Zhang W, Wu X et al (2020) D2k: Turning historical data into retrievable knowledge for click-through rate prediction. In: Proceedings of the 29th ACM international conference on information & knowledge management, pp 2685–2692 Richards C (2020) Boyd’s OODA loop. Necesse 5(1):142–165 Richthammer C, Pernul G (2020) Situation awareness for recommender systems. Electron Commer Res 20(4):783–806 Schilit BN, Theimer MM (1994) Disseminating active map information to mobile hosts. IEEE Netw 8(5):22–32 Srivastava D, Kolb J, Feigh K (2024a) Impact of abstraction levels of context information on AI-advised decision making for an entry descent and landing task. In: Proceedings of the AIAA Scitech 2024 Forum Srivastava D, Lilly J, Feigh K (2024b) Exploring the role of judgement and shared situation awareness when working with AI recommender systems. Cognition, technology and work Szczerbak M, Toutain F, Bouabdallah A et al (2014) KRAMER: new social medium based on collaborative recognition of important situations. Comput J 57(9):1296–1317 Tavakolifard M (2009) Situation-aware trust management. In: Proceedings of the 2009 ACM symposium on applied computing, pp 413–416 Tzanetakis G, Cook P (2002) Musical genre classification of audio signals. IEEE Trans Speech Audio Process 10(5):293–302 Villegas N, Sánchez C, Díaz-Cely J et al (2018) Characterizing context-aware recommender systems: a sys­ tematic literature review. Knowl Based Syst 140:173–200 Viswanathan S, Boulard C, Bruyat A et al (2022) Situational recommender: are you on the spot, refining plans, or just bored? In: Proceedings of the 2022 ACM conference on recommender systems

<!-- page 38 -->

101 Page 38 of 38 L. Aliberti et al. Wang S, Zhang X, Wang Y et al (2024) Trustworthy recommender systems. ACM Trans Intell Syst Technol 15(4):1–20 Wang H, Lu Y, Zhai C (2011) Tensor factorization for multi-criteria recommender systems. In: Proceedings of the 2011 IEEE 11th international conference on data mining. IEEE, pp 1248–1253 Wu F, Qiao Y, Chen JH et al (2020) Mind: A large-scale dataset for news recommendation. In: Proceedings of the 58th annual meeting of the association for computational linguistics, pp 3597–3606 Ye J, Dobson S, McKeever S (2012) Situation identification techniques in pervasive computing: a review. Pervasive Mob Comput 8(1):36–66 Zhang H, Qin X, Zheng H (2018) Terminals research and implementation of agricultural information recom­ mendation system based on situational awareness. J Phys Conf Ser Zhang H, Qin X, Zheng H (2020) Research on contextual recommendation system of agricultural science and technology resource based on user portrait. J Phys Conf Ser 012186 Zhao Y (2022) Research on context-aware recommendation algorithm based on RFID application. In: Lec­ ture notes of the institute for computer sciences, social informatics and telecommunications engineer­ ing, pp 313–327 Zheng Y (2017) Situation-aware multi-criteria recommender system: using criteria preferences as contexts. In: Proceedings of the 12th ACM conference on recommender systems, ACM, pp 689–692 Zhou C, Shen J, Wang Y et al (2020) Battlefield situation information recommendation based on recall- ranking. Intell Autom Soft Comput 26(6):1429–1440 Zhou C, Shen J, Guo X et al (2021) Task-oriented battlefield situation information hybrid recommendation model. Intell Autom Soft Comput 27(1):127–141 Zhu H, Li X, Zhang P et al (2018) Learning tree-based deep model for recommender systems. In: Proceed­ ings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining, pp 1079–1088 Zimmermann A, Lorenz A, Oppermann R (2007) An operational definition of context. In: Modeling and using context: 6th international and interdisciplinary conference, CONTEXT 2007, Roskilde, Denmark, proceedings. Springer, pp 558–571 Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Authors and Affiliations Luca Aliberti1 · Giuseppe D’Aniello1 · Matteo Gaeta1 Luca Aliberti laliberti@unisa.it Giuseppe D’Aniello gidaniello@unisa.it Matteo Gaeta mgaeta@unisa.it 1 Department of Information and Electrical Engineering and Applied Mathematics, University of Salerno, Via Giovanni Paolo II 132, 84084 Fisciano, Salerno, Italy
