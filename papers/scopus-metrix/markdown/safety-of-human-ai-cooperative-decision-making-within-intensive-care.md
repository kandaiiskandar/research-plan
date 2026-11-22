# Safety of human-AI cooperative decision-making within intensive care

> **Source PDF:** `Safety of human-AI cooperative decision-making within intensive care.pdf` · **Pages:** 17 · Converted by `scripts/paper2md.py` from the original PDF.

<!-- page 1 -->

RESEARCH ARTICLE Safety of human-AI cooperative decisionmaking within intensive care: A physical simulation study

Paul Festor1,2☯, Myura Nagendran1,2,3☯, Anthony C. Gordon1,3, Aldo A. Faisal 1,2,4*‡ Matthieu Komorowski1,3‡

1 UKRI Centre for Doctoral Training in AI for Healthcare, Imperial College London, London, United Kingdom, 2 Departments of Bioengineering and Computing, Brain and Behavior Lab, Imperial College London, London, United Kingdom, 3 Division of Anaesthetics, Pain Medicine and Intensive Care, Imperial College London, London, United Kingdom, 4 Digital Health and Data Science, Universität Bayreuth, Bayreuth, Germany

☯ These authors contributed equally to this work. ‡ These authors jointly supervised this work * a.faisal@imperial.ac.uk

Abstract

The safety of Artificial Intelligence (AI) systems is as much one of human decision-making as a technological question. In AI-driven decision support systems, particularly in high-stakes settings such as healthcare, ensuring the safety of human-AI interactions is paramount, given the potential risks of following erroneous AI recommendations. To explore this question, we ran a safety-focused clinician-AI interaction study in a physical simulation suite. Physicians were placed in a simulated intensive care ward, with a human nurse (played by an experi­ menter), an ICU data chart, a high-fidelity patient mannequin and an AI recommender system on a display. Clinicians were asked to prescribe two drugs for the simulated patients suffer­ ing from sepsis and wore eye-tracking glasses to allow us to assess where their gaze was directed. We recorded clinician treatment plans before and after they saw the AI treatment recommendations, which could be either ‘safe’ or ‘unsafe’. 92% of clinicians rejected unsafe AI recommendations vs 29% of safe ones. Physicians paid increased attention (+37% gaze fixations) to unsafe AI recommendations vs safe ones. However, visual attention on AI expla­ nations was not greater in unsafe scenarios. Similarly, clinical information (patient monitor, patient chart) did not receive more attention after an unsafe versus safe AI reveal suggesting that the physicians did not look back to these sources of information to investigate why the AI suggestion might be unsafe. Physicians were only successfully persuaded to change their dose by scripted comments from the bedside nurse 5% of the time. Our study emphasises the importance of human oversight in safety-critical AI and the value of evaluating human-AI systems in high-fidelity settings that more closely resemble real world practice.

OPEN ACCESS

Citation: Festor P, Nagendran M, Gordon AC, Faisal AA, Komorowski M (2025) Safety of human-AI cooperative decision-making within intensive care: A physical simulation study. PLOS Digit Health 4(2): e0000726. https://doi. org/10.1371/journal.pdig.0000726

Editor: Martin G Frasch, University of Washington, UNITED STATES OF AMERICA

Received: May 24, 2024

Accepted: December 17, 2024

Published: February 24, 2025

Peer Review History: PLOS recognizes the benefits of transparency in the peer review process; therefore, we enable the publication of all of the content of peer review and author responses alongside final, published articles. The editorial history of this article is available here: https://doi.org/10.1371/journal. pdig.0000726

Copyright: © 2025 Festor et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Author summary

Artificial intelligence (AI) demonstrates increasingly promising results for supporting medical decision-making. However, most systems are evaluated outside of the clinical

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 1 / 17

<!-- page 2 -->

context within which they will be used, predominantly to avoid incurring risks for pa­ tients. When used at the bedside, these AI systems will be part of larger human-computer decision teams and little work evaluates the safety of this tandem as a whole. Here, we use a physical simulation suite and eye-tracking glasses to analyse the interaction between doctors and an AI support tool. Using the examplar of cardiovascular management in patients with sepsis, we report clinician behaviour when facing both (intentionally crafted) ‘safe’ and ‘unsafe’ recommendations from the AI system. We show that unsafe recommendations capture the attention of clinicians, increase the number of requests for a second opinion, and would be stopped over 90% of the time. However, unsafe AI recommendations did not draw more attention to accompanying explanations so the cognitive process behind the decision to reject them is not elucidated here. Working in a simulation suite also allowed us to study the potential human factor of decision safety: an experimenter playing the role of a nurse was able to convince 5% of clinicians to adopt an unsafe AI recommendation using pre-set challenge arguments. Combined with an objec­ tive measure of attention via eye-tracking, our approach allows us to capture and analyse human-AI interactions in safety-critical medical settings.

Data availability statement: The data and code (in the form of Jupyter notebooks) to reproduce the results and figures in both the manuscript and the supplementary appendices are available at: https://figshare. com/s/78c5ff5c6031f701c0d1

Funding: This work was funded by the University of York and the Lloyd’s Register Foundation through the Assuring Autonomy International Programme (Project Reference 03/19/07) and supported by the National Institute for Health Research (NIHR) Imperial Biomedical Research Centre (BRC). PF and MN were supported by a PhD studentship of the UKRI Centre for Doctoral Training in AI for Healthcare (EP/S023283/1). ACG was support­ ed by an NIHR Research Professorship (RP2015-06-018). AAF was supported by a UKRI Turing AI Fellowship (EP/V025449/1). This study/project/report is independent research funded by the NIHR (Artificial Intelligence, 'Validation of a machine learning tool for optimal sepsis treatment', AI_AWARD01869). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

### Introduction

Artificial Intelligence (AI) driven systems have an increasingly prominent role in decision-­ making including in high-stakes (e.g., potentially life-threatening) settings [1–3]. However, the final decision usually remains in human hands. Therefore, understanding how AI recom­ mendations impact end-user behaviour is crucial, and recent work has highlighted differ­ ences in the human perception of human vs AI advice such as the latter being significantly more influential on the final decision [4,5]. In high-risk shared decision-making settings, even non-autonomous AI-decision-support tools have high safety assurance requirements such as rigorous testing and usage auditing by notified bodies [6,7]. Understanding the human-AI cooperation dynamic is key to ensuring safe AI deployment. Work has been done to use human feedback as an active learning mechanism for robots, sometimes enforcing safe behaviour [8–10]. Yet, the evolution of AI safety has little focus on quantifying its impact on the final decision-maker, the human.

Competing interests: MK has received consult­ ing fees from Philips Healthcare, and speaker honoraria from GE Healthcare. The other authors declare that there are no competing interests.

