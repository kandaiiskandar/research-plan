# An operational risk awareness tool for small fishing vessels operating in harsh environment

> **Source PDF:** `An operational risk awareness tool for small fishing vessels operating in harsh environment.pdf` · **Pages:** 17 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Contents lists available at ScienceDirect

Reliability Engineering and System Safety

journal homepage: www.elsevier.com/locate/ress

An operational risk awareness tool for small fishing vessels operating in harsh environment

Vindex Domeh a, Francis Obeng a, Faisal Khan a,b,*, Neil Bose c, Elizabeth Sanli d

a Center for Risk, Integrity, and Safety Engineering (C-RISE), Faculty of Engineering and Applied Science, Memorial University of Newfoundland, St. John’s, NL, Canada b Mary Kay O’Connor Process Safety Center, Artie McFerrin Department of Chemical Engineering Texas A&M University, College Station, TX, USA c Department of Ocean and Naval Architectural Engineering, Faculty of Engineering and Applied Science, Memorial University of Newfoundland, St. John’s NL, Canada d Ocean Safety Research, School of Maritime Studies, Fisheries and Marine Institute of Memorial University of Newfoundland, St. John’s NL, Canada

### A R T I C L E I N F O

### A B S T R A C T

Keywords: Situational or situation awareness (SA) Probabilistic safety assessment Bayesian network (BN) Small fishing vessels (SFV) Risk analysis Fishing accidents Reliability

Probabilistic safety assessment using the Bayesian network (BN) has emerged as a popular method for developing risk analysis tools. The method allows for risk-influencing factors from several areas to be captured probabi­ listically, enabling an easy-to-use safety assessment tool to be developed. Meanwhile, because the resulting tool is a BN model, the use of subject-matter experts in eliciting probabilities for the conditional probability tables (CPT) makes the method subjective. The subjectivity makes the tool’s output result less reliable since different experts rarely produce the same probabilities for CPTs. Therefore, the present study proposed a probability-scoring scale that uses pre-determined scores to assign probabilities to CPTs. Using the scale ensures that different experts working on a common CPT produce identical probabilities. That way, the variability amongst experts’ results is minimised while the reliability of a BN’s output result increases. The scale was applied to a BN-based risk- awareness (RAw) tool developed for monitoring safety aboard small fishing vessels (SFV). Advanced safety monitoring equipment is lacking aboard many SFVs, especially those in developing countries. Hence, the RAw tool developed in the present study demonstrates how the probabilistic safety assessment method could be leveraged to equip SFVs with safety monitoring tools. The study will benefit SFV owners and operators, the commercial fishing industry, and maritime administrations in charge of ensuring safety aboard SFVs.

## 1. Introduction

accident scenarios at sea. Several SFV accidents have been recorded [5, 6] because of the lack of adequate SA information, leading to several cases of fisher injury, death, and loss of vessels at sea. In fishing safety publications [4–8], the SFV sector has been identified for minimising the high fatality rate in the global fishing industry.

The availability of situational (or situation) awareness (SA) infor­ mation is a significant step in mitigating accident occurrences in risky industries. Around 71% of human error occurrences in the maritime sector could be blamed on the lack of SA information. From Sharma et al. [1], SA is an individual’s continuous awareness of the ongoing events within an incident. Thus, with adequate SA information, humans in charge of systems and operations are better equipped to take decisions. Like other transport systems, marine vessels rely heavily on equipment to gather the SA information required for navigation and safety moni­ toring. While marine vessels employed in shipping and industrial fishing have sufficient safety equipment, the same cannot be said for most small fishing vessels (SFV) within the commercial fishing fleet [2–4]. As a result, some SFVs lack adequate SA information to properly monitor

The definition of SFV varies a lot in the publications. Generally, the SFV is known as a fishing boat with an overall length not exceeding 12—15 m [9]. In other parts of the world too, the gross tonnage is the basis for differentiating SFVs from the industrial-fishing vessels [10]. The gross tonnages are small with a typical example being the 30 tons fishing boat used in Budiyanto et al. [10] to study the cooling perfor­ mance of fish holds aboard SFVs. Most SFVs use traditional methods to harvest fish and propel the boat. Some, however, have been modernized by using outboard engines for propulsion. Still, very little change can be observed in the fish harvesting methods handed down to the fishers by

Abbreviations: BN, Bayesian network; CPT, Conditional probability table; DMS, Database management system; OOP, Object-orientated programming; OCS, Operational conditions at sea; RAw, Risk awareness; SA, Situation (or situational) awareness; SFV, Small fishing vessel; SME, Subject-matter expert.

* Correspondence author. E-mail address: fikhan@tamu.edu (F. Khan).

https://doi.org/10.1016/j.ress.2023.109139 Received 5 November 2022; Received in revised form 23 January 2023; Accepted 1 February 2023

Available online 4 February 2023 0951-8320/© 2023 Elsevier Ltd. All rights reserved.

<!-- page 2 -->

Reliability Engineering and System Safety 234 (2023) 109139

their forefathers. For those SFVs with outboard engines, some have lengths exceeding 15 m. Although SFVs are the most populous in com­ mercial fishing, their operation is not thoroughly regulated like industrial-fishing vessels or shipping vessels. As a result, the use of safety equipment aboard SFVs is sometimes left at the will of boat owners and operators. This class of marine vessels need safety equipment adapted to their operations to help curb the frequent accidents they experience at sea.

fishing accidents they encounter during voyages. The fishers have gained this knowledge through years of experience in fishing. Mean­ while, Abdullah-Bin-Farid et al. [17], Braga and Schiavetti [18], and Wekke and Cahaya [19] identified that these fishers have low educa­ tional levels, usually not beyond the high school level. Therefore, to make the RAw tool user-friendly, the present study adopted the cause-effect modelling approach for developing the tool. The risk factors were identified as causes, while fishing-accidents became the effects. The literature review uncovered the SA information that presents the scenarios under which risk factors translate into fishing accidents. In defining accident scenarios, Animah and Shafiee [20] discussed how helpful literature on the subject matter could be, especially at the initial stages of a research study. In that vein, the present study’s use of liter­ ature for cause-effect modelling could be considered satisfactory. Hence, the RAw tool is primarily a cause-effect model. Fishers only have to input the risk factors (i.e., technical, environmental, and human-related factors)—the tool then identifies the fishing accidents and associated conducive conditions (i.e., the SA information).

The present study developed a risk awareness (RAw) tool in the Bayesian network (BN) to contribute to the inadequate equipment for safety monitoring aboard SFVs. The RAw tool, when engaged, connects risk factors to fishing accidents through SA-information. That way, the SA information—not readily available—could be traced back to the risk factors. Consequently, appropriate control measures can be imple­ mented to forestall the SA realised and avoid a possible fishing accident. In the study, risk factors are the active failures and categorised broadly into technical factors (i.e., operational activities related to fishing and the vessel and machinery running), environmental factors (i.e., the marine and onboard environmental conditions and elements within), and human-related factors (i.e., human commissions and omissions). Often, fishers are previewed to these factors but may not know how they combine as SA to cause a fishing accident. Hence, SA-information de­ scribes SA with the potential to cause a fishing accident. Once the tool identifies the prime SA-information, fishers can trace back to the conducive condition(s) onboard, favouring their existence. The fishing accident, which is either vessel-related (e.g., capsize, grounding, fire and explosion, etc.) or fisher-related (e.g., injury, person overboard, death, etc.), can now be mitigated by eliminating the conducive condition.

The RAw tool development is the practical contribution made by the present study to SFV’s operational safety. Theoretically, the study contributed to the existing knowledge on probabilistic safety assessment applications by demonstrating the tool’s functionality in safety moni­ toring aboard an SFV. Publications in that area are quite scarce. The probability scoring scale introduced for conditional probability elicita­ tion to achieve higher reliability in BN modelling [5,21] is another theoretical contribution made by the study. When the CPTs are filled using the proposed scale, each time fishers activate the prevailing risk-factor states in the tool, fishing accidents and SA-information are assigned percentages ranging from zero to 100%. When the estimated percentage for a fishing accident is 100% or closer, the interpretation is that a conducive condition exists onboard, which could cause the acci­ dent. Furthermore, an SA-information with an estimated percentage of exactly 100% or closer is considered critical and more likely to trigger an accident. Such SA information must be controlled first to lower the chances of a fishing accident occurring.

By developing the RAw tool and demonstrating its implementation, the present study aims to provide SFV skippers, owners, and maritime administrations in charge of fishing safety with a digital tool to create awareness about the conducive conditions existing aboard for fishing- accident occurrence while on a voyage. The tool shows how the prob­ abilistic safety assessment method could be leveraged to build digital tools for safety monitoring aboard marine vessels, particularly SFVs. Subjectivity is a current challenge in probabilistic safety assessment using BN. The challenge arises due to subject-matter experts’ engage­ ment to elicit probabilities for the conditional probability tables (CPT). As seen in Sonal and Ghosh [11] and Elidolu et al. [12], multiple experts providing probabilities for a CPT produce different dataset per expert. The variability in resulting datasets raises questions about consistency in the conditional probability elicitation approach and the reliability of the output result from BN.

The remainder of the paper is organized as follows; section two is next and discusses the literature on fishing accidents, their causation factors, and the BN modelling approach. The RAw tool development is explained in section three, together with its case study application. Then, section four discusses the case study results and the study limi­ tations. Finally, section five, the concluding section, presents the main findings, the key message, and future research directions.

In addition to the statistical methods available for addressing the variability challenge, the present study proposes using a probability scoring scale. The scale with predefined probability scores and objective guidelines on choosing a score purpose to eliminate subjectivity on the experts’ side, minimise (if not avoid) variability in conditional proba­ bilities elicited, and boost the reliability of BN result. That way, more trust would be repose in the outcome of a BN modelling for probabilistic safety assessment. Just as machinery reliability [13] continues to receive considerable attention in research, so, by proposing this scoring scale, the present study also aims to further the discussion on the reliability of probabilities elicited for CPTs in BN.

## 2. Literature review

The current section discusses the literature on fishing accidents and their contributing factors and explains BN modelling before it is used in Section three. The review aimed at providing enough background for the particular probabilistic safety assessment approach used in the cause- effect modelling that resulted in the BN model named, RAw tool. The probability scoring scale introduced is also explained in detail here.

### 2.1. Fishing accidents and the causation factors

