# A hybrid recommendation system using association rule mining, i-ALS algorithm, and SVD++ approach: A case study of a B2B company

---

## 📄 Paper Information

- **Authors:** Thamer Saraei, Maha Benali, Jean-Marc Frayret  
- **Year:** 2025  
- **Journal:** Intelligent Systems with Applications  
- **Publisher:** Elsevier  
- **DOI:** https://doi.org/10.1016/j.iswa.2025.200477  
- **Available online:** 9 January 2025  
- **License:** CC BY-NC-ND 4.0  
- **Type:** Journal Article  

---

## Abstract

In the field of recommendation systems, collaborative filtering is a widely used technique. It provides recommendations to active users based on the ratings provided by similar users. However, this method may reduce the accuracy of user preference predictions and lead to lower-quality recommendations in cases of high data sparsity. This issue is often observed in the Business-to-Business (B2B) context, where user-generated reviews are often sparse.  

To overcome this challenge, we present a novel hybrid approach that explores product taxonomies and association rule mining combined with an advanced method for initialization. Our approach first involves generating a new explicit taxonomy based solely on textual product descriptions and extending the user–product matrix using association rule mining results. Second, complementary items are added to the user–item matrix based on users’ purchasing behaviors, as emphasized by the extracted association rules. Finally, we use the implicit Alternating Least Squares (i-ALS) algorithm and initialize the latent factor matrices with values obtained through the singular value decomposition approach (BLS-SVD++).  

This hybrid approach is tested and compared with conventional approaches, considering a real-world case study of a distributor located in Quebec. The results obtained from feedback implicitly inferred from sales data demonstrated improved RS performance compared to conventional approaches.

---

## Keywords

Recommendation System · Collaborative Filtering · Association Rule Mining · Implicit Alternating Least Squares · Singular Value Decomposition · Business-To-Business  

---

## 1. Introduction

E-commerce sites offer customers a wide range of products, making it challenging for users to select the most suitable ones. Recommendation Systems (RSs) assist users by filtering items and displaying only those likely to be relevant to them.  

RSs can employ Content-Based Filtering (CBF) or Collaborative Filtering (CF), depending on the type of data used to generate recommendations.  

However, CF faces challenges such as:
- sparsity problem  
- synonymy problem  

In the B2B context:
- data is sparse  
- items have multiple names and descriptions  

---

## 2. Background and Related Works

### 2.1 Matrix Factorization

Matrix factorization decomposes the user–item matrix into latent factors representing hidden relationships.

The i-ALS algorithm alternately updates:
- user matrix  
- item matrix  

---

### 2.2 Product Taxonomy

Taxonomies organize items hierarchically to improve recommendation accuracy.

Examples include:
- hierarchical taxonomies  
- Bayesian models  
- latent factor models  

---

### 2.3 Association Rule Mining (ARM)

Association rules identify relationships between items:

A → B  

Meaning:
- users interested in A are likely interested in B  

---

### 2.4 Initialization of Factor Matrices

Initialization impacts:
- convergence speed  
- model accuracy  

SVD and BLS-SVD++ provide improved initialization compared to random values.

---

## 3. Methodology and Implementation

The methodology addresses:
- synonymy problem  
- sparsity problem  

### Step 1: Creation of New Item Taxonomy

- Items grouped by similarity in textual descriptions  
- Uses NLP techniques:
  - tokenization  
  - stop-word removal  
  - clustering  

Similarity metric:

WO(D, C) = |W(D) ∩ W(C)| / |W(D) ∪ W(C)|  

---

### Step 2: Enhancement of User–Item Matrix

Association rules extracted using Apriori algorithm:

A → B  

Score assignment:

n_uiB = n_c × n_uiA  

Where:
- n_c = confidence  
- n_uiA = purchase frequency  

---

### Step 3: Initialization of i-ALS

- Uses BLS-SVD++ initialization  
- Improves latent factor quality  

---

### Overall Methodology

(From Fig. 1, page 4)

1. Raw data → preprocessing  
2. Create taxonomy  
3. Apply association rules  
4. Enhance user–item matrix  
5. Decompose matrix (SVD++)  
6. Initialize i-ALS  
7. Generate Top-3 recommendations  

---

## 4. Experiments

### Dataset

- 5000+ customers  
- 15,000+ items  
- ~10 million transactions  
- Time period: 2007–2020  
- Sparsity: 0.43%  

---

### Evaluation Metric

Precision:

P = |RL ∩ SL| / |RL|  

Precision@k:

P@k = (1 / |U|) × Σ SL(u)@k / k  

---

### Baselines

- Random  
- Most Popular  
- BPR  
- NeuMF  

---

## 5. Results

### Experiment 1

- ITEM_FAMILY taxonomy performs best  
- Improves accuracy by 23.25%  

---

### Experiment 2

- ARM improves performance  
- Low confidence (0.35) gives best result  

---

### Experiment 3

- BLS-SVD++ initialization improves accuracy by 7.54%  
- Combined method improves by 12.57%  

---

### Final Results

| Approach | P@3 |
|---------|-----|
| Proposed | 0.358 |
| BPR | 0.316 |
| NeuMF | 0.314 |
| Most Popular | 0.134 |
| Random | 0.09 |

---

## 6. Conclusion

A hybrid approach combining:
- ARM  
- i-ALS  
- BLS-SVD++  

was proposed to address:
- sparsity  
- synonymy  

The approach:
- improves recommendation accuracy  
- outperforms baseline methods  

Future work includes:
- scalability  
- online evaluation  
- integration of optimization algorithms  

---

## References

(References preserved as in original paper)