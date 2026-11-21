# Merging Deep Learning with Rule-Based and Explainable Techniques Across Imaging Modalities

> **Source PDF:** `Merging Deep Learning with Rule-Based and Explainable Techniques Across Imaging Modalities.pdf` · **Pages:** 6 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Hybrid AI Framework for Accurate Diagnostics:

Merging Deep Learning with Rule-Based and Explainable Techniques Across Imaging Modalities

2025 Third International Conference on Cyber Physical Systems, Power Electronics and Electric Vehicles (ICPEEV) | 979-8-3315-8606-5/25/$31.00 ©2025 IEEE | DOI: 10.1109/ICPEEV67897.2025.11291270

Naga Nirmala Kongara

Dr. B. Sujatha

Dr. Bhukya Krishna, Professor, Department of CSE Gandhi Institute of Engineering and

Research Scholar Department of CSE Gandhi Institute of Engineering and

Professor Godavari Institute of Engineering &

Technology, NH-5, Chaitanya Knowledge City, Rajahmundry

Technology University, Gunupur

Technology University, Gunupur

Odisha, India. dr.krishnab@giet.edu

Odisha, India. kongaranaga.nirmala@giet.edu

Andhra Pradesh, India birudusujatha@gmail.com

Abstract: This paper presents a robust hybrid artificial intelligence (AI) framework designed to improve diagnostic accuracy in medical imaging tests such as magnetic resonance imaging (MRI), computed tomography (CT), and positron emission tomography (PET) scans. The enhancement is achieved by combining deep learning methods with rule-based reasoning and model-agnostic explainability techniques. The proposed hybrid architecture integrates convolutional neural networks (CNNs) and transformer models for feature extraction, while incorporating expert-defined rule-based logic to strengthen interpretability and ensure consistency in decision-making. To improve transparency, modelagnostic explainability approaches such as SHAP (Shapley Additive Explanations) and LIME (Local Interpretable Model-Agnostic Explanations) are applied, offering deeper insights into AI-driven diagnoses. This integration addresses critical clinical concerns related to trust, traceability, and adoption of AI systems. Experimental evaluations conducted on benchmark medical imaging datasets achieved an accuracy of 94.2%, which is 3.8% higher than conventional deep learning approaches, demonstrating improved robustness. Additionally, the proposed system enhances clinical interpretability, with a 21% increase in explainability ratings provided by healthcare professionals. These findings highlight the novelty and clinical relevance of hybrid AI models by combining automation with decision support, thereby promoting greater trust and adoption of AI in diagnostic workflows across healthcare facilities.

classification, segmentation, and anomaly detection. However, these models are often perceived as “black boxes,” offering limited transparency in their decisionmaking despite high accuracy. This lack of interpretability hinders clinical acceptance, where trust, traceability, and transparency are as critical as diagnostic accuracy. A further strength of the proposed system is the integration of model-agnostic explanation methods such as SHAP and LIME, which provide post hoc interpretability by identifying the contribution of individual features to predictions. SHAP highlights critical image regions by assigning importance scores, while LIME builds simplified surrogate models to approximate local behavior of the complex system. Together, these tools enable clinicians to validate AIdriven predictions, reinforcing trust and transparency. The proposed framework was evaluated on publicly available MRI, CT, and PET datasets. Results demonstrated a mean diagnostic accuracy of 94.2%, representing a 3.8% improvement over conventional deep learning models. Furthermore, clinical experts reported a 21% improvement in explainability ratings, indicating that the hybrid model better supports human–AI collaboration in diagnostic workflows. By combining deep learning, rule-based systems, and model-agnostic interpretability, this work introduces a foundation for a new class of AI tools in medical imaging. The framework achieves strong diagnostic performance while ensuring transparent reasoning, making it suitable for real-world clinical environments. With further refinement and large-scale validation, such systems have the potential to support early diagnosis, treatment planning, and informed clinical decision-making— thereby advancing safe, explainable, and trustworthy AI adoption in healthcare.

Keywords: Hybrid AI, Deep Learning, Explainability Techniques, Medical Imaging, CNN, Transformer Architecture, Rule-Based Systems, Diagnostic Accuracy