The specific objectives the study tackled are as follows: (1) To demonstrate how the fishers’ experience at sea and the existing litera­ ture on how fishing accidents occur can be consolidated to develop the RAw tool for SFV operational safety monitoring purposes, (2) To use the RAw tool to facilitate decision-making about the time-to-time dangerous situations that fishers at sea must be aware of in advance, and (3) To leverage on the RAw tool’s capabilities, to design a safety monitoring programme for SFVs. These objectives provided answers to the ques­ tions—what fishing accidents are the most probable at a given time­ —what situations are the drivers of the identified fishing accidents?

Commercial fishing is counted amongst the world’s occupations with the high number of employee deaths and injuries [5,6,8]. In Case et al. [22], commercial fishing in the United States of America (USA) recorded 86 deaths per 100,000 employees in 2016. This fatality rate was sig­ nificant because it was 23 times more than the fatality rate for all USA employees in the period. Similarly, Byard [23] study in 2012 says commercial fisher deaths were 52.4 times more than fatality rates for other British sector employees in the United Kingdom. In 2003, South Africa also published a fatality rate of 162 yearly—meaning at least one fisher dies every two days [24]. The rates in other countries, like Australia, Canada, New Zealand, Norway, Poland, and Sweden, are no different [24,25]. Fishing accidents are, thus, a global challenge and are

Thorvaldsen [14] and other researchers [15,16] mentioned that fishers in the SFV sector have rich knowledge about the risk factors and

<!-- page 3 -->

Reliability Engineering and System Safety 234 (2023) 109139

fast diminishing the human workforce in the commercial fishing industry.

rounded rectangles, like, Poor Visibility or Officer-of-the-watch Lapses. Hence, such explicitly defined factors are the root causes of SFV Grounding, and the present study refers to them as risk factors. Poor Visibility, like other factors in the rounded rectangles, needs further breakdown to uncover their risk factors. These factors are still at the information stage, and the present study referred to them as SA infor­ mation. The SA information is challenging to conceive from a glance, mainly because, in reality, they occur with the simultaneous actions of several risk factors at the same time. For SFV fishers, who typically employ low monitoring technology and have a low educational back­ ground, the mental exercise of perceiving the individually occurring risk factors to culminate into an SA-information and, subsequently, an ac­ cident is the challenge to resolve when fishing. If only fishers could easily connect vibration from equipment (or machinery) to Officer-of- the-watch Lapses, fishers can conclude that a conducive condition ex­ ists aboard for Grounding to occur. Fishers would then take appropriate steps to find the onboard situation responsible for the vibration and address it. In that regard, the cause-effect model has been worthwhile.

Table 1 presents some fishing accidents in the last three decades. Besides the deaths and injuries, vessel losses are also a major conse­ quence of fishing accidents. Hence, solutions to curb fishing-accident occurrences must consider both the human and vessel perspectives. Broadly, fishing-accident resulting in damage to the vessel is called a vessel accident, while if causing injury to fishers or leads to fisher deaths, the fishing accident is referred to as a personal accident [5,6,26, 27]. Meanwhile, the studies of U˘gurlu et al. [5], Roberts [6] and Domeh et al. [26] show that, often, the bulk of the fishing accidents (see Table 1) are traced to the SFVs. In Byard [23], it is said that about 59% of fisher deaths realised at one time in the Danish fisheries were linked to the SFV group. With Table 1 showing evidence of similar accidents in various parts of the world, alongside their happening even in the last four years, tools to envisage accident causation factors before they result in the accident are undoubtedly needed.

The literature on fishing accidents abounds. They can be sourced from as far back as the 1960s [35,36,37] to as recent as the 2020s [5,38, 39]. Studying these publications to unveil the accident causation factors is cost-effective and saves time. Additionally, because the authors of these publications are diverse in location, educational background, and objective of their studies, the literature survey helps to analyse fishing-accident causes from several perspectives. A field study typically would localise the accident’s causes and not give complete information about the various ways the accident could happen. Comprehensive in­ formation on fishing-accident causalities is an excellent way to match the causes to typical accident types. When the accident causes are traced to root causes, the technical (which involves operational matters), environmental, and human-related factors at the forefront of fishing-accidents occurrences are identified. Building a cause-effect relationship is then possible and could become a valuable tool for fishers to connect the daily happenings at sea to potential fishing acci­ dents. That way, SFV fishers can proactively correct onboard situations to avoid a fishing-accident occurrence.

In the methodology section, the present study followed the above procedure to define risk factors and SA information for the various fishing accidents encountered by SFVs. The resulting cause-effect model was later transformed into a BN to become the RAw tool by putting together all the risk factors and SA information.

### 2.2. Bayesian network modelling

The BN is a directed acyclic graphical model excellent at represent­ ing causal relationships in which probabilistic safety assessment is the objective. In recent times, probabilistic safety assessment [40,41] has emerged as a useful method in identifying the risk influencing factors responsible for an incident. Apart from identifying risk factors, their occurrence rate updating and the most probable accident scenarios an­ alyses [42,43,44] are also studied in probabilistic safety assessment. The BN has a data-driven modelling capability that makes possible all these tasks, and as such, it is highly favoured by researchers undertaking probabilistic safety assessments. Fan et al. [43] used BN to develop a human factors analysis tool for marine vessels. The tool facilitated the human error rate prediction for different ship types and accident sce­ narios. Yu et al. [45] used BN to bring together factors from multiple sources, resulting in a data-driven model that estimated the overall risk of ships in coastal waters. Animah and Shafiee [20] also commended the flexibility BN offers in merging information elements of diverse back­ grounds. Moreso, the modelling of ships colliding with offshore in­ stallations was also done by Yu et al. [46] using BN. The application areas of BN are numerous; BN presents a straightforward way for data-driven tools development for probabilistic safety assessment. Later in the methodology section of the present study, BN was used to develop the RAw tool proposed for safety monitoring purposes aboard SFVs through probabilistic safety assessment.

Fig. 1 is an example model of a cause-effect relationship for a fishing accident, Grounding. Information to develop the model was sourced from Byard [23]: “Grounding on rocks or at harbour entrances has been documented in conditions of poor visibility or at night when watchmen were either fatigued or had fallen asleep. Fatigue is contributed to by long working hours at sea with short rest periods, cramped sleeping spaces, interruption of sleep by engine noise and vibration and the effects of heavy seas.” The arcs in the figure extend from a cause factor to the effect, resulting in a cause-effect diagram for SFV Grounding based on factors abstracted from the italicised information.

From the diagram in Fig. 1, Poor Visibility and Shallow Waters are environmental factors, while Officer-of-the-watch Lapses, Fatigue, and Sleep Interruption, have direct human involvement, so they qualify as human factors. Although the Time of Day has an environmental connotation, the factor also provides a physically immersive work experience so that it could be viewed as a technical factor. Meanwhile, all these factors are brought about by operational conditions (i.e., the factors of space, time, and force concerning a given objective), as evident in the factors within the ellipses. As an example, if not for operational conditions of working long hours and machinery running to cause vibration, the SA information, Fatigue and Sleep Interruption would not emerge, triggering Officer-of-the-watch Lapses and, eventu­ ally, Grounding. Thus, operational conditions often are the underlying causes for the technical, human, and environmental factors resulting in fishing accidents aboard SFVs. For easy identification, however, the present study in section three broadly grouped SFV accident causality into technical, human, and environmental factors; then, within each group, the typical operational conditions were defined.

In BN, information describing the cause-effect relationship is repre­ sented by nodes bearing their respective names. Each node is also given states (which vary from two onwards) to tell the occurrence or non- occurrence of the information. Arcs are then extended from one node to another to realise the network structure for the relationship under study. Two kinds of nodes are in a BN model: child and parent nodes. An arc can only be extended from a parent node to the respective child node; the opposite is not allowed due to the acyclic nature of BN. Hence information only flows from parent nodes to child nodes. In Fig. 2, an example BN model is shown for the “Sleep interruption” information in Fig. 1. The “Engine noise”, “Heavy sea”, and “Equipment/machinery Vibration” factors being the information describing “Sleep interruption” are the parent nodes while the later, is the child node.

Data-driven decision-making is made possible in BN models through the estimation of percentage scores that can be used to infer the chances of a situation happening. To do the estimation, child nodes have CPTs that establish the mathematical relationship between parent and child

Furthering the discussion in Fig. 1, the factors in ellipses, for example, Short Rest, Engine Noise, or Harbour Entrance, are explicitly defined. Fishers can identify with them more quickly than those in the

<!-- page 4 -->

**Table 1 Summary record of sampled fishing accidents in publications.**

Researcher Investigation Fishing Accident Region of period accident consequence occurrence

Bye and Lamvik [28] Reliability Engineering and System Safety Journal 1990 - 1999 Man overboard 34 fisher deaths Capsize 3 fisher deaths Collision 5 fisher deaths Grounding 9 fisher deaths Drowning 16 fisher deaths Wang et al. [27] Accident Analysis & Prevention Journal 1994 – 1999 Machinery damage 128 fisher deaths United Foundering and 179 vessels lost Kingdom flooding Collision and contact Fire and explosion Capsize and list Heavy weather damage flooding McGuinness et al. [25] Safety Science Journal 1990 – 2011 Capsize 281 fisher deaths Norway Foundering Collision Grounding Crush/impact Drowning Man overboard

Kum and Sahin [29] Safety Science Journal 1993 – 2011 Occupational In all: 30 accidents, Canada, accident 27 injuries, 1fisher Greenland, Collision death Russia Grounding Federation, Machinery failure USA, Flooding/foundering Denmark, Fire and explosions Iceland Capsizing Arctic Council [30] Arctic Marine Shipping Assessment 2009 Report 1995 - 2010 Collision 108 accidents in total Circumpolar Smith et al. [31] Proceedings of the ASME 2015 34th International Conference Grounding north region on Ocean, Offshore and Arctic Engineering Fire and explosion Machinery failure in Canada, Grounding Sinking Faroe Machinery failure Islands, USA, Rezaee et al. [32] Ocean & Coastal Management Journal Iceland, Khan et al. [33] Reliability Engineering and System Safety Journal Norway Roberts [6] Accident Analysis & Prevention Journal 1996 - 2000 Man overboard 32 fisher deaths United Kingdom Capsize 59 fisher deaths Collision 5 fisher deaths Grounding 14 fisher deaths Fire and explosion 3 fisher deaths Struck by gear 10 fisher deaths, injury Struck by waves 6 fisher deaths, injury Entangled in gear 11 fisher deaths Asphyxiated by 4 fisher deaths fumes

