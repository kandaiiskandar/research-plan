# A Hybrid AI and Rule-Based Decision Support System for Disease Diagnosis and Management Using Labs

---

## 📄 Paper Information

- **Authors:** Muhammad Hammad Maqsood, Mubashir Sajid, Khubaib Ahmed, Muhammad Usamah Shahid, Muddassar Farooq  
- **Affiliation:** CureMD Research, 80 Pine St 21st Floor, New York, NY 10005, United States  
- **Emails:** {hammad.maqsood, mubashir.sajid, khubaib.ahmed, muhammad.usamah, muddassar.farooq}@curemd.com  
- **Organization Website:** https://www.curemd.com/  
- **Year:** 2026  
- **Source:** arXiv  
- **arXiv ID:** 2603.14876  
- **Category:** cs.AI  
- **Submission Date:** 16 March 2026  
- **Document Type:** Research Paper (Preprint)  
- **Pages:** 13  

---

## Abstract

This research paper outlines the development and implementation of a novel Clinical Decision Support System (CDSS) that integrates AI predictive modeling with medical knowledge bases. It utilizes the quantifiable information elements in lab results for inferring likely diagnoses a patient might have. Subsequently, suggesting investigations to confirm the likely diagnoses – an assistive tool for physicians.  

The system fuses knowledge contained in a rule-base expert system with inferences of data driven predictors based on the features in labs. The data for 593,055 patients was collected from 547 primary care centers across the US to model our decision support system and derive Real-Word Evidence (RWE) to make it relevant for a large demographic of patients.  

Our Rule-Base comprises clinically validated rules, modeling 59 health conditions that can directly confirm one or more of diseases and assign ICD-10 codes to them. The Likely Diagnosis system uses multi-class classification, covering 37 ICD-10 codes, which are grouped together into 11 categories based on the labs that physicians prescribe to confirm the diagnosis.  

This research offers a novel system that assists a physician by utilizing medical profile of a patient and routine lab investigations to predict a group of likely diseases and then confirm them, coupled with providing explanations for inferences, thereby assisting physicians to reduce misdiagnosis of patients in clinical decision-making.

---

## Keywords

Clinical Decision Making · Hybrid CDSS · Laboratory Data Analysis · AI in Healthcare  

---

## 1. Introduction

Clinical Decision Support Systems (CDSS) are vital tools in modern healthcare, designed to enhance medical decisions by leveraging knowledge and patients’ data to provide insights. These systems help physicians use RWE derived from Real World EMR Data.  

These systems integrate data from a variety of sources to recommend actionable interventions, improving patient outcomes and streamlining healthcare processes. They assist healthcare providers by offering decision-support tools that are directly integrated into clinical workflows of EMR systems.  

Despite advances in technology, many CDSS remain restricted, primarily utilizing either rule-based algorithms or classical artificial intelligence (AI) techniques without fully integrating both approaches to harness their combined potential.  

Knowledge driven rule-based systems have historically enjoyed higher acceptability among physicians as the rules can be clinically validated by providers. Machine learning (ML) systems, however, offer higher predictive accuracy but often lack interpretability and trust.

---

## 2. The Proposed CDSS

### 2.1 System Overview

This paper introduces a CDSS that integrates Machine Learning (ML) with a rule-based framework to provide a robust support mechanism for diagnosing a wide range of diseases with a focus on interpretability.

### Components

#### Diagnosis Confirming Module
This component assigns International Classification of Diseases (ICD-10) codes to patients based on a disease specific rule base, made using clinical guidelines of relevant associations or institutes, by factoring in demographics and laboratory results.

#### Likely Diagnosis Assistive Module
By analyzing laboratory results, which offer a quantifiable snapshot of a patient’s health profile, this component predicts potential diagnoses and helps physicians in focusing their diagnostic efforts.

---

### CDSS Output

1. Rule-Based Diagnosis Confirmation  
2. Multiclass Probabilities (Likely Diagnosis)  
3. Prediction Explanation via SHAP Values  
4. Recommendation for Follow-Up Labs  

---

## 3. Data Overview

The dataset utilized for developing and validating the proposed Clinical Decision Support System (CDSS) uses demographic (age and gender) of patients, and laboratory results extracted from anonymized CureMD EHR data.

- Total records: 593,055  
- Sources: 547 primary care centers  
- Time span: 2000–2023  

---

## 4. Methodology

### 4.1 Diagnosis Confirmation Methodology

The Diagnosis Confirmation System is designed to utilize lab results to confirm patient diagnoses. It is based on a rule-based expert system, where each rule within the rule base can confirm a diagnosis if conditions in the antecedents are met.

Each rule includes:
- lab test identifier  
- comparison value  
- unit  
- comparison type  

The system includes rules for 59 health conditions.

---

### 4.2 Likely Diagnosis Methodology

The system uses XGBoost for multi-class classification to infer likely diagnoses based on available lab data.

- Training split: 80%  
- Testing split: 20%  
- Cross-validation: 5-fold  

---

## 5. Results and Discussion

### Top-N Accuracy

| N | Accuracy (%) |
|--|-------------|
| 1 | 31.18 |
| 5 | 83.10 |
| 11 | 99.6 |

The Top-5 approach provides an optimal trade-off between accuracy and number of predicted diseases.

---

## 6. Conclusion

In this paper, we propose a novel disease inference engine that fuses the knowledge from a rule based expert system with the prediction models of ML to overcome the shortcomings of each one of them.  

The likely diagnosis system serves as an assistant to a physician, helping in correctly diagnosing a patient and recommending subsequent investigations. The expert system confirms the diagnosis based on rules when additional lab results are available.

---

## Limitations and Future Work

- Limited to laboratory data  
- Does not include patient history or symptoms  

Future work includes:
- treatment recommendations  
- procedural guidance  
- system expansion  

---

## References

(References preserved as in original paper)