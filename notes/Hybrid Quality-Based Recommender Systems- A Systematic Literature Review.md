# 📄 Paper Extraction

## 1. Basic Information

- **Title:** Hybrid Quality-Based Recommender Systems: A Systematic Literature Review  
- **Authors:** Bihi Sabiri, Amal Khtira, Bouchra El Asri, Maryem Rhanoui  
- **Year:** 2025  
- **Journal:** Journal of Imaging  
- **DOI:** https://doi.org/10.3390/jimaging11010012  
- **Type:** Systematic Literature Review  
- **Publisher:** MDPI  

---

## 2. Problem Addressed

Recommender systems face a visibility problem. Many available items are not discovered by users, while a small number dominate attention.  [oai_citation:0‡jimaging-11-00012-v2.pdf](sediment://file_000000008e007207bef4b0524ec46f40)  

Traditional recommendation approaches also struggle with:
- Data sparsity  
- Scalability in big data environments  
- Limited accuracy when using a single method  

The paper positions hybrid recommender systems as a response to these limitations.

---

## 3. Key Idea

The core idea is to combine multiple recommendation techniques into a **hybrid system** to improve performance.

These systems integrate:
- Collaborative filtering  
- Content-based methods  
- Knowledge-based approaches  

The goal is to improve:
- Accuracy  
- Robustness  
- Coverage of recommendations  

The paper reviews how hybrid models are designed and applied across domains.

---

## 4. Methodology

This study follows a **systematic literature review (SLR)** approach.

### Process:
1. Define research questions  
2. Construct search strings using keywords and synonyms  
3. Search databases (ACM, Scopus, Springer, Google Scholar, Web of Science)  
4. Apply filtering criteria (year, relevance, language)  
5. Analyse selected studies  
6. Synthesize findings  

The search uses Boolean logic such as:
- “AND” to combine concepts  
- “OR” to group synonyms  [oai_citation:1‡jimaging-11-00012-v2.pdf](sediment://file_000000008e007207bef4b0524ec46f40)  

The study also uses **ASReview**, an active learning tool, to support paper selection.  [oai_citation:2‡jimaging-11-00012-v2.pdf](sediment://file_000000008e007207bef4b0524ec46f40)  

---

## 5. Key Findings

### 5.1 Hybrid Approaches Improve Performance
Hybrid systems outperform single-method systems in:
- Recommendation accuracy  
- Handling sparse data  
- Managing large-scale datasets  

### 5.2 Multiple Hybrid Strategies Exist
Common hybridisation techniques include:
- Weighted hybrid  
- Switching hybrid  
- Cascade hybrid  
- Feature combination  

Each strategy addresses different limitations of standalone models.

### 5.3 Big Data Challenges
Hybrid systems must deal with:
- Volume (large datasets)  
- Velocity (real-time data)  
- Variety (heterogeneous data sources)  [oai_citation:3‡jimaging-11-00012-v2.pdf](sediment://file_000000008e007207bef4b0524ec46f40)  

### 5.4 Practical Impact
Recommender systems are widely adopted by major technology companies.  
They improve:
- User experience  
- Product visibility  
- Business performance  [oai_citation:4‡jimaging-11-00012-v2.pdf](sediment://file_000000008e007207bef4b0524ec46f40)  

---

## 6. Limitations Identified

Despite improvements, several issues remain:

- Increased system complexity  
- Higher computational cost  
- Integration challenges between methods  
- Lack of standard evaluation frameworks  

Most systems optimise performance but do not address **decision control or safety constraints**.

---

## 7. Research Gaps

The review highlights several gaps:

1. **Lack of unified hybrid design frameworks**  
   Many systems combine methods ad hoc without formal structure.

2. **Limited explainability**  
   Hybrid systems often act as black boxes.

3. **Weak handling of decision constraints**  
   Systems optimise recommendations but do not restrict unsafe or undesirable outputs.

4. **Insufficient focus on real-world constraints**  
   Few studies consider low-resource environments or operational risk.

---

## 8. Relevance to Your Research

This paper is directly relevant to hybrid AI design but reveals a critical gap.

### What it supports:
- Hybrid architectures improve decision quality  
- Combining methods is necessary in complex environments  

### What is missing:
- No concept of **deterministic safety control**  
- No formal separation between:
  - what AI *can recommend*  
  - what AI *is allowed to recommend*  

### Link to your work:

Your research extends this by introducing:

- **Layered governance architecture**
- **Deterministic safety gate (Layer 2)**
- **Restricted AI advisory space (Layer 3)**

This addresses a key limitation:
> Existing hybrid systems optimise recommendations but do not control them under risk.

---

## 9. Suggested Citation (APA)

Sabiri, B., Khtira, A., El Asri, B., & Rhanoui, M. (2025).  
Hybrid quality-based recommender systems: A systematic literature review.  
*Journal of Imaging, 11*(1), 12.  
https://doi.org/10.3390/jimaging11010012  

---

## 10. One-Line Positioning (for writing)

Hybrid recommender systems improve performance by combining multiple techniques, but they lack formal governance mechanisms to constrain decisions under risk, which motivates the need for a safety-gated hybrid architecture.

---