U˘gurlu et al. [5] Ocean Engineering Journal 2008 - 2018 Man overboard 20 fisher deaths Europe, Collision 29 fisher deaths, Australia, 17 vessels lost; Sinking 37 fisher deaths, Canada 44 vessels lost; Grounding 12 fisher deaths, 14 vessels lost; Fire and explosion 1 fisher death, 10 vessels lost; Occupational injury 21 fisher deaths, 1 vessel lost Sinking 37 fisher deaths, Paolo et al. [34] Transportation Research Procedia 2009 – 2019 Capsize 23% Vessel lost Worldwide Collision 32% fisher deaths Damage to vessel Fire Flooding Grounding Machinery failure Occupational/work accident

<!-- page 5 -->

Reliability Engineering and System Safety 234 (2023) 109139

**Fig. 1. A cause-effect diagram for SFV Grounding (in yellow) showing direct failures in rounded rectangles and indirect failures in ellipses.**

**Fig. 2. A BN model for “Sleep interruption” scenario aboard an SFV.**

nodes. These CPTs must be filled with probability values, which, as mentioned in section one, is usually done by subject-matter experts [5, 21]. In the present study, however, the scoring scale in Fig. 3 is proposed to replace the expert elicitation approach. Using the scale would help minimise (if not remove) the variability in different expert scores when assigned the same CPT. Thus, the scale presents an objective approach to eliciting probabilities for CPTs in BN.

probabilistic. Certainty scores, one or zero, are issued if all parent nodes indicate only occurrence or non-occurrence states, respectively. The probabilistic scores are used instead when the states for parent nodes are a mix of occurrence and non-occurrence. Depending on the number of non-occurrence states in the mix, the choice score may be low-impact, medium-impact, or high-impact. High-impact scores must be selected for the least number of non-occurrence states in the mix. Medium- impact score will be the best choice as the number of non-occurrence states increases in the mix. However, if the non-occurrence state num­ ber is greater than the occurrence state number in a mix, the score would come from low impact.

From Fig. 3, the scale has mainly two score types, certainty and

As also shown in Fig. 3, within each probabilistic score class, two scores exist from which the analyst (or expert) would decide whether to give a low (X) or a high (Y) score. For the situation where the occurrence states outnumber the non-occurrence states, the “Y” score must be assigned. The “X” will be the chosen score in the opposite situation. Where there is a tie in the state types number, the analyst may decide between “X” and “Y” in the medium-impact class through consideration for the severity of the child node impact on the incident (e.g., a fishing accident) under study. If complete objective elicitation is desired, the subjectivity could be avoided using the mean score of 0.53. Also, the number of parent nodes connected to the child node can be controlled by object-orientated programming to prevent the tie situation from surfacing. The scoring approach described is based on the proposed scale and drives objectivity when eliciting probabilities for CPTs. Ultimately,

**Fig. 3. The proposed scale for eliciting probabilities required in a CPT.**

<!-- page 6 -->

the scale aims at eliminating variability in expert scores for CPTs. Reliability is then enhanced, and more trust is reposed in the model outcome result.

percentage scores for leaf and intermediate nodes in the network. Probabilistic safety assessment tools to aid accident monitoring aboard SFVs are scarce in the literature, so the development of the RAw tool is a significant contribution in that regard. As mentioned in section one, the percentage scores only give quantitative measurements for the likeli­ hood of a fishing accident and the presence of conducive conditions aboard the SFV, favouring the accident.

Let us demonstrate the proposed probability scoring approach using the example BN in Fig. 2. Each node has two states: Engine noise, “High/ Low”; Heavy sea, “Yes/No”; Equipment vibration, “High/Low”; and Sleep interruption, “Possible/Not-possible”. The goal is to develop the CPT for “Sleep interruption”, the child node, and then fill the CPT with probability scores. From Eq. (1), eight probability values are expected at the “Possible” state of the “Sleep interruption” node. Once the “Possible” state probability score is subtracted from one, the corresponding prob­ ability for the “Not-possible” state is realised. That is to say, the sum of probabilities for a node’s occurrence and non-occurrence states is equal to one. Using the proposed scale and following the procedure described earlier, the analyst (or expert) would score the probabilities in the last two columns of Table 2. Therefore, Table 2 is the CPT with the elicited probabilities for the “Sleep interruption” node. With the CPT filled, once prior probabilities are entered for each parent node, the total proba­ bility, Eq. (2), is used to estimate the percentage score that defines the likelihood of “Sleep interruption” occurring (i.e., the “Possible” state score).

The BN modelling done here is also different from those of U˘gurlu et al. [5], Domeh et al. [26], and Obeng et al. [38] due to the application of the proposed probability scoring scale, which adds to the scholarly contribution made by the present study to the existing BN modelling methodologies [21,47]. By applying the proposed scoring scale in Fig. 3, the study presents a more objective viewpoint for experts’ judgement when eliciting probabilities for CPTs. Compared with other expert elicitation approaches [43,45,46], the present one aims for consistency and reliability in experts’ judgement.

In section 2.2, BN modelling was discussed in detail. The current section describes the step-by-step procedures employed to develop the RAw tool as a BN model. The methodology framework is described first.

### 3.1. Framework to develop the RAw tool

```math
NCPT = 2np
(1)
```

The concept framework to develop, operate, and maintain the RAw tool, is shown in Fig. 4. In all, five steps are involved: information ele­ ments identification (Step 1), cause-effect database design (Step 2), the RAw tool development (Step 3), voyage situation assessment (Step 4), and maintaining the RAw tool (Step 5). Before starting the database design, verifying if sufficient information elements have been identified is essential. That was achieved through inspection to ensure no obvious fishing-accident type, SA-information, or risk factor was left out of the identified elements from Step 1. After the tool has been developed and used, it is crucial to constantly enquire if new accident types have emerged or information elements have changed. That way, Step 4 would be relevant and help keep the tool up-to-date with future changes in fishing safety aboard an SFV. If no new knowledge is discovered about fishing safety aboard SFVs, then Step 5 will be skipped to end the ac­ cident monitoring. At the higher-level, Fig. 4 is sectioned into three: Steps 1 to 3, the aim is to develop the RAw tool; Step 4, demonstrates the RAw tool in an application; and Step 5 is aimed at updating the RAw tool so that it remains relevant to current and future fishing safety needs. In the proceeding sections, each step is described in more detail.

where, NCPT is the number of probability scores expected in the child node states if each parent node has exactly two states, and np is the number of parent nodes connected to the child node.

```math
P(A) = P(A) × P(A|B = occurred) + P(A) × P(A|B = not −occurred)
(2)
```

where, A and B are two conditional events; P(A) is the total probability of event A; and P(A|B) is the conditional probability of A given the occurrence or nonoccurrence of B.

BN modelling has seen several applications in fishing safety studies. Domeh et al. [26] and Obeng et al. [38] used BN to model man over­ board and capsize scenarios for SFVs, respectively. Also, U˘gurlu et al. [5] used BN to model fishing vessel sinking and collision. Sotiralis et al. [47] developed a BN model that incorporates human factor issues into vessel collision incident. In all these researches, the subjective expert elicita­ tion procedure is used in eliciting probabilities for the CPTs involved. The BN developed for the RAw tool in the present study differs from those of previous researchers. That is because of the semi-objective approach adopted to elicit probabilities for CPTs, using the proposed scoring scale. By using the scale as described, variability in experts’ scores for CPTs could be minimised, reliability in experts’ scores enhanced, and more trust reposed in risk results from BN modelling. The following section discusses detailed information on the RAw tool development using the proposed scale.

### 3.2. Step 1: Information elements identification

The goal of this section was to define fishing-accidents and their information elements. The goal was achieved by surveying literature in Scopus, Google Scholar, and the databases of Fish, Fisheries and Aquatic biodiversity Worldwide. These databases hold several journals from various publishers studying commercial fishing. Also, to ensure credible information elements are sourced, only journal articles and conference papers from top-tier publishers and in English were used. The query statement used was “(Commercial OR Small) AND Fishing (Vessel OR Boat) AND Accident”. More than 105 thousand paper results were

## 3. The methodology to develop the RAw tool and the proposed monitoring programme

The method applied in developing the RAw tool is BN modelling, which uses probabilistic safety assessment [40,41] to estimate

**Table 2 CPT for the “Sleep interruption” node.**

Number Engine Heavy Equipment Score Sleep interruption

noise sea vibration type appropriate Possible state Not-possible state 1 High Yes High Y Certainty 1.00 0.00 2 High Yes Low Y High-impact 0.90 0.10 3 High No High Y High-impact 0.90 0.10 4 High No Low X Low-impact 0.15 0.85 5 Low Yes High Y High-impact 0.90 0.10 6 Low Yes Low X Low-impact 0.15 0.85 7 Low No High X Low-impact 0.15 0.85 8 Low No Low X Certainty 0.00 1.00

<!-- page 7 -->

Reliability Engineering and System Safety 234 (2023) 109139

**Fig. 4. The framework for developing and operationalising the RAw tool.**

realised when the query statement was executed. By prioritizing journal articles and conference papers, leading scientific journal types, studies primarily focused on fishing safety, leaving out review papers, and not going beyond twenty years back from 2023, the results were filtered to 28, which was used for the survey. For the selected papers, the text inside each paper was searched, and portions of relevance were copied, as demonstrated earlier in Section 2.1, paragraph four. Each copied text was mined by developing cause- effect diagrams similar to Fig. 1. Finally, the information elements realised from the diagrams were organised into Table 3; the complete information elements are in Appendix A1. In the table, active and latent failures have been captured under information elements whilst the person [48–50] and vessel-related [51] accidents became fishing acci­ dents. As a result, further review was done in Step 2 to realise the database used in developing the RAw tool.

Table 1 and Appendix A1 into SA-information and risk factors. That was achieved by inspecting the elements in the second column of Table 1 and Appendix A1 and putting those elements that are latent failures (e.g., human factor, poor visibility, and adverse weather) under SA- information. The remainder of the elements are active failures and, therefore, were noted under risk factors. Active failures are the everyday happenings at sea that fishers know because they are so evident and fundamental. However, the latent failures are implicit and would be triggered by the risk factors, so they are not evident to fishers.

The second objective was to identify SA-information without risk factors. A further literature search was conducted to define appropriate risk factors for such elements. Lastly, all risk factors were inspected, and those found to be advanced were replaced with replica ones. The reason for doing this is that the present study aimed at adapting the RAw tool to the safety monitoring needs of SFVs not using advanced safety equip­ ment and systems. Hence, technological systems like the global posi­ tioning system, automatic identification system, and high-frequency and medium frequency radios were considered too advanced and must be replaced. In Størkersen and Thorvaldsen [16] and Menakhem [37], it was discovered that SFV fishers had adopted practices that enabled fishers to perform the functions that the named advance systems do. The

