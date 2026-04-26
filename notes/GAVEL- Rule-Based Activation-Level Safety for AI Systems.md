# Literature Extraction: Rozenfeld, S., et al. (2026)  
## "GAVEL: Towards Rule-Based Safety through Activation Monitoring"

---

## Section 1 — Paper Identity

- **Title:** GAVEL: Towards Rule-Based Safety through Activation Monitoring  
- **Authors:** Shir Rozenfeld et al.  
- **Year:** 2026  
- **Venue:** International Conference on Learning Representations (ICLR 2026)  
- **DOI:** Not specified in extracted document *(verify official proceedings if needed)*  
- **Type:** Research paper (AI Safety, Large Language Models, Rule-Based Systems)  

---

## Section 2 — Core Contribution

### Problem Addressed

Existing AI safety methods primarily rely on:

- input/output filtering  
- dataset-based classification  

These approaches suffer from:

- **low precision** due to broad misuse categories :contentReference[oaicite:0]{index=0}  
- **limited flexibility**, requiring retraining for new policies :contentReference[oaicite:1]{index=1}  
- **lack of interpretability**, making decisions difficult to explain :contentReference[oaicite:2]{index=2}  

---

### Proposed Solution

The paper introduces:

> **GAVEL — a rule-based safety framework operating at the activation level of AI models**

Instead of analysing outputs, the system:

- monitors **internal model activations**  
- decomposes them into interpretable units  
- applies **logical rules** to detect unsafe behaviour  

---

### Main Contributions (as presented in the paper)

- **Cognitive Elements (CEs):**  
  Interpretable units representing internal model behaviour  

- **Rule-based safety mechanism:**  
  Logical rules applied over combinations of CEs  

- **Activation-level monitoring pipeline:**  
  Safety enforced during model inference  

- **Decoupled safety framework:**  
  Safety rules are independent of model training  

---

### What is Novel

- Moves safety from:
  - output-level detection  
→ to  
  - **activation-level reasoning with explicit rules**

---

## Section 3 — Relevance to My Research

| Theme | Relevance | Notes |
|------|--------|------|
| Deterministic safety layer | Yes | Rule-based safety constraints |
| AI advisory role | Partial | Focus on safety, not advisory |
| AI participation control | No | AI always active |
| Admissible action space | Partial | Rules restrict behaviour implicitly |
| State-based governance | No | No safety state model |
| Formal guarantees | No | No formal proof |
| Low-resource environment | No | Not discussed |
| Hybrid AI architecture | Yes | Rule layer + neural model |

---

### Gate Decision

- Yes: 2  
- Partial: 2  

➡️ **REDUCED EXTRACTION**

---

## Section 12 — Key Concepts and Definitions

- **Cognitive Elements (CEs)**  
  Interpretable activation-level representations of model behaviour  

- **Activation-level monitoring**  
  Observing internal neural states during inference  

- **Rule-based safety constraints**  
  Logical rules applied over CEs to detect unsafe patterns  

- **Decoupled safety enforcement**  
  Safety policies are independent from model training  

---

## Section 13 — Limitations and Unsolved Problems

- No system-level decision architecture  
- No control over:
  - when AI should act  
  - when AI should be disabled  

- No explicit admissible action space  
- Reactive approach:
  - detects behaviour after it emerges  

- No formal safety guarantees  

---

## Section 16 — Relation to My Research and Positioning

### Alignment

This paper supports:

- the use of **rule-based mechanisms for AI safety**  
- separation between:
  - AI capability  
  - safety constraints  

- trend toward:
  - structured and interpretable safety control  

---

### Gap

The system:

- operates at **activation level**, not system level  
- does not define:
  - AI participation control  
  - state-based governance  
  - constrained decision space  

---

### Positioning

GAVEL demonstrates that rule-based mechanisms can constrain AI behaviour by monitoring internal activations and applying logical rules. However, it focuses on reactive safety enforcement within the model rather than governing decision-making at the system level. This research extends this idea by introducing a governance architecture that controls both when AI participates and what it is permitted to recommend under varying risk conditions.

---

## Section 17 — Overall Relevance Score

⭐⭐⭐☆☆ (3/5)

### Justification

- Strong support for rule-based AI safety  
- Relevant to constraint-based control concepts  
- Limited direct contribution to decision architecture and governance  

---