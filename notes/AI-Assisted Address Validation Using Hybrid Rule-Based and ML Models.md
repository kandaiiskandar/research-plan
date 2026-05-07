# Literature Extraction: Pappula, K. K., & Rusum, G. P. (2024)  
## "AI-Assisted Address Validation Using Hybrid Rule-Based and ML Models"

---

## Section 1 — Paper Identity

- **Title:** AI-Assisted Address Validation Using Hybrid Rule-Based and ML Models  
- **Authors:** K. K. Pappula, G. P. Rusum  
- **Year:** 2024  
- **Venue:** *International Journal of Artificial Intelligence, Data Science, and Machine Learning (IJAIDSML)*, Vol. 5, Issue 4  
- **DOI:** https://doi.org/10.63282/3050-9262.IJAIDSML-V5I4P110  
- **Type:** System design + empirical evaluation  

---

## Section 2 — Core Contribution

### Problem Addressed
Address validation systems face:
- **inconsistent input formats**
- **noise and missing fields**
- limitations of purely rule-based systems (rigidity)
- limitations of purely ML systems (lack of structure and interpretability)

---

### Proposed Solution
A **hybrid pipeline** that integrates:
- **rule-based preprocessing and validation**
- **machine learning classification for ambiguity resolution**

---

### Main Contributions (as presented in the paper)

- **Rule-based preprocessing layer:**  
  Handles normalization, parsing, and structured validation.

- **ML-based classification layer:**  
  Resolves ambiguous or incomplete address cases.

- **Hybrid integration:**  
  Combines outputs from both components using confidence scoring.

- **Performance improvement:**  
  Demonstrates higher accuracy compared to standalone approaches.

---

### What is Novel (from the paper context)

- Integration of deterministic rules with ML classification in a **structured pipeline**
- Demonstration that **hybrid systems outperform single-method approaches**

---

## Section 3 — Relevance to My Research

| Theme | Relevance | Notes |
|------|--------|------|
| Deterministic safety layer | Partial | Rules used for preprocessing |
| AI advisory role | Yes | ML handles uncertain cases |
| AI participation control | No | ML always active |
| Admissible action space | No | No bounded decision space |
| State-based governance | No | No safety states |
| Formal guarantees | No | No formal model |
| Low-resource environment | No | Not discussed |
| Hybrid AI architecture | Yes | Rule + ML integration |

---

### Gate Decision

- Yes: 2  
- Partial: 1  

➡️ **REDUCED EXTRACTION**

---

## Section 12 — Key Concepts and Definitions

- **Rule-based preprocessing:**  
  Deterministic transformation and validation using predefined logic.

- **Machine learning classification:**  
  Statistical model used to interpret ambiguous or incomplete data.

- **Hybrid system:**  
  Integration of rule-based and ML approaches to improve performance.

- **Confidence-based fusion:**  
  Mechanism to combine outputs from rule-based and ML components.

---

## Section 13 — Limitations and Unsolved Problems

- No governance mechanism for AI behaviour  
- No control over **when ML should be used**  
- No restriction on **what ML can output**  
- No safety-critical framing  
- Rules are used for **data cleaning**, not decision control  

---

## Section 16 — Relation to My Research and Positioning

### Alignment

This paper supports:
- the effectiveness of **hybrid architectures**
- the need to combine:
  - deterministic logic (structure)
  - probabilistic models (flexibility)

---

### Gap

The system:
- does not control AI participation  
- does not define an admissible action space  
- does not provide safety guarantees  
- treats rules as preprocessing rather than governance  

---

### Positioning

The paper demonstrates that hybrid rule-based and machine learning systems improve performance in structured tasks. However, it applies rule-based logic primarily for preprocessing rather than as a governance mechanism. In contrast, this research elevates rule-based systems to a control layer that constrains AI participation and recommendation scope under risk.

---

## Section 17 — Overall Relevance Score

⭐⭐⭐☆☆ (3/5)

### Justification

- Supports hybrid AI design principle  
- Shows deterministic + probabilistic integration  
- Limited relevance to safety governance and formal control  

---