### 3.3. Step 2: cause-effect database design

With Step 1 completed, three objectives were targetted in Step 2 to ensure a suitable database is realised for RAw tool development in Step 3. The first objective was to put the information elements collected in

<!-- page 8 -->

Reliability Engineering and System Safety 234 (2023) 109139

positioning system, automatic identification system, and very high-frequency and medium-frequency radios.

**Table 3 Fishing-accidents and associated information elements.**

To conclude Step 2, a database was designed to collate all the in­ formation elements realised from the activities of Step 2. The database had columns named risk factors, SA-information, and fishing accident. Each column held information elements of that type as its data. A summary of the resulting database is Table 4; the complete database is shown in Appendix A2. Information elements in the database were given state names, too, describing their occurrence and non-occurrence.

Number Information element Fishing-accident Citation

1 UKC*, squat effect, storm, navigation

Grounding [5,6,52–56]

error, alcohol use, fatigue, drifting ice, human error, poor visibility, adverse weather, and tall waves. 2 Operational status of GPS*, ECDIS *, Radar Navigation failure

[1,47,52, 57–59] AIS*, radio system (VHF/MF)*, steering system, communication channels (portable radios, PA systems*), signal lights, main engine controls on bridge, propulsion system, human error, paper nautical chart detection, and bridge system software malfunction. 3 Poor visibility, ambient temperature, seawater

### 3.4. Step 3: RAw tool development

This section was devoted to using the information in the database (see Appendix A2) to develop the RAw tool in the GeNIe software environment. GeNIe is a BN modelling software belonging to the BayeFusion Lab [63]. The lab has made available a free academic version of GeNIe for educational purposes. It is widely used in research publications; it was used by Yu et al. [45] in the BN model developed to assess the overall risk of ships in coastal waters. Being a BN model, the RAw tool was developed using chance nodes for all information ele­ ments except for risk factors. Decision nodes instead were used to define risk factors. The decision node type was used because, in operational­ ising the tool, the fisher is not expected to input numerical data. Instead,

Adverse weather [1,57,60]

temperature, wind speed, ocean current, sea swell, wave height, and sea surface appearance. 4 Adverse weather, loss of buoyancy (overloading,

**Table 4 Fishing accidents and their information elements.**

Sinking [5]

loss of watertightness, damaged pipelines, ice accretion on ship), and loss of intact stability (unstable loading, fishing gear operating, and ice accretion on ship). . . . . . . . . . . . . 20 Fuel shortage and engine breakdown.

Number Risk factor SA-information Fishing accident

1 Steering gear (Failed/ Working)

Difficult manoeuvring

Helm (Failed/Working) 2 Wind speed (Calm/ Light-air/Light-breeze/ Gentle

Ice drifting

-breeze/Moderate- breeze/Fresh- breeze/Strong-breeze/Near-gale/Gale /Gale Strong-gale/Storm-gale/Storm Violent-storm/Hurricane) Seasons (December-to-March/April-to-May/ June -to-September/October-to- November) Ocean current (Horizontal-current/Vertical-current) 3 Ocean type (Arctic- ocean/North-Atlantic- ocean/

Loss of power [27,37]

21 Adverse weather and loss of power.

Lost/stranded at sea

[27,37]

22 Lightning, engine room fire, fire fighting

Fire and explosion

[27,37]

Iceberg present

equipment failure, electric spark, cooking gas leakage, smoking, and lack of ventilation. 23 Human factor, burns, loss of finger or whole

Southern-ocean/Others) Seawater temperature (Cold/Warm) Seasons (December-to-March/April-to-May/ June -to-September/October-to- November) 4 aIceberg present Ship besetting aIce Drifting aDifficult manoeuvring 5 Behaviour in emergency (Unsafe/Safe)

[5,29,34,61, 62] limb, injury from sharp tools, knife use, negligence, fatigue, holding fish without gloves on, and beheading a life fish manually.

Occupational injury

Unheeded risk taking

* UKC: under keel clearance; GPS: global positioning system; ECDIS: electronic chart display and information system; AIS: automatic identification system; VHF: very high frequency; MF: medium frequency; and PA: public address.

Fishing know-how (Unsafe/Safe) Cultural practice (Unsafe/Safe) Understanding of modern fishing practices (Low/High) 6 Manual beheading of fish (Yes/No)

Injury from knife

systems broadly serve communication and identification purposes. Menakhem [37] also realised SFV fishers do the following to ultimately achieve the same purposes: “Able to use water colour to tell vessel location (Yes/No); Shouts to nearby vessels understood (Yes/No); Hearing whistle sound from nearby vessels (Yes/No); Seeing flags of other vessels (Yes/No); Seeing a fishing float or bobber (Yes/No); Paper nautical chart (Useable/Not-used); Flashing torchlight acknowledged by nearby vessels (Yes/No); Shouts from nearby vessels understood (Yes/No); and Able to use wind speed intensity and direction to tell vessel location (Yes/No)”. The present study saw these operations instead as befitting fishers running SFVs in remote communities. Accordingly, they replaced the advanced equipment for the global

Fish filleted manually (Yes/No) Fish gutted manually (Yes/No) Fish skinned manually (Yes/No) 7 Fishing gear shooting (Ongoing/Not- performed)

Man overboard (MOB) Working close to fishing gear (Yes/No) Fishing gear hauling (Ongoing/Not-performed) Guardrail (Low/High) Working area (Close-to-guardrail/Not-close-to-guardrail) Strolling (Close-to-guardrail/Not-close-guardrail) Drug use (Yes/No) Alcohol (Consumed/Not-consumed)

a Risk factors to the SA-information have been defined earlier.

<!-- page 9 -->

Reliability Engineering and System Safety 234 (2023) 109139

a fisher would choose amongst a node’s states based on the evidence gathered about the risk factor. Both chance and decision nodes had their names in the database inscribed on the nodes and were given state names too. Each node had at least two state names to tell its occurrence or non-occurrence. The number of states (or state names) depends on the physical states of the information element in real-life applications.

∏ n

```math
P(Xi|Parents(Xi))
(3)
```

P(X1, X2, …, Xn) =

i=1

where, Xi are the factors (i.e., fishing accidents, SA-information, and risk factors), n is the number of factors present, Parents(Xi) is the parents of Xi, P(X1, X2, …, Xn) is the joint probability, and P(Xi|Parents(Xi)) is the conditional probability.

Following the explanation in Section 2.2 about BN modelling and guided by the database information, the nodes were joined successfully. A fishing-accident node is a child node to its SA-information, and the SA- information is also a child to its risk factors. Ultimately, risk factors are the parent nodes. Because the nodes were so many due to the equally many information elements, object-orientated programming (OOP) was done to prevent the resulting network from becoming cumbersome and complicated. For a step-by-step approach to doing OOP in BN, the reader is encouraged to consult the studies of Domeh et al. [26] and Khan et al. [33]. For the present study, OOP was done by grouping risk factors into technical, environmental, and human risk factors. The submodel feature in GeNIe [63] was then used to capture these groupings into separate sub-networks. The resulting three sub-networks were further captured into a new sub-network called “Dynamic operational conditions at sea (Dynamic OCS)”, as shown in Fig. 5. In Appendices A2 and A3, the risk factors in each of the three subnetworks are shown.

### 3.5. Step 4: situation assessment aboard an SFV using the RAw tool

Now that the RAw tool has been developed, it is time to demonstrate how it will be used in practice. Three operations must be performed to illustrate how the tool works. First, field data must be collected on the fishing situation observed during the assessment. Second, using the data collected, the appropriate state names for risk factors in the tool must be activated and the tool run. Lastly, the results outputted by the tool must be analysed diagnostically to identify critical fishing accidents and their SA-information. The SA-information is what the onboard fishers would work towards de-escalating to avoid any potential accident. The following sections describe the hypothetical case study that shows how all three operations are performed.

The submodel feature was again engaged to put SA-information into three sub-networks: human-related SA, vessel-and-equipment SA, and prevailing-conditions SA. As the names imply, human activities, vessel and shipboard equipment operations, and the onboard and marine environmental conditions, which are SA-information in Appendix A2, were captured as fragments in the sub-networks. All the fishing acci­ dents were also captured as a separate sub-network, as shown in Fig. 6. Through further abstraction, the sub-networks for the three groups of SA-information, and the fishing accidents, were absorbed into a new sub-network called SA-scenarios sub-network. In all, sixteen fishing accidents and sixty-two SA-information were considered for SFV safety monitoring using 145 risk factors. The sixteen accident types considered are succinctly defined in Table 5 in the context of SFV operation.

3.5.1. The example case study Let us consider the case of a hypothetical SFV, single-decked, oper­ ating in Ghana’s territorial waters. Assume the SFV has no advanced safety monitoring equipment, and it is agreed to use the RAw tool at various time instants so that decision can be made regarding the pres­ ence of conditions favouring fishing-accident occurrence.

Ghana is a West African country boarded by Togo (on the east), Cote d’Ivoire (on the west), Burkina Faso (in the north), and the Gulf of Guinea (on the south). The country has a 228,000 km2 exclusive eco­ nomic zone, a 550 km coastal line, and twenty-six coastal districts [64, 65] where marine commercial fishing thrives. In 2013, Ghana’s Ministry of Fisheries and Aquaculture Development survey [64] revealed a total of 139,155 fishers operating 12,728 artisanal fishing vessels (i.e., ca­ noes) and 403 semi-industrial fishing vessels [65]. Both vessel types are locally made, but unlike the canoes, the semi-industrial ones are single-decked and not open to the atmosphere. These two groups of vessels constitute the SFV industry in Ghana and contribute immensely to the total annual fish catch. These vessels mostly do not use advanced systems and lack the appropriate safety monitoring equipment. Often, fishers aboard these vessels rely on years of experience gained in the fishing profession to decide on their safety when on a voyage. The case study SFV is assumed to be one of these vessels operating in Ghana’s territorial waters for demonstration purposes.

Finally, the RAw tool was realised by connecting the SA-scenarios sub-network to the “SFV risk awareness score” node, as shown in Fig. 7. In BN, the node, “SFV risk awareness score”, is called the leaf node. The tool uses the joint probability distribution in Eq. (3) to esti­ mate “High-risk” and “Low-risk” percentage scores at the leaf node. As mentioned in earlier sections, the percentage scores estimated by the RAw tool only indicate that conducive conditions exist aboard the SFV and could result in a fishing accident. The scores are not estimates of the probability of the accident happening. The closer the leaf nodes, “High- risk” score is to 100%, the more substantial the evidence that conducive conditions exist aboard the SFV. The evidence is weak if the “Low-risk” score exceeds the “High-risk” score.

