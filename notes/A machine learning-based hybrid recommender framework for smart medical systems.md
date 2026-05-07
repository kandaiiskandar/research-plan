# A machine learning-based hybrid recommender framework for smart medical systems

---

## 📄 Paper Information

- **Authors:** Jianhua Wei, Honglin Yan, Xiaoli Shao, Lili Zhao, Lin Han, Peng Yan, Shengyu Wang  
- **Year:** 2024  
- **Journal:** PeerJ Computer Science  
- **DOI:** https://doi.org/10.7717/peerj-cs.1880  
- **Published Date:** 20 February 2024  
- **Submitted:** 7 December 2023  
- **Accepted:** 24 January 2024  
- **Article Type:** Journal Article  
- **License:** Creative Commons CC-BY 4.0  
- **Pages:** 24  

---

## Abstract

This article presents a hybrid recommender framework for smart medical systems by introducing two methods to improve service level evaluations and doctor recommendations for patients.  

The first method uses big data techniques and deep learning algorithms to develop a registration review system in medical institutions. This system outperforms conventional evaluation methods, thus achieving higher accuracy.  

The second method implements the term frequency and inverse document frequency (TF-IDF) algorithm to construct a model based on the patient’s symptom vector space, incorporating score weighting, modified cosine similarity, and K-means clustering.  

Then, the alternating least squares (ALS) matrix decomposition and user collaborative filtering algorithm are applied to calculate patients’ predicted scores for doctors and recommend top-performing doctors.  

Experimental results show significant improvements in metrics called precision and recall rates compared to conventional methods.

---

## Keywords

Medical registration · Medical evaluation · Big data · Deep learning algorithms · Doctor recommendations  

---

## 1. Introduction

Assessing the service level of medical institutions is vital to enhancing patient care and promoting quality improvements.  

The conventional approach involves collecting various types of data from each department and applying predetermined processing methods to generate evaluation labels. However, this process inaccurately reflects the relationships between indicators across departments.  

Recent years have witnessed the rising popularity of big data, deep learning, and neural networks, which provide remarkable performance improvements across various domains.  

However, current systems:
- rely heavily on manual input  
- lack effective triage and recommendation mechanisms  
- struggle with scalability and cold-start problems  

---

## 2. The Evaluation System of Big Data-Based Registration

### Composition and Workflow

The system comprises several modules:

1. **Index Data Collection Module**
   - Collects multiple index data for each department  

2. **Context Encoder**
   - Embedding layer  
   - Converts index data into semantic feature vectors  

3. **Multi-Scale Feature Extraction Module**
   - Extracts features at different scales using CNN  

4. **Eigenvalue Correction Module**
   - Corrects feature vectors using maximum value-based adjustment  

5. **Inter-Department Association Encoding**
   - Builds 2D feature matrix  
   - Uses CNN for feature extraction  

6. **Classification Module**
   - Produces service-level labels  

---

## Mathematical Formulation

Convolution operation:

Z = f(Σ w * x + b)

Feature correction:

V' = V * e^(-sin(2π * V / vmax))

CNN transformation:

F_out = CNN(F_in)

---

## 3. Hybrid Recommendation Algorithm-Based Intelligent Triage System

### Symptom Vector Space Model (TF-IDF)

TF:
TFi,j = ni,j / n*,j  

IDF:
IDFi = log(N / Di + 1)  

Vector representation:
v(j) = (Wj1, Wj2, ..., Wjn)

---

### Score-Weighted TF-IDF

TFi = Σ(ni,k * rk) / Σ(n*,k * rk)

---

### Department Representation

v(d) = (Wd1, Wd2, ..., Wdn)

---

### Similarity Calculation

Modified cosine similarity used for:
- patient ↔ department matching  

---

## Clustering (K-Means + Trust)

Trust formula:

Tu,v = √(I(u) ∪ I(v)) / (I(u) ∩ I(v))

Distance:

Du,v = Tu,v * √Σ(Wu,i − Wv,i)^2  

---

## Recommendation Model

### ALS Matrix Decomposition

R ≈ P × Q  

### Prediction Formula

r_ai = r̄_i + Σ(sim(a,j) * (r_ji − r̄_j)) / Σ(sim(a,j))

---

## 4. Results

### Department Triage

- Accuracy: 96.57%  
- Recall improved by ~6.93%  

---

### Recommendation Performance

- Precision ↑ 2.25%  
- Recall ↑ 3.25%  

---

### Clustering Impact

- Reduced computation complexity  
- Improved efficiency  

---

## 5. Discussion

### Advantages
1. Enhanced accuracy  
2. Efficient triage  
3. Personalized recommendations  
4. Scalability  

### Disadvantages
1. Data dependency  
2. Privacy concerns  
3. System complexity  

---

## 6. Conclusion

This study presents methods for:
- evaluating medical institutions  
- improving department triage  
- enhancing doctor recommendations  

The system integrates:
- big data analysis  
- deep learning  
- collaborative filtering  

Future work includes:
- integrating more data sources  
- applying NLP techniques  
- improving real-time recommendations  

---

## Additional Information

- No funding declared  
- No competing interests  
- Data and code available in supplemental files  

---

## References

(References preserved as in original paper)