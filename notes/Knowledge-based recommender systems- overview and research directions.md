# Knowledge-based recommender systems: overview and research directions

---

## Paper Information

- **Authors:** Mathias Uta, Alexander Felfernig, Viet-Man Le, Thi Ngoc Trang Tran, Damian Garber, Sebastian Lubos, Tamim Burgstaller  
- **Year:** 2024  
- **Journal:** Frontiers in Big Data  
- **DOI:** https://doi.org/10.3389/fdata.2024.1304439  
- **Published:** 26 February 2024  
- **Type:** Review Article  

---

## Abstract

Recommender systems are decision support systems that help users to identify items of relevance from a potentially large set of alternatives. In contrast to the mainstream recommendation approaches of collaborative filtering and content-based filtering, knowledge-based recommenders exploit semantic user preference knowledge, item knowledge, and recommendation knowledge, to identify user-relevant items which is of specific relevance when dealing with complex and high-involvement items. Such recommenders are primarily applied in scenarios where users specify (and revise) their preferences, and related recommendations are determined on the basis of constraints or attribute-level similarity metrics. In this article, we provide an overview of the existing state-of-the-art in knowledge-based recommender systems. Different related recommendation techniques are explained on the basis of a working example from the domain of survey software services. On the basis of our analysis, we outline different directions for future research.

---

## Keywords

recommender systems, semantic recommender systems, knowledge-based recommender systems, case-based recommendation, constraint-based recommendation, critiquing-based recommendation, constraint solving, model-based diagnosis

---

## 1. Introduction

Recommender systems support users in identifying relevant items from a large set of alternatives and thus help to reduce the complexity of decisions and increase user satisfaction and sales.

Collaborative filtering is based on determining recommendations on the basis of the preferences of nearest neighbors. A major advantage is an easy setup. A disadvantage is the cold-start problem.

Content-based filtering recommends items similar to those consumed in the past. It requires item knowledge and may lack diversity.

Knowledge-based recommender systems are based on collecting user preferences within a dialog and recommending items using constraints or similarity metrics. These systems are useful in complex and high-involvement domains.

---

## 1.1 Further Recommendation Approaches

Hybrid recommender systems combine different recommendation approaches.

Group recommender systems determine recommendations for groups instead of individual users.

---

## 1.2 Article Contributions

- Overview of knowledge-based recommender systems  
- Explanation of techniques using a working example  
- Identification of research directions  

---

## 2. Methodology

The literature analysis was conducted using search, review, and discussion activities.

Queries were performed on platforms including Google Scholar, ResearchGate, ScienceDirect, SpringerLink, and Elsevier.

A total of 97 publications were identified as relevant.

---

## 3. Basic Approaches and Applications

Knowledge-based recommender systems operate on different knowledge representations.

### 3.1 Recommendation Knowledge Representations

#### Table-based representations
Items are explicitly defined in a product table.

#### Constraint-based representations
Items are defined using constraints instead of enumeration.

---

### 3.2 Case-Based Recommendation

Case-based recommendation identifies items that support user preferences.

#### Techniques include:
- Interest confidence value  
- Attribute-level similarity  
- Refine, relax, compromise  
- Critiquing  

Critiquing allows users to iteratively refine recommendations.

---

### 3.3 Constraint-Based Recommendation

Constraint-based recommendation defines a task as a constraint satisfaction problem (CSP).

A recommendation must satisfy:
- domain constraints  
- user requirements  

Ranking can be based on:
- feature support  
- utility functions  

Inconsistent requirements can be resolved using:
- conflict sets  
- diagnoses  

---

## 4. Recent Advances

### 4.1 Recommending Preference Settings
Systems can suggest attribute values based on similar users.

### 4.2 Handling No-Solution Situations
Conflict detection and diagnosis help resolve inconsistencies.

### 4.3 Reconfiguration
Systems support adapting already selected items.

### 4.4 Group Recommendation
Recommendations can be generated for groups using aggregation methods.

### 4.5 Further Aspects
- Hybrid recommendation  
- Search optimisation  
- Knowledge acquisition  
- Conversational systems  
- Explanations  

---

## 5. Research Directions

- Integration with machine learning  
- Diagnosis performance optimisation  
- Cognitive aspects of preference elicitation  
- Evaluation metrics  
- Consequence-based explanations  
- Integration of large language models  
- Sustainability  

---

## 6. Conclusion

The article provides an overview of knowledge-based recommender systems, explains underlying techniques, and outlines future research directions.

---

## Reference

Uta, M., Felfernig, A., Le, V.-M., Tran, T. N. T., Garber, D., Lubos, S., & Burgstaller, T. (2024). Knowledge-based recommender systems: overview and research directions. Frontiers in Big Data, 7, 1304439.