### 3.5.2. Data collection to define risk factors states The goal here is to choose, for each risk factor, the state that

**Fig. 5. Illustrates how the “Dynamic OCS” subnetwork was formed.**

<!-- page 10 -->

Reliability Engineering and System Safety 234 (2023) 109139

**Fig. 6. Illustrates how the fishing accident and SA-scenario sub-networks were formed.**

wind speed, 16 knots; wind direction, south-southwest; wave height, 6 ft; wave period, 14 s; temperature, 28.1 ◦C; tides, 2 ft above sea level; latitude/longitude, 2◦40.14′N/0◦10.56′E; and water depth, 1569.2 m. Then, by benchmarking the observed conditions against the Beaufort scale in Table 6, the crew selected the state names in Table 7 for the risk factors: “Sea swell”, “Wave height”, and “Wind speed”. For the remaining environmental risk factors, some state names were guessed (i. e., simulated conditions) for purposes of acquiring data to demonstrate the workability of the RAw tool. Some risk-factor states, too, have been selected based on objective reasons, as shown in the “Reference” column of Table 7. Because Ghana is in the tropical region and it does not snow, the state “No”, defined for the risk factors “Blowing snow” and “Freezing rain/ice pellets”, is objectively defined. Similar objective reasons have been given for non-simulated state names.

**Table 5 Definitions for fishing accident types considered in the modelling.**

Number Fishing accident Definition

1 Capsize The accident of the SFV turning over at sea and emptying its content into the water 2 Collision The accident of impact between an SFV and another SFV or different ship type 3 Contact The accident of impact between an SFV and an offshore structure or marine mammal 4 Fire and explosion An accident leading to fire occurrence onboard and possibly, the burning of items and humans 5 Flooding/ Foundering

The accumulation of water inside the ship due to hull damage and bursting of internal pipelines carrying liquids 6 Gear entanglement The accident of a fisher caught in a fishing gear or restrained from movement by a gear 7 Grounding The accident of an SFV’s underwater hull touching the sea floor due to being in shallow waters 8 Hull integrity failure The accident of the underwater hull section of a ship being opened for ingress of sea water due to damage to the hull 9 Hypothermia The accident of a fisher experiencing abnormally low body temperature due to exposure to extremely cold temperatures 10 Lost/Stranded at sea The accident of the fishing crew unable to return home from sea often due to the SFV’s propulsion system failure or bad weather that makes navigation on chosen course extremely difficult 11 Man overboard The accident of a fisher unintentionally falling off the SFV into the sea water and requiring rescue thereof 12 Musculoskeletal disorder

To define state names for the technical-risk factors, the crew in charge would have to observe the ongoing fishing operations, machinery systems running, and the shipboard environment for clues on making the right decision. Again, let us assume that the states defined in Table 8 apply to the hypothetical case study. Because technical factors in the RAw tool are many, Table 8 is only a portion; the complete list is in Appendix A3. Like Table 7, some state names have been simulated too in Table 8, while others are based on objective reasons. The purpose is to gather data to facilitate the demonstration of how to operationalise the RAw tool.

When defining state names for the human-risk factors, the SFV crew would have to observe the fishers performing their duties and then choose a state name that best describes the human behaviour for each risk factor. Like was done for technical and environmental risk factors, let Table 9 represent the states defined for the human-risk factors. Ap­ pendix A3 has the complete list of human-risk factors as well.

Once Tables 7 to 9 have been realised, the data collection exercise to determine risk-factors states has been completed. The risk analyst acti­ vates the defined states in the RAw tool and runs the tool to perform diagnostic analysis.

The accident of a fisher experiencing pain in the muscles and joints due to strenuous work performances 13 Occupational injury A physical injury, disease, or death sustained by a fisher due to fishing tasks undertaken 14 Piracy and armed robbery

3.5.3. Diagnostic analysis The diagnostic analysis uses a bottom-up approach to enable the RAw tool to compute scores for each SA-information node; after, the fish-accident node scores are computed. The analyst must first activate in the tool the state names in Tables 7 to 9. After which, the tool is run, and the result is analysed. The result is the percentage score at each fishing accident and SA-information node, as well as the “SFV risk awareness score” node. The RAw tool calculates the percentage scores using the total probability theory in Eq. (2).

The attack of an SFV at gun point by robbers in territorial and international waters 15 Ship besetting The accident of an SFV being surrounded closely by ice, making manoeuvring difficult, and the vessel liable to hull integrity failure 16 Sinking The submerging of an SFV entirely below the water surface

*SFV: Small fishing vessel.

describes the observed happening at sea at the time of data collection. The vessel crew must observe the onboard environment, marine envi­ ronment, and fishers’ behaviours to decide on the most appropriate state name for each technical, environmental, and human risk factor. Assume the following sea conditions have been prevailing in Ghana’s territory of the Gulf of Guinea at the time of data collection: sea state, light winds;

Results for the “SFV risk awareness score” node are analysed first, after which the results of the fishing-accident nodes follow, and lastly, the SA-information nodes’ results. At the “SFV risk awareness score” node, if the high-risk-state score exceeds the low-risk-state score, it means conducive conditions favouring fishing-accident occurrence most

<!-- page 11 -->

Reliability Engineering and System Safety 234 (2023) 109139

**Fig. 7. The RAw tool for safety monitoring aboard the SFV.**

**Table 6 Beaufort scale for wave, wind, and water surface appearance at sea.**

Beaufort Beaufort Wind Wave Wave Sea surface Sea

number description Speed height height appearance swell (knot) (m) code 0 Calm < 1 0 Code0 Calm glassy None 1 Light air 1–3 0.0–0.2 Code1 Calm rippled Low short 2 Light breeze 4–6 0.2–0.5 Code2 Smooth wavelets Low long 3 Gentle breeze 7–10 0.5–1.0 Code3 Slight Moderate short 4 Moderate breeze 11–16 1.0–2.0 Code4 Moderate Moderate average 5 Fresh breeze 17–21 2.0–3.0 Code5 Rough Moderate long 6 Strong breeze 22–27 3.0–4.0 Code6 Very rough High short 7 Near gale 28–33 4.0–5.5 Code7 High High average 8 Gale 34–40 5.5–7.0 Code8 Very high High long 9 Strong gale 41–47 7.0–10.0 Code9 Phenomenal Confused 10 Storm 48–55 10.0–12.5 Code9 Phenomenal Confused 11 Violent storm 56–63 12.5–14.0 Code9 Phenomenal Confused 12 Hurricane > 64 > 14 Code9 Phenomenal Confused

likely exist. The vice-versa situation is interpreted as weak evidence for claims of conducive conditions existence. Similarly, suppose the possible-state score is higher than the not-possible-state score at a fishing-accident node. In that case, the interpretation is that, most likely, conducive conditions exist aboard in favour of that fishing accident. The opposite scenario would mean that fishing-accident is not expected to occur. Then, for SA-information nodes, when a possible-state score is greater than the not-possible-state score, the SA-information in question is a conducive condition and could trigger a fishing accident. It is such SA information that an SFV crew would note and remedy to promote safety aboard the SFV as they fish. That way, the RAw tool has aided in monitoring incidents during fishing to avoid a possible fishing accident. Section four discusses the diagnostic analysis results for the hypothetical case study.

information elements missing from the tool or new situations encoun­ tered by fishers must be noted. The SFV’s management may also wish to give some fishing accidents or SA information priority attention and would like the risk analyst to make some changes in the RAw tool to serve the purpose. All these information would be collected and used to update the tool accordingly.

### 3.7. The proposed monitoring programme for SFVs

For effective safety monitoring of SA aboard SFVs, the RAw tool and the various monitoring assessments discussed must be programmed into an instantaneous monitoring system. A schematic layout to develop such a system is shown in Fig. 9. With such a monitoring system in place, the fishing crew can follow the procedures described in Sections 3.5.2 to 3.5.4 to monitor and address fishing incidents. The actor represents the fishing crew or a designated individual amongst the crew responsible for initiating the monitoring process. At a given instant, the command is issued for data collection on risk factors in the “Dynamic OCS” sub-network. The raw data collected is stored in a database, where the data is processed into decision-state names specific to each risk factor. Therefore, the database management system (DMS) functions to facilitate data storage, processing, and retrieval. A choice DMS for the monitoring programme could be as simple as a notebook with ruled columns specifying data types collected, including the time and date for the data collection. The DMS could be advanced, too, like the cloud-based ones (e.g., MySQL). However, the ability of the SFV crew to operate the choice DMS must be the defining factor. After completing the DMS activities, the decision-state names realised are activated in the RAw tool to perform diagnostic analysis. The five-point scale identifies the fishing accidents and SA information with high occurrence-state scores at the assessment stage. Risk control measures are subsequently implemented to avoid a fishing accident. Meanwhile, the computed scores must be warehoused as historical data in the DMS for future data analysis tasks.

3.5.4. Risk assessment scale For decision-making on whether a score is severe or not and if a control measure must be administered, the five-points scale in Fig. 8 was developed. A score identified as point five or point four is severe. The fishing crew are encouraged to apply necessary control measures. A point of five or four on the scale is severe because the occurrence-state score is greater than the non-occurrence-state score. Thus, the evi­ dence favouring the SA information or fishing accident linked to the score is strong. When a score earns a point of two or one on the scale, there is weak evidence against the occurrence of the SA information or fishing accident linked to the score. The crew may not prioritise the information element for remedy purposes. At point three, an SA- information or fishing accident would require attention only when its occurrence-state score exceeds fifty percent. When the occurrence-state score is exactly 50%, the crew may choose to or not to focus on that SA information or fishing accident linked to the score. Resource availability may be considered when making a final decision in cases like that.

### 3.6. Step 5: RAw tool updating

To ensure the RAw tool can tackle present and future safety moni­ toring issues aboard SFVs when section 3.5 activities are ongoing,

<!-- page 12 -->

Reliability Engineering and System Safety 234 (2023) 109139

**Table 7 The defined state names for environmental risk factors.**

**Table 8 The defined state names for technical risk factors.**

Number Risk factor State Reference

Number Risk factor State name chosen

## References