We study safety in human-AI cooperative settings in healthcare because healthcare reflects many of the issues that make real-world AI deployment challenging: regulatory requirements, high stakes, high cognitive load on decision-makers, and limited availability of human experts. Furthermore, the post-hoc rationalisations of human decision-makers can sometimes be “blackbox” in nature, just as AI decisions can be [11]. In situations where the “optimal” decision has historically been unclear, and where recommending decisions could surpass the standard of care [12–14], the safety-assessment challenge becomes even harder. One such example is cardio­ vascular management during sepsis where the optimal personalised doses of intravenous (IV) fluids and vasopressors remain unknown [15,16]. Their personalisation has been designated as a research priority by the international reference taskforce the “Surviving Sepsis Campaign” [17]. Sepsis treatment in intensive care embodies all the characteristics that make healthcare AI both a difficult challenge but also one that could have a significant beneficial patient impact if successful. Sepsis affects up to 50 million people around the world with 20% annually dying. It represents the most common cause of death in the hospital and the most expensive condition treated in hospital [18]. As such, applying AI and data-driven approaches to deliver precision medicine therapy for sepsis is a global and urgent research priority. Yet, the translation to the bedside has been slow due to concerns for patient safety and clinician trust in these systems [19–21].

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 2 / 17

<!-- page 3 -->

Attempts have been made to improve the safety profile of AI-driven decision support in retrospective intensive care settings [12–14]. Still, the necessity of prospective and higher fidelity evaluations involving clinical end users is clear from recent examples in other fields [13]. For instance, an acute kidney injury alert system showing good performance on retro­ spective data was found to worsen outcomes when deployed in a real-world setting, illustrat­ ing the need for a careful transition between retrospective testing and prospective deployment of digital systems [22]. Safely transitioning from “bytes to bedside” is a particularly complex challenge because of the dynamic interaction with human users who are prone to biases and can behave in unpredictable ways [23–26].

In response to the growing emphasis on ecologically valid experimentation, we need to evaluate the dynamics of human-AI cooperative systems in the same context [27,28], and therefore we run our behavioural experiment in a physical simulation suite. Simulation exer­ cises have historically been used as a widely accepted training tool for both modelling high-­ fidelity situations and capturing patterns of human behaviour. They now form a core part of medical training [29]. This immersive approach enables physicians to respond to bedside stimuli more realistically, aligning their behaviours with actual clinical practice [30] Further­ more, this shift towards a more realistic setting aligns with the evolving regulatory land­ scape surrounding AI which emphasises “human-centred AI” and the holistic evaluation of human-AI team performance [31,32]. AI safety assessment is not a mere problem of computer science but also one of human-AI cooperation [33], which should incorporate behavioural elements grounded in human perceptual and decision-making studies.

We use the example of cardiovascular management in sepsis to study the behaviour of physicians in response to AI recommendations. Here, we share the results of an observational study of human-AI interaction in a high-fidelity simulation suite focusing on the influence of safe and unsafe AI recommendations on treatment decisions. We explore eye-tracking data and explainable AI questions deeper in a related/sister manuscript [34].

Materials and methods Objective

We conducted an observational human-AI interaction study in a high-fidelity simulation facility. This study had two primary objectives. The first was to measure whether participants were able to detect, and correctly reject, unsafe recommendations from an AI tool (such as dramatically increasing doses of vasopressors to a patient with sepsis related to infected and leaky heart valves and elevated blood pressure) and/or ask for senior help when appropri­ ate. The second was to identify whether or not human intervention could interfere with this interaction and sway clinicians away from their initial decision (potentially toward an unsafe treatment). Secondary study objectives included: (i) quantifying the shift in fluid and vaso­ pressor doses induced by seeing an AI recommendation, and (ii) determining whether or not gaze patterns varied differentially depending on the safety status of the AI recommendation.

### Experimental design

Participants (clinicians) were briefed on the experiment and completed a pre-experiment questionnaire. The questionnaire recorded their demographics (age, gender, years of expe­ rience), prior experience with AI, as well as attitude towards AI through questions on their perception of AI benefits/issues. See S1 Appendix for the full content of the briefing and questionnaire. Participants were told that they would conduct a review of several adult patients with sepsis within a simulation suite (Imperial College Simulation Centre) and that they would need to prescribe appropriate doses of fluid and vasopressor for each patient both

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 3 / 17

<!-- page 4 -->

before and after getting advice from an AI tool. Critically, physicians were told that the AI recommendation engine had been successfully validated in multiple retrospective settings but had not been prospectively evaluated. The simulation layout is shown in Fig 1a.

Each physician completed a total of six different patient scenarios, simulating a virtual “ward round”. Each scenario started with physicians entering the simulation suite and conducting their assessment of the patient as they saw fit. Data sources within the room included a stan­ dard paper ICU bedside data chart with observations and blood results, an ICU handover note including details of the patient’s presentation and medical history, a vital signs monitor and a physical patient mannequin (Simman 3G, Laerdal Medical, Stavanger, Norway) which could be examined (see S2 Appendix for the details of each patient scenario). A member of the research team played the role of the bedside ICU nurse who could only give standardised responses to any question, and was always the same person for all subjects. Following their assessment of the patient, physicians were asked to recommend a dose rate for fluids (ml/hr) and vasopressors (noradrenaline, mcg/kg/min) for the coming hour (to match the format of AI recommenda­ tions). Physicians rated their confidence on a 1–10 scale and whether or not they would like support for their decision from a senior physician (or a second opinion if the physician was

**Fig 1. Experimental design. A. Visual representation of the simulation suite and overall summary of experimental design. A full descrip­ tion and rationale for the methods chosen including the realism limitation of the environment is given in the main text.: (1) Bedside monitor (2) AI screen (3) Participant (4) Bedside nurse (5) Patient mannequin (6) Intensive care unit (ICU) bedside information chart. B. Experimental protocol diagram. C. Gaze-based attention extraction pipeline: eye-tracking glasses, pupil camera view, a recorded field of view with April tags (QR codes) and reconstructed data with fixation heatmaps on the different regions of interest (ROIs).**

https://doi.org/10.1371/journal.pdig.0000726.g001

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 4 / 17

<!-- page 5 -->

already senior themselves). They were then shown the AI recommendation, asked to what extent they agreed with the recommendation on a 5-point Likert scale (from completely dis­ agree to completely agree) [35], and then the initial dosing-related questions again (what dose they would prescribe, their confidence level, optional ask for senior help - see Fig 1b).

Finally, physicians were asked whether or not they would stop the AI recommendation if it were to be automatically administered to the patient. This question was intended to nuance the agreement prompt and identify situations where a participant might disagree with an AI recommendation but not necessarily consider it a threat to patient safety. Participants were clearly introduced to the nuance between these two questions in the pre-experiment briefing.

The running of a single patient scenario from entry into the simulation suite to exit constituted one trial. Trials were categorised by the nature of the AI tool’s recommenda­ tion provided to the participant: safe, unsafe or “challenged” unsafe. In the latter, after the physician reported whether or not they would stop the AI recommendation if it were to be automatically administered, the bedside nurse was permitted three attempts (all following a standardised script) to verbally try to convince them to change their mind (see S3 Appendix for the scripts). The patient scenarios, including the AI recommendations, were piloted with specialist clinicians (not enrolled in this experiment) within the Imperial College Critical Care research group who validated their credibility. Each physician experienced four safe trials, one unsafe and one “challenged” unsafe in a pseudo-randomised order (see the trial matrix in S4 Appendix). The first trial encountered by every physician was always in the safe condition to establish a baseline level of trust with the AI tool and let the physician familiarise themselves with the environment. The number of safe and unsafe scenarios was chosen to balance rec­ ommendation type and statistical power. Physicians experienced more safe than unsafe trials to maintain some form of trust in the system. There was no time pressure on the physicians to make their decisions: in early dry-runs we estimated 7 minutes per trial, so we fitted 6 trials in the 45 minutes allocated to the experiment. Actual trial length depended on the speed of individual physicians. The details of each patient scenario are presented in S2 Appendix.