I. INTRODUCTION: Medical imaging is a cornerstone of modern healthcare, supporting early detection, diagnosis, and treatment of diseases such as cancer, neurological disorders, and cardiovascular conditions. Advanced imaging modalities, including MRI, CT, and PET scans, provide detailed views of anatomical and physiological structures, enabling clinicians to make informed decisions. In recent years, deep learning has transformed medical image analysis by achieving state-of-the-art results in

**Fig. 1: Block Diagram of Developed work**

979-8-3315-8606-5/25/$31.00 ©2025 IEEE

<!-- page 2 -->

II. LITERATURE REVIEW Deep learning has significantly advanced medical imaging by enabling automated classification, segmentation, and anomaly detection. However, a major limitation of these models is their lack of interpretability, which restricts their integration into clinical workflows where transparency and trust are essential. To address these challenges, recent studies have explored reinforcement learning, competitive learning, and hybrid frameworks that embed interpretability mechanisms.

Zhou et al. [1] proposed a meta-learning approach using reinforcement learning, which improved stability and localization in ultrasound and cephalometric X-ray analysis. Similarly, Ahmadian and Reza-Alikhani [3] introduced a super-resolution algorithm based on competitive learning that enhanced MRI image quality. While effective, these models are computationally expensive and highly domain-specific, thereby limiting generalizability.

Qiu et al. [4] developed a Dual-Stream Shared Feature model that achieved higher segmentation accuracy but lacked efficiency in low-resource environments. Wang et al. [7] introduced a Transformer-enhanced U-Net for brain tumor (BraTS 2019) and liver (CHAOS) segmentation, which achieved state-of-the-art performance but required substantial GPU resources.

For explainability, Zhuang et al. [11] proposed a Weakly Supervised Similarity Analysis Network for lung CT retrieval, which reduced reliance on annotated data but occasionally compromised accuracy. Yang et al. [13] applied Multiple Instance Learning (MIL) with transformers for diabetic retinopathy detection, achieving strong accuracy but demonstrating sensitivity to datasetspecific characteristics.

Hybrid approaches have also been investigated to balance performance and interpretability. Cai et al. [12] applied Sparse Bayesian Learning for brain imaging, improving spatial feature representation though computational efficiency remained a concern. Lang et al. [14] designed a 3D Mask R-CNN for craniomaxillofacial landmark localization with high accuracy; however, its dependence on high-resolution cone-beam CT data limits broader applicability.

Relevance to the Proposed Hybrid AI Model

While existing deep learning models emphasize accuracy, their lack of interpretability remains a critical obstacle for clinical adoption. The proposed Hybrid AI Model addresses this gap by combining data-driven feature extraction with rule-based reasoning and interpretable outputs using SHAP and LIME. This integration provides both strong diagnostic accuracy and transparent reasoning, thereby fostering clinician trust and enabling wider adoption across multiple imaging modalities. By

embedding clinical rules and explanation processes into a high-performance AI framework, the model ensures more reliable, reproducible, and transparent decision-making in healthcare applications

### III.NOVELTY OF THE PROPOSED WORK

Unlike conventional deep learning models that function as black-box systems, the proposed approach integrates rulebased reasoning with model-agnostic explanation techniques to deliver significant improvements in transparency and interpretability for diagnostic applications.

The framework leverages transformer-based architectures for high-level abstraction, enabling better extraction of global contextual features from medical images—an aspect particularly valuable for complex diagnostic tasks.

A multi-stage decision fusion mechanism is employed, combining the outputs of deep learning models with rulebased logic. This fusion enhances diagnostic robustness and provides clinicians with greater confidence in the results by aligning automated predictions with established medical reasoning.

Compared with Qiu et al.’s feature similarity-based model and Wang et al.’s self-distilled Transformer U-Net, the proposed hybrid model achieves a more effective balance among diagnostic accuracy, interpretability, and computational efficiency, making it highly suitable for real-world clinical deployment.

## IV. PROPOSED METHODOLOGY

The proposed hybrid AI framework integrates deep learning, rule-based expert systems, and model-agnostic explainability techniques to enhance diagnostic accuracy and interpretability. This section details each component with a mathematical formulation to describe their functioning comprehensively.