1 Ambient/workplace temperature Warm Ghana is in the tropics 1 Block coefficient Slender Fishing vessel hulls are mostly not bulky 2 Bridge management system 2 Blowing snow No It does not snow in Ghana 3 Daytime No Ghanaian fishers, fish at dawn 4 Fog No Simulated condition 5 Freezing rain/ice pellets No Absent in Ghana’s climate 6 Huge aquatic animal in vessel’s way Not working Simulated condition 3 Pipe burst Yes Simulated condition 4 Collision avoidance alarm Not working Simulated condition 5 Deck spray-washed Water spill Simulated condition 6 Cooking gas leaking Yes Simulated condition 7 Cooking stove on No Simulated condition 8 Crossing surf Yes Simulated condition 9 Deck fittings Tight Simulated condition 10 Defence measures aboard Yes Simulated condition 7 Lightning occurrence No Lightning is not common at dawn 8 Nighttime Yes Ghanaian fishers, fish at dawn 9 Ocean current Vertical current None Only lookout personnel are available aboard 11 Electric spark Yes Simulated condition 12 Human machine interface Present Exist Simulated condition 10 Ocean type Others Gulf of Guinea (i.e., Atlantic ocean) 11 Polar day No Absent in the Gulf of Guinea 12 Polar night No Absent in the Gulf of Guinea 13 Polar region Southern hemisphere problems 13 Equipment/machinery age Old The vessels and equipment are usually old 14 Unsafe loading Yes Simulate condition 15 Equipment/machinery automation Insufficient Equipment operation is mainly manual 16 Fish stock caught Large Simulated condition 17 Fishing gear hauling Ongoing Simulated condition 18 Fishes caught kicking tails Gulf of Guinea is more southern 14 Sea swell Moderate long Beaufort scale-point 5 (see Table 5) 15 Seasons December to March Yes Simulated condition Simulated condition 19 Fishing gear shooting Not performed Simulated condition 20 Fishing gear snags Yes Simulated condition 16 Seawater temperature Warm Gulf of Guinea in the tropics 17 Submerged offshore structure in vessel’s way No Simulated condition its 71% (see Fig. 11) occurrence state puts it in the red zone according to the five-point risk assessment scale in Fig. 8, also evident in Fig. 13. The SFV crew need to seek for the SA-information responsible for the 71% rate. When doing so, some fishing accidents in the yellow zone may also need redress since Fig. 13 reveals that zone as presenting the second highest risk. As the pie-chart shows 94% of the fishing accidents out of the red zone, it could be concluded that the SFV in the defined states is safe. 18 Typical area Others Gulf of Guinea was put in this category 19 Vessel geographical location at sea Gulf of Guinea Place of fishing 20 Water depth Shallow Simulated condition 21 Wave height Code5 Simulated condition: 6 ft; see Table 5 22 Wind speed Moderate breeze Simulated condition: 16 knots; see Table 5 4.3. Situation awarenesses contributing to the most probable fishing accidents

4. Results and discussion The occurrence state diagnostic analysis results for SA-information nodes are shown in Table 10 (human-related), Table 11 (vessel-and- equipment), and Table 12 (prevailing conditions). The SA information in bold fonts is in the red zone when the result is subjected to the five-point risk assessment scale in Fig. 8. These need immediate control measures since their occurrence-state scores suggest strong evidence favouring the presence of conducive conditions aboard the SFV to cause a fishing ac­ cident. As Fig. 14 deduced from the tables show, the conducive condi­ tions are more likely to be caused by humans, vessel features, and onboard equipment than the marine or onboard environmental condi­ tions. Only “Slippery deck” (i.e., an onboard environmental condition) and “Vessel in pirate zone” (i.e., a marine geographical condition) are the prevailing conditions needing urgent control measures. Meanwhile, the mean score for the “Human-related SA” (53.67%) is greater than that for the “Vessel and equipment SA” (45.88%). Showing that, even though these categories of SA information have equal numbers in the red zone on the five-point scale, human-related conducive-conditions are more probable. This outcome is not surprising since the fishing accident identified as falling in the red zone in Section 4.2, the “Occupational injury”, is a human type. The case study results are discussed first, after which discussions on the present study’s contributions and limitations follow to highlight future works. 4.1. Risk awareness score for the case study SFV The RAw tool estimated 39% at the high-risk state of the leaf node, as shown in Fig. 10. From the five-point scale, a 39% occurrence-state score is in the green zone. Hence the tool infers there is no cause for alarm as far as the risk-factor states defined in Section 3.5.2 are concerned. The conditions existing aboard the case study vessel are not conducive enough to trigger a fishing accident. However, it is important to study also, the fishing accident scores to know which ones have scores in the red zone. 4.2. The most probable fishing accidents identified The occurrence state diagnostic analysis results for fishing-accident nodes are shown in Figs. 11 and 12. For the case studied, Figs. 11 and 12 show that a person-related accident is more likely to occur than a vessel-related one. Ship besetting is the least likely to occur (see Fig. 12), which is expected since ice does not form in the Gulf of Guinea. Mean­ while, only “Occupational injury”, demands immediate attention since It is important to note that the scores show that the situations rep­ resented by the SA information in these tables were present aboard the SFV but unnoticed. Also, fishers often see the risk factors responsible for this SA information during their daily fishing routines. However,

<!-- page 13 -->

Reliability Engineering and System Safety 234 (2023) 109139 possible knife injury. Therefore, by using the RAw tool, the root causes would be traced to “Manual beheading of fish”, “Fish filleted manually”, “Fish gutted manually”, and “Fish skinned manually” (see Table 4). Appropriate control measures include reminding fishers performing the duty to be careful with the knife or, better still, asking them to put on thick gloves while undertaking the tasks. That way, the conducive conditions for a possible knife injury are brought under control, and any accident it might lead to, such as “Occupational injury”, is avoided too.
**Table 9 Human risk factors and the defined state names.**

Number Risk factor State Reference 1 Alcohol Not consumed Simulated condition 2 Back pain Yes Simulated condition 3 Behaviour in emergency Unsafe Simulated condition 4 Bending over guardrail/ gunwale Defecating at Simulated condition gunwale edge 5 Caught up in fishing gear No Simulated condition 6 Prestige consideration Low Simulated condition 7 Confusing/conflicting directives 4.4. RAw tool and results validation The question of whether the RAw tool predicts right is vital to show how well the tool can replicate real scenarios. Another equally impor­ tant question is whether the tool’s estimated scores are reasonable. Both questions centre on the validity of the tool and its predictions. This section of the study investigated the validity issue by studying snippets of the tool and results. Yes Simulated condition 8 Crew number aboard Adequate Simulated condition 9 Cultural practice Unsafe Simulated condition 10 Inadequate rest/sleep No Simulated condition 11 Distractions No Simulated condition 12 Diving Yes Simulated condition 13 Drug use Yes Simulated condition 14 Economic and financial pressures High Simulated condition 15 Elbow pain No Simulated condition 16 Emotional condition/mental health Compare the scores for “Unheeded risk-taking” and “Ship besetting” in Table 9 and Fig. 12, respectively. Their risk factors are in Table 4, items four and five. Also, in Tables 6 to 8, the states defined are shown. The tool used these to compute the less than 10% and 90% occurrence- state rates for “Ship besetting” and “Unheeded risk-taking”, respectively. The moderate breeze selected for wind speed is on the low side compared to a hurricane state. Contrary, the December-to-March is the top-scored occurrence state for seasons. Meanwhile, the Gulf of Guinea, where the case study SFV fished, is in Ghana. Due to that, the high score for seasons will be neutralized by the states, others (i.e., Gulf of Guinea) and warm, belonging to ocean type and seawater temperature, respec­ tively. As a result, the tool computes an occurrence rate of around 10% for “Ship besetting”. Simulated condition 17 Fatigue No Simulated condition 18 Fish filleted manually Yes Simulated condition 19 Fish gutted manually Yes Simulated condition 20 Fish skinned manually Yes Simulated condition Not suitable for work In reality, a fishing vessel operating in Ghana’s territorial waters would not encounter an iceberg since the region is in the tropics, so no ship besetting must be expected. On the other hand, the selected occurrence states for risk factors of “Unheeded risk taking” are the culpable states for the SA information to happen. Consequently, the tool appropriately scores “Unheeded risk taking” 90%. It would have been 100% if the risk factor, “Fishing know-how”, had an “Unsafe” state instead. Thus, one can say the tool is practical in its predictions by face validity. The scores inferred are also meaningful and reasonable. fisherfolk may find it challenging to draw a direct connection between the SA information and risk factors to help control any possible fishing accident. Therefore, using the RAw tool, the SA information, hidden from fishers, is made known, and appropriate controls can be applied to avoid a fishing accident. Let us use the SA information, “Injury from knife”, as an example illustration. From Table 10, its occurrence-state score is 100%. This score means the conducive condition, favouring an injury from knife use, was present while fishers were doing their work. Fishers could be too busy for their cognition to comprehend a 4.5. The study contributions, limitations, and future work The present study made four significant contributions. First, a tai­ lormade monitoring tool, the RAw tool, was developed to monitor safety aboard an SFV. The tool is unique from the ones by U˘gurlu et al. [5], Obeng et al. [38], ¨Ozaydın et al. [39], and Yu et al.

[45] because its root factors are decision nodes and not chance nodes. As a result, the SFV

**Fig. 8. A five-point scale to assess scores estimated by the RAw tool.**

<!-- page 14 -->

Reliability Engineering and System Safety 234 (2023) 109139

**Fig. 9. The proposed system for safety monitoring aboard SFVs.**

**Fig. 10. The RAw tool with the leaf node results.**

**Fig. 11. Result of the tool’s estimates for person-related fishing accidents.**

**Fig. 12. Result of the tool’s estimates for vessel-related fishing accidents.**

<!-- page 15 -->

**Table 11 Diagnostic analysis results for vessel-and-equipment SA with scores greater than 59% emboldened.**

Number SA Information Occurrence state score (%) 1 Vessel unnoticed by nearby ships 90 2 Fire in accommodation 28 3 Navigation failure 54 4 Reduction in transverse metacentric height 90 5 Difficult manoeuvring 0 6 Machinery damage 77 7 Squat effect 15 8 Electrical fire 53 9 Cooking compartment heated 50 10 Submarine trawling fishing gear 0 11 Inter-ship communication failure 60 12 Rotational motion 90 13 Nearby ships detection failure 100 14 Unseaworthy 22 15 Propulsion system failure 15 16 Loss of power 60 17 Under keel clearance 100 18 Translational motion 15 19 Fishing gear setting 0 20 Overloading 15 21 Firefighting equipment failure 15 22 Freezing of firefighting equipment 15 23 Ship motion 55 24 Fire in engine-room 75 25 Fire due to lightning 53