All AI recommendations were synthetically generated by the research team to ensure a standardised experimental format (i.e., they were not from a real AI system). The definition of unsafe recommendations was based on extreme under- or over-dosing of fluid and/or vaso­ pressor as per previous work [13]. Our conservative approach to defining unsafe doses could lead to an overestimation of the stopping probability. Our design choice was justified by the clinical challenge of establishing dose-specific causality and the difficulty of recruiting large numbers of clinicians. All participating physicians were fully debriefed at the conclusion of the study on the synthetic nature of the AI recommendations so as not to bias their opinions of future interactions with AI-driven systems. Four types of explanations for the fictitious AI system were constructed:a natural language description of the Q-value difference between the recommended action and alternative actions (marker of the extent to which the optimal AI recommendation is significantly better than the alternative or only marginally better), the change in short-term mortality after dosing changes as predicted by the AI, the top-five ranked feature importance for input data contributing to the AI recommendation, and the three most influential training examples during the Q-learning process. These explanations are all realistic explanation types for reinforcement learning decision support systems [36]

During each trial, all physician responses were recorded by a member of the research team sitting in a dead angle in the simulation suite. This data, along with questionnaire answers was reformatted and analysed in Python (code available online here: https://figshare.com/s/78c5ff­ 5c6031f701c0d1). All statistical tests presented in this report compare proportions with a two-sided z-test, giving the probability of rejecting the hypothesis that the proportions of the compared groups are the same. When multiple comparisons are run on the same dataset, the

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 5 / 17

<!-- page 6 -->

p-values are adjusted with the Bonferroni correction. When reporting proportions, we adopt the following format: “[mean] ± [standard error]%, 95% CI: [Weld confidence interval]”. Any reference to a standard deviation is explicit.

### Eye-tracking for gaze recording

In this study, gaze was employed as an indicator of physicians’ attentional focus during sim­ ulations, with particular interest in whether this varied according to the safety of the AI rec­ ommendation. Pupil and first-person videos were recorded with non-invasive commercially available eye-tracking glasses (Pupil Core headset). The Pupil Labs software (Core, version 3.3) utilised both eye cameras to delineate the pupil and estimate the direction of gaze within the recorded field of view.

Prior to the experiment, a two-part 2D calibration procedure was conducted. The initial stage involved a static calibration using five screen markers on a laptop display (default Pupil Labs ‘screen marker’ calibration). Subsequently, a depth-based static exercise was performed, requiring participants to focus on nine screen markers sequentially (‘natural features’ mode) displayed on a 60-inch TV screen, initially at 1 metre and then at 2-metre distance. A laptop (Lenovo Thinkpad) was connected to the eye-tracking glasses for the entire experiment. To allow for unrestricted movement in the suite, the glasses were connected via USB to a battery-­ powered laptop (Lenovo Thinkpad) worn by physicians in a lightweight backpack.

Subjects were eligible for eye-tracking data collection according to the following inclu­ sion criteria: the Pupil Labs glasses were able to detect their pupils, the calibration step was passed successfully, and the glasses-laptop connection was not lost during the experiment. In total, 19/38 physicians passed the calibration exercises and had their gaze-based attention data collected. There was no evidence that this data loss led to any inclusion bias. 13/19 male doctors had gaze data (68% male compared to 66% male in the overall sample). 6/19 senior doctors had gaze data (32% senior compared to 55% senior in the overall sample). Physicians were instructed to point to where they were reading on the handover note at the start of each scenario as a final level of validation that the eye tracking was appropriately calibrated.

We defined four key regions of interest (ROIs) (Fig 1c): the paper ICU data chart, the vital signs monitor, the patient mannequin (Laerdal Simman 3G) and the AI display screen. Four further sub-regions were identified within the AI screen ROI corresponding to four types of explanation for the AI recommendation. April tags (simple QR codes) within the simula­ tion suite (see Fig 1c) were used to identify ROIs in post-processing. As is common practice in eye-tracking literature [37,38], we used the number of gaze fixations per ROI—a fixation being the predominant eye movement occurring when the foveal region of the visual field is held stationary—as a proxy for participant attention.

### Participant recruitment and simulation facility

Recruitment of ICU physicians made use of both convenience sampling and targeted advertis­ ing to a local NHS trust (Imperial College Healthcare NHS Trust) Inclusion criteria were: (i) practising physician, (ii) has worked for two or more months in an adult ICU, (iii) currently works in ICU or has worked in ICU within the last 6 months. Physicians were compensated for their time and each experiment lasted approximately 60 minutes.

### Ethics statement

The study was approved by the Research Governance and Integrity Team (RGIT) at Imperial College London and the UK Health Research Authority (Ref: 22/HRA/1610). Every partici­ pant gave written consent to take part in the study.

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 6 / 17

<!-- page 7 -->

### Results

A total of 38 intensive care physicians took part in the experiment (see Fig 2). This cohort comprised 25 men (66%) and 13 women (34%), proportions in line with the national popula­ tion of intensivists [39]. The balance between junior and senior physicians (with less or more than 5 years of experience respectively) was even and 21% of participants reported having been personally involved or having had experience in AI research.

Each physician completed six (four safe, two unsafe) different patient scenarios leading to a total of 228 recorded trials. Of these trials, 76 featured an unsafe AI recommendation and 152 were safe ones. See S4 Appendix for the full trial matrix.

In total, unsafe AI recommendations were stopped more often than safe AI recommenda­ tions (83 ± 4%, 95% CI: 0.75–0.91 vs. 29 ± 4%, 95% CI: 0.21–0.37, p < 0.0001). The proportion stopping unsafe AI recommendations rose to 92 ± 3%, 95% CI: 0.86–0.98 (p = 0.0823) when including physicians who asked for a senior opinion, which would most likely lead to the unsafe AI recommendation being rejected (see Fig 3a). This analysis was further expanded by categorising physicians into junior (< 5 years of intensive care unit (ICU) experience) and senior (≥5 years of ICU experience) practitioners. There was a non-significant trend for junior physicians to stop AI recommendations less often than senior physicians (79 ± 7%, 95% CI: 0.65–0.93 vs. 83 ± 6%, 95% CI: 0.71–0.95, p = 0.11). Junior physicians asked more often for a second opinion than senior physicians (70 ± 4%, 95% CI: 0.62–0.78 vs. 28 ± 4%, 95% CI: 0.20–0.36, p < 0.0001), which led to more (though not significantly more) unsafe recommen­ dations being stopped or escalated by juniors (94 ± 4%, 95% CI: 0.86–1, against 91 ± 5%, 95% CI: 0.81–1, by seniors, p = 0.12). To bring more depth to the analysis than a binary outcome, we investigated the extent of AI influence which was calculated on a continuous scale from 0 (completely ignoring advice) to 1 (completely relying on advice) using the formula [(final estimate – initial estimate)/ (advice – initial estimate)] per work by Yaniv et al. [40]. The safety status of AI recommendations did not significantly impact this metric, see S5 Appendix. Deeper analysis of AI influence on the same clinical task using the response shift paradigm can be found in earlier work [4,41].

**Fig 2. Recruited cohort demographics (n = 38). – A. Distribution of intensive care experience. Consultant, most senior and equivalent to attending in the United States (US); SpR, specialist registrar and equivalent to fellow in the US; SHO, senior house officer, most junior and equivalent to resident in the US. B. Gender distribution. C. Propor­ tion of physicians who had ever been involved in a research project involving AI. This cohort covers the whole range of experience levels, is in line with national gender ratios and contains both people who have and have not worked with AI.**

https://doi.org/10.1371/journal.pdig.0000726.g002

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 7 / 17

<!-- page 8 -->

**Fig 3. Impact of AI recommendation safety status on clinician decisions, and gaze fixations on each ROI. A. Bar chart of the proportion of stopped safe recommendations, stopped unsafe recommendations and stopped or escalated unsafe recommendations. B. Proportions of requests for senior help before seeing any recommendation and after having seen a safe or an unsafe one. C. Number of gaze fixations on each ROI before revealing the AI recommendation (i.e., there can be no fixations on the AI) D. Number of gaze fixations on each ROI after revealing the AI recommendation (when clinicians have already evaluated the non-AI information sources and so would be expected to look at these much less). Z-score Bonferroni-corrected proportion statistical tests: *** p < 0.0001, ** p < 0.005, * p < 0.05, n.s. not significant, error bars represent the standard error of the mean (SEM), XAI = explainable AI.**

https://doi.org/10.1371/journal.pdig.0000726.g003

Similarly, second-opinion requests rose from 40 ± 3% (95% CI: 0.34–0.46) before seeing any AI recommendation to 57 ± 6% (95% CI: 0.45–0.69) after seeing an unsafe AI recommen­ dation (p = 0.016) but the reduction in requests to 36 ± 4% (95% CI: 0.28–0.44) after seeing a safe AI recommendation was not significant (Fig 3b). Seeing an unsafe rather than a safe AI recommendation triggered more senior/second opinion requests (57 ± 6%, 95% CI: 0.45–0.69 vs. 36 ± 4%, 95% CI: 0.28–0.44, p = 0.0051). Seeing unsafe AI recommendations therefore significantly increased the proportion of requests for senior help.

As expected, prior to the AI recommendation being revealed, no significant difference in gaze fixations on regions of interest (ROIs) was observed between safe and unsafe scenarios regarding the three AI-independent regions (ICU data chart, vital signs monitor, and patient mannequin), see Fig 3c. Subsequent to the disclosure of the AI recommendation, there were more fixations on the AI screen in the unsafe scenarios (mean 960, SD 218) versus safe scenar­ ios (mean 700, SD 236) (p = 0.0015, see Fig 3d). Finally, the number of gaze fixations on the AI explanation ROI was not significantly different between safe and unsafe scenarios.

The distributions of initial fluid and vasopressor dose prescriptions across participants in our six scenarios are shown in Fig 4. These results show wide variation in clinical practice,

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 8 / 17

<!-- page 9 -->

**Fig 4. Clinical practice variability. Distribution of initial (i.e., pre AI reveal) vasopressor (left) and fluid (right) prescrip­ tions by physicians for each patient scenario.**

https://doi.org/10.1371/journal.pdig.0000726.g004

even when given the exact same information. Fig 4 suggests that the extent of the variation in prescribing might depend on case-specific features (e.g., in scenario 2, the patient had already had more fluids than in scenario 1 so physicians gave less fluid, or patient 5 had sepsis related to infected and leaky heart valves so physicians were more careful with both fluid and vasopressor). We also evaluated the extent to which being far from the human mean dose initially was indicative of not stopping unsafe AI recommendations. While subjects with most unsafe AI misses were further from the mean, there was no statistically significant correlation between the distance to human mean in initial dose and likelihood of accepting an unsafe AI recommendation (see S6 Appendix).

We also investigated the extent to which AI recommendations influenced prescription decisions. Physicians changed their prescription (dose of fluids and/or vasopressors) in 46 ± 3% (105/228), 95% CI: 0.40–0.52, of trials after seeing what the AI suggested. Both safe and unsafe AI recommendations influenced human decisions to different extents: fluid doses shifted on average by 80 ml/h (and vasopressor doses by 0.01 mcg/kg/min) after a safe AI recommendation compared to 40 ml/h (and 0.08 mcg/kg/min) after an unsafe AI recommen­ dation. This difference can be attributed to the nature of unsafe AI suggestions, which involve under- or over-dosing of one or both drugs. The larger discrepancy between unsafe AI sugges­ tions and physicians’ typical practices likely contributes to the reduced influence of unsafe rec­ ommendations. Fig 5 shows the shift of distribution in vasopressor prescriptions before and after the AI recommendation was seen for two scenarios (split by whether the entire cohort is considered or only those physicians who did not ask for senior/second opinion). In scenarios (such as number two) where the unsafe AI recommendation was significantly influencing, this did not seem apparent when exclusively considering the physicians who did not request senior help (see S7 Appendix for this plot over all scenarios).

Finally, each physician had one of the two unsafe scenarios extended with a “challenge” section where the bedside nurse (a member of the experimental team) was given three attempts to change the physician’s mind on whether or not to stop the AI recommendation were it to be automatically implemented. In 95 ± 4% (95% CI: 0.87–1.03) of cases (), the verbal input challenge from the bedside nurse did not change the decision of the physician to accept or reject the automated application of the AI recommendation. However, two participants (both junior) were persuaded to change their minds from interrupting an unsafe recommen­ dation to accepting it. While we recorded previous experience with AI as an independent variable, our analyses did not find any impact on the primary outcomes of this study.

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 9 / 17

<!-- page 10 -->

**Fig 5. Shift analysis. Distributions of vasopressors dose distribution before and after having seen a safe or unsafe AI recommendation for two patient scenarios across all physicians (left) and only those who did not ask for senior help/second opinion (right). For each group of physicians and patient scenarios, we show the distributions of doses before seeing any recommendation (grey), after seeing a safe recommendation (blue), and after seeing an unsafe one (yellow). The dashed bars represent the values of the safe and unsafe AI recommendations for each patient scenario. Unsafe AI recommendations do not always influence the final decision. Physicians most influenced by unsafe AI recommendations tend to ask for a second opinion, while those who do not ask for help are less influenced by unsafe recommendations.**

https://doi.org/10.1371/journal.pdig.0000726.g005

### Discussion

Our conclusions on the study objectives include the following:

• AI advice alters treatment decisions and therefore patient care;

• Physicians stop unsafe recommendations more frequently than safe ones, though not all unsafe AI advice was stopped;

• Junior physicians escalate their decision more often than senior physicians do, and unsafe AI recommendations lead to more decision escalation than safe ones;

• Unsafe AI recommendations drew more direct attention than safe ones but the visual atten­ tion brought to AI explanations did not differ;

• Intervention from human colleagues can sway a minority of physicians to follow an unsafe recommendation.

These findings show the importance of educating clinical teams who will interact with a new AI recommender system on the correct intended use of the system, including target patient population, indications, and limitations, as well as the importance of clinical context when integrating the AI recommendations into their practice. We hypothesise that the human influence towards unsafe recommendations could have been avoided by a small briefing on the key points touched on by the bedside nurse: technology benefits, limitations, and legal paradigms. Domain experts should explore how to provide effective education given the context of limited time, resources, and varying AI literacy among clinicians. Similarly, highlevel supervision of junior clinicians using these tools would ensure constant availability of a second opinion to discuss the system’s output in cases where there might be disagreement.

This study reinforces the call for more interdisciplinary and realistic human-AI interaction studies on domain experts [42,43]. Critically, our experimental design also allowed us to study human-human behavioural dynamics during an encounter with AI decision support. This is

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 10 / 17

<!-- page 11 -->

important as most clinical uses of AI-driven decision support tools will be in the context of multi-disciplinary teams where humans other than the final decision-maker can still positively or negatively influence the interaction between the final human decision-maker and the AI. This is why our study was run in a simulation suite: an environment that reproduces natural stimuli of bedside practice for clinicians without any risk to patients.

Our findings highlight important implications for clinical practice that warrant further exploration. Recent work by Hasan et al. examines the ethical considerations of AI in phar­ macy practice and reveals similar themes around patient autonomy, data protection, and the need for regulatory frameworks [44]. Their study found widespread concerns about patient data privacy, cybersecurity threats, and lack of legal regulation among pharmacy profession­ als. To address these issues in clinical settings, we recommend developing comprehensive education and training programs for healthcare professionals that encompass both technical skills and ethical considerations. Such programs could include AI literacy modules, case stud­ ies on responsible AI integration, ethical frameworks for evaluating AI recommendations, and hands-on training with AI tools. Healthcare institutions should also consider establishing AI ethics committees to provide ongoing guidance and oversight.

The ethical implications of using AI in clinical decision-making are profound. While AI has the potential to enhance diagnostic accuracy and treatment optimization, it also raises concerns about the erosion of human judgement and the patient-provider relation­ ship. To mitigate these risks, we advocate for a human-centred approach to AI integration that preserves clinician autonomy while leveraging AI as a supportive tool. By proactively addressing these ethical and practical challenges, healthcare systems can work towards responsible AI adoption that enhances rather than compromises the quality and humanity of patient care.

While eye-tracking is typically used in controlled environments [45], this study demon­ strates the feasibility of using this behavioural phenotypic marker of attention in more realistic, less constrained, environments. Our findings indicate that physicians fixated more on unsafe than safe AI recommendations implying an appropriately higher level of allocated cognitive attention. However, we also observed that physicians did not rely more on AI expla­ nations in the unsafe scenarios calling into question the use of explanations as a mitigation strategy for unsafe AI. Nor did physicians devote significantly more attention to looking back at the ‘traditional’ (non-AI based) clinical data after seeing an unsafe AI recommendation to understand why the recommendation might be unsafe (i.e., there was no outward evidence of a desire to ‘debug’ the unsafe AI recommendation). The eye-tracking and explainability aspects of this experiment are discussed in greater depth in a sister manuscript [34].

The influence of AI recommendations on clinical judgement has been studied previously in vignette-type experiments. In tasks with a gold standard to compare against like medical imaging, AI advice has been shown to impact clinical decisions differently depending on its quality and the level of expertise of the clinical user. In this context, explainability did not help physicians identify biased models [46,47]. Similarly, even in settings with no gold standard like cardiovascular management of sepsis in intensive care, AI advice has been shown to significantly shift final treatment decisions in a vignette setting [4]. This work goes one step closer to clinical deployment by studying these interactions in a high-fidelity simulation envi­ ronment. This setup enabled the study of human-AI interaction with eye-tracking as well as the ability to investigate human-human interactions as they relate to AI. Most safety studies of clinical decision support systems use medication error as both the primary outcome measure and proxy for patient safety [26,48]. Here, we look at systems that are not yet deployed in clinical practice, so measuring prescription error rate directly (and correlating that to ‘error’ without a gold standard) is challenging. Therefore, we tackled the problem from a different

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 11 / 17

<!-- page 12 -->

angle and aimed to estimate the ability of clinicians to spot unsafe treatment recommenda­ tions from an AI tool.

The limitations of the study should also be acknowledged. First, prescribing hourly fluid and vasopressor doses directly is unusual for intensive care physicians who typically indicate blood pressure or urine output targets and let the bedside nurse titrate the actual doses within a reasonable range to reach the set targets. However, direct drug dose recommendation has become the standard for reinforcement learning (RL)-based decision support tools in health­ care [49,50]. While clinicians do not usually work directly with drug doses in their current practice, the AI systems they will encounter in their practice likely will and so our study better replicates the actual context in which clinicians will interact with AI prescription decision support tools in the ICU. Similarly, the simulation limited the physician’s action space to one specific aspect of patient care, preventing action plans that might go beyond the defined possi­ bilities (e.g., altering sedation levels and antimicrobial choices). Moreover, making treatment decisions for the next hour is less dynamic than real clinical practice (where for example the ability to examine a real patient and use advanced cardiac output monitors might add to the nuance of the overall clinical picture).

Although the simulation suite replicates many of the features of the clinical environ­ ment (including real bedside monitors displaying data in real time, with working alarms and some human interactions) it cannot completely replicate the competing priorities and time-­pressured clinical environment of a real intensive care unit. Additionally, we were not able to replicate the dynamic sequential assessment/ treatment decisions provided over time, as we asked subjects for a single decision on each of six separate patients. Assessing multiple decision points in each scenario would have been more reflective of real clinical practice, but would have created an exponential number of potential scenarios, and therefore led to less similar situations to compare in the statistical analysis.

While the data is not the same as might be obtained from real-world settings, it is none­ theless far higher fidelity than comparable vignette studies. Moreover, while running the experiment in a simulation suite increases the ecological validity of the results, it also makes recruitment harder as physicians must physically attend (compared to vignettes which can be performed remotely over the internet). In terms of other data collection inefficiencies, eye-tracking technology fails to capture pupil position for some subjects thus limiting the sta­ tistical power of gaze analysis. This study was run in one simulation suite in a modern univer­ sity hospital which, although providing a controlled and realistic setting, may not fully capture the diversity and nuances present in different hospital environments. Potential biases from the use of convenience sampling were not particularly mitigated against, we thought it was a good trade-off between clinicians’ low availability (frequent out of hours shifts and heavy clinical commitments) and the study’s recruitment target.

Finally, the results from this study demonstrate the existence of human-human influence, within the context of interacting with AI, but the sample size limits the capacity to accurately estimate the likelihood and significance of the phenomenon or generalise it to different settings. The human-human influence in a human-AI team remains an open research field, especially for multi-disciplinary teams.

From a different perspective, one could challenge the definitions of safe and unsafe recommendations used in the scenarios by arguing that there is no ground truth in sepsis resuscitation and that they are therefore subjective. One might even go further and argue that strategies that under- or over-dose in specific patients (compared to the ‘average’) could be desirable in some cases. The scenarios used in this experiment were designed for the unsafe recommendations to be inappropriate to a majority of clinicians and validated by an indepen­ dent panel of intensivists. The introduction of AI-driven decision support tools, particularly

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 12 / 17

<!-- page 13 -->

those using reinforcement learning, aims to improve patient outcomes beyond the current standard of care [51,52]. This means that such systems will give recommendations that differ from what the clinical team would ordinarily have done but potentially without explanation - a “mysterious oracle dilemma” where the AI oracle recommends actions that on average lead to better outcomes but might occasionally be suboptimal, and the users do not get context on the AI recommendation. It will therefore be essential for humans to exert critical thinking and assess how reasonable the AI recommendation is to filter potentially novel but superior calls by the AI from harmful recommendations. This dilemma relates to philosophical discussions on epistemic authority and testimonial knowledge [53,54], and deserves more discussion in future works. Critically, this study does not claim to control for all the potential failure modes of AI recommendation systems in the ICU. Questions of connectivity, data mapping and updates should also be addressed before deploying such systems. For researchers seeking to evaluate safe and unsafe recommendations similarly, we recommend grounding the choice of criteria for decision safety in a combination of legal documentation (i.e., which decision could make the user liable), and/or opinions from a panel of domain experts (in this case, experi­ enced intensivists) as done in (1).

Another interesting angle for analysis is cognitive load, which can be evaluated through eye-tracking proxies [55,56]. These metrics did not show significant correlations with estimated scenario difficulty (see S8 Appendix). Fig 3 shows that recommendation safety impacted the number of fixations on the screen, indicative of a higher mental load. The ques­ tion of task load on clinicians in a real context with AI interaction should be explored further with tools like NASA TLX [57], which are however subjective questionnaires.

As regulators require clear intended purpose statements for software as medical devices [58], our high-fidelity eye-tracking-based approach to evaluating an AI-driven decision support tool serves as a basis for promoting the generation of safety evidence, with a particular emphasis on ecologically valid settings. This work also provides pointers on how medical education could tailor for the increasing use of AI technologies in medical decision-making. Furthermore, the recent rise in popularity of generative AI (most notably as large language models) highlights the safety concerns of hallucinatory outputs that might be acted upon in a clinical setting and bring harm to patients [59,60]. The unsafe AI recommendations in this work share characteristics with generative AI hallucinations: they are presented to users with no warning and as much confidence as safe recommendations. It is likely that an AI system that shows overall super­ human performance in a given task will still show lower-quality performance in some specific cases [61]. Solutions such as uncertainty-aware models or explainable AI might help users dif­ ferentiate between well-informed recommendations and flawed calls [41,62,63]. The human-AI interactions at the bedside, with a particular focus on high-pressure decision-making, would also help to accelerate the safe translation of AI-based decision support tools to the bedside.

To conclude, it is critical for clinician acceptance, regulatory compliance and real-world adoption that we evaluate cooperation between clinical experts and AI decision-support tools in high-fidelity settings. This study demonstrates the influence of AI recommendations on clinical behaviour and suggests that the vast majority of unsafe AI recommendations are appropriately rejected by bedside clinicians. The findings on junior physicians occasionally accepting an unsafe AI recommendation and their general willingness to seek senior help when unsure should inform the intended use (i.e., some tools might need to be only used by junior clinicians if they have access to senior advice). We study the role of XAI in greater detail in our sister manuscript [64]. Uncertainty awareness, novel forms of AI interpretability and a better understanding of human-human interactions (i.e., team decisions) in the context of AI-driven decision support will help not only with assuring safety from a regulatory perspec­ tive but also in fostering confidence and trust from clinician end-users.

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 13 / 17

<!-- page 14 -->

### Supporting information

S1 Appendix. Pre-experiment questionnaire filled in by every subject to draw a picture of each subject’s profile. (DOCX)

S2 Appendix. List of all patient scenarios used in this study, with their safe and unsafe ver­ sions, as well as a justification for them. (DOCX)

S3 Appendix. Scripts of the challenges used by the accomplice bedside nurse to challenge toe clinician’s decisions to follow or not the AI in the “challenged unsafe” arm of the experiment. (DOCX)

S4 Appendix. Trial matrix of the experiment showing the psrudo-random order of trials and conditions. (DOCX)

S5 Appendix. Extension of the persuasion coefficient analysis of both safe and unsafe AI recommendations. (DOCX)

S6 Appendix. Analysis of the link between clinicians giving initial doses far away from the average of their peers and their likelihood of accepting an unsafe AI recommendation. (DOCX)

S7 Appendix. Extension of Fig 5 showing the dose distribution shifts for all patient scenarios and conditions. (DOCX)

S8 Appendix. Graphs of eye-tracking based cognitive load metrics. (DOCX)

### Author contributions

Conceptualization: Paul Festor, Myura Nagendran, Anthony C. Gordon, Aldo A. Faisal,

Matthieu Komorowski.

Data curation: Paul Festor, Myura Nagendran.

Formal analysis: Paul Festor, Myura Nagendran, Aldo A. Faisal.

Funding acquisition: Anthony C. Gordon, Aldo A. Faisal.

Investigation: Paul Festor, Myura Nagendran, Aldo A. Faisal, Matthieu Komorowski.

Methodology: Paul Festor, Myura Nagendran, Aldo A. Faisal.

Project administration: Anthony C. Gordon, Aldo A. Faisal, Matthieu Komorowski.

Resources: Aldo A. Faisal.

Software: Paul Festor, Myura Nagendran, Aldo A. Faisal.

Supervision: Anthony C. Gordon, Aldo A. Faisal, Matthieu Komorowski.

Validation: Myura Nagendran.

Visualization: Paul Festor, Myura Nagendran.

Writing – original draft: Paul Festor, Myura Nagendran.

Writing – review & editing: Paul Festor, Myura Nagendran, Anthony C. Gordon, Aldo A.

Faisal, Matthieu Komorowski.

PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 14 / 17

<!-- page 15 -->

## References

1. Wang G, Liu X, Ying Z, Yang G, Chen Z, Liu Z, et al. Optimized glycemic control of type 2 diabetes with reinforcement learning: a proof-of-concept trial. Nat Med. 2023 Sep 14;29:2633–42. https://doi. org/10.1038/s41591-023-02552-9 PMID: 37710000

2. Zhan X, Xu H, Zhang Y, Zhu X, Yin H, Zheng Y. DeepThermal: combustion optimization for thermal power generating units using offline reinforcement learning. Proc AAAI Conf Artif Intell. 2022 Jun 28;36(4):4680–8. https://doi.org/10.1609/aaai.v36i4.20393

3. Galea SA. Better science for better decision-making in future crises. Nat Hum Behav. 2021;5(11):1463–63. https://doi.org/10.1038/s41562-021-01226-1 PMID: 34675368

4. Nagendran M, Festor P, Komorowski M, Gordon AC, Faisal AA. Quantifying the impact of AI rec­ ommendations with explanations on prescription decision making. NPJ Digital Med. 2023 Nov 7;6(1):206. https://doi.org/10.1038/s41746-023-00955-z PMID: 37935953

5. Köbis N, Bonnefon JF, Rahwan I. Bad machines corrupt good morals. Nat Hum Behav. 2021 Jun;5(6):679–85. https://doi.org/10.1038/s41562-021-01128-2 PMID: 34083752

6. Festor P, Habli I, Jia Y, Gordon A, Faisal AA, Komorowski M. Levels of Autonomy and Safety Assur­ ance for AI-Based Clinical Decision Systems. Springer; 2021. p. 291–6.

7. European Parliament and Council. Regulation (EU) 2024/Artificial Intelligence Act [Internet]. 2024. Available from: https://artificialintelligenceact.eu/wp-content/uploads/2024/01/AI-Act-FullText.pdf

8. Hong J, Levine S, Dragan A. Learning to influence human behavior with offline reinforcement learning. Advances in neural information processing systems. 2023;36. Available from: https:// proceedings.neurips.cc/paper_files/paper/2023/file/70f286e0fc977c0a3a64ef96849c8d7d-Paper-­ Conference.pdf

9. Christiano PF, Leike J, Brown T, Martic M, Legg S, Amodei D. Deep reinforcement learning from human preferences. Advances in neural information processing systems. 2017;30. Available from: https://papers.nips.cc/paper_files/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-­ Abstract.html

10. Monarch RM. Human-in-the-Loop Machine Learning: Active learning and annotation for human-­ centered AI. Simon and Schuster; 2021 Aug 17.

11. Cadario R, Longoni C, Morewedge CK. Understanding, explaining, and utilizing medical artificial intelligence. Nat Hum Behav. 2021 Dec ;5(12):1636–42. https://doi.org/10.1038/s41562-021-01146-0 PMID: 34183800

12. Jia Y, Burden J, Lawton T, Habli I. Safe reinforcement learning for sepsis treatment. In: 2020 IEEE International conference on healthcare informatics (ICHI). IEEE; 2020. p. 1–7.

13. Festor P, Jia Y, Gordon AC, Faisal AA, Habli I, Komorowski M. Assuring the safety of AI-based clinical decision support systems: a case study of the AI Clinician for sepsis treatment. BMJ Health Care Inform. 2022;29(1):e100549. https://doi.org/10.1136/bmjhci-2022-100549 PMID: 35851286

14. Peng X, Ding Y, Wihl D, Gottesman O, Komorowski M, et al. Improving sepsis treatment strategies by combining deep and kernel-based reinforcement learning. American Medical Informatics Association; 2018. p. 887.

15. Yealy DM, Mohr NM, Shapiro NI, Venkatesh A, Jones AE, Self WH. Early care of adults with suspected sepsis in the emergency department and out-of-hospital environment: a consensus-­based task force report. Ann Emerg Med. 2021;78(1):1–19. https://doi.org/10.1016/j. annemergmed.2021.02.006 PMID: 33840511

16. Van der Ven W, Schuurmans J, Schenk J, Roerhorst S, Cherpanath T, Lagrand WK, et al. Moni­ toring, management, and outcome of hypotension in intensive care unit patients, an international survey of the European Society of Intensive Care Medicine. J Crit Care. 2022;67:118–25. https://doi. org/10.1016/j.jcrc.2021.10.008 PMID: 34749051

17. De Backer D, Deutschman CS, Hellman J, Myatra SN, Ostermann M, Prescott HC, et al; Surviv­ ing Sepsis Campaign Research Committee. Surviving sepsis campaign research priorities 2023. Crit Care Med. 2024 Feb;52(2):268–96. https://doi.org/10.1097/CCM.0000000000006135 PMID: 38240508

18. Rudd KE, Johnson SC, Agesa KM, Shackelford KA, Tsoi D, Kievlan DR, et al. Global, regional, and national sepsis incidence and mortality, 1990-2017: analysis for the Global Burden of Disease Study. Lancet (London, England). 2020;395(10219):200–11. https://doi.org/10.1016/S0140-6736(19)32989-7 PMID: 31954465

19. Asan O, Bayrak AE, Choudhury A. Artificial Intelligence and Human Trust in Healthcare: Focus on Clinicians. J Med Internet Res. 2020 Jun 19;22(6):e15154. https://doi.org/10.2196/15154 PMID: 32558657 PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 15 / 17

<!-- page 16 -->

20. Van de Sande D, Van Genderen ME, Huiskens J, Gommers D, van Bommel J. Moving from bytes to bedside: a systematic review on the use of artificial intelligence in the intensive care unit. Intensive Care Med. 2021;47(7):750–60. https://doi.org/10.1007/s00134-021-06446-7 PMID: 34089064

21. Esmaeilzadeh P. Challenges and strategies for wide-scale artificial intelligence (AI) deployment in healthcare practices: a perspective for healthcare organizations. Artif Intell Med. 2024 May 1;151:102861. https://doi.org/10.1016/j.artmed.2024.102861 PMID: 38555850

22. Wilson FP, Martin M, Yamamoto Y, Partridge C, Moreira E, Arora T, et al. Electronic health record alerts for acute kidney injury: multicenter, randomized clinical trial. BMJ. 2021 Jan 18;372:m4786. https://doi.org/10.1136/bmj.m4786 PMID: 33461986

23. Saposnik G, Redelmeier D, Ruff CC, Tobler PN. Cognitive biases associated with medical decisions: a systematic review. BMC Med Inform Decis Mak. 2016 Nov 3;16(1):138. https://doi.org/10.1186/s12911016-0377-1 PMID: 27809908

24. Sujan M, Furniss D, Grundy K, Grundy H, Nelson D, Elliott M, et al. Human factors challenges for the safe use of artificial intelligence in patient care. BMJ Health Care informat. 2019;26(1):e100081. https://doi.org/10.1136/bmjhci-2019-100081 PMID: 31780459

25. Dawson NV, Arkes HR. Systematic errors in medical decision making: judgment limitations. J Gen Intern Med. 1987;2(3):183–7. https://doi.org/10.1007/BF02596149 PMID: 3295150

26. Kaushal R, Shojania KG, Bates DW. Effects of computerized physician order entry and clinical decision support systems on medication safety: a systematic review. Arch Intern Med. 2003 Jun 23;163(12):1409–16. https://doi.org/10.1001/archinte.163.12.1409 PMID: 12824090

27. Quinan PS, Padilla LM, Creem-Regehr SH, Meyer M. Towards ecological validity in evaluating uncer­ tainty. Proceedings of Workshop on Visualization for Decision Making Under Uncertainty, 2015.

28. Madras D, Pitassi T, Zemel R. Predict responsibly: improving fairness and accuracy by learning to defer. Advances in neural information processing systems. 2018;31. Available from: https://proceed­ ings.neurips.cc/paper_files/paper/2018/hash/09d37c08f7b129e96277388757530c72-Abstract.html

29. Cato DL, Murray M. Use of Simulation Training in the Intensive Care Unit. Crit Care Nurs Q. 2010 Mar;33(1):44–51. https://doi.org/10.1097/CNQ.0b013e3181c8dfd4 PMID: 20019509.

30. Chang M, Büchel D, Reinecke K, Lehmann T, Baumeister J. Ecological validity in exercise neuro­ science research: A systematic investigation. Eur J Neurosci. 2022 Jan;55(2):487–509. https://doi. org/10.1111/ejn.15595 PMID: 34997653

31. EU AI Act Article 8 [Internet]. Artificial Intelligence Act. [cited 2023 Sep 29]. Available from: https://arti­ ficialintelligenceact.com/title-iii/chapter-2/article-8/

32. GOV.UK [Internet]. Software and AI as a Medical Device Change Programme. 2023 [cited 2023 Oct 2]. Available from: https://www.gov.uk/government/publications/ software-and-ai-as-a-medical-device-change-programme

33. Fiannaca A, Bennett C, Kane S, Morris MR. Beyond safety: toward a value-sensitive approach to the design of AI systems. 2022

34. Nagendran M, Festor P, Komorowski M, Gordon AC, Faisal AA. Eye tracking insights into physician behaviour with safe and unsafe explainable AI recommendations. NPJ Digit Med. 2024;7(1):202. https://doi.org/10.1038/s41746-024-01200-x PMID: 39095449

35. Joshi A, Kale S, Chandel S, Pal DK. Likert scale: Explored and explained. Br J Appl Sci Technol. 2015;7(4):396–403. https://doi.org/10.9734/bjast/2015/14975

36. Milani S, Topin N, Veloso M, Fang F. A survey of explainable reinforcement learning. arXiv preprint arXiv:2202.08434. 2022.

37. Harston JA, Faisal AA. Methods and models of eye-tracking in natural environments. In: Eye Tracking: Background, Methods, and Applications. Springer; 2022. p. 49–68.

38. Gidlöf K, Wallin A, Dewhurst R, Holmqvist K. Using eye tracking to trace a cognitive process: Gaze behaviour during decision making in a natural environment. J Eye Mov Res. 2013;6(1).

39. Women in Intensive Care Medicine | The Faculty of Intensive Care Medicine [Inter­ net]. [cited 2023 Jan 4]. Available from: https://www.ficm.ac.uk/careersworkforceworkforce/ women-in-intensive-care-medicine

40. Yaniv I. Receiving other people’s advice: Influence and benefit. Organ Behav Hum Decis Process. 2004;93(1):1–13. https://doi.org/10.1016/j.obhdp.2003.08.002

41. Shafti A, Derks V, Kay H, Faisal AA. The response shift paradigm to quantify human trust in AI recom­ mendations. arXiv preprint arXiv:2202.08979. 2022.

42. Xu W, Dainoff MJ, Ge L, Gao Z. From human-computer interaction to human-AI Interaction: new chal­ lenges and opportunities for enabling human-centered AI. 2021;5. ArXiv Prepr ArXiv210505424 PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 16 / 17

<!-- page 17 -->

43. Zhang Y, Liao QV, Bellamy RKE. Effect of confidence and explanation on accuracy and trust calibra­ tion in AI-assisted decision making. In: Proceedings of the 2020 Conference on Fairness, Accountabil­ ity, and Transparency [Internet]. Barcelona Spain: ACM; 2020.

44. Hasan HE, Jaber D, Khabour OF, Alzoubi KH. Ethical considerations and concerns in the implemen­ tation of AI in pharmacy practice: a cross-sectional study. BMC Med Ethics. 2024 May 16;25(1):55. https://doi.org/10.1186/s12910-024-01062-8 PMID: 38750441

45. Cao S, Huang CM. Understanding User Reliance on AI in Assisted Decision-Making. Proc ACM Hum-Comput Interact. 2022;6(CSCW2):1–23. https://doi.org/10.1145/3555572

46. Gaube S, Suresh H, Raue M, Merritt A, Berkowitz SJ, Lermer E, et al. Do as AI say: susceptibility in deployment of clinical decision-aids. NPJ Digit Med. 2021 Feb 19;4(1):1–8. https://doi.org/10.1038/ s41746-021-00385-9 PMID: 39095449

47. Jabbour S, Fouhey D, Shepard S, Valley TS, Kazerooni EA, Banovic N, et al. Measuring the impact of AI in the diagnosis of hospitalized patients: a randomized clinical vignette survey study. JAMA. 2023;330(23):2275–84. https://doi.org/10.1001/jama.2023.22295 PMID: 38112814

48. Ranji SR, Rennke S, Wachter RM. Computerised provider order entry combined with clinical decision support systems to improve medication safety: a narrative review. BMJ Qual Saf. Sep;23(9):773–80. https://doi.org/10.1136/bmjqs-2013-002165 PMID: 24728888

49. Catling FJR, Nagendran M, Festor P, Bien Z, Harris S, Faisal AA, et al. Data-driven decision support for individualised cardiovascular resuscitation in sepsis: a scoping review and primer for clinicians. 2023;2023-08. medRxiv.

50. Liu S, See KC, Ngiam KY, Celi LA, Sun X, Feng M. Reinforcement learning for clinical decision support in critical care: comprehensive review. J Med Internet Res. 2020;22(7):e18477. https://doi. org/10.2196/18477 PMID: 32706670

51. Komorowski M, Celi LA, Badawi O, Gordon AC, Faisal AA. The artificial intelligence clinician learns optimal treatment strategies for sepsis in intensive care. Nat Med. 2018;24(11):1716–20. https://doi. org/10.1038/s41591-018-0213-5 PMID: 30349085

52. Zhang K, Wang H, Du J, Chu B, Arévalo AR, Kindle R, et al. An interpretable RL framework for pre-deployment modeling in ICU hypotension management. NPJ Digit Med. 2022 Nov 18;5(1):1–10. https://doi.org/10.1038/s41746-022-00708-4 PMID: 30349085

53. Zagzebski LT. Epistemic authority: A theory of trust, authority, and autonomy in belief. Oxford Univer­ sity Press; 2012.

54. Coady CAJ. Testimony: A philosophical study. Clarendon Press; 1992.

55. Krejtz K, Duchowski AT, Niedzielska A, Biele C, Krejtz I. Eye tracking cognitive load using pupil diameter and microsaccades with fixed gaze. PLoS One. 2018 Sep 14;13(9):e0203629. https://doi. org/10.1371/journal.pone.0203629 PMID: 30216385

56. Zagermann J, Pfeil U, Reiterer H. Measuring Cognitive Load using Eye Tracking Technology in Visual Computing. In: Proceedings of the Sixth Workshop on Beyond Time and Errors on Novel Evaluation Methods for Visualization [Internet]. Baltimore MD USA: ACM; 2016 p. 78–85.

57. Hart SG. Nasa-Task Load Index (NASA-TLX); 20 Years Later. Proc Hum Factors Ergon Soc Ann Meet. 2006 Oct;50(9):904–8. https://doi.org/10.1177/154193120605000909

58. GOV.UK [Internet]. Crafting an intended purpose in the context of software as a medical device (SaMD). [cited 2023 Mar 28]. Available from: https://www.gov.uk/government/publi­ cations/crafting-an-intended-purpose-in-the-context-of-software-as-a-medical-device-samd/ crafting-an-intended-purpose-in-the-context-of-software-as-a-medical-device-samd

59. Azamfirei R, Kudchadkar SR, Fackler J. Large language models and the perils of their hallucinations. Crit Care. Mar;27(1):120. https://doi.org/10.1186/s13054-023-04393-x PMID: 36945051

60. Banovic N, Yang Z, Ramesh A, Liu A. Being Trustworthy is Not Enough: How Untrustworthy Artificial Intelligence (AI) Can Deceive the End-Users and Gain Their Trust. Proc ACM Hum-Comput Interact. 2023 Apr 16;7(CSCW1):1–17. https://doi.org/10.1145/3579460

61. Quinonero-Candela J, Sugiyama M, Schwaighofer A, Lawrence ND. Dataset Shift in Machine Learn­ ing. MIT Press; 2022. p. 246.

62. Festor P, Luise G, Komorowski M, Faisal AA. Enabling risk-aware Reinforcement Learning for medical interventions through uncertainty decomposition. ICML. 2021.

63. Trombley CM, Gulum MA, Ozen M. Evaluating Uncertainty-Based Deep Learning Explanations for Prostate Lesion Detection. MLHC. 2022.

64. Nagendran M, Festor PG, Komorowski M, Gordon AC, Faisal AA. Clinical Evaluation Framework Using Behavioural & Visual Attention Read-Outs for Explainable AI (XAI). Available from: SSRN 4496127 PLOS Digital Health | https://doi.org/10.1371/journal.pdig.0000726 February 24, 2025 17 / 17
