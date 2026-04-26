# Literature Extraction: (Authors to be verified) (2024)  
## "Generating Context-Aware Contrastive Explanations in Rule-Based Systems"

---

## Section 1 — Paper Identity

- **Title:** Generating Context-Aware Contrastive Explanations in Rule-based Systems  
- **Authors:** Lars Herbold, Mersedeh Sadeghi, Andreas Vogelsang  
- **Year:** 2024  
- **Venue:** Proceedings of the 2024 Workshop on Explainability Engineering  
- **Publisher:** Association for Computing Machinery (ACM)  
- **DOI:** https://doi.org/10.1145/3648505.3648507  
- **ISBN:** 979-8-4007-0596-0  
- **Pages:** 8–14  
- **Location:** Lisbon, Portugal  
- **Keywords:** explainability, software engineering, smart environments  
- **Type:** Conference paper (Explainable AI / rule-based systems)  


---

## Section 2 — Core Contribution

### Problem Addressed

Traditional explanation systems in AI:

- Explain **why a decision occurred**
- Do not explain:
  - why this decision occurred **instead of another possible outcome**

This leads to:

- limited user understanding  
- reduced trust in automated systems  
- difficulty in interpreting system behaviour  

---

### Proposed Solution

The paper introduces:

> **Context-aware contrastive explanations** in rule-based systems

This shifts explanation from:

- absolute explanation  
→ to  
- **relative explanation between outcomes**

---

### Main Contributions (as presented in the paper)

- **Contrastive explanation framework**
  - explains outcome A relative to outcome B  

- **Context-aware expectation modelling**
  - identifies what the user likely expected  

- **Rule-based explanation generation**
  - explanations derived directly from triggered rules  

- **Ranking mechanism (TOPSIS)**
  - selects the most relevant alternative explanation  

---

### What is Novel

- Introduces **contrastive reasoning** into rule-based explanation  
- Moves beyond:
  - “why this happened”  
→ to  
  - **“why this instead of that”**

---

## Section 3 — Relevance to My Research

| Theme | Relevance | Notes |
|------|--------|------|
| Deterministic safety layer | Yes | Based on rule-based systems |
| AI advisory role | No | No AI advisory component |
| AI participation control | No | Not addressed |
| Admissible action space | Partial | Actions defined by rules |
| State-based governance | No | No state model |
| Formal guarantees | No | No formal model |
| Low-resource environment | No | Not discussed |
| Hybrid AI architecture | No | Pure rule-based |

---

### Gate Decision

- Yes: 1  
- Partial: 1  

➡️ **REDUCED EXTRACTION**

---

## Section 12 — Key Concepts and Definitions

- **Contrastive explanation**  
  Explanation that answers:
  > “Why outcome A instead of outcome B?”

- **Rule-based system**  
  Decision-making system based on:
  - IF–THEN rules  

- **Rule firing**  
  Process where rules are triggered based on input conditions  

- **Context-aware reasoning**  
  Explanation depends on:
  - user expectation  
  - system context  

- **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)**  
  A multi-criteria ranking method used to select the most relevant explanation  

---

## Section 13 — Limitations and Unsolved Problems

- Focuses only on **explanation**, not decision-making  
- No mechanism to:
  - control system behaviour  
  - restrict actions  
  - enforce safety  

- No integration with AI or probabilistic models  
- No modelling of risk or uncertainty  
- No governance architecture  

---

## Section 16 — Relation to My Research and Positioning

### Alignment

This paper supports:

- importance of **explainability in rule-based systems**  
- need for **transparent and traceable decisions**  
- role of explanation in:
  - user trust  
  - human-AI interaction  

---

### Gap

The system:

- operates **after decisions are made**  
- does not:
  - govern decisions  
  - restrict action space  
  - control AI behaviour  

---

### Positioning

The paper demonstrates that rule-based systems can generate transparent and context-aware explanations, improving user understanding and trust. However, it focuses on post-hoc explanation rather than decision governance. This research extends the role of rule-based systems from explaining decisions to **controlling decisions**, by introducing a governance architecture that constrains AI participation and recommendation space before decisions are made.

---

## Section 17 — Overall Relevance Score

⭐⭐⭐☆☆ (3/5)

### Justification

- Strong support for explainability argument  
- Useful for human-AI trust discussion  
- Limited direct contribution to governance or safety architecture  

---