**Fig. 13. The fishing accidents zoned into red (1 accident), yellow (7 accidents), and green (8 accidents) using the five-point-risk-assessment scale.**

**Table 10 Diagnostic analysis results for human-related SA with scores greater than 59% emboldened.**

Number SA Information Occurrence state score (%)
**Table 12 Diagnostic analysis results for prevailing conditions SA with scores greater than 59% emboldened.**

1 Swept overboard 21 2 Unheeded risk taking 90 3 Fall overs due to slip 53 4 High risk-taking behaviour 73 5 Struck by waves 49 6 Cigarette burn 53 7 Smooking in cooking compartment 0 8 Injury to finger and whole limb 15 9 Wounds from fishing gear 90 10 Mistrust amongst fishers/Information mistrust Number SA Information Occurrence state score (%) 1 Slippery deck 100 2 Iceberg present 0 3 Severe temperature 0 4 Polar darkness 0 5 Darkness 28 6 Ice/snow accretion on superstructure and main deck 53 0 11 Human error 67 12 Burns 52 13 Contusions 30 14 Watchkeeping failure 35 15 Competing with other boats 53 16 Bites and stings 53 17 Fire due to cooking 72 18 Officer-of-the-watch failure 67 19 Fall overs due to bending over guardrail/ gunwale 7 Adverse weather 7 8 Unsafe external loading 55 9 Atmosphere during voyage 53 10 Seastate rough 45 11 Poor visibility 0 12 Ice drifting 45 13 Vessel in pirate zone 100 100 produced by multiple subject-matter experts for the same CPT. 20 Injury from knife 100 21 Loss of finger 60 22 Injury by storm 34 23 Onboard defence personnel unready 53 24 Communication channels failure 15 As future work, the proceeding limitations are being considered. Firstly, the RAw tool only serves instantaneous safety monitoring needs aboard SFVs. If real-time data collection and RAw tool operation can be done, a dynamic monitoring tool would emerge for SFV risk monitoring. Next, it would be more convenient to have the RAw tool as a handheld device like the calculator. Fishers can then operate it with ease. Also, knowing that SFV fishers might not have high levels of education, it is likely interpreting the tool’s results by themselves, as described in the study, could be a difficult task for the fishers. Future studies will explore the possibilities of integrating the five-point scale into the RAw tool. That way, only red, yellow, and green colours would be used to show the severity of a risk item. Also, probability updating was not performed for the chance nodes. That is because the present study’s objective was diagnosing probable fishing accidents and the conducive conditions for their occurrence; uncertainty measurement was not prioritised. Never­ theless, future studies would consider uncertainty in the RAw tool scores to determine how much variability exists between prior and posterior crew only has to input non-numerical facts and not probabilities, which comes with the challenges of uncertainty in data. As the second contribution, the tool was situated in a monitoring system resulting in a proposed safety monitoring programme layout for SFVs. The pro­ gramme would promote instantaneous enquiry into fishing safety aboard a vessel. Thirdly, a risk assessment scale, the five-point scale, was developed to tell which results outputted by the RAw tool must be considered for mitigation purposes. The scale is unique from others [26, 45] because it compares risk-item-states results to decide whether strong or weak evidence exists for the risk item to happen. The fourth and final contribution is the proposed scale for eliciting probabilities for CPTs. Using the proposed scale minimizes the variations in probability values

<!-- page 16 -->

Reliability Engineering and System Safety 234 (2023) 109139 SA information and fishing accidents noted would be identified and controlled to avoid an actual accident. Apart from the RAw tool and the five-point scale, the present study introduced an objective approach to eliciting probabilities for condi­ tional probability tables (CPT) in BN. The approach provides a probability-scoring scale that guides a subject-matter expert (SME). Using the approach could help the probabilities estimated by multiple SMEs to converge. This would help minimise SME results variations when using the subjective approach. In the long run, the proposed elicitation approach aims to improve the reliability of BN results since CPT is an integral part of BN modelling; less variability in SME estimated probabilities for CPT could then translate into reliable BN results. The study is recommended to small fishing boat owners, skippers, and fish­ ing administrations overseeing SFV operations. The study demonstrates how the probabilistic safety assessment method facilitates sourcing in­ formation on fishers knowledge about risks encountered at sea and from the existing secondary data on how fishing accidents occur and brings the gathered information together to develop a risk analysis tool that would serve the safety monitoring needs of small fishing boats.

**Fig. 14. Percentage results for SA information in the red zone.**

In the future, researchers will work at making the RAw tool dynamic through real-time data collection and time-driven operation of the RAw tool. Also, the tool in its current form is digital and would be more convenient to use if made into a handheld device such as a calculator. probabilities. Meanwhile, the study is limited by the publications sourced to define risk factors, SA information, and fishing accidents. Different publications may give additional information elements that would enrich the RAw tool. It also could mean context defining is essential when developing the RAw tool. If one is sure that the necessary information elements in the defined context have been captured, then it is most likely that a suitable RAw tool would emerge to serve the intended purpose. CRediT authorship contribution statement Vindex Domeh: Conceptualization, Methodology, Software, Inves­ tigation, Writing – original draft, Writing – review & editing. Francis Obeng: Conceptualization, Methodology, Software, Investigation, Writing – original draft, Writing – review & editing. Faisal Khan: Conceptualization, Methodology, Formal analysis, Writing – review & editing, Supervision, Project administration, Funding acquisition. Neil Bose: Methodology, Formal analysis, Project administration, Writing – review & editing, Supervision, Funding acquisition. Elizabeth Sanli: Formal analysis, Supervision, Writing – review & editing, Supervision.

5. Conclusions Most artisanal and semi-industrial fishing vessels, constituting the small fishing vessel (SFV) sector, do not have adequate safety moni­ toring systems to decide on possible accidents ahead of time. Mean­ while, SFV fishers know the risk factors they encounter daily. Also, literature on fishing accidents abounds and contains information on how the accidents occur. The present study consolidated the information on fishing accidents from the literature and fishers’ risk factors awareness to develop a risk analysis tool. First, a cause-effect diagram was devel­ oped from the information gathered. Through the method of probabi­ listic safety assessment using Bayesian network (BN) modelling, the collected information was used to develop a risk monitoring model called the risk awareness (RAw) tool. Broadly, the RAw tool has three kinds of information elements: risk factors as root causes, situation awareness (SA) information as latent failures, and fishing accidents as incidents targeted for monitoring. Because decision nodes were used for risk factors and fishers already know about the root causes of safety at sea, the tool can be operated relatively easily. Declaration of Competing Interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. Data availability Data will be made available on request. Supplementary materials An SFV crew only needs to activate the state evidence for each risk factor by observing the marine and shipboard environment for the technical, environmental, and human-related operational factors occurring during fishing. The RAw tool then uses a bottom-up approach to estimate percentage scores for SA information nodes and, after, fishing-accident nodes. The scores are assessed on a five-point scale developed as a risk assessment tool. Because each SA-information node and fishing accident node has two states defining its occurrence and non- occurrence, the five-point scale compares the states’ scores at each node to prioritise an SA information and a fishing accident for control pur­ poses. Results indicating that the occurrence-state score is greater than the non-occurrence-state score is strong evidence that the SA informa­ tion, or the fishing accident in question, must be prioritised. The vice- versa would mean weak evidence, so SA information or fishing- accident may not receive immediate attention. Once the prioritised fishing accidents are defined, they can also be traced to the high-score SA information. Then, the conducive conditions aboard favouring the Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.ress.2023.109139.

## References

[1] Sharma A, Nazir S, Ernstsen J. Situation awareness information requirements for maritime navigation: a goal directed task analysis. Saf Sci 2018;120:745–52. October2019.

[2] Dalaklis D. Chapter 9: safety and security in shipping operations. Shipping operations management; 2017. p. 197–213.

[3] An K. E-navigation services for Non-SOLAS ships. Int J e-Navigat Marit Econ 2016; 4:13–22.

[4] Jin D, Kite-Powell H, Talley W. The safety of commercial fishing: determinants of vessel total losses and injuries. J Saf Res 2001;32(2):209–28.

[5] U˘gurlu F, Yıldız S, Boran M, U˘gurlu ¨O, Wang J. Analysis of fishing vessel accidents with Bayesian network and Chi-square methods. Ocean Eng 2019;198:2020. December.

[6] Roberts SE. Britain’s most hazardous occupation: commercial fishing. Accid Anal Prev 2010;42(1):44–9.

<!-- page 17 -->

Reliability Engineering and System Safety 234 (2023) 109139

[7] Loughran CG, Pillay A, Wang J, Wall A, Ruxton T. A preliminary study of fishing

[36] Jensen OCC, Petursdottir G, ari. Holmen IM, Abrahamsen A, Lincoln J. A review of vessel safety. J Risk Res 2002;5(1):3–21.

[8] Ugurlu H, Cicek I. Analysis and assessment of ship collision accidents using fault fatal accident incidence rate trends in fishing. Int Marit Health 2014;65(2):47–52. https://doi.org/10.5603/IMH.2014.0011.

[37] B.-.Y. Menakhem, “Risks and dangers in small-scale fisheries : an overview,” 2000. tree and multiple correspondence analysis. Ocean Eng 2021;245:110514. September2022.

[9] Obeng F, Domeh V, Khan F, Bose N, Sanli E. Analyzing operational risk for small [Online]. Available: https://ideas.repec.org/p/ilo/ilowps/993427803402676. html.

[38] Obeng F, Domeh V, Khan F, Bose N, Sanli E. Capsizing accident scenario model for fishing vessels considering crew effectiveness. Ocean Engineering 2022;249. https://doi.org/10.1016/j.oceaneng.2021.110512. Apr.

[10] Budiyanto MA, Azharrisman F, Utama AF. Cooling performance of modular fish small fishing trawler. Saf Sci 2022;145:105500. October 2020.

[39] ¨Ozaydın E, Fıs¸kın R, U˘gurlu ¨O, Wang J. A hybrid model for marine accident hold for 30 gross-tonnage fishing vessel. J Mar Eng Technol 2022. https://doi.org/ 10.1080/20464177.2022.2094655.

[11] Sonal, Ghosh D. Impact of situational awareness attributes for resilience analysis based on Bayesian Network (BN) and association rule mining (ARM). Ocean Eng 2020;247:2022. https://doi.org/10.1016/j.oceaneng.2022.110705. October.