A.Deep Learning Component Feature Extraction and Classification Deep learning models, primarily Convolutional Neural Networks (CNNs) and Transformer-based architectures, are employed for feature extraction. Given an input medical image 𝐼, a CNN extracts features using a set of convolutional filters: 𝐹= 𝜎(𝑊∗𝐼+ 𝑏) (1) where:

• 𝑊 represents the convolutional filters,

o denotes the convolution operation, • 𝑏 is the bias term, and • 𝜎 is a non-linear activation function, typically ReLU. The Transformer-based architectures such as Vision Transformers (ViTs) process image patches using self-

<!-- page 3 -->

attention mechanisms. Given an image split into 𝑃× 𝑃 patches, the feature embedding 𝑍 is computed as:

𝑄𝐾𝑇

```math
√𝑑𝑘) 𝑉        (2)
```

𝑍= Softmax⁡ (

where:

• 𝑑𝑘 is the dimension of the key vectors, • Softmax normalizes the attention scores. The extracted features are then fine-tuned using a fully connected classifier: 𝑦= Softmax⁡(𝑊𝑓𝐹+ 𝑏𝑓) (3) where 𝑊𝑓 and 𝑏𝑓 are the trainable parameters for classification. B. Rule-Based Expert System Integration of Domain Knowledge A rule-based expert system complements the deep learning predictions by embedding medical domain knowledge. The system follows an if-then rule format: 𝑅𝑗: ⁡ IF ⁡𝑋𝑘∈𝐶𝑚⁡ THEN ⁡𝑦= 𝑙𝑛 (4) where:

• 𝑋𝑘 is the input feature, • 𝐶𝑚 is the condition defined by domain experts, • 𝑦 is the predicted label 𝑙𝑛. Such rules were derived from standard radiological guidelines (e.g., BI-RADS and Fleischner criteria) and implemented using decision trees to enable fast runtime logic evaluation. Rule-Based Decision Making To fuse deep learning outputs with rule-based logic, an inference engine evaluates predefined medical conditions using Boolean logic: 𝐷= ⋁ 𝑛 𝑖=1 (𝐶𝑖∧𝑀𝑖) (5) where:

• 𝐶𝑖 is a domain-specific condition, • 𝑀𝑖 is the model's prediction, • 𝑉 represents logical 𝑂𝑅, ensuring that either a rule-based condition or the deep learning model can trigger a final diagnosis. This combination was particularly effective in cases with low contrast or ambiguous lesion boundaries, where rules compensate for model uncertainty. C. Techniques - Model-Agnostic Explainability To enhance interpretability, SHAP values assign importance to each feature in determining the model's decision. The Shapley value for a feature 𝑥𝑖 is computed as:

|𝑆|!(𝑛−|𝑆|−1)!

𝑛! (𝑓(𝑆∪{𝑖}) −𝑓(𝑆))

```math
𝜙𝑖= ∑
 
𝑆⊆{1,…,𝑛}∖{𝑖}
```

(6) where:

• 𝑆 represents a subset of features, • ⁡𝑓(𝑆) is the model output when using subset 𝑆, • 𝑛 is the total number of features, • 𝜙𝑖 quantifies feature 𝑥𝑖 's contribution to the final prediction.

In our use case, SHAP was applied to highlight critical voxels in PET scan tumor classification. Radiologists confirmed that high-weighted regions coincided with metabolically active tumor zones, validating model reasoning. LIME approximates model predictions by perturbing input samples and generating locally weighted surrogate models: 𝑓ˆ(𝑥) = arg⁡ min

```math
𝑔∈𝐺 ∑
 
𝑚
𝑖=1 𝜋𝑥(𝑧𝑖)[𝑓(𝑧𝑖) −𝑔(𝑧𝑖)]2 + Ω(𝑔)
```

(7) where:

• 𝑓ˆ(𝑥) is the interpretable approximation, • 𝜋𝑥(𝑧𝑖) is the weight function assigning proximity-based weights, • 𝑔(𝑧𝑖) represents the simpler surrogate model,

• Ω(𝑔) penalizes model complexity.

For example, in lung CT classification, LIME explanations showed that nodule density and edge spiculation were key determinants. These explanations were rated useful by 4 out of 5 radiologists involved in the validation study.

These methods visualize which regions of an image most strongly influence Al predictions, ensuring clinicians can validate the decision-making process.

D. Hybrid Model Fusion

A multi-stage decision fusion strategy is implemented to optimally integrate deep learning, expert rules, and explainability outputs.

Fusion of Predictions

Let 𝑃𝑑 be the deep learning prediction and 𝑃𝑟 the rulebased output. The final decision 𝐷𝑓 is derived as:

```math
𝐷𝑓= 𝑤1𝑃𝑑+ 𝑤2𝑃𝑟⁡⁡⁡⁡⁡⁡⁡⁡(8)
```

where w₁ and w₂ were dynamically tuned using grid search over the validation set to balance accuracy (from CNN) and interpretability (from rules). The final weights w₁ = 0.7 and w₂ = 0.3 yielded the best F1-score without compromising clinical transparency.

Ensemble Optimization

To further refine predictions, a weighted ensemble method aggregates multiple classifiers:

```math
𝑃𝑓= ∑
 
𝑘
𝑖=1 𝛼𝑖𝑃𝑖        (9)
```

where:

• 𝑃𝑖 represents the probability output of the 𝑖th classifier,

• 𝛼𝑖 is the corresponding weight.

<!-- page 4 -->

This layered ensemble approach enables flexibility in accommodating domain-specific rules and learned patterns, improving robustness while ensuring alignment with medical standards.

V. EXPERIMENTAL SETUP AND RESULTS To guarantee the validity of the designed hybrid AI model, we trained it with publicly accessible medical imaging datasets across MRI, CT, and PET scan diagnostic applications. Before training, standard preprocessing techniques were implemented to improve both data quality and uniformity. The model’s effectiveness was measured using multiple performance metrics to evaluate both its predictive accuracy and interpretability for real-world clinical applications. A. Datasets We employed three primary datasets:

• MRI Modality: The Brain Tumor Segmentation (BraTS) dataset from the MICCAI Challenge and Medical Segmentation Decathlon was used for segmentation and classification of brain tumour images. • CT Modality:

o The LIDC-IDRI dataset provided annotated lung CT scans, including nodule malignancy ratings. o The COVID-19 Radiology CT dataset (from Kaggle) included CT scans labeled for COVID-positive and negative patients. • PET Modality: • The Alzheimer’s Disease Neuroimaging Initiative (ADNI) PET dataset was used for Alzheimer’s and Mild Cognitive Impairment classification.

o The TCIA Head and Neck FDGPET/CT dataset enabled analysis of metabolic activity in cancer patients. o Class distributions for all datasets were balanced using stratified sampling to mitigate bias. Further, demographic variation (e.g., age, gender) was recorded where available to evaluate representativeness. Preprocessing Techniques All imaging data were preprocessed by the following steps:

| Metric | Training | Validation |
|---|---|---|
| Accuracy (%) | 94.2 | 92.5 |
| Sensitivity (%) | 93.5 | 91.7 |
| Specificity (%) | 94.8 | 93.2 |
| F1-Score (%) | 93.9 | 92 |
| AUC | 0.95 | 0.93 |

 Resolution Standardization: The images were

resized to 224×224 pixels for CNN-based models and 384×384 for transformer architectures. These preprocessing techniques provided enhanced generalization and robustness in diverse clinical environments.

**Fig. 2: Sample images from Datasets**

A. Evaluation Metrics The model was tested on:

 Accuracy: Proportion of well-classified samples.  Sensitivity (Recall): Rate of true positives among

diseased cases.  Specificity: Rate of true negatives among healthy

cases.

 F1-Score: Harmonic mean between precision and

recall.  Area Under the Curve (AUC): From ROC

curves.  Explainability Score: Averaged from three

clinicians on SHAP and LIME visualizations using a 5-point Likert scale.

VI.RESULTS AND DISCUSSION The hybrid AI model was experimented with various imaging datasets like MRI, CT, and PET scans to measure its diagnostic accuracy, interpretability, and robustness. Comparison with the state-of-the-art existing deep learning models was carried out to highlight performance and reliability enhancement. Experimental results like performance metrics (Table 1), ROC curve (Fig. 3), confusion matrix (Fig. 4), and precision-recall curve (Fig. 5) provide a hint about the efficacy of the model for realworld clinical applications.

**TABLE I: PERFORMANCE METRICS Metric Training Validation**

<!-- page 5 -->

| Study | Accuracy (%) | Sensitivity (%) | Specificity (%) | F1- Score (%) |
|---|---|---|---|---|
| Proposed Hybrid AI Model | 94.2 | 93.5 | 94.8 | 93.9 |
| Zhou et al. (2022) | 90.4 | 89.1 | 91.3 | 89.9 |
| Ahmadian & Reza- Alikhani (2021) | 88.9 | 87.3 | 89.7 | 88.1 |
| Qiu et al. (2022) | 91.2 | 90.5 | 92.1 | 91 |
| Wang et al. (2023) | 92.5 | 91.7 | 93.2 | 92 |
| Li et al. (2022) | 89.8 | 88.2 | 90.4 | 89.1 |

**Fig. 4: Confusion Matrix**

**Fig. 5: precision Recall curve**

Performance Evaluation of the Proposed Model The classification performance of the model was compared using standard measures like accuracy, sensitivity, specificity, and F1-score. Results, presented in Table 1, suggest that the hybrid model performed with 94.2% accuracy in training and 92.5% in validation, outperforming traditional deep learning approaches. Sensitivity and specificity were 93.5% and 94.8% (training) and 91.7% and 93.2% (validation), which reflect its capability of classifying diseased and healthy cases with a good accuracy. The high F1-score of 93.9% (training) and 92.0% (validation) ensures that the model possesses high precision-recall ratio. Comparative Analysis with Existing Models A detailed comparison of the proposed hybrid model with existing literature is presented in Table 2. The comparison indicates that our approach is superior to models such as those of Zhou et al. (90.4% accuracy), Ahmadian & RezaAlikhani (88.9% accuracy), and Wang et al. (92.5% accuracy). The integration of rule-based expert systems and explainability techniques (SHAP and LIME) provides higher interpretability without sacrificing high classification performance. This validates that our model

is precise and trustworthy, overcoming the limitation of black-box AI systems in medical imaging.

**TABLE II: COMPARATIVE PERFORMANCE ANALYSIS Study Accuracy (%)**

**Fig. 6: Accuracy curve of proposed model**

**Fig. 7: loss curve of proposed model Explainability and Clinical Interpretability SHAP and LIME outputs were visually validated by three radiologists, with an average interpretability rating increase of 21% over baseline CNNs. Fig. 5 and Fig. 6 illustrate example SHAP overlays and LIME perturbations, respectively. Training Convergence**

<!-- page 6 -->

Fig. 6 and Fig. 7 demonstrate learning curves. After 50 epochs, the model reached:

• Training loss: Reduced from 1.5 → 0.1 • Validation loss: Reduced from 1.6 → 0.15 • No overfitting observed Real-Time Performance Inference latency averaged 118 ms per image, with average CPU usage below 70% on a standard AWS EC2 (g4dn.xlarge) instance. These results support deployment feasibility in real-time hospital environments.

VII. CONCLUSION This study presents a hybrid AI framework that integrates deep learning, rule-based expert systems, and modelagnostic interpretability techniques (SHAP and LIME) to enhance diagnostic accuracy and explainability across MRI, CT, and PET modalities. By addressing the blackbox nature of conventional deep learning models, the framework improves transparency, clinician trust, and suitability for real-world deployment. Experimental evaluation demonstrated strong performance, achieving 94.2% training accuracy and 92.5% validation accuracy, surpassing several state-ofthe-art approaches. The high AUC value (0.96) and favorable precision-recall analysis further confirm the robustness of the proposed framework. Importantly, the integration of SHAP and LIME improved explainability ratings by 21%, showing that clinicians could better understand and validate AI-driven outputs. The model’s multi-stage decision fusion strategy, combining transformer-based feature extraction with rulebased logic, contributed significantly to diagnostic reliability. Nevertheless, the current inference latency of 118 ms per image and moderate computational demands indicate that additional optimization is required for deployment in resource-limited clinical environments. Future enhancements will focus on:

• Reducing inference latency through model pruning and compression, • Integrating with electronic health records (EHRs) for seamless workflow adoption, and • Validating performance across diverse demographic and institutional datasets to ensure fairness and generalizability. By uniting high diagnostic performance with interpretable reasoning, the proposed hybrid AI framework establishes a reliable and scalable foundation for next-generation diagnostic decision support. Its ability to balance accuracy, interpretability, and efficiency positions it as a promising tool for fostering greater trust and adoption of AI in healthcare.

## References

[1] Zhou, G. -Q., et al. (2021). Learn fine-grained adaptive loss for multiple anatomical landmark detection in medical images. IEEE Journal of Biomedical and Health Informatics, 25(10), 3854-3864. https://doi.org/10.1109/JBHI.2021.3080703

[2] Chen, Z., et al. (2022). High temporal resolution total-body dynamic PET imaging based on pixel-level time-activity curve correction. IEEE Transactions on Biomedical Engineering, 69(12), 3689-3702. https://doi.org/10.1109/TBME.2022.3176097

[3] Ahmadian, K., & Reza-Alikhani, H. -R. (2021). Self- organized maps and high-frequency image detail for MRI image enhancement. IEEE Access, 9, 145662-145682. https://doi.org/10.1109/ACCESS.2021.3123119

[4] Qiu, Z., et al. (2024). Rethinking dual-stream super- resolution semantic learning in medical image segmentation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 46(1), 451-464. https://doi.org/10.1109/TPAMI.2023.3322735

[5] Ahlborg, M., et al. (2022). First dedicated balloon catheter for magnetic particle imaging. IEEE Transactions on Medical Imaging, 41(11), 3301-3308. https://doi.org/10.1109/TMI.2022.3183948

[6] Dong, H., et al. (2023). SWSSL: Sliding window-based self- supervised learning for anomaly detection in high-resolution images. IEEE Transactions on Medical Imaging, 42(12), 3860-3870. https://doi.org/10.1109/TMI.2023.3314318

[7] Wang, N., et al. (2023). MISSU: 3D medical image segmentation via self-distilling TransUNet. IEEE Transactions on Medical Imaging, 42(9), 2740-2750. https://doi.org/10.1109/TMI.2023.3264433

[8] Li, A. -C., et al. (2021). Patch-based U-Net model for isotropic quantitative differential phase contrast imaging. IEEE Transactions on Medical Imaging, 40(11), 3229-3237. https://doi.org/10.1109/TMI.2021.3091207

[9] Feng, L., et al. (2024). MLU-Net: A multi-level lightweight U-Net for medical image segmentation integrating frequency representation and MLP-based methods. IEEE Access, 12, 20734-20751. https://doi.org/10.1109/ACCESS.2024.3360889

[10] Qiao, S., et al. (2024). HCMMNet: Hierarchical Conv-MLP- Mixed Network for medical image segmentation in metaverse for consumer health. IEEE Transactions on Consumer Electronics, 70(1), 2078-2089. https://doi.org/10.1109/TCE.2023.3337234

[11] Zhuang, Y., et al. (2022). WSAN: An effective model of weakly supervised similarity analysis network for the lung CT images. IEEE Access, 10, 53777-53787. https://doi.org/10.1109/ACCESS.2022.3174099

[12] Cai, C., et al. (2023). Bayesian adaptive beamformer for robust electromagnetic brain imaging of correlated sources in high spatial resolution. IEEE Transactions on Medical Imaging, 42(9), 2502-2512. https://doi.org/10.1109/TMI.2023.3256963

[13] Yang, Y., et al. (2024). A novel transformer model with multiple instance learning for diabetic retinopathy classification. IEEE Access, 12, 6768-6776. https://doi.org/10.1109/ACCESS.2024.3351473

[14] Lang, Y., et al. (2022). Localization of craniomaxillofacial landmarks on CBCT images using 3D Mask R-CNN and local dependency learning. IEEE Transactions on Medical Imaging, 41(10), 2856-2866. https://doi.org/10.1109/TMI.2022.3174513