[40] Kwag S, Choi E, Eem S, Ha JG, Hahm D. Toward improvement of sampling-based assessment of active distribution networks using hybrid dynamic Bayesian multi criteria decision-making approach. Reliab Eng Syst Saf 2022;228. https://doi.org/ 10.1016/j.ress.2022.108772. Dec.

[12] Elidolu G, Sezer SI, Akyuz E, Arslan O, Arslanoglu Y. Operational risk assessment of seismic probabilistic safety assessment method for nuclear facilities using composite distribution and adaptive discretization. Reliab Eng Syst Saf 2021;215. https://doi.org/10.1016/j.ress.2021.107809. Nov.

[41] Park JW, Lee SJ. Simulation optimization framework for dynamic probabilistic ballasting and de-ballasting on-board tanker ship under FMECA extended Evidential Reasoning (ER) and Rule-based Bayesian Network (RBN) approach. Reliab Eng Syst Saf 2023;231. https://doi.org/10.1016/j.ress.2022.108975. Mar.

[13] Kimera D, Nangolo FN. Reliability maintenance aspects of deck machinery for safety assessment. Reliab Eng Syst Saf 2022;220. https://doi.org/10.1016/j. ress.2021.108316. Apr.

[42] Li H, Ren X, Yang Z. Data-driven Bayesian network for risk analysis of global ageing/aged fishing vessels. J Mar Eng Technol 2022;21(2):100–10. https://doi. org/10.1080/20464177.2019.1663595.

[14] Thorvaldsen T. The importance of common sense: how Norwegian coastal maritime accidents. Reliab Eng Syst Saf 2023;230:108938. https://doi.org/ 10.1016/j.ress.2022.108938. Feb.

[43] Fan S, Blanco-Davis E, Yang Z, Zhang J, Yan X. Incorporation of human factors into fishermen deal with occupational risk. Mar Policy 2013;42:85–90.

[15] Paterson B. Tracks, trawls and lines-Knowledge practices of skippers in the maritime accident analysis using a data-driven Bayesian network. Reliab Eng Syst Saf 2020;203. https://doi.org/10.1016/j.ress.2020.107070. Nov.

[44] Pristrom S, Yang Z, Wang J, Yan X. A novel flexible model for piracy and robbery Namibian hake fisheries. Mar Policy 2015;60:309–17.

[16] Størkersen KV, Thorvaldsen T. Traps and tricks of safety management at sea. Saf Sci assessment of merchant ship operations. Reliab Eng Syst Saf 2016;155:196–211. https://doi.org/10.1016/j.ress.2016.07.001. Nov.

[45] Yu Q, Teixeira ˆAP, Liu K, Rong H, Soares CGuedes. An integrated dynamic ship risk 2018;134:2021. November.

[17] Abdullah-Bin-Farid BS, Mondal S, Satu KA, Adhikary RK, Saha D. Management and socio-economic conditions of fishermen of the Baluhar Baor, Jhenaidah, Bangladesh. J Fish 2013;1(1):30. https://doi.org/10.17017/jfish.v1i1.2013.7.

[18] de O. Braga H, Schiavetti A. Attitudes and local ecological knowledge of experts model based on bayesian networks and evidential reasoning. Reliab Eng Syst Saf 2021;216. https://doi.org/10.1016/j.ress.2021.107993. Dec.

[46] Yu Q, Liu K, Yang Z, Wang H, Yang Z. Geometrical risk evaluation of the collisions fishermen in relation to conservation and bycatch of sea turtles (reptilia: testudines), Southern Bahia, Brazil. J Ethnobiol Ethnomed 2013;9(1):1–13. https://doi.org/10.1186/1746-4269-9-15.

[19] Wekke IS, Cahaya A. Fishermen poverty and survival strategy: research on poor between ships and offshore installations using rule-based Bayesian reasoning. Reliab Eng Syst Saf 2021;210. https://doi.org/10.1016/j.ress.2021.107474. Jun.

[47] Sotiralis P, Ventikos NP, Hamann R, Golyshev P, Teixeira AP. Incorporation of human factors into ship collision risk models focusing on human centred design aspects. Reliab Eng Syst Saf 2016;156:210–27.

[48] Fulmer S, Buchholz B, Scribani M, Jenkins P. Musculoskeletal disorders in households in bone Indonesia. Procedia Econ Financ 2015;26(15):7–11. https:// doi.org/10.1016/s2212-5671(15)00962-4.

[20] Animah I, Shafiee M. Application of risk analysis in the liquefied natural gas (LNG) northeast lobstermen. Saf Health Work 2017;8(3):282–9.

[49] Kujala P, H¨anninen M, Arola T, Ylitalo J. Analysis of the marine traffic safety in the sector: an overview. J Loss Prev Process Ind 2019;63:103980. https://doi.org/ 10.1016/j.jlp.2019.103980. August2020.

[21] Chen SH, Pollino CA. Good practice in Bayesian network modelling. Environ Model gulf of Finland. Reliab Eng Syst Saf 2009;94(8):1349–57.

[50] Islam R, Khan F, Abbassi R, Garaniya V. Human error assessment during Softw 2012;37:134–45. https://doi.org/10.1016/j.envsoft.2012.03.012.

[22] S.L. Case, J.M. Lincoln, and D.L. Lucas, “Fatal falls overboard in commercial fishing maintenance operations of marine systems – what are the effective environmental factors? Saf Sci 2018;107:85–98. no. April.

[51] Davis B, Colbourne B, Molyneux D. Analysis of fishing vessel capsizing causes and — United States, 2000 –2016,” 2018.

[23] Byard RW. Commercial fishing industry deaths-Forensic issues. J Forensic Leg Med links to operator stability training. Saf Sci Oct. 2019;118:355–63.

[52] Galierikov´a A. The human factor and maritime safety. Transp Res Procedia 2019; 2013;20(3):129–32. https://doi.org/10.1016/j.jflm.2012.05.010.

[24] Windle MJS, Neis B, Bornstein S, Binkley M, Navarro P. Fishing occupational 40:1319–26. Transcom.

[53] Lusic Z, Marcic M, Bakota M, Pusic D. Detecting a man in the sea. In: 8th health and safety: a comparison of regulatory regimes and safety outcomes in six countries. Mar Policy 2008;32(4):701–10. https://doi.org/10.1016/j. marpol.2007.12.003.

[25] Mcguinness E, Aasjord HL, Utne IB, Marie I. Fatalities in the Norwegian fishing International Maritime Science Conference; 2019. p. 560–70.

[54] Valdez Banda OA, Goerlandt F, Montewka J, Kujala P. A risk analysis of winter navigation in Finnish sea areas. Accid Anal Prev 2015;79:100–16.

[55] Zhang G, Thai VV. Expert elicitation and Bayesian Network modeling for shipping fleet 1990–2011. Saf Sci 2013;57:335–51.

[26] Domeh V, Obeng F, Khan F, Bose N, Sanli E. Risk analysis of man overboard accidents: a literature review. Saf Sci 2016;87:53–62.

[56] U˘gurlu ¨O, K¨ose E, Yıldırım U, Yüksekyıldız E. Marine accident analysis for collision scenario in a small fishing vessel. Ocean Eng 2021;229:108979. Jun.

[27] Wang J, Pillay A, Kwon YS, Wall AD, Loughran CG. An analysis of fishing vessel and grounding in oil tanker using FTA method. Marit Policy Manag 2015;42(2): 163–85.

[57] Rahman MS, Khan F, Shaikh A, Ahmed S, Imtiaz S. Development of risk model for accidents. Accid Anal Prev 2005;37(6):1019–24.

[28] Bye R, Lamvik GM. Professional culture and risk perception: coping with danger on board small fishing boats and offshore service vessels. Reliab Eng Syst Saf 2007;92 (12):1756–63. https://doi.org/10.1016/j.ress.2007.03.024. Dec.

[29] Kum S, Sahin B. A root cause analysis for Arctic Marine accidents from 1993 to marine logistics support to offshore oil and gas operations in remote and harsh environments. Ocean Eng 2019;174:125–34. January 2018.

[58] H¨anninen M, Kujala P. Influences of variables on ship collision probability in a

2011. Saf Sci 2015;74:206–20.

[30] A. Council, “Arctic marine shipping assessment 2009 report,” 2010.

[31] Smith D, Veitch B, Khan F, Taylor R. An accident model for Arctic shipping. In: Bayesian belief network model. Reliab Eng Syst Saf 2012;102:27–40.

[59] Afenyo M, Khan F, Veitch B, Yang M. Arctic shipping accident scenario analysis using bayesian network approach. Ocean Eng 2016;133:224–30. August2017.

[60] Khan B, Khan F, Veitch B. A dynamic bayesian network model for ship-ice collision Proceedings of the ASME 2015 34th International Conference on Ocean, Offshore and Arctice Engineering (OMAE2015); 2015. p. 4–9.

[32] Rezaee S, Pelot R, Ghasemi A. The effect of extreme weather conditions on risk in the arctic waters. Saf Sci 2020;130:1–9. no. June.

[61] Abraham P. International comparison of occupational injuries among commercial commercial fishing activities and vessel incidents in Atlantic Canada. Ocean Coast Manag 2016;130:115–27. https://doi.org/10.1016/j.ocecoaman.2016.05.011. Oct.

[33] Khan B, Khan F, Veitch B, Yang M. An operational risk analysis tool to analyze fishers of selected northern countries and regions. In: Proceedings of the International Fishing Industry Safety and Health Conference; 2002. p. 455–65.

[62] Lincoln JM, Lucas DL. Occupational fatalities in the United States commercial fishing industry, 2000-2009. J Agromedicine 2010;15(4):343–50.

[63] L. BayesFusion, “GeNIe Modeler: user manual,” 2016.

[64] S. Akyeampong, K. Amador, and B. Nkrumah, “Report on the 2013 Ghana Marine marine transportation in Arctic waters. Reliab Eng Syst Saf 2017;169:485–502. July2018.

[34] Paolo F, et al. Investigating the role of the human element in maritime accidents Canoe Frame Survey, ” 2013.

[65] MoFAD, “Fisheries management plan of Ghana: a national policy for the using semi-supervised hierarchical methods. Transp Res Procedia 2021;52:252–9.

[35] Chochinov A. Alcohol ‘on board,’ man overboard - Boating fatalities in Canada. management of the marine fisheries sector,” pp. 1–48, 2019. Can Med Assoc J 1998;159(3):259–60.
